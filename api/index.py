from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Video Game Dictionary",
    description="A beginner-friendly REST API containing simple information about video games.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BAGS DATA
vgames = [

    {
        "id": 1,
        "name": ,
        "brand": ,
        "shape": ,
        "material": ,
        "rating": ,
        "price": " ",
        "collection": ,
        "shape": ,
        "color": ,
        "rating": 4.8,
        "type:" # if handbag, tote bag, etc. 
        "availability:" #if available online or nah
        "description": "A sandbox game focused on exploration, building, crafting, and survival."
        "buyer-notes:" ,
    },


]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Video Game Dictionary!",
        "endpoints": [
            "/vgames",
            "/vgames/{id}",
            "/vgames/search"
        ]
    }


# GET ALL CARS
@app.get("/vgames")
def get_vgames():

    return {
        "count": len(vgames),
        "vgames": vgames
    }

# SEARCH CARS
@app.get("/vgames/search")
def search_vgames( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for games in vgames:
        searchable_text = (
            f"{games['title']} "
            f"{games['genre']} "
            f"{games['year']} "
            f"{games['platform']}"
        ).lower()

        if q in searchable_text:
            results.append(games)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }
    
# GET ONE CAR
@app.get("/vgames/{game_id}")
def get_game(game_id: int):

    for games in vgames:

        if games["id"] == game_id:
            return games

    raise HTTPException(
        status_code=404,
        detail="Game not found."
    )


