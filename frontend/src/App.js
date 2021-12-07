import { BrowserRouter as Router, Switch, Route, } from "react-router-dom";

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/font-awesome/css/font-awesome.min.css';
import '../node_modules/simple-line-icons/dist/styles/simple-line-icons.css';
import '../node_modules/highlight.js/styles/atom-one-dark.css';
import './assets/style.css'

import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import PostList from './components/posts/PostList';
import PostDetail from './components/posts/PostDetail';
import PostArchive from './components/posts/PostArchive';
import Contact from './components/pages/Contact';
import Sidebar from "./components/layout/Sidebar/index";

function App() {
  console.log(process.env);
  return (
    <Router>
      <Header />
      <section className="main-content" style={{marginTop:'80px'}}>
        <div className="container-xl">
          <div className="row ">
            <div className="col-lg-9">
              <Switch>
                <Route path='/' exact component={PostList} />
                <Route path='/contact' exact component={Contact} />
                <Route path='/archive' exact component={PostArchive} />
                <Route path='/posts/:slug' component={PostDetail} />
                <Route path='/categories/:categorySlug' component={PostList} />
                <Route path='/tags/:tagSlug' component={PostList} />
              </Switch>
            </div>
            <div className="col-lg-3 sticky-top px-4">
              <Sidebar />
            </div>
          </div>
        </div>
      </section>
      <Footer />
    </Router>
  );
}
export default App;
