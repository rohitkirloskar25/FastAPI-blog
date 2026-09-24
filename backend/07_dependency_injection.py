from fastapi import Depends, FastAPI, HTTPException, status

blogs = {
    "1": "Fast API Prequisites",
    "2": "Building APIs with Fast API",
    "3": "Background Tasks | Fast API x Celery",
}

users = {
    "1": "Rohit",
    "2": "John"
}

app = FastAPI(title="Dependency Injection")

def get_object_or_404(model: dict, id: str):
    obj = model.get(id)
    if not obj:
        raise HTTPException(detail=f"Object with ID: {id} not found", 
                            status_code=status.HTTP_404_NOT_FOUND)
    return obj

class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"Object with ID: {id} not found", 
                                status_code=status.HTTP_404_NOT_FOUND)
        return obj

blog_dependency = GetObjectOr404(blogs)
@app.get("/blog/{id}")
def get_blog(blog_name:str = Depends(blog_dependency)):
    return blog_name

user_dependency = GetObjectOr404(users)
@app.get("/user/{id}")
def get_user(user_name:str = Depends(user_dependency)):
    return user_name