import pgzrun
import random

#Screen Size
WIDTH = 1000
HEIGHT = 400

#Basket
basket = Actor("basket2")
basket.pos = (WIDTH//2, HEIGHT - 50)

#Falling Fruit
fruit = Actor("apple")
fruit.pos = (random.randint(50,WIDTH-50),0)

#Game Variables
score = 0 
lives = 3
speed = 3

def draw():
    screen.clear()
    screen.blit("background", (0,0)) 
    basket.draw()
    fruit.draw()
    screen.draw.text(f"Score: {score}", (10,10), fontsize = 30, color = "white")
    screen.draw.text(f"'Lives: {lives}", (10,50), fontsize=30, color = "white")
    if lives <=0:
        screen.fill("pink")
        screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop= (WIDTH/2,10), fontsize=40, color="red")

def update():
    global score, lives, speed

    #Move basket with arrow keys
    if keyboard.left and basket.x > 50:
        basket.x -=5
    if keyboard.right and basket.x < WIDTH - 50:
        basket.x +=5

    #Move Fruit Down
    fruit.y += speed

    #move fruit down
    if fruit.colliderect(basket):
        score += 1
        fruit.pos = (random.randint(50, WIDTH - 50), 0) # Rest Fruit Position
        speed += 0.2 # Increase difficulty

    #If fruit reached the bottom, lose a life
    if fruit.y > HEIGHT:
        lives -= 1
        fruit.pos = (random.randint(50,WIDTH - 50), 0)

    #End game if no lives left

pgzrun.go()