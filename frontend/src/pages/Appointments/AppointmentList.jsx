//src/pages/Appointments/AppointmentList.jsx 

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getAppointments, deleteAppointment } from "./appointment.api";

export default function AppointmentList() {
    const [appointments, setAppointments] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        loadAppointments();
    }, []);

    const loadAppointments = async () => {
        try {
            const response = await getAppointments();
            setAppointments(response.data);
        } catch(error) {
            console.error("Failed to fetch appointments:", error);
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm("Are you sure you want to delete this appointment?")) return;
        try {
            await deleteAppointment(id);
            loadAppointments();
        } catch (error) {
            console.error("Delete failed:", error);
        }
    };

    return (
        <div className="container mt-5">
            <h2>Appointments</h2>
            <button className="btn btn-success mb-3" onClick={() => navigate("/appointments/new")}> + New Appointment </button>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Patient</th>
                        <th>Doctor</th>
                        <th>Date & Time</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {AppointmentList.map((a) => (
                        <tr key={a.appointment_id}>
                            <td>{a.appointment_id}</td>
                            <td>{a.patient_name}</td>
                            <td>{a.doctor_name}</td>
                            <td>{new date(a.appointment_datetime).toLocaleString()}</td>
                            <td>{a.status}</td>
                            <td>
                                <button className="btn btn-primary btn-sm me-2" onClick={() => navigate(`/appointments/edit/${a.appointment_id}`)}>Edit</button>
                                <button className="btn btn-danger btn-sm" onClick={() => handleDelete(a.appointment_id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}