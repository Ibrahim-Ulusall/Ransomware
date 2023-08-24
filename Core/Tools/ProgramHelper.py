import os
import sys
import time

class ProgramHelper:

    @staticmethod
    def ClearTerminal():
        if os.name == 'posix':
            os.system('clear')
        if os.name == 'nt':
            os.system('cls')
        else:
            pass

    @staticmethod
    def Shutdown():
        ProgramHelper.ClearTerminal()
        time.sleep(2)
        print('Bye')
        sys.exit()
    
    @staticmethod
    def GetAllFiles():
        files = list()
        directories = list()
        currentPath = ProgramHelper.GetPath()
       
        for item in os.listdir(currentPath):
            if os.path.isdir(os.path.join(currentPath,item)):
                directories.append(item)
            else:
                files.append(item)

        return directories,files

    @staticmethod
    def GetPath():
        path:str = None
        if os.name != 'nt':
            path = r'/'
        return path

    @staticmethod
    def FileExists(path:str):
        if os.path.exists(path) and os.path.isfile(path):
            return True
        return False
