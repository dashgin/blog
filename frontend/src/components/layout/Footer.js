export default function Footer() {

    return (
        <footer>
            <div className="container-xl">
                <div className="footer-inner">
                    <div className="row d-flex align-items-center gy-4">
                        <div className="col-md-4">
                            <span className="copyright">&copy; {new Date().getUTCFullYear()} TC Blogs</span>
                        </div>
                        <div className="col-md-4 text-center">
                            <ul className="social-icons list-unstyled list-inline mb-0">
                                <li className="list-inline-item">
                                    <a href="https://www.facebook.com/dashqin.khudiyev">
                                        <i className="fab fa-facebook-f"></i>
                                    </a>
                                </li>
                                <li className="list-inline-item">
                                    <a href="https://www.instagram.com/dasqinxudiyev">
                                        <i className="fab fa-instagram"></i>
                                    </a>
                                </li>
                                <li className="list-inline-item">
                                    <a href="https://github.com/dashgin">
                                        <i className="fab fa-github"></i>
                                    </a>
                                </li>
                                <li className="list-inline-item">
                                    <a href="https://www.twitter.com/_dashgin_/">
                                        <i className="fab fa-twitter"></i>
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div className="col-md-4">
                            {
                                // eslint-disable-next-line jsx-a11y/anchor-is-valid
                                <a href="#" id="return-to-top" className="float-md-end">
                                    <i className="icon-arrow-up"></i>
                                    Back to Top
                                </a>
                            }
                        </div>
                    </div>
                </div>
            </div>
        </footer>

    )
}
