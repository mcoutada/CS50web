import React from "react";
import { useEffect, useState } from "react";
import Posts from "./Posts";

const Profile = () => {
    const [userposts, setUserposts] = useState([]);
    const [followers, setFollowers] = useState([]);
    const [following, setFollowing] = useState([]);
    const [followbutton, setFollowbutton] = useState([]);

    let route = window.location.href.split("/");
    let profile_id = route[route.length - 1];

    console.log(route);
    useEffect(() => {
        fetch(`/profile/${profile_id}`, { method: "GET" })
            .then((response) => response.json())
            .then((result) => {
                console.log(result);
            });
    }, []);

    return (
        <div>
            <h2>My profile</h2>
            {/* <Posts posts={userposts} /> */}
        </div>
    );
};

export default Profile;
