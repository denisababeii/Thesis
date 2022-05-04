import React, { useState, useEffect } from "react";

function UserProfile() {
    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom" style={{background: "radial-gradient(circle, rgba(76,106,255,1) 0%, rgba(241,225,255,1) 100%)"}}>
                <h1 className="display-4">You</h1>
                </div>
            </div>
        </div>
    );
}

export default UserProfile;