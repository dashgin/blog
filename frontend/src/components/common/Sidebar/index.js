import React from 'react'
import Newsletter from './Newsletter';
import PopularPosts from './PopularPosts';
import RecentPosts from './RecentPosts';
import Tags from './Tags';

const Sidebar = () => {

    return (
        <div className="sidebar">
            <div className="post-tabs widget rounded">
                <ul className="nav-tabs nav-pills nav d-flex justify-content-evenly" id="postTab" role="tablist">
                    <li className="nav-item" role="presentation">
                        <button aria-controls="popular" aria-selected="true" className="nav-link active"
                            data-bs-target="#popular" data-bs-toggle="tab" id="popular-tab" role="tab"
                            type="button">Popular</button>
                    </li>
                    <li className="nav-item" role="presentation">
                        <button aria-controls="recent" aria-selected="false" className="nav-link"
                            data-bs-target="#recent" data-bs-toggle="tab" id="recent-tab" role="tab"
                            type="button">Recent</button>
                    </li>
                </ul>

                <div className="tab-content" id="postsTabContent">
                    <div className="lds-dual-ring"></div>
                    <PopularPosts />

                    <RecentPosts />
                </div>
            </div>

            <Tags />
            <Newsletter />
        </div>

    )
}

export default Sidebar
