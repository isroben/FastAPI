from fastapi import FastAPI, HTTPException
from schemas import postCreate


app = FastAPI()

text_post = {1:"This is sample post",
             2: "Pain and suffering is inevitable for large intelligence and deep heat.",
             3: "Be optimistic"}

@app.get("/")
def helloworld():
    return {"message" : "Hello world"}

@app.get("/posts")
def getAllPosts(limit: int = None):
    if limit:
        return list(text_post.values())[:limit]
    return text_post

@app.get("/post/{id}")
def getPost(id: int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post Not Found")

    return text_post.get(id)

@app.post("/posts")
def createPost(post: postCreate):
    text_post[max(text_post.keys()) +1 ] = {"title": post.title, "Content": post.content}
