from celestial_api.phases import phase_1, phase_2
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to run the phases.
    """
    logging.info("Running Phase 1:")
    try:
        phase_1()
    except Exception as e:
        logging.error(f"An error occurred during Phase 1: {e}")

    logging.info("Running Phase 2:")
    try:
        phase_2()
    except Exception as e:
        logging.error(f"An error occurred during Phase 2: {e}")

if __name__ == "__main__":
    main()