import { useEffect, useState } from 'react'
// import PostComments from './PostComments'
// import PostDetailComment from './PostDetailComment'
import ShareButtons from '../utils/ShareButtons'
import axios from "axios";
import { Link } from 'react-router-dom';
import Highlight from 'react-highlight'

export default function PostDetail({ match }) {

    const [post, setPost] = useState('');
    const [mostReadsPosts, setMostReadsPosts] = useState([])
    const url = (`http://127.0.0.1:8000/api/v1/posts/${match.params.slug}/`);
    const urlMostReads = (`http://127.0.0.1:8000/api/v1/posts/most_reads/`);
    // eslint-disable-next-line no-unused-vars
    const [loading, setLoading] = useState(false);


    useEffect(() => {
        const getPost = async () => {
            setLoading(true);
            const res = await axios.get(url)
            setPost(res.data);
            setLoading(false);
        };
        const getMostReadsPost = async () => {
            setLoading(true);
            const resMostReadsPosts = await axios.get(urlMostReads)
            setMostReadsPosts(resMostReadsPosts.data);
            setLoading(false);
        };
        getPost()
        getMostReadsPost()
        window.scrollTo(0, 0)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    if (!post) return null;
    return (
        <div id='intro'>
            <div className="container mx-auto">
                <section className="w-75 mx-auto">
                    <img src={post.image} className='img-fluid w-100 px-5 pt-4'></img>
                    <section className="border-bottom px-5 mx-auto mb-5 mt-3">
                        <div className="row align-items-center pb-2 border-bottom">
                            <div className="col-lg-6 text-center text-lg-start mb-3 m-lg-0">
                                <img src="/img/avatar.jpg"
                                    className="rounded-circle me-2"
                                    height="40" alt=""></img>
                                <span> Published <b>{post.date_display}</b> by </span>
                                <u><b>{post.author}</b></u>
                            </div>
                            <div className="col-lg-6 text-center text-lg-end">
                                <ShareButtons post={post} />
                            </div>
                        </div>
                        <div className="row align-items-center mt-3">
                            <h1 style={{ fontSize: "3em" }} className='text-capitalize fw-bold'>{post.title}</h1>
                            {post.post_tags.map(tag =>
                                <Link to={'/'} key={tag.name}>#{tag.name}</Link>
                            )}
                        </div>
                    </section>
                    <Highlight innerHTML={true}>
                        {post.content}
                    </Highlight>
                    {/* <div id='post-content' dangerouslySetInnerHTML={{ __html: post.content }} /> */}
                </section>
            </div >
            <section className="text-center border-bottom fs-3">
                <p><strong>Thanks for reading :)</strong></p>
            </section>
            <section className="container">
                <div className='text-center my-3'>
                    <h1 className='mb-3 h1'>Most Reads</h1>
                </div>
                <div className=' container row row-cols-1 row-cols-md-4 g-4 justify-content-center'>
                    {mostReadsPosts.map(post =>
                        <div className="col">

                            <div className="card h-100 py-0 border shadow-0">
                                <img src={post.image}
                                    className="card-img-top h-100 bg-light"
                                    alt={post.slug} />
                                <Link id="mostReadId" to={`/posts/${post.slug}`}>
                                    <div className="card-body py-0 bg-light text-dark">
                                        <h4 className="card-title py-0">{post.title}</h4>
                                    </div>
                                </Link>
                                <div className="card-footer text-light py-0">
                                    <small className="text-muted">Published at {post.date_display}</small>
                                </div>
                            </div>

                        </div>
                    )}
                </div>
            </section>
        </div >
    )
}
