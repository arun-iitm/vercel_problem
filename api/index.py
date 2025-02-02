from fastapi import FastAPI, HTTPException
from typing import List
import json
import os

app = FastAPI()

# Load marks data from JSON file
data_file = os.path.join(os.path.dirname(__file__), 'data', 'q-vercel-python.json')
with open(data_file, 'r') as f:
    marks = json.load(f)

@app.get("/api")
async def get_marks(names: List[str]):
    try:
        return {name: marks.get(name, "Not Found") for name in names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))