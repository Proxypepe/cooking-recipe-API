from pydantic import BaseModel
from typing import Sequence


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: str


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str
    source: str
    url: str
    submitter_id: int
