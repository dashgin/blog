import React from 'react'
import { Link } from 'react-router-dom'

const PostArchive = () => {
    const postsArray = [
        {
            year: '2020',
            posts: [
                {
                    id: 1,
                    title: 'Post 1 Lorem ipsum dolor sit amet consectetur adipisicing elit.',
                    date: 'May 29'
                },

                {
                    id: 2,
                    title: 'Post 2 Lorem ipsum dolor sit amet consectetur adipisicing elit.',
                    date: 'Aug 29'

                }
            ]
        }
    ]
    return (
        <div className='mt-5' >
            {
                postsArray.map(archive => (
                    <div className="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">
                        <div className="h3">
                            <u>{archive.year}</u>
                        </div>

                        {archive.posts.map(post => (
                            < Link to='/'>
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
