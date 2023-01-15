import { useEffect, useState } from "react";
import Movie from '../components/Movie.js'

function Home () {
    const [loading, setLoading] = useState(true);
    const [movies, setMovies] = useState([]);
    // async 함수를 활용한 버전
    const getMovies = async () => {
      const response = await fetch(
        "https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year"
      );
      const json = await response.json();
      setMovies(json.data.movies);
      setLoading(false);
    };
    useEffect(() => {
      getMovies();
    }, []);
    //   useEffect(() => {
    //     fetch(
    //       "https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year")
    //       .then((response) => response.json())
    //       .then((json) => {
    //         setMovies(json.data.movies);
    //         setLoading(false);
    //       });
    //   }, []);
  
    return (
      <div>
        {loading ? (
          <h1>Loading</h1>
        ) : (
          <div>
            {movies.map((movie) => (
              <Movie key={movie.id} movie={movie} id={movie.id}/>
            ))}
          </div>
        )}
      </div>
    );
};
export default Home;
