from fastapi import FastAPI
import yaml

# create API app instance
app = FastAPI()

# load data from data.yuml
with open('data.yml') as yml_data:
    data = yaml.safe_load(yml_data)

@app.get("/about")
async def about():
    return data['about']

@app.get("/img")
async def img():
    return None