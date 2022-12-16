import os
import uvicorn

if __name__ == "__main__":
    os.system("cd /app/app/alembic && alembic upgrade head")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=os.getenv("PORT", default=5000),
        log_level="info",
    )
