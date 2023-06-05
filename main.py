import os
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import openai



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

    print(background_prompt)

    thing_to_evaluate = """
    on the 2022 california ballot measures here: 
    https://calmatters.org/explainers/california-ballot-measures-2022/ 
    please rank how much you think i would care, tell me what you think i'd vote
    and why you think i'd vote that way 
    and give an estimated % likelihood that your voting suggestion is accurate. 
    separate the responses with new lines"""

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





