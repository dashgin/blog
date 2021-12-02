import React, { useState, useEffect } from 'react'
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
    }, [categories])


    return (
        <ul className="dropdown-menu rounded-3 rounded">
            {
                categories.map(category => (
                    <li key={category.slug}>
                        <a href="!#" className="dropdown-item">{category.name}</a>
                    </li>
                ))
            }
        </ul>
    )
}

export default Categories
