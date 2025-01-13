#!/usr/bin/env python3

"""
Created: By Jakub Malhotra
Created: On December 2024
This is my "VTEC Velocity" game for the Adafruit Pybadge
"""

@namespace
class SpriteKind:
    tree = SpriteKind.create()
    player = SpriteKind.create()

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

    def move(self):
        controller.move_sprite(self.sprite)

# Define the Tree class
class Tree:
    def __init__(self, img_data, x, y):
        self.sprite = sprites.create(img_data, SpriteKind.tree)
        self.sprite.set_position(x, y)

    def update(self):
        self.sprite.y += 1
        if self.sprite.y > 120:
            self.sprite.y = 0

# Define the GameManager class
class GameManager:
    def __init__(self):
        self.player = Player()
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
        """), 10, 99)
        self.tree_2 = Tree(img("""
            ...............cc...............
            ............ccc65c66............
            ............c6c55c76............
            ...........6cc7557c66...........
            ..........cc77777577c6..........
            .........666c677776cc66.........
            ........c7776c7c67657576........
            ........ccc666c666655666........
            ......c66cc7666667777c6766......
            .....c777c77667667767767776.....
            .....cc66cccc77c677cc666666.....
            ....c6766666c7c6767677777766....
            ...cc777666666677767777667c66...
            .666cc6677666667777777776677666.
            .67776677c676677777776677677776.
            cc6666ccc67767776777776cc7767666
            c666777667766776c776777c67776c66
            .c6777666ccc667c676cc666667776c.
            .cc6666766666cc66666666776cc666.
            ...66776c666666666677667766cccc.
            ...cc76c66766666667677667776c...
            ...6cccc677666666776777c77666...
            ......6ccc7c67767776c776cc......
            ........ccc6777c67776cc6........
            ...........cc77c67766...........
            .............6c6666.............
            ............ffeeeef.............
            ..........ffeeeeeeeef...........
            .............feeeffe............
            ..............fef...............
            ..............fef...............
            ...............f................
        """), 16, 57)

    def update(self):
        self.tree_1.update()
        self.tree_2.update()

# Initialize the GameManager
game_manager = GameManager()

# Game update function
def on_on_update():
    game_manager.update()

game.on_update(on_on_update)
