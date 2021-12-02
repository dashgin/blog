import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import API from '../../../services/API'

const Tags = () => {

    const [tags, setTags] = useState([])

    const getTags = async () => {
        const res = await API.get('/posts/tags/')
        setTags(res.data)
    }

    useEffect(() => {
        getTags()
    }, [])
    return (
        <div className="widget rounded">
            <div className="widget-header text-center">
                <h3 className="widget-title">Tags</h3>
            </div>
            <div className="widget-content">
                {
                    tags.map(tag => (
                        <Link to={`/tags/${tag.slug}`} className="tag me-1" key={tag.slug}>
                            {'#' + tag.name}
                        </Link>
                    ))
                }

            </div>
        </div>
    )
}

export default Tags
