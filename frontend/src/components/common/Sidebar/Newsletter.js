import React from 'react'

const Newsletter = () => {
    return (
        <div className="widget rounded">
            <div className="widget-header text-center">
                <h3 className="widget-title">Newsletter</h3>
            </div>
            <div className="widget-content">
                <span className="newsletter-headline text-center mb-3">Join 50,000 subscribers</span>
                <form action="#">
                    <div className="mb-2">
                        <input type="email" className="form-control w-100 text-center"
                            placeholder="Email address..." />
                    </div>
                    <button className="btn btn-default btn-full">Sign Up</button>

                </form>
            </div>
        </div>
    )
}

export default Newsletter
