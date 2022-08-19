from typing import Optional

from fastapi import FastAPI, APIRouter

from data import RECIPES

app = FastAPI(
    title="Recipe API"
)

router = APIRouter()


@router.get('/', status_code=200)
def root() -> dict:
    return {"msg": "root endpoint"}


@router.get('/recipe/{recipe_id}', status_code=200)
def get_recipe_by_id(*, recipe_id: int) -> dict:
    result = [recipe for recipe in RECIPES if recipe['id'] == recipe_id]
    if result:
        return result[0]


@router.get('/search/', status_code=200)
def search_recipe(
    keyword: Optional[str] = None, max_results: Optional[int] = 10
) -> dict:
    if keyword is None:
        return {'result': RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES)
    return {'result': list(results)[:max_results]}


app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8001, log_level="debug")
