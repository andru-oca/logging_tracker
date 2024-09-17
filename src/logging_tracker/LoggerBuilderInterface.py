from logging_tracker import FileLogger, WrapperLogger, PrinterLogger

from google.cloud.logging import Client
from google.cloud.logging import Logger


class LoggerBuilderInterface:
    def _get_logger(self, name: str, sink: str) -> Logger:
        client = Client(project=name)
        return client.logger(sink)

    def _cloud_logger(self, params):
        name = params.get("gcp_name")
        sink = params.get("gcp_sink")

        if None in [name, sink]:
            raise ValueError("Missing required parameters for cloud logger.")

        logger = self._get_logger(name, sink)

        key = f"cloud_{name}_{sink}"

        if key not in self._loggers:
            logger = self._get_logger(name, sink)
            self._loggers[key] = WrapperLogger(logger)

        return self._loggers[key]

    def _local_logger(self, params):
        file = params.get("log_file","logger.log")
        level = params.get("log_level","debug")

        key = f"local_{file}_{level}"

        if key not in self._loggers:
            self._loggers[key] = FileLogger(file, level=level)

        return self._loggers[key]

    def _printer_logger(self):

        key = "printer"

        if key not in self._loggers:
            self._loggers[key] = PrinterLogger()

        return self._loggers[key]
