//src/pages/Billings/billing.api.js 

import apiClient from '../../services/apiClient';

export const getAllBillings = async () => {
    const response = await apiClient.get('/billings');
    return response.data;
};

/* Get billing by billing ID */
export const getBillingById = async (id) => {
    const response = await apiClient.get(`/billings/${id}`);
    return response.data;
};

/* Get all billing entries for a specific patient */
export const getBillingsByPatientId = async (patientId) => {
    const response = await apiClient.get(`/billings/patient/${patientId}`);
    return response.data;
};

/* Create a new billing entry */
export const createBilling = async (billingData) => {
    const response = await apiClient.post('/billings', billingData);
    return response.data;
};

/* Update an existing billing entry */
export const updateBilling = async (id, billingData) => {
    const response = await apiClient.put(`/billings/${id}`, billingData);
    return response.data;
};

/* Delete a billing entry */
export const deleteBillingById = async (id) => {
    const response = await apiClient.delete(`/billings/${id}`);
    return response.data;
};

export default {
    getAllBillings,
    getBillingById,
    getBillingsByPatientId,
    createBilling,
    updateBilling,
    deleteBillingById
};  