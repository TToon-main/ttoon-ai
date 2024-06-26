from openai import OpenAI
from configs import gpt_config


class Prompt():
    def __init__(self, model) -> None:
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

    def set_model(self):
        response = openai.chat.completions.create(
            model = self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer

    def generate_image(self, story):
        assistant = self.set_model()
        story = self, story
        self.message.append(
            {
                "role": "user",
                "content": self.story
            }
        )
        response = openai.chat.completions.create(
            model = self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer