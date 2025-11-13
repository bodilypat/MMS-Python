//src/pages/Appointments/appointment.api.js 

import apiClient from "../../services/apiClient";

export const getAppointments = () => apiClient.get("/appointments");
export const getAppointmentById = (id) => apiClient.get(`/appointments/${id}`);
export const createAppointment = (data) => apiClient.post("/appointments", data);
export const updateAppointment = (id, data) => 
        apiClient.put(`/appointments/${id}`, data);
export const deleteAppointment = (id) => 
        apiClient.delete(`/appointments/${id}`);
