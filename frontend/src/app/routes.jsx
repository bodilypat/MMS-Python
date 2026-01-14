// src/app/routes.jsx

import { Routes, Route } from "react-router-dom";
import ProtectedRoute from "../components/common/ProtectedRoute";

import AdminDashboard from "../features/admin/Dashboard";
import DoctorDashboard from "../features/doctor/Dashboard";
import PatientDashboard from "../features/patient/Dashboard";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/admin" element={
                <ProtectedRoute role="admin">
                    <AdminDashboard />
                </ProtectedRoute>
            } />

            <Route path="/doctor" element={
                <ProtectedRoute role="doctor">
                    <DoctorDashboard />
                </ProtectedRoute>
            } />

            <Route path="/patient" element={
                <ProtectedRoute role="patient">
                    <PatientDashboard />
                </ProtectedRoute>
            } />    
        </Routes>
    );
}
