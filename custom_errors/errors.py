class CustomError(Exception):
    """Interface for custom errors"""

class WrongFileFormat(CustomError):
    """Raised when file format is not correct"""