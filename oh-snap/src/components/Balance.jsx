import React, { useEffect, useState } from "react";
import NavScreen from "./NavScreen";
import Buttons from "./Buttons";

function Balance({ user }) {
  const [balance, setBalance] = useState(0);

  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const res = await fetch(`http://localhost:5000/balance?username=${user?.username}`);
        const data = await res.json();
        setBalance(data.balance || 0);
      } catch (e) {
        console.error(e);
      }
    };
    if (user?.username) fetchBalance();
  }, [user?.username]);

  return (
    <>
      <div className="mt-12">
        {!user?.username ? (
          <div className="text-red-500">You must be logged in to view balance.</div>
        ) : (
          <>
            <h1 className="text-2xl">Hello, {user?.username}</h1>
            <p style={{ fontSize: "80px" }}>${balance}</p>
            <Buttons username={user?.username} onBalanceChange={setBalance} />
          </>
        )}
      </div>
    </>
  );
}

export default Balance;
