import fastapi as _fastapi
import uvicorn as _uvicorn
import fastapi.security as _security


import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas


app = _fastapi.FastAPI()


@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)


if __name__ == "__main__":
    _uvicorn.run(app, host="0.0.0.0", port=8000)
