import pokebase as pb

s1 = pb.SpriteResource('pokemon', 17)
s1.url
s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
s2.path
s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
s3.img_data

# https://stackoverflow.com/questions/69239521/unable-to-display-pokemon-image-from-pokeapi-co
# https://github.com/PokeAPI/pokeapi
