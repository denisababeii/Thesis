import { useNavigate } from "react-router-dom";
import Combobox from "react-widgets/Combobox";
import "react-widgets/styles.css";
import "./style.css"
import React, { useState, useEffect } from "react";

function GradesForm() {
    let navigate = useNavigate();
    const routeChange = () => {
        let path = `/preference`;
        navigate(path);
    }
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        fetch('/compulsory').then(res => res.json()).then(data => {
          setCourses(data.courses);
        });
      }, []);

    const comboboxes = []
    const grades= []

    for (const [i, course] of courses.entries()) {
        comboboxes.push (
        <div className="two-col-item">
            <label>{course}</label>
            <Combobox
                data={["10", "9", "8", "7", "6", "5", "Not yet passed"]}/>
        </div>
        )
      }

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Tell us about yourself!</h1>
                    <p className="lead" style={{"padding-left":"0.5em"}}> 
                        First, we will need a bit of insight on your previous academic performance. <br></br>What were your grades for these subjects?
                    </p>
                    <div className="two-col-box">
                        {comboboxes}
                    </div>
                    <button className="btn-change" onClick={routeChange}>Next</button>
                </div>
            </div>
        </div>
    );
}

export default GradesForm;