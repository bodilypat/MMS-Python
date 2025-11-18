//src/pages/billing/BillingList.jsx

import React, { useState, useEffect } from 'react';
import billingApi from '../../api/billingApi';
import BillingTable from '../../components/tables/BillingTable';
import BillingForm from '../../components/forms/BillingForm';

const BillingList = () => {
    const [billingData, setBillingData] = useState([]);
    const [selectedBilling, setSelectedBilling] = useState(null);
    const [isFormVisible, setIsFormVisible] = useState(false);

    const fetchBillingData = async () => {
        try {
            const response = await billingApi.getAll();
            setBillingData(response.data);
        } catch (error) {
            console.error('Error fetching billing data:', error);
        }
    };

    useEffect(() => {
        fetchBillingData();
    }, []);
    
    const handleEdit = (id) => {
        const billing = billingData.find(item => item.id === id);
        setSelectedBilling(billing);
        setIsFormVisible(true);
    };

    const handleDelete = async (id) => {
        try {
            await billingApi.delete(id);
            fetchBillingData(); // Refresh the list after deletion
        } catch (error) {
            console.error('Error deleting billing record:', error);
        }
    };

    const handleFormClose = () => {
        setIsFormVisible(false);
        setSelectedBilling(null);
        fetchBillingData(); // Refresh the list after form submission
    };
    return (
        <div>
            <h1>Billing Records</h1>
            <BillingTable
                data={billingData}
                onEdit={handleEdit}
                onDelete={handleDelete}
            />
            {isFormVisible && (
                <BillingForm
                    billing={selectedBilling}
                    onClose={handleFormClose}
                />
            )}
        </div>
    );
};

export default BillingList;