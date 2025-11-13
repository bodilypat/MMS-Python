// src/pages/Patients/patient.api.js
const API_URL = "http://localhost:5000/api/patients"; // adjust as needed

export const getPatients = async () => {
  const res = await fetch(API_URL);
  if (!res.ok) throw new Error("Failed to fetch patients");
  return res.json();
};

export const getPatientById = async (id) => {
  const res = await fetch(`${API_URL}/${id}`);
  if (!res.ok) throw new Error("Failed to fetch patient");
  return res.json();
};

export const createPatient = async (patient) => {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(patient),
  });
  if (!res.ok) throw new Error("Failed to create patient");
  return res.json();
};

export const updatePatient = async (id, patient) => {
  const res = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(patient),
  });
  if (!res.ok) throw new Error("Failed to update patient");
  return res.json();
};

export const deletePatient = async (id) => {
  const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete patient");
  return true;
};
