import React from "react";
import { GiTurtle } from "react-icons/gi";
import { Link } from "react-router-dom";

function Start() {
  return (
    <>
      <div>
        <GiTurtle size={150} />
      </div>
      <div>
        <p style={{ fontSize: "75px" }}>Oh-Snap</p>
      </div>
      <div>
        <button onClick={() => {}}>Register</button>
      </div>
      <div>
        <Link to="/login">Login</Link>
        {/* <button onClick={() => {}}>Log In</button> */}
      </div>
    </>
  );
}

export default Start;
