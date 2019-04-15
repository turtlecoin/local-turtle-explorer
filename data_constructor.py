from gui_classes import TxPoolData, RecentBlockData, BigLabel, SmallLabel, \
					TXInputs,TXOutputs, BlkSearchData,BlkSearchTx
from datetime import datetime
from kivy.uix.relativelayout import RelativeLayout

import logging

"""
This file contains the functions that
construct and return the data objects to be displayed in 
the local turtle explorer kivy app.
"""

def TxPool(txpool):
	txs_list = []
	for i in range(len(txpool)):
		tpd = TxPoolData()
		if i%2!=1:
			pass
		else:
			tpd.colors = (128/255,128/255,128/255,0.8)
		amount = "{:,}".format(txpool[i]['amount_out']/100)
		fee = "{:,}".format(txpool[i]['fee']/100)
		size = "{:,}".format(txpool[i]['size'])
		txhash = str(txpool[i]['hash'])
		tpd.setText(amount,fee,size,txhash)
		txs_list.append(tpd)
	return txs_list

def RecentBlocks(recentblocks):
	recentblks_list = []
	for i in range(len(recentblocks)):
		RecentBlockData1 = RecentBlockData()
		if i%2!=1:
			pass
		else:
			RecentBlockData1.colors = (128/255,128/255,128/255,0.8)
		height = "{:,}".format(recentblocks[i]['height'])
		size = "{:,}".format(recentblocks[i]['cumul_size'])
		blockhash = str(recentblocks[i]['hash'])
		difficulty = "{:,}".format(recentblocks[i]['difficulty'])
		txs = "{:,}".format(recentblocks[i]['tx_count'])
		dateTime = datetime.fromtimestamp(recentblocks[i]['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
		RecentBlockData1.setText(height,size,blockhash,difficulty,txs,dateTime,)
		recentblks_list.append(RecentBlockData1)
		
	return recentblks_list

def TxSearchResult(Result):
	#This part formats and construct the search transaction results then display them in labels
	#get tx search result from queue
	#if there is error display error msg, if not construct and display search result
	LabelList = []
	if Result["error"] == "yes":
		ErrorLabel = BigLabel(text = Result['msg'], height = 60, size_hint = (1,None))
		LabelList.append(ErrorLabel)
		
	elif Result["error"] == "no":
		current_h = Result['current_height']
		MyResult = Result['result']['result']
		#calculate confirmation from block height
		if current_h - MyResult['block']['height'] <= 0:
			confirmation = 0
		else:
			confirmation = "{:,}".format(current_h - MyResult['block']['height'])
		#first confirmation timestamp
		Firstconfirmation = datetime.fromtimestamp(MyResult['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S')

		#calculate sum of the outputs
		sumOfOutputs = sum(amount['amount'] for amount in MyResult['tx']['vout'])
		sumOfOutputs = "{:,}".format(sumOfOutputs/100)

		#get block hash, used for on click search
		blkHash = MyResult['block']['hash']

		TxLabel = BigLabel(text = "[b]TRANSACTION[/b]")
		#get transaction hash
		txHashLabel = SmallLabel(text = "Hash: "+MyResult['txDetails']['hash'])
		#confirmation and first confirmation time
		ConfirmLabel = SmallLabel(text = "Confirmations: " + confirmation +", First confirmation time: "+Firstconfirmation)
		#fee
		feeLabel = SmallLabel(text = "Fee: " + "{:,}".format(MyResult['txDetails']['fee']/100) + " TRTL")
		#sum of outputs
		sumOutLabel = SmallLabel(text = "Sum of outputs: " + sumOfOutputs+ " TRTL")
		#transaction size
		sizeLabel = SmallLabel(text = "Size: "+ "{:,}".format(MyResult['txDetails']['size']))
		#mixin count
		mixinLabel = SmallLabel(text = "Mixin: "+ "{:,}".format(MyResult['txDetails']['mixin']))

		InBlockLabel = BigLabel(text = "[b]IN BLOCK[/b]" )
		 #'[color=556b2f][ref='+self.hashText+']'+self.hashText+'[/ref][/color]'
		#in block info, add on_click_search behavior for block hash
		blkHashLabel = SmallLabel(text = "Hash: "+'[color=ffd700][ref='+blkHash+']'+blkHash+'[/ref][/color]')  #add click to hash search
		blkHashLabel.markup = True
		blkHashLabel.setBlkHash(blkHash)
		blkHashLabel.bind(on_ref_press = blkHashLabel.goToSearch)

		#block height
		blkheighLabel = SmallLabel(text = "Height: " + "{:,}".format(MyResult['block']['height']))
		timeLabel = SmallLabel(text = "Timestamp: " + Firstconfirmation)

		#input header
		inputHeader = TXInputs()
		inputHeader.setText("Amount", "Image")
		inputHeader.colors = (0.5, 0.5, 0.5, 0.8)
		#loop through input data and save to list
		inputList = []
		if MyResult['tx']['vin'][0]['type'] == 'ff': #check tx input counts
			inputCount = str(1)
			txinput = TXInputs()
			txinput.setText(sumOfOutputs+" TRTL","Miner Reward")
			inputList.append(txinput)
		else:
			inputCount = "{:,}".format(len(MyResult['tx']['vin']))
			for i in range(len(MyResult['tx']['vin'])):
				txinput = TXInputs()
				if i%2!=1:
					pass
				else:
					txinput.colors = (1,1,1,0.5)
				inAmount = "{:,}".format(MyResult['tx']['vin'][i]['value']['amount']/100)
				txinput.setText(inAmount+" TRTL",str(MyResult['tx']['vin'][i]['value']['k_image']))
				inputList.append(txinput)
		#input big label
		InputLabel = BigLabel(text = "[b]INPUTS ("+inputCount+")[/b]" )
		#add 2 padding label
		paddingLabel1 = SmallLabel()
		paddingLabel2 = SmallLabel()
		#save above constructors into a list
		LabelList = [TxLabel,txHashLabel,ConfirmLabel,feeLabel,sumOutLabel,
					sizeLabel,mixinLabel, paddingLabel1,InBlockLabel, blkHashLabel,
					blkheighLabel,timeLabel, paddingLabel2,InputLabel,inputHeader]
		#append inputs to the big list
		LabelList = LabelList + inputList

		#get output count
		outputCount = "{:,}".format(len(MyResult['tx']['vout']))
		#output title lable
		OutputLabel = BigLabel(text = "[b]OUTPUTS ("+outputCount+")[/b]" )
		#output header
		outputHeader = TXOutputs()
		outputHeader.setText("Amount", "Key")
		outputHeader.colors = (0.5, 0.5, 0.5, 0.8)
		#loop through outputs and save to a list
		outputList = [OutputLabel,outputHeader]
		for i in range(len(MyResult['tx']['vout'])):
			txoutput = TXOutputs()
			if i%2!=1:
				pass
			else:
				txoutput.colors = (1,1,1,0.5)
			outAmount = "{:,}".format(MyResult['tx']['vout'][i]['amount']/100)
			txoutput.setText(outAmount+" TRTL",str(MyResult['tx']['vout'][i]['target']['data']['key']))
			outputList.append(txoutput)
		#append outputlist to big list
		LabelList += outputList
		paddingLabel3 = BigLabel()
		LabelList.append(paddingLabel3)
		#add labels in big list to container widget
	return LabelList

def BlockSearchResult(Result):
	blockInfoList = []
	#if there is error, display error msg, if not, display search block result
	if Result["error"] == "yes":
		ErrorLabel = BigLabel(text = Result['msg'], height = 60, size_hint = (1,None))
		blockInfoList.append(ErrorLabel)
		return blockInfoList
	elif Result["error"] == "no":
		Result = Result['result']['result']

		#big labels are for titles, small labels for content
		BlockTitleLabel = BigLabel(text = "[b]BLOCK[/b]", size_hint = (1,0.6), pos_hint={"x":0, "y":0.4},valign = 'bottom')
		blockHashLabel = SmallLabel(text = "[b]"+Result['block']['hash']+"[/b]",size_hint = (1,0.4), pos_hint={"x":0, "y":0},
									valign ='bottom', font_size = 16, color = (47/255,79/255,79/255,1))
		blkTitleandHashLabel = RelativeLayout(size_hint = (1,None), height = 50)
		blkTitleandHashLabel.add_widget(BlockTitleLabel)
		blkTitleandHashLabel.add_widget(blockHashLabel)
		#add padding
		paddingLabel1 = SmallLabel(height = 10)

		#1 block height and total transaction size  
		#'[color=556b2f][ref='+self.hashText+']'+self.hashText+'[/ref][/color]'
		heighAndTotalTxSizelabel = BlkSearchData()
		heighAndTotalTxSizelabel.setText("Height: {} {:,} {}".format("[b][size=20][color=ffd700][ref=<]<[/ref][/color][/size][/b]",Result['block']['height'],"[b][size=20][color=ffd700][ref=>]>[/ref][/color][/size][/b]"),
										"Total transaction size, bytes: {:,}".format(Result['block']['transactionsCumulativeSize']))
		heighAndTotalTxSizelabel.setMyHeight(Result['block']['height'])

		#2 time and total block size
		timeAndTotalblkSizelabel = BlkSearchData()
		#the genesis block returns 0 in the timestamp, set genesis timestamp to nothing
		if Result['block']['timestamp'] != 0:  #check if it is genesis block
			timeAndTotalblkSizelabel.setText("Timestamp: "+datetime.fromtimestamp(Result['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
										"Total block size, bytes: {:,}".format(Result['block']['blockSize']))
		else:
			timeAndTotalblkSizelabel.setText("Timestamp: ",
										"Total block size, bytes: {:,}".format(Result['block']['blockSize']))
		#3 version and block size median
		versionAndCurrentTxMedianLabel = BlkSearchData()
		versionAndCurrentTxMedianLabel.setText("Version: {}.{}".format(Result['block']['major_version'],Result['block']['minor_version']),
											"Current txs median, bytes: {:,}".format(Result['block']['sizeMedian']))
		#4 difficulty and effective tx median
		difficultyAndEffectiveTxMedianLabel = BlkSearchData()
		difficultyAndEffectiveTxMedianLabel.setText("Difficulty: {:,}".format(Result['block']['difficulty']),
												"Effective txs median, bytes: {:,}".format(Result['block']['effectiveSizeMedian']))
		#5 Orphan status and reward penalty
		orphanAndRewardPenaltylabel = BlkSearchData()
		orphan = "No" if Result['block']['orphan_status'] == False else "Yes"
		orphanAndRewardPenaltylabel.setText("Orphan: {}".format(orphan),
											"Reward penalty: {:,}%".format(Result['block']['penalty']))
		#6 transactions and base reward
		txsAndBaserewardLabel = BlkSearchData()
		txsAndBaserewardLabel.setText("Transactions: {:,}".format(len(Result['block']['transactions'])),
										"Base reward: {:,} TRTL".format(Result['block']['baseReward']/100))
		#7 total coins in the network and transaction fee
		totalCoinNetAndTxFeeLabel = BlkSearchData()
		totalCoinNetAndTxFeeLabel.setText("Total coins in the network:\n {:,} TRTL".format(int(Result['block']['alreadyGeneratedCoins'])/100),
											"Transactions fee: {:,} TRTL".format(Result['block']['totalFeeAmount']/100))
		#8 total transactions in the network and reward
		totalTxsInNetAndReward = BlkSearchData()
		totalTxsInNetAndReward.setText("Total transactions in the network:\n {:,} TRTL".format(Result['block']['alreadyGeneratedTransactions']),
										"Reward: {:,}".format(Result['block']['reward']/100))
		#add padding in the search result display
		paddingLabel2 = SmallLabel()
		TxsLabel = BigLabel(text = "[b]TRANSACTIONS[/b]")

		#add tx header in the block to the result display
		TxheaderLabel = BlkSearchTx()
		TxheaderLabel.colors = (0.5, 0.5, 0.5, 0.8)
		TxheaderLabel.setText("Hash", "Fee", "Total Amount", "Size", "ForSearchHash")

		#append the above data to a list
		blockInfoList = [blkTitleandHashLabel,paddingLabel1,heighAndTotalTxSizelabel,timeAndTotalblkSizelabel,
						versionAndCurrentTxMedianLabel,difficultyAndEffectiveTxMedianLabel,orphanAndRewardPenaltylabel,
						txsAndBaserewardLabel,totalCoinNetAndTxFeeLabel,totalTxsInNetAndReward,paddingLabel2,TxsLabel,
						TxheaderLabel]
		#loop through block transaction data and construct a display label object and append to a list
		tmpTxList = []
		for i in range(len(Result['block']['transactions'])):
			txLabel = BlkSearchTx()
			if i%2!=1:
				pass
			else:
				txLabel.colors = (1,1,1,0.5)
			#'[color=556b2f][ref='+self.hashText+']'+self.hashText+'[/ref][/color]'
			txLabel.setText('[color=ffd700][ref='+Result['block']['transactions'][i]['hash']+']'+Result['block']['transactions'][i]['hash']+'[/ref][/color]',
							"{:,} TRTL".format(Result['block']['transactions'][i]['fee']/100),
							"{:,} TRTL".format(Result['block']['transactions'][i]['amount_out']/100),
							"{:,}".format(Result['block']['transactions'][i]['size']),
							Result['block']['transactions'][i]['hash']) #last hash is for searching purpose
			tmpTxList.append(txLabel)
		
		#append the tx data to the bigger list that has the general info
		blockInfoList+=tmpTxList
		#add last padding
		paddingLabel3 = BigLabel()
		blockInfoList.append(paddingLabel3)
		
	return blockInfoList

