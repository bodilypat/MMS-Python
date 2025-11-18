//scr/pages/Appointments/AddAppointment.jsx

import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import appointmentAPI from "../../api/appointmentAPI";
import patientAPI from "../../api/patientAPI";
import doctorAPI from "../../api/doctorAPI";
import AppointmentForm from "../../components/forms/AppointmentForm";

const AddAppointment = () => {
    const navigate = useNavigate();
    const [patients, setPatients] = useState([]);
    const [doctors, setDoctors] = useState([]);
    const [error, setError] = useState(null);

    /* Fetch patients and doctors */
    useEffect(() => {
        const fetchPatients = async () => {
            try {
                const response = await patientAPI.getPatients();
                setPatients(response.data);
            } catch (err) {
                setError("Failed to fetch patients");
            }
        };

        const fetchDoctors = async () => {
            try {
                const response = await doctorAPI.getDoctors();
                setDoctors(response.data);
            } catch (err) {
                setError("Failed to fetch doctors");
            }
        };

        fetchPatients();
        fetchDoctors();
    }, []);

    /* Submit handler */
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const appointmentData = {
            patient_id: formData.get("patient_id"),
            doctor_id: formData.get("doctor_id"),
            appointment_datetime: formData.get("appointment_datetime"),
            status: formData.get("status")
        };

        try {
            await appointmentAPI.createAppointment(appointmentData);
            navigate("/appointments");
        } catch (err) {
            setError("Failed to create appointment");
        }
    };
    const handleChange = (key, value) => {
        setFormData(prev => ({
            ...prev,
            [key]: value
        }));
    };

    return (
        <div>
            <h2>Add Appointment</h2>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <AppointmentForm
                patients={patients}
                doctors={doctors}
                onSubmit={handleSubmit}
            />
        </div>
    );
};

export default AddAppointment;