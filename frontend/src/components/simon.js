import React from "react";
import {BUTTONS} from "../config"
import SimonBtn from "./button"
import {getGameId} from "../utils"


export default class Simon extends React.Component {
    constructor(props){
        super(props);
        this.state = {activeBtn:"none", sequenceStep:0};
        this.sounds = {};
        BUTTONS.map(b => {
            this.sounds[b] = new Audio(`/sounds/${b}.mp3`);
        });
    }

    activateBtn(color, userInitiated){
        this.setState(() => ({
            activeBtn:color
        }), () => { 
            this.sounds[color].play();
            setTimeout(() => { this.setState({activeBtn:"none"})}, 500);
        });
        if (userInitiated){
            fetch(`/games/${getGameId()}/turn`, {
                method: 'POST',
                body: JSON.stringify({"color":color})
            }).then(function (data) {  
            console.log('Request success: ', data);  
            })  
            .catch(function (error) {  
            console.log('Request failure: ', error);  
            });
        }
    }

    playSequence(){
        setTimeout(() => {
            this.activateBtn(this.props.sequence[this.state.sequenceStep], false)
            this.setState((prevState, props) => ({
                sequenceStep: prevState.sequenceStep + 1
            }), () => { 
                if (this.state.sequenceStep < this.props.sequence.length){
                    this.playSequence();
                }else{
                    fetch(`/games/${getGameId()}/players`, {
                        method: 'PUT',
                    }).then(function (data) {  
                        console.log('Request success: ', data);  
                    })  
                    .catch(function (error) {  
                        console.log('Request failure: ', error);  
                    });
                }
            }); 
           
        }, ((this.state.sequenceStep == 0) ? 0 : 1500));
    }

    playSound(sound) {
        this.sounds[sound].currentTime=0;
        this.sounds[sound].play();
      };

    render() {
        return <div className="simon" >
            {BUTTONS.map(b => (
                <SimonBtn  key={b} color={b} active={this.state.activeBtn == b} disabled={this.props.disabled} clickAction={this.activateBtn.bind(this)} />
            ))}
            { this.state.sequenceStep == 0 && this.props.showPlayBtn &&
            <button className="play-btn" onClick={this.playSequence.bind(this)}>Play</button>
            }
            </div>
    }

    
}