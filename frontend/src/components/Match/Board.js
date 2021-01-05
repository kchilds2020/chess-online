import React, {useEffect} from 'react'
import styled from 'styled-components'
import Square from './Square'

const Board = ({match, pov}) => {

  useEffect(()=>{
    console.log("MATCH", match,"POV",pov)
  }, [match, pov])
  return (
        <BoardDiv> 
        {/* {match !== ''?
        
          (pov === 'black' ? 
            match.board.map(row => row.slice(0).reverse().map((col,index) => <Square key = {index} match = {match} position={col}/>) ) :
            match.board.slice(0).reverse().map((row => row.map((col,index) => <Square key = {index} match = {match} position={col}/>))))
         : <></>} */}
         Board
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
