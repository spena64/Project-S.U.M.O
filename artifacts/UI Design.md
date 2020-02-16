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
- [UI/User Story Relation Chart](#ui-relation-chart)

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

In the private lobby view for classic mode as a host, the game space is displayed as the most prominent part of the screen. While waiting (either for another player to join or for another player to ready up) the players can practice by freely moving around in the game space. The room code is displayed above the game space, such that it can be shared for other players to join. To the left of the room code, there is a dropdown menu containing the game mode - the host can use this to change the mode to [tournament](#tournament-mode---host) if they see fit. Below the game space is the button to ready up (such that when both players have readied up the game can start) and a the button to force start (if the host chooses to start the game without the other player readying up). Once a game starts, the players are put into [character selction](#character-select). To the upper right of the game space is the player list, showing the current players in the lobby. Player1 has a badge next to their username to indicate they are the host of the lobby, and as a host they have the option to promote (represented by the up arrow) or kick (represented by the block symbol) other players. Below the player list is the chat, where players can input text to communicate with other players in the lobby. 

### Classic Mode - Non-Host

![Private Lobby - Classic Mode as Non-Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Classic.png)

In the private lobby view for classic mode as a non-host, the game space is displayed as the most prominent part of the screen. While waiting (either for another player to join or for another player to ready up) the players can practice by freely moving around in the game space. The room code is displayed above the game space, such that it can be shared for other players to join. To the left of the room code, there is a dropdown menu containing the game mode; however, as a non-host this is just to display the mode, as the non-host cannot interact with the dropdown menu. Below the game space is the button to ready up (such that when both players have readied up the game can start). Once a game starts, the players are put into [character selction](#character-select). To the upper right of the game space is the player list, showing the current players in the lobby. Player1 has a badge next to their username to indicate they are the host of the lobby. Below the player list is the chat, where players can input text to communicate with other players in the lobby. 

### Tournament Mode - Host

![Private Lobby - Tournament Mode as Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Tournament_Host.png)

In the private lobby view for tournament mode as a host, the tournament bracket is displayed as the most prominent part of the screen. After each match, the tournment bracket will be updated to reflect the winners/new matches. The room code is displayed above the tournament bracket, such that it can be shared for other players to join. To the left of the room code, there is a dropdown menu containing the game mode - the host can use this to change the mode to [classic](#classic-mode---host) if they see fit. Below the tournament bracket are several options. Specific to tournament mode, there is the option to allow the game to auto-generate matches (in which an algorithm places players from the player list randomly in bracket slots). There is also an option to shuffle, which runs the algorithm again, resulting in different random matchups. If the auto-generate matches option is unchecked, then the host can move players to each slot as they choose. There is, of course, the button to ready up (such that when all players have readied up the game can start) and a the button to force start (if the host chooses to start the game without the other players readying up). Once a game starts, the players are put into [character selction](#character-select). To the upper right of the tournament bracket is the player list, showing the current players in the lobby. Player1 has a badge next to their username to indicate they are the host of the lobby, and as a host they have the option to promote (represented by the up arrow) or kick (represented by the block symbol) other players. Below the player list is the chat, where players can input text to communicate with other players in the lobby. 

### Tournament Mode - Non-Host

![Private Lobby - Tournament Mode as Non-Host](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_Private_Lobby_Tournament.png)

In the private lobby view for tournament mode as a non-host, the tournament bracket is displayed as the most prominent part of the screen. After each match, the tournment bracket will be updated to reflect the winners/new matches. The room code is displayed above the tournament bracket, such that it can be shared for other players to join. To the left of the room code, there is a dropdown menu containing the game mode; however, as a non-host this is just to display the mode, as the non-host cannot interact with the dropdown menu. Below the game space is the button to ready up (such that when all players have readied up the game can start). Once a game starts, the players are put into [character selction](#character-select). To the upper right of the tournament bracket is the player list, showing the current players in the lobby. Player1 has a badge next to their username to indicate they are the host of the lobby. Below the player list is the chat, where players can input text to communicate with other players in the lobby. 

## In Queue

![In Queue](https://github.com/spena64/Project-S.U.M.O/blob/master/images/3_In_Queue.png)

When a player joins a public match, they are immediately placed in a queue while waiting to find a match. This simply serves as a loading screen - when a match has been found, the players are put into [character selction](#character-select). They also have the option to leave the queue and return to the [main menu](#as-user). 

## Character Select

![Character Select](https://github.com/spena64/Project-S.U.M.O/blob/master/images/4_Character_Select.png)

Before a match begins, the players are able to choose their characters. Both players in a match are shown the same character select screen, and they can view what the other player is choosing. The character select screen allows players to scroll through availble characters, view their stats and aesthetics, and finally ready up when they have chosen their character. Once both players have chosen their characters and readied up, [the match can begin](#game-space). 

## Game Space

![Game Space](https://github.com/spena64/Project-S.U.M.O/blob/master/images/5_Game_Space.png)

The game space is the actual arena space in which the game will be played. Displayed promintently is the ciruclar arena, which each player beginning at either side. The players will use key inputs to move around the arena (using arrow keys or WASD), and the first player to knock the other out of the arena will be the [winner](#winner), while the other will [lose](#lose). Displayed next to the game space is the chat log and each player's usernames. 

### Winner

![You Win!](https://github.com/spena64/Project-S.U.M.O/blob/master/images/6_Winner.png)

This screen displays a message to the winner of the match. It also gives the option to rematch (which, if reciprocated, will place both players back into [character selection](#character-select)), start a new game (which will place the player back into the [matchmaking queue](#in-queue)]), or return to the [main menu](#as-user). This screen is specific to public matches. For private lobbies and public tournaments, it would display the winner message and then present the option to return to the lobby ([tournament](#tournament-mode---host) or [classic](#classic-mode---host)) or to quit and return to the [main menu](#as-user)

### Loser

![You Lose!](https://github.com/spena64/Project-S.U.M.O/blob/master/images/6_Loser.png)

This screen displays a message to the loser of the match. It also gives the option to rematch (which, if reciprocated, will place both players back into [character selection](#character-select)), start a new game (which will place the player back into the [matchmaking queue](#in-queue)]), or return to the [main menu](#as-user). This screen is specific to public matches in classic mode. For private lobbies and public tournaments, it would display the loser message and then present the option to return to the lobby ([tournament](#tournament-mode---host) or [classic](#classic-mode---host)) or to quit and return to the [main menu](#as-user).


## UI Relation Chart

| User Story ID | User Story | UI Screen | Relation |
|---------------|------------|-----------|----------|
| US-0 | As a player, I want to access the web page so that I can access the game. | [Landing Page](#landing-page) | The landing page is the first page seen on the website, thus allowing the player to access the game. |
| US-1 | As a player, I want to make a username, so that I can be identified. | [Create an Account](#create-an-account) / [Login](#login) | Creating an account allows the user to make a username to be identified, and logging in allows past users to be identified. |
| US-2 | As a social person, I want to chat with other players so that I can socialize with them. | [Private Lobbies](#private-lobby) / [Game Space](#game-space) | Chatting with other players is supported in private lobbies as well as in any public match. |
| US-3 | As a solo player I want to play with CPU's, so that I can practice the game | TODO | TODO |
| US-4 | As a solo player, I want to queue for a random match, so that I can play against another player. | [Quick Play](#quick-play) / [In Queue](#in-queue) | Players can join a matchmaking queue through the quick play option in the main menu. |
| US-5 | As an unskilled player, I want to access a tutorial, so that I can learn how to play the game. | [How to Play](#how-to-play) | By selecting "How to Play" from the main menu, the user can view controls and objectives to teach them how to interact with the game. |
| EP-1 | Core Gameplay Mechanics | [Game Space](#game-space) | All core gameplay mechanics are interacted with through the game space. |
| EP-2-1 | As a social person, I want to create a private lobby so that I can play with my friends. | [Home Page](#home-page) / [Private Game](#private-game) | Players can create a private lobby using the "Private Game" option in the main menu and the "Create Lobby" option in the private game menu. |
| EP-2-2 - EP-2-5 | Room Host Privileges | [Classic Mode - Host](#classic-mode---host) / [Tournament Mode - Host](#tournament-mode---host) | All room host privileges are accessible as a room host in any private lobby. |
| EP-3 | Tournament Brackets | [Tournament Mode - Host](#tournament-mode---host) / [Tournament Mode - Non-Host](#tournament-mode---non-host) | Tournament lobbies create tournament brackets and display tournament information to players. |
| EP-4 | Character Selection | [Character Select](#character-select) | The character select page allows players to scroll through different characters, view stat differences, and choose a character that fits their desired playstyle. |
| EP-5 | Audio | [Home Page](#home-page) / TODO | The header bar (first shown on the home page and accessible from every subsequent screen) displays the "Game Settings" option, which will allow the user to change audio settings. |

