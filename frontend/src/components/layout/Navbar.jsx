//components/layout/Navbar.jsx 

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Proptypes from 'prop-types';
import ".global.css";

const Navbar = ({ 
    user,
    onToggleSidebar,
    onLogout
}) => {
    const navigate = useNavigate();

    const handleLogout = () => {
        if (typeof onLogout === 'function') onLogout();
        localStorage.removeItem('Token');
        navigate('/login');
    };

    return (
        <header className="navbar">
            {/* Sidebar toggle for small screens */}
            {typeof onToggleSidebar === 'function' && (
                <button 
                    className="sidebar-toggle" 
                    onClick={onToggleSidebar} 
                    aria-label="Toggle sidebar"
                >
                    ☰
                </button>
            )}

            {/* App Title Logo */}
            <Link to="/" className="navbar-logo">
                Medical Management
            </Link>

            {/* Spacer */}
            <div className="navbar-spacer" />

            {/* User Menu */}
            <div className="navbar-user">
                {user ? (
                    <> 
                    <span 
                        className="navbar-logout-btn"
                        onClick={handleLogout}
                        aria-label="Logout"
                    >
                        Logout
                    </span>
                </>
                ) : (
                    <Link to="/login" className="navbar-login-btn">
                        Login
                    </Link> 
                )}
            </div>
        </header>
    );
};
export default Navbar;

/* PropTypes */
Navbar.propTypes = {
    user: Proptypes.shape({
        name: Proptypes.string.isRequired,
        role: Proptypes.string
    }),
    onToggleSidebar: Proptypes.func,
    onLogout: Proptypes.func
};

