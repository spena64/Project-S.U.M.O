# Program Organization

![Context Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_SystemContext.PNG)
At the highest level, the system is simple, involving only the player (a human actor) and the game itself (our project). The game does not interact with any external third party systems.
![Container Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_Container.PNG)
The game system can be broken up into several containers. The Web Application handles sending static content such as HTML to the player's web browser. This allows the player to access the site via HTTPS (User stories: US-0). The Browser Application refers to the front end scripts that are executed in the player's web browser and allow them to interact with the game and perform actions such as creating an account, logging in, searching for games, messaging other players, and moving their character (User stories: US-2, US-4, US-8, US-9, EP-1-1). The Game Application computes game events, responds to clients about the state of the game, and updates the Database with player scores (User stories: EP-1-2, EP-1-3, EP-2-1, EP-3-1). The Database stores information about each player's account credentials along with their game scores.
![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentGameApp.PNG)
The Game Application is made of several components. The Matchmaking System allows players to queue for matches (User stories: US-4, EP-1-3). The Lobby System creates a separate game instance for each group of players and provides chat functions (User stories: US-2, US-7, EP-2-1, EP-2-2, EP-2-3, EP-2-4, EP-2-5, EP-3-1, EP-3-2, EP-3-3, EP-3-4). The Gameplay Component manages game logic such as movement, collisions, and win / lose states (User stories: EP-1-1, EP-1-2, EP-1-3). The Scoreboard System records each player's score in the Database at the conclusion of each match.
![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentWebApp.PNG)
The Web Application has several components. The Sign-In Controller manages sign-in requests and accesses user account credentials from the Database (User stories: US-8, US-9). The Player Score Controller accesses information about personal and global game scores from the Database to create a leaderboard page for the user to view (User stories: US-9).
![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentBrowserApp.PNG)
The Browser Application has several components. The Login Page allows the user to log in to their account or create a new account (User stories: US-8, US-9). The User Profile Page allows the user to view their account information (User stories: US-9). The Home Page provides the user with a central menu for them to navigate the site and queue for or create games (User stories: US-4, US-5, EP-2-1, EP-2-2, EP-3-1). The Game Page is a single-page application that provies an interface between the player and the game session (User stories: US-2, US-6, US-7, EP-1-1, EP-2-3, EP-2-4, EP-2-5, EP-3-3, EP-3-4, EP-4-1, EP-4-2).

# Major Classes

![Player Class Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/classDiagram.png)
This image is a visulaization of our major class diagram. In the diagram we have the Match class which creates cointains the players of the match. The player class has all the information about the players and then the playerSprite which has the information about the sprite.
# Data Design

![Entity Relationship Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Entity%20Relationship%20Diagram.PNG) This image is a vizualization of our Entity Relationship Diagram (ERD). The ERD is structural diagram of how entitities interact with one another within the database. Within the Player entity you have a primary key User_ID. In the scope of the player entity the User_ID is just an attribute. Within the entities such as Player_Stats, Leaderboards, Lobby, Private_Lobby, Tournament_Lobby, and Private_Tournament_Lobby you also see a User_ID denoted with a foreign key (FK) tag. This is becuase all the other User_ID's from the other entities are referencing the main User_ID from the Player entity. The lines also represent the relationship of the attribute that it is attacked to. The User_ID attribute in Player starts with a crow’s feet shape, going to the User_IDs in each lobby denoted by a crow’s feet with a blank circle. This represents that one or many User_ID's can map to zero or many User_ID's in each lobby. This means that you can put one or more players into a lobby, but a lobby doesnt nessassarily need any player in it. The replationship between Player, Player_Stats, and Leaderboards are connected with a single line with a slash. This denotes that there is a one to one relationship between them. Each player will have one set of stats and one entry in the leaderboards. The Host_ID in Private_Lobby, and Private_Tournament_Lobby is directily conneted to the Player entity denoted by a single line with a slash from the Player entity to a single line with a slash, and blank circle for Host_ID. This denotes that you need only one player to be a host in the Private_Lobby, and Private_Tournament_Lobby, however each Private_Lobby, and Private_Tournament_Lobby can have at most only one player being host.


# Business Rules

- Terms and Services
    - [Terms of Service for Firebase Services](https://cloud.google.com/terms/)
    - [Google APIs Terms of Service](https://developers.google.com/terms/)
    - [Firebase Data Processing and Security Terms](https://firebase.google.com/terms/data-processing-terms)

- Guidelines
    - [Firebase Logo Guidelines](https://firebase.google.com/brand-guidelines)

# User Interface Design

[UI Design](https://github.com/spena64/Project-S.U.M.O/blob/master/artifacts/UI%20Design.md) (all UI wireframes created using https://wireframepro.mockflow.com/)

# Resource Management

# Security
Login information will be sanitized to prevent SQL injection.

# Performance

# Scalability

# Interoperability
We will be using a Firebase database and storing data by client/server database system

# Internationalization/Localization
Our product will not aim to reach international audience and plan to stay with the local language of English

# Input/Output

# Error Processing

# Fault Tolerance

# Architectural Feasibility

# Overengineering

# Build-vs-Buy Decisions

- Third Party Libraries
    - Firebase JavaScript SDK
    - Firebase Tools

# Reuse

# Change Strategy
