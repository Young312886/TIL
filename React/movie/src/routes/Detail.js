import {useParams} from "react-router-dom"
import { useEffect, useState } from "react"


function Detail() {
    const {id} = useParams()
    const [movie, setMovie] = useState([])

    const getMovie = async () => {
        const json = await ( await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`).json()) 
    return json}
    useEffect(() => {
        const single = getMovie()
        setMovie(single)
    }, [])
    return <div>Detail
        <div>{movie}</div>
    </div>
}
export default Detail;
