//src/components/layout/Header.jsx

import React from 'react';

const Header = ({ title }) => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
            <div className="container-fluid">
                <span className="navbar-brand mb-0 h1">{title}</span>
            </div>
        </nav>
    );
};

export default Header;
