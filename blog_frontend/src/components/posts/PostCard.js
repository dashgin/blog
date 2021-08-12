import React from 'react'
import Skeleton from "react-loading-skeleton";
import { Link } from "react-router-dom";

const PostCard = ({ posts, loading }) => {
    if (loading) {
        return (
            <Skeleton count={3} height={320}/>
        )
    }
    return (
        posts.map(post =>
            <div className="col mb-3" key={post.id}>
                <div className="card h-100 rounded-2 shadow-0 border">
                    <div className="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
                        <img src={post.image} className="img-fluid" alt="post"
                            style={{ height: "210px", width: "100%" }}></img>
                        <Link to={`/posts/${post.slug}`}>
                            <div className="mask"
                                style={{ backgroundColor: "rgba(251, 251, 251, 0.15)" }}></div>
                        </Link>
                    </div>
                    <div className="card-body py-2">
                        <h5 className="card-title">
                            <Link to={`/posts/${post.slug}`}>{post.title}</Link>
                        </h5>
                        <p className="card-text">
                            {post.subtitle}
                        </p>
                    </div>
                    <div className="card-footer text-end py-1">
                        <a href="#!"><i
                            className="far fa-comments"></i> 1</a> | <i className="far fa-eye"></i> {post.post_views_count}
                        <small className="text-muted float-start">{post.date_display}</small>
                    </div>
                </div>
            </div>

        )
    )
}

export default PostCard;