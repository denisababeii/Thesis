import React, { useState, useEffect } from "react";
import Footer from "./Footer";
import Navigation from "./Navigation";
import axios from "axios";
import { trackPromise } from 'react-promise-tracker'
import Loading from "./Loading";

function UserProfile(props) {
    const [result, setResult] = useState([]);
    var content;

    useEffect(() => {
        trackPromise(
      axios({
        method: "GET",
        url:"/last_result",
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
                <h1 className="display-4">Hi, {props.username}!</h1>
                <p className="lead">
                   Here is your last recommendation!  
                </p>
                <Loading></Loading>
                <div>
                    {
                        result.length > 0
                        ? <ul className="ul-course-info">{result.map(course => <li className="li-result" key={course}> <p className="lead">{course}</p> </li>)}</ul>
                        : <p className="lead" style={{paddingRight:"5px", display:"inline-block"}}>Hmm, seems like you have no previous results. Get started <a className="lead" href="/home" style={{color:"rgba(96,106,255,1)"}}>here</a>!</p>
                    }
                </div>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default UserProfile;