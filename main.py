from fastapi import FastAPI, Request, Response
import uvicorn
import base64

app = FastAPI()

# 1x1 transparent PNG
PIXEL_B64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
PIXEL_DATA = base64.b64decode(PIXEL_B64)

@app.get("/")
async def root():
    return {"message": "Service is alive"}

@app.get("/static/pixel.png")
async def track(request: Request, p: str | None = None):
    print(f"Received data: {p}")
    return Response(content=PIXEL_DATA, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
