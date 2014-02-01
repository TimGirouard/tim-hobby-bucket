#Pizza Panic
#Players must catch falling pizzas before they hit the ground

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """A mouse-controlled pan to catch the pizzas."""
    image = games.load_image("../Res/pan.bmp")
    #games.screen.add(the_pan)
    def __init__(self):
        """Initialize Pan object and create Text object for score."""
        super(Pan,self).__init__(image = Pan.image,
                        x = games.mouse.x,
                        bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width-10)
        games.screen.add(self.score)
        self.speedboard = games.Text(value = Pizza.speed, size = 25, color = color.black,
                                top = 5, left = 100)
        games.screen.add(self.speedboard)
        level_message = games.Message(value="Level 1",size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps)
        games.screen.add(level_message)

    def update(self):
        """Move to match mouse's x coordinate."""
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        """Check if pizza is caught."""
        for pizza in self.overlapping_sprites:
            self.score.value += 10 * Pizza.level
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
            self.speedboard.value = Pizza.speed

class Pizza(games.Sprite):
    """A falling pizza."""
    image = games.load_image("../Res/pizza.bmp")
    speed = 1
    level = 2
    count = 0

    def __init__(self,x,y=90):
        """ Initialize a pizza object."""
        super(Pizza, self).__init__(image = Pizza.image,
                                    x=x,y=y,dy=Pizza.speed)

    def update(self):
        """Check if bottom edge has reached screen bottom."""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    
    def handle_caught(self):
        """Get caught."""
        Pizza.count += 1
        if Pizza.count == 20:
            Pizza.count = 0
            self.next_level()
            Pizza.speed = 1
        Pizza.speed += .01*Pizza.level
        self.destroy()

    def next_level(self):
        level_message = games.Message(value="Level "+str(Pizza.level),size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps)
        games.screen.add(level_message)
        Pizza.level += 1

    def end_game(self):
        """End the game."""
        end_message = games.Message(value="Game Over",size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    """A chef that moves left and right, dropping pizzas."""
    image=games.load_image("../Res/chef.bmp")
    pizzas = 0
    def __init__(self,y=55,speed=2,odds_change=200):
        """Initialize the Chef object."""
        super(Chef,self).__init__(image=Chef.image,
                                  x=games.screen.width/2,
                                  y=y,dx=speed)
        self.odds_change = odds_change
        self.time_till_drop = 0

    def update(self):
        """Determing if direction needs to be reversed."""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change)==0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        """Decrease countdown or drop pizza and reset countdown."""
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        elif self.pizzas % 20 == 0 and self.pizzas != 0:
            self.time_till_drop = int(90*1.3/Pizza.speed)+1
            self.pizzas += 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.pizzas += 1

            #set buffer to approx 30% of pizza height,
            #regardleess of pizza speed
            self.time_till_drop = int(new_pizza.height*1.3/Pizza.speed)+1
       
def main():
    """Play the game."""
    wall_image = games.load_image("../Res/wall.jpg", transparent = False)
    games.screen.background = wall_image

    the_chef=Chef()
    the_chef2=Chef()
    games.screen.add(the_chef)
    games.screen.add(the_chef2)

    the_pan=Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

#do it!
main()
