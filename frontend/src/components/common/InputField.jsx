src/components/common/InputField.jsx

import React from "react";
import "./InputField.css";

const InputField = ({ label, name, type = "text", value, onChange, error}) => {
    return (
       <div className="input-field">
            {label && <label htmlFor={name}>{label}</label>}
            <input id={name} name={name} type={type} value={value} onChange={onChange} />
            {error && <span className="error-text">{error}</span>}
       </div>
    );
};

export default InputField;