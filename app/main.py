from fastapi import FastAPI

app = FastAPI(
    title="AWS DevOps Cloud-Native API",
    description="FastAPI application deployed with Jenkins, Docker, Helm and AWS EKS",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AWS DevOps Cloud-Native Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def info():
    return {
        "project": "AWS DevOps Cloud-Native",
        "technologies": [
            "Python",
            "FastAPI",
            "Docker",
            "Jenkins",
            "Terraform",
            "Kubernetes",
            "AWS EKS"
        ],
        "version": "1.0.0"
    }