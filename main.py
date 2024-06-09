from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# CORS 설정 추가
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://100.28.146.73"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuestbookEntry(BaseModel):
    id: int = None
    author: str
    content: str
    timestamp: str = None

guestbook = []

@app.post('/guestbook', response_model=GuestbookEntry)
async def add_entry(entry: GuestbookEntry):
    entry.id = len(guestbook) + 1
    entry.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guestbook.append(entry)
    return entry

@app.get('/guestbook', response_model=List[GuestbookEntry])
async def get_entries():
    return guestbook

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("/home/ec2-user/guest-book/static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.delete('/guestbook/{entry_id}')
async def delete_entry(entry_id: int):
    global guestbook
    for index, entry in enumerate(guestbook):
        if entry.id == entry_id:
            del guestbook[index]
            return {"message": f"Entry with ID {entry_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Entry not found")

app.mount("/static", StaticFiles(directory="/home/ec2-user/guest-book/static"), name="static")

