/* src/components/layout/Footer.py */

import React from "react";
import "./Footer.css";

const Footer = () => {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="app-footer">
            <div className="footer-left">
                <span className="footer-left">@ {currentYear}<strong>MedManage</strong>. All Rights Reserved.</span>
                <span className="footer-center">
                    <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="footer-link">GitHub</a>{" "}.{" "}
                    <a href="https://medical.com" target="_blank" rel="noopener noreferrer" className="footer-link">Docs</a>
                </span>
                <span className="footer-right">Developed</span>
            </div>
        </footer>
    );
};

export default Footer;
