/* App.jsx */

import React from "react";
import "./assets/styles/main.css";
import "./assets/styles/layout.css";

import Navbar from "./components/layout/Navbar";
import Sidebar from "./components/layout/Sidebar";
import Footer from "./components/layout/Footer";
import AppRoutes from "./routes/AppRoutes";

const App = () => {
    return (
        <div className="app-layout">
            <aside className="sidebar">
                <Sidebar />
            </aside>

            <header className="navbar">
                <Navbar />
            </header>
            
            <main className="main-content">
                <AppRoutes />
            </main>

            <footer className="footer">
                <Footer />
            </footer>
        </div>
    );
};

export default App;