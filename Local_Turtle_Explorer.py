# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

'''
'''
__author__ = 'Sabo (Revolutionary)'

import time
import sys
import subprocess
import threading
import time
from datetime import datetime
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon


from dialogs import aboutQt_Dialog, aboutTRTL_local_explorer_Dialog
from explorer_services import Daemon_Connect, Block_Finder, Tx_Finder

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(1460, 870)
        self.setMinimumSize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material\\img\\turtlecoin_icon_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setObjectName("tab")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_blktx = QtWidgets.QHBoxLayout()
        self.horizontalLayout_blktx.setSpacing(3)
        self.horizontalLayout_blktx.setObjectName("horizontalLayout_blktx")
        self.verticalLayout_blk = QtWidgets.QVBoxLayout()
        self.verticalLayout_blk.setObjectName("verticalLayout_blk")
        
        self.label_rblk = QtWidgets.QLabel(self.tab)
        self.label_rblk.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_rblk.setObjectName("label_rblk")
        self.verticalLayout_blk.addWidget(self.label_rblk)
        
        self.tableWidget_blk = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_blk.setFont(font)
        self.tableWidget_blk.setObjectName("tableWidget_blk")
        self.tableWidget_blk.setColumnCount(6)
        self.tableWidget_blk.setRowCount(0)
        self.tableWidget_blk.verticalHeader().setVisible(False)
        self.verticalLayout_blk.addWidget(self.tableWidget_blk)
        self.horizontalLayout_blktx.addLayout(self.verticalLayout_blk)
        
        self.verticalLayout_tx = QtWidgets.QVBoxLayout()
        self.verticalLayout_tx.setObjectName("verticalLayout_tx")
        self.label_txpl = QtWidgets.QLabel(self.tab)
        self.label_txpl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_txpl.setObjectName("label_txpl")
        self.verticalLayout_tx.addWidget(self.label_txpl)
        self.tableWidget_txPool = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_txPool.setFont(font)
        self.tableWidget_txPool.setObjectName("tableWidget_txPool")
        self.tableWidget_txPool.setColumnCount(4)
        self.tableWidget_txPool.setRowCount(0)
        self.tableWidget_txPool.verticalHeader().setVisible(False)
        self.verticalLayout_tx.addWidget(self.tableWidget_txPool)
        
        
        self.horizontalLayout_blktx.addLayout(self.verticalLayout_tx)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_blktx)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material\\img\\blocks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_search = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search.setSpacing(7)
        self.horizontalLayout_search.setObjectName("horizontalLayout_search")
        self.verticalLayout_blksearch = QtWidgets.QVBoxLayout()
        self.verticalLayout_blksearch.setSpacing(3)
        self.verticalLayout_blksearch.setObjectName("verticalLayout_blksearch")
        self.textEdit_blk = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_blk.setObjectName("textEdit_blk")
        self.verticalLayout_blksearch.addWidget(self.textEdit_blk)
        self.tableWidget_blk_search = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        
        self.textEdit_blk.setFont(font)
        self.tableWidget_blk_search.setFont(font)
        self.tableWidget_blk_search.setObjectName("tableWidget_blk_search")
        self.tableWidget_blk_search.setColumnCount(5)
        self.tableWidget_blk_search.setRowCount(0)
        self.tableWidget_blk_search.verticalHeader().setVisible(False)
        self.verticalLayout_blksearch.addWidget(self.tableWidget_blk_search)
        
        self.lineEdit_blk = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_blk.setObjectName("lineEdit_blk")
        self.verticalLayout_blksearch.addWidget(self.lineEdit_blk)
        
        self.btn_blk = QtWidgets.QPushButton(self.tab_2)
        self.btn_blk.setObjectName("btn_blk")
        self.verticalLayout_blksearch.addWidget(self.btn_blk)
        
        self.horizontalLayout_search.addLayout(self.verticalLayout_blksearch)
        self.verticalLayout_txsearch = QtWidgets.QVBoxLayout()
        self.verticalLayout_txsearch.setSpacing(3)
        self.verticalLayout_txsearch.setObjectName("verticalLayout_txsearch")
        self.textEdit_tx = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_tx.setObjectName("textEdit_tx")
        self.verticalLayout_txsearch.addWidget(self.textEdit_tx)
        
        self.tableWidget_tx_input_search = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        
        self.textEdit_tx.setFont(font)
        self.tableWidget_tx_input_search.setFont(font)
        self.tableWidget_tx_input_search.setObjectName("tableWidget_tx_input_search")
        self.tableWidget_tx_input_search.setColumnCount(3)
        self.tableWidget_tx_input_search.setRowCount(0)
        self.tableWidget_tx_input_search.verticalHeader().setVisible(False)
        self.verticalLayout_txsearch.addWidget(self.tableWidget_tx_input_search)
        
        self.tableWidget_tx_output_search = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_tx_output_search.setFont(font)
        self.tableWidget_tx_output_search.setObjectName("tableWidget_tx_output_search")
        self.tableWidget_tx_output_search.setColumnCount(3)
        self.tableWidget_tx_output_search.setRowCount(0)
        self.tableWidget_tx_output_search.verticalHeader().setVisible(False)
        self.verticalLayout_txsearch.addWidget(self.tableWidget_tx_output_search)

        self.lineEdit_tx = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_tx.setObjectName("lineEdit_tx")
        self.verticalLayout_txsearch.addWidget(self.lineEdit_tx)
        self.btn_tx = QtWidgets.QPushButton(self.tab_2)
        self.btn_tx.setObjectName("btn_tx")
        self.verticalLayout_txsearch.addWidget(self.btn_tx)
        self.horizontalLayout_search.addLayout(self.verticalLayout_txsearch)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_search)
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("material\\img\\search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1457, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAbout_Qt = QtWidgets.QAction(QIcon("material\\img\\aboutqt.png"), '&About Qt', self)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_TRTL_Local_Block_Explorer = QtWidgets.QAction(QIcon("material\\img\\turtlecoin_icon_color.png"), '&About Local Turtle Explorer', self)
        self.actionAbout_TRTL_Local_Block_Explorer.setObjectName("actionAbout_TRTL_Local_Block_Explorer")
        self.menuHelp.addAction(self.actionAbout_TRTL_Local_Block_Explorer)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuHelp.menuAction())
        
