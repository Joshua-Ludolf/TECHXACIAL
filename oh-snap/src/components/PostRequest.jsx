import React, { useState, useEffect } from "react";
import axios from "axios";

function PostRequest() {
  const [response, setResponse] = useState(null);
  const [text, setText] = useState('');
    const [translatedText, setTranslatedText] = useState('');
    const [targetLanguage, setTargetLanguage] = useState('');

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

  const addMoney = async (amount, description) => {
    try {
        const response = await axios.post('http://localhost:5000/add_money', 
            { amount, description },
            { headers: { 'Content-Type': 'application/json' } }
        );
        console.log(response.data);
    } catch (error) {
        console.error(error.response.data);
    }
};

   const handleTranslate = async () => {
     try {
         const response = await axios.post('http://localhost:5000/translate', {
             text,
             target_language: targetLanguage
         });
         setTranslatedText(response.data.translatedText);
     } catch (error) {
         console.error('Error translating text:', error);
     }
   };
 

  return (
    <div>
      <button onClick={handleSubmit}>Make Post Request</button>
      {response && <div>Response: {JSON.stringify(response)}</div>}
      <div>PostRequest</div>
    </div>
  );
}

export default PostRequest;
