# Image Recognition Project

This repository provides a basic structure for an image recognition system with a Python backend and a Node.js frontend.

## Backend

- **Framework:** FastAPI
- **Purpose:** Accept image uploads, detect objects (faces, cars, license plates), store embeddings in a Postgres database with vector search, and return identification results.
- **Key files:**
  - `backend/app.py` – main FastAPI application.
  - `backend/detection/object_detection.py` – placeholder for detection logic.
  - `backend/models/db.py` – simplified database interface using pgvector.
  - `backend/requirements.txt` – Python dependencies.

Run the backend with:
```bash
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

## Frontend

- **Framework:** Node.js with Express
- **Purpose:** Provide a simple web UI to upload images and display results from the backend.
- **Key files:**
  - `frontend/server.js` – Express server handling uploads and forwarding to the backend.
  - `frontend/public/index.html` – Upload form.
  - `frontend/package.json` – Node.js dependencies.

Run the frontend with:
```bash
npm install --prefix frontend
node frontend/server.js
```

## How It Works

1. The user uploads an image via the frontend.
2. The frontend sends the image to the backend `/upload` endpoint.
3. The backend detects objects, extracts embeddings, and checks them against a Postgres database with vector search (e.g., using the `pgvector` extension).
4. Results are returned to the frontend and displayed to the user.

This project serves as a starting point; you will need to implement actual object detection and database logic to suit your requirements.
