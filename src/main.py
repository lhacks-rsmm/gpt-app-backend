import os
import sys
from gpt import GPTContext

def Main():
    if (not("OPENAI_KEY" in os.environ.keys())):
        print("OPENAI_KEY is empty, it must be set to a valid API key.")
        return

    if (len(sys.argv) < 2):
        print("Usage: gpt <prompt>")
        return

    context = GPTContext("user", "gpt-3.5-turbo", os.environ["OPENAI_KEY"])
    
    context.Initialize()
    
    print(context.Prompt(sys.argv[1]))

Main()
