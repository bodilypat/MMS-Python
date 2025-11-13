//src/pages/Doctors/doctor.api.js 

import apiClient from "../../services/apiClient";

export const doctorApi = {
    getAll: () => apiClient.get("/doctors"),
    getById: (id) => apiClient.get(`/doctors/${id}`),
    create: (data) => apiClient.post("/doctors", data),
    update: (id, data) => apiClient.put(`/doctors/${id}`, data),
    delete: (id) => apiClient.delete(`/doctors/${id}`),
};
