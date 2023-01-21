#############################################################################
# Author:Mohammad El-Hassan
# Description:Final Project
# Date Created:01/16/2023
# Date Modified:01/16/2023
#############################################################################
from winsound import PlaySound, SND_ASYNC, SND_FILENAME, SND_LOOP
from typing import List
from graphics import *
import random, time, os

# Try importing requests
# If requests isn't installed, install it and then import it
try: import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

# Try importing TTS module
# If the module isn't installed, install it and then import it
try: import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3

# Try importing playsound for sound effects
# If the module isn't installed, install it and then import it. Install the 1.2.2 version because latest version doesn't work
try: from playsound import playsound
except ModuleNotFoundError:
    os.system("pip install playsound==1.2.2")
    from playsound import playsound

# Define a class for music 
class Music:
    enabled: bool # True | False
    song: str # The current song, Ex: "rickroll.wav"
    def __init__(self) -> None:
        """
        Instantiate the music class
        """
        self.enabled = False
        self.song = ""
    def isEnabled(self) -> typing.Literal["ON", "OFF"]:
        """Returns if the music is currently enabled

        Returns:
            "ON" | "OFF": Depending on the current status of the music, you'll get one of the strings
        """
        if (self.enabled == True): return "ON"
        else: return "OFF"
    def getSong(self) -> str: 
        """Get the current song

        Returns: 
            str: The current song
        """ 
        return self.song
    def stop(self):
        """Stops the current song from playing

        Returns:
            Self@Music: Returns the base class for chaining :)
        """
        PlaySound(None, SND_ASYNC)
        return self
    def playSong(self, song):
        """Play the provided song

        Args:
            song (str): String of a .wav file. Ex: "rickroll.wav"

        Returns:
            Self@Music: Returns the base class for chaning :)
        """
        self.song = song
        PlaySound(self.song, SND_ASYNC | SND_FILENAME | SND_LOOP)
        return self

class Settings:
    difficulty: str
    players: int
    music: Music
    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = Music()
    def viewDifficulty(self) -> str: 
        """Gets the current difficulty

        Returns:
            str: The difficulty of the game
        """
        return self.difficulty
    def viewPlayers(self) -> int: 
        """Find how many players are playing

        Returns:
            int: The amount of players
        """
        return self.players
    def updateDifficulty(self, newValue: typing.Literal["easy", "medium", "hard"]):
        """Update the difficulty of the game

        Args:
            newValue (easy, medium, hard): New difficulty of the game

        Returns:
            Self@Settings: Returns the base class for chaining :)
        """
        self.difficulty = newValue
        return self

