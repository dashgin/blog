import React, { useEffect, useState } from 'react'
import PostItem from './PostItem';
import Skeleton from "react-loading-skeleton";

import API from "../../../services/API";
const RecentPosts = () => {

    const [posts, setPosts] = useState([])
    const [loading, setLoading] = useState(false)
    let url = `/posts/?ordering=-created_at`

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
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url])
    if (loading) return (<div  className="tab-pane fade"><Skeleton count={3} height={70} /></div>)

    return (

        <div className="tab-pane fade"
            id="recent" aria-labelledby="recent-tab" role="tabpanel">
            <PostItem posts={posts} />
        </div>


    )
}

export default RecentPosts
