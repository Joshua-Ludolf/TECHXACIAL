import React, { useState } from "react";
import NavScreen from "./NavScreen";
import Buttons from "./Buttons";

function Balance( { user }) {
  return (
    <>
      <div>
        <p style={{ fontSize: "100px" }}>$1000</p>
        <Buttons />
      </div>
      <NavScreen />
    </>
  );
}

export default Balance;