class Player:
    playerName: str
    playerFiles: List[str]
    def __init__(self, name: str, win: GraphWin, files: typing.List[str]) -> None:
        """Instantiate the player class

        Args:
            name (str): The name of the player
            win (GraphWin): The window where the player is going to be
            files (typing.List[str]): List of images to cycle through
        """
        self.playerName = name
        self.playerFile = files
        self.player = Image(Point(0, -210), files[2])
        self.win = win
        self.players = []
        self.lives = 3
        self.current = self.player
        for img in self.playerFile: self.players.append(Image(Point(0, 0), img))
    def draw(self):
        """Draw the player to the screen

        Returns:
            Self@Player: Returns the base class for chaning :)
        """
        self.player.draw(self.win)
        return self
    def movement(self):
        """Check for the player movement
        """
        if (self.win.keys.get("a")):
            if ((self.player.anchor.x - 10) <= -400): return
            if ("Giga" in self.playerFile[-2]):
                index = 0
                self.x = self.player.anchor.x
                self.y = self.player.anchor.y
                for img in self.players:
                    self.player.undraw()
                    img.anchor.x = self.x - 10
                    img.anchor.y = self.y
                    self.x = img.anchor.x
                    self.y = img.anchor.y
                    img.draw(self.win)
                    self.win.update()
                    self.current = img
                    index += 1
                    if index == 3:
                        self.player.anchor.x = self.x
                        self.player.anchor.y = self.y
                        img.undraw()
                        self.player.draw(self.win)
                        self.current = self.player
                        break
                    img.undraw()
                    continue
            else:
                index = 0
                for i in range(4):
                    self.player.move(-3, 0)
        if self.win.keys.get("d"):
            if (self.player.anchor.x + 10) >= 400: return
            if "Giga" in self.playerFile[0]:
                index = 0
                self.x = self.player.anchor.x
                self.y = self.player.anchor.y
                for img in self.players:
                    self.player.undraw()
                    img.anchor.x = self.x + 10
                    img.anchor.y = self.y
                    self.x = img.anchor.x
                    self.y = img.anchor.y
                    img.draw(self.win)
                    self.current = img
                    self.win.update()
                    index += 1
                    if index == 3:
                        self.player.anchor.x = self.x
                        self.player.anchor.y = self.y
                        img.undraw()
                        self.player.draw(self.win)
                        self.current = self.player
                        break
                    img.undraw()
                    continue
            else:
                index = 0
                for i in range(4):
                    self.player.move(3, 0)
    def hasCollided(self,ballx,bally,ballHeight,ballWidth,playerx,playery,playerHeight,playerWidth):
        """Check if the user has collided with the provided ball

        Args:
            ballx (float): The ball's current X position
            bally (float): The ball's current Y position
            ballHeight (int): The ball's height
            ballWidth (int): The ball's width
            playerx (float): The player's current X position
            playery (float): The player's current Y position. 
            playerHeight (int): The player's height.
            playerWidth (int): The player's width.

        Returns:
            bool: Whether the Player is colliding or not
        """
        ball_top = bally + (ballHeight / 2) # The Y value of the top of the ball 
        ball_bottom = bally - (ballHeight / 2) # The Y value of the bottom of the ball
        ball_right = ballx + (ballWidth / 2) # The X value of the right of the ball
        ball_left = ballx - (ballWidth / 2) # The X value of the left of the ball

        player_top = playery + (playerHeight / 2) # The Y value of the top of the player
        player_bottom = playery - (playerHeight / 2) # The Y value of the bottom of the player
        player_right = playerx + (playerWidth / 2) # The X value of the right of the player
        player_left = playerx - (playerWidth / 2) # The X value of the left of the player.
        if ball_bottom < player_top: # If the ball's Y position is under the Y position of the top of the player
            if (ball_right < player_right and ball_left > player_left):return True # If the ball is in between the right and left of the player
            if (ball_right == player_right and ball_left == player_left):return True # If the ball is perfectly lined up on the player.
            if (ball_right > player_right and ball_left < player_left):return True # If the ball is in between the right and left of the player.
            if (player_right > ball_left and player_left < ball_left):return True # If the right of the player is covering the left side of the ball, but the left of the player isn't.
            if (player_left < ball_right and player_right > ball_right):return True # If the left of the player is covering the right side of the ball, but the right side of the player isn't.
            else: return False # No contact was made
        if ball_bottom == player_top:
            if (ball_right < player_right and ball_left > player_left):return True # If the ball is in between the right and left of the player.
            if (ball_right == player_right and ball_left == player_left):return True # If the ball is perfectly lined up on the player.
            if (ball_right > player_right and ball_left < player_left):return True # If the ball is in between the right and left of the player.
            if (player_right > ball_left and player_left < ball_left):return True # If the right of the player is covering the left side of the ball, but the left of the player isn't
            if (player_left < ball_right and player_right > ball_right):return True # If the left of the player is covering the right side of the ball, but the right side of the player isn't
            else:return False # No contact was made

