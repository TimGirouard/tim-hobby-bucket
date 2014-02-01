#Explosion
#Demos an animation

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

nebula_image = games.load_image("../Res/nebula.jpg", transparent=False)
games.screen.background = nebula_image

explosion_files = ["../Res/explosion1.bmp",
                   "../Res/explosion2.bmp",
                   "../Res/explosion3.bmp",
                   "../Res/explosion4.bmp",
                   "../Res/explosion5.bmp",
                   "../Res/explosion6.bmp",
                   "../Res/explosion7.bmp",
                   "../Res/explosion8.bmp",
                   "../Res/explosion9.bmp"]

explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats=0,
                                repeat_interval = 5)
games.screen.add(explosion)

games.screen.mainloop()
