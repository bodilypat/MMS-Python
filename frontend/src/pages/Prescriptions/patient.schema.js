//src/pages/Patients/patient.schema.js 

import * as Yup from "yup";

export const patientSchema = Yup.object().shape({
    full_name: Yup.string()
        .trim()
        .min(2, "full name must be at least 2 characters")
        .required("Full name is required"),

    age: Yup.number()
        .typeError("Age must be a number")
        .min(0, "Age cannot be negative")
        .max(120,"Age must be realistic")
        .required("Age is required"),

    gender: Yup.string().required("Gender is required"),
    address: Yup.string().min(3, "Address too short").required("Address is required"),
    city: Yup.string().required("City is required"),
    phone: Yup.string()
        .matches(/^[0-9+\-\s]{7,15}$/,"Invalid phone number")
        .required("Phone is required"),

    email:  Yup.string().email("Invalid email").required("Email is required"),

    medical_history: Yup.string().nullable(),
});
