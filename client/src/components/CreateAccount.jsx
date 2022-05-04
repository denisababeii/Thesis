import { useNavigate } from "react-router-dom";
import "react-widgets/styles.css";
import "./style.css"
import React from "react";

function CreateAccount() {
    return (
        <div>
            <div className="container h-100 d-flex" style={{paddingBottom:"100px"}}>
                <div className="jumbotron my-auto jumbotron-custom" >
                    <h1 className="display-4">Nice to meet you!</h1>
                    <form class="needs-validation" novalidate>
                    <div class="form-row" style={{padding:"10px"}}>
                        <label for="validationCustom01">First name</label>
                        <input type="text" class="form-control" id="validationCustom01" placeholder="First name" required></input>
                        <div class="valid-feedback">
                            Looks good!
                        </div>
                    </div>
                    <div class="form-row" style={{padding:"10px"}}>
                        <label for="validationCustom02">Last name</label>
                        <input type="text" class="form-control" id="validationCustom02" placeholder="Last name" required></input>
                        <div class="valid-feedback">
                            Looks good!
                        </div>
                    </div>
                    <div class="form-row" style={{padding:"10px"}}>

                        <label for="validationCustomUsername">Username</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                            <span class="input-group-text" id="inputGroupPrepend">@</span>
                            </div>
                            <input type="text" class="form-control" id="validationCustomUsername"  aria-describedby="inputGroupPrepend" required></input>
                            <div class="invalid-feedback">
                            Wrong username.
                            </div>

                        </div>
                    </div>
                    <div class="form-row" style={{padding:"10px"}}>
                        <label for="validationCustom03">Password</label>
                        <input type="password" class="form-control" id="validationCustom03" placeholder="Password" required></input>
                        <div class="invalid-feedback">
                            Wrong password.
                        </div>
                    </div>
                    <div style={{display:"flex"}}><p style={{paddingRight:"5px", paddingLeft:"5px"}}>Already here?</p><a href="/login" style={{color:"rgba(96,106,255,1)"}}>Log in</a></div> 
                    <div style={{display:"flex", alignItems:"center", justifyContent:"center"}}>
                        <button class="btn-change" type="submit" style={{width:"100px"}}>Sign up</button>
                    </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default CreateAccount;