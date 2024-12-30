import time
import requests
from celestial_api.config import API_ENDPOINT, CANDIDATE_ID
from celestial_api.exceptions import APIError


class Celestial:
    def __init__(self, celestial_type, row, column):
        self.celestial_type = celestial_type
        self.row = row
        self.column = column

    def create_celestial(self, **kwargs):
        """Creates a celestial object on the map."""
        data = {
            "candidateId": CANDIDATE_ID,
            "row": self.row,
            "column": self.column,
        }
        data.update(kwargs)

        response = requests.post(f"{API_ENDPOINT}{self.celestial_type}", json=data)
        if response.status_code == 200:
            print(f"{self.celestial_type.title()[:-1]} created on ({self.row}, {self.column}).")
        else:
            raise APIError(f"Failed to create {self.celestial_type} at ({self.row}, {self.column}).")

    def delete_celestial(self):
        """Deletes a celestial object from the map."""
        data = {
            "candidateId": CANDIDATE_ID,
            "row": self.row,
            "column": self.column,
        }

        response = requests.delete(f"{API_ENDPOINT}{self.celestial_type}", json=data)
        if response.status_code == 200:
            print(f"{self.celestial_type} deleted on ({self.row}, {self.column}).")
        else:
            raise APIError(f"Failed to delete {self.celestial_type} at ({self.row}, {self.column}).")


class Polyanets(Celestial):
    def __init__(self, row, column):
        super().__init__("polyanets", row, column)


class Soloons(Celestial):
    def __init__(self, row, column, color):
        super().__init__("soloons", row, column)
        self.color = color

    def create(self):
        self.create_celestial(color=self.color)


class Comeths(Celestial):
    def __init__(self, row, column, direction):
        super().__init__("comeths", row, column)
        self.direction = direction

    def create(self):
        self.create_celestial(direction=self.direction)
