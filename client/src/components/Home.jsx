import React from "react";
import './style.css';
import { useNavigate } from "react-router-dom";
import Footer from "./Footer";

function Home(props) {
    let navigate = useNavigate(); 
    const routeChange = () =>{
      let path = `/grades`; 
      navigate(path);
    }
    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">About</h1>
                    <p className="lead">
                        The Elective Course Recommender is a tool designed to aid students in making the best out of their last year of studies. Sometimes finding your perfect match regarding elective courses might be confusing and time-consuming. This is where this tool comes in handy! The algorithm takes into consideration your prior performance and personal preference in order to provide you with a personalized recommendation of elective courses, so you have a helping hand in your quest for success!
                    </p>
                    <button className="btn-change" onClick={routeChange}>Get your match now!</button>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default Home;