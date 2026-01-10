//src/pages/patient/Appointments.jsx 

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Appointments() {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        api.get('/api/patient/appointments').then(res => setAppointments(res.data));
    }, []);

    return (
        <div className="container">
            <h1>My Appointments</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Doctor</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {appointments.map(appointment => (
                        <tr key={appointment.id}>
                            <td>{appointment.doctor.name}</td>
                            <td>{appointment.date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}


