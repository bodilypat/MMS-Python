//src/pages/Doctors/DoctorDetails.jsx 

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import DoctorAPI from '../../api/DoctorAPI';
import DoctorForm from '../../components/forms/DoctorForm';
import DoctorTable from '../../components/tables/DoctorTable';
import LoadingSpinner from '../../components/LoadingSpinner';
import Notification from '../../components/Notification';

const DoctorDetails = () => {
    const { doctorId } = useParams();
    const navigate = useNavigate();
    const [doctor, setDoctor] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    useEffect(() => {
        const fetchDoctor = async () => {
            try {
                const response = await DoctorAPI.getDoctorById(doctorId);
                setDoctor(response.data);
                setLoading(false);
            } catch (err) {
                setError('Failed to fetch doctor details.');
                setLoading(false);
            }
        };
        fetchDoctor();
    }, [doctorId]);

    const handleUpdate = async (updatedData) => {
        try {
            await DoctorAPI.updateDoctor(doctorId, updatedData);
            setSuccessMessage('Doctor details updated successfully.');
            // Refresh doctor details
            const response = await DoctorAPI.getDoctorById(doctorId);
            setDoctor(response.data);
        } catch (err) {
            setError('Failed to update doctor details.');
        }
    };
    const handleDelete = async () => {
        try {
            await DoctorAPI.deleteDoctor(doctorId);
            setSuccessMessage('Doctor deleted successfully.');
            navigate('/doctors');
        } catch (err) {
            setError('Failed to delete doctor.');
        }
    };

    if (loading) return <LoadingSpinner />;
    if (error) return <Notification type="error" message={error} />;

    return (
        <div>
            {successMessage && <Notification type="success" message={successMessage} />}
            <h2>Doctor Details</h2>
            <DoctorForm doctor={doctor} onSubmit={handleUpdate} onDelete={handleDelete} />
            <h3>All Doctors</h3>
            <DoctorTable />
        </div>
    );
};

export default DoctorDetails;

            