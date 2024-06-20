from openai import OpenAI
import configs

class Prompt():
    def __init__(self, model, story) -> None:
        self.model = configs.GPT_MODEL
        self.story = story

        self.message = [
        {
            "role" : "system",
            "content" : configs.SYSTEM
        },
        {
            "role": "user",
            "content": configs.USER1
        },
        {
                "role": "assistant",
                "content": configs.ASSISTANT1
        },
        {
            "role": "user",
            "content": configs.USER2
        },
        {
                "role": "assistant",
                "content":configs. ASSISTANT2
        },
        {
            "role": "user",
            "content": configs.USER3
        },
        {
                "role": "assistant",
                "content": configs.ASSISTANT3
        }
        ]

    def set_model(self):
        response = openai.chat.completions.create(
            model=self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer

    def generate(self):
        assistant = self.set_model()
        self.message.append(
            {
                "role": "user",
                "content": self.story
            }
        )
        response = openai.chat.completions.create(
            model=self.model,
            messages = self.message
            )

        answer = response.choices[0].message.content
        return answer