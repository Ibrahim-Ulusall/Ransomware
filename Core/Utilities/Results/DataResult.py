from .Result import Result
from .IDataResult import IDataResult

class DataResult(Result,IDataResult):

    def __init__(self,message:str,success:bool,data:object):
        self.Data = data
        super().__init__(message,success)
