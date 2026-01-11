//src/components/AdminLayout.jsx

import React from "react";
import Header from "../../components/common/Header";
import Sidebar from "../../components/common/Sidebar";
import Navbar from "../../components/common/Navbar";
import Footer from "../../components/common/Footer";

const AdminLayout = ({ children }) => {
    return (
        <div className="admin-layout">
            <Header />
            <Sidebar />
            <div className="main-content">
                <Navbar />
                <div className="content-area">
                    {children}
                </div>
                <Footer />
            </div>
        </div>
    );
};
export default AdminLayout;
