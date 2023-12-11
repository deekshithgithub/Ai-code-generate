from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Type

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

import instructor

open_ai_client = OpenAI(
    api_key=openai_api_key,
)

instructor.patch(open_ai_client)

def code_generator(openai_model, prompt, custom_model: Type[BaseModel]):
    result = open_ai_client.chat.completions.create(
        model=openai_model,
        response_model=custom_model,
        messages=[{"role": "user", "content": f"{prompt}, output must be in plain text, not in json string"}]
    )
    return result
