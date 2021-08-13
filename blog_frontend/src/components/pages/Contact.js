import React from 'react'

export default function Contact() {
    return (

        <div>
            {/* <!-- Jumbotron --> */}
            <div id='intro' className='p-2 text-center bg-image'
                style={{ backgroundImage: 'url(img/jumbotron.jpg)', height: '35vh' }}>
                <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }} >
                    <div className='d-flex justify-content-center align-items-center h-100'>
                        <div className='text-white'>
                            <h1 className='mb-3 h1'>Contact</h1>
                        </div>
                    </div>
                </div>
            </div>
            <section className="col-md-8 mb-4 mx-auto">
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
                    <button type="submit" className="btn btn-dark btn-block mb-4">Send</button>
                </form>
            </section>
        </div>
    )
}
