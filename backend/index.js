import express from "express";
import { PORT, mongoDBURL } from "./config.js";
import { Stop } from "./models/stopModel.js";
import stopsRoute from './routes/stopsRoute.js';
import cors from 'cors';

 const app = express();
 app.use(express.json());

 app.use(cors());

 app.listen(PORT, () => {
    console.log(`App is listening to port: ${PORT}`)
 });

 app.get('/', (request, response) => {
    console.log(request)
    return response.status(234).send('Welcome to ')
 });

app.use('/stops', stopsRoute);

 mongoose 
    .connect(mongoDBURL)
    .then(() => {
        console.log('App connected to database');
        app.listen(PORT, () => {
            console.log(`App is listening to port: ${PORT}`);
        });
    })
    .catcth((error) => {
        console.log(error);
    })