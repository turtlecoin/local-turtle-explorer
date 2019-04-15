<<<<<<< HEAD
# Local-Turtle-Explorer 2.0

This 2.0 version uses kivy for its GUI.

The choice of Kivy is just a personal adventure which I wanted to make something out of it.

If you find any issue or have a request or suggestion please submit a new issue in the github repo.


## Overview

Once you open the local explorer, it will take you to the start screen.

Your TurtleCoind daemon is set to your local host at prot 11898.

Simply click *Start Explorer* to start the program.

![alt text](img/readme_img/start_screen.PNG)

### Transaction Pool and Recent Blocks

When you start the explorer, the screen is going to jump to the *Tx pool and recent blocks* screen.

Notice that there is nothing showing on the screen because the program just started and is still synching.

Give it sometime and things will start showing up.

![alt text](img/readme_img/main_screen_at_synch.PNG)

Once the program is fully synched you can see the recent blocks and transaction pool.

![alt text](img/readme_img/main_screen_tx_inPool.PNG)

Sometimes the tx pool is empty. 

It is normal because there might not always be a pending transaction in the network.

![alt text](img/readme_img/main_screen_no_tx_inPool.PNG)

### Search

Click search at the buttom and it will take you to the search screen.

![alt text](img/readme_img/Search_screen_empty.PNG)

Just enter the hash or block height and you can begin to search.

#####Search for block
![alt text](img/readme_img/Search_screen_block.PNG)

#####Search for transaction
![alt text](img/readme_img/Search_screen_tx.PNG)

#####If you provide a invalid hash or height you will get an error
![alt text](img/readme_img/Search_screen_tx_error.PNG)

#### Note: *the yellow texts in the program are clickable. Once clicked, it will search the transaction or block for you accordingly. This includes the texts in the transaction pool and recent block screen.*





##### Credits to:

[Turtlecoin](https://github.com/turtlecoin)

[Kivy](https://kivy.org/#home)

##### Find Turtle Local Explorer in Turtlecoin repo:

[turtle-explorer-desktop](https://github.com/turtlecoin/turtle-explorer-desktop)

##### My Repo:

[Sabo (Revolutionary)](https://github.com/yumingchangsabodota)
=======
# local-turtle-explorer

If you are a TRTL, explorer other TRTLs locally!

Just download and extract the release .zip file. You will find Local_Turtle_Explorer.exe there.

When you start the local explorer, it will initiate the RPC daemon itself, there is nothing else you need to do.

Please note that the local explorer will start the daemon which other users can connect to your daemon. The option of choosing the daemon starting mode might be added in the future.

*The status bar in the window disappear ocassionally, it is a known issue; however, after some research, it might be a bug in Qt5. We will find a solution for this issue in the future.

Feel free to suggest anything or report any issue.

Sabo (Revolutionary)
>>>>>>> e7d47dbd9d00fd30a76b6a516bd4cad1be05819d
