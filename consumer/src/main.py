import uvicorn

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.23.1", port=4200, log_level="info")