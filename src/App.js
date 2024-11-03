import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'; 
import Home from './pages/Home';
import NetFlixShow from './pages/NetFlixShow';
import './App.css';
import Footer from './components/Footer/Footer';
import Signin from './components/Auth/Signin';
import Signup from './components/Auth/Signup';
import Questionnaire from './components/Questionnaire/Questionnaire';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes> 
          <Route exact path='/' element={<Home />} /> 
          <Route path='/signin' element={<Signin />} /> 
          <Route path='/signup' element={<Signup />} /> 
          <Route path='/questionnaire' element={<Questionnaire />} /> 
          <Route path="/homepage" element ={<NetFlixShow />}/>
        </Routes>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
