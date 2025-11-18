//src/pages/Appointments/BookAppointment.jsx

import React, { useEffect, useState } from "react";
import appointmentApi from "../../api/appointmentApi";
import doctorApi from "../../api/DoctorApi";
import patientApi from "../../api/patientApi";
import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";
import Loader from "../../components/common/Loader";
import { useNavigate } from "react-router-dom";

const BookAppointment = () => {
    const navigate = useNavigate();

    const [patients, setPatients] = useState([]);
    const [doctors, setDoctors] = useState([]);

    const [form, setForm] = useState({
        patient_id: "",
        doctor_id: "",
        appointment_datetime: "Consulation",
        reason_for_visit: "",
        duration_minutes: 30,
        notes: "",
    });

    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchInitialData();
    }, []);

    const fetchInitialData = async () => {
        try {
            const [patientsRes, DoctorsRes] = await Promise.all([
                patientApi.getAllPatients(),
                doctorApi.getAllDoctors(),
            ]);

            setPatients(patientsRes.data);
            setDoctors(DoctorsRes.data);
        } catch (err) {
            console.error("Failed to load form data", err);
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (e) => 
        setForm({ ...form, [e.target.name]: e.target.value });

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await appointmentApi.CreateAppointment(form);
            navigate('/appointments');
        } catch (err) {
            console.error("Failed to create appointment", err);
        }
    };

    if (loading) return <Loader fullscreen />

    return (
        <div className="apt-container">
            <Card header="Book Appointment">
                <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* Patient */}
                    <div>
                        <label>Patient</label>
                        <select 
                            required 
                            name="patient_id"
                            className="border p-2 rounded w-full"
                            onChange={handlechange}
                        >
                            <option value="">Select Patient</option>
                            {patients.map((p) => (
                                <option key={p.patient_id} value={p.patient_id}>
                                    {p.first_name} {p.last_name}
                                </option>
                            ))}
                        </select>
                    </div>

                    {/* Doctor */}
                    <div>
                        <label>Doctor</label>
                        <select 
                            required
                            name="doctor_id"
                            className="border p-2 rounded w-full"
                        >
                            <option value="">Select Doctor</option>
                            {doctors.map((d) => (
                                <option key={d.doctor_id} value={d.doctor_id}>
                                    {d.first_name} {d.last_name} - {d.specializaton}
                                </option>
                            ))}
                        </select>
                    </div>

                    {/* Date Time */}
                    <div>
                        <label>Appointment Date/Time</label>
                        <input  
                            type="datetime- local"
                            name="appointment_datetime"
                            required 
                            className="border p-2 rounded w-full"
                            onChange={handleChange}
                        />
                    </div>
                    {/* Appointment Type */}
                    <div>
                        <label>Type</label>
                        <select 
                            name="appointment_type"
                            className="border p-2 rounded w-ful"
                            onchange={handleChange}
                        >
                            <option>Consulation</option>
                            <option>Follow-up</option>
                            <option>Emergency</option>
                            <optional>Routine Checkup</optional>
                        </select>
                    </div>
                    {/* Reason */}
                    <div className="md:col-span-2">
                        <label>Reason for visit</label>
                        <input  
                            type="text"
                            name="reason_for_visit"
                            className="border p-2 rounded w-full"
                            onChange={handlechange}
                        />
                    </div>
                    {/* Duration */}
                    <div>
                        <label>Duration (minute)</label>
                        <input  
                            type="number"
                            name="5"
                            className="border p-2 rounded w-full"
                            onChange={handleChange}
                            value={form.duration_minutes}
                        />
                    </div>
                    {/* Notes */}
                    <div className="md:col-span-2">
                        <label>Note</label>
                        <textarea 
                            name="notes"
                            rows="3"
                            className="border p-2 rounded w-full"
                            onChange={hadleChange}
                        ></textarea>
                    </div>
                    {/* Submit */}
                    <div className="md:col-span-2 flex justify-end">
                        <button type="submit">Book Appointmet</button>
                    </div>
                </form>
            </Card>
        </div>
    );
};

export default BookAppointment;

