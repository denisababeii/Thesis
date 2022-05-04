import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Combobox from "react-widgets/Combobox";
import "react-widgets/styles.css";

function PreferencesForm() {
    let navigate = useNavigate(); 
    const routeChange = () => { 
        let path = `/result`; 
        navigate(path);
    }

    const [electives1, setElectives1] = useState([]);
    const [electives2, setElectives2] = useState([]);
    const [electives3, setElectives3] = useState([]);

    useEffect(() => {
        fetch('/electives1').then(res => res.json()).then(data => {
          setElectives1(data.courses);
        });
      }, []);

      useEffect(() => {
        fetch('/electives2').then(res => res.json()).then(data => {
          setElectives2(data.courses);
        });

      }, []);    useEffect(() => {
        fetch('/electives3').then(res => res.json()).then(data => {
          setElectives3(data.courses);
        });
      }, []);

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Just one more step</h1>
                    <p className="lead">
                        Your opinion matters!<br></br>Which of these courses sound interesting to you?
                    </p>
                    
                    <div className="one-col-box">
                        <div className="one-col-item">
                            <label>First Elective</label>
                            <Combobox
                                data={electives1}/>
                        </div>

                        <div className="one-col-item">
                            <label>Second Elective</label>
                            <Combobox
                                data={electives2}/>
                        </div>

                        <div className="one-col-item">
                            <label>Third Elective</label>
                            <Combobox
                                data={electives3}/>
                        </div>
                    </div>
                    <button className="btn-change" onClick={routeChange}>See your result!</button>
                </div>
            </div>
        </div>
    );
}

export default PreferencesForm;