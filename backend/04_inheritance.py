# class Python:
#     def __init__(self)-> None:
#         self.is_cool = True

# class FastAPI(Python):
#     pass

# f = FastAPI()
# print(f.is_cool)


class Pydantic:
    def is_valid(self, text):
        if "admin" in text:
            return False
        return True

class Starlette:
    def is_valid(self, text):
        return True

class FastAPI(Pydantic, Starlette):
    pass

f = FastAPI()
print(FastAPI.__mro__)  # False
print(f.is_valid("admin tried something"))  # True
