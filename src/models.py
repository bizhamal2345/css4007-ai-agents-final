from pydantic import BaseModel, Field
from typing import Optional


class Paper(BaseModel):

    paper_id: str = Field(min_length=1)
    title: str = Field(min_length=1)

    authors: list[str] = Field(default_factory=list)

    publication_year: Optional[int] = None
    doi: Optional[str] = None
    abstract: Optional[str] = None

    cited_by_count: int = Field(default=0, ge=0)

    url: Optional[str] = None
    pdf_url: Optional[str] = None
