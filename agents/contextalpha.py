import sys
import json
import typing 
import execute

class ContextAlpha:

    def __init__(self, model,) -> None:
        self.model = model
        sys.prompt =""


    def functionlist( list : typing.List):
        return list
    

    def execute( list : typing.List[typing.Callable])-> typing.Any:
      result: typing.Dict = {
          
      }
      for i in list:
          result[i.__getattribute__()] = execute(i)
          
          