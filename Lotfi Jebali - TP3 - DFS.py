# Lotfi Jebali L2CS1
import pygame
import time

# dimensions of the Taquin game board
BLOCK_SIZE = 100
BOARD_SIZE = BLOCK_SIZE * 3
WINDOW_SIZE = (BOARD_SIZE, BOARD_SIZE)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


def draw_board(state):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the tiles
    for i in range(3):
        for j in range(3):
            tile_value = state[i][j]
            if tile_value == 0:
                color = (0, 0, 0)
            else:
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (j*BLOCK_SIZE, i *
                             BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            font = pygame.font.Font(None, 36)
            text = font.render(str(tile_value), 1, (255, 255, 255))
            textpos = text.get_rect(
                centerx=j*BLOCK_SIZE+BLOCK_SIZE/2, centery=i*BLOCK_SIZE+BLOCK_SIZE/2)
            screen.blit(text, textpos)

    # Update the display
    pygame.display.flip()


def dfs(state, goal_state, depth, max_depth, path):
    if state == goal_state:
        print("Solution found:")
        print_path(path)
        return True
    elif depth == max_depth:
        return False
    # Draw the current state of the board
    draw_board(state)
    time.sleep(0.5)  # Add a delay to slow down the animation
    for movement in ["up", "down", "left", "right"]:
        new_state = move(state, movement)
        if new_state is not None and new_state not in path:
            path.append(new_state)
            if dfs(new_state, goal_state, depth+1, max_depth, path):
                return True
            path.pop()
    return False


def move(state, movement):
    # new_state = [row[:] for row in state]
    new_state = [list(row) for row in state]
    row, col = get_blank_pos(new_state)
    if movement == "up":
        if row == 0:
            return None
        new_state[row][col], new_state[row -
                                       1][col] = new_state[row-1][col], new_state[row][col]
    elif movement == "down":
        if row == 2:
            return None
        new_state[row][col], new_state[row +
                                       1][col] = new_state[row+1][col], new_state[row][col]
    elif movement == "left":
        if col == 0:
            return None
        new_state[row][col], new_state[row][col -
                                            1] = new_state[row][col-1], new_state[row][col]
    elif movement == "right":
        if col == 2:
            return None
        new_state[row][col], new_state[row][col +
                                            1] = new_state[row][col+1], new_state[row][col]
    else:
        raise ValueError("Invalid movement: " + movement)
    return new_state


def get_blank_pos(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] is None:
                return row, col
    raise ValueError("Blank tile not found in state: " + str(state))


def print_path(path):
    for state in path:
        print_state(state)
        print()


def print_state(state):
    for row in state:
        print(row)
    print()


# Example usage
initial_state = [[2, 4, 3], [1, 5, 6], [7, 8, None]]
goal_state = [[2, 4, 3], [5, 1, None], [7, 8, 6]]

# 8 in this case is the max depth
for depth in range(1, 8):
    print("Searching depth", depth)
    path = [initial_state]
    if dfs(initial_state, goal_state, 0, depth, path):
        break
    else:
        print("No solution found within search depth limit.")

# Draw the final state of the board
draw_board(goal_state)

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
