import React, { useState } from "react";
import NavScreen from "./NavScreen";
import Buttons from "./Buttons";

function Balance({ user }) {
  return (
    <>
      <div className="mt-12">
        <h1 className="text-2xl">Hello, {user[1]}</h1>
        {console.log("User in Balance: ", user)}  
        <p style={{ fontSize: "80px" }}>${user[5]}</p>
        <Buttons />
      </div>
    </>
  );
}

export default Balance;
