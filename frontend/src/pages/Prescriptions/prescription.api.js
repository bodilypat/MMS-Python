//src/pages/Prescriptions/prescription.api.js

import apiClient from "../../services/apiClient";

const BASE_URL = "/prescriptions";

/* Prescription API functions */
export const getAllPrescriptions = async (params = {}) => {
    try {
        const response = await apiClient.get(BASE_URL, { params });
        return response.data;
    } catch (error) {
        console.error("Error fetching prescriptions:", error);
        throw error.response;
    }
};

/* Get a single prescription by ID */
export const getPrescriptionById = async (id) => {
    try {
        const response = await apiClient.get(`${BASE_URL}/${id}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching prescription:", error);
        throw error.response?;
    }
};

/* Create a new prescription */
export const createPrescription = async (prescriptionData) => {
    try {
        const response = await apiClient.post(BASE_URL, prescriptionData);
        return response.data;
    } catch (error) {
        console.error("Error creating prescription:", error);
        throw error.response?.data || error;
    }
};

/* Update an existing prescription */
export const updatePrescription = async (id, prescriptionData) => {
    try {
        const response = await apiClient.put(`${BASE_URL}/${id}`, prescriptionData);
        return response.data;
    } catch (error) {
        console.error("Error updating prescription:", error);
        throw error.response?.data || error;
    }
};

/* Delete a prescription */
export const deletePrescription = async (id) => {
    try {
        const response = await apiClient.delete(`${BASE_URL}/${id}`);
        return response.data;
    } catch (error) {
        console.error("Error deleting prescription:", error);
        throw error.response?.data || error;
    }
};

/* Update only the status of prescription */
export const updatePrescriptionStatus = async (id, status) => {
    try {
        const response = await apiClient.patch(`${BASE_URL}/${id}/status`, { status });
        return response.data;
    } catch (error) {
        console.error("Error updating prescription status:", error);
        throw error.response?.data || error;
    }
};

export default {
    getAllPrescriptions,
    getPrescriptionById,
    createPrescription,
    updatePrescription,
    deletePrescription,
    updatePrescriptionStatus
};