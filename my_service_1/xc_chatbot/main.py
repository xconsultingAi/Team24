from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HealthCheckResponse(BaseModel):
    status: str
    message: str

@app.get("/healthcheck", response_model=HealthCheckResponse)
def healthcheck():
    return HealthCheckResponse(status="success", message="API is healthy and running.")

@app.get("/")
def read_root():
    return {"Hello": "XConsoole Bot here, How can i help you?"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
