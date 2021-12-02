import { useEffect, useState } from 'react'
import ShareButtons from '../utils/ShareButtons'
import { Link } from 'react-router-dom';
import Highlight from 'react-highlight'
import { DiscussionEmbed } from 'disqus-react';
import API from '../../services/API'


export default function PostDetail({ match }) {

    const [post, setPost] = useState('');

    const url = (`/posts/${match.params.slug}/`);

    useEffect(() => {
        const getPost = async () => {
            const res = await API.get(url)
            setPost(res.data);
        };
        getPost()
    }, [url]);

    if (!post) return null;
    return (
        <div className="blog-post-content">
            <img className="rounded" src={post.image} alt={post.slug}></img>
            <h1 style={{ fontSize: "3em" }}>{post.title}</h1>
            <div>

                <span><b>{post.date_display}</b> by </span>
                <u>{post.author}</u>

                <span className='float-end'><ShareButtons post={post} /></span>
            </div>

            <div className="my-2">
                {post.post_tags.map(tag =>
                    <Link className='tag me-2' to={'/'} key={tag.name}>{tag.name}</Link>
                )}

            </div>
            <Highlight innerHTML={true}>
                {post.content}
            </Highlight>
            {/* <div id='post-content' dangerouslySetInnerHTML={{ __html: post.content }} /> */}

            <section className="text-center border-bottom fs-3">
                <p><strong>Thanks for reading :)</strong></p>
            </section>
            <hr></hr>
            <DiscussionEmbed
                shortname='dashgin-personal-blog'
                config={
                    {
                        url: window.location.href,
                        identifier: post.slug,
                        title: post.title,
                        language: 'en_UK'
                    }
                }
            />
        </div>
    )
}
