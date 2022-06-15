import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer


app = FastAPI()

posts = [
   {
        "id": 1,
        "title": "Grocery_items",
        "text": "Any kind of Grocery can be ordered!!!"
    },
    {
        "id": 2,
        "title": "Fruits",
        "text": "Any kind of Fruits can be ordered!!!"
    },
    {
        "id": 3,
        "title": "Vegetables",
        "text": "Any kind of Veggies can be ordered!!!"
    }
]


users = []

# Get for testing
@app.get("/", tags=["Test"])
def greet():
    return {"Hello": "World!!!"}


# Get Posts
@app.get("/posts", tags = ["posts"])
def get_post():
    return {"data": posts}
    
# Get single post{id}
@app.get("/posts/{id}", tags = ["posts"])
def get_one_posts(id :int):
    if id > len(posts):
        return {
            "error":"Posts with this ID does not exists"
        }
    for post in posts:
        if post["id"] == id:
            return {"data": post}

# Post a blog post [A handler for creating post]
@app.post("/posts",dependencies=[Depends(JWTBearer())],tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return{
        "info": "Post Added"
    }

# User signup [ create a new user]
@app.post("/user/signup", tags=["user"])
def user_signup(user:UserSchema =Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }