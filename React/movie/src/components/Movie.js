import PropTypes from 'prop-types'
import {Link} from 'react-router-dom';

function Movie({ id, movie }) {
  return (
    <div>
      <h2><Link to={`/movie/${id}`}> {movie.title} </Link> </h2>
      <img src={movie.medium_cover_image} alt="none" />
      <p>{movie.summary}</p>
      <ul>
        {movie.genres.map((g) => (
          <li key={g}>{g}</li>
        ))}
      </ul>
    </div>
  );
}

Movie.propTypes = {
  id: PropTypes.number.isRequired,
    movie: PropTypes.object.isRequired
}
export default Movie;
