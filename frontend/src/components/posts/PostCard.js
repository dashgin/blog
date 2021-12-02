import React from 'react'
import Skeleton from "react-loading-skeleton";
import { Link } from "react-router-dom";


const PostCard = ({ post, loading }) => {
    const aImage = 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png';

    if (loading) return (<Skeleton count={3} height={120} />)

    return (
        <div className="post border-bottom pb-4 mb-4" key={post.id}>
            <div className="thumb rounded">
                <a href="/" className="category-badge position-absolute">{post.category}</a>
                <Link to={`/posts/${post.slug}/`}>

                    <div className="inner"  style={{maxHeight:"300px", width:"100%"}}>
                        <img src={post.image} width="100%" alt="" />
                    </div>
                </Link>

            </div>
            <ul className="meta list-inline mt-4 mb-0">
                <li className="list-inline-item">
                    <span>
                        <img src={aImage} width="30" className="author" alt="" />
                        {post.author}
                    </span>
                </li>
                <li className="list-inline-item">
                    {post.date_display}
                </li>
                <li className="list-inline-item">
                    {post.reading_time}
                </li>
            </ul>
            <h5 className="post-title mb-3 mt-3">
                <Link to={`/posts/${post.slug}/`}>
                    {post.title}
                </Link>
            </h5>
            <p className="excerpt mb-0 px-1">
                {post.post_tags.map(tag => (
                    <small className="tag border-0 py-1 px-2 ms-1 bg-dark text-white">#{tag.name}</small>
                ))}
                <small className="float-end">
                    <i className="fas fa-eye"></i> {post.post_view_count}
                </small>
                {/* <Link to=''>Read more &gt;</Link> */}
            </p>
        </div>



    )
}

export default PostCard;