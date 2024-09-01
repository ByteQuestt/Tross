from typing import (
            List,
            Sequence,
            Dict,
            Tuple,
            Callable,
            Optional
            )
  
import json


class Basellm():

    def __init__(self, config: Optional[Dict]) -> None:
        pass

    def getresponse(self, prompt:Optional[str]):
        response = self.llm.completion(
            messages=[message.model_dump() for message in messages],
            temperature=0.0,
            stop=[')```', ')\n```'],
        )

    def parse_response(self, response) -> str:
        action_str = response['choices'][0]['message']['content']
        if action_str is None:
            return ''
        action_str = action_str.strip()
        if not action_str.endswith('```'):
            action_str = action_str + ')```'
        logger.info(action_str)
        return action_str