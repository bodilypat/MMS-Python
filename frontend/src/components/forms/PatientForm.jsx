//src/components/forms/PatientForm.jsx 

import React, { useState } from 'react';
import '../../styles/global.css';

const intialFormState = {
    first_name: '',
    last_name: '',
    gender: '',
    dob: '',
    blood_group: '',
    /* Contact Information */
    contact_number: '',
    alternate_contact_number: '',
    email: '',
    /* national_id */
    national_id: '',
    /* Address Information */
    address_line1: '',
    address_line2: '',
    city: '',
    state: '',
    zip_code: '',
    country: '',
    /* Emergency Contact */
    emergency_contact_name: '',
    emergency_contact_relation: '',
    emergency_contact_number: '',
    /* Profile image */
    profile_image: '',
    notes: '',
    is_active: true,

};

export default function PatientForm({ onSubmit, defaultValues = intialFormState }) {
    const [formData, setFormData] = useState(defaultValues);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value,
        });
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit} className="patient-form">
            <div className="form-group">
                <label htmlFor="first_name">First Name</label>
                <input
                    type="text"
                    id="first_name"
                    name="first_name"
                    value={formData.first_name}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="last_name">Last Name</label>
                <input
                    type="text"
                    id="last_name"
                    name="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                />
            </div>  
            <div className="form-group">
                <label htmlFor="gender">Gender</label>
                <select
                    id="gender"
                    name="gender"
                    value={formData.gender}
                    onChange={handleChange}
                >
                    <option value="">Select Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
            </div>
            <div className="form-group">
                <label htmlFor="dob">Date of Birth</label>
                <input
                    type="date"
                    id="dob"
                    name="dob"
                    value={formData.dob}
                    onChange={handleChange}
                />
            </div>  
            <div className="form-group">
                <label htmlFor="blood_group">Blood Group</label>
                <input
                    type="text"
                    id="blood_group"
                    name="blood_group"
                    value={formData.blood_group}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="contact_number">Contact Number</label>
                <input
                    type="tel"
                    id="contact_number"
                    name="contact_number"
                    value={formData.contact_number}
                    onChange={handleChange}
                />
            </div>      
            <div className="form-group">
                <label htmlFor="alternate_contact_number">Alternate Contact Number</label>
                <input
                    type="tel"
                    id="alternate_contact_number"
                    name="alternate_contact_number"
                    value={formData.alternate_contact_number}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="national_id">National ID</label>
                <input
                    type="text"
                    id="national_id"
                    name="national_id"
                    value={formData.national_id}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="address_line1">Address Line 1</label>
                <input
                    type="text"
                    id="address_line1"
                    name="address_line1"
                    value={formData.address_line1}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="address_line2">Address Line 2</label>
                <input
                    type="text"
                    id="address_line2"
                    name="address_line2"
                    value={formData.address_line2}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="city">City</label>
                <input
                    type="text"
                    id="city"
                    name="city"
                    value={formData.city}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="state">State</label>    
                <input
                    type="text"
                    id="state"
                    name="state"
                    value={formData.state}
                    onChange={handleChange}
                />  
            </div>
            <div className="form-group">
                <label htmlFor="zip_code">Zip Code</label>
                <input
                    type="text"
                    id="zip_code"
                    name="zip_code"
                    value={formData.zip_code}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="country">Country</label>
                <input
                    type="text"
                    id="country"
                    name="country"
                    value={formData.country}
                    onChange={handleChange}
                />  
            </div>
            <div className="form-group">
                <label htmlFor="emergency_contact_name">Emergency Contact Name</label>
                <input
                    type="text"
                    id="emergency_contact_name"
                    name="emergency_contact_name"
                    value={formData.emergency_contact_name}
                    onChange={handleChange}
                />  
            </div>
            <div className="form-group">
                <label htmlFor="emergency_contact_relation">Emergency Contact Relation</label>
                <input
                    type="text"
                    id="emergency_contact_relation"
                    name="emergency_contact_relation"
                    value={formData.emergency_contact_relation}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="emergency_contact_number">Emergency Contact Number</label>
                <input
                    type="text"
                    id="emergency_contact_number"
                    name="emergency_contact_number"
                    value={formData.emergency_contact_number}
                    onChange={handleChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="profile_image">Profile Image URL</label>
                <input
                    type="text"
                    id="profile_image"
                    name="profile_image"
                    value={formData.profile_image}
                    onChange={handleChange}
                />      
            </div>
            <div className="form-group">
                <label htmlFor="notes">Notes</label>
                <textarea
                    id="notes"
                    name="notes"
                    value={formData.notes}
                    onChange={handleChange}
                />  
            </div>
            <div className="form-group">
                <label htmlFor="is_active">
                    <input
                        type="checkbox"
                        id="is_active"
                        name="is_active"
                        checked={formData.is_active}
                        onChange={handleChange}
                    />
                    Active
                </label>
            </div>
            <button type="submit" className="submit-button">Submit</button> 
        </form>
    );
};

