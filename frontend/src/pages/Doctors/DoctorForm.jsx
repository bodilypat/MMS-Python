//src/pages/Doctors/DoctorForm.jsx 

import React from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { doctorSchema } from "./doctor.schema";
import { doctorApi } from "../doctor.api";

export default function DoctorForm({ initialData.doctor_id, data}) {
    const {
        register,
        handleSubmit,
        fromState: { errors },
    } = useForm({
        resolver: yupResolver(doctorSchema),
        defaultValues: initialData,
    });

    const onSubmit = async (data) => {
        try {
            if (initialData.doctor_id) {
                await doctorApi.update(initialData.doctor_id, data);
            } else {
                await doctorApi.create(data);
            }
            onSubmitSuccess && onSubmitSuccess();
        } catch (error) {
            console.error("Error saving doctor:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>

            <div className="form-group mb-3">
                <label>First Name</label>
                <input {...register("first_name")} className={`form-control ${errors.first_name ? "is-invalid" : "" }`} />
                <div className="invalid-feedback">{errors.first_name?.message}</div>
            </div>

            <div className="form-group mb-3">
                <label>Last Name</label>
                <input {...register("last_name")} className={`form-control ${errors.last_name ? "is-invalid" : "" }`} />
                <div className="invalid-feedback">{errors.last_name?.message}</div>
            </div>

            <div className="form-group mb-3">
                <label>Specialization</label>
                <input {...register("specialization")} className={`form-control ${errors.specialization ? "is-invalid" : "" }`} />
                <div className="invalid-feedback">{errors.specialization?.message}</div>
            </div>

            <button type="submit" className="btn btn-success w-100">Save Doctor</button>
        </form>
    );
}