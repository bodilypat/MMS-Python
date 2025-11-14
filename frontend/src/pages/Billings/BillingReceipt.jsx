//src/pages/Billing/BillingReceipt.jsx 

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './BillingList.css';

const BillingReceipt =({ billingId }) => {
    const [receiptData, setReceiptData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchReceiptData = async () => {
            try {
                const response = await axios.get(`/api/billings/${billingId}`);
                setReceiptData(response.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        if (billingId) {
            fetchReceiptData();
        }
    }, [billingId]);
    
    if (loading) return <div>Loading billing information...</div>;
    if (error) return <p>Error: {error}</p>;
    if (!receiptData || receiptData.length === 0) return <p>No billing information found.</p>;

    return (
        <div className="billing-receipt">
            <h2>Billing Receipt</h2>
            {receiptData.map((bill) => (
                <div key={bill.bill_id} className="bill-item">
                    <p><strong>Bill ID:</strong>{bill.bill_id}</p>
                    <p><strong>Patient ID:</strong>{bill.patient_id}</p>
                    <p><strong>Amount:</strong>${Number(bill.amount).toFixed(2)}</p>
                    <p><strong>Billing date:</strong>{new Date(bill.billing_date).toLocaleDateString()}</p>
                    <p><strong>Status:</strong>{bill.status}</p>
                    <p><small><strong>Created:</strong>{" "}{new Date(bill.created_at).toLocaleString()}</small></p>
                    <p><small><strong>Update:</strong>{" "}{new Date(bill.updated_at).toLocaleString()}</small></p>
                    <hr />
                </div>
            ))}
        </div>
    );
};

export default BillingReceipt;

