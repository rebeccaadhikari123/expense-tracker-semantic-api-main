from fastapi import FastAPI
from pydantic import BaseModel
import semantic as semanticsms
import spacy

class Message(BaseModel):
    message_body: str

app = FastAPI()

nlp = spacy.load('en_core_web_sm')

@app.get("/")
def index():
    return {"Index": "page"}

@app.post("/analyse_sms/")
def analyse_sms(message: Message):
    message_body = message.message_body
    message_doc = nlp(message_body)
    extracted_amount = semanticsms.extract_amount(message_doc)

    # create a function that finds out the type of message
    message_type = semanticsms.key_extraction(message_doc)

    # remove all the print statements once everthing is done
    data = {
        "extracted_amount": extracted_amount,
        "message_type": message_type,
    }
    return data

