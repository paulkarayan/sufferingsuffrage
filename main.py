from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import openai
import os


# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)


app = FastAPI()


openai.api_key = os.getenv("OPENAI_API_KEY")


# Add CORS middleware to allow all origins, and expose necessary headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuizResponse(BaseModel):
    speech: Optional[str]
    military: Optional[str]
    sex: Optional[str]
    drugs: Optional[str]
    immigration: Optional[str]
    loans: Optional[str]
    healthcare: Optional[str]
    retirement: Optional[str]
    welfare: Optional[str]
    taxes: Optional[str]
    politicalView: Optional[str]

@app.post("/submit")
async def submit(quiz_response: QuizResponse):
    print(quiz_response, type(quiz_response))

    background_prompt = f"""
    I am an american voter.

    I believe that
    {quiz_response.politicalView}
    best reflects my political views.

    I {quiz_response.speech}
    Government should not censor speech, press, media or internet


    I {quiz_response.military} 
    Military service should be voluntary. There should be no draft


    I {quiz_response.sex}  
    There should be no laws regarding sex between consenting adults


    I {quiz_response.drugs} we should
    Repeal laws prohibiting adult possession and use of drugs


    I {quiz_response.immigration}
    Government should not target, detain, and deport undocumented workers


    I {quiz_response.loans}
    Taxpayers should NOT be responsible for student loan debt


    I {quiz_response.healthcare} 
    Government should not be responsible for providing healthcare


    I {quiz_response.retirement}  we should
    Let people control their own retirement; privatize Social Security


    I {quiz_response.welfare}  we should
    Replace government welfare with private charity


    I {quiz_response.taxes} we should
    Cut taxes and government spending by 50% or more
    \n
    """


    legislation_prompt = """
https://ballotpedia.org/California_Proposition_1,_Right_to_Reproductive_Freedom_Amendment_(2022)
    """

    thing_to_evaluate = f"""
    on the legislation described here: 
    {legislation_prompt}
    1. if it is a url, use the web browser plugin to get the text of the legislation. 
       otherwise use the text provided
    2. describe the legislation in 1 sentence including its name,
    3. rank how much you think i would care
    4. tell me what you think i'd vote
    5. tell me why you think i'd vote that way 
    6. give an estimated percent likelihood that your voting suggestion is accurate. 
    separate the responses with new lines"""

    print(background_prompt + thing_to_evaluate)


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=background_prompt + thing_to_evaluate,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    logging.info(f"ChatGPT API response: {response}")
    
    print(response)
    print(type(response))

    # Extract and return generated text
    generated_text =  response["choices"][0]["text"]
    print(generated_text)
    return {"generated_text": generated_text}





