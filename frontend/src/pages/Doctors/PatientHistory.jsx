//src/pages/doctor/PatientHistory.jsx

import { useState, useEffect } from "react";
import Table from "../../components/patient/Table";
import SearchBar from "../../components/patient/SearchBar";
import Loader from "../../components/common/Loader";
import EmptyState from "../../components/common/EmptyState";
import doctorServices from "../../services/doctorServices";

/* Display list of patients previously treated */
/* Show visit count & last visit */
/* Search & pagination ready */
/* Loading & empty states */
/* Service-based data fetching */

import { useEffect, useState } from "react";
import Table from "../../components/patient/Table";
import SearchBar from "../../components/patient/SearchBar";
import Loader from "../../components/common/Loader";
import EmptyState from "../../components/common/EmptyState";
import doctorServices from "../../services/doctorServices";

const PatientHistory = () => {
    const [patients, setPatients] = useState([]);
    const [filteredPatients, setFilteredPatients] = useState([]);
    const [loading, setLoading] = useState(true);
    const [search,setSearch] = useState("");

    useEffect(() => {
        const fetchHistory = async () => {
            try {
                const response = await doctorServices.getPatientHistory();
                setPatients(response.data);
                setFilteredPatients(response.data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching patient history:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchHistory();
    }, []);

    const handleSearch = (query) => {
        setSearch(query);
        if (!query) {
            setFilteredPatients(patients);
            return;
        }
        const filtered = patients.filter((patient) =>
            patient.name.toLowerCase().includes(query.toLowerCase())
        );
        setFilteredPatients(filtered);
    };

    useEffect(() => {
        const result = patients.filter((patient) =>
            patient.name.toLowerCase().includes(search.toLowerCase())
        );
        setFilteredPatients(result);
    }
    , [search, patients]);

    if (loading) {
        return <Loader />;
    }
    if (filteredPatients.length === 0) {
        return <EmptyState message="No patient history found." />;
    }


    const columns = [
        { header: "Patient Name", accessor: "name" },
        { header: "Visit Count", accessor: "visitCount" },
        { header: "Last Visit", accessor: "lastVisit" },
    ];

    return (
        <>
            <h1 className="mainTitle">Patient History</h1>
            {/* Search Bar */}
            <div className="row mb-3">
                <div className="col-md-4">
                    <SearchBar
                        placeholder="Search patients..."
                        value={search}
                        onChange={handleSearch}
                    />
                </div>
            </div>
            {/* Patient Table */}
            <Table columns={columns} data={filteredPatients} />
        </>
    );
};
export default PatientHistory;

