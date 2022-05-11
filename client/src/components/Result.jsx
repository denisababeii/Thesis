import React, { useState, useEffect } from "react";
import { trackPromise } from 'react-promise-tracker'
import Footer from "./Footer";
import Loading from "./Loading";
import Navigation from "./Navigation";
import axios from "axios";

function Result(props) {
    const [result, setResult] = useState([]);

      useEffect(() => {
          trackPromise(
        axios({
          method: "GET",
          url:"/result",
          headers : {
            Authorization: 'Bearer ' + props.token
        }
        })
        .then((response) => {
          const res =response.data
          setResult(res.result)
        }).catch((error) => {
            if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        }));
      },[]);

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Hooray!</h1>
                    <p className="lead">
                        Here are our top 3 suggestions for you!
                    </p>
                        <Loading></Loading>
                        <ul className="ul-course-info">{result.map(course => <li className="li-result" key={course}> <p className="lead">{course}</p> </li>)}</ul>
                    <p className="lead">
                    We hope this will guide you in your decision. Thank you for using the Elective Course Recommender and wish you good luck in your final year!
                    Curious to find out more about these courses? Take a look at our <a href="/info" style={{color: "rgba(135,55,255,1)"}}>Courses</a> section for more!</p>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default Result;