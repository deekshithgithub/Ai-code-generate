from pydantic import BaseModel
from typing import List
from helpers import code_generator

class GeneratedCode(BaseModel):
    code: str

input_text = ""
prompt = f"I want you to act as a expert code generator in all programming languages. Think of code is beginner friendly and easy to understand at the same time,and will provide comments to understand the code.You should ready to generate code based on the user reqirement.Try to come up with each details of the code which you are generating.you have knowledge about writing code to achieve specific tasks, you can write code in every programming language. Now your task is [Generate a code based on user requirement {input_text}, You have to Analyze this topice and Generate code step by step]"

openai_model = "gpt-3.5-turbo"

result = code_generator(openai_model, prompt, GeneratedCode)
print("Generated Code:")
print(result.code)
