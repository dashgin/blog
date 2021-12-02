import { BrowserRouter as Router, Switch, Route, } from "react-router-dom";

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/font-awesome/css/font-awesome.min.css';
import '../node_modules/simple-line-icons/dist/styles/simple-line-icons.css';
import './assets/style.css'

import Header from './components/common/Header';
import Footer from './components/common/Footer';
import PostList from './components/posts/PostList';
import PostDetail from './components/posts/PostDetail';
import PostArchive from './components/posts/PostArchive';
import Contact from './components/pages/Contact';
import CategoryDetail from './components/pages/CategoryDetail';
import Sidebar from "./components/common/Sidebar/index";

function App() {
  return (
    <Router>
      <Header />
      <section className="main-content">
        <div className="container-xl"><div className="row gy-4">
          <div className="col-lg-8">
            <Switch>
              <Route path='/' exact component={PostList} />
              <Route path='/contact' exact component={Contact} />
              <Route path='/archive' exact component={PostArchive} />
              <Route path='/posts/:slug' component={PostDetail} />
              <Route path='/categories/:slug' component={CategoryDetail} />
            </Switch>
          </div>
          <div className="col-lg-4">
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
