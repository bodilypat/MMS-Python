//src/pages/Patients/AddPatient.jsx 

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import patientAPI from '../../api/patientAPI';
import PatientForm from '../../components/forms/PatientForm';
import { toast } from 'react-toastify';

const AddPatient = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleAddPatient = async (patientData) => {   
        setLoading(true);
        setError(null);
        try {
            await patientAPI.addPatient(patientData);
            toast.success('Patient added successfully!');
            navigate('/patients');
        } catch (err) {
            setError(err.response?.data?.message || 'Failed to add patient.');
            toast.error('Failed to add patient.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Add New Patient</h2>
            {error && <div className="error">{error}</div>}
            <PatientForm onSubmit={handleAddPatient} loading={loading} />
        </div>
    );
};

export default AddPatient;
