import React from "react";

export default class Loader extends React.Component {
    render() {
        let styles={};
        return <div className="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
    }
}