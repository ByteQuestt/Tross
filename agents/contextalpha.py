import sys
import json
import typing 
import execute
from models import llmbase
class ContextAlpha:

    def __init__(self, Basellm,) -> None:
        self.model = Basellm()
        sys.prompt =""



    def functionlist(self, list : typing.List):
        return list
    

    def execute(self, list : typing.List[typing.Callable])-> typing.Any:
      result: typing.Dict = {
          
      }
      for i in list:
          result[i.__getattribute__()] = execute(i)

    def step():
        
          