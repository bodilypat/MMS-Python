// src/pages/patient/MedicalHistory.jsx

import { useEffect, useState } from "react";
import api from "../../services/api";

export default function MedicalHistory() {
    const [history, setHistory] = useState([]);

    useEffect(() => {
        api.get('/api/patient/medical-history').then(res => setHistory(res.data));
    }, []);

    return (
        <div className="container">

            <h1>My Medical History</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Diasnosis</th>
                        <th>Treatment</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {history.map( h => (
                        <tr key={h.id}>
                            <td>{h.diagnosis}</td>
                            <td>{h.treatment}</td>
                            <td>{h.visitDate}</td>
                            <td>{h.notes}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

