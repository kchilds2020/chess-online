import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'
import axios from 'axios'

const Login = () => {
    const [data, setData] = useState({
        username: '',
        password: ''
    })
    let history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('http://localhost:8000/api/login/', data)
        .then(res=>{
            if(res.status === 200){
                
                localStorage.setItem('token',res.data.token)
                localStorage.setItem('user_id',res.data.id)
                history.push('/home')
            }else{
                alert(res.data)
                setData({username:'', password:''})
            }
        })
        .catch(err => console.log(err))
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
