from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import routes

app = FastAPI(
    title="Reprompt API",
    description="Backend service for optimizing prompts.",
    version="1.2.0"
)

 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           
    allow_credentials=True,
    allow_methods=["*"],           
    allow_headers=["*"],         
)

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Reprompt API is up and running !! 🔥🔥"}