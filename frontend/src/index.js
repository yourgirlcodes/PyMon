import React from "react";
import ReactDOM from "react-dom";
import {getGameId} from "./utils"
import Simon from "./components/simon"
import Players from "./components/players"

class SimonGame extends React.Component {
    constructor(){
        super();
        this.state = {game:{status:"loading", sequence:""}, user:null, players:[]}
    }

    componentDidMount() {
        this.gameLoop();
    }

    gameLoop(){
        var self = this;
        var gameId = getGameId();
        fetch(`/game_status/${gameId}`).then(function(response) { 
            return response.json();
        }).then(function(newStatus) {
            //Game started
            // if (self.state.game.status == "open" && newStatus.game.status == "on"){
                newStatus.playSequence = true;
            // }
            self.setState(newStatus)
            // setTimeout(() => {self.gameLoop()}, 5000);
        });
    }


    


    join(){
        fetch(`/games/${getGameId()}/players`, {
            method: 'POST',
        }).then(function (data) {  
          console.log('Request success: ', data);  
        })  
        .catch(function (error) {  
          console.log('Request failure: ', error);  
        });
    }


    render() {
        let playerJoined = false;
        for( let p in this.state.players){
            if (this.state.players[p].player == this.state.user){
                playerJoined = true;
                break;
            }
        }
        let viewMode = !playerJoined && this.state.game.status === "on";
        return <div >
                <h1 >{this.state.game.status}</h1>
                <Simon  sequence={this.state.game.sequence} playSequence={this.state.playSequence}/>
                { !playerJoined && this.state.game.status === "open" &&
                    <button onClick={this.join.bind(this)}>Join!</button>
                }
                <Players players={this.state.players} user={this.state.user} viewMode={viewMode} />
            </div>
    }
}

ReactDOM.render(<SimonGame />, document.getElementById("game"));