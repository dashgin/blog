import { useEffect, useState } from 'react'

export default function ShareButtons({ post }) {
    const [tags, setTags] = useState([])
    useEffect(() => {
        setTags(post.post_tags)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <span>
            <a href={`https://www.facebook.com/sharer/sharer.php?u=${window.location.href}`}
                target="_blank" rel="noopener noreferrer"
                className="btn btn-primary me-1">
                <i className="fab fa-facebook-f"></i>
            </a>
            <a href={`https://twitter.com/intent/tweet?hashtags=${tags.map(tag => tag.name)}&text=Look%20at%20this%20post%20about%20${post.title}%20at&url=${window.location.href}`}
                target="_blank" rel="noopener noreferrer"
                className="btn btn-info me-1">
                <i className="fab fa-twitter"></i>
            </a>
            <a href={`https://wa.me/?text=${window.location.href}`}
                target="_blank" rel="noopener noreferrer"
                className="btn btn-success me-1">
                <i className="fab fa-whatsapp"></i>
            </a>
        </span>

    )
}