#-----------------------------------------------------------------------------
# These are the objects for updating blockchain info and searching
        self.daemon_thread = Daemon_Connect()
        self.block_finder = Block_Finder()
        self.tx_finder = Tx_Finder()
#This variable is used to check whether if it is first time synched after opening the program or not
        self.firstTimeOpen = True
#-----------------------------------------------------------------------------  

        #self.retranslateUi(MainWindow)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

        #update the blockchain stat when receiving the signal from Daemon_connect
        self.daemon_thread.signal.connect(self.set_daemon_stat)
        #update the search result when receiving the signal from Block_Finder
        self.block_finder.Resultsignal.connect(self.update_search_result)
        self.tx_finder.Resultsignal.connect(self.update_search_result)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Local Turtle Explorer v0.0.1"))
        self.label_rblk.setText(_translate("MainWindow", "Recent Block"))
        self.label_txpl.setText(_translate("MainWindow", "Transaction Pool"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Recent Blocks and Tx Pool"))
        self.btn_blk.setText(_translate("MainWindow", "Go to Block"))
        self.btn_blk.setEnabled(False)
        self.btn_tx.setText(_translate("MainWindow", "Find Transaction"))
        self.btn_tx.setEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionAbout_TRTL_Local_Block_Explorer.setText(_translate("MainWindow", "About Local Turtle Explorer"))
        
        horblkheader = ["Height","Size","Block Hash","Difficulty","Txs Count","Date & Time"]
        horTxpoolheader = ["Amount","Fee","Size","Hash"]
        searchblkheader = ["Tx","Hash", "Fee", "Amount Out", "Size"]
        searchtxoutheader = ["Output", "Amount", "Key"]
        searchtxinheader = ["Input", "Amount", "Image"]

        self.statusbar.showMessage('TRTL Chain Status -')
        
        #Set blk table header
        self.tableWidget_blk.setHorizontalHeaderLabels(horblkheader)
        #Set Txpool table header
        self.tableWidget_txPool.setHorizontalHeaderLabels(horTxpoolheader)
        #Set block search table header
        self.tableWidget_blk_search.setHorizontalHeaderLabels(searchblkheader)
        #Set tx search table header
        self.tableWidget_tx_input_search.setHorizontalHeaderLabels(searchtxinheader)
        self.tableWidget_tx_output_search.setHorizontalHeaderLabels(searchtxoutheader)

        #Starts the daemon thread on GUI start
        self.daemon_thread.start()
        
        #When button clicked, starts the thread of Block_finder object and passes the hash from lineEdit()
        self.btn_blk.clicked.connect(self.block_search)
        self.btn_tx.clicked.connect(self.tx_search)

        #set menubar actions
        self.actionAbout_Qt.triggered.connect(self.open_aboutQt_Dialog)
        self.actionAbout_TRTL_Local_Block_Explorer.triggered.connect(self.open_aboutTRTL_local_explorer_Dialog)

        
    #Actions when shutting donw local explorer    
    def shut_down(self):
        self.daemon_thread.shut_down_daemon()

    def open_aboutQt_Dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = aboutQt_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        Dialog.show()

    def open_aboutTRTL_local_explorer_Dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = aboutTRTL_local_explorer_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        Dialog.show()
        
    def block_search(self):
        self.block_finder.blk_searchHash= self.lineEdit_blk.text()
        self.btn_blk.setEnabled(False)
        self.btn_tx.setEnabled(False)
        self.textEdit_blk.setText("Searching might take a while depending on your connection...")
        self.tableWidget_blk_search.setRowCount(0)
        self.block_finder.start()
        
    def tx_search(self):
        self.tx_finder.tx_searchHash= self.lineEdit_tx.text()
        self.btn_blk.setEnabled(False)
        self.btn_tx.setEnabled(False)
        self.textEdit_tx.setText("Searching might take a while depending on your connection...")
        self.tableWidget_tx_input_search.setRowCount(0)
        self.tableWidget_tx_output_search.setRowCount(0)
        self.tx_finder.start()
        
    def update_search_result(self, Resultsignal):

        if Resultsignal['method'] == "block":
            if Resultsignal['error'] == "yes":
                self.textEdit_blk.setText(Resultsignal['response'])
                self.btn_blk.setEnabled(True)
                self.btn_tx.setEnabled(True)
            else:
                results = self.formatting_Text(Resultsignal)
                self.textEdit_blk.setText(results['mainResult'])
                self.tableWidget_blk_search.setRowCount(len(results['transactions']))
                for i in range(len(results['transactions'])):
                    self.tableWidget_blk_search.setItem(i , 0, results['transactions'][i]['tx'])
                    self.tableWidget_blk_search.setItem(i , 1, results['transactions'][i]['hash'])
                    self.tableWidget_blk_search.setItem(i , 2, results['transactions'][i]['fee'])
                    self.tableWidget_blk_search.setItem(i , 3, results['transactions'][i]['amount_out'])
                    self.tableWidget_blk_search.setItem(i , 4, results['transactions'][i]['size'])
                self.tableWidget_blk_search.resizeColumnsToContents()
                self.tableWidget_blk_search.resizeRowsToContents()
                self.tableWidget_blk_search.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table
                self.btn_blk.setEnabled(True)
                self.btn_tx.setEnabled(True)
        elif Resultsignal['method'] == "tx":
            if Resultsignal['error'] == "yes":
                self.textEdit_tx.setText(Resultsignal['response'])
                self.btn_blk.setEnabled(True)
                self.btn_tx.setEnabled(True)
            else:
                results = self.formatting_Text(Resultsignal)
                self.textEdit_tx.setText(results['mainResult'])
                self.tableWidget_tx_input_search.setRowCount(len(results['inputs']))
                self.tableWidget_tx_output_search.setRowCount(len(results['outputs']))
                
                for i in range(len(results['inputs'])):
                    self.tableWidget_tx_input_search.setItem(i , 0, results['inputs'][i]['input'])
                    self.tableWidget_tx_input_search.setItem(i , 1, results['inputs'][i]['amount'])
                    self.tableWidget_tx_input_search.setItem(i , 2, results['inputs'][i]['image'])
                self.tableWidget_tx_input_search.resizeColumnsToContents()
                self.tableWidget_tx_input_search.resizeRowsToContents()
                
                for i in range(len(results['outputs'])):
                    self.tableWidget_tx_output_search.setItem(i , 0, results['outputs'][i]['output'])
                    self.tableWidget_tx_output_search.setItem(i , 1, results['outputs'][i]['amount'])
                    self.tableWidget_tx_output_search.setItem(i , 2, results['outputs'][i]['key'])
                self.tableWidget_tx_output_search.resizeColumnsToContents()
                self.tableWidget_tx_output_search.resizeRowsToContents()

                self.tableWidget_tx_input_search.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table
                self.tableWidget_tx_output_search.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table
                self.btn_blk.setEnabled(True)
                self.btn_tx.setEnabled(True)

    def formatting_Text(self, Resultsignal):
        if Resultsignal['method'] == "block":
            resultString ='''Height: {}\nTimestamp: {}\nVersion: {}\nDifficulty: {}\nOrphan: {}\nTransaction: {}\n
Total coins in the network: {} trtl\nTotal transactions in the network: {}\n
Total transaction size, bytes: {}\nTotal block size, bytes: {}\n
Current txs median, bytes: {}\nEffective txs median, bytes: {}\n
Reward penalty: {}%\nTransaction fee: {} trtl\nReward: {}\n
'''        
            resultString = resultString.format(Resultsignal['response']['result']['block']['height'],
                                               datetime.fromtimestamp(Resultsignal['response']['result']['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                                               str(Resultsignal['response']['result']['block']['major_version'])+"."+str(Resultsignal['response']['result']['block']['minor_version']),
                                               Resultsignal['response']['result']['block']['difficulty'],
                                               Resultsignal['response']['result']['block']['orphan_status'],
                                               len(Resultsignal['response']['result']['block']['transactions']),
                                               str(int(Resultsignal['response']['result']['block']['alreadyGeneratedCoins'])/100),
                                               Resultsignal['response']['result']['block']['alreadyGeneratedTransactions'],
                                               Resultsignal['response']['result']['block']['transactionsCumulativeSize'],
                                               Resultsignal['response']['result']['block']['blockSize'],
                                               Resultsignal['response']['result']['block']['sizeMedian'],
                                               Resultsignal['response']['result']['block']['effectiveSizeMedian'],
                                               Resultsignal['response']['result']['block']['penalty'],
                                               Resultsignal['response']['result']['block']['totalFeeAmount']/100,
                                               Resultsignal['response']['result']['block']['reward']/100)

            resultAll = {"mainResult":resultString, "transactions":[]}            
            
            i = 0
            for tx in Resultsignal['response']['result']['block']['transactions']:
                i+=1
                tmpDict = {}
                tmpDict = {"tx":QtWidgets.QTableWidgetItem(str(i)),
                           "hash":QtWidgets.QTableWidgetItem(tx['hash']),
                           "fee":QtWidgets.QTableWidgetItem(str(tx['fee']/100)),
                           "amount_out":QtWidgets.QTableWidgetItem(str(tx['amount_out']/100)),
                           "size":QtWidgets.QTableWidgetItem(str(tx['size']))}
                resultAll['transactions'].append(tmpDict)
        
            return resultAll

        elif Resultsignal['method'] == "tx":
            
            sumOut = 0

            for outp in Resultsignal['response']['result']['tx']['vout']:
                sumOut += outp['amount']

            sumOut = sumOut/100

            resultString = '''Confirmations: {}\nFirst confirmation time: {}\nFee: {} trtl\nSum of outputs: {} trtl\nSize: {}\nMixin count: {}\n\n
In Block:\nHash: {}\nHeight: {}\n
'''
            resultString = resultString.format(Resultsignal['current_blk_height'] - Resultsignal['response']['result']['block']['height'],
                                               datetime.fromtimestamp(Resultsignal['response']['result']['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                                               Resultsignal['response']['result']['txDetails']['fee']/100,
                                               sumOut,
                                               Resultsignal['response']['result']['txDetails']['size'],
                                               Resultsignal['response']['result']['txDetails']['mixin'],
                                               Resultsignal['response']['result']['block']['hash'],
                                               Resultsignal['response']['result']['block']['height'])

            resultAll = {"mainResult":resultString, "inputs":[], "outputs":[]}

            #Add inputs to dictionary
            i = 0
            #print(Resultsignal['response']['result']['tx']['vin'])
            if Resultsignal['response']['result']['tx']['vin'][0]['type']!='ff':
                for tx in Resultsignal['response']['result']['tx']['vin']:
                    i+=1
                    tmpDict = {}
                    tmpDict = {"input":QtWidgets.QTableWidgetItem(str(i)),
                        "amount":QtWidgets.QTableWidgetItem(str(tx['value']['amount']/100)),
                        "image":QtWidgets.QTableWidgetItem(str(tx['value']['k_image']))}
                    resultAll['inputs'].append(tmpDict)

            #Add outputs to dictionary
            i = 0
            for tx in Resultsignal['response']['result']['tx']['vout']:
                i+=1
                tmpDict = {}
                tmpDict = {"output":QtWidgets.QTableWidgetItem(str(i)),
                           "amount":QtWidgets.QTableWidgetItem(str(tx['amount']/100)),
                           "key":QtWidgets.QTableWidgetItem(str(tx['target']['data']['key']))}
                resultAll['outputs'].append(tmpDict)

            return resultAll
        
    def set_daemon_stat(self, signal):

        if signal['signal'] =="Connecting":
            self.statusbar.showMessage("TRTL Chain Status - ...Initializing daemon. It might take longer depending on your connection.")
            self.textEdit_blk.setText("Search will be available when the daemon is synched!")
            self.textEdit_tx.setText("Search will be available when the daemon is synched!")
        elif signal['signal'] =="Connected":
            self.statusbar.showMessage("TRTL Chain Status - ...daemon initialized, waiting to synch")
            self.textEdit_blk.setText("Search will be available when the daemon is synched!")
            self.textEdit_tx.setText("Search will be available when the daemon is synched!")
            
        elif signal['signal'] =="synching":

            self.statusbar.showMessage("TRTL Chain Status - Local Block Height:"+ str(signal['current_daemon_height'])+
                                               " / "+"Network Block Height:"+str(signal['network_height'])+"...Synching")
        elif signal['signal'] =="synched":
            self.statusbar.showMessage("TRTL Chain Status - Local Block Height:"+ str(signal['current_daemon_height'])+
                                               " / "+"Network Block Height:"+str(signal['network_height']))

            self.tableWidget_blk.setRowCount(len(signal['recentBlocks']))
            self.tableWidget_txPool.setRowCount(len(signal['transactionPool']))

            for i in range(len(signal['recentBlocks'])):
                #add block info to table
                blockheight = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['height']))
                size = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['cumul_size']))
                blockHash = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['hash']))
                difficulty = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['difficulty']))
                txs = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['tx_count']))
                dateTime = QtWidgets.QTableWidgetItem(datetime.fromtimestamp(signal['recentBlocks'][i]['timestamp']).strftime('%Y-%m-%d %H:%M:%S'))
                self.tableWidget_blk.setItem(i , 0, blockheight)
                self.tableWidget_blk.setItem(i , 1, size)
                self.tableWidget_blk.setItem(i , 2, blockHash)
                self.tableWidget_blk.setItem(i , 3, difficulty)
                self.tableWidget_blk.setItem(i , 4, txs)
                self.tableWidget_blk.setItem(i , 5, dateTime)
                self.tableWidget_blk.resizeColumnsToContents()
                self.tableWidget_blk.resizeRowsToContents()
                self.tableWidget_blk.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table

            for i in range(len(signal['transactionPool'])):
                #add transaction info to table
                amount = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['amount_out']))
                fee = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['fee']/100))
                size = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['size']))
                txHash = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['hash']))
                self.tableWidget_txPool.setItem(i , 0, amount)
                self.tableWidget_txPool.setItem(i , 1, fee)
                self.tableWidget_txPool.setItem(i , 2, size)
                self.tableWidget_txPool.setItem(i , 3, txHash)
                self.tableWidget_txPool.resizeColumnsToContents()
                self.tableWidget_txPool.resizeRowsToContents()
                self.tableWidget_txPool.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table

            self.btn_blk.setEnabled(True)
            self.btn_tx.setEnabled(True)
            #Check whether this is the first sych after opening the program
            if self.firstTimeOpen == True:
                self.textEdit_blk.setText("Daemon is synched! Start searching now!!!")
                self.textEdit_tx.setText("Daemon is synched! Start searching now!!!")
                self.firstTimeOpen = False
            else:
                pass

    def closeEvent(self, QCloseEvent):
        #QCloseEvent.ignore()
        self.shut_down()
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    #MainWindow.show()
    ui.show()
    sys.exit(app.exec_())

