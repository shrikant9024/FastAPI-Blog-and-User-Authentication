import uvicorn
from fastapi import FastAPI, Body, Request, Depends
from app.model import PostSchema
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "penguins are a group of aquatic flightless birds"
    },
    {
        "id": 2,
        "title": "tigers",
        "text": "tigers are the largest living cat species and are members of the genus Panthera"
    },
    {
        "id": 3,
        "title": "koalas",
        "text": "Koalas are arboreal herbivorous marsupials native to Australia"
    }
]

users = []

app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}

@app.get("/post", tags=["post"])
def get_post():
    return {"data": posts}

@app.get("/posts/{id}", tags=["post"])  # Fixed the "tags" parameter
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "post with this id does not exist"
        }
    
    for post in posts:  # Fixed the variable name from "post" to "posts"
        if post["id"] == id:
            return {
                "data": post
            }
# ahandler for creating a post
@app.post("/posts", dependencies =[Depends(jwtBearer())],tags = ["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"Post Added"
    }

# user signup
@app.post("/user/signup",tags =["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data:UserLoginSchema):
    for user in users:
        if user.email==data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema=Body()):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"Invalid login details"
        }
 