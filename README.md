# nix-python-utils

**Description**:
A collection of versatile classes, methods and decorators that I frequently use across my work projects.

## Content

- [Install](#Install)
- [Classes](#Classes)
- [Decorators](#Decorators)
- [Licence](#Licence)

##Install

```bash
pip install nix-python-utils
```

## Classes

| Class | Methods | Description |
|-------|---------|-------------|

## Decorators

For use decorators you need to import them from the package:

```python
import nix.utils.decorators as decorators
```

| Decorator    | Args                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @retry       | - max_retries (int, default=3) <br> - delay (int, default=2) <br> - exceptions (Exception or tuple of Exceptions, default=Exception) <br> - backoff_factor (int, default=1) <br> - logger (Logger, optional) | A decorator that retries a function upon failure. You can set the maximum number of retries, the delay between retries, the type of exceptions to catch, and the backoff factor to increase the delay with each retry. If a logger is provided, exceptions are logged. |
| @thread_pool | - num_threads (int, default=4) <br> - exceptions (Exception or tuple of Exceptions, default=Exception) <br> - raise_first_exception (bool, default=False) <br> - logger (Logger, optional)                   | A decorator that runs a function in a thread pool with a specified number of threads. It collects results from all tasks and returns them as a list. It also handles exceptions, with an option to re-raise the first exception or just log it.                        |

## Licence

This project is licensed under the MIT License. See the LICENSE file for more details.