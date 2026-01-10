//src/pages/doctor/Profile.jsx 

import { useEffect, useState } from "react";
import InputField from "../../components/ui/InputField";
import Button from "../../components/ui/Button";
import Loader from "../../components/ui/Loader";
import DoctorService from "../../services/DoctorService";
import { validateProfile } from "../../utils/validators";


const Profile = () => {
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        phone: "",
        specialization: "",
        experience: "",
        feesPerConsultation: "",
        timings: "",
    });
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [errors, setErrors] = useState({});
    const [success, setSuccess] = useState("");

    /* Fetch doctor profile */
    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await DoctorService.getProfile();
                setFormData(response.data);
            } catch (error) {
                console.error("Error fetching profile:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchProfile();
    }, []);

    /* Handle form input changes */
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
        setErrors({ ...errors, [e.target.name]: "" });
    };

    /* Handle form submission */
    const handleSubmit = async (e) => {
        e.preventDefault();

        const validationErrors = validateProfile(formData);
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }
        setSaving(true);
        setErrors({});
        setSuccess("");

        try {
            await DoctorService.updateProfile(formData);
            setSuccess("Profile updated successfully!");
        } catch (error) {
            console.error("Error updating profile:", error);
            setErrors({ submit: "Failed to update profile. Please try again." });
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return <Loader />;
    }

    return (
        <div className="max-w-3xl mx-auto p-6 bg-white rounded shadow">
            <h2 className="text-2xl font-bold mb-6">Doctor Profile</h2>
            {success && <div className="mb-4 p-3 bg-green-100 text-green-800 rounded">{success}</div>}
            {errors.submit && <div className="mb-4 p-3 bg-red-100 text-red-800 rounded">{errors.submit}</div>}
            <form onSubmit={handleSubmit} className="row">
                <div className="mb-4">
                    <InputField
                        label="Full Name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        error={errors.name}
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        error={errors.email}
                        type="email"
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Phone Number"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        error={errors.phone}
                        type="tel"
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Specialization"
                        name="specialization"
                        value={formData.specialization}
                        onChange={handleChange}
                        error={errors.specialization}
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Experience (years)"
                        name="experience"
                        value={formData.experience}
                        onChange={handleChange}
                        error={errors.experience}
                        type="number"
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Fees Per Consultation"
                        name="feesPerConsultation"
                        value={formData.feesPerConsultation}
                        onChange={handleChange}
                        error={errors.feesPerConsultation}
                        type="number"
                    />
                </div>
                <div className="mb-4">
                    <InputField
                        label="Timings"
                        name="timings"
                        value={formData.timings}
                        onChange={handleChange}
                        error={errors.timings}
                    />
                </div>
                <Button type="submit" disabled={saving}>
                    {saving ? "Saving..." : "Update Profile"}
                </Button>
            </form>
        </div>
    );
};

export default Profile;
