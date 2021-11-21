import axios from 'axios'


    class GetMoviesByGenreService {
        async execute(genre_id) {

        const { data } = await axios(`https://api.themoviedb.org/3/discover/movie?api_key=d4a0eb627931e1e8dbc864d5afc2202e&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=${genre_id}&with_watch_monetization_types=flatrate`)

        return data
        }
        

    }       
    
    export { GetMoviesByGenreService }
    
      


