from typing import Optional, Any
from pathlib import Path

from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates

from app.schemas.recipe import Recipe, RecipeCreate, RecipeSearchResults
from data import RECIPES

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(
    title="Recipe API"
)

router = APIRouter()


@router.get('/', status_code=200)
def root(request: Request):
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "recipes": RECIPES},
    )


@router.get('/recipe/{recipe_id}', status_code=200, response_model=Recipe)
def get_recipe_by_id(*, recipe_id: int) -> Any:
    result = [recipe for recipe in RECIPES if recipe['id'] == recipe_id]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )

    return result[0]


@router.get('/search/', status_code=200)
def search_recipe(
        keyword: Optional[str] = Query(None, min_length=3, example="chicken"), max_results: Optional[int] = 10
) -> dict:
    if keyword is None:
        return {'result': RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES)
    return {'result': list(results)[:max_results]}


@router.post('/recipe', status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> Recipe:
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.dict())

    return recipe_entry


app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8001, log_level="debug")
