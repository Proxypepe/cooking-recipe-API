from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Recipe API"
)


router = APIRouter()


@router.get('/', status_code=200)
def root() -> dict:
    return {"msg": "root endpoint"}


app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8001, log_level="debug")
