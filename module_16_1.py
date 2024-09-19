from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": f"Главная страница"}


@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_number(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


@app.get(f"/user")
async def user_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}