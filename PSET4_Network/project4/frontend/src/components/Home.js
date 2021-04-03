import React, { useState, useEffect } from "react";
import Posts from "./Posts";
import NewPost from "./NewPost";

const Home = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetch(`/posts`)
            .then(response => response.json())
            .then(result => {
                setPosts(result)
                // Object.entries(result).forEach(([k, v]) => {
                //     console.log("The value: ", v)
                // })
            })
    }, []);

    return (
        <div>
            <h3>Home:</h3>
            <NewPost />
            <Posts posts={posts} />
        </div>
    );
};

export default Home;
