# Suffering Suffrage

Make sure you say it like Looney Toons!

# Infranchise

Intelligent Enfranchisement


## Figuring out your political views

Tried multiple quizzes and the like. this seems like the best one in terms of brevity:insight ratio.

https://www.theadvocates.org/quiz/


## running this

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000


curl -d "question1=agree&question2=disagree" -X POST http://localhost:8000/submit

curl -X POST "http://localhost:8000/submit" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"speech\":\"agree\",\"military\":\"disagree\",\"sex\":\"agree\",\"drugs\":\"disagree\",\"immigration\":\"maybe\",\"loans\":\"disagree\",\"healthcare\":\"maybe\",\"retirement\":\"agree\",\"welfare\":\"disagree\",\"taxes\":\"agree\",\"politicalView\":\"libertarian\"}"
