import os
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
    q1: str
    q1_1: Optional[str]
    q2: str
    q3: str
    q4: str
    q5: str
    q5_1: Optional[str]
    q6: str
    q7: str
    q8_1: str
    q8_2: str
    q9: str
    q10_1: str
    q10_2: str
    q11: str
    q12: str
    q13: str
    q14: str
    q15: str
    q16: str


# Questions from the Pew Research Center Political Typology Quiz:

#Q1: If you had to choose, would you rather have…
#A1: A smaller government providing fewer services
#A2: A bigger government providing more services
#Q1.1 (for A2): When you say you favor a bigger government providing more services, do you think it would be better to...
#A1: Modestly expand on current government services
#A2: Greatly expand on current government services

#Q2: Which of the following statements come closest to your view?
#A1: America’s openness to people from all over the world is essential to who we are as a nation
#A2: If America is too open to people from all over the world, we risk losing our identity as a nation

#Q3: In general, would you say experts who study a subject for many years are… 
#A1: Usually BETTER at making good policy decisions about that subject than other people
#A2: Usually WORSE at making good policy decisions about that subject than other people 
#A3: NEITHER BETTER NOR WORSE at making good policy decisions about that subject than other people

#Q4: Thinking about increased trade of goods and services between the U.S. and other nations in recent decades, would you say that the U.S. has...
#A1: Gained more than it has lost because increased trade has helped lower prices and increased the competitiveness of some U.S. businesses
#A2: Lost more than it has gained because increased trade has cost jobs in manufacturing and other industries and lowered wages for some U.S. workers

#Q5: How much more, if anything, needs to be done to ensure equal rights for all Americans regardless of their racial or ethnic backgrounds?
#A1: A lot
#A2: A little
#A3: Nothing at all
#Q5.1 (for A1): Which comes closer to your view about what needs to be done to ensure equal rights for all Americans regardless of their racial or ethnic backgrounds -- even if neither is exactly right?
#A1: Most U.S. laws and major institutions need to be completely rebuilt because they are fundamentally biased against some racial and ethnic groups
#A2: While there are many inequities in U.S. laws and institutions, necessary changes can be made by working within the current systems

#Q6: Which of the following statements comes closest to your view?
#A1: Business corporations make too much profit
#A2: Most corporations make a fair and reasonable amount of profit

#Q7: How much, if at all, would it bother you to regularly hear people speak a language other than English in public places in your community?
#A1: A lot
#A2: Some
#A3: Not much
#A4: Not at all

#Q8: On a scale of 0 to 100, where 0 means you feel as cold and negative as possible and 100 means you feel as warm and positive as possible, how do you feel toward... 
#Q8.1: How do you feel toward Democrats?
#A1: 0-100
#Q8.2: How do you feel toward Republicans?
#A1: 0-100

#Q9: Which of these statements best describes your opinion about the United States?
#A1: The U.S. stands above all other countries in the world
#A2: The U.S. is one of the greatest countries in the world, along with some others
#A3: There are other countries that are better than the U.S.

#Q10: How much of a problem, if any, would you say each of the following are in the country today? 
#Q10.1: People being too easily offended by things others say
#A1: Major problem
#A2: Minor problem
#A3: Not a problem
#Q10.2: People saying things that are very offensive to others
#A1: Major problem
#A2: Minor problem
#A3: Not a problem

#Q11: Which comes closer to your view of candidates for political office, even if neither is exactly right? I usually feel like...
#A1: There is at least one candidate who shares most of my views 
#A2: None of the candidates represent my views well

#Q12: In general, how much do White people benefit from advantages in society that Black people do not have? 
#A1: A great deal
#A2: A fair amount
#A3: Not too much
#A4: Not at all

#Q13: Do you think greater social acceptance of people who are transgender (people who identify as a gender that is different from the sex they were assigned at birth) is…
#A1: Very good for society
#A2: Somewhat good for society
#A3: Neither good nor bad for society
#A4: Somewhat bad for society
#A5: Very bad for society

