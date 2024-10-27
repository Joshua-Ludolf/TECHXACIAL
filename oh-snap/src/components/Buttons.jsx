import React from "react";
import PostRequest from "./PostRequest";

function Buttons() {
  const handleSend = () => {
    console.log("Send/Receive button clicked");
  };
  const handleCashIn = () => {
    console.log("Cash-In button clicked");
  };
  const handlePay = () => {
    console.log("Pay button clicked");
  };
  const handleReceive = () => {
    console.log("Receive button clicked");
  };
  return (
    <div>
      <style>
        {`
      button {
      border: 2px solid black;
      padding: 10px;
      border-radius: 5px;
      }
    `}
      </style>
      <button onClick={handlePay}> Send </button>
      <button onClick={handleReceive}>Receive</button>
      <button onClick={handleCashIn}> Cash-In </button>
    </div>
  );
}

export default Buttons;
