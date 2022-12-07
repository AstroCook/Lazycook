import os

os.system("pip install requirements/base.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload")