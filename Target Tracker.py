from pygame import *
import sys
from random import randint

# resimler
aim_pic = "crosshair.png"
hedef_pic = "target.png"

font.init()
font1 = font.Font(None,36)

# pencere boyutu
screen_width = 800
screen_height = 600

screen = display.set_mode((screen_width, screen_height))
display.set_caption("aim game")
mouse.set_visible(False)


WHITE = (255, 255, 255)
GREY = (150,150,150)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# hedef sprite'ı ve zaman takipçisi
hedef = GameSprite(hedef_pic, randint(0, 720), randint(0, 500), 80, 100)
hedef_timer = time.get_ticks()  # ms cinsinden zaman takibi

clock = time.Clock()

puan = 0

# oyun döngüsü
while True:
    mouse_pos = mouse.get_pos()

    # aim sprite'ı mouse pozisyonuna göre her döngüde güncelleniyor
    aim = GameSprite(aim_pic, mouse_pos[0] - 30, mouse_pos[1] - 30, 60, 60)

    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if aim.rect.colliderect(hedef.rect):
                    hedef.rect.x = randint(0, 720)  # 800 - hedef genişliği
                    hedef.rect.y = randint(0, 500)  # 600 - hedef yüksekliği
                    puan += 1
                    print(puan)

    # her 5 saniyede bir hedefin yerini değiştir
    current_time = time.get_ticks()
    if current_time - hedef_timer > 3000:
        hedef.rect.x = randint(0, 720)  # 800 - hedef genişliği
        hedef.rect.y = randint(0, 500)  # 600 - hedef yüksekliği
        hedef_timer = current_time

    screen.fill(GREY)

    text = font1.render("Puan: " + str(puan), 1, (255, 0, 0))
    screen.blit(text, (10, 20))

    
    hedef.reset()
    aim.reset()


    display.flip()
    clock.tick(60)

