import pygame
import sys
import requests
import urllib.request
import os
from util.poke.pokebattle.battle import check_pokemon
FPS = pygame.time.Clock()
time = 0

def get_name():
    valid_input = False
    while valid_input != True:
        pokemon_name = input(" > ")
        if check_pokemon(pokemon_name) == True:
            return pokemon_name
        print("Old man: I don't have that pokemon!")

def display(pokemon_name=None):
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

    if not pokemon_name:
        valid_input = False
        while valid_input != True:
            pokemon_name = input(" > ")
            try:
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
                response = response.json()
                if response != "Not Found" and check_pokemon(pokemon_name) == True:
                    valid_input = True
                if check_pokemon(pokemon_name) != True:
                    raise Exception
            except:
                print("Old man: I don't have that pokemon!")
    else:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        response = response.json()
    sprite_list = response["sprites"]
    url = sprite_list["front_default"]
    urllib.request.urlretrieve(url, "../util/poke/pokemon.png")

    pygame.init()
    screen_width = 200
    screen_height = 200
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pokemon Battle!")

    # Load the image you want to display
    image_path = "../util/poke/pokemon.png"  # Replace with the path to your image file
    image = pygame.image.load(image_path)

    # Get the dimensions of the image
    image_width, image_height = image.get_size()

    # Define button properties
    button_font = pygame.font.Font("../util/pokemon testing/Consolas.ttf", 16)
    button_color = (255, 255, 255)
    button_text = button_font.render("Pokemon Acquired!", True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(screen_width // 2, screen_height - 50))

    # Main game loop
    frames = 0
    running = True
    while running:
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if frames == 60:
            running = False

        # Clear the screen
        screen.fill((255, 255, 255))  # Fill with white color

        # Display the image on the screen
        screen.blit(image, ((screen_width - image_width) // 2, (screen_height - image_height) // 2))

        # Draw the button
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_rect.topleft)

        # Update the display
        pygame.display.flip()

        FPS.tick(30)

    # Quit Pygame
    pygame.quit()
    return pokemon_name

