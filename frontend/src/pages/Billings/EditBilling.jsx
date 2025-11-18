//src/pages/billing/EditBillnig.jsx 

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import BillingForm from '../../components/forms/BillingForm';
import { getBillingById, updateBilling } from '../../api/billingApi';

const EditBilling = () => {
    const { bill_id } = useParams();
    const navigate = useNavigate();

    const [billingData, setBillingData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [submitting, setSubmitting] = useState(false);
    const [success, setSuccess] = useState(null);
    const [error, setError] = useState(null);

    /* Fetch billing data on component mount */
    useEffect(() => {
        const fetchBilling = async () => {
            try {
                const data = await getBillingById(bill_id);
                setBillingData(data);
            } catch (err) {
                setError('Failed to fetch billing data.');
            } finally {
                setLoading(false);
            }
        };

        fetchBilling();
    }, [bill_id]);

    /* Handle form submission */
    const handleUpdateBilling = async (formData) => {
        setSubmitting(true);
        setError(null);
        setSuccess(null);
        try {
            const response = await updateBilling(bill_id, formData);

            if (response.success) {
                setSuccess('Billing updated successfully.');
                setTimeout(() => navigate('/billing'), 2000);
            } else {
                setError('Failed to update billing.');
            }       
        } catch (err) {
            setError('Failed to update billing.');
        } finally {
            setSubmitting(false);
        }
    };
    
    if (loading) {
        return <div>Loading...</div>;
    }

    if (!billingData) {
        return <div>Error loading billing data.</div>;
    }

    return (
        <div>
            <h2>Edit Billing</h2>
            <BillingForm
                initialData={billingData}
                onSubmit={handleUpdateBilling}
            />
        </div>
    );  
};

export default EditBilling;
