//src/components/layout/Sidebar.jsx

import React from 'react';

const Sidebar = () => {
    return (
        <aside className="sidebar" style={{ width: '250px', backgroundColor: '#f8f9fa', padding: '20px' }}>
            <h2>Admin Panel</h2>
            <nav>
                <ul className="nav flex-column">
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/dashboard">Dashboard</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/users">Manage Users</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/doctors">Manage Doctors</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/appointments">Manage Appointments</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/patients">Manage Patients</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/admin/queries">Manage Queries</a>
                    </li>
                </ul>
            </nav>
        </aside>
    );
};

export default Sidebar;
