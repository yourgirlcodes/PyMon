import React from "react";
import ReactDOM from "react-dom";
import {getGameId} from "./utils"
import Simon from "./components/simon"
import Players from "./components/players"

class SimonGame extends React.Component {
    constructor(){
        super();
        this.state = {game:{status:"loading", sequence:""}, user:{name:"", status:""}, players:[]}
    }

    componentDidMount() {
        this.gameLoop();
    }

    gameLoop(){
        var self = this;
        var gameId = getGameId();
        fetch(`/games/${gameId}/status`).then(function(response) { 
            return response.json();
        }).then(function(newStatus) {
            //Game started
            self.setState((prevState, props) => (newStatus), () => {
                setTimeout(() => {self.gameLoop()}, 5000);
             });
        }).catch(function (error) {  
            console.log('Request failure: ', error);  
        });
    }

    isViewMode(){
        return this.state.user.status == "viewer" && this.state.game.status === "on";
    }


    render() {
        return <div className="main">
                <h1 >{this.state.game.status}</h1>
                <Simon  sequence={this.state.game.sequence} disabled={this.state.user.status != "turn"} showPlayBtn={this.state.user.status == "new"}/>
                <Players players={this.state.players} userName={this.state.user.name} viewMode={this.isViewMode()} showJoinBtn={ this.state.user.status == "viewer" && this.state.game.status === "open"} />
            </div>
    }
}

ReactDOM.render(<SimonGame />, document.getElementById("game"));