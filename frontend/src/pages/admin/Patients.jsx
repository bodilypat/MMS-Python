// src/pages/admin/Patients.jsx 

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function Patients() {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        api.get("/admin/patients").then(res => setPatients(res.data));
    }, []);

    return (
        <div className="container">
            <h3>Patients</h3>
            <table className="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Gender</th>
                        <th>Email</th>
                        <th>Age</th>
                    </tr>
                </thead>
                <tbody>
                    {patients.map(patient => (
                        <tr key={patient.id}>
                            <td>{patient.name}</td>
                            <td>{patient.gender}</td>
                            <td>{patient.email}</td>
                            <td>{patient.age}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
