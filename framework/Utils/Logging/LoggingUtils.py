import logging, os

class LoggingUtils(object):

    def get_logger(self, path, file_name, log_level=None):
        logger = logging.getLogger('TestAutomation')
        handler = logging.StreamHandler()
        full_path = path + "/" + file_name
        # format_message = '%(asctime)s| %(levelname)s|%(filename)s- %(funcName)10s():%(lineno)s| %(message)s'
        format_message = '%(asctime)s| %(levelname)s|%(filename)s:%(lineno)s| %(message)s'
        logging.basicConfig(filename=full_path, format=format_message)
        # formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        # handler.setFormatter(formatter)
        logger.addHandler(handler)
        if log_level is not None:
            logger.setLevel(log_level)
        else:
            logger.setLevel(logging.INFO)

        return logger
