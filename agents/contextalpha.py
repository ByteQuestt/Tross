import sys
import json
import typing 
import execute
from models import llmbase
from agents import utils


class ContextAlpha:

    def __init__(self, Basellm,) -> None:
        self.model = llmbase.Basellm()
        sys.prompt =""



    def functionlist(cls, list : typing.List):
        return list
    

    def execute(cls, list : typing.List[typing.Callable])-> typing.Any:
      result: typing.Dict = {
          
      }
      for i in list:
          result[i.__getattribute__()] = execute(i)

      return result

    def step(cls):
        result = cls.model.getresponse()
        action = cls.model.parse_response(result)
        # if isinstance(action, dict):
        #  outputs = cls.execute(methods, args )
    
    def actions( cls , 
            action:typing.Optional, # type: ignore
            method: typing.Optional, # type: ignore
            args
    ):
       if action == "searchClass":
        output =  cls.execute(utils.searchcls())
        return output

       if action == "searchmethod":
          output = cls.execute(utils.searchmethods())
          return output
    
       if action == "executescript":
          output = cls.execute()
          return output
          