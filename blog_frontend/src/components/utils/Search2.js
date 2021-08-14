import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Skeleton from "react-loading-skeleton";
import { Link } from 'react-router-dom'

export default function Search() {
    const [posts, setPosts] = useState([])
    const [search, setSearch] = useState('')
    const [loading, setLoading] = useState(false)
    const [pageSize, setPageSize] = useState(1)

    let url = `http://localhost:8000/api/v1/posts/?page_size=${pageSize}&search=${search}`

    function timeout(delay) { return new Promise(res => setTimeout(res, delay)) }

    const getPosts = async () => {
        setLoading(true)
        await timeout(1000)
        const res = await axios.get(url)
        setLoading(false)
        setPosts(res.data.results)
        posts ? setPageSize(res.data.count) : setPageSize(1)
    }

    console.log(url)
    useEffect(() => {
        getPosts()
        window.scrollTo(0, 0)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [url])


    return (

        <form className='input-group w-auto' method='get'>

            <input onChange={event => setSearch(event.target.value)}
                autoComplete={'off'}
                type='search' className='form-control  dropdown-toggle'
                placeholder='Search' data-mdb-toggle="dropdown"
                aria-expanded="true" aria-label='Search' id="search"
                aria-describedby='search-addon'>
            </input>
            <button class="btn btn-outline-primary rounded"
                type="button"
            //  onClick={document.getElementById('search').innerText = ''}
            >
                <i class="fas fa-search"></i>
            </button>

            <ul
                className="dropdown-menu dropdown-menu dropdown-menu-end w-100"
                style={{ maxHeight: '13.5em', overflowY: 'auto' }}>
                {
                    loading ?
                        <li>
                            <Skeleton height={32} />
                        </li>
                        :
                        search && posts.map(post =>
                            <li key={post.id}><Link to={`/posts/${post.slug}`} className="dropdown-item" type="button">{post.title} - {post.subtitle}</Link></li>
                        )
                }

            </ul>
        </form>
    )
}
