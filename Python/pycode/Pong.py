#Pong
#Demos sprite collisions

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """A mouse-controlled paddle."""

    image = games.load_image("../Res/pong.jpg")

    def __init__(self):
        super(Pan, self).__init__(image = Pan.image, x = 0, y = games.mouse.y)
        self.score = games.Text(value = str(Pizza.bounces)+" bounces.", size = 25, color = color.black,
                                top = 5, right = games.screen.width - 70)
        games.screen.add(self.score)

    def update(self):
        """Move to match mouse coordinates."""
        self.x = 0
        self.y = games.mouse.y
        self.check_collide()
        self.score.value = str(Pizza.bounces)+" bounces."
    def check_collide(self):
        """Check for collision with pizza."""
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

class Pizza(games.Sprite):
    """A slippery pizza."""
    bounces = 0
    def update(self):
        """Move to a random screen location."""
        """Reverse a velocity component if an edge is reached."""
        if self.right>games.screen.width:
            self.dx = -self.dx
        if self.bottom>games.screen.height or self.top < 0:
            self.dy = -self.dy
        if self.left < 0:
            self.destroy()
            self.end_game()

    def handle_collide(self):
        self.dx = -(self.dx*1.1)
        self.dy = self.dy*1.1
        Pizza.bounces += 1

    def end_game(self):
        """ End the game. """
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
            
        
def main():
    wall_image = games.load_image("../Res/wall.jpg", transparent = False)
    games.screen.background = wall_image

    pizza_image = games.load_image("../Res/pizza.bmp")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    the_pizza = Pizza(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx = 1.5, dy = 1.5)
    games.screen.add(the_pizza)

    pan_image = games.load_image("../Res/pong.jpg")
    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

#do it!
main()
