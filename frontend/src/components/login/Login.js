import React, {useState} from 'react'
import axios from 'axios'

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    const handleSubmit = (e) => {
        e.preventDefault()
        
    }

    return (
        <div>
            Login
            <form onSubmit={handleSubmit}>
                <input type="text" value = {username} onChange={e => setUsername(e.target.value)}/>
                <input type="password" value = {password} onChange={e => setPassword(e.target.value)}/>
                <button>Submit</button>
            </form>
            <a href="/create-account">
                Create Account
            </a>
        </div>
    )
}

export default Login
