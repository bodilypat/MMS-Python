/* src/components/common/Button.jsx  */

import React from "React";
import "./Button.css";

const Button = ({ label, onClick, type = "button", variant = "primary", disabled = false }) => {
    return (
        <button
            type={type}
            className={'btn btn-${variant}'}
            onClick={onClick}
            disabled={disabled}
        >
        {label}
        </button>
    );
};