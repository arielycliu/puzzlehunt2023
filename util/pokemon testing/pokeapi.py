import requests
from PIL import Image
import urllib.request

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
sprite_list = response.json()["sprites"]
url = sprite_list["front_default"]
urllib.request.urlretrieve(url, "../poke/pokemon.png")
x = Image.open('../poke/pokemon.png').quantize(colors=10, method=1)
x = x.convert('RGB')
x.show()