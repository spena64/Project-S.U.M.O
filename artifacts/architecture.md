# Program Organization

![Context Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_SystemContext.PNG)
![Container Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_Container.PNG)
![Component Diagram](https://github.com/spena64/Project-S.U.M.O/blob/master/images/Arch_ComponentGameApp.PNG)

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
