# Program Organization

![Context Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_SystemContext.PNG)

At the highest level, the system is simple, involving only the player (a human actor) and the game itself (our project). The game does not interact with any external third party systems.

![Container Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_Container.PNG)

The game system can be broken up into several containers. The Web Application handles sending static content such as HTML to the player's web browser. This allows the player to access the site via HTTPS (User stories: US-0). The Browser Application refers to the front end scripts that are executed in the player's web browser and allow them to interact with the game and perform actions such as creating an account, logging in, searching for games, messaging other players, and moving their character (User stories: US-2, US-4, US-8, US-9, EP-1-1). The Game Application computes game events, responds to clients about the state of the game, and updates the Database with player scores (User stories: EP-1-2, EP-1-3, EP-2-1, EP-3-1). The Database stores information about each player's account credentials along with their game scores.

![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentGameApp.PNG)

The Game Application is made of several components. The Matchmaking System allows players to queue for matches (User stories: US-4, EP-1-3). The Lobby System creates a separate game instance for each group of players and provides chat functions (User stories: US-2, US-7, EP-2-1, EP-2-2, EP-2-3, EP-2-4, EP-2-5, EP-3-1, EP-3-2, EP-3-3, EP-3-4). The Gameplay Component manages game logic such as movement, collisions, and win / lose states (User stories: EP-1-1, EP-1-2, EP-1-3). The Scoreboard System records each player's score in the Database at the conclusion of each match.

![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentWebApp.png)

The Web Application has several components. The Sign-In Controller manages sign-in requests and accesses user account credentials from the Database (User stories: US-8, US-9). The Player Score Controller accesses information about personal and global game scores from the Database to create a leaderboard page for the user to view (User stories: US-9).

![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentBrowserApp.png)

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
As we will be using the free-tier Firebase Spark Plan, there are certain hard limits on storage/user management to which we will need to adhere. The most pressing of these pertain to database storage, which is capped at one database with 1 GB stored and 100 simultaneous connections. This will not pose an issue, as we do not expect to have that many concurrent users and we do not require storage-heavy data to be kept in the database, so we should be able to stay well within these contraints. 

# Security
Most security issues will be handled using built-in firebase scripts. Passwords will not be stored in the database unless hashed, and due to the no-SQL nature of the firebase database, input sanitization will not be necessary, and we will not be at risk for code injection. 

# Performance
As this is a multiplayer game, performance is a top priority. The game must be able to perform at real-time speeds to allow for fair competition between users. Using websockets will help allow for concurrent connected users to see realtime changes in the game space. Additionally, game-related functions will be minimally intensive so as to avoid lag. 

# Scalability
While we do not intend to scale this game to a larger audience, we intend to implement slightly smaller "scalable" functionality within the game within private lobbies. In private lobbies set to tournmanet mode, the tournamnet bracket will be able to scale and populate based on the number of participants who have joined the lobby. 

# Interoperability
We will be using a Firebase realtime database and storing data by client/server database system.

# Internationalization/Localization
At this time, we do not have the capacitiy to implement localization into our game. As such, all text will be available solely in English. This should not be an issue as we are not anticipating our game to reach an international audience.

# Input/Output
The only input necessary to interact with the website and game will be through keyboard and mouse. The user can use WASD or arrow keys to interact with the game and move their character up, left, down, or right, respectively. Mouse interactions will be handled on click, and keyboard inputs will be read and handled at the speed at which they are entered.

# Error Processing
In order to have our website and game run as smoothly as possible, we take preventitive measures to avoid errors, and handle them appropriately as they are encountered. When users input data, the data is checked for improper formatting before it is input for authentication or entered into the database. In doing so, we are able to prevent incorrect or improper data from entering the database. When we encounter improper data, we alert the user that their data has been incorrectly entered and allow them to retype their data. As well as this, when authentication fails, we immediately alert the user of what error has been encountered and why their authentication has failed, so that they may try again. 

# Fault Tolerance
We want the website to be as usable as possible at all times. If a fault is detected - such as if the user is unable to connect to Websockets - we still want the user to be able to navigate the site, while keeping them informed that functionality may be impaired while they are unable to connect. In doing so, we will have a state of default functionality which has been extensively tested and is widely operational, regardless of possible connection errors. 

# Architectural Feasibility
The biggest risk in our architecture is the feasibility of using Python as the programming language for our game's backend/logic. Making a game in Python is certainly feasible - proven through the very existence of PyGame - however, PyGame does not have built-in functionality to handle collisions (unlike game engines such as Unity or Unreal, which make handling collisions simple). Given that our game relies heavily on collision mechanics, it is extremely pertinent that we are able to detect and handle collisions as they happen. This being said, handling collisions in PyGame is certainly possible, albeit with a bit of work. Through research, we have found many tutorials and code samples to aid us in handling collisions. 

# Overengineering
We have sufficiently mapped out use cases and requirements in order to lessen overengineering. Our entire team is well aware of the requirements we aim to fulfill as well as the intended use of our game, and as such we have made design decisions accordingly, keeping them minimal yet properly functional. 

# Build-vs-Buy Decisions
We are using entirley free or open source resources for our game, including the free tier of Firebase (which allows us the use of the Firebase JavaScript SDK and Firebase tools) as well as PyGame. We are also using Firebase's free hosting services in order to host our website, and we have obtained a domain name for free as well. 

# Reuse
We will not be reusing any pre-existing software for our game. 

# Change Strategy
In order to anticipate change, we will be avoiding using hard-coded values in our code, and instead use more easily flexible constant values, which can be changed in one keystroke. As well as this, we have created a single script which connects the website to the database, so that if the connection script ever needs to be changed it will only need to change in one place. 