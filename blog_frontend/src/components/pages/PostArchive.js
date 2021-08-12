import React from 'react'

export default function PostArchive() {
    return (
        <div>
            {/* <!-- Jumbotron --> */}
            <div id='intro' className='p-2 text-center bg-image'
                style={{ backgroundImage: 'url(img/jumbotron.jpg)', height: '35vh' }}>
                <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }} >
                    <div className='d-flex justify-content-center align-items-center h-100'>
                        <div className='text-white'>
                            <h1 className='mb-3 h1'>Archieve</h1>
                        </div>
                    </div>
                </div>
            </div>
            <section className='col-md-8 mb-4 mx-auto'>
                <h2 className="mb-5 pt-4 ps-4">
                    Monthly Post Archieve
                </h2>
                <hr />
                <ul>
                    <li>2021
                        <ul>
                            <li>
                                <a href="/posts/2021/6/">
                                    June (2)
                                </a>
                            </li>
                            <li>
                                <a href="/posts/2021/5/">
                                    May (1)
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
                {/* <p>
                        Previous Month: 2019 December <br />
                        Next Month: 2021 Mart
                    </p> */}
            </section>
        </div>
    )
}
