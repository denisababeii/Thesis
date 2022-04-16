import React from "react";
import { useNavigate } from "react-router-dom";
import Combobox from "react-widgets/Combobox";
import "react-widgets/styles.css";

function PreferencesForm() {
    let navigate = useNavigate(); 
    const routeChange = () => { 
        let path = `/result`; 
        navigate(path);
    }

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Just one more step!</h1>
                    <p className="lead">
                        Your opinion matters!<br></br>Which of these courses sound interesting to you?
                    </p>
                    <div className="one-col-box">
                        <div className="one-col-item">
                            <label>First Elective</label>
                            <Combobox
                                data={[]}/> //GET IT FROM SERVER!!!!!
                        </div>

                        <div className="one-col-item">
                            <label>Second Elective</label>
                            <Combobox
                                data={[]}/> //GET IT FROM SERVER!!!!!
                        </div>

                        <div className="one-col-item">
                            <label>Third Elective</label>
                            <Combobox
                                data={[]}/> //GET IT FROM SERVER!!!!!
                        </div>
                    </div>
                    <button className="btn-change" onClick={routeChange}>See your result!</button>
                </div>
            </div>
        </div>
    );
}

export default PreferencesForm;