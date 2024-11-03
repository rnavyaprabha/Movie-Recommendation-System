import React, { useState, useEffect } from "react";
import "./Nav.css";
import { Link } from "react-router-dom";
import NetFlixAvatar from "../../images/NetflixAvatar.png";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Nav = () => {
  const navigate = useNavigate();
  const [show, setShow] = useState(false);
  const [dropdownVisible, setDropdownVisible] = useState(false); // State to handle the dropdown visibility

  const NavBarVisibility = () => {
    if (window.scrollY > 100) {
      setShow(true);
    } else {
      setShow(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", NavBarVisibility);

    return () => {
      window.removeEventListener("scroll", NavBarVisibility);
    };
  }, []);

  const toggleDropdown = () => setDropdownVisible(!dropdownVisible);

  const handlelogOut = async (e) => {
    console.log('Inside handle logout');
    e.preventDefault();

    try {
      const response = await axios.post(
        'https://pfwwebdev-6b47cef20bd2.herokuapp.com/logout/', 
        {},
        { withCredentials: true }
      );
      console.log('Logout successful');
      navigate('/'); 
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <div className={`nav ${show ? "nav-black" : ""}`}>
      <Link to="/homepage" className="nav-logo">
        MovieRecommender
      </Link>
      <div className="nav-item-container" onClick={toggleDropdown}>
        <img src={NetFlixAvatar} className="nav-avatar" alt="Avatar" />
        {dropdownVisible && (
          <div className="dropdown-menu">
            <Link to="/questionnaire" className="dropdown-item">Watch Preferences</Link>
            <div className="dropdown-item" onClick={handlelogOut}>Logout</div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Nav;
