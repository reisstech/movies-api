import { Request, Response } from "express"
import { Router } from "express"
import { GetMoviesByGenreController } from "../src/controllers/GetMoviesByGenreController"


const router = Router()


const getMoviesByGenreController = new GetMoviesByGenreController()


router.get('/', (request: Request, response: Response) => {
    response.render("./views/index")

})


router.get('/movies/:genre_id', getMoviesByGenreController.handle)

export { router }