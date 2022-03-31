import React from "react";
import { useNavigate } from "react-router-dom";

function GradesForm() {
    let navigate = useNavigate(); 
    const routeChange = () => { 
        let path = `/preference`; 
        navigate(path);
    }
    
    return (
        <div className="about">
            <div className="container h-100 d-flex">
                <div className="jumbotron my-auto">
                    <h1 className="display-3">Tell us about yourself!</h1>
                    <p className="lead">
                        First, we will need a bit of insight on your previous academic performance. What were your grades for these subjects?
                    </p>
                    


                    <button className="btn-change" onClick={routeChange}>Next</button>
                </div>
            </div>
        </div>
    );
}

export default GradesForm;