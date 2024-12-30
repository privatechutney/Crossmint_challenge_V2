import requests
import time


def retry_request(request_func, retries=3, delay=2, backoff=2):
    """Retries a request function with exponential backoff."""
    for attempt in range(retries):
        try:
            return request_func()
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= backoff
            else:
                raise
