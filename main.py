import pygame
import time

pygame.init()
pygame.font.init()
# window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ping pong ")
FPS = 60
VEL = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)

SCORE_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comiscans", 100)
Name_FONT = pygame.font.SysFont("comicsans", 70)
# elements

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 2.5, HEIGHT)
LEFT_PAD = pygame.Rect((10, 10), (10, HEIGHT // 4))
RIGHT_PAD = pygame.Rect((880, 10), (10, HEIGHT // 4))
BALL = pygame.Rect((WIDTH / 2, HEIGHT / 2), (25, 25))


def left_pad_movement(keys, left_pad):
    if keys[pygame.K_w] and left_pad.y > 0:
        left_pad.y -= VEL
    if keys[pygame.K_s] and left_pad.y + VEL + left_pad.height < HEIGHT - 15:
        left_pad.y += VEL


def right_pad_movement(keys, right_pad):
    if keys[pygame.K_UP] and right_pad.y > 0:
        right_pad.y -= VEL
    if keys[pygame.K_DOWN] and right_pad.y + VEL + right_pad.height < HEIGHT - 15:
        right_pad.y += VEL


def ball_movement(ball, right_pad, left_pad, ball_speed_x, ball_speed_y):
    if right_pad.colliderect(ball):
        BALL.x += ball_speed_x
        BALL.y += ball_speed_y

    if left_pad.colliderect(ball):
        BALL.x += ball_speed_x
        BALL.y += ball_speed_y


def splash_screen():
    welcome_text = WINNER_FONT.render("Welcome To Pong", True, GREY)
    WIN.blit(welcome_text, (WIDTH / 2 - welcome_text.get_width() / 2, HEIGHT / 2 - welcome_text.get_height() / 2))
    name_text = Name_FONT.render("by alliance", True, GREY)
    WIN.blit(name_text, (WIDTH / 2 - name_text.get_width() / 2, HEIGHT / 2 - name_text.get_height() / 2))
    pygame.display.update()
    time.sleep(5)


def draw_window(left_score, right_score):
    WIN.fill(WHITE)
    left_score_text = SCORE_FONT.render("player1 :" + str(left_score), True, GREY)
    right_score_text = SCORE_FONT.render("player2 :" + str(right_score), True, GREY)
    WIN.blit(right_score_text, (WIDTH - right_score_text.get_width() - 10, 10))
    WIN.blit(left_score_text, (10, 10))
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.draw.ellipse(WIN, BLACK, BALL)
    pygame.draw.rect(WIN, BLACK, LEFT_PAD)
    pygame.draw.rect(WIN, BLACK, RIGHT_PAD)
    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, GREY)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    ball_speed_x = 1
    ball_speed_y = 1
    run = True
    left_score = 0
    right_score = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        winner_text = ""
        if left_score >= 10 and left_score > right_score:
            winner_text = "player 1 winns !!"
        if right_score >= 10 and right_score > left_score:
            winner_text = "player 2 winns !!"
        if right_score == left_score and right_score >= 10:
            winner_text = "Draw !!!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        BALL.x += ball_speed_x
        BALL.y += ball_speed_y

        if BALL.top <= 0 or BALL.bottom >= HEIGHT:
            ball_speed_y *= -1
        if BALL.left <= 0 or BALL.right >= WIDTH:
            ball_speed_x *= -1

        if BALL.right >= WIDTH and not RIGHT_PAD.colliderect(BALL):
            left_score += 1
        if BALL.x <= 0 and not LEFT_PAD.colliderect(BALL):
            right_score += 1

        if RIGHT_PAD.colliderect(BALL) or LEFT_PAD.colliderect(BALL):
            BALL.x += ball_speed_x

        keys = pygame.key.get_pressed()
        left_pad_movement(keys, LEFT_PAD)
        right_pad_movement(keys, RIGHT_PAD)
        draw_window(left_score, right_score)

    main()


if __name__ == "__main__":
    main()
