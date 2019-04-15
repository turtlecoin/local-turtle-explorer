from turtle_local_explorer import Turtle_Local_Explorer
import logging
from logging.handlers import RotatingFileHandler


if __name__ =="__main__":
	#get logger
	logger = logging.getLogger('turtle_local_explorer_log')
	logger.setLevel(logging.DEBUG)
	#add file handler to logger
	fileh = RotatingFileHandler('turtle_local_explorer.log', maxBytes=20971520, backupCount=2)
	formatter = logging.Formatter('[%(asctime)s] [%(name)s] \t[%(levelname)s]:\t %(message)s')
	fileh.setLevel(logging.DEBUG)
	fileh.setFormatter(formatter)
	logger.addHandler(fileh)

	#app instance
	#then run app
	myApp = Turtle_Local_Explorer()
	myApp.run()
