import React from "react";
import "./MovieGrid.css";

const MovieGrid = ({ movies }) => {
  // Get the top 15 movies
  const topMovies = movies.slice(0, 15);

  return (
    <div className="movie-grid">
      {topMovies.map((movie, index) => (
        <div className="movie" key={index}>
          <img src={movie.url} alt={movie.title} />
          <div className="movie-info">
            <h3>{movie.title}</h3>
            <p>Director: {movie.director}</p>
            <p>IMDB: {movie.imdb}</p>
            <p>Year: {movie.year}</p>
            <p>Genres: {movie.genres.join(", ")}</p>
            <p>{movie.overview}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default MovieGrid;
