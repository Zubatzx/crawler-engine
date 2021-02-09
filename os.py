import os
import platform

class Os:
    main_dir = ""

    def __init__(self):
        operating_system = platform.system().lower()

        if operating_system == "linux":
            self.main_dir = "/home/" + os.getlogin()
        elif operating_system == "windows":
            self.main_dir = "C:\\Users\\" + os.getlogin()

    def GetMainDirectory(self):
        print('Main directory: ' + self.main_dir)
        return self.main_dir

    def GetListDirectory(self, dir):
        print('Files in directory ' + self.main_dir + ': ')
        for entry in os.listdir(dir):
            print(entry)
        return os.listdir(dir)

    def DeleteFile(self, dir):
        if os.path.isfile(dir):
            print('Deleting file: ' + dir)
            os.remove(dir)
        else:
            print('Error Deleting file: ' + dir + ' is not a valid filename')

    def EmptyFolder(self, dir):
        for entry in os.listdir(dir):
            entry_path = dir + '/' + entry
            if os.path.isfile(entry_path):
                print('Deleting file: ' + entry_path)
                os.remove(entry_path)
            # logic untuk hapus directory kedepannya (pakai shutil.rmtree())