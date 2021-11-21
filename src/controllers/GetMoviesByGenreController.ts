import { Request, Response } from 'express'
import { GetMoviesByGenreService} from '../services/GetMoviesByGenreService'
import axios from 'axios'


const getMoviesByGenreService = new GetMoviesByGenreService


class GetMoviesByGenreController {
    async handle(request: Request, response: Response) {
        try {
    
            const {genre_id} = request.params
            
            const { data } = await axios.get(`http://localhost:5000/movies/${genre_id}`)

            return response.json(data)

     
           } catch(err) {
               console.log(err)
           }
        

    }
}

export { GetMoviesByGenreController }
