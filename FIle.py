import os 
import string
import typing


class File:
    def __init__(self) -> None:
       self.file_index ={}
        # os.listdir("C:\Users\pranav\Desktop\input_data")
       for (root,dir,files) in os.walk("C:\\Users\\pranav\\Desktop\\input_data'",topdown=True):
            for file in files:
             file_path = os.path.join(root,file)
             print(self.file_path)
             self.file_index[file:string] =  file_path 
                
    def filehandler(self):
       for (root,dir,files) in os.walk("C:\\Users\\pranav\\Desktop\\input_data'",topdown=True):
            print(root,dir,files)
            for file in files:
             file_path = os.path.join(root,file)
             print(file_path)
             self.file_index[file:string] =  file_path 
                
f = File()
print(f.filehandler())