class Ball:
    img: str
    speed: int
    def __init__(self, img: str) -> None:
        """Instantiate the ball

        Args:
            img (str): The image for the ball
        """
        self.img = img
        self.ball = Image(Point(random.randint(-375, 375), 250), self.img)
        self.speed = 0
    def draw(self, screen: GraphWin):
        """Draw the Ball

        Args:
            screen (GraphWin): Screen to be drawn to

        Returns:
            Self@Ball: Returns the base class for chaining :)
        """
        self.ball.draw(screen)
        return self
    def setSpeed(self, speed: int):
        """Set the speed (y) that the button changes b4y

        Args:
            speed (int): The speed in which the ball falls

        Returns:
            Self@Ball: Returns the base class for chaining :)
        """
        self.speed = speed
        return self
    def moveDown(self, screen: GraphWin):
        """Make the ball move down on the screen, and once it reaches the bottom, respawn at the top
        """
        if (self.ball.anchor.y - (self.speed)) <= -250:
            game.score += 1
            game.score_button.text.setText(f"Score:{game.score}")
            self.ball.undraw()
            self.ball.anchor.x = random.randint(-375, 375)
            self.ball.anchor.y = 250
            self.draw(screen)
        else:
            if self.speed: self.ball.move(0, self.speed)
            else: self.ball.move(0, -10)
    def isDrawn(self, screen: GraphWin):
        """Check if the ball is drawn

        Args:
            screen (GraphWin): The window where the ball exists

        Returns:
            "YES" | "NO": Whether the ball is drawn or hidden
        """
        if self.ball in screen.items: return "yes"
        else: return "no"

