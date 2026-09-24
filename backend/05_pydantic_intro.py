from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Blog(BaseModel):
    title: str = Field(min_length=10, max_length=100)
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.PY
    created_at: datetime = Field(default_factory=datetime.now)

first_blog = Blog(title="My first blog", is_active=True)
print(first_blog)  # Output: My first blog

import time
time.sleep(5)

second_blog = Blog(title="My second blog", is_active=False)
print(second_blog)  # Output: My second blog