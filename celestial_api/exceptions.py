class APIError(Exception):
    """
    Custom exception for API errors.
    
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="An error occurred with the API."):
        self.message = message
        super().__init__(self.message)