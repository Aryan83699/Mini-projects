import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

# Capture FastAPI, Starlette and Uvicorn logs
for name in ["uvicorn", "uvicorn.error", "uvicorn.access",
             "fastapi", "starlette"]:
    log = logging.getLogger(name)
    log.handlers = logging.getLogger().handlers
    log.setLevel(logging.INFO)
    log.propagate = False