import { useState, useEffect } from "react";
import axios from 'axios'
import DarkMode from '../utils/DarkModeToggle'
import { Link, NavLink } from "react-router-dom"
import Search from "./Search";

export default function Navbar() {
    const [categories, setCategories] = useState([])

    const url = 'http://localhost:8000/api/v1/categories/';

    const getCategories = async () => {
        const res = await axios.get(url)
        setCategories(res.data);
    };
    console.log(categories)
    useEffect(() => {
        getCategories()
    }, [])

    return (
        <nav className='navbar navbar-expand-md navbar-light bg-light fixed-top py-1 px-5 shadow-none border-bottom'>
            <div className='container ps-5'>
                <NavLink to={'/'} className='navbar-brand py-0 active'>
                    {/* <img src={logo} height='30' alt='Technology blog' /> */}
                    <i className="fab fa-blogger-b text-dark fs-1 active"></i>
                </NavLink>
                <button className='navbar-toggler' type='button' data-mdb-toggle='collapse'
                    data-mdb-target='#navbarSupportedContent' aria-controls='navbarSupportedContent'
                    aria-expanded='false' aria-label='Toggle navigation'>
                    <i className='fas fa-bars'></i>
                </button>
                <div className='collapse navbar-collapse' id='navbarSupportedContent'>
                    <ul className='navbar-nav me-auto mb-2 mb-lg-0 text-center'>
                        <li className='nav-item'>
                            <NavLink activeClassName="active"
                                isActive={(match, location) => {
                                    if (location.pathname === match.url) {
                                        return true;
                                    }
                                }}
                                className='nav-link' aria-current='page' to={"/"}>Home</NavLink>
                        </li>
                        <li className='nav-item'>
                            <NavLink activeClassName="active" className='nav-link' to={'/posts'}>Post Archive</NavLink>
                        </li>
                        <li className='nav-item'>
                            <NavLink activeClassName="active" className='nav-link' to={'/contact'}>Contact</NavLink>
                        </li>
                        {/* Navbar dropdown */}
                        <li className='nav-item dropdown align-self-center'>
                            <a href="/#" className='nav-link dropdown-toggle' d='navbarDropdown' role='button'
                                data-mdb-toggle='dropdown' aria-expanded='false'>
                                Categories
                            </a>
                            {/* Dropdown menu */}
                            <ul className='dropdown-menu align-self-center' aria-labelledby='navbarDropdown'>
                                {
                                    categories.map(category =>
                                        <li><Link to={`/categories/${category.slug}`} className='dropdown-item'>{category.name}</Link></li>
                                    )}
                            </ul>
                        </li>
                    </ul>
                    <Search />
                    <DarkMode />
                </div>
            </div>
        </nav>

    )
}
