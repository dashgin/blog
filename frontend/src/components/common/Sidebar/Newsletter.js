import React from 'react';
import { useFormik } from 'formik';
import API from '../../../services/API';
const Newsletter = () => {


    const formik = useFormik({
        initialValues: {
            email: '',
        },
        onSubmit: values => {
            API.post('/newsletter/subscribe/', values)
                .then(res => {
                    console.log(res);
                    alert(res);
                })
                .catch(err => {
                    console.log(err);
                    alert('something went wrong');
                });
        },
    });
    return (


        <div className="widget rounded">
            <div className="widget-header text-center">
                <h3 className="widget-title">Newsletter</h3>
            </div>
            <div className="widget-content">
                <span className="newsletter-headline text-center mb-3">Join 50,000 subscribers</span>

                <form onSubmit={formik.handleSubmit}>
                    <div className="mb-2">
                        <input
                            id="email"
                            name="email"
                            type="email"
                            onChange={formik.handleChange}
                            value={formik.values.email}
                            className="form-control w-100 text-center"
                            placeholder="Email address..."
                        />
                    </div>

                    <button className="btn btn-default btn-full" type="submit">Sign Up</button>
                </form>

            </div>
        </div>
    )
}

export default Newsletter
