import React from "react";
import {getGameId} from "../utils"
import Simon from "./simon"
import Players from "./players"
import Sequence from "./sequence"

export default class SimonGame extends React.Component {
    constructor(){
        super();
        this.state = {game:{status:"loading", sequence:[]}, user:{name:"", status:""}, players:[]}
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
                setTimeout(() => {self.gameLoop()}, 2000);
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
                <div className="center">
                    <Simon  sequence={this.state.game.sequence} disabled={this.state.user.status != "turn"} showPlayBtn={this.state.user.status == "new"}/>
                    <Sequence sequence={this.state.game.sequence} step={this.state.game.step} />
                </div>
                <div className="side">
                    <div className="game-name">{this.state.game.name}</div>
                    <div className={`game-status ${this.state.game.status}`}>{this.state.game.status}</div>
                    <Players players={this.state.players} userName={this.state.user.name} viewMode={this.isViewMode()} showJoinBtn={ this.state.user.status == "viewer" && this.state.game.status === "open"} />
                </div>
            </div>
    }
}