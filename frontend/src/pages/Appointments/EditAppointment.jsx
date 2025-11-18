//src/pages/Appointments/EditAppointment.js 

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import AppointmentForm from '../../components/forms/AppointmentForm';
import appointmentAPI from '../../api/appointmentAPI';
import patientAPI from '../../api/patientAPI';
import doctorAPI from '../../api/doctorAPI';

const EditAppointment = () => {
    const { id } = useParams();
    const navigate = useNavigate(); 
    const [appointment, setAppointment] = useState(null);
    const [patients, setPatients] = useState([]);
    const [doctors, setDoctors] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    /* Load initial data */
    useEffect(() => {
        const fetchData = async () => {
            try {
                const [appointmentRes, patientsRes, doctorsRes] = await Promise.all([
                    appointmentAPI.getAppointmentById(id),
                    patientAPI.getPatients(),
                    doctorAPI.getDoctors()
                ]);
                setAppointment(appointmentRes.data);
                setPatients(patientsRes.data);
                setDoctors(doctorsRes.data);
            } catch (err) {
                setError("Failed to fetch data");
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [id]);
    
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
            await appointmentAPI.updateAppointment(id, appointmentData);
            navigate("/appointments");
        } catch (err) {
            setError("Failed to update appointment");
        }
    };
    

    if (loading) return <p>Loading...</p>;
    if (error) return <p style={{ color: "red" }}>{error}</p>;

    return (
        <div>
            <h2>Edit Appointment</h2>
            {appointment && (
                <AppointmentForm
                    patients={patients}
                    doctors={doctors}
                    initialData={appointment}
                    onSubmit={handleSubmit}
                />
            )}
        </div>
    );
};

export default EditAppointment;