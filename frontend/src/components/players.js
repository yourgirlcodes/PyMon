import React from "react";
import {getGameId} from "../utils"
import Loader from "./loader"

export default class Players extends React.Component {
    constructor(props){
        super(props);
        this.state = {joinClicked:false};
    }

    render() {
        let viewMode = (this.props.viewMode) ?<div>View mode</div> :"" ;
        return <div className="players">
            {viewMode}
            <h3>Players</h3><ul className="players">
            {this.props.showJoinBtn &&
            <button className={`join-btn ${(this.state.joinClicked) ? "loading" : ""}`} onClick={this.join.bind(this)}>
            {(this.state.joinClicked) ? <Loader />: "Join!" }
            </button>
            }
            {this.props.players.map(k => (
                <li key={k.player} className="player" >
                <span className="player-name">{k.player} {(k.player === this.props.userName) ? "(you)":""}</span>
                <span className={`player-status ${k.status}`}>{k.status}</span>
                </li>
            ))}
            </ul>
            </div>
    }

    join(){
        if (this.state.joinClicked){
            return;
        }
        this.setState(() => ({
            joinClicked:true
        }), () => { 
            fetch(`/games/${getGameId()}/players`, {
                method: 'POST',
            }).then(function (data) {  
            console.log('Request success: ', data);  
            })  
            .catch(function (error) {  
            console.log('Request failure: ', error);  
            });
        });
    }
}