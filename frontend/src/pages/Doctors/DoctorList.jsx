//src/pages/Doctors/DoctorList.jsx

import React, { useEffect, useState } from 'react';
import doctorApi from '../../api/doctorApi';
import SearchBar from '../../components/ui/SearchBar';
import DoctorTable from '../../components/tables/DoctorTable';
import Pagination from '../../components/ui/Pagination';
import { useNavigate } from 'react-router-dom';

const DoctorList = () => {
    const [doctors, setDoctors] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const pageSize = 10;

    const fetchDoctors = async (page, query) => {
        setLoading(true);
        try {
            const response = await doctorApi.getDoctors({ page, pageSize, search: query });
            setDoctors(response.data.doctors);
            setTotalPages(response.data.totalPages);
        } catch (error) {
            console.error('Error fetching doctors:', error);
        } finally {
            setLoading(false);
        }
    };
    useEffect(() => {
        fetchDoctors(currentPage, searchQuery);
        }, [currentPage, searchQuery]);

    const handleSearch = (query) => {
        setSearchQuery(query);
        setCurrentPage(1); // Reset to first page on new search
    };

    const handleRowClick = (doctorId) => {
        navigate(`/doctors/${doctorId}`);
    };

    return (    
        <div>
            <h1 className="text-2xl font-bold mb-4">Doctors</h1>
            <SearchBar placeholder="Search doctors..." onSearch={handleSearch} />
            <DoctorTable doctors={doctors} onRowClick={handleRowClick} loading={loading} />
            <Pagination
                currentPage={currentPage}
                totalPages={totalPages}
                onPageChange={setCurrentPage}
            />
        </div>
    );
};

export default DoctorList;

