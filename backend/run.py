from .sql_app import main

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main.app, host="0.0.0.0", port=8000)