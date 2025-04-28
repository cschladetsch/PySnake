import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.x = GRID_WIDTH // 2
        self.y = GRID_HEIGHT // 2
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]

    def move(self):
        if self.direction == "UP":
            self.y -= 1
        elif self.direction == "DOWN":
            self.y += 1
        elif self.direction == "LEFT":
            self.x -= 1
        elif self.direction == "RIGHT":
            self.x += 1

        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        # Check wall collision
        if (self.x < 0 or self.x >= GRID_WIDTH or
            self.y < 0 or self.y >= GRID_HEIGHT):
            return True

        # Check self collision
        if (self.x, self.y) in self.body[1:]:
            return True

        return False

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        # Move snake
        snake.move()

        # Check collision
        if snake.check_collision():
            game_over = True

        # Check if snake ate food
        if (snake.x, snake.y) == food.position:
            snake.grow()
            food.position = food.random_position()
            score += 1

        # Draw everything
        screen.fill(BLACK)

        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN,
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE,
                            GRID_SIZE - 2, GRID_SIZE - 2))

        # Draw food
        pygame.draw.rect(screen, RED,
                        (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE,
                         GRID_SIZE - 2, GRID_SIZE - 2))
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Control game speed
        clock.tick(10)

    # Game over
    pygame.quit()

if __name__ == "__main__":
    main()
