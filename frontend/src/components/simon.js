import React from "react";
import {BUTTONS} from "../config"
import SimonBtn from "./button"


export default class Simon extends React.Component {
    constructor(props){
        super(props);
        this.state = {activeBtn:"none", sequenceStep:0};
        this.sounds = {};
        BUTTONS.map(b => {
            this.sounds[b] = new Audio(`/sounds/${b}.mp3`);
        });
    }

    activateBtn(color){
        this.setState(() => ({
            activeBtn:color
        }), () => { 
            this.sounds[color].play();
            setTimeout(() => { this.setState({activeBtn:"none"})}, 500);
        });
    }

    playSequence(){
        const currentColorIndex = this.props.sequence[this.state.sequenceStep];
        this.activateBtn(BUTTONS[parseInt(currentColorIndex) - 1])
        // this.setState((prevState, props) => ({
        //     activeBtn: BUTTONS[parseInt(currentColorIndex) - 1]
        // }), () => { 
        //     this.playSound(this.state.activeBtn);
        // });
        setTimeout(() => {
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
           
        }, 1500);
    }

    playSound(sound) {
        this.sounds[sound].currentTime=0;
        this.sounds[sound].play();
      };

    render() {
        return <div className="simon" >
            {BUTTONS.map(b => (
                <SimonBtn  key={b} color={b} active={this.state.activeBtn == b} clickAction={this.activateBtn.bind(this)} />
            ))}
            { this.state.sequenceStep == 0 && this.props.playSequence &&
            <button onClick={this.playSequence.bind(this)}>Play</button>
            }
            </div>
    }

    
}