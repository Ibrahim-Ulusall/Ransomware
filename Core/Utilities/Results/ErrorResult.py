from .Result import Result

class ErrorResult(Result):
    
    def __init__(self,message:str = None):
        super().__init__(message,False)
