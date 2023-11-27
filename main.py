import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def name():
    return {
        "second_name": "Shnajder",
        "first_name": "Alexander",
        "middle_name": "Sergeevich"
    }


@app.get("/users")
def users():
    return {
        "phone": "89640805026",
        "email": "alexxschh@gmail.com"
    }
    

@app.get("/tools")
def tools():
    skills = {
        "languages": ["Python", "C#", "C++", "Golang"],
        "frameworks": ["FastAPI", "Django", "ASP.NET"],
        "databases": ["PostgresSQL", "MongoDB"],
        "tools": ["unit tests", "git"],
    }
    return skills


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)