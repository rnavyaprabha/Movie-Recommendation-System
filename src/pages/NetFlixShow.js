import Row from "../components/Row/Row"; 
import Banner from "../components/Banner/Banner";
import api from "../api/api";
import Nav from "../components/Nav/Nav";
import axios from 'axios';
import React, { useState, useEffect } from 'react';
import MovieGrid from "../components/MovieGrid/MovieGrid";

const getRecommendedMovies = async () => {
  try {
    const response = await axios.get('http://localhost:8000/usermovies/', { withCredentials: true });
    if (response.status === 200) {
    console.log('Preferences fetched successfully!');
    return response.data; // Return only the data from the response
    } else {
     console.error('Failed to fetch recommended movies');
      return []; // Return an empty array in case of failure
    }
  } catch (error) {
   console.error('Error fetching recommended movies:', error);
   return []; // Return an empty array in case of error
  }
};


const NetFlixShow = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get('https://pfwwebdev-6b47cef20bd2.herokuapp.com/usermovies/', { withCredentials: true });
        setMovies(response.data.movies);
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    };

    fetchMovies();
  }, []);

  return (
    <div>  
      <Nav />
      <Banner />
      <Row title="Recommended Movies" />
      <MovieGrid  movies={movies} />
      <Row title="Movies that you may also enjoy" fetchUrl={api.fetchNetflixOriginals} isLargeRow />
      <Row title="Trending Now" fetchUrl={api.fetchTrending} />
      <Row title="Top Rated" fetchUrl={api.fetchTopRated} />
      <Row title="Action Movies" fetchUrl={api.fetchActionMovies} />
      <Row title="Comedy Movies" fetchUrl={api.fetchComedyMovies} />
      <Row title="Horror Movies" fetchUrl={api.fetchHorrorMovies} />
      <Row title="Romance Movies" fetchUrl={api.fetchRomanceMovies} />
      <Row title="Documentaries" fetchUrl={api.fetchDocumentaries} />
    </div>
  );
};

export default NetFlixShow;



  