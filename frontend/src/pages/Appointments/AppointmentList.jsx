//src/pages/Appointments/AppointmentList.jsx 

import React, { useEffect, useState } from 'react';
import appointmentAPI from '../../api/appointmentAPI';
import AppointmentTable from '../../components/tables/AppointmentTable';
import Pagination from '../../components/ui/Pagination';
import SearchBar from '../../components/ui/SearchBar';

const AppointmentList = () => {
    const navigate = useNavigate();

    /* State for appointments data */
    const [appointments, setAppointments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [searchQuery, setSearchQuery] = useState(''); 
    const [statusFilter, setStatusFilter] = useState('all');
    const [dateFilter, setDateFilter] = useState(null);

    const AppointmentList = async () => {
        const navigate = useNavigate();

    /* State for appointments data */
    const [appointments, setAppointments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [filters, setFilters] = useState({
        status: "",
        doctor_id: "",
        patient_id: "",
        date_from: "",
        date_to: ""     
    });
    /* Fetch appointments from API */
    const fetchAppointments = async () => {
        setLoading(true);
        try {
            const response = await appointmentAPI.getAppointments({
                page: currentPage,
                search: searchQuery,
                filters: filters
            });

            setAppointments(response.data);
            setTotalPages(response.totalPages);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    useEffect(() => {
        fetchAppointments();
    }, [currentPage, searchQuery, filters]);

    /* Handlers */
    const handleAdd = () => {
        navigate('/appointments/add');
    };

    const handleEdit = (appointmentId) => {
        navigate(`/appointments/edit/${appointmentId}`);
    };

    const handleView = (appointmentId) => {
        navigate(`/appointments/view/${appointmentId}`);
    };
    const handleSearch = (query) => {
        setSearchQuery(query);
        setCurrentPage(1); 
    };
    const handleFilterChange = (newFilters) => {
        setFilters(newFilters);
        setCurrentPage(1);
    };
    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    return (
        <div>
            <h1>Appointment List</h1>
            <button onClick={handleAdd}>Add Appointment</button>    
            <SearchBar onSearch={handleSearch} />
            <FilterBar onFilterChange={handleFilterChange} />
            {loading ? (
                <p>Loading...</p>
            ) : error ? (
                <p>Error: {error}</p>
            ) : (
                <>
                    <AppointmentTable
                        appointments={appointments}
                        onEdit={handleEdit}
                        onView={handleView}
                    />
                    <Pagination
                        currentPage={currentPage}
                        totalPages={totalPages}
                        onPageChange={handlePageChange}
                    />
                </>
            )}
        </div>
    );
};

export default AppointmentList;

