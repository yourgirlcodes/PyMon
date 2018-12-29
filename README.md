# Welcome to PYmon

PYmon is an online multiplayer version of the famous Hasbro game simon


## Getting Started

First visit [The Demo](https://py-mon.herokuapp.com/) (hopefully it will be awake)
Clone the project and make sure you have all of the tools below installed.


### Prerequisites

* [Python 2.7.x](https://www.python.org/downloads/release/python-2715/)
* [Pip](https://pypi.org/project/pip/)
* [npm](https://www.npmjs.com/)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* [Remote MySql Server](https://www.db4free.net)


### Installing

1. Create a new "pymon" folder under your dev folder.
2. cd into the folder.
3. clone this repository
    ```
    git init
    git clone <this repository url>
    ```
4. run pip and install the required libraries
    ```
    pip install -r requirements.txt
    ```
4. cd into "/frontend" folder, run npm and install the required libraries
    ```
    cd frontend
    npm install
    ```
5. run webpack to build the react files into the dist folder. webpack is configured to watch fie changes, so this cmd window should remain open.
    ```
    npm run build
    ```
6. create a remote or local MYSQL DB on (you can use [db4free](https://www.db4free.net) or your own machine for now follow the instruction on this [section](#installing-the-db)


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### Installing the DB

Explain what these tests test and why

```

CREATE TABLE `game` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `status` varchar(30) DEFAULT 'open',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sequence` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `creator` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'anonymous',
  `step` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `player` (
  `id` varchar(30) NOT NULL,
  `avatar` varchar(30) NOT NULL DEFAULT 'anonymous',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `playergame` (
  `game` int(11) NOT NULL,
  `player` varchar(30) NOT NULL,
  `status` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'new',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes 
--

ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playergame`
--
ALTER TABLE `playergame`
  ADD KEY `game` (`game`),
  ADD KEY `player` (`player`);


--
-- AUTO_INCREMENT for table `game`
--
ALTER TABLE `game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;


--
-- Constraints for table `playergame`
--
ALTER TABLE `playergame`
  ADD CONSTRAINT `game` FOREIGN KEY (`game`) REFERENCES `game` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `player` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;


```

## Deployment

The project is "Heroku Deploy Ready"
All you have to do is to create a new Heroku app
Git push heroku master

## Built With

* [Bottle](https://bottlepy.org/docs/dev/) - The web framework used
* [React](https://reactjs.org/) - FrontEnd Framework
* [Webpack](https://webpack.js.org/) - Frontend module bundler

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Gilad Navot** - *Initial work* - [navotgil](https://github.com/navotgil)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## TODO

* Implement the filters on /games page 
    **description:** (should allow users to filter games according to status)
    **desing:** A selected filter should be css "brown" color ("OPEN" should be selected on load)
    **constraints:** frontend implementation (HTML/CSS/JS)
* Implement a back button in /game page.
    **description:** allow users to exit a game to the /games page
    **design:** total freedom
    **constraints:** react component implementation "BackBtn"
* Implement a more impressive "Game Over"/"Game Won" prompt
    **description:** currently there are none, try to make something nice...
    **design:** total freedom
    **constraints:** total freedom (follow application structure)
* Implement highscores page
    **description:** A standalone page showing the top 10 users with the heighest score (most games won) descending order.
    **design:** total freedom
    **constraints:** total freedom (follow application structure)
* Implement the ability for a player to select one of 5 avatars
    **description:** On the /start page add the ability to select an avatar
    (the DB already contains that field)
    The avatar should be shown in the "players" component next to the players name
    **design:** total freedom
    **constraints:** total freedom (follow application structure)
* Update project to Python 3.x
    **description:** currently the project runs Pyhton 2.7.x
    update the projuct and make sure all third party libraries works.
    Also verify deploying to Heroku is not borken.
* Implement delete button for game in the /games page
    **description:** users should be able to delete old games
    **design:** show the delete button only for games the user can delete
    **constraints:** only the game creator should be able to delete a game (follow application structure)
* Fix responsiveness on mobile
    **description:** The simon itself is quite responsive but we need to fix side menu somehow
    **design:** total freedom
    **constraints:** use media queries


