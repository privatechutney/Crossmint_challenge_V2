# Celestial API Automation

This project interacts with the Celestial API to create and delete celestial objects.

## Features
- Modular design for maintainability.
- Retry mechanism with exponential backoff for robust error handling.
- Support for multiple celestial types (Polyanets, Soloons, Comeths).

## Setup Instructions
1. Clone this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your `CANDIDATE_ID` to `celestial_api/config.py`.
4. Run the script:
    ```bash
    python main.py
    ```

## Directory Structure
- `celestial_api/`: Contains core modules for celestial handling and utilities.
- `main.py`: Entry point for running the program.
