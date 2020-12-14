import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'

const TopNavigation = ({user}) => {

    const logout = (e) => {
        e.preventDefault()
        localStorage.removeItem('token')
        localStorage.removeItem('user_id')
        window.location.href = '/'
    }

    return (
        <>
            <Navbar bg="#1976d2" expand="lg" variant="dark" style={{backgroundColor: '#1976d2', boxShadow: '0px 2px 6px #aaa', marginBottom: '20px'}}>
                <Navbar.Brand href="/">Chess Online</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        {user ? <Nav.Link onClick={logout}>Logout</Nav.Link> : <Nav.Link href="/login">Login</Nav.Link>}
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </>
    )
}

export default TopNavigation;
