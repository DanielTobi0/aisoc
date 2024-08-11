from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from script import generate
from script import models


app = FastAPI()

@app.get("/llm_app")
async def llm_app():
    return {
        "application": "Simple LLM app",
        "message": "running successful"
    }


@app.post("/chat")
async def generate_chat(request: Request):
    query = await request.json()
    model = query["model"]

    if model not in models:
        return {
            "error": "you did not pass a correct model name"
        }
    
    response = generate(
        model, query["question"], query["temperature"]
        )

    return {
        "status": "success",
        "response": response
    }


if __name__ == "__main__":
    import uvicorn
    print("Starting LLM App")
    uvicorn.run(app, host="0.0.0.0", reload=True)