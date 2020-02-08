# UI Design

## Table of Contents

- [Landing Page](#landing-page)
  * [Login](#login)
  * [Create an Account](#create-an-account)
  * [Continue as Guest](#continue-as-guest)
- [Home Page](#home-page)
  * [As User](#as-user)
  * [As Guest](#as-guest)
  * [Quick Play](#quick-play)
  * [Private Game](#private-game)
  * [How to Play](#how-to-play)
  * [About](#about)
  * [Credits](#credits)
- [Private Lobby](#private-lobby)
  * [Classic Mode - Host](#classic-mode---host)
  * [Classic Mode - Non-Host](#classic-mode---non-host)
  * [Tournament Mode - Host](#tournament-mode---host)
  * [Tournament Mode - Non-Host](#tournament-mode---non-host)
- [In Queue](#in-queue)
- [Character Select](#character-select)
- [Game Space](#game-space)
  * [Winner](#winner)
  * [Loser](#loser)

## Landing Page

![Landing Page](https://github.com/spena64/Project-S.U.M.O/blob/master/images/1_Landing_Page.png)

The landing page is the first page any user will see upon visiting the page for any given new session. The purpose of this page is to identify the user before allowing them to play the game. The user has the option to [log in](#login), [create an account](#create-an-account), or [continue as a guest](#continue-as-guest). 

### Login

![Login Page](https://github.com/spena64/Project-S.U.M.O/blob/master/images/1a_Login.png)

This page allows the user to log in to the website using their unique username and password which is stored in the database. Once successfully logged in, the user proceeds to the [main menu](#as-user). If the user does not, in fact, have an account, the links at the bottom of the card allow them to go back and [create an account](#create-an-account) or [continue as a guest](#continue-as-guest).

### Create an Account

![Create an Account](https://github.com/spena64/Project-S.U.M.O/blob/master/images/1b_Create_an_Account.png)

If the user does not already have an account, they can use this page to create one by inputting a unique username, a nickname, and a password. After creating an account, the user proceeds to the [main menu](#as-user). If the user already has an account, a link at the bottom of the page allows them to go back and [log in](#login). The user also has the choice to [continue as a guest](#continue-as-guest).

### Continue as Guest

![Continue as Guest](https://github.com/spena64/Project-S.U.M.O/blob/master/images/1c_Continue_as_Guest.png)

If the user does not have an account, does not want to create an account and/or does not want to log in for any reason, they have the choice of continuing as a guest. By doing so, they are issued a unique temporary guest ID, and their player data will not be saved. After entering a nickname, they will progress to the [main menu](#as-guest). They also have the option of [logging in](#login) or [creating an account](#create-an-account).

## Home Page

### As User:

![Home Page as User](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2_Home_Page_as_User.png)

The home page contains the main menu of the game, allowing the user to [hop into a game](#quick-play), [create or join a private game](#private-game), [view the tutorial](#how-to-play), [view the about page](#about), or [view the credits](#credits). As a user, the header bar includes links to the user's match history and account settings, as well as the more general game settings, available to anyone. 

### As Guest:

![Home Page as Guest](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2_Home_Page_as_Guest.png)

The home page contains the main menu of the game, allowing the user to [hop into a game](#quick-play), [create or join a private game](#private-game), [view the tutorial](#how-to-play), [view the about page](#about), or [view the credits](#credits). As a guest, the header bar includes links to allow the user to [log in](#login) or [create an account](#create-an-account). It also allows them to access the game settings. 

### Quick Play

![Quick Play](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2a_Quick_Play.png)

Quick play allows users to join a [matchmaking queue](#in-queue) to quickly get into a public game. The user has the option of choosing classic mode (a fast 1v1 match) or tournament mode (a bracket-style single elimination tournmanet). The user also has the option to return to the [main menu](#as-user). 

### Private Game

![Private Game](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2b_Private_Game.png)

When choosing to create a private game, the user has the option to either create a private lobby, or to join using a room code. If creating a lobby, the lobby created defaults to a [classic lobby](#classic-mode---host), but once in the lobby the host has the option to change it to a [tournament lobby](#tournament-mode---host). When joining using a room code, the user will be prompted to enter their code, and will then enter the correspoding lobby (which could be either [classic](#classic-mode---non-host) or [tournament](#tournament-mode---non-host) style). The user also has the option to return to the [main menu](#as-user). 


### How to Play

![How to Play](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2c_How_to_Play.png)

This page displays information about the mechanics of the game including controls, players stats, and objectives. The user may then return to the [main menu](#as-user). 

### About

![About](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2d_About.png)

This page displays information about the game in the general sense, including genre, influences, and purpose. The user may then return to the [main menu](#as-user). 

### Credits

![Credits](https://github.com/spena64/Project-S.U.M.O/blob/master/images/2e_Credits.png)

This page displays the names of the developers of the game. The user may then return to the [main menu](#as-user). 

## Private Lobby

### Classic Mode - Host

![Private Lobby - Classic Mode as Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Classic_Host.png)

### Classic Mode - Non-Host

![Private Lobby - Classic Mode as Non-Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Classic.png)

### Tournament Mode - Host

![Private Lobby - Tournament Mode as Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Tournament_Host.png)

### Tournament Mode - Non-Host

![Private Lobby - Tournament Mode as Non-Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Tournament.png)

## In Queue

![In Queue](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_In_Queue.png)

## Character Select

![Character Select](https://github.com/spena64/Project-S.U.M.O/blob/master/images/4_Character_Select.png)

## Game Space

![Game Space](https://github.com/spena64/Project-S.U.M.O/blob/master/images/5_Game_Space.png)

### Winner

![You Win!](https://github.com/spena64/Project-S.U.M.O/blob/master/images/6_Winner.png)

### Loser

![You Lose!](https://github.com/spena64/Project-S.U.M.O/blob/master/images/6_Loser.png)
