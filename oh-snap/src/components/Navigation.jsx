import React from "react";
import { Link } from "react-router-dom";
import { IoHome } from "react-icons/io5";
import { FaBook, FaCamera } from "react-icons/fa";

function Navigation() {
  return (
    <nav className="">
      <ul>
        <li className="">
          <Link to={"/scan"}>
            <p className="icon">
              <FaCamera />
            </p>
            Scan
          </Link>
        </li>
        <li>
          <Link to={"/"}>
            <p className="icon">
              <IoHome />
            </p>
            Home
          </Link>
        </li>
        <li>
          <Link to={"/education"}>
            <p className="icon">
              <FaBook />
            </p>
            Education
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
