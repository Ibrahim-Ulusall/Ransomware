from Core.Constants.Messages import Messages
from Core.Utilities.Results.IDataResult import IDataResult
from Core.Utilities.Results.ErrorDataResult import ErrorDataResult
from Core.Utilities.Results.SuccessDataResult import  SuccessDataResult


class FileHelper:

    @staticmethod
    def Writer(filename:str,context:str = None) -> IDataResult:
        try:
            with open(filename,'wb') as file:
                file.write(context)
        except FileNotFoundError as err:
            return ErrorDataResult(message = Messages.Error.FileNotFoundErr)
        except Exception as e:
            return ErrorDataResult(message=e)
        return SuccessDataResult(message = Messages.Successfull.SaveSuccessfull)

    @staticmethod
    def Reader(filename:str) -> IDataResult:
        try:
            with open(filename,'rb') as file:
                context = file.read()
        except FileNotFoundError:
            return ErrorDataResult(message = Messages.Error.FileNotFoundErr)
        except Exception as e:
            return ErrorDataResult(message = e)
        return SuccessDataResult(data = context)
