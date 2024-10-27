import axios from "axios";
import React, { useState } from "react";
import { Link } from "react-router-dom";

function Register({ setIsAuthenticated }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // const handleSubmit = (e) => {
  //   e.preventDefault();

  //   // Add authentication logic here
  //   setIsAuthenticated(true);
  // };

  const handleUsernameChange = (e) => {
    console.log("Username changed:", e.target.value);
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    console.log("Password changed:", e.target.value);
    setPassword(e.target.value);
  };

  const [response, setResponse] = useState(null);

  const api = axios.create({
    baseURL: "http://localhost:5000",
  });

  const handleSubmit = async (e) => {
    const data = { username: { username }, password: { password } };
    e.preventDefault();
    console.log("Authenticating...");
    try {
      const res = await api.post("/login", data, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      setResponse(res.data);
      console.log(res.data);
      if (res.data.success) {
        setIsAuthenticated(true);
      } else {
        alert("register failed");
      }
    } catch (error) {
      alert("Error during register");
      console.error("Error fetching data", error);
    }
  };

  return (
    <>
      <main>
        <h1>Register</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username">Username:</label>
            <input
              className="text-black"
              type="text"
              id="username"
              value={username}
              onChange={handleUsernameChange}
            />
          </div>
          <div>
            <label htmlFor="password">Password:</label>
            <input
              className="text-black"
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
            />
          </div>
          <button type="submit">Register</button>
        </form>

        <Link to="/login">Already have an account? Login</Link>
        <br/>
        <Link to="/">Back to Home</Link>
      </main>
    </>
  );
}

export default Register;
