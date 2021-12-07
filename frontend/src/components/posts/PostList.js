import React, { useState, useEffect } from 'react'
import API from '../../services/API'
import Pagination from '../utils/Pagination'
import PostCard from './PostCard'


export default function PostList({ match }) {
    const [posts, setPosts] = useState([])
    const [data, setData] = useState({})
    const [page, setPage] = useState(1)
    const [loading, setLoading] = useState(false)

    const categorySlug = match.params.categorySlug !== undefined ? match.params.categorySlug : ''
    const tagSlug = match.params.tagSlug !== undefined ? match.params.tagSlug : ''
    const url = (
        `/posts/${page && `?page=${page}`}${categorySlug && `&category=${categorySlug}`}${tagSlug && `&tag=${tagSlug}`}`
    );

    // eslint-disable-next-line
    function timeout(delay) { return new Promise(res => setTimeout(res, delay)) }

    const getPosts = async () => {
        setLoading(true)
        console.log(url)
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

                    <Pagination data={data} page={page} setPage={setPage} />
                </div>
            </div>
        </div>
    )
}