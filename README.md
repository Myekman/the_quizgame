# The Quizgame

## Introduktion
This is a command-line game created with python for my Project portfolio 3 at Code Institute, Full-stack development program. 

The game is structured in 3 levels. If you pass the first level, you move on to the next, if you don't, you get more attempts. At the end, your results are compiled and saved to a google worksheet. The result is also printed out in the end of the game. So the player is able to se the results aswell.

### README Table Content
* [Indtroduction](#introduktion)
* [User Stories](#user-stories)
* [Design](#design)
* [Flowcharts](#flowcharts)
* [Storage Data](#storage-data)
* [Technologies Used](#technologies-sed)

### Game Features
* [Welcome/Intro](#welcome)
* [Level 1](#level-1)
* [Level 2](#level-2)
* [Level 3](#level-3)

## User Stories 
* As a creator, I want to:
1. Build an easy app with python.
2. Build an app that is structered and easy to follow. 
3. Build an app that is easy but challenging. 

* As a visitor, i want to:
1. Enter the game with my name.
2. Be able to understand how to play the game. 
3. Be able to see my results so i can develop next time i play. 

## Design
* I have not imporded any colorama for colors since there where no time left for me to do that. But is it something to add to develop the app further in the feature. 
* The design thinking i did was that i clear the terminal when move to next levels. I think it looks less messy and the app is easier to follow. 

## Flowcharts

# Game features

## Welcome/Intro 
* Explains how the game works and asks you to fill in your name to play.
![IMG](docs/pp3.2.png)
* When you have filled in your name, this will show.
![IMG](docs/pp3.3.png)
* If you write no, goodbye.
![IMG](docs/pp3.4.png)
* If any other, ValueError.
![IMG](docs/pp3.6.png)
* If you write yes the game begin
![IMG](docs/pp3.5.png)
## Level 1
* When you type yes the game will begin,
* Level one questions:
![IMG](docs/pp3.5.png)
* When answer correct the score will add +1
![IMG](docs/pp3.7.png)
* When answer wrong the wrong answer count will add +1
![IMG](docs/pp3.8.png)
* If you fail you get another try and the questions run again.
![IMG](docs/pp3.9.png)
## Level 2
* In this level you will guess a secret number between 0-15.
![IMG](docs/pp3.10.png)
* You have 3 tries and if you guess wrong you get 3 more tries.
![IMG](docs/pp3.11.png)
## Level 3
* In level 3 you can have minimun 0 score and max 3 score. Just one try here.
![Img](docs/pp3.12.png)

## Result
* When game is finished you can se your result and it will be saved to a google worksheet.
![img](docs/pp3.13.png)

## Storage Data
I have used a Google sheet to save results every time the game is played. This sheet is connected to the code via Google Drive and Google Sheet API by Google Cloud Platform. This method allows me to send and save data. Since this is sensitive data, I had to add creds.json to the Git ignore file. This is so that it will not be pushed to github.
![IMG](docs/pp3.14.png)

## Google sheet
![img](docs/pp3.15.png)
* The goal is to have 0 failed tries in level 1 and 2, and the max score 3 in level 3.

## Technologies Used:
* Python

### Python Packages
* [Gspread](https://pypi.org/project/gspread/): Allows communication with Google Sheets.
* [Google Auth](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts.
* [import os](https://www.geeksforgeeks.org/clear-screen-python/): To clear the terminal

