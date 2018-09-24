import subprocess
import threading
from threading import Thread
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from turtlecoin import TurtleCoind

class Daemon_Connect(QThread):
    signal= pyqtSignal(object)

    def __init__(self, parent = None):
        super(Daemon_Connect, self).__init__(parent)

        #-------------explorer parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        trtlDaemon = "turtleDaemon\\TurtleCoind.exe --enable_blockexplorer --rpc-bind-ip=0.0.0.0 --rpc-bind-port=11898"  #remove --rpc-bind-ip=0.0.0.0 if you don't want to be connected
       #-------------------------------------------------------------------------------------
        #start Daemon throught subprocess
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE #hide daemon console
        self.daemon = subprocess.Popen(trtlDaemon, startupinfo = startupinfo)
        
    def run(self):  #initializing the connection with daemon and update the status between local and remote chain

        current_daemon_height = None
        network_height = None
        recentBlocks = None
        transactionPool = None
        
        mySignal = {}
        
        while current_daemon_height  == None or network_height== None :  #this while loop makes sure that local daemon is connected first
            try:
                current_daemon_height = self.turtlecoind.get_height()['height']
                network_height = self.turtlecoind.get_height()['network_height']
            except Exception as e:
                mySignal['signal'] = "Connecting"
                self.signal.emit(mySignal)
                #print(e)
                pass
            
        mySignal['signal'] = "Connected"
        self.signal.emit(mySignal)
        
        
        while True:  #updating synching status
            
            try:
                network_height = self.turtlecoind.get_height()['network_height']
                current_daemon_height = self.turtlecoind.get_height()['height']
                recentBlocks = self.turtlecoind.get_blocks(current_daemon_height)
                transactionPool = self.turtlecoind.get_transaction_pool()
                
                if current_daemon_height == network_height or current_daemon_height >= network_height:
                    
                    mySignal['signal'] = "synched"
                    mySignal['network_height'] = network_height
                    mySignal['current_daemon_height'] = current_daemon_height 
                    mySignal['recentBlocks'] = recentBlocks['result']['blocks'] #a list of recent blocks
                    mySignal['transactionPool'] = transactionPool['result']['transactions'] #a list of transaction
                    
                    self.signal.emit(mySignal)
              
                else:
                    
                    mySignal['signal'] = "synching"
                    mySignal['network_height'] = network_height
                    mySignal['current_daemon_height'] = current_daemon_height 
                    
                    self.signal.emit(mySignal)

            except Exception as e:
                mySignal['signal'] = 'exception'
                mySignal['msg'] = str(e)
                self.signal.emit(mySignal)
                
    #shuts down the daemon initiated by subprocess      
    def shut_down_daemon(self):
        self.daemon.terminate()
        self.daemon.kill()
        
class Block_Finder(QThread):
    Resultsignal = pyqtSignal(object)

    def __init__(self, parent = None):
        super(Block_Finder, self).__init__(parent)
        #-------------daemon parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        #-------------------------------------------------------------------------------------
        self.blk_searchHash = ""

   
    def run(self):
        result = {}
        result['method'] = "block"
        try:
            result['response'] = self.turtlecoind.get_block(self.blk_searchHash)
            result['error'] = "no"
        except:
            result['error'] = "yes"
            result['response'] = "Block not found!"
        self.Resultsignal.emit(result)

class Tx_Finder(QThread):
    Resultsignal = pyqtSignal(object)

    def __init__(self, parent = None):
        super(Tx_Finder, self).__init__(parent)
        #-------------daemon parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        #-------------------------------------------------------------------------------------
        self.tx_searchHash = ""
   
    def run(self):
        result = {}
        result['method'] = "tx"
        try:
            result['response'] = self.turtlecoind.get_transaction(self.tx_searchHash)
            result['current_blk_height'] = self.turtlecoind.get_height()['height']
            result['error'] = "no"
        except:
            result['error'] = "yes"
            result['response'] = "Transaction not found; either the tx hash is incorrect or it is not added to the blockchain yet."
        self.Resultsignal.emit(result)

