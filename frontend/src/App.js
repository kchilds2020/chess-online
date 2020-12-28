import React, {useState, useEffect} from 'react'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import TopNavigation from './components/navigation/TopNavigation'
import Landing from './components/landing/Landing'
import Login from './components/login/Login'
import CreateAccount from './components/create-account/CreateAccount'
import Home from './components/Home/Home'
import Match from './components/Match/Match'
import PrivateRoute from './components/Auth/PrivateRoute'
import axios from 'axios'




const App = () => {
 
  const [user, setUser] = useState(null);

  useEffect(() => {
    console.log(localStorage.getItem('token'), localStorage.getItem('user_id'))
    if(localStorage.getItem('token')){
        let token = localStorage.getItem('token')
        let user_id = localStorage.getItem('user_id')
        axios.get(`http://localhost:8000/api/users/${user_id}`,{headers: {'Authorization': `token ${token}`}})
            .then(res => {
              console.log(res.data)
              setUser(res.data)
            })
    }
}, [])

  return (
    <Router>
    <div>
      <TopNavigation user = {user}/>

      {/* A <Switch> looks through its children <Route>s and
          renders the first one that matches the current URL. */}
      <Switch>
        <PrivateRoute path="/home" user={user} setUser={setUser}>     
          <Route exact strict component={Home}/>
        </PrivateRoute>
        <PrivateRoute path="/match" user={user} setUser={setUser}>     
          <Route exact strict component={Match}/>
        </PrivateRoute>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/create-account">
          <CreateAccount />
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

