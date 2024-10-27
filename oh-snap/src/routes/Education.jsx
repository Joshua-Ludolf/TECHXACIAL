import React, { useState } from "react";
import PostRequest from "../components/PostRequest";
import Markdown from 'react-markdown'
import { GiTurtleShell, GiTurtle } from "react-icons/gi";



function Education({ user }) {
  const [chatInput, setChatInput] = useState("");
  const [responses, setResponses] = useState([{response: `Oh Snap! Hey, ${user[1]}! How can I help you today? 
    Try typing "*What SNAP benifits do I qualify for?*" or "*How can I better manage my money?*"`}]);

  
  return (
    <>
      <main>
      <h1 className="text-5xl">Education</h1>

        <div className="">
          <form className="flex flex-row mt-6">
          <input
              type="text"
              value={chatInput}
              onChange={(e) => setChatInput(e.target.value)}
              placeholder="Type your message here..."
              className="border p-2 w-full text-black"
            />
                    <PostRequest user={user} chatInput={chatInput} responses={responses} setResponses={setResponses}/>

          </form>
            

          </div>
          <div>
          {responses.map((newResponse, index) => {
        return <div key={index} className="text-black bg-white p-4 m-2 rounded-lg flex flex-row text-left	">
          <div className="mr-6 ">
          <GiTurtle size={40} className="bg-[#006d5b] p-1 rounded-full text-white" />

          </div>
          <div>
          <Markdown>{newResponse["response"]}</Markdown></div>
          </div>
      }).reverse()}
      {/* <Markdown>{markdown}</Markdown> */}


          </div>

        
        {console.log("User in Education: ", user)}
        
      </main>
    </>
  );
}

export default Education;
