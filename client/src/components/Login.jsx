import "react-widgets/styles.css";
import "./style.css"
import React from "react";
import Navigation from "./Navigation";
import Footer from "./Footer";
import axios from "axios";
import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { Form, InputGroup, Col, Row } from "react-bootstrap";

function Login(props) {
    let navigate = useNavigate(); 
    const [loginForm, setloginForm] = useState({
        username: "",
        password: ""
      })

    const [validated, setValidated] = useState(false);

    function logMeIn(event) {
    setValidated(false)
    axios({
        method: "POST",
        url:"/login",
        data:{
        username: loginForm.username,
        password: loginForm.password
        }
    })
    .then((response) => {
        props.setToken(response.data.access_token)
        props.setUsername(loginForm.username)
    }
    ).then(()=>{
        let path = `/`;
        navigate(path);
    }
    ).catch((error) => {
        if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        setValidated(true)
        }
        
    })

    setloginForm(({
        username: "",
        password: ""}))

      event.preventDefault()
    }

    function handleChange(event) { 
        const {value, name} = event.target
        setloginForm(prevNote => ({
            ...prevNote, [name]: value})
        )}

    return (
        <div>
            <div className="navigation">
            <nav className="navbar navbar-expand navbar-dark bg-dark fixed-top">
                <div className="container">
                    <img src="icon.png" alt="Icon" width="85" height="85"></img>
                    </div>
            </nav>
            </div>
            <div className="container h-100 d-flex">
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-4" style={{paddingLeft:"6px"}}>Welcome back!</h1>
                    <Form noValidate validated={validated} onSubmit={logMeIn} style={{padding:"10px"}}>
                    <Row className="mb-3">
                        <Form.Group as={Col} md="12" controlId="validationCustomUsername">
                        <Form.Label>Username</Form.Label>
                        <InputGroup hasValidation>
                            <InputGroup.Text id="inputGroupPrepend">@</InputGroup.Text>
                            <Form.Control
                            type="text"
                            aria-describedby="inputGroupPrepend"
                            name="username"
                            onChange={handleChange} 
                            text={loginForm.username} 
                            value={loginForm.username}
                            required
                            />
                            <Form.Control.Feedback type="invalid">
                            Wrong username.
                            </Form.Control.Feedback>
                        </InputGroup>
                        </Form.Group>
                    </Row>
                    <Row className="mb-3">
                        <Form.Group controlId="validationCustomUsername" as={Col} md="12">
                        <Form.Label>Password</Form.Label>
                        <InputGroup hasValidation>
                            <Form.Control
                            type="password"
                            aria-describedby="inputGroupPrepend"
                            name="password"
                            required
                            onChange={handleChange} 
                            text={loginForm.password} 
                            value={loginForm.password}
                            />
                            <Form.Control.Feedback type="invalid">
                            Wrong password.
                            </Form.Control.Feedback>
                        </InputGroup>
                        </Form.Group>
                    </Row>
                   <div style={{display:"flex"}}><p style={{paddingRight:"5px"}}>New here?</p><a href="/account" style={{color:"rgba(96,106,255,1)"}}>Sign up</a></div> 
                    <div style={{display:"flex", alignItems:"center", justifyContent:"center"}}>
                        <button class="btn-change" type="submit" style={{width:"100px"}}>Log in</button>
                    </div>
                    </Form>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default Login;