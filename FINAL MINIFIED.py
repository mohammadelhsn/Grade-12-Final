#############################################################################
# Author:Mohammad El-Hassan
# Description:Final Project
# Date Created:01/16/2023
# Date Modified:01/16/2023
#############################################################################
from winsound import PlaySound,SND_ASYNC,SND_FILENAME,SND_LOOP;from typing import List;from graphics import *;import threading,random,time,os
try:import requests
except ModuleNotFoundError:os.system("pip install requests");import requests
try:import pyttsx3
except ModuleNotFoundError:os.system("pip install pyttsx3");import pyttsx3
try:from playsound import playsound
except ModuleNotFoundError:os.system("pip install playsound==1.2.2");from playsound import playsound
class Music:
    enabled:bool;song:str
    def __init__(self)->None:self.enabled=False;self.song=""
    def isEnabled(self)->typing.Literal["ON","OFF"]:
        if(self.enabled==True):return("ON")
        else:return("OFF")
    def getSong(self)->str:return(self.song)
    def stop(self):PlaySound(None,SND_ASYNC);return(self)
    def playSong(self,song):self.song=song;PlaySound(self.song,SND_ASYNC|SND_FILENAME|SND_LOOP);return(self)
class Settings:
    difficulty:str;players:int;music:Music
    def __init__(self)->None:self.difficulty="medium";self.players=1;self.music=Music()
    def viewDifficulty(self)->str:return(self.difficulty)
    def viewPlayers(self)->int:return(self.players)
    def updateDifficulty(self,newValue):self.difficulty=newValue;return self
class Player:
    playerName:str;playerFiles:List[str]
    def __init__(self,name:str,win:GraphWin,files:typing.List[str])->None:
        self.playerName=name;self.playerFile=files;self.player=Image(Point(0,-210),files[2]);self.win=win;self.players=[];self.lives=3;self.current=self.player
        for(img)in(self.playerFile):self.players.append(Image(Point(0,0),img))
    def draw(self):self.player.draw(self.win);return self
    def movement(self):
        if(self.win.keys.get("a")):
            if((self.player.anchor.x-10)<=-400):return 
            if("Giga"in(self.playerFile[-2])):
                index=0;self.x=self.player.anchor.x;self.y=self.player.anchor.y
                for(img)in(self.players):
                    self.player.undraw();img.anchor.x=self.x-10;img.anchor.y=self.y;self.x=img.anchor.x;self.y=img.anchor.y;img.draw(self.win);self.win.update();self.current=img;index+=1
                    if(index==3):self.player.anchor.x=self.x;self.player.anchor.y=self.y;img.undraw();self.player.draw(self.win);self.current=self.player;break
                    img.undraw();continue
            else:
                index=0
                for(i)in(range(4)):self.player.move(-3,0)
        if(self.win.keys.get('d')):
                if((self.player.anchor.x + 10)>=400):return
                if("Giga"in(self.playerFile[0])):
                    index=0;self.x=self.player.anchor.x;self.y=self.player.anchor.y
                    for(img)in(self.players):
                        self.player.undraw();img.anchor.x=self.x+10;img.anchor.y=self.y;self.x=img.anchor.x;self.y=img.anchor.y;img.draw(self.win);self.current=img;self.win.update();index+=1
                        if(index==3):self.player.anchor.x=self.x;self.player.anchor.y=self.y;img.undraw();self.player.draw(self.win);self.current=self.player;break
                        img.undraw();continue
                else:
                    index=0
                    for(i)in(range(4)):self.player.move(3,0)
    def hasCollided(self,ballx,bally,ballHeight,ballWidth,playerx,playery,playerHeight,playerWidth):
        ball_top=bally+(ballHeight/2);ball_bottom=bally-(ballHeight/2);ball_right=ballx+(ballWidth/2);ball_left=ballx-(ballWidth/2);player_top=playery+(playerHeight/2);player_bottom=playery-(playerHeight/2);player_right=playerx+(playerWidth/2);player_left=playerx-(playerWidth/2)
        if(ball_bottom<player_top):
            if((ball_right<player_right)and(ball_left>player_left)):return(True)
            if((ball_right==player_right)and(ball_left==player_left)):return(True)
            if((ball_right>player_right)and(ball_left<player_left)):return(True)
            if((player_right>ball_left)and(player_left<ball_left)):return(True)
            if((player_left<ball_right)and(player_right>ball_right)):return(True)
            else:return(False)
        if(ball_bottom==player_top):
            if((ball_right<player_right)and(ball_left>player_left)):return(True)
            if((ball_right==player_right)and(ball_left==player_left)):return(True)
            if((ball_right>player_right)and(ball_left<player_left)):return(True)
            if((player_right>ball_left)and(player_left<ball_left)):return(True)
            if((player_left<ball_right)and(player_right>ball_right)):return(True)
            else:return(False)
