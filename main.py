import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import chatbot_routes

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "api.djtretailers.com",
    "http://qa-admin.djtretailers.com",
    "http://dev-admin.djtretailers.com",
    "http://admin.djtretailers.com"
]

app.add_middleware(
    CORSMiddleware,
    
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(chatbot_routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=6071, reload=True)