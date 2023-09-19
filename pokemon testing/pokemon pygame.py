import pygame
import sys
import requests
import urllib.request
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pokemon_name = "ditto"
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
sprite_list = response.json()["sprites"]
url = sprite_list["front_default"]
urllib.request.urlretrieve(url, "pokemon.png")

pygame.init()
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Battle!")

# Load the image you want to display
image_path = "pokemon.png"  # Replace with the path to your image file
image = pygame.image.load(image_path)

# Get the dimensions of the image
image_width, image_height = image.get_size()

# Define button properties
button_font = pygame.font.Font("Consolas.ttf", 16)
button_color = (255, 255, 255)
button_text = button_font.render("Acquire Pokemon!", True, (0, 0, 0))
button_rect = button_text.get_rect(center=(screen_width // 2, screen_height - 50))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the button area
            if button_rect.collidepoint(event.pos):
                print(f"{pokemon_name} is now in your inventory")
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

# Quit Pygame
pygame.quit()
sys.exit()
