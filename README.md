# Celestial API Automation

This project interacts with the Celestial API to create and delete celestial objects in a structured and efficient manner.

## Features
- **Modular Design**: Ensures maintainability and scalability.
- **Robust Error Handling**: Includes a retry mechanism with exponential backoff.
- **Versatile Support**: Handles multiple celestial types (Polyanets, Soloons, Comeths).

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/privatechutney/Crossmint_challenge_V2.git
    cd Crossmint_challenge_V2
    ```
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure API**:
    - Add your `CANDIDATE_ID` to `celestial_api/config.py`.

4. **Run the Script**:
    ```bash
    python main.py
    ```

## Directory Structure
- `celestial_api/`:
    - Contains core modules for celestial handling and utilities.
- `main.py`:
    - Entry point for running the program.

## Contact
For any inquiries or support, please contact [cherrytinlatt@gmail.com].