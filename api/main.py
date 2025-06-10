from fastapi import FastAPI

import user.usuario.endpoint
import user.rol.endpoint
import user.rating.endpoint
import user.review.endpoint
import user.coleccion.endpoint
import user.coleccion_canciones.endpoint

import music.album.endpoint
import music.genero.endpoint
import music.artista.endpoint
import music.artista_genero.endpoint
import music.cancion.endpoint


app = FastAPI()

# prefix_base = "/api/v1"

app.include_router(user.usuario.endpoint.router)
app.include_router(user.rol.endpoint.router)
app.include_router(user.rating.endpoint.router)
app.include_router(user.review.endpoint.router)
app.include_router(user.coleccion.endpoint.router)
app.include_router(user.coleccion_canciones.endpoint.router)

app.include_router(music.album.endpoint.router)
app.include_router(music.genero.endpoint.router)
app.include_router(music.artista.endpoint.router)
app.include_router(music.artista_genero.endpoint.router)
app.include_router(music.cancion.endpoint.router)