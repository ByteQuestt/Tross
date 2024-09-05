import typing


# def execute( fn : typing.Callable, args : str):
#     pass


def hello():
     return "hello"

def done():
     print("done")
     return "done"


def execute( list : typing.List[typing.Callable]):
      for fn in list:
          result = fn()
          print(result)

fn_list: typing.List[typing.Callable] =[hello,done]


execute(fn_list)