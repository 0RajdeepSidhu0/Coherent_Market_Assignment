from fastapi import FastAPI, HTTPException
from ml_model import get_similar_startups
from fastapi.responses import JSONResponse
import sqlite3

DB_PATH = "../data/startups.db"

app = FastAPI(
    title="Startup Lead Generator API",
    description="API to fetch and search YC startup leads",
    version="1.0"
)

@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

def get_connection():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def root():
    return {"message": "Startup Lead Generator API is running "}

# fetching data
@app.get("/startups")
def get_startups(limit: int = 50):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, slug, link, source
        FROM startups
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    startups = [
        {
            "name": r[0],
            "slug": r[1],
            "link": r[2],
            "source": r[3]
        }
        for r in rows
    ]

    return {"count": len(startups), "data": startups}

@app.get("/startups/{slug}")
def get_startup(slug: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, slug, link, source
        FROM startups
        WHERE slug = ?
    """, (slug,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Startup not found")

    return {
        "name": row[0],
        "slug": row[1],
        "link": row[2],
        "source": row[3]
    }

# searching for a scpacific entery
@app.get("/search")
def search_startups(query: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, slug, link, source
        FROM startups
        WHERE name LIKE ?
        LIMIT 20
    """, (f"%{query}%",))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "name": r[0],
            "slug": r[1],
            "link": r[2],
            "source": r[3]
        }
        for r in rows
    ]

@app.get("/recommend/{slug}")
def recommend(slug: str):
    results = get_similar_startups(slug)

    if not results:
        raise HTTPException(status_code=404, detail="Startup not found")

    return {"recommendations": results}