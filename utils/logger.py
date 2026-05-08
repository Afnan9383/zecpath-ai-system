from loguru import logger

logger.add(
    "logs/zecpath_ai.log",
    rotation="1 MB",
    retention="7 days",
    level="INFO"
)

def get_logger():
    return logger
