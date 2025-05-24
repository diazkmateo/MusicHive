from fastapi import FastAPI

import api.user.usuario.endpoint
import api.user.rol.endpoint
import api.user.rating.endpoint
import api.user.review.endpoint
import api.user.coleccion.endpoint
import api.user.coleccion_canciones.endpoint

import api.music.album.endpoint
import api.music.genero.endpoint
import api.music.artista.endpoint
import api.music.artista_genero.endpoint
import api.music.cancion.endpoint


app = FastAPI()

prefix_base = "/api/v1"

app.include_router(api.user.usuario.endpoint.router, prefix=f"{prefix_base}/usuario")
app.include_router(api.user.rol.endpoint.router, prefix=f"{prefix_base}/rol")
app.include_router(api.user.rating.endpoint.router, prefix=f"{prefix_base}/rating")
app.include_router(api.user.review.endpoint.router, prefix=f"{prefix_base}/review")
app.include_router(api.user.coleccion.endpoint.router, prefix=f"{prefix_base}/coleccion")
app.include_router(api.user.coleccion_canciones.endpoint.router, prefix=f"{prefix_base}/coleccion_canciones")

app.include_router(api.music.album.endpoint.router, prefix=f"{prefix_base}/album")
app.include_router(api.music.genero.endpoint.router, prefix=f"{prefix_base}/genero")
app.include_router(api.music.artista.endpoint.router, prefix=f"{prefix_base}/artista")
app.include_router(api.music.artista_genero.endpoint.router, prefix=f"{prefix_base}/artista_genero")
app.include_router(api.music.cancion.endpoint.router, prefix=f"{prefix_base}/cancion")