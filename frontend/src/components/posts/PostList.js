import React, { useState, useEffect } from 'react'
import API from '../../services/API'
import PostCard from './PostCard'


export default function PostList() {
    const [posts, setPosts] = useState([])
    const [data, setData] = useState({})
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(false)

    let url = `/posts/${page && `?page=${page}`}`

    // eslint-disable-next-line
    function timeout(delay) { return new Promise(res => setTimeout(res, delay)) }

    const getPosts = async () => {
        setLoading(true)
        const res = await API.get(url)
        setData(res.data)
        setPosts(res.data.result)
        setLoading(false)
    }


    useEffect(() => {
        getPosts()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url])

    return (
        <div>
            <div className="padding-30 rounded bordered">
                <div className="row gy-5">
                    <div className="col-sm-12">
                        {posts.map(
                            post => (
                                <PostCard post={post} loading={loading} key={post.id} />
                            )
                        )}
                    </div>

                    <div className="text-center">
                        {/* <button className="btn btn-simple">Load More</button> */}
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
                                    <span className="page-link py-1">{page}</span>
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
        </div>
    )
}