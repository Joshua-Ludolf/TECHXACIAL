import React, { useState, useEffect } from "react";
import axios from "axios";



function PostRequest( { chatInput, user, responses, setResponses } ) {
  const [response, setResponse] = useState(null);
  const [text, setText] = useState('');
    const [translatedText, setTranslatedText] = useState('');
    const [targetLanguage, setTargetLanguage] = useState('');

  const api = axios.create({
    baseURL: "http://localhost:5000",
  });

  const handleSubmit = async (e) => {
    const data = { query: chatInput };
    e.preventDefault();
    console.log("Making POST request");
    try {
      const res = await api.post("/query", data, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      setResponse(res.data);
      setResponses([...responses, res.data]);
      console.log(res.data);
      console.log(responses)
    } catch (error) {
      console.error("Error fetching data", error);
    }
  };



     const addMoney = async (amount, description) => {
     try {
       const response = await axios.post('http://localhost:5000/add_money', 
         { username: user?.username, amount },
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
      <button onClick={handleSubmit} type="submit"
        className="bg-[#0b6380] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Send

        
      </button>
      
    </div>
  );
}

export default PostRequest;
