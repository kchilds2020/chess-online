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
            <div>Games: {user.active_games.games.map(element => 
            <div key={element.id}>{element.white}(White) VS {element.black}(Black), turn: {element.turn === 'white' ? element.white : element.black}</div>)}</div>
            <button>Find Match</button>
            
        
            </>:<></>
            }
        </>
    )
}

export default Home
