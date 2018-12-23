import React from "react";

export default class SimonBtn extends React.Component {
    render() {
        return <button onClick={this.activate.bind(this)} className={`${this.props.color} ${(this.props.active)? "active" : ""}`}>
        
        </button>
    }

    activate(){
        this.props.clickAction(this.props.color)
    }
}