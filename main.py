import pygame
import random


def update_target_position():
    global target_x, target_y, target_speed, target_radius, SCREEN_WIDTH, SCREEN_HEIGHT

    target_x += target_speed[0]
    target_y += target_speed[1]

    if target_x <= target_radius or target_x >= SCREEN_WIDTH - target_radius:
        target_speed[0] *= -1
    if target_y <= target_radius or target_y >= SCREEN_HEIGHT - target_radius:
        target_speed[1] *= -1


def display_score(score, shoots):
    white = (255, 255, 255)
    font = pygame.font.Font(None, 36)
    if shoots == 0:
        result = 0
    else:
        result = round(100*score/shoots, 2)
    text = font.render(f"Выстрелы: {shoots}  Очки: {score}  Процент попаданий: {result}%", 1, white)
    screen.blit(text, (10, 10))


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game "Shooting gallery"')

icon = pygame.image.load("img/shooter.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
# target_width = 80
# target_height = 80
target_radius = 80
# target_x = random.randint(0, SCREEN_WIDTH - target_width)
# target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_x = random.randint(0, SCREEN_WIDTH - target_radius)
target_y = random.randint(0, SCREEN_HEIGHT - target_radius)
target_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
score_game = 0
shoots_game = 0
clock = pygame.time.Clock()

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

timeout = 3000  # Время до смены мишени в мс
last_time = pygame.time.get_ticks()

runnig = True
while runnig:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            shoots_game += 1
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= target_radius:
                score_game += 1
                target_x = random.randint(target_radius, SCREEN_WIDTH - target_radius)
                target_y = random.randint(target_radius, SCREEN_HEIGHT - target_radius)

            # if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
            #    target_x = random.randint(0, SCREEN_WIDTH - target_width)
            #    target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    current_time = pygame.time.get_ticks()
    if current_time - last_time > timeout:
        last_time = current_time
        target_x = random.randint(target_radius, SCREEN_WIDTH - target_radius)
        target_y = random.randint(target_radius, SCREEN_HEIGHT - target_radius)

    # screen.blit(target_image, (target_x, target_y))
    # pygame.display.update()

    update_target_position()
    screen.blit(target_image, (target_x, target_y))
    display_score(score_game, shoots_game)
    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
