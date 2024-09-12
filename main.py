from logging_tracker import LoggerBuilder


Logger = LoggerBuilder()
log = Logger.builder(option="cloud")

log.warning("check")
