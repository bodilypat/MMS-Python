// src/pages/Appointments/AppointmentForm.jsx
import React, { useEffect } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { useNavigate, useParams } from "react-router-dom";
import { appointmentSchema } from "./appointment.schema";
import {
  createAppointment,
  getAppointmentById,
  updateAppointment,
} from "./appointment.api";

export default function AppointmentForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const isEdit = !!id;

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({ resolver: yupResolver(appointmentSchema) });

  useEffect(() => {
    if (isEdit) loadAppointment();
  }, [id]);

  const loadAppointment = async () => {
    try {
      const res = await getAppointmentById(id);
      const data = res.data;
      Object.keys(data).forEach((key) => setValue(key, data[key]));
    } catch (error) {
      console.error("Error loading appointment:", error);
    }
  };

  const onSubmit = async (data) => {
    try {
      if (isEdit) {
        await updateAppointment(id, data);
        alert("Appointment updated successfully!");
      } else {
        await createAppointment(data);
        alert("Appointment created successfully!");
      }
      navigate("/appointments");
    } catch (error) {
      console.error("Error saving appointment:", error);
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: 600 }}>
      <h2>{isEdit ? "Edit Appointment" : "New Appointment"}</h2>
      <form onSubmit={handleSubmit(onSubmit)} noValidate>
        <div className="mb-3">
          <label>Patient ID</label>
          <input {...register("patient_id")} className={`form-control ${errors.patient_id ? "is-invalid" : ""}`} />
          <div className="invalid-feedback">{errors.patient_id?.message}</div>
        </div>

        <div className="mb-3">
          <label>Doctor ID</label>
          <input {...register("doctor_id")} className={`form-control ${errors.doctor_id ? "is-invalid" : ""}`} />
          <div className="invalid-feedback">{errors.doctor_id?.message}</div>
        </div>

        <div className="mb-3">
          <label>Date & Time</label>
          <input type="datetime-local" {...register("appointment_datetime")} className={`form-control ${errors.appointment_datetime ? "is-invalid" : ""}`} />
          <div className="invalid-feedback">{errors.appointment_datetime?.message}</div>
        </div>

        <div className="mb-3">
          <label>Status</label>
          <select {...register("status")} className={`form-control ${errors.status ? "is-invalid" : ""}`}>
            <option value="Scheduled">Scheduled</option>
            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>
            <option value="No-Show">No-Show</option>
          </select>
          <div className="invalid-feedback">{errors.status?.message}</div>
        </div>

        <div className="mb-3">
          <label>Reason</label>
          <input {...register("reason")} className={`form-control ${errors.reason ? "is-invalid" : ""}`} />
          <div className="invalid-feedback">{errors.reason?.message}</div>
        </div>

        <div className="mb-3">
          <label>Notes</label>
          <textarea {...register("notes")} className={`form-control ${errors.notes ? "is-invalid" : ""}`} />
        </div>

        <button className="btn btn-primary w-100" type="submit">
          {isEdit ? "Update" : "Create"} Appointment
        </button>
      </form>
    </div>
  );
}
