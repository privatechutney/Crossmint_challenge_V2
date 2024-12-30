import time
import requests
from celestial_api.celestial import Polyanets, Soloons, Comeths
from celestial_api.utils import retry_request


def get_goal_map():
    """Fetches the goal map from the API."""
    from celestial_api.config import API_ENDPOINT, CANDIDATE_ID

    def fetch():
        response = requests.get(f"{API_ENDPOINT}map/{CANDIDATE_ID}/goal")
        response.raise_for_status()
        return response.json()["goal"]

    return retry_request(fetch)


def phase_1():
    dec = 8
    for cr in range(2, 9):
        retry_request(lambda: Polyanets(cr, cr).create_celestial())
        time.sleep(1)
        retry_request(lambda: Polyanets(cr, dec).create_celestial())
        dec -= 1
        time.sleep(1)


def phase_2():
    goal_map = get_goal_map()
    rows, columns = len(goal_map), len(goal_map[0])

    for r in range(rows):
        for c in range(columns):
            if goal_map[r][c] == "POLYANET":
                retry_request(lambda: Polyanets(r, c).create_celestial())
            elif "SOLOON" in goal_map[r][c]:
                color = goal_map[r][c][:-7].lower()
                retry_request(lambda: Soloons(r, c, color).create())
            elif "COMETH" in goal_map[r][c]:
                direction = goal_map[r][c][:-7].lower()
                retry_request(lambda: Comeths(r, c, direction).create())
