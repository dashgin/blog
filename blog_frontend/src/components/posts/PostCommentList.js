import React from 'react'

export default function PostCommentList() {
    return (
        < section className="border-bottom mb-3" >
            <p className="text-center" id="comments"><strong>Comments: 3</strong></p>
            <div className="row mb-4">
                <div className="col-1">
                    <img src="img/avatar.jpg" className="img-fluid shadow-1-strong rounded" alt="" />
                </div>
                <div className="col-10">
                    <p className="mb-2"><strong>User</strong></p>
                    <small><a className="text-muted" href="mailto:{{ comment.email }}">
                        user@example.com
                    </a></small>

                    <div className="ps-2">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. A alias odit commodi ut
                        dicta saepe qui iusto nostrum doloribus sapiente.
                    </div>

                </div>
            </div>
            {/* <p className="text-muted">There is no comment yet ...</p> */}
        </section >

    )
}
