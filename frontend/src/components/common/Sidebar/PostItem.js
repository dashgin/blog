import React from 'react'

const PostItem = ({ posts }) => {
    return (
        <div>
            {
                posts && posts.map(post => {
                    return (
                        <div className="post post-list-sm" key={post.id}>
                            <div className="details clearfix">
                                <h6 className="post-title my-0 fs-5 px-0">
                                    <a href="!#">{post.title}</a>
                                </h6>
                                <ul className="meta list-inline mt-1 mb-0">
                                    <li className="list-inline-item">
                                        {post.date_display} - {post.reading_time} read
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
