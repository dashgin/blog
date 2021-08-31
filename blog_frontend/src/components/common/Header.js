import Navbar from './Navbar'

export default function Header() {
    return (
        <header>
            <Navbar />
            <div id="intro" class="p-2 text-center bg-image "
                style="background-image: url({% static 'img/jumbotron.jpg' %}); height: 35vh;"
                >
            <div class="mask" style="background-color: rgba(0, 0, 0, 0.6)">
            <div class="d-flex justify-content-center align-items-center h-100">
                <div class="text-white">
                    <h1 class="mb-3 h1">Blog</h1>
                    <a class="btn btn-outline-light btn-lg m-2" href="#" role="button">Subscribe</a>
                </div>

            </div>
        </div>
    </div>
  
        </header>
    )
}
