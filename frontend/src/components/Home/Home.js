import React, {useContext} from 'react'
import {UserContext} from '../Utilities/UserContext'

const Home = () => {
    let {user, setUser} = useContext(UserContext)
    return (
        <>
            <h1>Home</h1>
            {user ? 
            <>
            <div>{user.firstname}</div>
            <div>{user.lastname}</div>
            </>:<></>
            }
        </>
    )
}

export default Home
