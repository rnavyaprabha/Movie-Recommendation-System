import React, { useEffect, useState } from "react";
import axios from "axios";
import"./Row.css";
import YouTube from "react-youtube";
import movieTrailer from "movie-trailer";


const base_url = "https://image.tmdb.org/t/p/original";

const Row = ({ title, fetchUrl, isLargeRow }) => {
  const [movies, setMovies] = useState([]);
  const [trailerUrl, setTrailerURL] = useState("");
  console.log("process.env.REACT_APP_API", process.env.REACT_APP_API);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(
        `${process.env.REACT_APP_API}${fetchUrl}`
      );
      setMovies(response.data.results);
      return response;
    };

    fetchData();
  }, []); 

  const handleClick = (movie) => {
    if (trailerUrl) {
      setTrailerURL("");
    } else {
      movieTrailer(movie?.name || "")
      .then((url) => {
          const urlParams = new URLSearchParams(new URL(url).search);
          //https://www.youtube.com/watch?v=ue80QwXMRHg
          setTrailerURL(urlParams.get("v")); // ue80@wXMRHg
      })
      .catch((error) => console.log(error));

    }
    
  };

  const opts = {
    height: "390",
    width: "100%", 
    playerVars: {
      autoplay: 1,
    },
  } ;

  return (
    <div className="row">
      <h2>{title}</h2>
      <div className="row-posters">
        {movies &&
          movies.map((movie) => (
            <img
              onClick={() => handleClick(movie)}
              key={movie.id}
              className={`row-poster ${isLargeRow && "row-posterLarge"}`}
              src={`${base_url}${
                isLargeRow ? movie.poster_path : movie.backdrop_path
              }`}
              alt={movie.name}
            />
          ))}
      </div>
      {trailerUrl && <YouTube videoId={trailerUrl} opts={opts} />}
    </div>
  );
};

export default Row;
