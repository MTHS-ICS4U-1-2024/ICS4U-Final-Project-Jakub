#!/usr/bin/env python3

"""
Created: By Jakub Malhotra
Created: On December 2024
This is my "VTEC Velocity" game for the Adafruit Pybadge
"""

@namespace
class SpriteKind:
    # Create the SpriteKinds not already created by makecode
    tree = SpriteKind.create()
    barricade = SpriteKind.create()

# Splash screen menu
def show_splash_screen():
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
    def __init__(self):
        self.sprite = sprites.create(img("""
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
        """), SpriteKind.player)
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

# Define the Tree class
class Tree:
    def __init__(self, img_data, x, y):
        self.sprite = sprites.create(img_data, SpriteKind.tree)
        self.sprite.set_position(x, y)

    def update(self):
        self.sprite.y += 1
        if self.sprite.y > 120:
            self.sprite.y = 0

# Define the Barricade class
class Barricade:
    def __init__(self, img_data, x, y):
        self.sprite = sprites.create(img_data, SpriteKind.create())
        self.sprite.set_position(x, y)

    def update(self):
        # Move the barricade down
        self.sprite.y += 1
        # Reset to the top when it goes off-screen
        if self.sprite.y > 120:
            self.sprite.y = 0
            # Set x randomly within the road boundary
            self.sprite.x = randint(48,112)


# Define the GameManager class
class GameManager:
    def __init__(self):
        self.player = Player()
        # Manages the trees
        self.tree_1 = Tree(img("""
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
        """), 16, 42)
        self.tree_2 = Tree(img("""
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
        """), 16, 85)
        self.tree_3 = Tree(img("""
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
        """), 16, 127)
        self.tree_4 = Tree(img("""
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
        """), 144, 42)
        self.tree_5 = Tree(img("""
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
        """), 144, 85)
        self.tree_6 = Tree(img("""
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
        """), 144, 127)
        # Manages the barricades
        self.barricade_1 = Barricade(img("""
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
        """), 52, 0)


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
        if (self.player.sprite.overlapsWith(self.barricade_1.sprite)):
            # Play a game over melody
            music.play_melody("C5 B A G F E D C ", 240)
            game.splash("Game Over!", "Press A to restart")
            game.reset()

# Initialize the GameManager
game_manager = GameManager()

# Game update function
def on_on_update():
    game_manager.update()
    game_manager.player.move()

game.on_update(on_on_update)