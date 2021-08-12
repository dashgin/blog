export default function Footer() {
    return (
        <footer className="bg-light text-lg-start">
            <hr className="m-0" />
            <div className="text-center py-3 align-items-center">
                <p>Follow me on social media</p>
                {/* <!-- <a href="#" className="btn btn-primary m-1" role="button" rel="nofollow">
                    <i className="fab fa-facebook-f"></i>
                </a> --> */}
                <a href="https://twitter.com/_dashgin_" className="btn btn-info m-1" role="button"
                    target="_blank" rel="noopener noreferrer">
                    <i className="fab fa-twitter"></i>
                </a>
                <a href="https://github.com/dashgin" className="btn btn-dark m-1" role="button"
                    target="_blank" rel="noopener noreferrer">
                    <i className="fab fa-github"></i>
                </a>
            </div>
            {/* <!-- Copyright --> */}
            <div className="text-center p-3"
                style={{ backgroundColor: "rgba(0, 0, 0, 0.2)" }}>
                ©{new Date().getUTCFullYear()} Copyright: <a className="text-dark" href="/">Dashgin</a>
            </div>
        </footer>

    )
}
