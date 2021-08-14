import React, { useState, useEffect } from 'react'
import axios from 'axios'
import PostCard from './PostCard'
// import Pagination from '../utils/Pagination'


export default function PostList() {
    const [posts, setPosts] = useState([])
    const [data, setData] = useState('')
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(false)

    let url = `http://localhost:8000/api/v1/posts/${page && `?page=${page}`}`

    function timeout(delay) { return new Promise(res => setTimeout(res, delay)) }

    const getPosts = async () => {
        setLoading(true)
        await timeout(1)
        const res = await axios.get(url)
        setData(res.data)
        setPosts(res.data.results)
        setLoading(false)
    }


    // console.log(url)
    useEffect(() => {
        getPosts()
        window.scrollTo(0, 0)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url])

    return (
        <div>
            {/* <!-- Jumbotron --> */}
            <div id='intro' className='p-2 text-center bg-image'
                style={{ backgroundImage: 'url(img/jumbotron.jpg)', height: '35vh' }}>
                <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }} >
                    <div className='d-flex justify-content-center align-items-center h-100'>
                        <div className='text-white'>
                            <h1 className='mb-3 h1'>Technology Blog</h1>
                            <a className='btn btn-outline-light btn-lg m-2' href='/' role='button'>Download CV</a>
                        </div>
                    </div>
                </div>
            </div>

            <div className="col-md-6 mb-4 mx-auto">
                <section className="mb-4">
                    <h2 className="mb-5 pt-4 ps-4">
                        Latest Posts
                    </h2>
                </section>
                <div className="row row-cols-1 g-4 px-4">
                    <PostCard posts={posts} loading={loading} />
                    <nav className="my-4" aria-label="Page navigation example">
                        <ul className="pagination justify-content-center">
                            <li className={
                                `${data.previous ? "page-item px-1 " : "page-item px-1 d-none"}`
                            }>
                                <button className="page-link"
                                    onClick={
                                        () => data.previous ? setPage(page - 1) : ''
                                    }>⟨⟨</button>
                            </li>
                            <li className="page-item active">
                                <span className="page-link">{page}</span>
                            </li>
                            <li className={`${data.next ? "page-item px-1 " : "page-item px-1 d-none"}`}>
                                <button className="page-link"
                                    onClick={() => data.next ? setPage(page + 1) : ''}>⟩⟩</button>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    )
}