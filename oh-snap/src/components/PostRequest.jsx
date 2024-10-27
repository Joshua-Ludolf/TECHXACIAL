import React, { useState, useEffect } from "react";
import axios from "axios";

function PostRequest() {
  const [response, setResponse] = useState(null);

  const api = axios.create({
    baseURL: "http://localhost:5000",
  });

  const handleSubmit = async (e) => {
    const data = { query: "Do you need help?" };
    e.preventDefault();
    console.log("Making POST request");
    try {
      const res = await api.post("/query", data, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      setResponse(res.data);
      console.log(res.data);
    } catch (error) {
      console.error("Error fetching data", error);
    }
  };

 

  return (
    <div>
      erm
      <button onClick={handleSubmit}>Make Post Request</button>
      {response && <div>Response: {JSON.stringify(response)}</div>}
      <div>PostRequest</div>
    </div>
  );
}

export default PostRequest;