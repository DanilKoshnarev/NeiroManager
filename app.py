from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from router.router import Router
from cache.redis_cache import RedisCache

app = FastAPI()
templates = Jinja2Templates(directory="templates")
router = Router()
cache = RedisCache()

@app.on_event("startup")
async def startup():
    await cache.connect()

@app.on_event("shutdown")
async def shutdown():
    await cache.close()

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    service = data.get("service", "chatgpt")
    response = await router.route_request(prompt, service)
    return response

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})