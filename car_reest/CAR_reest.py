from pygame import * 
from random import randint 
from time import time as timer
win_width = 700
win_heigt = 500 
window = display.set_mode( 
    (win_width ,win_heigt) 

)     

img_back=" st4_big.jpg " 
img_hero="pngtree-sniper-score-lens-png-image_1729776.jpg" 
img_enemy="480494456.png" 
img_back="png-transparent-paper-AIR-sticker-adhesive-planet-asteroid-child-sleep-slate.png"
score = 0 
lost = 0 
goal = 20
life = 3
display.set_caption("AVIA FIRE") 
background = transform.scale(image.load(img_back),(win_width , win_heigt))   


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 

class Player(GameSprite):
   
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self): 
    
    
finish = False   
score = 0 
lost = 0 
num_fire = 0 
life = 3
for b in bullets:
    b.kill() 
for m in bad
    m.kill() 
for a in:avia
    a.kill()

time.delay(3000)  
for i  in range (1,6): 
    monster = Enemy(img_enemy, randint(80, win_width - 80),-40, 80 , 50 , randint(1,5)) 
    monsters.add(monster) 
for i in range(1 , 3) :
    AIR = Enemy(img_ast, randint(30, win_width - 30)) ,-40, 80, 50 randint(1, 7) 
    asteroids.add(asteroid)

rel_time = False 

for c in collides: 
    score = score + 1
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40 , 80 , 50 , randint(1, 5)) 
    monsters.add(monster) 

if sprite.spritecollide(AIM ,AIR,  , False ) or sprite.spritecollide(AIM  , AIRS , False):



num fire = 0

run =  True 
Bullets = sprite.Group()
while run:
    for e in event.get(): 
        if e.type == QUIT: 
            run = False  
        elif e.type == keydown:
            if e.key == K_SPACE:
                if num_fire <5 and rel_time == False:
                    num_fire = num_fire + 1 
                    fire_sound.play() 
                    ship.fire 

                if num_fire >=5 and  rel_time == False :
                    last_time = timer() 
                    rel_time = True  

    if not finish:
        window.blit(background, (0,0)) 
        text = font2.render("счёт:" +str(score), 1, (255, 255, 255)) 
        window.blit(text,(10, 20)) 

        text_lose = font2.render("пропущено:" + str(lost), 1, (255, 255 , 255)) 

    ship.update() 
    monsters.update() 
    bullets.update() 
      rel_time = False 

collides =  sprite.groupcollide(monsters , bullets , True , True) 
for c in collides: 
    score = score + 1
    AIR = Enemy(img_enemy, randint(80, win_width - 80), -40 , 80 , 50 , randint(1, 5)) 
    monsters.add(monster) 

if sprite.spritecollide(AIM AIR,  , False ) or sprite.spritecollide( AIM ,AIR ,  , False):


num fire = 0

run =  True 
Bullets = sprite.Group()
while run:
    for e in event.get(): 
        if e.type == QUIT: 
            run = False  
        elif e.type == keydown:
            if e.key == K_SPACE:
                if num_fire <5 and rel_time == False:
                    num_fire = num_fire + 1 
                    fire_sound.play() 
                    ship.fire 

                if num_fire >=5 and  rel_time == False :
                    last_time = timer() 
                    rel_time = True

    if not finish:
        window.blit(background, (0,0)) 
        text = font2.render("счёт:" +str(score), 1, (255, 255, 255)) 
        window.blit(text,(10, 20)) 

        text_lose = font2.render("пропущено:" + str(lost), 1, (255, 255 , 255)) 

    ship.update() 
    monsters.update() 
    bullets.update() 


if rel_time  == True: 
    now_time = timer() 

    if now_time - last_time < 3: 
        reload = font2.render('перезарядка...',1, (150, 0 ,0)) 
        window.blit(reload , (260 , 460)) 
    else:
        num_fire = 0 
         rel_time = False
 



collides = sprite.groupcollide(AIR s, bullets, True, True ) 
for c in collides: 
    score = score + 1 
    AIR = Enemy(img_enemy , randint(80,)-40, 80, 50 ,randint (1,5))
    monsters.add(monster)

if sprite.spritecollide(AIM, AIR , False) or lost >= max_lost:
    finish = True 
    window.blit(lose, (200 , 200)) 

    if score >= goal: 
        finish = True 
        widow.blit(win ,(200 , 200))    


if life == 3: 
    life_color =  (0, 150, 0) 
if life == 2:
    life_color = (150, 150 , 0) 
if  life==1 
