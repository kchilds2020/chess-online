import React from 'react'
import styled from 'styled-components'

const Board = ({match, pov}) => {
    return (
        <BoardDiv> 
        {
          pov === 'black' ? 
            state.position.map(row => row.slice(0).reverse().map((col,index) => <Square key = {index} position={col} updateBoard={updateBoard}/>) ) :
            state.position.slice(0).reverse().map((row => row.map((col,index) => <Square key = {index} position={col} updateBoard={updateBoard}/>)))
        }
        </BoardDiv>
    )
}

const BoardDiv = styled.div`
  display: grid;
  grid-template-columns: auto auto auto auto auto auto auto auto;
  margin: 0px;
  width: 100%;
  background-color: black;
`

export default Board
