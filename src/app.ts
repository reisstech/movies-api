import "reflect-metadata"
import express from "express"
import { Request, Response, NextFunction } from "express"
import "express-async-errors"
import { router } from "./routes"
import { config } from 'dotenv'


const app = express()

config()
app.use(express.json())
app.set('view engine', 'ejs')



app.set('views', __dirname);

app.use(router)



app.use(
    (err: Error, request: Request, response: Response, next: NextFunction) => {
        if (err instanceof Error) {
            return response.status(400).json({
                error: err.message,
            })
        }

        return response.status(500).json({
            status: "error",
            message: "Internal Server Error"
        })  
    }
)


export { app }