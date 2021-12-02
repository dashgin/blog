import DarkMode from "../utils/DarkModeToggle";
import { Link } from "react-router-dom";
import Search from "../utils/Search";

export default function Navbar() {

    return (

        <nav className="navbar navbar-expand-lg">
            <div className="container-xl">
                <a href="index.html" className="navbar-brand text-dark rounded px-2 bordered">

                    {/* <!-- <img src="images/logo.svg" alt=""> --> */}
                    Blog
                </a>
                <button className="search icon-button px-3 d-lg-none ms-auto me-2">
                    <i className="icon-magnifier"></i>
                </button>
                <button className="navbar-toggler burger-menu icon-button" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span className="burger-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto">
                        <li className="nav-item">
                                <Link to='/archive' className="nav-link">Post Archive</Link>

                        </li>
                        <li className="nav-item">
                            <a href="!#" className="nav-link">About</a>
                        </li>
                        <li className="nav-item">
                            <a href="!#" className="nav-link">Contact</a>
                        </li>
                        <li className="nav-item dropdown ">
                            <a href="!#" className="nav-link dropdown-toggle" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">Categories</a>
                            <ul className="dropdown-menu rounded-3 rounded">
                                <li>
                                    <a href="!#" className="dropdown-item">Fashion</a>
                                </li>
                                <li>
                                    <a href="!#" className="dropdown-item">Movies</a>
                                </li>
                                <li>
                                    <a href="!#" className="dropdown-item">Electronic</a>
                                </li>
                                <li>
                                    <a href="!#" className="dropdown-item">Cricket</a>
                                </li>
                                <li>
                                    <a href="!#" className="dropdown-item">Technology</a>
                                </li>

                            </ul>
                        </li>

                    </ul>


                </div>
                <Search/>
                {/* <button className="search icon-button px-3 d-none d-lg-inline-flex">
                    <i className="icon-magnifier"></i>
                </button> */}
                {/* <button className="icon-button px-3 d-none d-lg-inline-flex ms-2">
                    <i className="fas fa-moon"></i>
                    <i className="fas fa-sun"></i>
                </button> */}
                <DarkMode />
            </div>
        </nav >

    )
}
