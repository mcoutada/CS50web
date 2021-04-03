import React from "react";
import ReactDOM from "react-dom";
import Home from "./components/Home";
import Profile from "./components/Profile";

const home = (
    <div>
        <Home />
    </div>
);

const profile = (
    <div>
        <Profile />
    </div>
);

const rootElement = document.getElementById("index");
if (rootElement) {
    ReactDOM.render(home, rootElement);
}

const profileElement = document.getElementById("profile");
if (profileElement) {
    ReactDOM.render(profile, profileElement);
}
