import openai
import sys, os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from configs import gpt_config

class Prompt():
    def __init__(self) -> None:
        openai.api_key = gpt_config.API_KEY

        self.model = gpt_config.GPT_MODEL
        
        self.message = [
        {
            "role" : "system",
            "content" : gpt_config.SYSTEM
        },
        {
            "role": "user",
            "content": gpt_config.USER1
        },
        {
                "role": "assistant",
                "content": gpt_config.ASSISTANT1
        },
        {
            "role": "user",
            "content": gpt_config.USER2
        },
        {
                "role": "assistant",
                "content":gpt_config. ASSISTANT2
        },
        {
            "role": "user",
            "content": gpt_config.USER3
        },
        {
                "role": "assistant",
                "content": gpt_config.ASSISTANT3
        }
        ]

    def generate_prompt(self, story):
        self.message.append(
            {
                "role": "user",
                "content": story
            }
        )
        response = openai.chat.completions.create(
            model = self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer