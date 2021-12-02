import React from 'react'

export default function Contact() {
    return (

        <div>
            <div id='intro' className='text-center mt-3'>
                    <h1 className='h1'>Contact</h1>
            </div>
            <section className="mx-auto">
                <form className="col-6 mx-auto mt-4" action="" method="post">
                    <div className="form-outine mb-4">
                        <input type="text" name="full_name" className="form-control" placeholder="Full Name"></input>
                    </div>
                    <div className="form-outine mb-4">
                        <input type="email" name="email" className="form-control" placeholder="Email"></input>
                    </div>
                    <div className="form-outine mb-4">
                        <textarea name="message" className="form-control" placeholder="Message" rows='7'></textarea>
                    </div>
                    <button type="submit" className="btn btn-dark mb-4 w-100">Send</button>
                </form>
            </section>
        </div>
    )
}
