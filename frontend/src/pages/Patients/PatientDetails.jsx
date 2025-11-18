//src/pages/Patients/PatientDetails.jsx 

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import patientApi from '../../api/patientApi';
import PatientForm from '../../components/PatientForm';
import PatientTable from '../../components/PatientTable';
import LoadingSpinner from '../../components/LoadingSpinner';
import Notification from '../../components/Notification';

const PatientDetails = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [patient, setPatient] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    useEffect(() => {   
        const fetchPatient = async () => {
            try {
                const response = await patientApi.getPatientById(id);
                setPatient(response.data);
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to fetch patient.');
            } finally {
                setLoading(false);
            }
        };

        fetchPatient();
    }, [id]);

    const handleDelete = async () => {
        try {
            await patientApi.deletePatient(id);
            setSuccessMessage('Patient deleted successfully.');
            setTimeout(() => navigate('/patients'), 2000);
        } catch (err) {
            setError(err.response?.data?.message || 'Failed to delete patient.');
        }
    };

    if (loading) return <LoadingSpinner />;
    if (error) return <Notification type="error" message={error} />;

    return (
        <div className="patient-container">
            <h2>Patient Details</h2>
            {patient && (
                <div>
                    <PatientForm initialData={patient} isViewOnly={true} />
                    <button onClick={handleDelete}>Delete Patient</button>
                </div>
            )}
            {successMessage && <Notification type="success" message={successMessage} />}
        </div>
    );
};

export default PatientDetails;