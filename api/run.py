import uvicorn
from server import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, port = 8080)
