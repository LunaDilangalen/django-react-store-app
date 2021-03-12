import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import ProductPage from "./ProductPage";
import CheckoutPage from "./CheckoutPage";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>This is the home page</p>
          </Route>
          <Route path="/products" component={ProductPage} />
          <Route path="/checkout" component={CheckoutPage} />
        </Switch>
      </Router>
    );
  }
}
    