import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import API from '../../services/API'
import Skeleton from "react-loading-skeleton";


const PostArchive = () => {
    const [postsArchive, setPostsArchive] = useState([])
    const [loading, setLoading] = useState(true)

    const getPostsArchive = async () => {
        setLoading(true)
        const response = await API.get('/posts/archive')
        setPostsArchive(response.data)
        setLoading(false)
    }

    useEffect(() => {
        getPostsArchive()
    }, [])
    if (loading) return (
        <div className='mt-5' >
            <Skeleton count={2} height={107} />
        </div>
    )
    return (
        <div className='mt-5' >
            {
                postsArchive.map(archive => (
                    <div className="shadow-sm shadow bordered mb-2 p-2 rounded" key={archive.year}>
                        <div className="h3 text-dark">
                            <u>{archive.year}</u>
                        </div>

                        {archive.posts.map(post => (
                            < Link to={`/posts/${post.slug}/`} key={post.slug}>
                                <p className="text-gray-500 ps-4 mt-3"><small>{post.date}</small> <span className='ps-2 h5'>{post.title}</span></p>
                            </Link>
                        ))}
                    </div>

                ))
            }
        </div >
    )
}

export default PostArchive
