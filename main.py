import pygame, random
from func import col
pygame.init()

w = 600
h = 600
screen_size = (w+h)//2
font = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Game")
obs = []

class pl:
    x = int(w / 2)
    y = int(h / 2)
    w = int(w / 50)
    h = int(h / 50)
    speed = int(screen_size / 300)
    size = int(w / 100)
    color = (0, 0, 255)

class block:
    x = int(screen_size / 2)
    y = int(screen_size / 2)
    w = int(screen_size / 25)
    h = int(screen_size / 25)
    size = int(w / 100)
    color = (0, 255, 200)
    sprite = 0
    @classmethod
    def create(cls):
        return cls()
loop = 0
clock = pygame.time.Clock()
jump = False
for i in range(20):
    obs.append(block.create())
    obs[i].x = random.randint(0, w)
    obs[i].y = random.randint(0, h)
y_change = 1
while True:
    #print(obs)
    x_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if pygame.key.get_pressed()[pygame.K_d] == 1:
        x_change = pl.speed
    elif pygame.key.get_pressed()[pygame.K_a] == 1:
        x_change = -pl.speed

    if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
        if jump == False:
            loop = 500
            y_change = -4
            jump = True

    if y_change < 2w:
        y_change += 0.1
    elif y_change > 2:
        jump = False

    for obj in obs:
        if col(pl, obj):
            print("collision")
            print(obj.x, obj.y)

            if pl.x > obj.x and pl.y + pl.h/2 < obj.y + obj.h/2 +5 and pl.y - pl.h/2 > obj.y - obj.h/2 -5: pl.x  = obj.x +obj.w/2 + pl.w/2
            elif pl.x < obj.x and pl.y + pl.h/2 < obj.y + obj.h/2 +5 and pl.y - pl.h/2 > obj.y - obj.h/2 -5: pl.x = obj.x -obj.w/2 - pl.w/2
            elif pl.y > obj.y: pl.y = obj.y +obj.h/2 + pl.h/2
            elif pl.y < obj.y: pl.y = obj.y -obj.h/2 - pl.h/2

    if pl.x < 0: pl.x = 0
    if pl.x > w: pl.x = w
    if pl.y < 0: pl.y = 0
    if pl.y > h: pl.y = h

    pl.x += x_change
    pl.y += y_change
    screen.fill((0, 200, 100))
    for obj in obs:
        pygame.draw.rect(screen, obj.color, (obj.x - int(obj.w / 2), obj.y - int(obj.h / 2), obj.w, obj.h), obj.size)
    pos = font.render(f"x:{pl.x} y:{pl.y}", True, (255, 255, 255))
    screen.blit(pos, (10, 5))
    pygame.draw.rect(screen, pl.color, (int(pl.x-(pl.w/2)), int(pl.y-(pl.h/2)), int(pl.w), int(pl.h)), pl.size)
    pygame.draw.circle(screen, (255, 0, 0), (int(pl.x), int(pl.y)), 2)
    #pygame.draw.rect(screen, pl.color, (pl.x, pl.y, int(pl.w), int(pl.h)), pl.size)
    pygame.display.update()
    clock.tick(60)