import kivy
kivy.require('1.10.1')

import ctypes
user32 = ctypes.windll.user32
device_width = user32.GetSystemMetrics(0)
device_height = user32.GetSystemMetrics(1)

app_width = round(device_width*0.8)
app_height = round(device_height*0.8)
min_app_width = round(device_width*0.65)
min_app_height = round(device_height*0.8)

from kivy.config import Config
Config.set('kivy', 'desktop', '1')
Config.set('kivy', 'window_icon','img/turtlecoin_icon_color_16.png')
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', app_width)
Config.set('graphics', 'height', app_height)
Config.set('graphics', 'minimum_width', min_app_width)
Config.set('graphics', 'minimum_height', min_app_height)

from kivy.core.window import Window
Window.clearcolor = (33/255,38/255,33/255,1) #set window background color

from kivy.app import App

from kivy.clock import Clock
from datetime import datetime
from kivy.properties import StringProperty
from gui_classes import ScreenManagement, StartScreen, MainScreen, CenteredTextInput,\
 DaemonScreen, SearchScreen, LoadingPopup, ErrorPopUp, TxPoolData, RecentBlockData, BigLabel, SmallLabel

from kivy.uix.label import Label

import threading
import time
import logging
import data_constructor
from functools import partial
from queue import Queue, Empty
from explorer import Turtle_Explorer


#daemon_infoq = Queue(maxsize = 0)
tx_search_q = Queue(maxsize = 1)
blk_search_q = Queue(maxsize = 1)
daemon_stats_q = Queue(maxsize = 1)
recent_blk_q = Queue(maxsize = 1)
tx_pool_q = Queue(maxsize = 1)

TRTLdaemon = Turtle_Explorer()

app_logger = logging.getLogger('turtle_local_explorer_log.app')

'''
def update_daemon_infoq():
    while True:
        daemon_infoq.put(TRTLdaemon.daemon_q.get())
'''
def update_explore_q():
    while True:
        time.sleep(0.5)
        daemon_stats_q.put(TRTLdaemon.status)
        if TRTLdaemon.blocks==None or TRTLdaemon.txPool==None:
            pass
        else:
            recent_blk_q.put(TRTLdaemon.blocks) 
            tx_pool_q.put(TRTLdaemon.txPool)

