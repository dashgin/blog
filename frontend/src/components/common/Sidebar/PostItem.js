import React from 'react'

const PostItem = ({ posts }) => {
    return (
        <div>
            {
                posts && posts.map(post => {
                    return (
                        <div className="post post-list-sm circle" key={post.id}>
                            <div className="thumb circle">
                                <a href="!#">
                                    <div className="inner">
                                        <img src={post.image} width="100" alt="" />
                                    </div>
                                </a>
                            </div>
                            <div className="details clearfix">
                                <h6 className="post-title my-0">
                                    <a href="!#">{post.title}</a>
                                </h6>
                                <ul className="meta list-inline mt-1 mb-0">
                                    <li className="list-inline-item">
                                        <i className="fas fa-eye"></i> {post.post_view_count} - {post.date_display}
                                    </li>
                                </ul>
                            </div>
                        </div>
                    )
                }

                )
            }

        </div>
    )
}


export default PostItem
