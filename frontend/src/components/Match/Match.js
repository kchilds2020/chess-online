import React, {useEffect, useState} from 'react'

const Match = () => {
    const [id, setID] = useState("");

    useEffect(() => {
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        let matchID = urlParams.get("id")
        setID(matchID)
        console.log("MATCH",matchID)

    }, [])

    return (
        <div>
            MATCH: {id}
        </div>
    )
}

export default Match
