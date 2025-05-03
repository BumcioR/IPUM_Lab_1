# IPUM Lab 1 — MLOps Intro

In this lab, we will build a production-ready machine learning application. Step by step, we will
introduce best practices and basic tools that are used throughout any MLOps project. At the end,
you will have a local server providing ML model predictions.

## Covered topics

1. Dependency management (`uv`)
2. Code versioning (Git, GitHub)
3. Pre-commit hooks
4. Configuration and environment variable management
5. Secrets management (`sops`)
6. Testing
7. FastAPI web server
8. Serving ML model
9. Containerization (Docker, Docker Compose)

## Final Check (Docker Compose)

The FastAPI server was successfully launched using `docker compose up`.

- The `/docs` endpoint is available locally at `http://localhost:8000/docs`.
- The `ml-app` image was built and the container started successfully.
- The `/predict` endpoint was tested and returned correct model predictions.