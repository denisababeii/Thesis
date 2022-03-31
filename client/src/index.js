import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import {
  Navigation,
  Footer,
  Home
} from "./components"
import GradesForm from './components/GradesForm';
import PreferenceForm from './components/PreferenceForm'
import Result from './components/Result'

ReactDOM.render(
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/grades" element={<GradesForm />} />
      <Route path="/preference" element={<PreferenceForm />} />
      <Route path="/result" element={<Result />} />
    </Routes>
    <Footer />
  </Router>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
