//src/pages/Patients/PatientForm.jsx 

import React from "react";
import { useForm } from "react-hook-form";
import {yupResolver } from "@hookform/resolvers/yup";
import { patientSchema } from "./patient.schema";
import { useNavigate } from "react-router-dom";
import { createPatient, updatePatient } from "../../services/patientService";
import InputField from "../../components/common/InputField";
import { formatPhoneNumber } from "../../utils/formatters";

export default function PatientForm({ existingData = null }) {
    const navigate = useNavigate();

    const {
        register,
        handleSubmit,
        reset,
        formState: { errors, isSubmitting },
    } = useForm({
        resolver: yupResolver(patientSchema),
        defaultValues: existingData || {},
    });

    const onSubmit = async (data) => {
        try {
            const formatteData = {...data, phone: formatPhoneNumber(data.phone),};

            let response;
            if (existingData?.id) {
                response = await updatePatient(existingData.id, formatteData);
            } else {
                response = await createPatient(formatteData);
            }

            console.log("Patient saved:", response);
            navigate("/patients");
        } catch (error) {
            console.error("Error saving patient:", error);
        }
    };

    return (
        <div className="container mt-4" style={{ maxWidth: 600 }}>
            <h2 className="mb-4 text-center">{existingData ? "Edit Patient" : "Add New Patient"}</h2>
            <form onSubmit={handleSubmit(onSubmit)} noValidation>
                /* Full Name */
                <InputField label="Full Name" {...register("full_name")} error={errors.full_name} />
                /* Age */
                <InputField label="Age" {...register("age")} error={errors.full_name} />
                /* Gender */
                <div className="form-group mb-3">
                    <label>Gender</label>
                    <select {...register("gender")} className={`form-control ${errors.gender ? "is-invalid" : ""}`}>
                        <option value="">Select Gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                    </select>
                    <div className="invalid-feedback">{errors.gender?.message}</div>
                </div>

                /* Address */
                <InputField label="Address" {...register("address")} error={errors.address} />

                /* city */
                <InputField label="City" {...register("city")} error={errors.city} />
                /* Phone */
                <InputField label="Phone" {...register("phone")} error={errors.phone} />
                /* Email */
                <InputField label="Email" type="email" {...register("email")} error={errors.email} />
                /* Medical History */
                <div className="form-group mb-3">
                    <label>Medical History</label>
                    <textarea {...register("medical_history")} rows={3} className={`form-control ${errors.medical_history ? "is-invalid" : "" }`} />
                    <div className="invalid-feedback">{errors.medical_history?.message}</div>
                </div>

                /* Buttons */
                <div className="d-flex justify-content-between">
                    <button type="button" className="btn btn-secondary" onClick={() => navigate("/patients")} >Cancel</button>
                    <button type="submit" className="btn btn-primary" disabled={isSubmitting}>{isSubmitting ? "Saving..." : "Save Patient"}</button>
                </div>
            </form>
        </div>
    );
}
