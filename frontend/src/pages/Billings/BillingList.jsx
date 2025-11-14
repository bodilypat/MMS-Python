//src/pages/Billings/BillingList.jsx 

import React, { useEffect, useState } from 'react';
import {
    getAllBillings,
    deleteBilling,
} from './billing.api';
import './BillingList.css';

const BillingList = ({ onViewReceipt }) => {
    const [billings, setBillings] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const [search, setSearch] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 8;

    /* Fetch data */
    const fetchBillings = async () => {
        try {
            setLoading(true);
            const response = await getAllBillings();
            setBillings(response.data);
        } catch (error) {
            console.error('Error fetching billings:', error);
            setError('Failed to load billings.');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchBillings();
    }, []);

    /* Search and Filter */
    const filteredBillings = billings.filter((billing) =>
        billing.patient_id.toString().includes(search) ||
        billing.status.toLowerCase().includes(search.toLowerCase())
    );

    /* Pagination logic */
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentBillings = filteredBillings.slice(indexOfFirstItem, indexOfLastItem);
    const totalPages = Math.ceil(filteredBillings.length / itemsPerPage);

    /* Delete a record */
    const handleDelete = async (BillingListd) => {
        if (window.confirm('Are you sure you want to delete this billing record?')) {
            try {
                await deleteBilling(billingId);
                fetchBillings(); // Refresh the list after deletion
            } catch (error) {
                console.error('Error deleting billing:', error);
                setError('Failed to delete billing.');
            }
        };

        if (loading) return <p className="loading">loading billings...</p>;
        if (error) return <p className="error">{error}</p>;

        return (
            <div className="billing-list">
                <h2>Billing Records</h2>
                {/* Search Box */}
                <input 
                    type="text"
                    className="search-box"
                    placeholder="Search by Patient ID or status..."
                    value={search}
                    onChange{(e) => setSearch(e.target.value)}
                />
                {/* Billing Table */}
                <table className="billing-table">
                <thead>
                    <tr>
                        <th>Billing ID</th>
                        <th>Patient ID</th>
                        <th>Doctor ID</th>
                        <th>Amount</th>
                        <th>Date</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {currentItems.length ===0 ? (
                        <tr>
                            <td colSpan="7" className="no-data">No matching records found.</td>
                    ) : (
                        currentItems.map((bill) => (
                            <tr key={bill.billing_id}>
                                <td>{bill.billing_id}</td>
                                <td>{bill.patient_id}</td>
                                <td>{bill.doctor_id}</td>
                                <td>${Number(bill.amount).toFixed(2)}</td>
                                <td>{new Date(bill.billing_date).toLocaleDateString()}</td>
                                <td><span className={`status-badge ${bill.status.toLowerCase()}`}>
                                    {bill.status}
                                    </span>
                                </td>
                                <td className="actions">
                                    <button className="btn-view" onClick={() => onViewReceipt(bill.billing_id)}>View Receipt</button>
                                    <button onClick={() => handleDelete(bill.billing_id)}>Delete</button>
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
                    
            {/* Pagination Controls */}
            <div className="pagination">
                    <button disabled={currentPage === 1} onClick={() => setCurrentPage((prev) => prev - 1)}>Previous</button>
                    <span>Page {currentPage} of {totalPages}</span>
                    <button disabled={currentPage === totalPages} onClick={() => setCurrentPage((prev) => prev + 1)}>Next</button>
            </div>
        </div>
        );
    };

    export default BillingList;