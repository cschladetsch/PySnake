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
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.x = GRID_WIDTH // 2
        self.y = GRID_HEIGHT // 2
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
        self.speed = 10  # Starting speed (frames per second)

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
        # Increase speed slightly when growing, up to a limit
        if self.speed < 20:
            self.speed += 0.2

    def check_collision(self):
        # Check wall collision - can be disabled for borderless mode
        if WALL_COLLISION:
            if (self.x < 0 or self.x >= GRID_WIDTH or
                self.y < 0 or self.y >= GRID_HEIGHT):
                return True
        else:
            # Wrap around screen (teleport to opposite side)
            if self.x < 0:
                self.x = GRID_WIDTH - 1
            elif self.x >= GRID_WIDTH:
                self.x = 0
            if self.y < 0:
                self.y = GRID_HEIGHT - 1
            elif self.y >= GRID_HEIGHT:
                self.y = 0

        # Check self collision - give a small grace period for newly formed segments
        # Only check segments after the third to avoid false collisions
        if (self.x, self.y) in self.body[3:]:
            return True

        return False

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)
        self.color = RED  # Default food color

    def random_position(self, snake_body):
        # Generate a position that's not inside the snake
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            position = (x, y)
            if position not in snake_body:
                return position

def draw_grid():
    # Draw light grid lines
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

def show_game_over(score):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    play_again_text = font.render("Press SPACE to play again", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(play_again_text, (WIDTH//2 - play_again_text.get_width()//2, 2*HEIGHT//3))
    pygame.display.flip()

def show_start_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    title_text = font.render("SNAKE GAME", True, GREEN)
    
    font = pygame.font.Font(None, 36)
    instructions_text1 = font.render("Use arrow keys to move", True, WHITE)
    instructions_text2 = font.render("Eat food to grow", True, WHITE)
    instructions_text3 = font.render("Press SPACE to toggle wall collisions", True, WHITE)
    instructions_text4 = font.render("Press ENTER to start", True, BLUE)
    
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//4))
    screen.blit(instructions_text1, (WIDTH//2 - instructions_text1.get_width()//2, HEIGHT//2 - 40))
    screen.blit(instructions_text2, (WIDTH//2 - instructions_text2.get_width()//2, HEIGHT//2))
    screen.blit(instructions_text3, (WIDTH//2 - instructions_text3.get_width()//2, HEIGHT//2 + 40))
    screen.blit(instructions_text4, (WIDTH//2 - instructions_text4.get_width()//2, HEIGHT//2 + 100))
    pygame.display.flip()

def main():
    global WALL_COLLISION
    WALL_COLLISION = True  # Default: wall collisions enabled
    
    clock = pygame.time.Clock()
    game_active = False
    game_over = False
    
    # Show start screen
    show_start_screen()
    waiting_for_start = True
    
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_start = False
                    game_active = True
                elif event.key == pygame.K_SPACE:
                    WALL_COLLISION = not WALL_COLLISION
                    # Update the wall collision status on screen
                    screen.fill(BLACK)
                    font = pygame.font.Font(None, 72)
                    title_text = font.render("SNAKE GAME", True, GREEN)
                    
                    font = pygame.font.Font(None, 36)
                    instructions_text1 = font.render("Use arrow keys to move", True, WHITE)
                    instructions_text2 = font.render("Eat food to grow", True, WHITE)
                    wall_status = "ON" if WALL_COLLISION else "OFF"
                    instructions_text3 = font.render(f"Wall collisions: {wall_status} (Press SPACE to toggle)", True, WHITE)
                    instructions_text4 = font.render("Press ENTER to start", True, BLUE)
                    
                    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//4))
                    screen.blit(instructions_text1, (WIDTH//2 - instructions_text1.get_width()//2, HEIGHT//2 - 40))
                    screen.blit(instructions_text2, (WIDTH//2 - instructions_text2.get_width()//2, HEIGHT//2))
                    screen.blit(instructions_text3, (WIDTH//2 - instructions_text3.get_width()//2, HEIGHT//2 + 40))
                    screen.blit(instructions_text4, (WIDTH//2 - instructions_text4.get_width()//2, HEIGHT//2 + 100))
                    pygame.display.flip()
    
    while True:
        if game_active:
            snake = Snake()
            food = Food(snake.body)
            score = 0
            last_move_time = time.time()
            game_over = False
            
            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and snake.direction != "DOWN":
                            snake.direction = "UP"
                        elif event.key == pygame.K_DOWN and snake.direction != "UP":
                            snake.direction = "DOWN"
                        elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                            snake.direction = "LEFT"
                        elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                            snake.direction = "RIGHT"
                        elif event.key == pygame.K_p:  # Pause the game
                            paused = True
                            font = pygame.font.Font(None, 72)
                            pause_text = font.render("PAUSED", True, WHITE)
                            screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2))
                            pygame.display.flip()
                            
                            while paused:
                                for ev in pygame.event.get():
                                    if ev.type == pygame.QUIT:
                                        return
                                    elif ev.type == pygame.KEYDOWN:
                                        if ev.key == pygame.K_p:
                                            paused = False
                                            last_move_time = time.time()  # Reset the move timer
                                clock.tick(10)
    
                # Move snake
                snake.move()
    
                # Check collision
                if snake.check_collision():
                    game_over = True
    
                # Check if snake ate food
                if (snake.x, snake.y) == food.position:
                    snake.grow()
                    food = Food(snake.body)
                    score += 1
    
                # Draw everything
                screen.fill(BLACK)
                
                # Optionally draw grid
                draw_grid()
    
                # Draw snake
                for i, segment in enumerate(snake.body):
                    # Make the head a slightly different color
                    color = (0, 255, 0) if i == 0 else (0, 200, 0)
                    pygame.draw.rect(screen, color,
                                   (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE,
                                    GRID_SIZE - 2, GRID_SIZE - 2))
    
                # Draw food
                pygame.draw.rect(screen, food.color,
                                (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE,
                                 GRID_SIZE - 2, GRID_SIZE - 2))
                
                # Draw score
                font = pygame.font.Font(None, 36)
                score_text = font.render(f"Score: {score}", True, WHITE)
                screen.blit(score_text, (10, 10))
                
                # Draw wall collision status
                wall_status = "ON" if WALL_COLLISION else "OFF"
                wall_text = font.render(f"Wall Collisions: {wall_status}", True, WHITE)
                screen.blit(wall_text, (WIDTH - wall_text.get_width() - 10, 10))
    
                # Update display
                pygame.display.flip()
    
                # Control game speed - adjusts for growth
                clock.tick(snake.speed)
    
            # Game over
            show_game_over(score)
            game_active = False
        else:
            # Wait for player to restart
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True

if __name__ == "__main__":
    main()
