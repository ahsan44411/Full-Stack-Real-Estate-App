import React from 'react'
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";

import Home from './containers/Home'
import Listings from './containers/Listings'
import About from './containers/About'
import Contact from './containers/Contact'
import ListingDetail from './containers/ListingDetail'
import Login from './containers/Login'
import Signup from './containers/SignUp'
import NotFound from "./components/NotFound";

import Layout from './hocs/Layout'

import './sass/main.scss';
import {Provider} from 'react-redux';
import store from "./store";

const App = () => (

    <Provider store={store}>
        <Router>
            <Layout>
                <Switch>
                    <Route exact path='/' component={Home}/>
                    <Route exact path='/about' component={About}/>
                    <Route exact path='/contact' component={Contact}/>
                    <Route exact path='/listings' component={Listings}/>
                    <Route exact path='/listing/:id' component={ListingDetail}/>
                    <Route exact path='/login' component={Login}/>
                    <Route exact path='/signup' component={Signup}/>
                    <Route component={NotFound}/>
                </Switch>
            </Layout>
        </Router>
    </Provider>
);


export default App;
