import uvicorn
from fastapi import FastAPI

app = FastAPI

@app.get("/examplo")
def example() -> str:
    return "Olá mundo"

if __name__=="__main__":
    print(example()) 
    uvicorn.run(app, port=8087)