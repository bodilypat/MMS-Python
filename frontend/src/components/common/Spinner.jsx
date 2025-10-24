src/components/common/Spinner.jsx

import React from "react";
import "./Spinner.css";

const Spinner = ({ size = "md", variant = "primary", text = ""}) => {
    return (
        <div className={'spinner-container ${size}'}>
            <div className={'spinner ${variant}'}></div>
            {text && <span className="spinner-text">{text}</span>}
        </div>
    );
};