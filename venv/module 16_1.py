from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcone(module_16_1) -> dict:
    return {"nessage": "Главная страница"}


@app.get("/module 16_1")
async def welcone() -> dict:
    return {"nessage": "module 16_1 page"}
