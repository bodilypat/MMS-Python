//src/pages/Prescriptions/prescription.shema.js

import * as Yup from "yup";

export const prescriptionSchema = Yup.object().shape({
    /* Foreign keys reference to medical_records */
    record_id: Yup.number()
        .typeError("Record ID must be a number")
        .integer("Record ID must be an integer")
        .positive("Record ID must be a positive number")    
        .required("Record ID is required"),

        /* Core prescription fields */
    medication_name: Yup.string()
        .trim()
        .max(100, "Medication name cannot exceed 100 characters")
        .required("Medication name is required"),

    dosage: Yup.string()
        .trim()
        .max(50, "Dosage cannot exceed 50 characters")
        .required("Dosage is required"),

    frequency: Yup.string()
        .trim()
        .max(50, "Frequency cannot exceed 50 characters")
        .required("Frequency is required"),
    
    /* Dates */
    start_date: Yup.date()
        .nullable()
        .typeError("Start date must be a valid date")
        .required("Start date is required"),

    end_date: Yup.date()
        .nullable()
        .typeError("End date must be a valid date")
        .required("End date is required"),

    duration: Yup.string()
        .trim()
        .max(50, "Duration cannot exceed 50 characters")
        .required("Duration is required"),

    /* Optional fi */
    instructions: Yup.string()
        .trim()
        .max(255, "Instructions cannot exceed 255 characters")
        .nullable(),
    
    status: Yup.string()
        .oneOf(["Active", "Completed", "Expired", "Cancelled"], "Invalid status value")
        .default("Active")
        .required("Status is required"),
});

export default prescriptionSchema;
