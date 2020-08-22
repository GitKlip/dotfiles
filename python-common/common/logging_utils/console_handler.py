
import logging


def setup_as_console_handler(logger=None, format_str=None, log_level=logging.INFO):
    """  Adds a console StreamHandler to the logger so expected commandline receives output.

    See: https://docs.python.org/3/howto/logging.html#configuring-logging

    Motivation:

        The default logger does not behave the way a person would expect

        [By default, logging uses a LastResort handler set to WARN loglevel (i.e.,
        you won't see info or debug messages, EVEN if you set the log level!).]

            import logging

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)

            logger.info("info!")
            logger.debug("debug!")
            logger.warning("warning!")
            logger.error("error!")

            # You expect all 4 of the above, UNEXPECTEDLY you only get "warning!" and "error!"

        Adding a console handler will then give the expected behavior

            from common.loggers import create_console_logger

            logger = setup_as_console_handler(logging.getLogger(__name__))
            logger.setLevel(logging.DEBUG)

            logger.info("info!")
            logger.debug("debug!")
            logger.warning("warning!")
            logger.error("error!")

            # Now we get "info!", "debug!", "warning!" and "error!"

    Args:
        logger (logging.Logger): The logger on which to add a handler;
            defaults to root logger if None.
        format_str (str): The format string for the logger (see example url
            for details)
        log_level (int): one of logging.INFO, logging.DEBUG, etc.  Note: this sets
            the logger level, not the handler level.  The handler is set to DEBUG
            so that it can handle messages of any log level.

    Returns:
        (logging.Logger): The logger passed in, or the root logger.
    """
    if logger is None:
        logger = logging.getLogger()

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    if format_str is not None:
        formatter = logging.Formatter(format_str)
        stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(log_level)
    return logger
