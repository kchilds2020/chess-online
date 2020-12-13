import React, {useState} from 'react'
import axios from 'axios'

const Login = () => {
    const [data, setData] = useState({
        username: '',
        password: ''
    })

    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('http://localhost:8000/api/login/',data)
        .then(res=>console.log(res))
    }

    return (
        <div>
            Login
            <form onSubmit={handleSubmit}>
                <input type="text" value = {data.username} onChange={e => setData({...data, username: e.target.value})}/>
                <input type="password" value = {data.password} onChange={e => setData({...data, password: e.target.value})}/>
                <button>Submit</button>
            </form>
            <a href="/create-account">
                Create Account
            </a>
        </div>
    )
}

export default Login
