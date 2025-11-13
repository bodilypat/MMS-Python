//src/pages/Patients/PatientList.jsx

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    getPatient,
    deletePatient,
} from "../../services/patientService";
import Spinner from "../../components/common/Spinner";
import Table from "../../components/common/Table";
import ModalConfirm from "../../components/modals/ModalConfirm";
import { formatPhoneNumber } from "../../utils/formatters";

export default function PatientList() {
    const navigate = useNavigate();
    const [patients, setPatients] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedPatient, setSelectPatient] = useState(null);
    const [showDeleteModal, setShowDeleteModal] = useState(false);

    /* Fetch all patients on boad */
    useEffect(() => {
        fetchPatients();
    }, []);

    const fetchPatients = async () => {
        try {
            setLoading(true);
            const response = await getPatients();
            setPatients(response.data || []);
        } catch (error) {
            console.error("Error fetching patients:", error);
        } finally {
            setLoading(false);
        }
    };

    const handleAdd = () => navigate("/patients/new");
    const handleEdit = (patient) => navigate(`/patients/edit/${patient.id}`);

    const handleDelete = async () => {
        try {
            await deletePatient(selectedPatient.id);
            setShowDeleteModal(false);
            fetchPatients();
        } catch (error) {
            console.error("Error deleting patient:", error);
        }
    };

    if (loading) return <Spinner />;

    return (
        <div className="Container mt-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2 className="mb-0">Patients</h2>
                <button className="btn btn-primary" onClick={handleAdd}>+ Add Patient</button>
            </div>

            {patients.length === 0 ? (
                <p className="text-center mt-4">No patients found.</p>
            ) : (
                <Table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Gender</th>
                            <th>Age</th>
                            <th>Phone</th>
                            <th>Email</th>
                            <th>City</th>
                            <th className="text-center">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {patients.map((p) => (
                        <tr key={p.id}>
                            <td>{p.full_name}</td>
                            <td>{p.gender}</td>
                            <td>{p.age}</td>
                            <td>{formatPhoneNumber(p.phone)}</td>
                            <td>{p.email}</td>
                            <td>{p.city}</td>
                            <td className="text-center">
                                <button className="btn btn-sm btn-outline-secondary me-2" onClick={() => handleEdit(p)}>Edit</button>
                                <button className="btn bn-sm btn-outline-danger" onClick={() => {setSelectPatient(p); setShowDeleteModal(true); }}>Delete</button>
                            </td>
                        </tr>
                        ))}
                    </tbody>
                </Table>
            )}

            {/* Confirm Delete Modal */}
            {showDeleteModal && (
                <ModalConfirm 
                    title="Confirm Delete" 
                    message={`Are you sure you want to delete ${selectedPatient.full_name}?`} 
                    onConfirm={handleDelete}
                    onCancel={() => setShowDeleteModal(false)} />
            )}
        </div>
    );
}
