from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data_loader import load_records
from database.local import LocalDatabase
from aitools.implementations import get_erasure_by_serial_number


app = FastAPI()

#Create a local database -object with example records from a JSON file.
records = LocalDatabase(load_records("../data/example_records.json"))

#Allow CORS for local React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "Python backend is running"}

#Chat request model for the /chat endpoint.
class ChatRequest(BaseModel):
    message: str

#Chat response model for the /chat endpoint.
class ChatResponse(BaseModel):
    reply: dict

#Chat endpoint that receives a message and returns a response based on the erasure records.
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    result = get_erasure_by_serial_number(records, request.message)

    return ChatResponse(reply=result)