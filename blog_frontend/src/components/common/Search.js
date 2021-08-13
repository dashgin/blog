import React from 'react'

export default function Search() {
    return (
        <form className='input-group w-auto' method='get' action=''>
            <input type='search' name='q' className='form-control rounded' placeholder='Search'
                aria-label='Search' aria-describedby='search-addon' />
        </form>
    )
}
