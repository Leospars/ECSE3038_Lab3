from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from markdown import markdown
from uuid import uuid4, UUID

class Tank(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    location: str
    lat: float
    long: float

tanks = [ Tank(id="2f5822b0-56ea-477f-bbbb-3476279b166b",
 location="Chemistry department", lat=18.004741066082236, long=-76.74875280426826),
] # list of tanks

def graceful_find(tanks, id: UUID) -> Tank :
    try :
        return list(filter(lambda tank: tank.id == id, tanks))[0]
    except :
        raise HTTPException(status_code=404, detail="Tank not found")

app = FastAPI()
@app.get("/")
async def root():
    file_content = open("README.md", "r").read()
    return HTMLResponse(markdown(file_content))

@app.get("/tank")
async def get_all_tanks():
    tanks_json = jsonable_encoder(tanks)
    return JSONResponse(tanks_json, status_code=200)

@app.get("/tank/{id}")
async def get_single_tank(id: UUID) :
    return graceful_find(tanks, id)

@app.post("/tank")
async def create_tank(tank: Tank) :
    tanks.append(tank)
    tank_json = jsonable_encoder(tank)
    return JSONResponse(tank_json, status_code=201)

class TankPatch(BaseModel):
    location: str = None
    lat: float = None
    long: float = None

@app.patch("/tank/{id}")
async def edit_tanks(tank_patch: TankPatch, id: UUID) :
    tank = graceful_find(tanks, id)
    location = tank_patch.location
    lat = tank_patch.lat
    long = tank_patch.long
    print(location, lat, long)

    if location is not None:
        tank.location = tank_patch.location
    
    if lat is not None:
        tank.lat = tank_patch.lat
    
    if long is not None:
        tank.long = tank_patch.long

    tank_json = jsonable_encoder(tank)
    return JSONResponse(tank_json, status_code=200)

@app.delete("/tank/{id}")
async def delete_tank(id: UUID) :
    tanks.remove(graceful_find(tanks, id))
    blank = jsonable_encoder({})
    return JSONResponse(blank, status_code=204)
