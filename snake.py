import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("application-icon.png")
pygame.display.set_icon(icon)

font = pygame.font.Font("./upheavtt.ttf", 30)

snake_size = 20
snake_speed = 5
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_length = 1
snake_postions = [(snake_x, snake_y)]
snake_direction = None

def random_location():
    return round(random.randrange(0, screen_width - snake_size) // snake_size) * snake_size, round(random.randrange(0, screen_height - snake_size) // snake_size) * snake_size

food_size = 15
[ food_x, food_y ] = random_location()

running = True
clock = pygame.time.Clock()
while running:
    [ snake_x, snake_y ] = snake_postions[0] 

    screen.fill((0, 0, 0))

    # Increase the speed of the snake as it gets longer
    snake_speed = max((snake_length * 5) / 7, 5)

    if len(snake_postions) > snake_length:
        snake_postions.pop()

    # Detect the snake running into itself
    if snake_postions[0] in snake_postions[1:]:
        screen.fill((0, 0, 0))

        text = font.render("You lost!", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        
        pygame.display.flip()

        running = False

        pygame.time.wait(2000)  

        snake_size = 20
        snake_x = screen_width // 2
        snake_y = screen_height // 2
        snake_length = 1
        snake_postions = [(snake_x, snake_y)]
        snake_direction = None

        running = True

    # Draw the snake
    for i in range(snake_length):
        [ x, y ] = snake_postions[i]
        
        if i == 0 and snake_x == food_x and snake_y == food_y:
            snake_length += 1
            [ food_x, food_y ] = random_location()
        
        pygame.draw.rect(screen, (255, 255, 255), [x, y, snake_size, snake_size])

    # Draw the food
    pygame.draw.circle(screen, (255, 255, 255), (food_x + food_size - 5, food_y + food_size - 5), food_size // 2)

    # Handle direction changes
    if snake_direction == "left":
        if (snake_x < 0):
            snake_x = screen_width
        snake_postions.insert(0, (snake_x - snake_size, snake_y))
    elif snake_direction == "right":
        if (snake_x > screen_width):
            snake_x = 0
        snake_postions.insert(0, (snake_x + snake_size, snake_y))
    elif snake_direction == "up":
        if (snake_y < 0):
            snake_y = screen_height
        snake_postions.insert(0, (snake_x, snake_y - snake_size))
    elif snake_direction == "down":
        if (snake_y > screen_height):
            snake_y = 0
        snake_postions.insert(0, (snake_x, snake_y + snake_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyborad events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake_direction != "right":
                    snake_direction = "left" 
            elif event.key == pygame.K_RIGHT:
                if snake_direction != "left":
                    snake_direction = "right"
            elif event.key == pygame.K_UP:
                if snake_direction != "down":
                    snake_direction = "up"
            elif event.key == pygame.K_DOWN:
                if snake_direction != "up":
                    snake_direction = "down"

    score_text = font.render(f"Score: {snake_length - 1}", True, (255, 255, 255))
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

    pygame.display.flip()

    clock.tick(snake_speed)