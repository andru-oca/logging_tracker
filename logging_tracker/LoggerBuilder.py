from typing import Union, Dict
from logging_tracker import FileLogger, WrapperLogger, PrinterLogger
from logging_tracker import SingletonMetaLogger
from logging_tracker import LoggerBuilderInterface


class LoggerBuilder(LoggerBuilderInterface, metaclass=SingletonMetaLogger):

    def __init__(self):
        self._loggers: Dict[
            str, Union["WrapperLogger", "FileLogger", "PrinterLogger"]
        ] = {}

    def builder(
        self, option: str = None, **params
    ) -> Union["WrapperLogger", "FileLogger", "PrinterLogger"]:
        """
        Creates and returns a logger based on the specified option.

        Keywords Arguments:
            option (str): The type of logger to create. Can be 'cloud' or 'local'.
            **params: Additional parameters required for the logger initialization:
                - gcp_path (str): The path to the GCP project.
                - gcp_name (str): The GCP project ID.
                - gcp_sink (str): The GCP sink name.
                - log_file (str, optional): The log file path. Defaults to "logs.log".
                - log_level (str, optional): The log level. Defaults to "debug".

        Returns:
            Builder Singleton: A singleton object that provides access to the created logger.

        Raises:
            ValueError: If the specified logger option is invalid or unsupported.
            

        Printer
        Logger = LoggerBuilder()
        log = Logger.builder(option="local", log_file="logger_test.log", log_level="debug")
        """
        if option == "cloud":
            return self._cloud_logger(params)

        if option == "local":
            return self._local_logger(params)

        return self._printer_logger()
