import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import { Search as SearchTag } from 'semantic-ui-react'
import 'semantic-ui-css/semantic.min.css';
import axios from 'axios';

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

    resultRenderer = ({ title, subtitle, slug }) => {
        return (
            <div key={slug}>
                <Link onClick={this.handleClick} to={`/posts/${slug}`}>{title} - {subtitle}</Link>
            </div>
        )
    }

    handleChange(event) {
        this.setState({ loading: true })
        this.setState({ value: event.target.value })
        setTimeout(() => {
            const url = `http://localhost:8000/api/v1/posts/?search=${this.state.value}`
            console.log(url)
            axios.get(url)
                .then(response => this.setState({ results: response.data.results })).catch(error => console.log(error))

            this.setState({ loading: false })
            event.preventDefault();
        }, 200
        )
    }


    render() {
        return (
            <SearchTag
                loading={this.state.loading}
                resultRenderer={this.resultRenderer}
                onSearchChange={this.handleChange}
                type='search'
                value={this.state.value}
                placeholder='Search'
                results={this.state.results}
            />
        )
    }
}

export default Search