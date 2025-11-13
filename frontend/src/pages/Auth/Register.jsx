//src/pages/Auth/Register.jsx

import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { registerSchema } from "./register.schema";
import { useNavigate } from "react-router-dom";

export default function Register() {

    const navigate = useNavigate();

    /* Initialize form with schema validation */
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(registerSchema),
    });

    /* Handle submit */
    const onSubmit = async (data) => {
        console.log("Register data:", data);

        try {
            const response = await fetch("/api/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            if (!response.ok) throw new Error("Registration failed");

            const result = await response.json();
            console.log("Registration successful: ", result);

            /* Redirect after success */
            navigate("/login");
        } catch (error) {
            console.error("Error during registration:", error);
        }
    };
    
    return (
        <div className="container mt-5" style={{ maxWidth: 500 }}>
            <h2 className="mb-4 text-center">Register</h2>
            <form onSubmit={handleSubmit(onSubmit)} noValidate>

                {/* Full Name */}
                <div className="form-group mb-3">
                    <label>Full Name</label>
                    <input {...register("full_name")} className={`form-control ${errors.full_name ? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.address?.message}</div>
                </div>
                
                {/* Address */}
                <div className="form-group mb-3">
                    <label>Address</label>
                    <input {...register("address")} className={`form-control ${errors.address ? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.address?.message}</div>
                </div>
                {/* City */}
                <div className="form-group mb-3">
                    <label>City</label>
                    <input {...register("city")} className={`errors.city ? "in-invalid" : "" }`} />
                    <div className="invalid-feedback">{errors.city?.message}</div>
                </div>

                {/* Gender */}
                <div className="form-group mb-3">
                    <label>Gender</label>
                    <select {...register("gender")} className={`form-control ${errors.gender ? "is-invalid" : ""}`}>
                        <option value="">Select gender</option>
                        <option value="">Male</option>
                        <option value="">Female</option>
                        <option value="other">Other</option>
                    </select>
                    <div className="invalid-feedback">{errors.gender?.message}</div>
                </div>

                {/* Email */}
                <div className="form-group mb-3">
                    <label>Email</label>
                    <input type="email" {...register("email")} className={`form-control ${errors.email ? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.email?.message}</div>
                </div>

                {/* Password */}
                <div className="form-group mb-3">
                    <label>Password</label>
                    <input type="password" {...register("password")} className={`form-control ${errors.password ? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.password?.message}</div>
                </div>

                {/* Confirm Password */}
                <div className="form-group mb-3">
                    <label>Confirm Password</label>
                    <input type="password" {...register("password again")} className={`form-control ${errors.password_again? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.password_again?.message}</div>
                </div>

                <button className="btn btn-success w-100" type="submit">Register</button>
            </form>
        </div>
    );
}