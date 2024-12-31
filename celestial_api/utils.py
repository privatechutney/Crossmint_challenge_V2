import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

def retry_request(request_func: callable, retries: int = 3, delay: int = 2, backoff: int = 2) -> any:
    """
    Retries a request function with exponential backoff.
    
    :param request_func: The request function to be retried
    :param retries: Number of retry attempts
    :param delay: Initial delay between retries in seconds
    :param backoff: Backoff multiplier
    :return: The result of the request function
    :raises: requests.RequestException if all retries fail
    """
    for attempt in range(retries):
        try:
            return request_func()
        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= backoff
            else:
                raise