#Q14: Overall, would you say people who are convicted of crimes in this country serve…
#A1: Too much time in prison
#A2: Too little time in prison
#A3: About the right amount of time in prison

#Q15: Which of the following statements comes closest to your view?
#A1: Religion should be kept separate from government policies
#A2: Government policies should support religious values and beliefs

#Q16: In the future, do you think...
#A1: U.S. policies should try to keep it so America is the only military superpower
#A2: It would be acceptable if another country became as militarily powerful as the U.S.

@app.post("/submit")
async def submit(quiz_response: QuizResponse):
    print(quiz_response, type(quiz_response))

    question1 = "If I had to choose, I would rather have "
    question1_1 = ""
    answer1_1 = ""
    if quiz_response.q1 == "1":
        answer1 = "a smaller government providing fewer services."
    elif quiz_response.q1 == "2":
        answer1 = "a bigger government providing more services."
        question1_1 = " When I say I favor a bigger government providing more services, I think it would be better to "
        if quiz_response.q1_1 == "1":
            answer1_1 = "modestly expand on current government services."
        if quiz_response.q1_1 == "2":
            answer1_1 = "greatly expand on current government services."

    question2 = "My view is that "
    if quiz_response.q2 == "1":
        answer2 = "America’s openness to people from all over the world is essential to who we are as a nation."
    elif quiz_response.q2 == "2":
        answer2 = "if America is too open to people from all over the world, we risk losing our identity as a nation."

    question3 = "In general, I would say that experts who study a subject for many years are "
    if quiz_response.q3 == "1":
        answer3 = "Usually BETTER at making good policy decisions about that subject than other people."
    if quiz_response.q3 == "2":
        answer3 = "Usually WORSE at making good policy decisions about that subject than other people."
    if quiz_response.q3 == "3":
        answer3 = "NEITHER BETTER NOR WORSE at making good policy decisions about that subject than other people."

    question4 = "Thinking about increased trade of goods and services between the U.S. and other nations in recent decades, I would say that the U.S. has "
    if quiz_response.q4 == "1":
        answer4 = "gained more than it has lost because increased trade has helped lower prices and increased the competitiveness of some U.S. businesses."
    elif quiz_response.q4 == "2":
        answer4 = "lost more than it has gained because increased trade has cost jobs in manufacturing and other industries and lowered wages for some U.S. workers."

    answer5_1 = ""
    if quiz_response.q5 == "1":
        answer5 = "a lot more"
        if quiz_response.q5_1 == "1":
            answer5_1 = "Most U.S. laws and major institutions need to be completely rebuilt because they are fundamentally biased against some racial and ethnic groups."
        elif quiz_response.q5_1 == "2":
            answer5_1 = "While there are many inequities in U.S. laws and institutions, necessary changes can be made by working within the current systems."
    if quiz_response.q5 == "2":
        answer5 = "a little more"
    if quiz_response.q5 == "3":
        answer5 = "nothing at all"
    question5 = f"""I believe that {answer5} needs to be done to ensure equal rights for all Americans regardless of their racial or ethnic backgrounds."""

    question6 = "It's my view that "
    if quiz_response.q6 == "1":
        answer6 = "business corporations make too much profit."
    elif quiz_response.q6 == "2":
        answer6 = "most corporations make a fair and reasonable amount of profit."

    if quiz_response.q7 == "1":
        answer7 = "a lot"
    elif quiz_response.q7 == "2":
        answer7 = "some"
    elif quiz_response.q7 == "3":
        answer7 = "not much"
    elif quiz_response.q7 == "4":
        answer7 = "not at all"
    question7 = f"""It bothers me {answer7} to regularly hear people speak a language other than English in public places in my community."""

    question8_1 = f"""On a scale of 0 to 100, where 0 means I feel as cold and negative as possible and 100 means I feel as warm and positive as possible, I feel {quiz_response.q8_1} towards Democrats."""
    question8_2 = f"""On a scale of 0 to 100, where 0 means I feel as cold and negative as possible and 100 means I feel as warm and positive as possible, I feel {quiz_response.q8_2} towards Republicans."""

    question9 = "In my opinion "
    if quiz_response.q9 == "1":
        answer9 = "the U.S. stands above all other countries in the world."
    elif quiz_response.q9 == "2":
        answer9 = "the U.S. is one of the greatest countries in the world, along with some others."
    elif quiz_response.q9 == "3":
        answer9 = "there are other countries that are better than the U.S."

    question10_1 = "I believe that people being too easily offended by things others say is "
    if quiz_response.q10_1 == "1":
        answer10_1 = "major problem."
    if quiz_response.q10_1 == "2":
        answer10_1 = "minor problem."
    if quiz_response.q10_1 == "3":
        answer10_1 = "not a problem."

    question10_2 = "I believe that people saying things that are very offensive to others is "
    if quiz_response.q10_2 == "1":
        answer10_2 = "major problem."
    if quiz_response.q10_2 == "2":
        answer10_2 = "minor problem."
    if quiz_response.q10_2 == "3":
        answer10_2 = "not a problem."

    question11 = "I usually feel like "
    if quiz_response.q11 == "1":
        answer11 = "there is at least one candidate who shares most of my views."
    elif quiz_response.q11 == "2":
        answer11 = "none of the candidates represent my views well."

    if quiz_response.q12 == "1":
        question12 = "I believe that in general White people benefit a great deal from advantages in society that Black people do not have."
    elif quiz_response.q12 == "2":
        question12 = "I believe that in general White people benefit a fair amount from advantages in society that Black people do not have."
    elif quiz_response.q12 == "3":
        question12 = "I believe that in general White people do not benefit too much from advantages in society that Black people do not have."
    elif quiz_response.q12 == "4":
        question12 = "I believe that in general White people do not benefit at all from advantages in society that Black people do not have."

    question13 = "I think greater social acceptance of people who are transgender (people who identify as a gender that is different from the sex they were assigned at birth) is "
    if quiz_response.q13 == "1":
        answer13 = "very good for society."
    elif quiz_response.q13 == "2":
        answer13 = "somewhat good for society."
    elif quiz_response.q13 == "3":
        answer13 = "neither good nor bad for society."
    elif quiz_response.q13 == "4":
        answer13 = "somewhat bad for society."
    elif quiz_response.q13 == "5":
        answer13 = "very bad for society."

    question14 = "Overall, I would say people who are convicted of crimes in this country serve "
    if quiz_response.q14 == "1":
        answer14 = "too much time in prison."
    if quiz_response.q14 == "2":
        answer14 = "too little time in prison."
    if quiz_response.q14 == "3":
        answer14 = "about the right amount of time in prison."

    question15 = "It is my view that "
    if quiz_response.q15 == "1":
        answer15 = "religion should be kept separate from government policies."
    elif quiz_response.q15 == "2":
        answer15 = "government policies should support religious values and beliefs."

    question16 = "In the future, I think "
    if quiz_response.q16 == "1":
        answer16 = "U.S. policies should try to keep it so America is the only military superpower."
    elif quiz_response.q16 == "2":
        answer16 = "it would be acceptable if another country became as militarily powerful as the U.S."

    background_prompt = f"""
    I am an american voter.

    {question1}{answer1}{question1_1}{answer1_1}

    {question2}{answer2}

    {question3}{answer3}

    {question4}{answer4}

    {question5} {answer5_1}

    {question6}{answer6}

    {question7}

    {question8_1}

    {question8_2}

    {question9}{answer9}

    {question10_1}{answer10_1}

    {question10_2}{answer10_2}

    {question11}{answer11}

    {question12}

    {question13}{answer13}

    {question14}{answer14}

    {question15}{answer15}

    {question16}{answer16}
    """


    legislation_prompt = """
https://ballotpedia.org/California_Proposition_1,_Right_to_Reproductive_Freedom_Amendment_(2022)
    """

    thing_to_evaluate = f"""
    On the legislation described here: 
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





