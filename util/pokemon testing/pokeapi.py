import requests
from PIL import Image
import urllib.request

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
sprite_list = response.json()["sprites"]
url = sprite_list["front_default"]
urllib.request.urlretrieve(url, "../poke/pokemon.png")
x = Image.open('../poke/pokemon.png').quantize(colors=10, method=1)
img = x.convert("RGB")
datas = img.getdata()
new_image_data = []
for item in datas:
    print(item)
    if item[0] == (0, 0, 0):
        new_image_data.append((255, 255, 250))
    else:
        new_image_data.append(item)

img.putdata(new_image_data)
img.save("test_image_altered_background.jpg")
img.show()
