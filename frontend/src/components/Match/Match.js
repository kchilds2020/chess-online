import React, {useEffect, useState, useContext} from 'react'
import axios from 'axios'
import styled from 'styled-components'
import Board from './Board'
import {UserContext} from '../Utilities/UserContext'

const Match = () => {
    const [match, setMatch] = useState("");
    let {user, setUser} = useContext(UserContext)
    const [pov, setPov] = useState('white')

    useEffect(() => {
        console.log("USER",user)
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        let matchID = urlParams.get("id")
        axios.get(`http://localhost:8000/api/get-match/${matchID}`)
        .then(res => {
            setMatch(res.data)
            user.username === match.white ? setPov('white') : setPov('black')
        })
        

    }, [user, match.white])

    return (
        <div>
            <Container> 
                {match ?
                <Board match ={match} pov={pov}/>:
                <div>no board</div>

                }
            </Container>
        </div>
    )
}

const Container = styled.div`
  width: 100%;
  max-width: 600px;
  margin: 50px auto;
`

export default Match
