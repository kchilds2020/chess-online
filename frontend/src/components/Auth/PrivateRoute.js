import React, {useEffect} from 'react'
import {Redirect, Route, useHistory} from 'react-router-dom'
import axios from 'axios'
import {UserContext} from '../Utilities/UserContext'


function PrivateRoute({children, path,user, setUser, menu, setMenu, ...rest}) {
    let history = useHistory()


    useEffect(() => {
        let mounted = true
        if(user === null && localStorage.getItem('token') && localStorage.getItem('user_id')){
            let user_id = localStorage.getItem('user_id')
            let token = localStorage.getItem('token')
            console.log('PRIVATE ROUTE ATTEMPT')
            axios.get(`http://localhost:8000/api/users/${user_id}`,{headers: {'Authorization': `token ${token}`}})
            .then(idRes => {
                    console.log('HELLOW')
                    console.log('PrivateRoute.js info',idRes)
                    if(!idRes.data.username){
                        console.log('Push')
                        localStorage.removeItem('user_id')
                        localStorage.removeItem('token')
                        history.push('/login')
                    }
                    if(mounted){
                        setUser(idRes.data)
                    }            
            })
        }

          return () => mounted = false
      },[history, setUser, user])


    return <UserContext.Provider value = {{user, setUser}}>
                <Route {...rest} render={({ location }) => localStorage.getItem('user_id') !== null ? 
                    (children) : 
                    ( <Redirect to={{ pathname: "/login", state: { from: location }}}/>)}/>
            </UserContext.Provider>

}


export default PrivateRoute