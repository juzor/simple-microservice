from fastapi import FastAPI
import uvicorn
from mylib import logic


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Welcome to the Wikipedia API"}

@app.get("/search/{value}")
async def search(value: str):
    return {"result" : logic.search_wiki(value)}

@app.get("/wiki/{name}")
async def wiki(name: str):
    return {"result" : logic.wiki(name)}

@app.get("/phrase/{name}")
async def phrase(name: str):
    return {"result" : logic.phrase(name)}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
