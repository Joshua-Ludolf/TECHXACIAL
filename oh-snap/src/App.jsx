import { useState } from "react";
import "./App.css";
import Balance from "./components/Balance";
import Buttons from "./components/Buttons";
import PostRequest from "./components/PostRequest";

function App() {
  return (
    <>
      <main>
        <Balance />
        <Buttons />
        <PostRequest />
      </main>
    </>
  );
}

export default App;
