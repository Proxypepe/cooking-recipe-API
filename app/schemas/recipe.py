from pydantic import BaseModel

from typing import Sequence


class RecipeBase(BaseModel):
    label: str
    source: str
    url: str


class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: str
    submitter_id: int


class RecipeUpdate(RecipeBase):
    label: str


class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


class Recipe(RecipeInDBBase):
    pass


class RecipeInDB(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
