from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html") as f:
        return f.read()

@app.get("/styles.css")
async def read_css():
    with open("styles.css") as f:
        return HTMLResponse(f.read(), media_type="text/css")

@app.get("/script.js")
async def read_js():
    with open("script.js") as f:
        return HTMLResponse(f.read(), media_type="application/javascript")
