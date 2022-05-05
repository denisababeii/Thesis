import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import './style.css';
import Combobox from "react-widgets/Combobox";
import Loading from "./Loading";
import { trackPromise } from 'react-promise-tracker'
import './style.css';

function CourseInfo() {
    const [electives, setElectives] = useState([]);

    useEffect(() => {
      trackPromise(
        fetch('/electives_links').then(res => res.json()).then(data => {
          setElectives(data.courses);
        }));
      }, []);

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-4">Have a quick look at the available electives</h1>
                    <p className="lead">Click any elective to find out more about it!</p>
                    <Loading></Loading>
                    <ul className="ul-course-info">{electives.map(course => <li className="li-course-info" key={course}> <a className="button lead" href={course[1]} style={{color: "rgba(0,0,0,1)"}}>{course[0]}</a> </li>)}</ul>
                </div>
            </div>
        </div>
    );
}

export default CourseInfo;