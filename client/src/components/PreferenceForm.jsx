import React from "react";
import { useNavigate } from "react-router-dom";

function PreferencesForm() {
    let navigate = useNavigate(); 
    const routeChange = () => { 
        let path = `/result`; 
        navigate(path);
    }
    return (
        <div className="about">
            <div className="container h-100 d-flex">
                <div className="jumbotron my-auto">
                    <h1 className="display-3">Just one more step!</h1>
                    <p className="lead">
                        Your opinion matters! Tell us which courses sound interesting to you?
                    </p>
                    <button className="btn-change" onClick={routeChange}>See your result!</button>
                </div>
            </div>
        </div>
    );
}

export default PreferencesForm;