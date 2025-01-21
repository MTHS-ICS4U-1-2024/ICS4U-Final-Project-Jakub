// !/usr/bin/env python3
/** 
Created by: Jakub Malhotra
Created on: December 2024
This is my "VTEC Velocity" game for the Adafruit Pybadge

 */
namespace SpriteKind {
    //  Create the SpriteKinds not already created by makecode
    export const tree = SpriteKind.create()
    export const barricade = SpriteKind.create()
}

//  Splash screen menu
function show_splash_screen() {
    //  Set a custom background color
    scene.setBackgroundColor(150)
    //  Create a splash image
    let splash_image = image.create(160, 120)
    splash_image.fill(150)
    //  Print the title on the splash image
    let title = "VTEC Velocity!"
    let x_position = Math.idiv(splash_image.width - title.length * 6, 2)
    //  Approximate centering
    let y_position = Math.idiv(splash_image.height, 2) - 8
    //  Center vertically
    splash_image.print(title, x_position, y_position, 6)
    //  Print in black
    //  Set the splash image as the background
    scene.setBackgroundImage(splash_image)
    //  Show a welcome message with instructions
    game.showLongText("Welcome to VTEC Velocity!", DialogLayout.Center)
    //  Wait until the user presses the A button
    while (!controller.A.isPressed()) {
        pause(100)
    }
}

//  Call the splash screen function
show_splash_screen()
//  Set the background image
scene.setBackgroundImage(assets.image`
    background
`)
//  Define the Player class
class Player {
    static player_image: Image
    private ___player_image_is_set: boolean
    private ___player_image: Image
    get player_image(): Image {
        return this.___player_image_is_set ? this.___player_image : Player.player_image
    }
    set player_image(value: Image) {
        this.___player_image_is_set = true
        this.___player_image = value
    }
    
    sprite: Sprite
    road_min_x: number
    road_max_x: number
    public static __initPlayer() {
        Player.player_image = img`
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
    `
    }
    
    constructor() {
        this.sprite = sprites.create(this.player_image, SpriteKind.Player)
        this.sprite.setStayInScreen(true)
        controller.moveSprite(this.sprite)
        this.road_min_x = 38
        //  Left boundary of the road
        this.road_max_x = 122
    }
    
    //  Right boundary of the road
    public move() {
        //  Restrict the player's movement to within the road boundaries
        if (this.sprite.x < this.road_min_x) {
            this.sprite.x = this.road_min_x
        } else if (this.sprite.x > this.road_max_x) {
            this.sprite.x = this.road_max_x
        }
        
    }
    
}

Player.__initPlayer()

class Tree {
    static tree_image: Image
    private ___tree_image_is_set: boolean
    private ___tree_image: Image
    get tree_image(): Image {
        return this.___tree_image_is_set ? this.___tree_image : Tree.tree_image
    }
    set tree_image(value: Image) {
        this.___tree_image_is_set = true
        this.___tree_image = value
    }
    
    sprite: Sprite
    speed: number
    public static __initTree() {
        Tree.tree_image = img`
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
    `
    }
    
    constructor(x: number, y: number) {
        this.sprite = sprites.create(this.tree_image, SpriteKind.tree)
        this.sprite.setPosition(x, y)
        this.speed = 1
    }
    
    public update() {
        this.sprite.y += this.speed
        if (this.sprite.y > 120) {
            this.sprite.y = 0
        }
        
    }
    
}

Tree.__initTree()

//  Define the Barricade class
class Barricade {
    static barricade_image: Image
    private ___barricade_image_is_set: boolean
    private ___barricade_image: Image
    get barricade_image(): Image {
        return this.___barricade_image_is_set ? this.___barricade_image : Barricade.barricade_image
    }
    set barricade_image(value: Image) {
        this.___barricade_image_is_set = true
        this.___barricade_image = value
    }
    
    sprite: Sprite
    speed: number
    public static __initBarricade() {
        Barricade.barricade_image = img`
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
    `
    }
    
    constructor(x: number, y: number) {
        this.sprite = sprites.create(this.barricade_image, SpriteKind.barricade)
        this.sprite.setPosition(x, y)
        this.speed = 1
    }
    
    public update() {
        //  Move the barricade down
        this.sprite.y += this.speed
        //  Reset to the top when it goes off-screen
        if (this.sprite.y > 120) {
            this.sprite.y = 0
            //  Set x randomly within the road boundary
            this.sprite.x = randint(48, 112)
        }
        
    }
    
}

Barricade.__initBarricade()

//  Define the GameManager class
class GameManager {
    player: Player
    score: number
    tree_1: Tree
    tree_2: Tree
    tree_3: Tree
    tree_4: Tree
    tree_5: Tree
    tree_6: Tree
    barricade_1: Barricade
    constructor() {
        this.player = new Player()
        this.score = 0
        info.setScore(this.score)
        //  Manages the trees
        this.tree_1 = new Tree(16, 42)
        this.tree_2 = new Tree(16, 85)
        this.tree_3 = new Tree(16, 127)
        this.tree_4 = new Tree(144, 42)
        this.tree_5 = new Tree(144, 85)
        this.tree_6 = new Tree(144, 127)
        //  Manages the barricades
        this.barricade_1 = new Barricade(52, 0)
    }
    
    public update() {
        let score_message: any;
        //  Update trees
        this.tree_1.update()
        this.tree_2.update()
        this.tree_3.update()
        this.tree_4.update()
        this.tree_5.update()
        this.tree_6.update()
        //  Update barricades
        this.barricade_1.update()
        //  Collision check
        if (this.player.sprite.overlapsWith(this.barricade_1.sprite)) {
            //  Play a game over melody
            music.playMelody("C5 B A G F E D C ", 240)
            score_message = "Your Score: " + ("" + this.score)
            game.splash("Game Over!", score_message)
            game.reset()
        }
        
    }
    
}

//  Update the increment_score function
//  Increment score every 150 milliseconds
game.onUpdateInterval(150, function increment_score() {
    game_manager.score += 1
    //  Increase score
    info.setScore(game_manager.score)
    //  Update score display
    //  Every time the score reaches a multiple of 75, increase speed by 0.5, play sound effect and display text
    if (game_manager.score % 75 == 0) {
        for (let tree of [game_manager.tree_1, game_manager.tree_2, game_manager.tree_3, game_manager.tree_4, game_manager.tree_5, game_manager.tree_6]) {
            tree.speed += 0.5
        }
        game_manager.barricade_1.speed += 0.5
        music.play(music.melodyPlayable(music.bigCrash), music.PlaybackMode.UntilDone)
        //  Speech bubble for 750 milliseconds
        game_manager.player.sprite.sayText("VTEC just kicked in yo", 750)
    }
    
})
//  Initialize the GameManager
let game_manager = new GameManager()
//  Game update function
game.onUpdate(function on_update() {
    game_manager.update()
    game_manager.player.move()
})
