import DarkMode from "../utils/DarkModeToggle";
import { Link } from "react-router-dom";
import Search from "../utils/Search";
import Categories from "../utils/Categories"

export default function Navbar() {

    return (

        <nav className="navbar navbar-expand-lg">
            <div className="container-xl">
                <Link to="/"
                    className="navbar-brand text-dark rounded py-1 px-2 bordered">

                    {/* <!-- <img src="images/logo.svg" alt=""> --> */}
                    Blog
                </Link>
                <span className="d-lg-none w-lg-25">
                    <Search />
                </span>
                <span className="d-lg-none">
                    <DarkMode />
                </span>
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
                            <Link to={'/contact'} className="nav-link">Contact</Link>
                        </li>
                        <li className="nav-item dropdown ">
                            <a href="!#" className="nav-link dropdown-toggle" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">Categories</a>
                            <Categories />
                        </li>

                    </ul>


                </div>
                <span className="d-none  d-lg-inline">
                    <Search />
                </span>
                <span className="d-none d-lg-inline">
                    <DarkMode />
                </span>
            </div>
        </nav >

    )
}
