import React, { useState, useEffect } from "react";

function Result() {
    const [result, setResult] = useState([]);

    useEffect(() => {
        fetch('/result').then(res => res.json()).then(data => {
          setResult(data.result);
        });
      }, []);

    return (
        <div>
            <div className="container h-100 d-flex">
                <div className="jumbotron my-auto jumbotron-custom">
                    <h1 className="display-3">Hooray!</h1>
                    <p className="lead">
                        Here are our top 3 suggestions for you!<br></br>
                        {result}
                        <br></br>
                        We hope this will guide you in your decision. Thank you for using the Elective Course Recommender and wish you good luck in your final year!
                    </p>
                </div>
            </div>
        </div>
    );
}

export default Result;