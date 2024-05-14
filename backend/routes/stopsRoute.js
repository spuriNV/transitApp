import express from 'express';
import { Stop } from '../models/stopModel.js';

const router = express.Router();


router.post('/', async (request, response) => {
    try {
        if (
            !request.body.stop_name ||
            !request.body.stop_id1 ||
            !request.body.stop_id2 ||
            !request.body.line_number ||
            !request.body.mode_type 
        ) {
            return response.status(400).send({
                message: 'Send all required fields: id, stop name, id1, id2, line number, mode type',
            });
        }
        const newStop = {
            stop_name: request.body.stop_name, 
            stop_id1: request.body.stop_id1,
            stop_id2: request.body.stop_id2,
            line_number: request.body.line_number,
            mode_type: request.body.mode_type,
        };

        const stop = await Stop.create(newStop);

        return response.status(201).send(stop);
    } catch(error) {
        console.log(error.message);
        response.status(500)
    }
 });

router.get('/', async (request, response) => {
    try {
        const stops = await Stop.find({});

        return response.status(200).json({
            count: stops.length, 
            data: stops
        });
    } catch (error) {
        console.log(error.message);
        response.status(500).send({message: error.message});
    }
 });

router.get('/:id', async (request, response) => {
    try {

        const { id } = request.params; 
        const stop = await Stop.findById(id);
        
        return response.status(200).json(stop);
    } catch (error) {
        console.log(error.message);
        response.status(500).send({message: error.message});
    }
 });

router.put('/:id', async (request, response) => {
    try {
        if (
            !request.body.stop_name ||
            !request.body.stop_id1 ||
            !request.body.stop_id2 ||
            !request.body.line_number ||
            !request.body.mode_type 
        ) {
            return response.status(400).send({
                message: 'Send all required fields. ',
            });
        }

        const { id } = request.params; 
        const result = await Stop.findByIdAndUpdate(id, request.body);

        if (!result) {
            return response.status(404).json({message: 'Stop not found'});
        }

        return response.status(200).send({message: 'Stop updated successfully'});

    } catch (error) {
      console.log(error.message);
      response.status(500).send({message: error.message});
    }
 })
 

router.delete(`/:id`, async (request, response) => {
    try {
        const { id } = request.params; 

        const result = await Stop.findByIdAndDelete(id);

        if(!result) {
            return response.status(404).json({message: `Stop not found`});
        }

        return response.status(200).send({message: `Stop deleted successfully`});

    } catch (error) {

    }
 });

 export default router; 

