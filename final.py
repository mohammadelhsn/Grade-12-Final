#############################################################################
# Author: Mohammad El-Hassan
# Description: Final Project
# Date Created: 01/16/2023
# Date Modified: 01/16/2023
#############################################################################
from winsound import PlaySound, SND_ASYNC, SND_FILENAME, SND_LOOP
from typing import List
from graphics import *
import threading, random, time, os

def setInterval(func, sec: int):
    def func_wrapper():
        setInterval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

try: import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests
try: import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3

class Music:
    enabled: bool
    song: str
    def __init__(self) -> None:
        self.enabled = False
        self.song = ""
    def isEnabled(self):
        if self.enabled == True: return "ON"
        else: return "OFF"
    def getSong(self): return self.song
    def stop(self):
        PlaySound(None, SND_ASYNC)
        return self
    def playSong(self, song):
        self.song = song
        print(self.song)
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
    def viewDifficulty(self): return self.difficulty
    def viewPlayers(self): return self.players
    def updateDifficulty(self, newValue):
        self.difficulty = newValue
        return self

class Player:
    playerName: str
    playerFiles: List
    def __init__(self, name: str, win: GraphWin, files: typing.List[str]) -> None:
        self.playerName = name
        self.playerFile = files
        self.player = Image(Point(0, 0), files[0])
        self.win = win
    def draw(self): 
        self.player.draw(self.win)
        return self
    def walkLeft(self):
        if "Giga" in self.playerFiles[0]:
            index = 0
            for i in range(3): self.player.move(-4, 0)
        else:
            index = 0
            for i in range(4): self.player.move(-3, 0)
    def walkRight(self):
        if "Giga" in self.playerFiles[0]:
            index = 0
            for i in range(3): self.player.move(4, 0)
        else:
            index = 0
            for i in range(4): self.player.move(3, 0)

class Ball:
    img: str
    def __init__(self, img: str) -> None:
        self.img = img
        self.ball = Image(Point(random.randint(-200, 200), 200), self.img)
    def draw(self, screen: GraphWin):
        self.ball.draw(screen)
        while self.ball.anchor.y != -200:
            self.ball.move(0, -5)
            time.sleep(0.5)
        self.ball.undraw()
        self.ball.x = random.randint(-350, 350)
        self.ball.y = 350
        return self
    def hasCollided(self, player: Player):
        if (self.ball.anchor.x == player.player.anchor.x and self.ball.anchor.y == player.player.anchor.y): return True
        else: return False

