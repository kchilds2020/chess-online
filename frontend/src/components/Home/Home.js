import React, {useContext} from 'react'
import {UserContext} from '../Utilities/UserContext'

const Home = () => {
    let {user, setUser} = useContext(UserContext)
    return (
        <>
            
            {user ? 
            <>
            <h1>Welcome {user.firstname}</h1>
            <div>Games Played: {user.total_games}</div>
            <div>Wins: {user.wins}</div>
            <div>Draws: {user.total_games - (user.wins + user.losses)}</div>
            <div>Losses: {user.losses}</div>
            <button>Find Match</button>
            
        
            </>:<></>
            }
        </>
    )
}

export default Home
