//src/components/forms/BillingForm.jsx

import React, { useState } from 'react';
import '../../assets/styles/global.css';

const BillingForm = () => {
    const [formData, setFormData] = useState({
        patient: billingData?.patient || '',
        doctor: billingData?.doctor || '',
        subtotal: billingData?.subtotal || '',
        tax: billingData?.tax || '',
        discount: billingData?.discount || '',
        insurance: billingData?.insurance || '',
        status: billingData?.status || 'Unpaid',
        payment_method: billingData?.payment_method || 'Cash',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onsubmit(formData);
    };

    return (
        <div className="form-container">
            <h2 className="form-title">Billing Information</h2>
            <form onSubmit={handleSubmit} className="billing-form">
                <div className="form-group">
                    <label htmlFor="patient">Patient</label>
                    <input
                        type="text"
                        name="patient"
                        value={formData.patient}
                        onChange={handleChange}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="doctor">Doctor</label>
                    <input
                        type="text"
                        name="doctor"
                        value={formData.doctor}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="subtotal">Subtotal</label>
                    <input
                        type="number"
                        name="subtotal"
                        value={formData.subtotal}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="tax">Tax</label>
                    <input
                        type="number"
                        name="tax"
                        value={formData.tax}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="discount">Discount</label>
                    <input
                        type="number"
                        name="discount"
                        value={formData.discount}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="insurance">Insurance</label>
                    <input
                        type="text"
                        name="insurance"
                        value={formData.insurance}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="status">Status</label>
                    <select
                        name="status"
                        value={formData.status}
                        onChange={handleChange}
                    >
                        <option value="Pending">Pending</option>
                        <option value="Paid">Paid</option>
                        <option value="unpaid">Unpaid</option>
                        <option value="canceled">Canceled</option>
                        <option value="refunded">Refunded</option>
                        <option value="Partially Paid">Partially Paid</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="payment_method">Payment Method</label>
                    <select
                        name="payment_method"
                        value={formData.payment_method}
                        onChange={handleChange}
                    >
                        <option value="Cash">Cash</option>
                        <option value="Credit Card">Credit Card</option>
                        <option value="Debit Card">Debit Card</option>
                        <option value="Insurance">Insurance</option>
                        <option value="Online Payment">Online Payment</option>
                    </select>
                </div>
                <button type="submit" className="submit-button">
                    Submit
                </button>
            </form>     
    </div>
    );
};

export default BillingForm;


