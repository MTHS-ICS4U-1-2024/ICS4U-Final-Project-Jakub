#!/usr/bin/env python3

"""
Created by: Jakub Malhotra
Created on: December 2024
This is my "VTEC Velocity" game for the Adafruit Pybadge
"""

@namespace
class SpriteKind:
    # Create the SpriteKinds not already created by makecode
    tree = SpriteKind.create()
    barricade = SpriteKind.create()

# Splash screen menu
def show_splash_screen():
    # Set a custom background color
    scene.set_background_color(150)
    
    # Create a splash image
    splash_image = image.create(160, 120)
    splash_image.fill(150)
    
    # Print the title on the splash image
    title = "VTEC Velocity!"
    x_position = (splash_image.width - len(title) * 6) // 2  # Approximate centering
    y_position = splash_image.height // 2 - 8  # Center vertically
    splash_image.print(title, x_position, y_position, 6)  # Print in black
    
    # Set the splash image as the background
    scene.set_background_image(splash_image)
    
    # Show a welcome message with instructions
    game.show_long_text(
        "Welcome to VTEC Velocity!",
        DialogLayout.CENTER
    )
    
    # Wait until the user presses the A button
    while not controller.A.is_pressed():
        pause(100)

# Call the splash screen function
show_splash_screen()

# Set the background image
scene.set_background_image(assets.image("""
    background
"""))

# Define the Player class
class Player:
    player_image = img("""
        . . . . . . e e c c e e . . . .
        . . . . . e 2 2 2 2 2 2 e . . .
        . . . . 2 c 2 2 2 2 2 2 c 2 . .
        . . . e 2 c 4 2 2 2 2 2 c 2 e .
        . . . f 2 2 4 2 2 2 2 2 c 2 f .
        . . . f 2 2 4 2 2 2 2 2 2 2 f .
        . . . f 2 2 4 2 2 2 2 2 2 2 f .
        . . . f 2 c 2 4 4 2 2 2 c 2 f .
        . . . e 2 c e c c c c e c 2 e .
        . . . e 2 e c b b b b c e 2 e .
        . . . e 2 e b b b b b b e 2 e .
        . . . e e e e e e e e e e e e .
        . . . f e d e e e e e e d e f .
        . . . f e 2 d e e e e d 2 e f .
        . . . f f e e e e e e e e f f .
        . . . . f f . . . . . . f f . .
    """)

    def __init__(self):
        self.sprite = sprites.create(self.player_image, SpriteKind.player)
        self.sprite.set_stay_in_screen(True)
        controller.move_sprite(self.sprite)
        self.road_min_x = 38  # Left boundary of the road
        self.road_max_x = 122  # Right boundary of the road

    def move(self):
        # Restrict the player's movement to within the road boundaries
        if self.sprite.x < self.road_min_x:
            self.sprite.x = self.road_min_x
        elif self.sprite.x > self.road_max_x:
            self.sprite.x = self.road_max_x

class Tree:
    tree_image = img("""
        ......cc66......
        .....c6576c.....
        ....c677576c....
        ....cc677666....
        ...cc6c6667cc...
        ..6c666777cc6c..
        ..c76666766776..
        ..c6777777776c..
        ..cc67777776cc..
        .c67cc76676676c.
        .c777666667777c.
        .c6777777777766.
        .cc7767776776666
        c676cc6766666776
        c777766666677776
        cc7777777777776c
        .c676777677767c.
        ..cc667666766c..
        ...ccc6c66ccc...
        .....cccccc.....
        .......ee.......
        ......eeee......
        .....eeeeee.....
        .......ee.......
    """)

    def __init__(self, x, y):
        self.sprite = sprites.create(self.tree_image, SpriteKind.tree)
        self.sprite.set_position(x, y)
        self.speed = 1

    def update(self):
        self.sprite.y += self.speed
        if self.sprite.y > 120:
            self.sprite.y = 0

# Define the Barricade class
class Barricade:
    barricade_image = img("""
        .........22..........22.........
        .........22..........22.........
        .........cc..........cc.........
        cccccccccccccccccccccccccccccccc
        c444111444111444111444111444111c
        c144411144411144411144411144411c
        c114441114441114441114441114441c
        c111444111444111444111444111444c
        c411144411144411144411144411144c
        c441114441114441114441114441114c
        c444111444111444111444111444111c
        cccccccccccccccccccccccccccccccc
        .....cc..................cc.....
        ....cc....................cc....
        ...cc......................cc...
        ..cc........................cc..
    """)

    def __init__(self, x, y):
        self.sprite = sprites.create(self.barricade_image, SpriteKind.barricade)
        self.sprite.set_position(x, y)
        self.speed = 1

    def update(self):
        # Move the barricade down
        self.sprite.y += self.speed
        # Reset to the top when it goes off-screen
        if self.sprite.y > 120:
            self.sprite.y = 0
            # Set x randomly within the road boundary
            self.sprite.x = randint(48,112)

# Define the GameManager class
class GameManager:
    def __init__(self):
        self.player = Player()
        self.score = 0
        info.set_score(self.score)
        # Manages the trees
        self.tree_1 = Tree(16, 42)
        self.tree_2 = Tree(16, 85)
        self.tree_3 = Tree(16, 127)
        self.tree_4 = Tree(144, 42)
        self.tree_5 = Tree(144, 85)
        self.tree_6 = Tree(144, 127)
        # Manages the barricades
        self.barricade_1 = Barricade(52, 0)

    def update(self):
        # Update trees
        self.tree_1.update()
        self.tree_2.update()
        self.tree_3.update()
        self.tree_4.update()
        self.tree_5.update()
        self.tree_6.update()
        # Update barricades
        self.barricade_1.update()

# Collision check
        if self.player.sprite.overlapsWith(self.barricade_1.sprite):
            # Play a game over melody
            music.play_melody("C5 B A G F E D C ", 240)
            score_message = "Your Score: " + str(self.score)
            game.splash("Game Over!", score_message)
            game.reset()

# Update the increment_score function
def increment_score():
    game_manager.score += 1  # Increase score
    info.set_score(game_manager.score)  # Update score display

    # Every time the score reaches a multiple of 75, increase speed by 0.5, play sound effect and display text
    if game_manager.score % 75 == 0:
        for tree in [game_manager.tree_1, game_manager.tree_2, game_manager.tree_3, game_manager.tree_4, game_manager.tree_5, game_manager.tree_6]:
            tree.speed += 0.5
        game_manager.barricade_1.speed += 0.5
        music.play(music.melody_playable(music.big_crash), music.PlaybackMode.UNTIL_DONE)
        # Speech bubble for 750 milliseconds
        game_manager.player.sprite.say_text("VTEC just kicked in yo", 750)
        
# Increment score every 150 milliseconds
game.on_update_interval(150, increment_score)

# Initialize the GameManager
game_manager = GameManager()

# Game update function
def on_update():
    game_manager.update()
    game_manager.player.move()

game.on_update(on_update)