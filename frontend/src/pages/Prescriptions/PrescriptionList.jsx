//src/pages/Prescription/PrescriptionList.jsx

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import prescriptionAPI from '../../api/prescriptionAPI';
import PrescriptionTable from '../../components/tables/prescriptionTable';
import PrescriptionForm from '../../components/forms/prescriptionForm';

const PrescriptionList = () => {
    const { patientId } = useParams();
    const [prescriptions, setPrescriptions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPrescriptions = async () => {
            try {
                const response = await prescriptionAPI.getPrescriptionsByPatientId(patientId);
                setPrescriptions(response.data);
            } catch (err) {
                setError('Failed to fetch prescriptions.');
            } finally {
                setLoading(false);
            }
        };
        fetchPrescriptions();
    }, [patientId]);
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (
        <div>
            <PrescriptionForm patientId={patientId} />
            <PrescriptionTable prescriptions={prescriptions} />
        </div>
    );
};
