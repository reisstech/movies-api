import { Request, Response } from 'express'
import axios from 'axios'


class GetMoviesByGenreController {
    async handle(request: Request, response: Response) {
        try {
    
            const {genre_id} = request.params
            
            const { data } = await axios.get(`http://flask_api:5000/movies/${genre_id}`)

            return response.json(data)

     
           } catch(err) {
               console.log(err)
           }
        

    }
}

export { GetMoviesByGenreController }
