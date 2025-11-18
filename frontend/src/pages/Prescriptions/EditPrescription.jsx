//src/pages/Prescription/EditPrescription.jsx

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import prescriptionAPI from '../../api/prescriptionAPI';
import PrescriptionForm from '../../components/forms/PrescriptionForm';
import LoadingSpinner from '../../components/common/LoadingSpinner';
import Notification from '../../components/common/Notification';
import '../../assets/styles/form.css';

const EditPrescription = () => {
    const { id } = useParams();
    const [prescription, setPrescription] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    useEffect(() => {
        const fetchPrescription = async () => {
            try {
                const data = await prescriptionAPI.getPrescriptionById(id);
                setPrescription(data);
            } catch (err) {
                setError('Failed to load prescription data.');
            } finally {
                setLoading(false);
            }
        };
        fetchPrescription();
    }, [id]);
    
    if (loading) return <LoadingSpinner />;

    if (error) return <Notification type="error" message={error} />;

    if (!prescription) return <Notification type="error" message="Prescription not found." />;

    const handleUpdate = async (updatedData) => {
        try {
            await prescriptionAPI.updatePrescription(id, updatedData);
            setSuccessMessage('Prescription updated successfully.');
        } catch (err) {
            setError('Failed to update prescription.');
        }
    };

    return (
        <div className="form-container">

            {successMessage && <Notification type="success" message={successMessage} />}
            {error && <Notification type="error" message={error} />}
            <h2>Edit Prescription</h2>
            <PrescriptionForm initialData={prescription} onSubmit={handleUpdate} />
        </div>
    );
};

export default EditPrescription;

