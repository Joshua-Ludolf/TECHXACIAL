import React, { useState, useEffect } from "react";
import axios from "axios";

function PostRequest() {
  const [response, setResponse] = useState(null);

  const api = axios.create({
    baseURL: "http://locahost:5000",
  });

  const handlePostRequest = () => {
    console.log("Making GET request");
    api
      .get("/")
      .then((res) => {
        console.log(res.data);
      })
      .catch((error) => {
        console.error("Error fetching data", error);
      });
  };

  return (
    <div>
      erm
      <button onClick={handlePostRequest}>Make Post Request</button>
      {response && <div>Response: {JSON.stringify(response)}</div>}
      <div>PostRequest</div>
    </div>
  );
}

export default PostRequest;
