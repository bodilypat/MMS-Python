//src/pages/Doctors/AddDoctor.jsx

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import doctorApi from '../../api/doctorApi';
import DoctorForm from '../../components/forms/DoctorForm';
import DoctorTable from '../../components/tables/DoctorTable';

const AddDoctor = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [doctorData, setDoctorData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        specialization: '',
        experience: '',
    });
    const handleChange = (e) => {
        const { name, value } = e.target;
        setDoctorData({ ...doctorData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await doctorApi.addDoctor(doctorData);
            navigate('/doctors');
        } catch (error) {
            console.error('Error adding doctor:', error);
        }
    };
    return (
        <div>
            <h2>Add New Doctor</h2>
            <DoctorForm
                doctorData={doctorData}
                loading={loading}
                handleChange={handleChange}
                handleSubmit={handleSubmit}
            />
            <h3>Existing Doctors</h3>
            <DoctorTable />
        </div>
    );
};


            