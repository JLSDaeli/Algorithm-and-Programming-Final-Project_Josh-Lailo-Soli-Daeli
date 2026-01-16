# import logging module in Python's built-in type
import logging

# Shape the global logging settings.
# The level turned in logging.info that logs info, warning, error, and critical messages.
# Format clarifies the process of diplaying log messages
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# form and recover a logger instance for applications of the calculator system
# The logger can be collected and used functionally in other files.
logger = logging.getLogger("TimeCalculatorLogger")
