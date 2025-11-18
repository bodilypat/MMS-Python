//src/pages/Appointments/ViewAppointment.jsx 

import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import appointmentApi from "../../api/appointmentApi";
import { formatDateTime } from "../../utils/formatDateTime";

const ViewAppointment = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [appointment, setAppointment] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAppointment = async () => {
            try {
                const response = await appointmentApi.getAppointmentById(id);
                setAppointment(response.data);
            } catch (err) {
                setError("Failed to fetch appointment");
            } finally {
                setLoading(false);
            }
        };

        fetchAppointment();
    }, [id]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p style={{ color: "red" }}>{error}</p>;

    return (
        <div>
            <h2>View Appointment</h2>
            {appointment && (
                <div>
                    <p><strong>Patient:</strong> {appointment.patient?.name || "Unknown"}</p>
                    <p><strong>Doctor:</strong> {appointment.doctor?.name || "Unknown"}</p>
                    <p><strong>Date & Time:</strong> {formatDateTime(appointment.appointment_datetime)}</p>
                    <p><strong>Status:</strong> {appointment.status}</p>
                </div>
            )}
        </div>
    );
};

export default ViewAppointment;

