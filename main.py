from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "AI  Assistant Backend Running!"}
