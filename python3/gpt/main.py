import openai
import neovim

openai.api_key = 'your-api-key'

def ask_gpt3(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

class Main(object):
    def __init__(self, vim):
        self.vim = vim

    def ask_gpt3_vim(self, args):
        question = args[0]
        response = ask_gpt3(question)
        self.vim.current.buffer.append(response)

