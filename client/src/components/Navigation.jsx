import React from "react";
import { NavLink } from "react-router-dom";
import './style.css';
import axios from "axios";

function Navigation(props) {
    function logMeOut() {
        axios({
          method: "POST",
          url:"/logout",
        })
        .then((response) => {
           props.removeToken()
        }).catch((error) => {
          if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        })}
    return (
        <div className="navigation">
            <nav className="navbar navbar-expand navbar-dark bg-dark fixed-top">
                <div className="container">
                    <NavLink className="navbar-brand" to="/" >
                    <img src="icon.png" alt="Icon" width="85" height="85"></img>
                    </NavLink>
                    <div>
                        <ul className="navbar-nav ml-auto">
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/">
                                    Home
                                    <span className="sr-only">(current)</span>
                                </NavLink>
                                </li>
                                <li>
                                <NavLink className="nav-link" to="/info">
                                    Courses
                                    <span className="sr-only">(current)</span>
                                </NavLink>
                                </li>
                                <li>
                                <NavLink className="nav-link" to="/profile">
                                    Profile
                                    <span className="sr-only">(current)</span>
                                </NavLink>
                            </li>
                            <li>
                            <NavLink className="nav-link" to="/" onClick={logMeOut} style={{color:"rgba(76,106,255,1)"}}>
                                Log out
                                <span className="sr-only">(current)</span>
                            </NavLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Navigation;