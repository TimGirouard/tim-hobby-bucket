#Simon Says
#Demonstrates reading complicated sequences on the keyboard

from livewires import games, color
import random
import time
import threading

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Color(games.Sprite):

    PAUSE = 5
    COLOR_DELAY = 50000

    def __init__(self,game):
        self.prompt = []
        self.game = game
        self.waity = 0

    image = games.Message(value = "y=yellow, r=red, g=green, b=blue",
                            size = 40,
                            color = color.white,
                            x = games.screen.width/2,
                            y = games.screen.width/10,
                            lifetime = 5*games.screen.fps,
                            is_collideable = False)
    games.screen.add(image)
    #time.sleep(PAUSE)


        
    def show_prompt(self):
        for colory in self.prompt:
            color_message = games.Message(value = colory,
                                          size = 40,
                                          color = color.white,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 1*games.screen.fps,
                                          is_collideable = False)
            if colory == "yellow":
                color_message.color = color.yellow
            if colory == "blue":
                color_message.color = color.blue
            if colory == "red":
                color_message.color = color.red
            if colory == "green":
                color_message.color = color.green
            games.screen.add(color_message)
            time.sleep(1.25)
            #time.sleep(self.PAUSE)

    def build_prompt(self):
        self.prompt.append(random.choice(["blue","red","green","yellow"]))

    def build_response(self):

        self.response = []

        go_message = games.Message(value = "Now your turn!",
                                        size = 40,
                                        color = color.white,
                                        x = games.screen.width/2,
                                        y = games.screen.width/10,
                                        lifetime = 0.75*games.screen.fps,
                                        is_collideable = False)
        games.screen.add(go_message)



        for i in range(len(self.prompt)):

            tempy = True

            while (not games.keyboard.is_pressed(games.K_q)) and tempy:
                if games.keyboard.is_pressed(games.K_b) and self.waity == 0:
                    self.waity = Color.COLOR_DELAY
                    self.response.append("blue")
                    color_message = games.Message(value = "blue",
                                          size = 40,
                                          color = color.blue,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 0.75*games.screen.fps,
                                          is_collideable = False)
                    games.screen.add(color_message)
                    if self.prompt[i] != "blue":
                        self.game.lose_game()
        
                if games.keyboard.is_pressed(games.K_r) and self.waity == 0:
                    self.waity = Color.COLOR_DELAY
                    self.response.append("red")
                    color_message = games.Message(value = "red",
                                          size = 40,
                                          color = color.red,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 0.75*games.screen.fps,
                                          is_collideable = False)
                    games.screen.add(color_message)
                    if self.prompt[i] != "red":
                        self.game.lose_game()
                    
                if games.keyboard.is_pressed(games.K_g) and self.waity == 0:
                    self.waity = Color.COLOR_DELAY
                    self.response.append("green")
                    color_message = games.Message(value = "green",
                                          size = 40,
                                          color = color.green,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 0.75*games.screen.fps,
                                          is_collideable = False)
                    games.screen.add(color_message)
                    if self.prompt[i] != "green":
                        self.game.lose_game()
                    
                if games.keyboard.is_pressed(games.K_y) and self.waity == 0:
                    self.waity = Color.COLOR_DELAY
                    self.response.append("yellow")
                    color_message = games.Message(value = "yellow",
                                          size = 40,
                                          color = color.yellow,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 0.75*games.screen.fps,
                                          is_collideable = False)
                    games.screen.add(color_message)
                    if self.prompt[i] != "yellow":
                        self.game.lose_game()

                if len(self.response) > i:
                    tempy = False

                if self.waity > 0:
                    self.waity -= 1        

        if self.prompt == self.response:
            self.game.advance()
            
        else:
            print("Simon said: ",self.prompt)
            print("You said: ",self.response)
        
class Game(object):

    def __init__(self):
        self.points = 0
        self.colors = Color(game=self)

    def play(self):

        black_image = games.load_image("black.jpg", transparent=False)
        games.screen.background = black_image
        t1 = threading.Timer(0.1, self.welcome_message)
        #time.sleep(Color.PAUSE)
        t2 = threading.Timer(3,self.advance)
        t1.start()
        t2.start()
        #colors = Color(game=self)
        #t2 = threading.Timer(3, colors.build_prompt)
        #t3 = threading.Timer(3.1, colors.show_prompt)
        #t4 = threading.Timer(6, colors.build_response)
        #t2.start()
        #t3.start()
        #t4.start()
        games.screen.mainloop()
        
    def welcome_message(self):

        first_message = games.Message(value = "Welcome to Simon!",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 3*games.screen.fps,
                                    is_collideable = False)
        games.screen.add(first_message)
        
    def advance(self):
        t3 = threading.Timer(1, self.colors.build_prompt)
        t4 = threading.Timer(1.1, self.colors.show_prompt)
        t5 = threading.Timer(1+len(self.colors.prompt)*1.1+2, self.colors.build_response)
        t3.start()
        t4.start()
        t5.start()

    def lose_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5*games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)

def main():
    simon = Game()
    simon.play()
main()
