import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        reload=True,
        app='project.main:app',
        host='0.0.0.0',
        port=8000,
    )