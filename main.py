from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from BrioWriter import BrioWriter

import shutil




app = FastAPI()
BW = BrioWriter()
app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")


def get_remaining_space():
    total, used, free = shutil.disk_usage("/")
    t = "Total: %d GiB" % (total // (2**30))
    u = "Used: %d GiB" % (used // (2**30))
    f = "Free: %d GiB" % (free // (2**30))
    return t, u, f

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    t = datetime.now()
    # BW.write_images()
    status = "FIle asdf jl asd wri"
    memory_usage = get_remaining_space()
    t = datetime.now() - t
    return templates.TemplateResponse("index.html", {"request": request, "timestamp":t, "memory_usage":memory_usage, "status": status})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
