// import React, { useState } from 'react'

const Pagination = (nextPage, prevPage) => {

    // const [currentPage, setCurrentPage] = useState(2)
    // const [url, setUrl] = useState('http://localhost:8000/api/v1/posts/');

    return (
        <nav className="my-4" aria-label="Page navigation example">
        {/* <ul className="pagination justify-content-center">

            <li className={
                `${prevPage ? "page-item px-1 " : "page-item px-1 d-none"}`
            }>
                <button className="page-link"
                    onClick={
                        () => prevPage ? setUrl(prevPage) : ''
                    }>⟨⟨</button>
            </li>
            <li className="page-item active">
                <span className="page-link">'currentPage'</span>
            </li>
            <li className={`${nextPage ? "page-item px-1 " : "page-item px-1 d-none"}`}>
                <button className="page-link"
                    onClick={
                        () => nextPage ? setUrl(nextPage) : ''
                    }>⟩⟩</button>
            </li>

        </ul>*/}
    </nav> 
    )
}

export default Pagination;