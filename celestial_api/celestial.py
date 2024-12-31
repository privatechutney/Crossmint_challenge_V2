import logging
import requests
from celestial_api.config import API_ENDPOINT, CANDIDATE_ID
from celestial_api.exceptions import APIError

logging.basicConfig(level=logging.INFO)

class Celestial:
    def __init__(self, celestial_type, row, column):
        """
        Initialize a celestial object.
        
        :param celestial_type: Type of the celestial object (polyanets, soloons, comeths)
        :param row: Row position on the map
        :param column: Column position on the map
        """
        self.celestial_type = celestial_type
        self.row = row
        self.column = column

    def _prepare_data(self, **kwargs):
        """
        Prepare the data payload for API requests.
        
        :param kwargs: Additional data to include in the payload
        :return: Data payload dictionary
        """
        data = {
            "candidateId": CANDIDATE_ID,
            "row": self.row,
            "column": self.column,
        }
        data.update(kwargs)
        return data

    def _send_request(self, method, data):
        """
        Send an API request to create or delete a celestial object.
        
        :param method: HTTP method ('POST' or 'DELETE')
        :param data: Data payload for the request
        :raises APIError: If the request fails
        """
        url = f"{API_ENDPOINT}{self.celestial_type}"
        if method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, json=data)
        if response.status_code == 200:
            logging.info(f"{self.celestial_type.title()[:-1]} operation succeeded on ({self.row}, {self.column}).")
        else:
            raise APIError(f"Failed to {method.lower()} {self.celestial_type} at ({self.row}, {self.column}).")

    def create_celestial(self, **kwargs):
        """
        Creates a celestial object on the map.
        
        :param kwargs: Additional data to include in the creation payload
        """
        data = self._prepare_data(**kwargs)
        self._send_request('POST', data)

    def delete_celestial(self):
        """
        Deletes a celestial object from the map.
        """
        data = self._prepare_data()
        self._send_request('DELETE', data)

class Polyanets(Celestial):
    def __init__(self, row, column):
        """
        Initialize a Polyanet object.
        
        :param row: Row position on the map
        :param column: Column position on the map
        """
        super().__init__("polyanets", row, column)

class Soloons(Celestial):
    def __init__(self, row, column, color):
        """
        Initialize a Soloon object.
        
        :param row: Row position on the map
        :param column: Column position on the map
        :param color: Color of the Soloon
        """
        super().__init__("soloons", row, column)
        self.color = color

    def create(self):
        """
        Creates a Soloon object on the map.
        """
        self.create_celestial(color=self.color)

class Comeths(Celestial):
    def __init__(self, row, column, direction):
        """
        Initialize a Cometh object.
        
        :param row: Row position on the map
        :param column: Column position on the map
        :param direction: Direction of the Cometh
        """
        super().__init__("comeths", row, column)
        self.direction = direction

    def create(self):
        """
        Creates a Cometh object on the map.
        """
        self.create_celestial(direction=self.direction)