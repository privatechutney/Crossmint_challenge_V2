import time
import requests
from celestial_api.celestial import Polyanets, Soloons, Comeths
from celestial_api.utils import retry_request
import logging

logging.basicConfig(level=logging.INFO)

def get_goal_map():
    """
    Fetches the goal map from the API.
    """
    from celestial_api.config import API_ENDPOINT, CANDIDATE_ID

    def fetch():
        response = requests.get(f"{API_ENDPOINT}map/{CANDIDATE_ID}/goal")
        response.raise_for_status()
        return response.json()["goal"]

    return retry_request(fetch)

def create_celestial_object(celestial_class, *args):
    """
    Creates a celestial object with retry logic.
    
    :param celestial_class: The class of the celestial object (Polyanets, Soloons, Comeths)
    :param args: Arguments required for the celestial object creation
    """
    retry_request(lambda: celestial_class(*args).create_celestial())
    time.sleep(1)

def phase_1():
    """
    Execute phase 1 of celestial creation.
    """
    dec = 8
    for cr in range(2, 9):
        create_celestial_object(Polyanets, cr, cr)
        create_celestial_object(Polyanets, cr, dec)
        dec -= 1

def phase_2():
    """
    Execute phase 2 of celestial creation based on the goal map.
    """
    goal_map = get_goal_map()
    rows, columns = len(goal_map), len(goal_map[0])
    
    for r in range(rows):
        for c in range(columns):
            cell = goal_map[r][c]
            if cell == "POLYANET":
                create_celestial_object(Polyanets, r, c)
            elif "SOLOON" in cell:
                color = cell[:-7].lower()
                create_celestial_object(Soloons, r, c, color)
            elif "COMETH" in cell:
                direction = cell[:-7].lower()
                create_celestial_object(Comeths, r, c, direction)