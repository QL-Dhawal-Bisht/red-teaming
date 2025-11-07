from fastapi import FastAPI, Request
from starlette.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Service is alive"}

@app.get("/static/pixel.png")
async def track(request: Request):
    query_params = dict(request.query_params)
    print(f"Received query params: {query_params}")
    return FileResponse("static/test.png", media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
