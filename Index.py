import typing import List,Any ,string # type: ignore
import re
import os


class Index:
    def _init_(code : String):
        tokenized_code: List = []
        for i in code:
           r = tokenize(i)
           tokenized_code(r)

    def build_maps(tokenized_code :List[String], source_repopath): 
        with open(source_repopath) as f2:
          result :List[string] =  f2.readlines()
          trigram_result = trigram(result)
        return 0
       
         
    def keyword_search(tokens:List ):
    #    pattern = regex patterns
     
     