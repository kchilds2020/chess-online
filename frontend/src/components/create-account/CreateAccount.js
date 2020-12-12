import React, {useState} from 'react'
import axios from 'axios'

const CreateAccount = () => {
    const [data, setData] = useState({
        username: '',
        firstname: '',
        lastname: '',
        email: ''
    })


    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('http://localhost:8000/api/create-account/',data)
        .then(res => console.log(res))
        
    }

    return (
        <div>
            Login
            <form onSubmit={handleSubmit}>
                <input type="text" value = {data.username} onChange={e => setData({...data, username: e.target.value})}/>
                <input type="text" value = {data.firstname} onChange={e => setData({...data, firstname: e.target.value})}/>

                <input type="text" value = {data.lastname} onChange={e => setData({...data, lastname: e.target.value})}/>

                <input type="email" value = {data.emailemail} onChange={e => setData({...data, email: e.target.value})}/>
                <button>Submit</button>
            </form>
        </div>
    )
}

export default CreateAccount