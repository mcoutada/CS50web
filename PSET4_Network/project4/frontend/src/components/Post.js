import React from "react";

const Post = ({ post }) => {
    let profile_page = `/profile/${post.writer_id}`;
    console.log('1');

    return (

        <div className="card">
            <div className="card-body">
                <h5 className="card-title">
                    <a href={profile_page}>{post.writer_name}</a>
                </h5>
                <h6 className="card-subtitle mb-2 text-muted">
                    {post.timestamp}
                </h6>
                <p className="card-text">{post.content}</p>
                <p className="card-text">{post.likes} likes</p>
            </div>
        </div>
    )
}

export default Post;
