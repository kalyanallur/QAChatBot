import sys
def create_error_message(error_message):
    _,_,exctb = sys.exc_info()
    filename = exctb.tb_frame.f_code.co_filename
    line = exctb.tb_lineno
    error_message = f"Exception occured within the file named {filename}, line number {line}, error description: {error_message}"
    return error_message

class CustomExceptions(Exception):
    def __init__(self, error_message) :
        super().__init__(error_message)
        self.error_message = create_error_message(error_message)

    def __str__(self) :
        return self.error_message
    

