import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

export default function PostList({ match }) {

    const [posts, setPosts] = useState([]);
    const [data, setData] = useState('');
    const url = (`http://127.0.0.1:8000/api/v1/categories/${match.params.slug}/`);

    const getPosts = async () => {
        const res = await axios.get(url)
        setData(res.data);
        setPosts(res.data.category_posts);
    };
    useEffect(() => {
        getPosts()
        window.scrollTo(0, 0)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url]);

    return (
        <div>
            {/* <!-- Jumbotron --> */}
            <div id='intro' className='mb-5'></div>
            <div className="col-md-8 mb-4 mx-auto">
                <section className="mb-4">
                    <h2 className="mb-5 pt-4">
                    Category - {data.name} ({posts.length})
                    </h2>
                </section>
                <div className="row row-cols-1 g-4 px-4">
                    {posts.map(post =>
                        <div className="col m-1" key={post.id}>

                            <ul className="py-1 ps-1 border-bottm" itemType=''>
                                <li className="card-title">
                                    <h5><Link to={`/posts/${post.slug}`}>{post.title} - {post.subtitle}</Link></h5>
                                </li>
                            </ul>

                        </div>

                    )}

                </div>
            </div>
        </div >
    )
}