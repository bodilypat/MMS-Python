//src/pages/Doctors/doctor.schema.js 

import * as Yup from "yup";

export const doctorSchema =  Yup.object().shape({
    first_name: Yup.string().required("First name is required"),
    last_name: Yup.string().required("Last name is required"),
    specialization: Yup.string().required("Specialization is required"),
    email: Yup.string().email("Invalid email").required("Email is required"),
    contact_number: Yup.string().matches(/^[0-9\-\+]{7,15}$/,"Invalid contact number"),
});

