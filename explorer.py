import subprocess
import time
import sys

from turtlecoin import TurtleCoind
import threading

from global_variable import Daemon_DB_config, status_txt, daemon_host, daemon_port

from subprocess import Popen, PIPE
from queue import Queue, Empty
from time import sleep
import datetime
import logging

explorer_logger = logging.getLogger('turtle_local_explorer_log.explorer')

class Turtle_Explorer(threading.Thread):
    """
    This class is the backend of the local explorer app.
    It opens the turtlecoind daemon and makes the connections.
    It requests for the recent blocks and transaction pool data, 
    and does the search request as well.
    """

    host = daemon_host
    port = daemon_port
    turtlecoind = TurtleCoind(host, port)
    daemon_q = Queue(maxsize = 0)
    daemon_running = False

    txPool = None
    blocks = None

    status = "  Synchronization:    /            Connected Peers: "

    can_search = False

    Daemon = None

    def __init__(self):
        
        super(Turtle_Explorer, self).__init__()

    def run(self, *args):
   
        console_command = "turtleservices\\TurtleCoind.exe --enable-blockexplorer --rpc-bind-ip=0.0.0.0 --rpc-bind-port=11898"
        
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE #hide daemon console
        #self.Daemon = subprocess.Popen(console_command, stdout = PIPE, bufsize = 1, startupinfo = startupinfo)
        self.Daemon = subprocess.Popen(console_command, startupinfo = startupinfo)
        #Thread_daemon_stdout = threading.Thread(target = self.get_daemon_stdout)
        #Thread_daemon_stdout.start()

        Thread_daemon_sych_stats = threading.Thread(target = self.get_daemon_sych_stats)
        Thread_daemon_sych_stats.daemon = True
        Thread_daemon_sych_stats.start()

        explorer_logger.info("Explorer backend started.")  
    '''
    def get_daemon_stdout(self,*args):
        i = 0
        while self.Daemon.poll() is None:
            time.sleep(1)
            i+= 1
            for line in self.Daemon.stdout:  #stdout still hangs, buffer issue is not solved
                self.daemon_q.put(line.decode()) #output is not realtime, some outputs are waiting in buffer
                sys.stdout.write(line.decode())
            if not line:
                print("nothing in line")
                     
            else:
                self.Daemon.stdout.flush()
            print("still in loop"+str(i))
        print("Out of loop")
    '''
    def get_daemon_sych_stats(self, *args):
        #gets daemon info while the subprocess daemon is still running
        while self.Daemon.poll() is None:
            sleep(0.1)
            try:
                height = self.turtlecoind.get_height()['height']
                netHeight = self.turtlecoind.get_height()['network_height']
                peers =self.turtlecoind.get_peers()['peers']
                peers_len =len(peers)
                self.status= status_txt.format(height,netHeight,peers_len)
                explorer_logger.info(self.status)
                #self.deamon_info = turtlecoind.get_info()  #make sure this doesn't throw exception or it will not update the pool info
                if height < netHeight:
                    self.txPool = None
                    self.blocks = None
                    #self.can_search = False
                    explorer_logger.info('Local Explorer has lower height than network.')
                else:
                    self.txPool = self.turtlecoind.get_transaction_pool()['result']['transactions']
                    recentBlocks1 = self.turtlecoind.get_blocks(height-1)
                    recentBlocks2 = self.turtlecoind.get_blocks(height-31)
                    self.blocks = recentBlocks1['result']['blocks']+recentBlocks2['result']['blocks']
                    self.can_search = True
                    explorer_logger.info('Explorer fully synched.')
                       
            except Exception as e:
                explorer_logger.debug('Something went wrong while getting synch stat. See below.')
                explorer_logger.debug(e)

    def searchTx(self, txHash, *args):
        #search tx function, can be called by the app
        txResult = {}
        if txHash == "":
            txResult['error'] = "yes"
            txResult['msg'] = "ERROR: Please Enter a valid Tx Hash."
            explorer_logger.info(txResult['msg'])
            return  txResult

        else:
            try:
                Result = self.turtlecoind.get_transaction(txHash)
                current_height = self.turtlecoind.get_height()['height']
                txResult['error'] = "no"
                txResult['result'] = Result
                txResult['current_height'] = current_height
                explorer_logger.info("Tx search done.")
                return  txResult

            except Exception as e:
                txResult['error'] = "yes"
                txResult['msg'] = "ERROR: No Such Tx was found, or it's not been added to the chain yet."
                explorer_logger.debug('Something went wrong while searching Tx. See below.')
                explorer_logger.debug(e)
                return  txResult

    def searchBlk(self, blkHash, *args):
        #search block function, can be called by the app
        blkResult = {}
        if blkHash == "":
            blkResult['error'] = "yes"
            blkResult['msg'] = "ERROR: Please Enter a valid Block Hash."
            explorer_logger.info(blkResult['msg'])
            return blkResult
        else:
            try:
                Result = self.turtlecoind.get_block(blkHash)
                blkResult['error'] = "no"
                blkResult['result'] = Result
                explorer_logger.info("Block search done.")
                return blkResult

            except Exception as e:
                blkResult['error'] = "yes"
                blkResult['msg'] = "ERROR: No Such Block was found, please check your block hash."
                explorer_logger.debug('Something went wrong while searching Block. See below.')
                explorer_logger.debug(e)
                return blkResult

    

    def create_blockchain_dir(self, *args):
        #from pathlib import Path
        #osPath = str(Path.home())
        #mainPath = osPath +"\\AppData\\Roaming\\TurtleCoin" make a copy of Turtlecoin folder here
        #target = "D:\\TurtleCoin"

        #create symbolic link in windows
        #mklink mainPath "D:\\TurtleCoin"

        #to change folder, delete previous symbolic link and make a new one
        pass
            
    def kill_daemon(self, *args):
        self.Daemon.terminate()
        self.Daemon.kill() 
        explorer_logger.info('Explorer Daemon killed.')
