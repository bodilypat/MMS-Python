//src/pages/PrescriptionDetails.jsx

import React, { useEffect, useState } from 'react';
import prescriptionAPI from '../api/prescriptionAPI';
import PrescriptionTable from '../components/tables/prescriptionTable';
import '../assets/styles/variables.css';
import '../assets/styles/PrescriptionDetails.css';

const PrescriptionDetails = ({ prescriptionId }) => {
    const [prescription, setPrescription] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchPrescription = async () => {
            try {
                const data = await prescriptionAPI.getPrescriptionById(prescriptionId);
                setPrescription(data);
            } catch (err) {
                setError('Failed to load prescription data.');
            } finally {
                setLoading(false);
            }
        };
        fetchPrescription();
    }, [prescriptionId]);

    if (loading) return <div className="loading">Loading...</div>;

    if (error) return <div className="error">{error}</div>;

    if (!prescription) return <div className="not-found">Prescription not found.</div>;

    return (
        <div className="prescription-details">
            <h2>Prescription Details</h2>
            <PrescriptionTable data={prescription} />
        </div>
    );
};

export default PrescriptionDetails;
