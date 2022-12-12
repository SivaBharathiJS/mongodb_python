from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
import io
import matplotlib.pyplot as plt

client = MongoClient()
db = client.testdb
images = db.images
image = images.find_one()

pil_img = Image.open(io.BytesIO(image['data']))
plt.imshow(pil_img)
plt.show()
