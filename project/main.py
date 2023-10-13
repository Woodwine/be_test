from fastapi import FastAPI
from project.questions.routers import router as question_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title='Bewise test'
)

app.include_router(question_router)


origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)