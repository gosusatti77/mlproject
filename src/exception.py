import sys

def error_message_detail(eror, error_detail: sys):
    """
    This function takes an error and its details and returns a formatted string with the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message 


class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException with an error message and its details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the string representation of the CustomException.
        """
        return self.error_message

