
# LoggerBuilder Repository

This repository contains the implementation of a `LoggerBuilder` class that allows the creation of different types of loggers (`WrapperLogger`, `FileLogger`, `PrinterLogger`) based on the specified option. It follows the Singleton pattern, ensuring only one instance of the logger is created.

## Overview

The `LoggerBuilder` class uses a builder pattern to generate and return different types of loggers. The available options for loggers include:
- **Cloud Logger (`WrapperLogger`)**: Used for cloud logging (e.g., GCP).
- **Local Logger (`FileLogger`)**: Logs messages to a file.
- **Printer Logger (`PrinterLogger`)**: Prints log messages directly to the console.

## Usage

### Creating a Logger

To create a logger, use the `builder` method of the `LoggerBuilder` class, specifying the type of logger and any additional parameters required for initialization.

```python
# Example for creating a File Logger
Logger = LoggerBuilder()
log = Logger.builder(option="local", log_file="logger_test.log", log_level="debug")
log.info("This is a test log message.")
```

### Available Logger Options

1. **`local` (File Logger)**: Logs messages to a file.
   - **Parameters**:
     - `log_file` (str, optional): The file where logs will be written. Defaults to `"logs.log"`.
     - `log_level` (str, optional): The log level. Defaults to `"debug"`.

2. **`cloud` (Wrapper Logger)**: Logs messages to a cloud-based logging system (e.g., GCP).
   - **Parameters**:
     - `gcp_name` (str): The GCP project ID.
     - `gcp_sink` (str): The GCP sink name.

3. **`printer` (Printer Logger)**: Prints log messages to the console.
   - **No additional parameters required**.

### Example Usage

#### Local File Logger
```python
Logger = LoggerBuilder()
log = Logger.builder(option="local", log_file="app.log", log_level="info")
log.info("Application started.")
```

#### Cloud Logger
```python
Logger = LoggerBuilder()
log = Logger.builder(option="cloud", gcp_name="project-id", gcp_sink="sink-name")
log.info("Logging to GCP.")
```

#### Printer Logger
```python
Logger = LoggerBuilder()
log = Logger.builder()
log.info("This is a console log message.")
```

## LoggerBuilder Class

### Method: `builder(option: str, **params) -> Union[WrapperLogger, FileLogger, PrinterLogger]`

Creates and returns a logger based on the specified option.

#### Keyword Arguments:
- `option` (str): The type of logger to create. Can be `'cloud'`, `'local'`, or `'printer'`.
- `**params`: Additional parameters required for logger initialization:
  - For **cloud**:
    - `gcp_path` (str): The path to the GCP project.
    - `gcp_name` (str): The GCP project ID.
    - `gcp_sink` (str): The GCP sink name.
  - For **local**:
    - `log_file` (str, optional): The log file path. Defaults to `"logs.log"`.
    - `log_level` (str, optional): The log level. Defaults to `"debug"`.

#### Returns:
- **Builder Singleton**: A singleton object that provides access to the created logger.

#### Raises:
- `ValueError`: If the specified logger option is invalid or unsupported.

## Installation

To use this repository, clone the project and install any dependencies using `pip`:

```bash
pip install git+https://github.com/andru-oca/logging_tracker
```

## Testing

To run tests for the `LoggerBuilder` class, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

If you'd like to contribute to this repository, feel free to fork the project, make your changes, and submit a pull request. All contributions are welcome!

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

