import { BrowserRouter as Router, Switch, Route, } from "react-router-dom";
import Header from './components/common/Header';
import Footer from './components/common/Footer';
import PostList from './components/posts/PostList';
import PostDetail from './components/posts/PostDetail';
import PostArchive from './components/pages/PostArchive';
import Contact from './components/pages/Contact';
import CategoryDetail from './components/pages/CategoryDetail';

function App() {
  return (
    <Router>
      <div>
        <Header />
          <main className="mt-4 mb-5 mx-auto" style={{minHeight:'100vh'}}>
            <Switch>
              <Route path='/' exact component={PostList} />
              <Route path='/contact' exact component={Contact} />
              <Route path='/posts' exact component={PostArchive} />
              <Route path='/posts/:slug' component={PostDetail} />
              <Route path='/categories/:slug' component={CategoryDetail} />
            </Switch>
            {/* <Sidebar /> */}
          </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
