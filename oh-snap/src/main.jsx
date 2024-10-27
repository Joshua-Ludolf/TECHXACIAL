import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Contact from "./routes/Education.jsx";
import Navigation from "./components/Navigation.jsx";
import Education from "./routes/Education.jsx";
import Scan from "./routes/Scan.jsx";
import PostRequest from "./components/PostRequest.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route index={true} path="/" element={<App />} />
        <Route path="/:id" element={<App />} />
        <Route path="/education" element={<Education />} />
        <Route path="/scan" element={<Scan />} />
      </Routes>
      <Navigation />

    </BrowserRouter>
  </StrictMode>
);
