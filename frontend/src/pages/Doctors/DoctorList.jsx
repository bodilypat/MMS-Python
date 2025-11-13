//src/pages/Doctors/DoctorList.jsx
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { doctorApi } from "./doctor.api";

export default function DoctorList() {
    const navigate = useNavigate();
    const [doctors, setDoctors] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    /* Fetch doctors on mount */

    useEffect(() => {
        const fetchDoctors = async () => {
            try {
                const response = await doctorApi.getAll();
                setDoctors(response.data || []);
            } catch (error) {
                console.error("Error fetching doctors", error);
                setError("Failedto load doctors.");
            } finally {
                setLoading(false);
            }
        };

        fetchDoctors();
    }, []);

    /* Handle delete */
    const handleDelete = async (id) => {
        if (!window.confirm("Are you sure you want to delete this doctor?")) return;

        try {
            await doctorApi.delete(id);
            setDoctors((prev) => prev.filter((d) => d.doctor.id !== id));
        } catch (error) {
            console.error("Error deleting doctor:", error);
            alert("Failed to delete doctor.");
        }
    };

    if (loading) return <div className="text-conter mt-5">Loading doctors...</div>
    if (error) return <div className="text-danger text-center mt-5">{error}</div>;

    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2>Doctor</h2>
                <button className="btn btn-success" onClick={() => navigate("/doctors/new")}> + Add Doctor</button>
            </div>

            {doctors.length ===0 ? (
                <p className="text-center">No doctors found.</p>
            ) : (
                <div className="table-responsive">
                    <table className="table table-striped table-bordered">
                        <thead className="table-light">
                            <tr>
                                <td>ID</td>
                                <td>Full Name</td>
                                <td>Specialization</td>
                                <td>Email</td>
                                <td>Contact</td>
                                <td>Status</td>
                                <td>Actions</td>
                            </tr>
                        </thead>
                        <tbody>
                        {doctors.map((doctor) => (
                            <tr key={doctor.doctor_id}>
                                <td>{doctor.doctor_id}</td>
                                <td>{doctor.first_name}</td>
                                <td>{doctor.last_name}</td>
                                <td>{doctor.specialization}</td>
                                <td>{doctor.email}</td>
                                <td>{doctor.contact_number || "-"}</td>
                                <td>
                                    <span className={`badge ${ doctor.status === "active" ? "bg-success" : "bg-secondary" }`} >{doctor.status || "unknow"} </span>
                                </td>
                                <td>
                                    <button className="btn btn-sm btn-primary me-2" onClick={() => navigate(`/doctors/edit/${doctor.doctor_id}`)}>Edit</button>
                                    <button className="btn btn-danger" onClick={() => handleDelete(doctor.doctor_id)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
