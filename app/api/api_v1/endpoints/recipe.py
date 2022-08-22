from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas.recipe import Recipe, RecipeCreate
from app.api import deps
from app import crud

router = APIRouter()


@router.get('/recipe/{recipe_id}', status_code=200, response_model=Recipe)
def get_recipe_by_id(*,
                     recipe_id: int,
                     db: Session = Depends(deps.get_db)
                     ) -> Any:
    result = crud.recipe.get(db=db, _id=recipe_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )

    return result


@router.get('/search/', status_code=200)
def search_recipe(
        *,
        keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
        max_results: Optional[int] = 10,
        db: Session = Depends(deps.get_db)
) -> dict:
    recipes = crud.recipe.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": recipes}

    results = filter(lambda recipe: keyword.lower() in recipe.label.lower(), recipes)
    return {"results": list(results)[:max_results]}


@router.post('/recipe', status_code=201, response_model=Recipe)
def create_recipe(
        *, recipe_in: RecipeCreate, db: Session = Depends(deps.get_db)
) -> dict:
    recipe = crud.recipe.create(db=db, obj_in=recipe_in)

    return recipe