class Ball:
    img:str;speed:int
    def __init__(self,img:str)->None:self.img=img;self.ball=Image(Point(random.randint(-375,375),250),self.img);self.speed=0
    def draw(self,screen:GraphWin):self.ball.draw(screen);return(self)
    def setSpeed(self,speed:int):self.speed=speed;return(self)
    def moveDown(self,screen:GraphWin):
        if((self.ball.anchor.y-(self.speed))<=-250):game.score+=1;game.score_button.text.setText(f"Score:{game.score}");self.ball.undraw();self.ball.anchor.x=random.randint(-375,375);self.ball.anchor.y=250;self.draw(screen)
        else:
            if(self.speed):self.ball.move(0,self.speed)
            else:self.ball.move(0,-10)
    def isDrawn(self,screen:GraphWin):
        if(self.ball in screen.items):return("yes")
        else:return("no")
class Game:
    screen:str;_settings:Settings;players:List[Player];balls:List[Ball];score:int;lives_button:Button;score_button:Button
    def __init__(self,score=0,settings=None):
        self._settings=Settings();self.players=[];self.balls=[];self.lives_button=None;self.score_button=None;self.default_screen=None
        if(score):self.score=score
        else:self.score=0
        if(settings):self._settings=settings
        else:self._settings=Settings()
    def increaseScore(self):self.score+=1
    def viewSettings(self):return self._settings
    def viewPlayers(self):return self.players
    def viewBalls(self):return self.balls
    def addPlayer(self,name,win,files):self.players.append(Player(name,win,files));return self
    def addBall(self,ball:Ball):self.balls.append(ball);return self
    def defaultScreen(self):
        defaultScreen=GraphWin("Dodge The Balls",800,500).zero().setImage("Settings page.gif");PLAY_BUTTON=Button(Point(-100,-20),Point(100,20),"PLAY",defaultScreen).setFontSize(20).draw();INSTURCTION_BUTTON=Button(Point(-100,-20),Point(0,-40),"INSTRUCTIONS",defaultScreen).setFontSize(10).draw();SETTINGS_BUTTON=Button(Point(0,-20),Point(100,-40),"SETTINGS",defaultScreen).setFontSize(10).draw();self.default_screen=defaultScreen
        if(self.score != 0):Button(Point(-100,-80),Point(100,-40),f"LAST SCORE:{self.score}",self.default_screen).activate().setFontSize(16).draw()
        while True:
            pt=defaultScreen.getMouse()
            if(INSTURCTION_BUTTON.clicked(pt)):INSTURCTION_BUTTON.clickAnimation();playsound("click.wav",block=False);defaultScreen.close();self.instructions();break
            if(SETTINGS_BUTTON.clicked(pt)):SETTINGS_BUTTON.clickAnimation();playsound("click.wav",block=False);defaultScreen.close(); res=self.settings();return res;break
            if(PLAY_BUTTON.clicked(pt)):PLAY_BUTTON.clickAnimation();playsound("click.wav",block=False);defaultScreen.close();res=self.gameScreen();return res
        defaultScreen.close()
    def gameScreen(self):
        gameScreen=GraphWin("Game Screen",800,500,False).zero().setImage("Blue Sky.gif");self.addPlayer("Player 1",gameScreen,["Giga walk2.gif","Giga walk3.gif","Giga walk1.gif"],);self.addBall(Ball(f"ball1.gif"))
        for(player)in(self.players):player.draw()
        for(ball)in(self.balls):ball.draw(gameScreen)
        self.lives_button=Button(Point(-400,200),Point(-350,250),f'Lives:{self.players[0].lives}',gameScreen).setFontSize(10).activate().draw();self.score_button=Button(Point(350,200),Point(400,250),f'Score:{self.score}',gameScreen).setFontSize(10).activate().draw();speed=-10;recentlyCollided=[]
        while True:
            if(self.players[0].lives==0):
                playsound("game over.wav",block=False)
                for(ball)in(self.balls):ball.ball.undraw()
                for(player)in(self.players):player.player.undraw()
                break
            self.players[0].movement()
            for(ball)in(self.balls):ball.moveDown(gameScreen)
            if((len(self.balls)!=3)and(self._settings.difficulty=="easy")):speed+=1;self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            if((len(self.balls)!=5)and(self._settings.difficulty=="medium")):speed+=1;self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            if((len(self.balls)!=10)and(self._settings.difficulty=="hard")):speed+=1;self.addBall(Ball(f"ball1.gif").setSpeed(speed))
            for(ball)in(self.balls):
                if(self.players[0].hasCollided(ball.ball.anchor.x,ball.ball.anchor.y,ball.ball.getHeight(),ball.ball.getWidth(),self.players[0].current.anchor.x,self.players[0].current.anchor.y,self.players[0].current.getHeight(),self.players[0].current.getWidth())):
                    if((ball.ball.id)in(recentlyCollided)):continue
                    else:
                        if(ball.isDrawn(gameScreen)=="no"):continue
                        self.players[0].lives-=1;self.lives_button.text.setText(f'Lives {self.players[0].lives}');recentlyCollided.append(ball.ball.id);ball.ball.undraw();playsound("pop.wav",block=False)
            gameScreen.update();time.sleep(.04)
        gameScreen.close();return self.score
    def settings(self):
        settingsScreen=GraphWin("Settings",800,500).zero().setImage("Settings page.gif");MUSIC_ON=Button(Point(-350,150),Point(-300,200),"ON",settingsScreen).setFontSize(15).draw();MUSIC_OFF=Button(Point(-250,150),Point(-200,200),"OFF",settingsScreen).setFontSize(15).draw();BACK=Button(Point(-50,-150),Point(50,-200),"BACK",settingsScreen).draw();AFTERPARTY=Button(Point(-350,50),Point(-250,100),"AFTER PARTY",settingsScreen).setFontSize(10);BIGGESTBIRD=Button(Point(-200,50),Point(-100,100),"BIGGEST BIRD",settingsScreen).setFontSize(10);RICKROLL=Button(Point(-50,50),Point(50,100),"RICK ROLL",settingsScreen).setFontSize(10);SEARCH=Button(Point(275,50),Point(350,100),"Search\nSong",settingsScreen);EASY=Button(Point(-350,-50),Point(-300,0),"EASY",settingsScreen).draw();MEDIUM=Button(Point(-250,-50),Point(-200,0),"MEDIUM",settingsScreen).setFontSize(9).draw();HARD=Button(Point(-150,-50),Point(-100,0),"HARD",settingsScreen).draw();entry=Entry(Point(175,75),17);AFTERPARTY.undraw();BIGGESTBIRD.undraw();RICKROLL.undraw();SEARCH.undraw();entry.undraw()
        if(self._settings.music.isEnabled()=="ON"):
            AFTERPARTY.draw();BIGGESTBIRD.draw();RICKROLL.draw();SEARCH.draw();entry.draw(settingsScreen)
            if(self._settings.music.song=="biggestbird.wav"):BIGGESTBIRD.activate()
            if(self._settings.music.song=="afterparty.wav"):AFTERPARTY.activate()
            if(self._settings.music.song=="rickroll.wav"):RICKROLL.activate()
        while(True):
            if(self._settings.music.isEnabled()=="ON"):MUSIC_OFF.deactivate();MUSIC_ON.activate()
            else:MUSIC_ON.deactivate();MUSIC_OFF.activate()
            if(self._settings.difficulty=="easy"):EASY.activate();MEDIUM.deactivate();HARD.deactivate()
            if(self._settings.difficulty=="medium"):MEDIUM.activate();EASY.deactivate();HARD.deactivate()
            if(self._settings.difficulty=="hard"):HARD.activate();EASY.deactivate();HARD.deactivate()
            pt=settingsScreen.getMouse()
            if(MUSIC_ON.clicked(pt)):MUSIC_ON.clickAnimation();playsound("click.wav",block=False);self._settings.music.enabled=True;AFTERPARTY.undraw();BIGGESTBIRD.undraw();RICKROLL.undraw();SEARCH.undraw();entry.undraw();AFTERPARTY.draw();BIGGESTBIRD.draw();RICKROLL.draw();SEARCH.draw();entry.draw(settingsScreen);continue
            if(MUSIC_OFF.clicked(pt)):MUSIC_OFF.clickAnimation();playsound("click.wav",block=False);self._settings.music.enabled=False;AFTERPARTY.undraw();BIGGESTBIRD.undraw();RICKROLL.undraw();SEARCH.undraw();entry.undraw();self._settings.music.stop();continue
            if(AFTERPARTY.clicked(pt)):AFTERPARTY.clickAnimation();playsound("click.wav",block=False);AFTERPARTY.activate();BIGGESTBIRD.deactivate();RICKROLL.deactivate();self._settings.music.playSong("afterparty.wav")
            if(BIGGESTBIRD.clicked(pt)):BIGGESTBIRD.clickAnimation();playsound("click.wav",block=False);BIGGESTBIRD.activate();AFTERPARTY.deactivate();RICKROLL.deactivate();self._settings.music.playSong("biggestbird.wav")
            if(RICKROLL.clicked(pt)):RICKROLL.clickAnimation();playsound("click.wav",block=False);RICKROLL.activate();AFTERPARTY.deactivate();BIGGESTBIRD.deactivate();self._settings.music.playSong("rickroll.wav")
            if(SEARCH.clicked(pt)):
                SEARCH.clickAnimation();SEARCH.activate();AFTERPARTY.deactivate();BIGGESTBIRD.deactivate();RICKROLL.deactivate();query=entry.getText();engine=pyttsx3.init();response=requests.get(f"https://some-random-api.ml/lyrics?title={query}");data=response.json();lyrics=data["lyrics"].split("\n")
                if(len(data)==1):print("No result(s) found! Please try a different song!")
                result_name=data["title"];engine.save_to_file(lyrics,f"{result_name}.wav");engine.runAndWait();self._settings.music.playSong(f"{result_name}.wav")
            if(BACK.clicked(pt)):BACK.clickAnimation();playsound("click.wav",block=False);settingsScreen.close();return(self._settings);break
            if(EASY.clicked(pt)):EASY.clickAnimation();playsound("click.wav",block=False);self._settings.updateDifficulty("easy");EASY.activate();MEDIUM.deactivate();HARD.deactivate()
            if(MEDIUM.clicked(pt)):MEDIUM.clickAnimation();playsound('click.wav',block=False);self._settings.updateDifficulty("medium");MEDIUM.activate();EASY.deactivate();HARD.deactivate()
            if(HARD.clicked(pt)):HARD.clickAnimation();playsound('click.wav',block=False);self._settings.updateDifficulty("hard");HARD.activate();EASY.deactivate();MEDIUM.deactivate()
            continue
    def instructions(self):
        instructionsScreen=GraphWin("Instructions",800,500).zero().setImage("Settings page.gif");BACK=Button(Point(-50,-150),Point(50,-200),"BACK",instructionsScreen).draw();Text(Point(0,100),"The goal of this game is to dodge the balls that fall down. In each game mode, you have 3 lives.").draw(instructionsScreen);Text(Point(0,50),"In easy mode,there are 3 balls. In medium difficulty there are 5. And lastly, in hard mode there are 10 balls.").draw(instructionsScreen);Text(Point(0,0),"Use the 'A'and'D' keys to move side to side to dodge the balls that are falling down ").draw(instructionsScreen)
        while True:
            pt=instructionsScreen.getMouse() 
            if(BACK.clicked(pt)):BACK.clickAnimation();playsound("click.wav",block=False);instructionsScreen.close();break
            continue
score=0;settings=None
while(True):
    game=Game(score=score,settings=settings);res=game.defaultScreen()
    if(type(res)==int):score=res
    else:settings=res