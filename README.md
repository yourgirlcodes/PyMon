# Welcome to PYmon

PYmon is an online multiplayer version of the famous Hasbro game simon
The rules are simple...


## Getting Started

First visit [The Demo](https://py-mon.herokuapp.com/) (hopefully it will be awake)
Clone the project and make sure you have all of the tools below installed.


### Prerequisites

* [Python 2.7.x](https://www.python.org/downloads/release/python-2715/)
* [Pip](https://pypi.org/project/pip/)
* [npm](https://www.npmjs.com/)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
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
    description: (should allow users to filter games according to status)
    desing: A selected filter should be css "brown" color ("OPEN" should be selected on load)
    constraints: frontend implementation (HTML/CSS/JS)
* Implement a back button in /game page.
    description: allow users to exit a game to the /games page
    design: total freedom
    constraints: react component implementation "BackBtn"
* Implement a more impressive "Game Over"/"Game Won" prompt
    description: currently there are none, try to make something nice...
    design: total freedom
    constraints: total freedom (follow application structure)
* Implement highscores page
    description: A standalone page showing the top 10 users with the heighest score (most games won) descending order.
    design: total freedom
    constraints: total freedom (follow application structure)
* Implement the ability for a player to select one of 5 avatars
    description: On the /start page add the ability to select an avatar
    (the DB already contains that field)
    The avatar should be shown in the "players" component next to the players name
    design: total freedom
    constraints: total freedom (follow application structure)
* Update project to Python 3.x
    description: currently the project runs Pyhton 2.7.x
    update the projuct and make sure all third party libraries works.
    Also verify deploying to Heroku is not borken.

