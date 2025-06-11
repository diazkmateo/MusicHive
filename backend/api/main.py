from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.usuario.endpoint import router as usuario_router
from user.rol.endpoint import router as rol_router
from user.rating.endpoint import router as rating_router
from user.review.endpoint import router as review_router
from user.coleccion.endpoint import router as coleccion_router
from user.coleccion_canciones.endpoint import router as coleccion_canciones_router

from music.album.endpoint import router as album_router
from music.genero.endpoint import router as genero_router
from music.artista.endpoint import router as artista_router
from music.artista_genero.endpoint import router as artista_genero_router
from music.cancion.endpoint import router as cancion_router

from core.rate_limit import rate_limit_middleware

app = FastAPI(title="MusicHive API")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers de usuario
app.include_router(usuario_router)
app.include_router(rol_router)
app.include_router(rating_router)
app.include_router(review_router)
app.include_router(coleccion_router)
app.include_router(coleccion_canciones_router)

# Incluir routers de música
app.include_router(album_router)
app.include_router(genero_router)
app.include_router(artista_router)
app.include_router(artista_genero_router)
app.include_router(cancion_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de MusicHive"}