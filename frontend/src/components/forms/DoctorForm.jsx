//src/components/forms/DoctorForm.jsx

import DoctorForm from '../components/forms/DoctorForm'
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import doctorAPI from '../../api/doctorAPI';
import { toast } from 'react-toastify';

const DoctorForm = () => {
    const { id } = useParams();
    const navigate = useNavigate(); 
    const [initialValues, setInitialValues] = useState({
        first_name: '',
        last_name: '',
        specialization: '',
        contact_number: '',
        email: '',
        notes: ''
    });
    useEffect(() => {
        if (id) {
            // Fetch existing doctor data for editing
            doctorAPI.getDoctorById(id)
                .then((data) => {
                    setInitialValues(data);
                })
                .catch((error) => {
                    toast.error('Error fetching doctor data');
                    console.error('Error fetching doctor data:', error);
                });
        }
    }, [id]);

    const handleSubmit = (values) => {
        if (id) {
            doctorAPI.updateDoctor(id, values)
                .then(() => {
                    toast.success('Doctor updated successfully');
                    navigate('/doctors');
                })
                .catch((error) => {
                    toast.error('Error updating doctor');
                    console.error('Error updating doctor:', error);
                });
        } else {
            doctorAPI.createDoctor(values)
                .then(() => {
                    toast.success('Doctor created successfully');
                    navigate('/doctors');
                })
                .catch((error) => {
                    toast.error('Error creating doctor');
                    console.error('Error creating doctor:', error);
                });
        }
    };

    return (
        <form className="doctor-form-container">
            <DoctorForm
                initialValues={initialValues}
                onSubmit={handleSubmit}
            />
        </form>
    );
};

export default DoctorForm;