import { useState } from "react";
import "./App.css";
import Balance from "./components/Balance";
import Buttons from "./components/Buttons";
import PostRequest from "./components/PostRequest";
import Start from "./routes/Start";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NavScreen from "./components/NavScreen";
import Login from "./auth/Login";
import Register from "./auth/Register";
import Education from "./routes/Education";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState({});

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Start />} />
        <Route path="/balance" element={<Balance user={user} />} />
        <Route path="/education" element={<Education user={user} />} />
        <Route
          path="/login"
          element={<Login setIsAuthenticated={setIsAuthenticated} setUser={setUser} user={user} />}
        />
        <Route
          path="/register"
          element={<Register setIsAuthenticated={setIsAuthenticated} />}
        />
        {/* Add more routes as needed */}
      </Routes>
      {isAuthenticated ? (
        <NavScreen setIsAuthenticated={setIsAuthenticated} user={user} />
      ) : (
        <div></div>
      )}
    </BrowserRouter>
  );
}

export default App;
