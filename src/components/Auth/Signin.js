import React, { useState } from 'react';
import './Auth.css';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const SignIn = ({ toggleForm }) => {
  const navigate = useNavigate();

  // State variables for form inputs and validation
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!email.trim()) {
      setErrors({ email: 'Email is required' });
      return;
    }
    if (!password.trim()) {
      setErrors({ password: 'Password is required' });
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setErrors({ email: 'Invalid email format' });
      return;
    }

    try {
        const response = await axios.post('https://pfwwebdev-6b47cef20bd2.herokuapp.com/login/', {
            username: email,
            password: password
          }, 
          { withCredentials: true }
      );
        console.log('Login successful:', response.data);
        localStorage.setItem('token', response.data.token);
        navigate('/homepage'); 
    } catch (error) {
        console.error('Login failed:', error);
        window.alert('Invalid username or password. Please try again.');
        setEmail('');
        setPassword('');
    }

  };

  return (
    <div className="signin-container showcase">
      <form className="signin-form" onSubmit={handleSubmit}>
        <h2>Sign In</h2>
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        {errors.email && <p className="error-message">{errors.email}</p>}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {errors.password && <p className="error-message">{errors.password}</p>}
        <button type="submit">SIGN IN</button>
        <Link to="/signup">
          New user? Sign up now.
        </Link>
      </form>
    </div>
  );
};

export default SignIn;
