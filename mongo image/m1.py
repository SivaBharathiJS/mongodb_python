from pymongo import MongoClient
from PIL import Image
import io

client = MongoClient()
db = client.testdb
images = db.images

im = Image.open("./img.png")

image_bytes = io.BytesIO()
im.save(image_bytes, format='PNG')

image = {
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id
