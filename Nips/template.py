from typing import Any, List, Dict
import os

class FolderTemplate :
    
    def __init__(self, filepath , llm_response) -> None:
    #    path of the files
     files : Dict={}

     for i in range(files):
         os.makedirs("key", exist_ok=True)
         with os.path.join("client", "client.js") as cl:
           cl.write("Queried response")
      
      