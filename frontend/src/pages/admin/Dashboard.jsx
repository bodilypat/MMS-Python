//src/pages/admin/Dashboard.jsx

import React, { useEffect, useState } from "react";
import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";
import Footer from "../components/loyout/Footer";
import { getDashboardState } from "../services/dashboard";

const AdminDashboard = () => {
    const [stats, setState] = useState({
        users: 0,
        doctors: 0,
        appointments: 0,
        patients: 0,
        queries: 0,
    });

    useEffect(() => {
        getDashboardState().then((data) => setState(data));
    }, []);

    return (
        <div className="admin-dashboard">
            <Sidebar />

            <div className="app-content">
                <Header />

                <div className="main-content">
                    <div className="wrap-content container">
                        <section id="page-title">
                            <div className="row">
                                <div className="col-sm-8">
                                    <h1 className="mainTitle">Admin Dashboard</h1>
                                    <span className="mainDescription">
                                        Overview of system statistics
                                    </span>
                                </div>
                            </div>
                        </section>

                        <div className="dashboard-stats">
                            <div className="row">

                                <DashboardCard 
                                    title="Manage Users"
                                    icon="fa-users"
                                    count={stats.users}
                                    link="/admin/users"
                                />

                                <DashboardCard
                                    title="Manage Doctors"
                                    icon="fa-user-md"
                                    count={stats.doctors}
                                    link="/admin/doctors"
                                />

                                <DashboardCard
                                    title="Manage Appointments"
                                    icon="fa-calendar"
                                    count={stats.appointments}
                                    link="/admin/appointments"
                                />

                                <DashboardCard
                                    title="Manage Patients"
                                    icon="fa-wheelchair"
                                    count={stats.patients}
                                    link="/admin/patients"
                                />

                                <DashboardCard
                                    title="Manage Queries"
                                    icon="fa-question-circle"
                                    count={stats.queries}
                                    link="/admin/queries"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                <Footer />
            </div>
        </div>
    );
}

const DashboardCard = ({ title, icon, count, link }) => (
    <div className="col-md-3">
        <div className="dashboard-card">
            <div className="card-body">
                <div className="stat-icon">
                    <i className={`fa ${icon} fa-3x`}></i>
                </div>
                <div className="stat-info">
                    <h4>{count}</h4>
                    <p>{title}</p>
                </div>
                <div className="stat-link">
                    <a href={link}>View Details <i className="fa fa-arrow-circle-right"></i></a>
                </div>
            </div>
        </div>
    </div>
);

export default AdminDashboard;

