import React from 'react'
import "./Header.css";
import {Link} from 'react-router-dom';

const Header = () => {
  return (
    <header className='showcase'>
        <div className='showcase-top' >
            <h1> Movie Recommeder </h1>
            <Link to="/signin" className='btn btn-rounded' >
                Sign In
            </Link>
        </div>
        <div className='showcase-content'>
            <h1> The Smart Way To Pick A Movie. </h1>
            <p> Discover cinema you'll love </p>
            <Link to="/signup" className='btn btn-xl'>
                Sign Up
                <i className='fas fa-chevron-right btn-icon'></i>
            </Link>
        </div>

    </header>
  )
}

export default Header