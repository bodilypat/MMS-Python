//src/pages/billing/ViewBilling.jsx 

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import billingApi from '../../api/billingApi';

const ViewBilling = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [billing, setBilling] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchBilling = async () => {
            try {
                const data = await billingApi.getBillingById(id);
                setBilling(data);
            } catch (err) {
                setError('Failed to fetch billing details.');
            } finally {
                setLoading(false);
            }   
        };
        fetchBilling();
    }, [id]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;   
    if (!billing) return <div>No billing details found.</div>;

    return (
        <div>
            <h1>Billing Details</h1>
            <p><strong>ID:</strong> {billing.id}</p>
            <p><strong>Amount:</strong> ${billing.amount}</p>
            <p><strong>Date:</strong> {new Date(billing.date).toLocaleDateString()}</p>
            <p><strong>Status:</strong> {billing.status}</p>
            <button onClick={() => navigate('/billings')}>Back to Billings</button>
        </div>
    );      
};

