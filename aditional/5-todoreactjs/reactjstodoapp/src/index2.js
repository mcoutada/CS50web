import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import React, { useState } from 'react'; 

function CntApp() {
  const [cnt, setCnt] = useState(0);
  
  function handleChange() {
    setCnt(cnt+1);
  }


  return (<div>
              <h1>  {cnt}  </h1>
              <button onClick={handleChange}>Submit</button>
          </div>
         ) ;
}

const el = <CntApp />; 
ReactDOM.render(
  el, 
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
