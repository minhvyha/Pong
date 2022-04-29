import pygame

pygame.init()
WIDTH = 700
HEIGHT = 500

BLUE = (10,174,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (217,11,32)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')




FPS = 80

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

FONT = pygame.font.SysFont('comicsans', 50)
FONT_start = pygame.font.SysFont('comicsans', 37)
FONT_start_small = pygame.font.SysFont('comicsans', 20)

class Paddle:
    VEL = 3.5
    def __init__(self, x, y, width, height, color):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, 2.5))
        pygame.draw.rect(win, WHITE, (self.x, self.y, 2.5, self.height))
        pygame.draw.rect(win, WHITE, (self.x, self.y + self.height, self.width, 2.5))
        pygame.draw.rect(win, WHITE, (self.x + self.width, self.y, 2.5, self.height+ 2.5))

    def move(self, up):
        if up and (self.y - self.VEL) > 5:
            self.y -= self.VEL
            return
        if (self.y + self.VEL) < HEIGHT - 9 - self.height:
            self.y += self.VEL

    def reset(self):
        self.y = self.origin_y
        self.x = self.origin_x

class Ball:
    VEL = 5

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.y_vel
        self.x += self.x_vel

def main(win):
    run = True
    clock = pygame.time.Clock()

    left = Paddle(10, (HEIGHT/2 - PADDLE_HEIGHT/2), PADDLE_WIDTH, PADDLE_HEIGHT, BLUE)
    right = Paddle(WIDTH - 28, (HEIGHT / 2 - PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT, RED)
    left_point = 0
    right_point = 0
    ball = Ball(WIDTH//2, HEIGHT//2, 6)
    r = False
    t = ''
    started = False
    end = False
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            started = True
        if keys[pygame.K_r] and end == True:
            end = False
        if not started:
            draw_start(win, [left, right])
            continue
        if left_point >= 10:
            t = FONT_start.render('Left Player WIN!!!', 1, WHITE)
            end = True
            r = True
            left_point = 0
            right_point = 0
        if right_point >= 10:
            t = FONT_start.render('Right Player WIN!!!', 1, WHITE)
            end = True
            r = True
            left_point = 0
            right_point = 0
        if end:
            draw_end(win, [left, right],t)

            pygame.display.update()
            continue
        if r:
            reset(ball)
            left.reset()
            right.reset()

            r = False
            end = False

        else:
            draw(win, [left, right], ball, left_point, right_point)
        clock.tick(FPS)
        handle_key(keys, left, right)
        handle_coll(ball, left, right)
        ball.move()

        if ball.x < 1:
            right_point += 1
            reset(ball)
        if ball.x > WIDTH:
            left_point += 1
            reset(ball)


    pygame.quit()


def reset(ball):
    ball.x = WIDTH // 2
    ball.y = HEIGHT // 2
    ball.y_vel = 0
    ball.x_vel *= -1

def handle_coll(ball, left, right):
    if ball.y - ball.radius < 3 or ball.y + ball.radius > HEIGHT - 5:
        ball.y_vel *= -1
        return

    if ball.x_vel < 0:
        if ball.x - ball.radius < left.x + PADDLE_WIDTH and ball.x > 10 and ball.y > left.y and ball.y < left.y + PADDLE_HEIGHT:
            ball.x_vel *= -1
            difference =  ball.y - (left.y + PADDLE_HEIGHT/2)
            ratio = (PADDLE_HEIGHT / 2) / ball.VEL
            ball.y_vel = difference / ratio
            return

    if ball.x_vel > 0:
        if ball.x + ball.radius > right.x and ball.x > WIDTH - 28 and ball.y > right.y and ball.y < right.y + PADDLE_HEIGHT:
            ball.x_vel *= -1
            difference = ball.y - (right.y + PADDLE_HEIGHT / 2)
            ratio = (PADDLE_HEIGHT / 2) / ball.VEL
            ball.y_vel = difference / ratio
            return

def handle_key(keys, left, right):
    if keys[pygame.K_w]:
        left.move(True)
    if keys[pygame.K_s]:
        left.move(False)
    if keys[pygame.K_UP]:
        right.move(True)
    if keys[pygame.K_DOWN]:
        right.move(False)



def draw(win, paddles=None, ball=None, left='', right=''):
    win.fill(BLACK)

    left_score = FONT.render(f'{left}', 1, WHITE)
    right_score = FONT.render(f'{right}', 1, WHITE)
    win.blit(left_score, (WIDTH // 4 - left_score.get_width(), 20))
    win.blit(right_score, (WIDTH // 4 * 3 - right_score.get_width(), 20))
    for paddle in paddles:
        paddle.draw(win)
    x = WIDTH // 2 - 15 // 2
    ball.draw(win)
    for i in range(10, HEIGHT - 10, 50):
        pygame.draw.rect(win, WHITE, (x, i, 15, 20))

    pygame.display.update()

def draw_end(win, paddles=None, t=''):
    win.fill(BLACK)

    reset = FONT_start_small.render('Press R To Reset', 1, WHITE)
    congrat = FONT_start.render('Congratulation', 1, WHITE)
    win.blit(congrat, (WIDTH // 2 - congrat.get_width() // 2, 40))
    win.blit(t, (WIDTH // 2 - t.get_width() // 2, 120))

    win.blit(reset, (WIDTH // 2 - reset.get_width()//2, 200))

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def draw_start(win, paddles=None):
    win.fill(BLACK)

    start = FONT_start.render('PONG', 1, WHITE)
    intro = FONT_start.render('First to 10 WIN!!!', 1, WHITE)
    space = FONT_start_small.render('Press Space To Start', 1, WHITE)
    credit = FONT_start_small.render('CREDIT to "TECH WITH TIM"', 1, WHITE)
    minh = FONT_start_small.render('Improve by Minh Vy Ha', 1, WHITE)
    win.blit(start, (WIDTH // 2 - start.get_width() // 2, 20))
    win.blit(intro, (WIDTH // 2 - intro.get_width() // 2, 80))
    win.blit(space, (WIDTH // 2 - space.get_width() // 2, 150))
    win.blit(credit, (WIDTH // 2 - credit.get_width() // 2, 200))
    win.blit(minh, (WIDTH // 2 - minh.get_width() // 2, 250))
    x = WIDTH // 2 - 15 // 2
    for i in range(310, HEIGHT - 10, 50):
        pygame.draw.rect(win, WHITE, (x, i, 15, 20))
    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()
if __name__ == '__main__':
    main(win)