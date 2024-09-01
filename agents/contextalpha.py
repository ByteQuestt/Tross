import sys
import json
import typing 
import execute
from models import llmbase


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
        methods :list = cls.model.parse_response(result)
        if isinstance(methods, list):
         outputs = cls.execute(methods)

          