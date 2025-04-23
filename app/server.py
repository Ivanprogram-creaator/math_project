from fastapi import FastAPI
from personality.characters import *
from person import Person
from pydantic import BaseModel

server = FastAPI()
class GetEmotion(BaseModel):
    character: str
    desire_value: float
    own_probability: float
    know_probability: float
    percents: list
    direction: bool
    timeline: bool
    surprise_coef: float
    relationship: int

@server.get('/get_emotion')
def get_emotion(data: GetEmotion):
    person = Person(eval(data.character)())
    emotion = person.emotion_define(
        desire_value=data.desire_value,
        know_probability=data.know_probability,
        own_probability=data.own_probability,
        needs_percent=data.percents,
        direction=data.direction,
        timeline=data.timeline,
        surprise_coef=data.surprise_coef,
        relationship=data.relationship
    )
    return emotion