class Turtle_Local_Explorer(App):
    """
    This is the turtle local explorer gui app.
    This class contains the functions that gets info 
    from the explorer class and updates it to the gui.

    """

    version = '2.0'
    error_msg = StringProperty('')
    sync_status = StringProperty("  Synchronization:    /            Connected Peers: ")
    daemon_address = StringProperty(TRTLdaemon.host+":"+str(TRTLdaemon.port))

    

    def on_start(self):
        pass

    def on_pause(self):
        pass

    def on_resume(self):
        pass

    def on_stop(self):
        TRTLdaemon.kill_daemon()


    def build(self):
        
        self.title = "Turtle Local Explorer 2.0"
        self.root.current = 'startscreen'
        self.root.searchscreen.ids.search_tx_button.disabled = True
        self.root.searchscreen.ids.search_block_button.disabled = True
        app_logger.info('Turtle Local Explorer App GUI built.')

    def establish_connection(self):
        #check connection parameters first
        #if not valid, return a popup saying not valid
        #if self.path_is_valid():
        #    p = LoadingPopup()
        #    p.open()
       # else:
         #   p = ErrorPopUp()
         #   p.open()

        #while 
        #p.dismiss()
        self.root.current = 'mainscreen'
        TRTLdaemon.daemon = True
        TRTLdaemon.start()

        #deamon_stdout_Thread = threading.Thread(target = update_daemon_infoq)
        #deamon_stdout_Thread.start()
        daemon_stats_Thread = threading.Thread(target = update_explore_q)
        daemon_stats_Thread.start()
        #Clock.schedule_interval(self.get_daemon_info, 0.1)
        Clock.schedule_interval(self.get_explorer_realtime, 5)
        app_logger.info('Sych stats loop scheduled.')
        Clock.schedule_interval(self.check_search_queue, 5)
        app_logger.info('Search result loop scheduled.')
        app_logger.info('Turtle Local Explorer started.')


    def path_is_valid(self):

        if self.TRTLdaemon!=None:
            return True
        else:
            self.error_msg = "Please check the parameters"
            return False
    '''
    def get_daemon_info(self, dt):  
    #updates stdout from daemon console
        if daemon_infoq.empty():
            pass
        else:
            line = daemon_infoq.get()
            self.root.daemonscreen.ids.daemon_info.text += line
            self.root.daemonscreen.ids.scroll_txtinput.scroll_to(self.root.daemonscreen.ids.bottom_label)
            line = ''
    '''

    def get_explorer_realtime(self, dt): 
        #get synch_stat, recent_block, and tx_pool
        self.sync_status = daemon_stats_q.get()
        #daemon is sych'd if can_search is True
        if TRTLdaemon.can_search: 
            self.root.searchscreen.ids.search_tx_button.disabled = False
            self.root.searchscreen.ids.search_block_button.disabled = False
        #update txpool and recent blocks here
            if tx_pool_q.empty()or recent_blk_q.empty():
                pass
            else:
                self.update_txpool_recentblocks(tx_pool_q.get(), recent_blk_q.get())
        else:
            self.root.searchscreen.ids.search_tx_button.disabled = True
            self.root.searchscreen.ids.search_block_button.disabled = True

    def update_txpool_recentblocks(self, txpool, recentblocks):
        #txpool
        try:
            self.root.mainscreen.ids.txp_datalistTemplate.clear_widgets()
            for i in data_constructor.TxPool(txpool):
                self.root.mainscreen.ids.txp_datalistTemplate.add_widget(i)
        except Exception as e:
            app_logger.debug('Something went wrong while updating tx pool. Check below.')
            app_logger.debug(e)
        #recent blocks
        try:
            self.root.mainscreen.ids.rctblk_datalistTemplate.clear_widgets()
            for i in data_constructor.RecentBlocks(recentblocks):
                self.root.mainscreen.ids.rctblk_datalistTemplate.add_widget(i)
        except Exception as e:
            app_logger.debug('Something went wrong while updating recent blocks. Check below.')
            app_logger.debug(e)

    def check_search_queue(self, dt):
        #for checking search queue has something or not 
        #and this function is scheduled on start

        if tx_search_q.empty():
            pass
        else:
            self.update_TxSearchResult()
        if blk_search_q.empty():
            pass
        else:
            self.update_BlkSearchResult()


    def TxSchThread(self):
        #this initiates the tx searching thread
        app_logger.info('Search Tx clicked')
        self.root.searchscreen.ids.txsearch_display.clear_widgets()
        txHash = self.root.searchscreen.ids.search_tx_input.text

        def searchTx_q(HashN):
            tx_search_q.put(TRTLdaemon.searchTx(HashN))
        
        txThread = threading.Thread(target = searchTx_q, args = (txHash,))
        txThread.start()
        
        SearchingLabel = Label(text="Searching Transaction...", size_hint= (1, None), height = 50, font_size = 20,
                               color = (1,1,1,0.8))
        self.root.searchscreen.ids.txsearch_display.add_widget(SearchingLabel)


    def update_TxSearchResult(self):
        #this is called is search queue is not empty
        #it will take the data from the queue and displays it in the app
        try:
            self.root.searchscreen.ids.txsearch_display.clear_widgets()
            Result = tx_search_q.get()
            for i in data_constructor.TxSearchResult(Result):
                self.root.searchscreen.ids.txsearch_display.add_widget(i)
        except Exception as e:
            app_logger.debug('Something went wrong while checking Tx search Queue. Check below.')
            app_logger.debug(e)


    def BlkSchThread(self):
        #this initiates the blk searching thread
        app_logger.info('Search Block clicked')
        self.root.searchscreen.ids.blksearch_display.clear_widgets()
        blkHash = self.root.searchscreen.ids.search_block_input.text

        def searchBlk_q(blkHash):
            blk_search_q.put(TRTLdaemon.searchBlk(blkHash))
        
        blkthread = threading.Thread(target = searchBlk_q, args = (blkHash,))
        blkthread.start()
        
        SearchingLabel = Label(text="Searching Block...", size_hint= (1, None), height = 50, font_size = 20,
                               color = (1,1,1,0.8))
        self.root.searchscreen.ids.blksearch_display.add_widget(SearchingLabel)

    def update_BlkSearchResult(self):
        #this is called is search queue is not empty
        #it will take the data from the queue and displays it in the app
        try:
            self.root.searchscreen.ids.blksearch_display.clear_widgets()
            Result = blk_search_q.get()
            #loop through the label list and add all the labels in the search result display
            for i in data_constructor.BlockSearchResult(Result):
                self.root.searchscreen.ids.blksearch_display.add_widget(i)
        except Exception as e:
            app_logger.debug('Something went wrong while checking Block search Queue. Check below.')
            app_logger.debug(e)

    def search_on_click(self, searchType, hashN):  
        #search by clicking on the live explorer data
        if searchType == 'tx':
            app_logger.info('Search on click: Tx - clicked')
            self.root.searchscreen.ids.txsearch_display.clear_widgets()
            self.root.searchscreen.ids.search_tx_input.text = hashN

            def searchTx_q(HashN):
                tx_search_q.put(TRTLdaemon.searchTx(HashN))
            
            txThread = threading.Thread(target = searchTx_q, args = (hashN,))
            txThread.start()
            
            SearchingLabel = Label(text="Searching Transaction...", size_hint= (1, None), height = 50, font_size = 20,
                                   color = (1,1,1,0.8))
            self.root.searchscreen.ids.txsearch_display.add_widget(SearchingLabel)

        elif searchType == 'blk':
            app_logger.info('Search on click: Block - clicked')
            self.root.searchscreen.ids.blksearch_display.clear_widgets()
            self.root.searchscreen.ids.search_block_input.text = hashN

            def searchBlk_q(blkHash):
                blk_search_q.put(TRTLdaemon.searchBlk(blkHash))
            
            blkthread = threading.Thread(target = searchBlk_q, args = (hashN,))
            blkthread.start()
            
            SearchingLabel = Label(text="Searching Block...", size_hint= (1, None), height = 50, font_size = 20,
                                   color = (1,1,1,0.8))
            self.root.searchscreen.ids.blksearch_display.add_widget(SearchingLabel)

    def quitApp(self):
        self.on_stop()
        app_logger.info('Quit GUI App.')
        App.get_running_app().stop()
        Window.close()
        




