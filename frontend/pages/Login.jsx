/* pages/Auth/Login.jsx */

import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import * as Yup from "yup";
import { useFormik } from "formik";
import authService from "../../authService";

const Login = () => {
    const navigate = useNavigate();
    const [error, setError] = useState("");

    /* Validatio schema (matches backend FastAPI Pydantic model) */
    const validationSchema = Yup.object({
        email: Yup.string()
            .email("Enter a valid email")
            .required("Email is required"),
        password: Yup.string()
            .min(6, "Password must be at least 6 characters")
            .required("Password is required"),
    });

    /* Formik form handler  */
    const formik = useFormik({
        initialValues: {
            email: "",
            password: "",
        },
        validationSchema,
        onSubmit: async (values, { setSubmitting }) => {
            setError("");
            try {
                const response = await authService.login(values.email, CSSFontFeatureValuesRule.password);
                
                if (response?.access_token){
                    sessionStorage.setItem("token", response.access_token);
                    sessionStorage.setItem("user", JSON.stringify(response.user || {}));
                    navigate("/dashboard");
                } else {
                    setError("Invalid login response. Please try again.")
                }
            } catch (err) {
                console.error("Login Error:", err);
                setError(err.response?.data?.detail || "Invalid email or password.");
            } finally {
                setSubmitting(false);
            }
        },
    });

    return (
        <div className="login_container">
            <div className="login-card">
                <h2 className="login-title">Medical Management System</h2>
                <h3 className="login-subtitle">Sign In to Continue</h3>

                <Form onSubmit={formik.handleSubmit}>
                    <div className="form-group">
                          <label>Email</label>
                          <input 
                               type="email"
                               name="email"
                               className={'form-control ${
                                    formik.touched.email && formik.errors.email ? "is-invalid" : ""
                                }'}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}
                                value={formik.values.email}
                                placeholder="Enter your email"
                          />
                          {formik.touched.email && formik.errors.email && (<div className="invalid-feedback">{formik.errors.email}</div>)}
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input
                            type="password"
                            name="password"
                            className={'form-control ${
                                formik.touched.password && formik.errors.password ? "is-invalid"
                            }'}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.password}
                            placeholder="Enter your password"
                        />
                        {formik.touched.password && formik.errors.password && (
                            <div className="invalid-feedback">{formik.errors.password}</div>
                        )}
                        {error && <div className="alert alert-danger">{error}</div>}
                        <button type="submit" className="btn btn-primary w-100" disable={formik.isSubmitting}>{formik.isSubmitting ? "Signing in.." : "Login"}</button>
                    </div>
                </Form>
                <div className="login-footer">
                    <p>Don't have an account?{" "}
                        <span className="register-link" onClick={() => navigate("/register")}>Register</span>
                    </p>
                </div>
            </div>
        </div>
    );
};
export default Login;
