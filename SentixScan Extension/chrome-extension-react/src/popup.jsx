import React from "react";
import { render } from "react-dom";

function Popup() {
    return (
        <div center="true">

            <h2>Press to analyze reviews</h2>

            {/* 
            <img src="background.png" alt="logo" width="500" /><br />

            <div>
                <img src="SentixScan-icon.png" alt="logo" width="150" height="150" />
            </div>
             */}
            
        </div>
    );
}

render(<Popup />, document.getElementById("react-target"));