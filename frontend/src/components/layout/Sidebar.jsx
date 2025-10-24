/* src/components/layout/sidebar.jsx  */

import React, { useState }from "react";
import { NavLink } from "react-router-dom";
import "./Sidebar.css";

const Sidebar = () => {
    const [openSection, setOpenSection] = useState(null);
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleSection = (section) => {
        setOpenSection(openSection === section ? null : section);
    }

    const toggleSidebar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
         <aside className={'sidebar ${isCollapsed ? "collapsed" : ""}'}>
            <div className="sidebar-header">
                <h3>MedManage</h3>
                <button className="collapse-btn" onClick={toggleSidebar}>
                    {isCollapsed ? "=" : "X"}
                </button>
            </div>
            <nav className="sidebar-nav">
                <NavLink to="/dashboard" className="sidebar-link">Dashbord</NavLink>
                {/* Patient Section */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-section-header"
                        onClick={() => toggleSection("patients")}
                    >
                        Patients
                        <span>{openSection === "patients" ? "-" : "+"}</span>
                    </div>
                    {openSection === "patients" && (
                        <div>
                            <NavLink to="/patients" className="sidebar-link sub">All Patient</NavLink>
                            <NavLink to="/patients/add" className="sidebar-link sub">Add Patient</NavLink>
                        </div>
                    )}
                </div>
                {/* Doctor Section */}
                <div className="sidebar-section">
                    <div 
                        className="sidebar-section-header"
                        onClick={() => toggleSection("doctors")}
                    >
                        Doctors 
                        <span>{openSection === "doctors" ? "-" : "+"}</span>
                    </div>
                    {openSection === "doctors" && (
                    <div>
                        <NavLink to="/doctors" className="sidebar-link sub">All Doctors</NavLink>
                        <NavLink to="/doctors/add" className="sidebar-link-sub">Add Doctors</NavLink>
                    </div>
                    )}
                </div>
                {/* Appointment Section */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-section-header"
                        onClick={() => toggleSection("appointments")}
                    >
                        Appoiontments 
                        <span>{openSection === "appointments" ? "-" : "+"}</span>
                    </div>
                    {openSection === "appointments" && ( 
                        <div className="sidebar-submenu">
                            <NavLink to="/appointments" className="sidebar-linksub">View Appointments</NavLink>
                            <NavLink to="/appointments/add" className="sidebar-link sub">Schedule New</NavLink>
                        </div>
                    )}
                </div>
                {/* Billing Section */}
                <div className="sidebar-section">
                    <div
                        className="sidebar-section-header"
                        onClick={() => toggleSection("billing")}
                    >
                        Billing
                        <span>{openSection === "billing" ? "-" : "+"}</span>
                    </div>
                    {openSection === "billing" && (
                        <div className="sidebar-submenu">
                            <NavLink to="/billing" className="sidebar-link sub">Invoices</NavLink>
                            <NavLink to="/billing/receipts" className="sidebar-link sub">Receipts</NavLink>
                        </div>
                    )}
                </div>
                {/* Reports Section */}
                <NavLink to="/reports" className="sidebar-link">Reports</NavLink>
            </nav>
         </aside>
    );
};

export default Sidebar;