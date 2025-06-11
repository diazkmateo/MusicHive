from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import time
from collections import defaultdict
import asyncio

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.requests = defaultdict(list)
        self.lock = asyncio.Lock()

    async def check_rate_limit(self, request: Request) -> bool:
        client_ip = request.client.host
        current_time = time.time()
        
        async with self.lock:
            # Limpiar solicitudes antiguas
            self.requests[client_ip] = [
                req_time for req_time in self.requests[client_ip]
                if current_time - req_time < 60
            ]
            
            # Verificar límite
            if len(self.requests[client_ip]) >= self.requests_per_minute:
                return False
            
            # Agregar nueva solicitud
            self.requests[client_ip].append(current_time)
            return True

rate_limiter = RateLimiter()

async def rate_limit_middleware(request: Request, call_next):
    if not await rate_limiter.check_rate_limit(request):
        return JSONResponse(
            status_code=429,
            content={"detail": "Demasiadas solicitudes. Por favor, intente más tarde."}
        )
    
    return await call_next(request) 