import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, NavLink, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';
import ColorSchemesExample from './components/NavBar';
import Container from './components/Container';
import Header from './components/Header';
import Login from './components/Login';
import Signup from './components/Signup';
import { UserProvider, useUser } from './context/UserContext';

function App() {

  return (
    <UserProvider>
    <Router>
     <Header/>
 
      <Routes>
        <Route index element={<Container/>} />
        <Route path="home" element={<Container/>} />
        <Route path="signup" element={<Signup />} />
        <Route path="login" element={<Login />} />
 
      </Routes>
  
    </Router>
    </UserProvider>
  );
}

export default App;
