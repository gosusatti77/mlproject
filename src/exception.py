import sys

def error_message_detail(error):
    """
    This function takes an error and returns a formatted string with its details.
    """
    exc_type, exc_value, exc_tb = sys.exc_info()  # Get exception details
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
    
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    """
    def __init__(self, error_message):
        """
        Initializes the CustomException with an error message.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        """
        Returns the string representation of the CustomException.
        """
        return self.error_message

