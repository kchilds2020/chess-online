import React from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import TopNavigation from './components/navigation/TopNavigation'
import Landing from './components/landing/Landing'
import Login from './components/login/Login'




const App = () => {
 
  return (
    <Router>
    <div>
      <TopNavigation />

      {/* A <Switch> looks through its children <Route>s and
          renders the first one that matches the current URL. */}
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/">
          <Landing />
        </Route>
      </Switch>
    </div>
  </Router>
  )
}


export default App

