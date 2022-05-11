import { useNavigate } from "react-router-dom";
import "react-widgets/styles.css";
import "./style.css"
import React, { useState, useEffect } from "react";
import Loading from "./Loading";
import { trackPromise } from 'react-promise-tracker'
import Combobox from "react-widgets/Combobox";
import Navigation from "./Navigation";
import Footer from "./Footer";
import axios from "axios";

function GradesForm(props) {
    let navigate = useNavigate();
    const [courses, setCourses] = useState([]);
    const comboboxes = []
    const [choice, setChoice] = useState([]);

    const routeChange = ()=> {
        var grades = []
        for(var c of choice) {
            if (c === "Not yet passed")
                grades.push(0)
            else
                grades.push(parseInt(c))
        }
        console.log(grades)
        axios({
            method: "POST",
            url:"/grades",
            headers : {
                'content-type':'application/json',
                Authorization: 'Bearer ' + props.token
          },
          data:{
              grades: JSON.stringify(grades)
          }
        }).then(function(response){ 
            console.log("OK");   
           }).then(() => {
            let path = `/preference`;
            navigate(path);
           }).catch((error) => {
            if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        })
    }

    useEffect(() => {
        trackPromise(
            axios({
                method: "GET",
                url:"/compulsory",
                headers: {
                  Authorization: 'Bearer ' + props.token
                }
              })
              .then((response) => {
                const res =response.data
                setCourses(res.courses)
              }
              ).catch((error) => {
            if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        }));
            },[]);

    for (const [i, course] of courses.entries()) {
        comboboxes.push (
        <div className="two-col-item">
            <label>{course}</label>
            <Combobox
            value={choice[i]}
            data={["10", "9", "8", "7", "6", "5", "Not yet passed"]}
            onChange={value => {
                let newArr = [...choice]
                newArr[i] = value;
                setChoice(newArr);
            }}
        />
        </div>
        )
      }

    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"150px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Tell us about yourself</h1>
                    <p className="lead" style={{"padding-left":"0.5em"}}> 
                        First, we will need a bit of insight on your previous academic performance. <br></br>What were your grades for these subjects?
                    </p>
                    <Loading></Loading>
                    <div className="two-col-box">
                        {comboboxes}
                    </div>
                    <button className="btn-change" onClick={routeChange}>Next</button>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default GradesForm;