import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Combobox from "react-widgets/Combobox";
import "react-widgets/styles.css";
import Footer from "./Footer";
import Navigation from "./Navigation";
import axios from "axios";
import { trackPromise } from "react-promise-tracker";
import {Modal, Button} from "react-bootstrap"

function PreferencesForm(props) {
    let navigate = useNavigate(); 
    const [electives1, setElectives1] = useState([]);
    const [electives2, setElectives2] = useState([]);
    const [electives3, setElectives3] = useState([]);
    const [choice, setChoice] = useState([]);
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const routeChange = () => {
      var count = 0
      for (let item of choice)
          if (item)
            count++
      if(count !== 3)
          setShow(true)
      else {
        axios({
          method: "POST",
          url:"/preference",
          headers : {
              'content-type':'application/json',
              Authorization: 'Bearer ' + props.token
        },
        data:{
          preference: JSON.stringify(choice)
        }
        }).then(function(response){ 
          console.log("OK");   
        }).then(() => {
          let path = `/result`;
          navigate(path);
        }).catch((error) => {
          if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
    })}
    }

    useEffect(() => {
      console.log(props)
      axios({
        method: "GET",
        url:"/electives1",
        headers : {
            Authorization: 'Bearer ' + props.token
      }
      })
      .then((response) => {
        const res =response.data
        setElectives1(res.courses)
      }).catch((error) => {
        if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    });
    },[]);

    useEffect(() => {
      axios({
        method: "GET",
        url:"/electives2",
        headers : {
            Authorization: 'Bearer ' + props.token
      }
      })
      .then((response) => {
        const res =response.data
        setElectives2(res.courses)
      }).catch((error) => {
        if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    });
    },[]);  
      
    useEffect(() => {
        axios({
        method: "GET",
        url:"/electives3",
        headers : {
            Authorization: 'Bearer ' + props.token
      }
      })
      .then((response) => {
        const res =response.data
        setElectives3(res.courses)
      }).catch((error) => {
        if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    });
    },[]);  

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
                                data={electives1}
                                onChange={value => {
                                  let newArr = [...choice]
                                  newArr[0] = value;
                                  setChoice(newArr);
                              }}/>
                        </div>

                        <div className="one-col-item">
                            <label>Second Elective</label>
                            <Combobox
                                data={electives2}
                                onChange={value => {
                                  let newArr = [...choice]
                                  newArr[1] = value;
                                  setChoice(newArr);
                              }}/>
                        </div>

                        <div className="one-col-item">
                            <label>Third Elective</label>
                            <Combobox
                                data={electives3}
                                onChange={value => {
                                  let newArr = [...choice]
                                  newArr[2] = value;
                                  setChoice(newArr);
                              }}/>
                        </div>
                    </div>
                    <div>
                    <Modal show={show} onHide={handleClose}>
                        <Modal.Header>
                        <Modal.Title>Oops!</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>You must fill in all the electives before moving on to the next step!</Modal.Body>
                        <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose}>
                            Close
                        </Button>
                        </Modal.Footer>
                    </Modal>
                    </div>
                    <button className="btn-change" onClick={routeChange}>See your result!</button>
                </div>
            </div>
          <Footer/>
        </div>
    );
}

export default PreferencesForm;