// src/pages/admin/Appointments.jsx

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Appointments() {
    const [data, setData] = useState([]);

    useEffect(() => {
        api.get("/admin/appointments").then(res => setData(res.data));
    }, []);

    return (
        <div className="container">
            <h3>Appointments</h3>
            <table className="table">
                <thead>
                    <tr>
                        <th>Patient Name</th>
                        <th>Doctor Name</th>
                        <th>Date</th>
                        <th>Time</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(appointment => (
                        <tr key={appointment.id}>
                            <td>{appointment.patient_name}</td>
                            <td>{appointment.doctor_name}</td>
                            <td>{appointment.date}</td>
                            <td>{appointment.time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

