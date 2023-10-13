import gits_logging


def gits_hello(args):
    """
    Function that prints hello message
    to user console
    """
    print("Hello from GITS Commandline Tools")
    gits_logging.gits_logger.info("Hello from GITS Commandline Tools")
