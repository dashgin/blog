import React from 'react'
import {DiscussionEmbed} from "disqus-react"


const DisqusDiv = (postSlug = 'java-1', title = "Java 1") => {
    const disqusConfig = {
        url: "http://localhost:3000/posts/java-1/",
        identifier: postSlug,
        title: title
    }

    return (
        <div className="article-container">

            <DiscussionEmbed
                shortname='tech-blog-glb2zkmtfa'
                config={disqusConfig}
            />
        </div>
    )
}

export default DisqusDiv
