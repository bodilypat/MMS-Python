//src/pages/Doctors/EditDoctor.jsx

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import doctorApi from '../../api/doctorApi';
import DoctorForm from '../../components/forms/DoctorForm';

const EditDoctor = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [doctor, setDoctor] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [fetching, setFetching] = useState(false);

    useEffect(() => {
        const fetchDoctor = async () => {
            setFetching(true);
            try {
                const response = await doctorApi.getDoctorById(id);
                setDoctor(response.data);
                setLoading(false);
            } catch (err) {
                setError('Failed to fetch doctor data.');
                setLoading(false);
            }
            setFetching(false);
        };
        fetchDoctor();
    }, [id]);

    const handleSubmit = async (updatedDoctor) => {
        try {
            await doctorApi.updateDoctor(id, updatedDoctor);
            navigate('/doctors');
        } catch (err) {
            setError('Failed to update doctor data.');
        }
    };
    if (loading || fetching) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (
        <div>
            <h2>Edit Doctor</h2>
            <DoctorForm initialData={doctor} onSubmit={handleSubmit} />
        </div>
    );
}

export default EditDoctor;


