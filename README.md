# Infranchise

Intelligent Enfranchisement


## Figuring out your political views

Tried multiple quizzes and the like. this seems like the best one in terms of brevity:insight ratio.

https://www.theadvocates.org/quiz/

but it's overfocused on certain areas.


## what it sorta does

1. get more info about your political beliefs
![image](https://github.com/paulkarayan/sufferingsuffrage/assets/97910476/4578fde9-2e7a-4250-bd54-786c59b92e33)

2. 
based on this, i ask it to talk about my voting. for example, what would it do on these ballot measures? 
https://calmatters.org/explainers/california-ballot-measures-2022/

output:
```
Proposition 14: Borrowing $5.5 billion for Stem Cell Research: 
I think you would care a lot about this proposition and would likely vote yes. You value individual liberty and value the freedom to make one's own decisions, which supports the idea that research should be funded and people should be allowed to make their own decisions about scientific research. This proposition is also in line with your belief that government should not censor speech, press, media or internet, as it involves the funding of scientific research. I estimate there is a 90% likelihood that you would vote yes on this proposition. 

Proposition 15: Increasing Taxes on Large Businesses to Fund Public Schools: 
I think you would care moderately about this proposition and would likely vote no. You believe in limited government intervention and reducing taxes and government spending by 50% or more. This proposition would increase taxes on large businesses to fund public schools, which goes against your core libertarian beliefs. I estimate there is a 75% likelihood you would vote no on this proposition.
```
etc..

## running this

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000


curl -d "question1=agree&question2=disagree" -X POST http://localhost:8000/submit

curl -X POST "http://localhost:8000/submit" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"speech\":\"agree\",\"military\":\"disagree\",\"sex\":\"agree\",\"drugs\":\"disagree\",\"immigration\":\"maybe\",\"loans\":\"disagree\",\"healthcare\":\"maybe\",\"retirement\":\"agree\",\"welfare\":\"disagree\",\"taxes\":\"agree\",\"politicalView\":\"libertarian\"}"
