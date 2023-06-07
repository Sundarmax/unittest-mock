import logging
#logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(level=logging.NOTSET)

logging.info('This is just an information')
logging.debug('This is for debugging')
logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# name = str(input("Enter Your Name:\n"))
# logging.info(f"{name} has logged in successfully !!")