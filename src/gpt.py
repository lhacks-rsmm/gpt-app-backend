import openai

class GPTMessage:
    def __init__(self, role: str, content: str):
        self.Role = role
        self.Content = content
    def ToDict(self) -> dict[str, str]:
        return dict({ "role": self.Role, "content": self.Content })
 
class GPTContext:
    def __init__(self, role: str, model: str, apiKey: str):
        self.Role = role
        self.Model = model
        self.APIKey = apiKey

    def Initialize(self) -> bool:
        openai.api_key = self.APIKey
        return True

    def Prompt(self, message: str) -> str:
        return openai.ChatCompletion.create(model=self.Model, messages=[GPTMessage(self.Role, message).ToDict()]).choices[0].message["content"]
    


