import React, { useState } from 'react';
import './Questionnaire.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const genresOptions = ['Sport', 'Film-Noir', 'Musical', 'Horror', 'Music', 'Mystery', 'War', 'Family', 'Animation', 'Thriller', 'Comedy', 'Fantasy', 'Western', 'Romance', 'Sci-Fi', 'History', 'Biography', 'Adventure', 'Action', 'Crime', 'Drama'];

const ratingOptions = [
  { value: 0, label: 'Select IMDb Rating' },
  { value: 1, label: '1+' },
  { value: 2, label: '2+' },
  { value: 3, label: '3+' },
  { value: 4, label: '4+' },
  { value: 5, label: '5+' },
  { value: 6, label: '6+' },
  { value: 7, label: '7+' },
  { value: 8, label: '8+' },
  { value: 9, label: '9+' },
  { value: 9.5, label: '9.5+' },
];

const Questionnaire = () => {
  const navigate = useNavigate();
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [selectedRating, setSelectedRating] = useState(0);

  const handleGenreSelect = (genre) => {
    if (selectedGenres.includes(genre)) {
      setSelectedGenres(selectedGenres.filter((g) => g !== genre));
    } else {
      if (selectedGenres.length < 3) {
        setSelectedGenres([...selectedGenres, genre]);
      }
    }
  };

  const handleRatingSelect = (event) => {
    setSelectedRating(parseFloat(event.target.value));
  };

  const handleSubmit = async () => {
    const data = {
      genres: selectedGenres,
      rating: selectedRating,
    };

    try {
          const response = await axios.post('https://pfwwebdev-6b47cef20bd2.herokuapp.com/usermovies/', data, { withCredentials: true });
          navigate('/homepage'); 
      if (response.ok) {
        console.log('Preferences submitted successfully!');
      } else {
        console.error('Failed to submit preferences');
      }
    } catch (error) {
      console.error('Error submitting preferences:', error);
    }
  };

  return (
    <div className="showcase">
        <div className="questionnaire-container-box">
            <h2>Movie Preferences Questionnaire</h2>

            <div className="genre-options">
            <h4>Select up to 3 genres you like:</h4>
            <div className="genre-tags">
                {genresOptions.map((genre) => (
                <span
                    key={genre}
                    className={`genre-tag ${selectedGenres.includes(genre) ? 'selected' : ''}`}
                    onClick={() => handleGenreSelect(genre)}
                >
                    {genre}
                </span>
                ))}
            </div>
            </div>

            <div className="rating-dropdown">
            <h4>Select minimum IMDb rating:</h4>
            <select value={selectedRating} onChange={handleRatingSelect}>
                {ratingOptions.map((option) => (
                <option key={option.value} value={option.value}>
                    {option.label}
                </option>
                ))}
            </select>
            </div>

            <div className="selected-info">
            <h4>Selected Genres: {selectedGenres.join(', ') || 'None'}</h4>
            <h4>Minimum IMDb Rating: {selectedRating || 'Not selected'}</h4>

            <button className="submit-button" onClick={handleSubmit}>
            Submit Preferences
            </button>

            </div>
        </div>
    </div>
  );
};
export default Questionnaire;
