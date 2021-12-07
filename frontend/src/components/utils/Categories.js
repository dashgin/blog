import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import API from '../../services/API'

const Categories = () => {

    const url = '/posts/categories'

    const [categories, setCategories] = useState([])


    const getCategories = async () => {
        const res = await API.get(url)
        setCategories(res.data)
    }

    useEffect(() => {
        getCategories()
    }, [])


    return (
        <ul className="dropdown-menu rounded-3 rounded">
            {
                categories.map(category => (
                    <li key={category.slug}>
                        <Link to={`/categories/${category.slug}`} className="dropdown-item">{category.name}</Link>
                    </li>
                ))
            }
        </ul>
    )
}

export default Categories
