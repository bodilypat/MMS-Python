//src/pages/Patients/PatientList.jsx

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import patientApi from '../../api/patientApi';
import PatientTable from '../../components/tables/PatientTable';
import SearchBar from '../../components/ui/SearchBar';
import Pagination from '../../components/ui/Pagination';

const PatientList = () => {
    const [patients, setPatients] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const navigate = useNavigate();
    const pageSize = 10;

    const fetchPatients = async (page, query) => {
        setLoading(true);
        try {
            const response = await patientApi.getPatients({ page, pageSize, query });
            setPatients(response.data.patients);
            setTotalPages(response.data.totalPages);
        } catch (error) {
            console.error('Error fetching patients:', error);
        } finally {
            setLoading(false);
        }
    };
    useEffect(() => {
        fetchPatients(currentPage, searchQuery);
    }, [currentPage, searchQuery]);

    const handleSearch = (query) => {
        setSearchQuery(query);
        setCurrentPage(1);
    };
    const handleRowClick = (patientId) => {
        navigate(`/patients/${patientId}`);
    };
    return (
        <div>
            <h1>Patient List</h1>
            <SearchBar onSearch={handleSearch} />
            <PatientTable
                patients={patients}
                loading={loading}
                onRowClick={handleRowClick}
            />
            <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPageChange={setCurrentPage}
            />
        </div>
    );
};

export default PatientList;