//src/pages/Auth/Login.schema.js 

import * as Yup from "yup";

export const loginSchema = Yup.object().shape({
    username: Yup.string()
        .trim()
        .min(2, "Username must be at least 2 characters long")
        .max(30, "Username cannot exceed 30 characters")
        .required("Username is required"),

    password: Yup.string()
    .min(6, "Password must be at least 6 characters long")
    .max(50, "Password cannot exceed 50 characters")
    .required("Password is required"),
});