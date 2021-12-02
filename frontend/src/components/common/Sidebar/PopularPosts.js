import React, { useEffect, useState } from 'react'
import PostItem from './PostItem';
import Skeleton from "react-loading-skeleton";

import API from "../../../services/API";

const PopularPosts = () => {
    const [posts, setPosts] = useState([])
    const [loading, setLoading] = useState(false)
    let url = `/posts/?ordering=-post_views`

    // eslint-disable-next-line
    function timeout(delay) { return new Promise(res => setTimeout(res, delay)) }

    const getPosts = async () => {
        setLoading(true)
        const res = await API.get(url)
        setPosts(res.data.result.slice(0, 3))
        setLoading(false)
    }


    useEffect(() => {
        getPosts()
        console.log(process.env.REACT_APP_API_URL)
        console.log(loading)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url])
    if (loading) return (<Skeleton count={3} height={70} />)

    return (

        <div className="tab-pane fade show active"
            id="popular" aria-labelledby="popular-tab" role="tabpanel">
            <PostItem posts={posts} />
        </div>


    )
}

export default PopularPosts
