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

prefix_base = "/api/v1"

app.include_router(user.usuario.endpoint.router, prefix=f"{prefix_base}/usuario")
app.include_router(user.rol.endpoint.router, prefix=f"{prefix_base}/rol")
app.include_router(user.rating.endpoint.router, prefix=f"{prefix_base}/rating")
app.include_router(user.review.endpoint.router, prefix=f"{prefix_base}/review")
app.include_router(user.coleccion.endpoint.router, prefix=f"{prefix_base}/coleccion")
app.include_router(user.coleccion_canciones.endpoint.router, prefix=f"{prefix_base}/coleccion_canciones")

app.include_router(music.album.endpoint.router, prefix=f"{prefix_base}/album")
app.include_router(music.genero.endpoint.router, prefix=f"{prefix_base}/genero")
app.include_router(music.artista.endpoint.router, prefix=f"{prefix_base}/artista")
app.include_router(music.artista_genero.endpoint.router, prefix=f"{prefix_base}/artista_genero")
app.include_router(music.cancion.endpoint.router, prefix=f"{prefix_base}/cancion")