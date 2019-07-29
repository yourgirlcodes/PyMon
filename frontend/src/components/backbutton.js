import React from "react";

export default class BackBtn extends React.Component {
    constructor(props){
        super(props); 
    }
    render(){
       return <button className="backBtn" onClick={() => location.replace("http://localhost:5001/games")}>back</button>;
    }
}
