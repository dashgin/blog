import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import { Search as SearchTag } from 'semantic-ui-react'
import '../../assets/semantic-custom/semantic-search.css';
import API from '../../services/API';

class Search extends Component {

    constructor(props) {
        super(props)
        this.state = { value: '', results: [], loading: false }
        this.handleChange = this.handleChange.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(event) {
        this.setState({ value: '' })
    }

    resultRenderer = ({ title, image, slug }) => {
        return (
            <div key={slug}>
                <Link onClick={this.handleClick} to={`/posts/${slug}`}>
                    <div className="inner">
                        <img src={image} width="40" style={{ borderRadius: "50%", marginRight: "10px" }} alt="" /> {title}
                    </div>
                </Link>
            </div>
        )
    }

    handleChange(event) {
        this.setState({ loading: true })
        this.setState({ value: event.target.value })
        setTimeout(() => {
            const url = `/posts/?search=${this.state.value}`
            console.log(url)
            API.get(url)
                .then(response => this.setState({ results: response.data.result }))
                .catch(error => console.log(error))

            this.setState({ loading: false })
            event.preventDefault();
        }, 200
        )
    }

    render() {
        return (
            // <div className="search-popup">
            //     <button className="btn-close" aria-label="Close" type="button"></button>
            //     <div className="search-content">
            //         <div className="text-center">
            //             <h3 className="mb-4 mt-0">Press ESC to close</h3>
            //         </div>

            <SearchTag
                loading={this.state.loading}
                resultRenderer={this.resultRenderer}
                onSearchChange={this.handleChange}
                type='search'
                value={this.state.value}
                placeholder='Search'
                results={this.state.results}
                size={'small'}
                fluid={true}
                noResultsMessage={'No posts found.'}
                selectFirstResult={true}
            />
            //     </div>
            // </div>
        )
    }
}

export default Search
