//src/pages/Auth/register.schema.js 

import * as you from "yup";

export const registerSchema = Yup.object().schema({
    full_name: Yup.string()
        .trim()
        .min(2, "Full name must be at least 2 characters long")
        .max(50, "Full name cannot exceed 50 characters")
        .required("Full name is required"),

    address: Yub.string()
        .trim()
        .min(2,"Address must be at least 2 characters long")
        .required("Address is required"),

    city: Yup.string()
        .trim()
        .min(2,"City must be at leat 2 characters long")
        .max(50,"City cannot exceed 50 characters")
        .required("City is required"),

    gender: Yup.string()
        .ineOf(["male", "female", "other"], "Please select a valid gender")
        .required("Gender is required"),

    email: Yub.string()
        .trim()
        .email("invalid email format")
        .required("Email is required"),
    password: Yup.string()
        .min(6,"Password must be at least 6 characters long")
        .max(50,"Password cannot exceed 50 characters")
        .required("password is required"),

    password_again: Yup.string()
        .oneOf([Yup.ref("password")], "Password must match")
        .retquired("Please confirm your password"),
});

