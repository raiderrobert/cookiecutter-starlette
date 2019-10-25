import uvicorn

from starlette.applications import Starlette
from starlette.middleware.session import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

import settings


app = Starlette()
app.mount('/static', StaticFiles(directory='statics'), name='static')

app.debug = settings.DEBUG
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS
)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
)

@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
