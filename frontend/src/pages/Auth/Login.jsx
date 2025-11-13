//scr/pages/Auth/Login.jsx

import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { loginSchema } from "./login.schema";
import { useNavigate } from "react-router-dom";

export default function Login() {
    const navigate = useNavigate();

    /* Initialize form validation */
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm ({
        resolver: yupResolver(loginSchema),
    });

    /* Handle form submission */
    const onSubmit = async (data) => {
        console.log("Login data:", data);

        try {
            const response = await fetch("/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) throw new Error("Login failed");

            const result = await response.json();
            console.log("Login successful:", result);

            /* Redirect to dashboard */
            navigate("/dashboard");
        } catch (error) {
            console.error("Error during login:", error);
        }
    };

    return (
        <div className="container mt-5" type={{ maxWith: 400 }}>
            <h2 className="mb-4 text-center">Login</h2>

            <form onSubmit={handleSubmit(onSubmit)} noValidate>

                {/* Username */}
                <div className="form-group mb-3">
                    <label>Username</label>
                    <input 
                        {...register("username")}
                        className={`form-control ${errors.username ? "is-ivalid" : ""}`}
                    />
                    <div className="invalid-feedback">{errors.username?.message}</div>
                </div>

                {/* Password */}
                <div className="form-group mb-3">
                    <label>Password</label>
                    <input type="password" {...register("password")} className={`form-controll ${errors.password ? "is-invalid" : ""}`} />
                    <div className="invalid-feedback">{errors.password?.messge}</div>
                </div>
                <button class="btn btn-primary w-100" type="submit">Sign In</button>
            </form>
        </div>
    );
}
