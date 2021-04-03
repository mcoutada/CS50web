import React from 'react'
import Post from "./Post"

const Posts = ({posts}) => {
    return (
        <div id="posts">
            <h3>Posts:</h3>
            {Object.values(posts).map( (post, index) =>(
                <Post key={index} post={post}/>
                // console.log(post)
            )) }
        </div>
    )
}

export default Posts
