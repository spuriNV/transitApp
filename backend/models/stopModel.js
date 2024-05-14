import mongoose from "mongoose";

const stopSchema = mongoose.Schema(
    {
        stop_name: {
            type: String, 
            required: true, 
        },
        stop_id1: {
            type: String, 
            required: true, 
        },
        stop_id2: {
            type: String, 
            required: true, 
        },
        line_number: {
            type: String, 
            required: true, 
        },
        mode_type: {
            type: String, 
            required: true, 
        },
    },
    {
        timestamps: true,
    }
);

export const Stop = mongoose.model('Cat', stopSchema);