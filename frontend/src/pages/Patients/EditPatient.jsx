//src/pages/Patients/EditPatient.jsx 

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import pateintAPI from '../../api/patientAPI';
import PatientForm from '../../components/PatientForm';

const EditPatient = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [patient, setPatient] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchPatient = async () => {
            try {
                const data = await patientAPI.getPatientById(id);
                setPatient(data);
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to fetch patient.');
            } finally {
                setLoading(false);
            }
        };

        fetchPatient();
    }, [id]);

    const handleUpdate = async (updatedData) => {
        try {
            await patientAPI.updatePatient(id, updatedData);    
            navigate(`/patients/${id}`);
        } catch (err) {
            setError(err.response?.data?.message || 'Failed to update patient.');
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div className="error">{error}</div>;

    return (
        <div>
            <h2>Edit Patient</h2>
            {patient && <PatientForm initialData={patient} onSubmit={handleUpdate} />}
        </div>
    );
};

export default EditPatient;