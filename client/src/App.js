import { BrowserRouter, Route, Routes} from 'react-router-dom'
import Home from './components/Home'
import useToken from './components/useToken'
import GradesForm from './components/GradesForm';
import PreferenceForm from './components/PreferenceForm'
import Result from './components/Result'
import Login from './components/Login'
import CreateAccount from './components/CreateAccount'
import UserProfile from './components/UserProfile'
import CourseInfo from './components/CourseInfo'
import './App.css'
import { Navigation } from './components';
import { useState } from 'react';
import useUsername from './components/useUsername';

function App() {
  const { token, removeToken, setToken } = useToken();
  const { username, setUsername } = useUsername()

  return (
    <BrowserRouter>
      <div className="App">
        {!token && token!=="" &&token!== undefined?  
        <Routes>
          <Route path="/" element={<Login setToken={setToken} setUsername={setUsername}/>}></Route>
          <Route path="/account" element={<CreateAccount setToken={setToken} setUsername={setUsername}/>} />
        </Routes>
        :(<>
          <Navigation removeToken={removeToken}/>
            <Routes>
                <Route path="/" element={<Home token={token} setToken={setToken}/>}></Route>
                <Route path="/grades" element={<GradesForm username={username} token={token} setToken={setToken}/>}></Route>
                <Route path="/preference" element={<PreferenceForm username={username} token={token} setToken={setToken}/>} />
                <Route path="/result" element={<Result username={username} token={token} setToken={setToken}/>} />
                <Route path="/info" element={<CourseInfo username={username} token={token} setToken={setToken}/>} />
                <Route path="/profile" element={<UserProfile username={username} setUsername={setUsername} token={token} setToken={setToken}/>} />
            </Routes>
          </>
        )}
      </div>
    </BrowserRouter>
  );
}

export default App;