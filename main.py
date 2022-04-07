# Simple pygame program

# Import and initialize the pygame library
from logic import broad, fix_spot, getPlayer, print_broad, isFilled, checkWinner
from heuristic import findBestMove
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

curr_turn = 1
rect_width = 100
rect_start_x = 0
rect_start_y = 0

def gridClick(x, y):
    r = 0
    c = 0
    r = (x - rect_start_x) // rect_width
    c = (y - rect_start_y) // rect_width
    if r < 3 and c < 3:
        return (r, c)
    else:
        return None

def get_center_icon(r, c):
    return (
        rect_start_x + (c + 0.5) * rect_width,
        rect_start_y + (r + 0.5) * rect_width,
    )

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # pos = (x, y)
            G = gridClick(pos[0], pos[1])
            if G != None and curr_turn == 1:
                # print(isFilled(G[0], G[1]))
                if not isFilled(G[0], G[1]):
                    if curr_turn == 1:
                        fix_spot(G[0], G[1], curr_turn)
                    curr_turn = 2
                print(curr_turn)
                print_broad()
                win = checkWinner()
                print(win)
                if win != 0:
                    running = False

    if curr_turn == 2:
        best_move = findBestMove(broad)
        fix_spot(best_move[1], best_move[0], curr_turn)
        curr_turn = 1

    # Fill the background with white
    screen.fill((255, 255, 255))

    for r in range(3):
        for c in range(3):
            color = (100, 0, 0) if (c+r) % 2 == 0 else (0, 0, 100)
            empty_rect = pygame.Rect(rect_start_x + r*rect_width, rect_start_y + c * rect_width, rect_width, rect_width)
            pygame.draw.rect(screen, color, empty_rect)
    for r in range(3):
        for c in range(3):
            if getPlayer(broad[r][c]) == 1:
                p = get_center_icon(r, c)
                pygame.draw.circle(screen, (0, 0, 255), p, 30)
            if getPlayer(broad[r][c]) == 2:
                p = get_center_icon(r, c)
                pygame.draw.circle(screen, (255, 0, 0), p, 30)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


