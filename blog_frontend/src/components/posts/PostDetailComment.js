import React from 'react'

export default function PostDetailComment() {
    return (
        <section>
            <p className="text-center"><strong>Leave a reply</strong></p>
            <form method="POST" className='w-75 mx-auto'>
                <div className="form-outline mb-4">
                    <input type="text" name='name' className="form-control"></input>
                    <label className="form-label" for="name">Full Name</label>
                </div>
                <div className="form-outline mb-4">
                    <input type="email" name='email' className="form-control"></input>
                    <label className="form-label" for="email">Email</label>
                </div>
                <div className="form-outline mb-4">
                    <textarea name='content' className="form-control" rows="10"></textarea>
                    <label className="form-label" for="content">Comment</label>
                </div>
                <button type="submit" className="btn btn-dark btn-block mb-4">
                    Publish
                </button>
            </form>
        </section>
    )
}
