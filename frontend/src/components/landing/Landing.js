import React from 'react'
import Button from 'react-bootstrap/Button'
import styled from 'styled-components'

const Landing = () => {
    return (
        <div>
            <Title>Online Chess!</Title>
            <Container>
                <Button style ={{width: '300px'}} onClick={() => window.location.href='/login'}>Login</Button>
                <Button style ={{width: '300px'}}>Play Both Sides</Button>
            </Container>
        </div>
    )
}

const Title = styled.h2`
    width: 95%;
    max-width: 600px;
    margin: auto;
    text-align: center;
`

const Container = styled.div`
    width: 95%;
    max-width: 600px;
    margin: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly; 
    height: 200px;
`

export default Landing
