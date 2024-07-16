from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar el directorio de archivos estáticos
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html") as f:
        return f.read()

@app.get("/styles.css")
async def read_css():
    with open("styles.css") as f:
        return HTMLResponse(f.read(), media_type="text/css")

@app.get("/scripts.js")
async def read_js():
    with open("scripts.js") as f:
        return HTMLResponse(f.read(), media_type="application/javascript")
