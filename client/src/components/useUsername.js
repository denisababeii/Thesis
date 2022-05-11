import { useState } from 'react';

function useUsername() {

  function getUsername() {
    const username = localStorage.getItem('username');
    return username
  }

  const [username, setUsername] = useState(getUsername());

  function saveUsername(username) {
    localStorage.setItem('username', username);
    setUsername(username);
  };

  function removeUsername() {
    localStorage.removeItem("username");
    setUsername(null);
  }
  
  return {
    setUsername: saveUsername,
    username,
    removeUsername
  }

}

export default useUsername;