class Game:
    screen: str
    _settings: Settings
    players: List[Player]
    balls: List[Ball]
    score: int
    lives_button: Button
    score_button: Button
    def __init__(self, score=0, settings=None):
        """Instantiate the game

        Args:
            score (int, optional): Previous score if it exists. Defaults to 0.
            settings (Settings, optional): Persisting settings if settings have been modified. Defaults to None.
        """
        self._settings = Settings()
        self.players = []
        self.balls = []
        self.lives_button = None
        self.score_button = None
        self.default_screen = None
        if score: self.score = score
        else: self.score = 0
        if settings: self._settings = settings
        else: self._settings = Settings() 
    def increaseScore(self):
        """Increase the score

        Returns:
            Self@Game: Returns the base class for chaining :)
        """ 
        self.score += 1
        return self
    def viewSettings(self):
        """View the current settings

        Returns:
            Settings: The current settings
        """
        return self._settings
    def viewPlayers(self):
        """The current players

        Returns:
            List[Player]: List of players
        """
        return self.players
    def viewBalls(self):
        """The balls for the game

        Returns:
            List[Ball]: List of balls
        """
        return self.balls
    def addPlayer(self, name, win, files):
        """Add a player to the game

        Args:
            name (str): Player Name
            win (GraphWin): The game window
            files (List[str]): List of files

        Returns:
            Self@Game: Returns the base class for chaining :)
        """
        self.players.append(Player(name, win, files))
        return self
    def addBall(self, ball: Ball):
        """Add a ball to the game

        Args:
            ball (Ball): The ball to add

        Returns:
            Self@Game: Returns the base class for chaining :)
        """
        
        self.balls.append(ball)
        return self
    def defaultScreen(self):
        """Starting screen for the game

        Returns:
            Settings | int: Can return the score or settings for persistance
        """
        
        # Create an instance of a graph win, zero it and set the image
        defaultScreen = GraphWin("Dodge The Balls", 800, 500).zero().setImage("Settings page.gif")

        # Define the buttons

        PLAY_BUTTON = Button(Point(-100, -20), Point(100, 20), "PLAY", defaultScreen).setFontSize(20).draw()
        INSTURCTION_BUTTON = Button(Point(-100, -20), Point(0, -40), "INSTRUCTIONS", defaultScreen).setFontSize(10).draw()
        SETTINGS_BUTTON = Button(Point(0, -20), Point(100, -40), "SETTINGS", defaultScreen).setFontSize(10).draw()
        self.default_screen = defaultScreen
        if self.score != 0: Button(Point(-100, -80),Point(100, -40),f"LAST SCORE:{self.score}",self.default_screen,).activate().setFontSize(16).draw()
        while True:
            pt = defaultScreen.getMouse()
            
            # If the instruction button is clicked

            if INSTURCTION_BUTTON.clicked(pt):
                # Cosmetic
                INSTURCTION_BUTTON.clickAnimation()
                playsound("click.wav", block=False)
                
                # Close the starting screen and run the instructions screen

                defaultScreen.close()
                self.instructions()
                break
            if SETTINGS_BUTTON.clicked(pt):
                # Cosmetic
                SETTINGS_BUTTON.clickAnimation()
                playsound("click.wav", block=False)
                
                # Close the starting screen and open the settings screen

                defaultScreen.close()

                # Get the result of the settings for persistance

                res = self.settings()

                # Return the settings for persistance

                return res
            if PLAY_BUTTON.clicked(pt):
                # Cosmetic

                PLAY_BUTTON.clickAnimation()
                playsound("click.wav", block=False)
                
                # Close the starting screen and open the settings screen

                defaultScreen.close()

                # Get the result of the score for persistance

                res = self.gameScreen()

                # Return the score for persistance

                return res
        defaultScreen.close()
    def gameScreen(self):
        # Create an instance of the GraphWin, zero it and set the background

        gameScreen = GraphWin("Game Screen", 800, 500, False).zero().setImage("Blue Sky.gif")\

        # Add a ball and the player

        self.addPlayer("Player 1",gameScreen,["Giga walk2.gif", "Giga walk3.gif", "Giga walk1.gif"])
        self.addBall(Ball(f"ball1.gif"))
        for player in self.players: player.draw()
        for ball in self.balls: ball.draw(gameScreen)

        # Set these buttons for later use

        self.lives_button = Button(Point(-400, 200),Point(-350, 250),f"Lives:{self.players[0].lives}",gameScreen,).setFontSize(10).activate().draw()
        self.score_button = Button(Point(350, 200), Point(400, 250), f"Score:{self.score}", gameScreen).setFontSize(10).activate().draw()
        speed = -10
        recentlyCollided = [] # list of recently collided balls to avoid duplicates
        while True:
            if self.players[0].lives == 0: # end the game if their lives are 0
                playsound("game over.wav", block=False)
                for ball in self.balls: ball.ball.undraw()
                for player in self.players: player.player.undraw()
                break
            self.players[0].movement()
            for ball in self.balls: ball.moveDown(gameScreen) # start with one ball and add the rest once the first one reaches the ground, each at a different speed
            if (len(self.balls) != 3 and self._settings.difficulty == "easy"):
                speed += 1
                self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            if (len(self.balls) != 5 and self._settings.difficulty == "medium"):
                speed += 1
                self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            if (len(self.balls) != 10 and self._settings.difficulty == "hard"):
                speed += 1
                self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            for ball in self.balls: # check if the ball has collided
                if self.players[0].hasCollided(ball.ball.anchor.x,ball.ball.anchor.y,ball.ball.getHeight(),ball.ball.getWidth(),self.players[0].current.anchor.x,self.players[0].current.anchor.y,self.players[0].current.getHeight(),self.players[0].current.getWidth()):
                    if (ball.ball.id) in (recentlyCollided): continue # if the ball has already collided before, skip it
                    else:
                        if ball.isDrawn(gameScreen) == "no":continue # check if the ball is drawn
                        self.players[0].lives -= 1 # take away a life if the ball is drawn 
                        self.lives_button.text.setText(f"Lives {self.players[0].lives}") # update the lives text
                        recentlyCollided.append(ball.ball.id) # append it to the list to avoid duplicates
                        ball.ball.undraw() # undraw the ball
                        playsound("pop.wav", block=False) # sfx
            gameScreen.update()
            time.sleep(0.04)
        gameScreen.close()
        return self.score
    def settings(self):
        # Create a GraphWin instance, center it and set the background image
        settingsScreen = GraphWin("Settings", 800, 500).zero().setImage("Settings page.gif")

        # Create the buttons to be used

        MUSIC_ON = Button(Point(-350, 150), Point(-300, 200), "ON", settingsScreen).setFontSize(15).draw()
        MUSIC_OFF = Button(Point(-250, 150), Point(-200, 200), "OFF", settingsScreen).setFontSize(15).draw()
        BACK = Button(Point(-50, -150), Point(50, -200), "BACK", settingsScreen).draw()
        AFTERPARTY = Button(Point(-350, 50), Point(-250, 100), "AFTER PARTY", settingsScreen).setFontSize(10)
        BIGGESTBIRD = Button(Point(-200, 50), Point(-100, 100), "BIGGEST BIRD", settingsScreen).setFontSize(10)
        RICKROLL = Button(Point(-50, 50), Point(50, 100), "RICK ROLL", settingsScreen).setFontSize(10)
        SEARCH = Button(Point(275, 50), Point(350, 100), "Search\nSong", settingsScreen)
        EASY = Button(Point(-350, -50), Point(-300, 0), "EASY", settingsScreen).draw()
        MEDIUM = Button(Point(-250, -50), Point(-200, 0), "MEDIUM", settingsScreen).setFontSize(9).draw()
        HARD = Button(Point(-150, -50), Point(-100, 0), "HARD", settingsScreen).draw()
        entry = Entry(Point(175, 75), 17)

        # In the event of being accidentally drawn

        AFTERPARTY.undraw()
        BIGGESTBIRD.undraw()
        RICKROLL.undraw()
        SEARCH.undraw()
        entry.undraw()
        if self._settings.music.isEnabled() == "ON":
            AFTERPARTY.draw()
            BIGGESTBIRD.draw()
            RICKROLL.draw()
            SEARCH.draw()
            entry.draw(settingsScreen)
            # For settings persistance and consistency 
            if self._settings.music.song == "biggestbird.wav": BIGGESTBIRD.activate()
            if self._settings.music.song == "afterparty.wav": AFTERPARTY.activate()
            if self._settings.music.song == "rickroll.wav": RICKROLL.activate()
        while True:
            if self._settings.music.isEnabled() == "ON":
                # Cosmetic
                MUSIC_OFF.deactivate()
                MUSIC_ON.activate()
            else:
                # Cosmetic
                MUSIC_ON.deactivate()
                MUSIC_OFF.activate()
            if self._settings.difficulty == "easy":
                # Cosmetic
                EASY.activate()
                MEDIUM.deactivate()
                HARD.deactivate()
            if self._settings.difficulty == "medium":
                # Cosmetic
                MEDIUM.activate()
                EASY.deactivate()
                HARD.deactivate()
            if self._settings.difficulty == "hard":
                # Cosmetic
                HARD.activate()
                EASY.deactivate()
                HARD.deactivate()
            pt = settingsScreen.getMouse()
            if MUSIC_ON.clicked(pt):
                # Cosmetic 

                MUSIC_ON.clickAnimation()
                playsound("click.wav", block=False)

                # Update the settings

                self._settings.music.enabled = True

                # In the event of being accidentally drawn

                AFTERPARTY.undraw()
                BIGGESTBIRD.undraw()
                RICKROLL.undraw()
                SEARCH.undraw()
                entry.undraw()

                # Re-draw the song-related buttons

                AFTERPARTY.draw()
                BIGGESTBIRD.draw()
                RICKROLL.draw()
                SEARCH.draw()
                entry.draw(settingsScreen)
                continue
            if MUSIC_OFF.clicked(pt):
                # Cosmetic

                MUSIC_OFF.clickAnimation()
                playsound("click.wav", block=False)

                # Enable music

                self._settings.music.enabled = False

                # Un draw song-related buttons 

                AFTERPARTY.undraw()
                BIGGESTBIRD.undraw()
                RICKROLL.undraw()
                SEARCH.undraw()
                entry.undraw()

                # Stop the music

                self._settings.music.stop()
                continue
            if AFTERPARTY.clicked(pt):
                # Cosmetic

                AFTERPARTY.clickAnimation()
                playsound("click.wav", block=False)
                AFTERPARTY.activate()
                BIGGESTBIRD.deactivate()
                RICKROLL.deactivate()

                # Play the song using winsound

                self._settings.music.playSong("afterparty.wav")
            if BIGGESTBIRD.clicked(pt):
                # Cosmetic

                BIGGESTBIRD.clickAnimation()
                playsound("click.wav", block=False)
                BIGGESTBIRD.activate()
                AFTERPARTY.deactivate()
                RICKROLL.deactivate()

                # Play the song using winsound

                self._settings.music.playSong("biggestbird.wav")
            if RICKROLL.clicked(pt):
                # Cosmetic

                RICKROLL.clickAnimation()
                playsound("click.wav", block=False)
                RICKROLL.activate()
                AFTERPARTY.deactivate()
                BIGGESTBIRD.deactivate()

                # Play the song using winsound

                self._settings.music.playSong("rickroll.wav")
            if SEARCH.clicked(pt):
                # Cosmetic

                SEARCH.clickAnimation()
                playsound("click.wav", block=False)
                SEARCH.activate()
                
                # Deactivate the other buttons
                
                AFTERPARTY.deactivate()
                BIGGESTBIRD.deactivate()
                RICKROLL.deactivate()

                # Create an Text-To-Speech instance and get the text from the entry

                query = entry.getText()
                engine = pyttsx3.init()

                # Make a REST API request to get the lyrics of the entered song

                response = requests.get(f"https://some-random-api.ml/lyrics?title={query}")
                data = response.json()

                # Split the lyrics by new lines

                lyrics = data["lyrics"].split("\n")

                # If there are no results, return 

                if len(data) == 1: print("No result(s) found! Please try a different song!")

                # If there are results, save the results and play the song using winsound

                result_name = data["title"]
                engine.save_to_file(lyrics, f"{result_name}.wav")
                engine.runAndWait()
                self._settings.music.playSong(f"{result_name}.wav")

            # If the back button is clicked, return the user to the main screen and return the current settings so that they can be persisted

            if BACK.clicked(pt):
                BACK.clickAnimation()
                playsound("click.wav", block=False)
                settingsScreen.close()
                return self._settings

            # If the easy button is clicked, set the difficulty for the game to easy

            if EASY.clicked(pt):
                EASY.clickAnimation()
                playsound("click.wav", block=False)
                self._settings.updateDifficulty("easy")
                EASY.activate()
                MEDIUM.deactivate()
                HARD.deactivate()

            # If the medium button is clicked, set the difficulty for the game to medium

            if MEDIUM.clicked(pt):
                MEDIUM.clickAnimation()
                playsound("click.wav", block=False)
                self._settings.updateDifficulty("medium")
                MEDIUM.activate()
                EASY.deactivate()
                HARD.deactivate()

            # If the hard button is clicked, set the difficulty for the game to hard

            if HARD.clicked(pt):
                HARD.clickAnimation()
                playsound("click.wav", block=False)
                self._settings.updateDifficulty("hard")
                HARD.activate()
                EASY.deactivate()
                MEDIUM.deactivate()
            continue

    # Code for the instructions screen

    def instructions(self):

        # Create a GraphWin instance

        instructionsScreen = GraphWin("Instructions", 800, 500).zero().setImage("Settings page.gif")

        # Define a buton for the user to return to the main screen 

        BACK = Button(Point(-50, -150), Point(50, -200), "BACK", instructionsScreen).draw()

        # Draw the isntructions to the screen

        Text(Point(0, 100),"The goal of this game is to dodge the balls that fall down. In each game mode, you have 3 lives.",).draw(instructionsScreen)
        Text(Point(0, 50),"In easy mode,there are 3 balls. In medium difficulty there are 5. And lastly, in hard mode there are 10 balls.",).draw(instructionsScreen)
        Text(Point(0, 0),"Use the 'A'and'D' keys to move side to side to dodge the balls that are falling down ",).draw(instructionsScreen)

        while True:
            pt = instructionsScreen.getMouse()

            # If the back button is clicked, return to the main screen

            if (BACK.clicked(pt)):
                BACK.clickAnimation()
                playsound("click.wav", block=False)
                instructionsScreen.close()
                break
            continue
# Since this is a while loop, a new class is made each time therefore losing all the settings and score that were previously there
# Using this method, we can pass in the score and settings if they exist

score = 0
settings = None
while True:
    game = Game(score=score, settings=settings)
    res = game.defaultScreen()
    if type(res) == int: score = res
    else: settings = res
