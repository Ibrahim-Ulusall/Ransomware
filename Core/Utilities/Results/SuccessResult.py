from .Result import Result

class SuccessResult(Result):
    
    def __init__(self,message:str = None):
        super().__init__(message,True)
