import os

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated
from gpt import GPTContext

Context = GPTContext("user", "gpt-3.5-turbo", os.environ["OPENAI_KEY"])

Context.Initialize()

app = FastAPI()

class Prompt(BaseModel):
    Message: str
 
async def GetContext() -> GPTContext:
    return Context


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/Prompt")
async def prompt(message: Prompt, context: Annotated[GPTContext, Depends(GetContext)]):
    return context.Prompt(message.Message)

