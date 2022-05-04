import React, { useState, useEffect } from "react";
import { trackPromise } from 'react-promise-tracker'
import Loading from "./Loading";

function Result() {
    const [result, setResult] = useState([]);
    
    useEffect(() => {
        trackPromise(
        fetch('/result').then(res => res.json()).then(data => {
          setResult(data.result);
        }));
      }, []);

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Hooray!</h1>
                    <p className="lead">
                        Here are our top 3 suggestions for you!
                    </p>
                        <Loading></Loading>
                        <ul>{result.map(course => <li key={course}> <p className="lead">{course}</p> </li>)}</ul>
                    <p className="lead">
                    We hope this will guide you in your decision. Thank you for using the Elective Course Recommender and wish you good luck in your final year!
                    Curious to find out more about these courses? Take a look at our <a href="/info" style={{color: "rgba(135,55,255,1)"}}>Courses</a> section for more!</p>
                </div>
            </div>
        </div>
    );
}

export default Result;