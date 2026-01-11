// src/pages/admin/Doctors.jsx 

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Doctors() {
    const [doctors, setDoctors] = useState([]);

    useEffect(() => {
        api.get("/admin/doctors").then(res => setDoctors(res.data));
    }, []);

    const remove = async (id) => {
        await api.delete(`/admin/doctors/${id}`);
        setDoctors(doctors.filter(d => d.id !== id));   
    };

    return (
        <div className="container">
            <h2>Doctors</h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Specialization</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {doctors.map(doctor => (
                        <tr key={doctor.id}>
                            <td>{doctor.name}</td>
                            <td>{doctor.email}</td>
                            <td>{doctor.specialization}</td>
                            <td>
                                <button className="btn btn-danger" onClick={() => remove(doctor.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