class Game:
    screen: str
    _settings: Settings
    players: List[Player]
    balls: List[Ball]
    score: int
    def __init__(self):
        self._settings = Settings()
        self.score = 0
        self.players = []
        self.balls = []
    def increaseScore(self): self.score += 1
    def viewSettings(self): return self._settings
    def viewPlayers(self): return self.players
    def viewBalls(self): return self.balls
    def addPlayer(self, name, win, files):
        self.players.append(Player(name, win, files))
        return self
    def addBall(self, ball: Ball): self.balls.append(ball)
    def defaultScreen(self):
        defaultScreen = GraphWin("Dodge The Balls", 800, 500).zero().setImage("Settings page.gif")
        PLAY_BUTTON = Button(Point(-100, -20), Point(100, 20), "PLAY", defaultScreen).setFontSize(20).draw()
        INSTURCTION_BUTTON = Button(Point(-100, -20), Point(0, -40), "INSTRUCTIONS", defaultScreen).setFontSize(10).draw()
        SETTINGS_BUTTON = Button(Point(0, -20), Point(100, -40), "SETTINGS", defaultScreen).setFontSize(10).draw()
        while True:
            pt = defaultScreen.getMouse()
            if INSTURCTION_BUTTON.clicked(pt):
                INSTURCTION_BUTTON.clickAnimation()
                defaultScreen.close()
                self.instructions()
                break
            if SETTINGS_BUTTON.clicked(pt):
                SETTINGS_BUTTON.clickAnimation()
                defaultScreen.close()
                self.settings()
                break
            if PLAY_BUTTON.clicked(pt):
                PLAY_BUTTON.clickAnimation()
                defaultScreen.close()
                self.gameScreen()
                break
        defaultScreen.close()
    def gameScreen(self):
        gameScreen = GraphWin("Game Screen", 800, 500).zero().setImage("Blue Sky.gif")
        while True:
            self.addPlayer("Player 1",gameScreen,["Giga walk1.gif", "Giga walk2.gif", "Giga walk3.gif"],)
            if self._settings.difficulty == "easy":
                for i in range(3):
                    ball = Ball("ball.gif")
                    self.balls.append(ball)
            if self._settings.difficulty == "medium":
                for i in range(7):
                    ball = Ball("ball.gif")
                    self.balls.append(ball)
            if self._settings.difficulty == "hard":
                for i in range(10):
                    ball = Ball("ball.gif")
                    self.balls.append(ball)
            for player in self.players: player.draw()
            for ball in self.balls: ball.draw(gameScreen)
            break
        gameScreen.getMouse()
        gameScreen.close()
    def settings(self):
        settingsScreen = GraphWin("Settings", 800, 500).zero().setImage("Settings page.gif")
        MUSIC_ON =Button(Point(-350, 150), Point(-300, 200), "ON", settingsScreen).setFontSize(15).draw()
        MUSIC_OFF = Button(Point(-250, 150), Point(-200, 200), "OFF", settingsScreen).setFontSize(15).draw()
        BACK = Button(Point(-50, -150), Point(50, -200), "BACK", settingsScreen).draw()
        AFTERPARTY = Button(Point(-350, 50), Point(-250, 100), "AFTER PARTY", settingsScreen).setFontSize(10)
        BIGGESTBIRD = Button(Point(-200, 50), Point(-100, 100), "BIGGEST BIRD", settingsScreen).setFontSize(10)
        RICKROLL = Button(Point(-50, 50), Point(50, 100), "RICK ROLL", settingsScreen).setFontSize(10)
        SEARCH = Button(Point(275, 50), Point(350, 100), "Search\nText", settingsScreen)
        EASY = Button(Point(-350, -50), Point(-300, 0), "EASY", settingsScreen).draw()
        MEDIUM = Button(Point(-250, -50), Point(-200, 0), "MEDIUM", settingsScreen).setFontSize(9).draw()
        HARD = Button(Point(-150, -50), Point(-100, 0), "HARD", settingsScreen).draw()
        entry = Entry(Point(175, 75), 17)
        while True:
            if self._settings.music.isEnabled() == "ON":
                MUSIC_OFF.deactivate()
                MUSIC_ON.activate()
            else:
                MUSIC_ON.deactivate()
                MUSIC_OFF.activate()
            if self._settings.difficulty == "easy":
                EASY.activate()
                MEDIUM.deactivate()
                HARD.deactivate()
            if self._settings.difficulty == "medium":
                MEDIUM.activate()
                EASY.deactivate()
                HARD.deactivate()
            if self._settings.difficulty == "hard":
                HARD.activate()
                EASY.deactivate()
                HARD.deactivate()
            pt = settingsScreen.getMouse()
            if MUSIC_ON.clicked(pt):
                MUSIC_ON.clickAnimation()
                self._settings.music.enabled = True
                AFTERPARTY.draw()
                BIGGESTBIRD.draw()
                RICKROLL.draw()
                SEARCH.draw()
                entry.draw(settingsScreen)
                continue
            if MUSIC_OFF.clicked(pt):
                MUSIC_OFF.clickAnimation()
                self._settings.music.enabled = False
                AFTERPARTY.undraw()
                BIGGESTBIRD.undraw()
                RICKROLL.undraw()
                SEARCH.undraw()
                entry.undraw()
                self._settings.music.stop()
                continue
            if AFTERPARTY.clicked(pt):
                AFTERPARTY.clickAnimation()
                self._settings.music.playSong("afterparty.wav")
            if BIGGESTBIRD.clicked(pt):
                BIGGESTBIRD.clickAnimation()
                self._settings.music.playSong("biggestbird.wav")
            if RICKROLL.clicked(pt):
                RICKROLL.clickAnimation()
                self._settings.music.playSong("rickroll.wav")
            if SEARCH.clicked(pt):
                SEARCH.clickAnimation()
                query = entry.getText()
                engine = pyttsx3.init()
                response = requests.get(f"https://some-random-api.ml/lyrics?title={query}")
                data = response.json()
                lyrics = data["lyrics"].split("\n")
                if len(data) == 1: print("No result(s) found! Please try a different song!")
                result_name = data["title"]
                engine.save_to_file(lyrics, f"{result_name}.wav")
                engine.runAndWait()
                self._settings.music.playSong(f"{result_name}.wav")
            if BACK.clicked(pt):
                BACK.clickAnimation()
                settingsScreen.close()
                break
            if EASY.clicked(pt):
                EASY.clickAnimation()
                self._settings.updateDifficulty("easy")
                EASY.activate()
                MEDIUM.deactivate()
                HARD.deactivate()
            if MEDIUM.clicked(pt):
                MEDIUM.clickAnimation()
                self._settings.updateDifficulty("medium")
                MEDIUM.activate()
                EASY.deactivate()
                HARD.deactivate()
            if HARD.clicked(pt):
                HARD.clickAnimation()
                self._settings.updateDifficulty("hard")
                HARD.activate()
                EASY.deactivate()
                MEDIUM.deactivate()
            continue
    def instructions(self):
        instructionsScreen = GraphWin("Instructions", 800, 500).zero().setImage("Settings page.gif")
        instructionsScreen.getMouse()
        instructionsScreen.close()

while True:
    game = Game()
    game.defaultScreen()
