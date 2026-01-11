//src/components/layout/Footer.jsx

import  React from 'react';

const Footer = () => {
    return (
        <footer className="bg-light text-center text-lg-start mt-auto">
            <div className="text-center p-3">
                © {new Date().getFullYear()} Medical Management System
            </div>
        </footer>
    );
}
export default Footer;


