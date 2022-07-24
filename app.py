from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome. This is yet another blogging app."}