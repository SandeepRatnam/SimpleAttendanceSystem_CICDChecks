import logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Generate log messages
logging.debug("This is a debug message")
logging.info("Attendance calculation started")
logging.warning("Attendance threshold is not configured")
logging.error("Invalid attendance values")
logging.critical("Application encountered a critical problem")