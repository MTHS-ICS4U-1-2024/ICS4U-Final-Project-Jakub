#!/usr/bin/env python3

"""
Created: By Jakub Malhotra
Created: On December 2024
This is my "VTEC Velocity" game on the Adafruit Pybadge
"""

import stage
import ugame


def game_scene() -> None:
    """
    This is the main function game scene
    """

    # image bank for circuit python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set the background to image 0 in the image bank
    #   and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8 )

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order 
    game.layers = [background]

    # render all sprites
    #   most likley you will only render the background once per game scene 
    game.render_block()

    # repeat forever, game loop
    while True:
        pass  # Just a placeholder for now


if __name__ == "__main__":
    game_scene()
