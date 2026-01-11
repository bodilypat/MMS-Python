// src/pages/patient/BookAppointment.jsx  

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function BookAppointment() {
    const [doctors, setDoctors] = useState([]);
    const [form, setForm] = useState({});


    useEffect(() => {
        api.get('/api/doctors').then(res => setDoctors(res.data));
    }, []);

    const submit = async (e) => {
        e.preventDefault();
        await api.post('/api/patient/book-appointment', form);
        alert("Appointment booked successfully!");
        setForm({});
    };

    return (
        <form onSubmit={submit} className="container">
            <h1>Book Appointment</h1>
            <select className="form-control mb-3" 
                onChange={e => setForm({...form, doctor: e.target.value})}>
                    <option>Select Doctor</option>
                    {doctors.map(doctor => (
                        <option key={doctor.id} value={doctor.id}>{doctor.name}</option>
                    ))}
                </select>
            <input type="date" className="form-control mb-3" 
                name="date" value={form.date || ''} onChange={(e) => setForm({...form, date: e.target.value})} required />
            <button type="submit" className="btn btn-primary">Book Appointment</button>
        </form>
    );
}