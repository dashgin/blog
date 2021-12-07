import React from 'react'

const Pagination = ({ data, page, setPage }) => {

    return (
        <div className="text-center">

            <nav className="my-4">
                <ul className="pagination justify-content-center">
                    <li className={
                        `${data.previous ? "page-item " : "page-item d-none"}`
                    }>
                        <span className="page-link"
                            onClick={
                                () => data.previous ? setPage(page - 1) : ''
                            }>⟨⟨</span>
                    </li>
                    <li className="page-item">
                        <span className="page-link bg-dark text-white">{page}</span>
                    </li>
                    <li className={`${data.next ? "page-item " : "page-item d-none"}`}>
                        <button className="page-link"
                            onClick={() => data.next ? setPage(page + 1) : ''}>⟩⟩</button>
                    </li>
                </ul>
            </nav>
        </div>

    )
}

export default Pagination
