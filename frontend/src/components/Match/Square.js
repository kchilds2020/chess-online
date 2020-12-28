import React, {useContext} from 'react'
import styled from 'styled-components' 
import {UserContext} from '../Utilities/UserContext'

function Square({ position, match}) {
    
    const {user, setUser} = useContext(UserContext)
    
    const drag = (ev) => {
      ev.dataTransfer.setData("text", ev.target.id);
    }
    
    const allowDrop = (ev) => ev.preventDefault();
      
    const drop = (ev) => {
        ev.preventDefault();
        //get piece ID and new Square ID and update position array
        let piece = document.getElementById(ev.dataTransfer.getData("text"));
        let destinationSquare = document.getElementById(ev.target.id);

        /* let currentObj = findObjectAtLocation(piece.id.slice(-2), state.position);
        let desiredObj = findObjectAtLocation(destinationSquare.id.slice(-2), state.position);

        if(checkValidation(currentObj, desiredObj, state, setState) === true){
            updateBoard( currentObj, desiredObj, state, setState);
        } */
    };

    const movePiece = (e) => {
        e.preventDefault();
        /* let pClickedObj;
        let desId = e.target.id.length <= 2 ? e.target.id : e.target.parentElement.id;
        let desObj = findObjectAtLocation(desId, state.position);
        //find object of active piece
        if(state.pieceClicked !== ''){
            console.log('THERE IS AN ACTIVE PIECE')
            pClickedObj = findObjectAtLocation(state.pieceClicked, state.position)
            console.log(pClickedObj)
            //if another piece of same color is clicked -> update square colors and pieceClickded
            //else -> if another piece of not the same color or an empty square
            if(state.turn === desObj.piece.slice(0,5)){
                console.log('another piece of same color is clicked')
                setState({...state, pieceClicked: desId});
            }else{
                console.log('opposite color piece is clicked or empty square')
                if(checkValidation(pClickedObj, desObj, state, setState) === true){
                    updateBoard( pClickedObj, desObj, state, setState);
                }else{
                    setState({...state, pieceClicked: ''});
                }
            }
        //else -> if there isnt a piece clicked yet, verify its the correct turn before assigning
        }else{
            console.log('NO PIECE ACTIVE', desObj.piece.slice(0,5), desId)
            if(state.turn === desObj.piece.slice(0,5)){
                console.log('TURN = PIECE CLICKED', desId)
                setState({...state, pieceClicked: desId});
            }
        } */
    }

    return (
        <SquareDiv style={{backgroundColor: `${position.squareColor}`}} id={`${position.file}${position.rank}`} className = 'square' onDrop={drop} onDragOver={allowDrop} onClick = {movePiece}>
                {/* {state.pieceClicked} */}
                {position.piece !== '' ? 
                    match.turn === position.piece.slice(0,5) ? 
                        <Img id={`${position.piece}>${position.file}${position.rank}`} src = {require(`../images/${position.piece}.png`)} alt={`${position.piece}`} draggable="true" onDragStart={drag} /> :
                        <Img id={`${position.piece}>${position.file}${position.rank}`} src = {require(`../images/${position.piece}.png`)} alt={`${position.piece}`} draggable="false"/>
                        : <></>}
        </SquareDiv>
    )
}

const SquareDiv = styled.div`
    position: relative;
    background-color: blue;
    padding-top: 100%;
`
const Img = styled.img`
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
`
//dfsdf

export default Square
