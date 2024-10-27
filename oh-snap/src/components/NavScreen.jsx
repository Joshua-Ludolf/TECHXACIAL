import React, { useState } from "react";
import { IoSettingsOutline } from "react-icons/io5";
import { CgProfile } from "react-icons/cg";
import { FaBook, FaBookOpen } from "react-icons/fa6";
import { GiTurtleShell, GiTurtle } from "react-icons/gi";
import Navigation from "./Navigation";

function NavScreen( {setIsAuthenticated} ) {
  const [isDrawerOpen, setDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!isDrawerOpen);
  };

  const [isOpen, setIsOpen] = useState(false);

  const dropdown = () => {
    setIsOpen(!isOpen);
  };
  return (
    <>
      <div style={{ position: "absolute", top: 0, right: 0 }} className="p-5">
        <button
          style={{
            background: "none",
            border: "none",
            cursor: "pointer",
            padding: "0",
            outline: "none",
          }}
          onClick={dropdown}
        >
          <FaBook size={45} />
        </button>
        {isOpen && <Navigation />}
      </div>
      <div style={{ position: "absolute", bottom: 0, left: 0 }} className="p-5">
        <button
          style={{
            background: "none",
            border: "none",
            cursor: "pointer",
            padding: "0",
            outline: "none",
          }}
          onClick={() => {}}
        >
          <GiTurtle size={75} />
        </button>
      </div>
      <div style={{ position: "absolute", top: 0, left: 0 }}>
        <button
          style={{
            background: "none",
            border: "none",
            cursor: "pointer",
            padding: "0",
            outline: "none",
          }}
          onClick={toggleDrawer}
        >
          <CgProfile size={45} />
        </button>

        {isDrawerOpen && (
          <div
            className="drawer flex flex-col justify-center items-center round-lg h-full w-full"
            style={{ backgroundColor: isDrawerOpen ? "black" : "red" }}
          >
            {
              <>
                <div>Username</div>
                <div className="justify-center">
                  <IoSettingsOutline size={45} />
                </div>
              </>
            }
            <button onClick={toggleDrawer}>Close Drawer</button>
          </div>
        )}
      </div>
    </>
  );
}

export default NavScreen;
