import time
from functools import wraps
from logging import Logger
from typing import Any


def retry(max_retries=3, delay=2, exceptions=Exception, backoff_factor=1, logger: Logger = None) -> Any:
    """
    A decorator that retries a function upon failure.

    This decorator wraps a function and retries it upon failure. The number of retries, delay between retries,
    type of exceptions to catch, and the backoff factor for the delay can be customized. If a logger is provided,
    exceptions are logged.

    Args:
        max_retries (int, optional): The maximum number of retries. Defaults to 3.
        delay (int, optional): The initial delay between retries in seconds. Defaults to 2.
        exceptions (Exception, optional): The type of exceptions to catch. Defaults to Exception.
        backoff_factor (int, optional): The factor by which the delay should increase after each retry. Defaults to 1.
        logger (Logger, optional): The logger to use for logging exceptions. Defaults to None.

    Returns:
        Any: The result of the decorated function, or None if it failed after all retries.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    wait_time = delay * (backoff_factor ** attempt)
                    if logger is not None:
                        logger.exception(f"Exception occurred: {error}, retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
            return None

        return wrapper

    return decorator
