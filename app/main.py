from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, tasks
from app.database.connection import engine
from app.models import user, task

# Create database tables (for development - use Alembic for production)
def init_db():
    user.Base.metadata.create_all(bind=engine)
    task.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management System",
    description="A FastAPI application with JWT authentication and task management using PostgreSQL",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
async def root():
    return {"message": "Task Management System API with PostgreSQL"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "PostgreSQL"}

init_db()