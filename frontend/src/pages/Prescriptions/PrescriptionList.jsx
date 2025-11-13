//src/pages/Prescriptions/PrescriptionList.jsx

import React, { useEffect, useState } from 'react';
import { fetchPrescriptions, deletePrescription } from  './prescription.api';
import precriptionForm from './PrescriptionForm';
import Spinner from '../../components/common/Spinner';
import Toast from '../../components/Notification/Toast';
import ModalConfirm from '../../components/modals/ModalConfirm';
import Pagination from '../../components/common/Pagination';
import Button from '../../components/common/Button';
import Table from '../../components/common/Table';

const PrescriptionList = () => {
    const [prescriptions, setPrescriptions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedPrescription, setSelectedPrescription] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const [confirmDelete, setShowConfirmDelete] = useState({ open: false, id: null });
    const [filter, setFilter] = useState({ search: "", status: ""});

    /*  Fetch all prescriptions */
    const loadPrescriptions = async () => {
        setLoading(true);
        try {
            const response = await fetchPrescriptions({
                search: filter.search,
                status: filter.status,
            });
            setPrescriptions(response.data);
        } catch (error) {
            console.error("Error fetching prescriptions:", error);
            Toast.error("Failed to load prescriptions.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadPrescriptions();
    }, [filter]);

    /*  Handle delete prescription */
    const handleDelete = async (id) => {
        try {
            await deletePrescription(id);
            setPrescriptions(prescriptions.filter(prescription => prescription.id !== id));
            Toast.success("Prescription deleted successfully.");
        } catch (error) {
            console.error("Error deleting prescription:", error);
            Toast.error("Failed to delete prescription.");
        } finally {
            setShowConfirmDelete({ open: false, id: null });
        }
    };

    /*  Handle edit prescription */
    const handleEdit = (prescription) => {
        setSelectedPrescription(prescription);
        setShowForm(true);
    };

    /* Handle new prescription */
    const handleAddNew = () => {
        setSelectedPrescription(null);
        setShowForm(true);
    };

    /* Refresh after form submission */
    const handleFormSuccess = () => {
        setShowForm(false);
        loadPrescriptions();
    };

    const handleSearchChange = (e) => {
        setFilter({ ...filter, search: e.target.value });
    };

    const handleStatusChange = (e) => {
        setFilter({ ...filter, status: e.target.value });
    };  

    if (loading) return <Spinner message="Loading prescriptions..." />;

    return (
        <div className="prescription-list container mx-auto p-4">
            <div className="header flex justify-between items-center mb-4">
                <h1 className="text-2xl font-bold">Prescriptions</h1>
                <Button onClick={handleAddNew} className="bg-blue-500 text-white px-4 py-2 rounded">
                    Add New Prescription
                </Button>
            </div>
            /* Filter & Search bar */
            <div className="filters mb-4 flex space-x-4">
                <input
                    type="text"
                    placeholder="Search prescriptions..."
                    value={filter.search}
                    onChange={handleSearchChange}
                    className="border rounded px-3 py-2 w-1/3"
                />
                <select
                    value={filter.status}
                    onChange={handleStatusChange}
                    className="border rounded px-3 py-2"
                >
                    <option value="">All Statuses</option>
                    <option value="Active">Active</option>
                    <option value="Completed">Completed</option>
                    <option value="Expired">Expired</option>
                    <option value="Cancelled">Cancelled</option>
                </select>
            </div>

            /* Table of prescriptions */
            {prescriptions.length === 0 ? (
                <p className="text-center text-gray-500">No prescriptions found.</p>
    
            ) : (
                <Table>
                    <thead>
                        <tr>
                            <th>Patient Name</th>
                            <th>Medication</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {prescriptions.map((prescription) => (
                            <tr key={prescription.id}>
                                <td>{prescription.patient_name}</td>                        
                                <td>{prescription.medication}</td>
                                <td>{prescription.status}</td>
                                <td>
                                    <Button onClick={() => handleEdit(prescription)} className="bg-yellow-500 text-white px-3 py-1 rounded mr-2">
                                        Edit
                                    </Button>
                                    <Button onClick={() => setShowConfirmDelete({ open: true, id: prescription.id })} className="bg-red-500 text-white px-3 py-1 rounded">
                                        Delete
                                    </Button>
                                </td>   
                            </tr>
                        ))}
                    </tbody>
                </Table>
            )}  

            {/* ModalConfirm for Delete */}
            {confirmDelete.open && (
                <ModalConfirm
                    title="Confirm Delete"
                    message="Are you sure you want to delete this prescription?"
                    onConfirm={() => handleDelete(confirmDelete.id)}
                    onCancel={() => setShowConfirmDelete({ open: false, id: null })}
                />
            )}

            {/* Prescription Form Modal (Add/Edit) */}
            {showForm && (
                <div className="modal fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <div className="modal-content bg-white p-6 rounded shadow-lg w-1/2">
                        <precriptionForm    
                            prescription={selectedPrescription}
                            onSuccess={handleFormSuccess}
                            onCancel={() => setShowForm(false)} 
                        />
                        <div className="modal-actions mt-4 text-right">
                            <Button onClick={() => setShowForm(false)} className="bg-gray-500 text-white px-4 py-2 rounded">
                                Close           
                            </Button>
                        </div>
                    </div>      
                </div>
            )}
        </div>
    );
};

export default PrescriptionList;