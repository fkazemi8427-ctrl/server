from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "سلام! به پروژه FastAPI خوش آمدید."}
