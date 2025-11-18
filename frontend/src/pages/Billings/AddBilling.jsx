//src/pages/billing/AddBilling.jsx

import React from 'react';
import billingApi from '../../api/billingApi';
import BillingForm from '../../components/forms/BillingForm';
import BillingTable from '../../components/tables/BillingTable';
import BillingFilter from '../../components/filters/BillingFilter';

const AddBilling = () => {
    const [billingData, setBillingData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);
    const [isFormVisible, setIsFormVisible] = useState(false);

    const fetchBillingData = async () => {
        try {
            const response = await billingApi.getAll();
            setBillingData(response.data);
            setFilteredData(response.data);
        } catch (error) {
            console.error('Error fetching billing data:', error);
        }
    };

    useEffect(() => {
        fetchBillingData();
    }, []);

    const handleFilter = (filters) => {
        let filtered = billingData;

        if (filters.status) {
            filtered = filtered.filter(item => item.status === filters.status);
        }

        if (filters.dateRange) {
            filtered = filtered.filter(item => {
                const itemDate = new Date(item.date);
                return itemDate >= filters.dateRange.start && itemDate <= filters.dateRange.end;
            });
        }

        setFilteredData(filtered);
    };

    const handleAddNew = () => {
        setIsFormVisible(true);
    };

    const handleFormClose = () => {
        setIsFormVisible(false);
        fetchBillingData(); // Refresh the list after form submission
    };

    return (
        <div>
            <h1>Billing Records</h1>
            <BillingFilter onFilter={handleFilter} />
            <button onClick={handleAddNew}>Add New Billing</button>
            <BillingTable data={filteredData} />
            {isFormVisible && (
                <BillingForm onClose={handleFormClose} />
            )}
        </div>
    );
};

export default AddBilling;
