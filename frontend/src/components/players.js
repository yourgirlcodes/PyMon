
import React from "react";

export default class Players extends React.Component {
    render() {
        let viewMode = (this.props.viewMode) ?<div>View mode</div> :"" ;
        return <div>
            {viewMode}
            <h3>Players</h3><ul className="players">
            {this.props.players.map(k => (
                <li key={k.player} className="player" >
                <span>{k.player}</span>
                <span>{(k.player === this.props.userName) ? "(you)":""}</span>
                <span>{k.status}</span>
                </li>
            ))}
            </ul>
            </div>
    }

    ready(){
        fetch(`/games/${getGameId()}/players`, {
            method: 'PUT',
        }).then(function (data) {  
          console.log('Request success: ', data);  
        })  
        .catch(function (error) {  
          console.log('Request failure: ', error);  
        });
    }
}