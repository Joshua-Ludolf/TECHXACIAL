import axios from "axios";
import React, { useState } from "react";
import { Link, redirect, useNavigate } from "react-router-dom";

function Login({ setIsAuthenticated, setUser, user }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

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
      console.log(res.data.response);
      if (res.data.response === "Logged In") {
        setIsAuthenticated(true);
        console.log("User in Login: ", res.data.user);
        setUser(res.data.user);
        navigate("/balance");
      } else {
        alert("Login failed");
      }
    } catch (error) {
      alert("Error during login");
      console.error("Error fetching data", error);
    }
  };

  return (
    <main>
      <h1>Login</h1>
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
        <button type="submit">Login</button>
      </form>

      <Link to="/register">Don't have an account? Register here</Link>
      <br />

      <Link to="/">Back to Home</Link>
    </main>
  );
}

export default Login;
