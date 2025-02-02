from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load marks data from JSON file
data_file = os.path.join(os.path.dirname(__file__), 'data', 'q-vercel-python.json')
with open(data_file, 'r') as f:
    marks_full_list = json.load(f)

@app.get("/api")
async def get_marks(names: Optional[List[str]] = Query(None)):
    if names is None:
        raise HTTPException(status_code=400, detail="Names must be provided")
    
    marks_list = []
    for name in names:
        mark = next((student["marks"] for student in marks_full_list if student["name"] == name), "Not Found")
        marks_list.append(mark)
    
    return {"marks" : marks_list}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)