import React, { useState } from "react";
import PostRequest from "./PostRequest";

function Buttons({ username, onBalanceChange }) {
  const [amount, setAmount] = useState(0);
  const [error, setError] = useState("");

  const handleSend = async () => {
    setError("");
    try {
      const res = await fetch('http://localhost:5000/send_money', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, amount })
      });
      const data = await res.json();
      if (res.status >= 400) {
        setError(data.error || "Failed to send money");
      }
      if (data.balance !== undefined) {
        onBalanceChange(data.balance);
      } else {
        // Fallback: refetch balance
        const b = await fetch(`http://localhost:5000/balance?username=${username}`);
        const bd = await b.json();
        if (bd.balance !== undefined) onBalanceChange(bd.balance);
      }
    } catch (e) {
      console.error(e);
      setError("Network error while sending");
    }
  };

  const handleReceive = async () => {
    setError("");
    try {
      const res = await fetch('http://localhost:5000/add_money', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, amount })
      });
      const data = await res.json();
      if (res.status >= 400) {
        setError(data.error || "Failed to add money");
      }
      if (data.balance !== undefined) {
        onBalanceChange(data.balance);
      } else {
        const b = await fetch(`http://localhost:5000/balance?username=${username}`);
        const bd = await b.json();
        if (bd.balance !== undefined) onBalanceChange(bd.balance);
      }
    } catch (e) {
      console.error(e);
      setError("Network error while receiving");
    }
  };
  return (
    <div>
      <style>
        {`
      button {
      border: 2px solid black;
      padding: 10px;
      border-radius: 5px;
      }
    `}
      </style>
      <input
        type="number"
        className="text-black mr-2"
        value={amount}
        onChange={(e) => {
          const v = parseFloat(e.target.value);
          setAmount(Number.isFinite(v) ? v : 0);
        }}
        placeholder="Amount"
      />
      {error && (<div className="text-red-500 mt-2">{error}</div>)}
      <button onClick={handleSend} disabled={!username || amount <= 0}> Send </button>
      <button onClick={handleReceive} disabled={!username || amount <= 0}>Receive</button>
    </div>
  );
}

export default Buttons;
