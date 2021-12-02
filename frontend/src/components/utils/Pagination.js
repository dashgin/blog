import React, { useState } from 'react'

const Pagination = (prev, next) => {

    const [page, setPage] = useState(1)

    return (
        <nav className="my-4" aria-label="Page navigation example">
            <ul className="pagination justify-content-center">
                <li className={
                    `${prev ? "page-item px-1 " : "page-item px-1 d-none"}`
                }>
                    <button className="page-link"
                        onClick={
                            () => prev ? setPage(page - 1) : ''
                        }>⟨⟨</button>
                </li>
                <li className="page-item active">
                    <span className="page-link">{page}</span>
                </li>
                <li className={`${next ? "page-item px-1 " : "page-item px-1 d-none"}`}>
                    <button className="page-link"
                        onClick={() => next ? setPage(page + 1) : ''}>⟩⟩</button>
                </li>
            </ul>
        </nav>

    )
}

export default Pagination
