from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.app import App

from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

"""
These are some of the gui class used in the app 
"""


class CenteredTextInput(TextInput):
    '''
    A centered TextInput.
    '''
    text_width = NumericProperty()
    '''The text width
    '''
    def update_padding(self, *args):
        '''
        Update the padding so the text is centered
        '''
        self.text_width = self._get_text_width(
            self.text,
            self.tab_width,
            self._label_cached
        )

class ScreenManagement(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class DaemonScreen(Screen):
    pass

class SearchScreen(Screen):
    pass

class LoadingPopup(Popup):
    pass

class ErrorPopUp(Popup):
    pass

class TxPoolData(RelativeLayout):
    #this class displays the tx pool data
    itemText_amount = StringProperty()
    itemText_fee = StringProperty()
    itemText_size = StringProperty()
    itemText_hash = StringProperty()
    txp_amount = ObjectProperty(None)
    txp_fee = ObjectProperty(None)
    txp_size = ObjectProperty(None)
    txp_hash = ObjectProperty(None)

    def setText(self, amount, fee, size, hashhash):
        self.itemText_amount = amount
        self.itemText_fee = fee
        self.itemText_size = size
        self.itemText_hash = hashhash
        self.txp_amount.text = self.itemText_amount
        self.txp_fee.text = self.itemText_fee
        self.txp_size.text = self.itemText_size
        self.txp_hash.text = '[color=ffd700][ref='+self.itemText_hash+']'+self.itemText_hash+'[/ref][/color]'
        self.txp_hash.markup = True
        self.txp_hash.bind(on_ref_press = self.goToSearch)

    def goToSearch(self, instance, value):
        #the function that calls the search function.
        #used for txpool data when the markup text is clicked
        App.get_running_app().root.current = 'searchscreen'
        App.get_running_app().search_on_click("tx", self.itemText_hash)

class RecentBlockData(RelativeLayout):
    #this class displays the recent block data
    itemText_height = StringProperty()
    itemText_size = StringProperty()
    itemText_hash = StringProperty()
    itemText_difficulty = StringProperty()
    itemText_tx = StringProperty()
    itemText_datetime = StringProperty()
    rctblk_height = ObjectProperty(None)
    rctblk_size = ObjectProperty(None)
    rctblk_hash = ObjectProperty(None)
    rctblk_difficulty = ObjectProperty(None)
    rctblk_tx = ObjectProperty(None)
    rctblk_datetime = ObjectProperty(None)

    def setText(self, height, size, hashhash, difficulty, tx, datetime):
        self.itemText_height = height
        self.itemText_size = size
        self.itemText_hash = hashhash
        self.itemText_difficulty = difficulty
        self.itemText_tx = tx
        self.itemText_datetime = datetime
        
        self.rctblk_height.text = '[color=ffd700][ref='+self.itemText_height+']'+self.itemText_height+'[/ref][/color]'
        self.rctblk_height.markup = True
        self.rctblk_height.bind(on_ref_press = self.goToSearch_byHeight)
        
        self.rctblk_size.text = self.itemText_size 
        self.rctblk_hash.text = '[color=ffd700][ref='+self.itemText_hash+']'+self.itemText_hash+'[/ref][/color]'
        self.rctblk_hash.markup = True
        
        self.rctblk_hash.bind(on_ref_press = self.goToSearch_byHash)
        self.rctblk_difficulty.text = self.itemText_difficulty
        self.rctblk_tx.text = self.itemText_tx
        self.rctblk_datetime.text = self.itemText_datetime

    def goToSearch_byHash(self, instance, value):
        #the function that calls the search function (using hash).
        #used for txpool data when the markup text is clicked
        App.get_running_app().root.current = 'searchscreen'
        App.get_running_app().search_on_click("blk", self.itemText_hash)
            
    def goToSearch_byHeight(self, instance, value):
        #the function that calls the search function (using height).
        #used for txpool data when the markup text is clicked
        App.get_running_app().root.current = 'searchscreen'
        height = self.itemText_height.replace(",","")
        App.get_running_app().search_on_click("blk", height)


class BigLabel(Label):
    pass
class SmallLabel(Label):
    blockHash = ""
    def setBlkHash (self, blkhash):
        self.blockHash = blkhash
    def goToSearch(self, instance, value):
        App.get_running_app().search_on_click("blk", self.blockHash)


class TXInputs(RelativeLayout):
    In_amount = StringProperty()
    In_image = StringProperty()
    input_amount = ObjectProperty(None)
    input_image = ObjectProperty(None)

    def setText(self, amount, image):
        self.In_amount = amount
        self.In_image = image
        self.input_amount.text = self.In_amount
        self.input_image.text = self.In_image
    
class TXOutputs(RelativeLayout):
    Out_amount = StringProperty()
    Out_key = StringProperty()
    output_amount = ObjectProperty(None)
    output_key = ObjectProperty(None)
    def setText(self, amount, key):
        self.Out_amount = amount
        self.Out_key = key
        self.output_amount.text = self.Out_amount
        self.output_key.text = self.Out_key

class BlkSearchData(RelativeLayout):
    #displays searched block data
    item1 = StringProperty()
    item2 = StringProperty()
    blkResultItem1 = ObjectProperty(None)
    blkResultItem2 = ObjectProperty(None)
    myHeight = ""
    def setText(self,item1text, item2text):
        self.item1 = item1text
        self.item2 = item2text
        self.blkResultItem1.text = self.item1
        self.blkResultItem2.text = self.item2
        self.blkResultItem1.bind(on_ref_press = self.goToSearch)
   
    def setMyHeight(self, blkHeight):
        self.myHeight = str(blkHeight)  #store blk height value for search on click
      
    def goToSearch(self, instance, value):
        if value == '<':
            #give clickability to arrows
            App.get_running_app().search_on_click("blk", str(int(self.myHeight)+1))
        elif value == '>':
            self.myHeight = int(self.myHeight) -1 
            if self.myHeight < 0:
                self.myHeight = 0
            App.get_running_app().search_on_click("blk", str(self.myHeight))


class BlkSearchTx(RelativeLayout):
    #displays searched tx data
    hashText = StringProperty()
    feeText = StringProperty()
    totalAmountText = StringProperty()
    sizeText = StringProperty()
    forSearchHash = ""
    tx_hash = ObjectProperty(None)
    tx_fee = ObjectProperty(None)
    tx_totalAmount = ObjectProperty(None)
    tx_Size = ObjectProperty(None)
    def setText(self, hashtext, fee, totalamount, size, forsearchHash):
        self.hashText = hashtext
        self.feeText = fee
        self.totalAmountText = totalamount
        self.sizeText = size
        self.tx_hash.text = self.hashText
        self.tx_hash.markup = True
        self.tx_hash.bind(on_ref_press = self.goToSearch)
        self.tx_fee.text = self.feeText 
        self.tx_totalAmount.text = self.totalAmountText
        self.tx_Size.text = self.sizeText
        self.forSearchHash = forsearchHash

    def goToSearch(self, instance, value):
        App.get_running_app().search_on_click("tx", self.forSearchHash)
