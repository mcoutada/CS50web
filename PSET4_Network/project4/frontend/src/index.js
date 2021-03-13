import React from "react";
import ReactDOM from "react-dom";
import Register from "./components/Register";
import Home from "./components/Home";

const home = (
    <div>
        <Home />
    </div>
);

const register = (
    <div>
        <Register />
    </div>
);

const rootElement = document.getElementById("index");
if (rootElement) {
    ReactDOM.render(home, rootElement);
}

const registerElement = document.getElementById("register");
if (registerElement) {
    ReactDOM.render(register, registerElement);
}
