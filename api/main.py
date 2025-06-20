import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import user.usuario.endpoint
import user.rol.endpoint
import user.rating.endpoint
import user.review.endpoint
import user.coleccion.endpoint
import user.coleccion_canciones.endpoint
import user.auth.endpoint
import admin.endpoint as admin_endpoint

import music.album.endpoint
import music.genero.endpoint
import music.artista.endpoint
import music.artista_genero.endpoint
import music.cancion.endpoint


app = FastAPI()

# Orígenes permitidos
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
templates_dir = os.path.join(project_root, "front-end")

app.mount("/front-end", StaticFiles(directory=templates_dir), name="templates")
templates = Jinja2Templates(directory=templates_dir)



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(user.usuario.endpoint.router)
app.include_router(user.rol.endpoint.router)
app.include_router(user.rating.endpoint.router)
app.include_router(user.review.endpoint.router)
app.include_router(user.coleccion.endpoint.router)
app.include_router(user.coleccion_canciones.endpoint.router)
app.include_router(user.auth.endpoint.router)
app.include_router(admin_endpoint.router)

app.include_router(music.album.endpoint.router)
app.include_router(music.genero.endpoint.router)
app.include_router(music.artista.endpoint.router)
app.include_router(music.artista_genero.endpoint.router)
app.include_router(music.cancion.endpoint.router)