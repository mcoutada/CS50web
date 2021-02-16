import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import React, { useState } from "react";

function AddPersonForm() {
  const [person, setPerson] = useState("");

  function handleChange(e) {
    setPerson(e.target.value);
  }

  function handleSubmit(e) {
    e.preventDefault();
  }
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Add new contact"
        onChange={handleChange}
        onSubmit={handleSubmit}
        value={person}
      />
      <button type="submit">Add</button>
    </form>
  );
}

function ContactList(props) {
  const dataList = props.data;

  const listItems = dataList.map((val, index) => <li key={index}>{val}</li>);
  return <ul>{listItems}</ul>;
}

function ContactManager() {
  return (
    <div>
      <AddPersonForm />
      <ContactList data={theList} />
    </div>
  );
}

const theList = ["a", "b", "c"];
// const el = <AddPersonForm />;
// const el = <ContactList data={theList} />;

const el = <ContactManager />;
ReactDOM.render(el, document.getElementById("root"));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
