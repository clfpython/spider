import logging

logging.basicConfig(level=logging.WARNING,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s : %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='myapp.log',
                filemode='a')


logging.debug('this is python')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is error')