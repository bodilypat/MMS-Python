//src/pages/Prescriptions/prescriptionForm.jsx

import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import prescriptionSchema from "./prescription.schema"; // Import the schema        
import { 
    createPrescription,
    getPrescriptionById,
    updatePrescription
} from "./prescription.api"; // Assume these API functions are defined elsewhere
import Spinner from "../../components/common/Spinner";
import Button from "../../components/Notifications/Button";
import Toast from "../../components/Notifications/Toast";

const PrescriptionForm = ({ prescriptionId = null, onSuccess }) => {
    const isEditMode = Boolean(prescriptionId)
    const [loading, setLoading] = useState(isEditMode);
    const [Submitting, setSubmitting] = useState(false);

    const {
        register,
        handleSubmit,
        setValue,
        reset,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(prescriptionSchema),
        mode: "onTouched",      
    });

    /* Fetch existing data for edit mode */
    useEffect(() => {
        if (isEditMode) {
            (async () => {
                try {
                    const data = await getPrescriptionById(prescriptionId);
                    if (data) {
                        Object.keys(data).forEach((key) => {
                            if (data[key] !== null && data[key] !== undefined) {
                                setValue(key, data[key]);
                            }
                        });
                    }
                } catch (error) {
                    console.error("Error fetching prescription:", error);
                    Toast.error("Failed to load prescription data");
                } finally {
                    setLoading(false);
                }   
            })();
        }
    }, [prescriptionId, isEditMode, setValue]);
    
    /* Handle Form Submit */
    const onSubmit = async (formData) => {
        setSubmitting(true);
        try {
            if (isEditMode) {
                await updatePrescription(prescriptionId, formData);
                Toast.success("Prescription updated successfully");
            } else {
                await createPrescription(formData);
                Toast.success("Prescription created successfully");
                reset();
            }
            if (onSuccess) onSuccess();
        } catch (error) {
            console.error("Error submitting prescription:", error);
            Toast.error("Failed to submit prescription");
        } finally {
            setSubmitting(false);
        }
    };

    if (loading) return <Spinner message="Loading prescription data..." />;
    return (
        <div className="precription-form-container card p-4 shadow-sm">
            <h2 className="mb-4">{isEditMode ? "Edit Prescription" : "New Prescription"}</h2>
            <form onSubmit={handleSubmit(onSubmit)} noValidate>
                <div className="from-group mb-3">
                    <label htmlFor="patient_id" className="form-label">Patient ID</label>
                    <input
                        type="number"
                        id="patient_id"
                        className="form-control"
                        {...register("patient_id")}
                    />
                    <div className="invalid-feedback">{errors.patient_id?.message}</div>
                </div>
                <div className="from-group mb-3">
                    <label htmlFor="doctor_id" className="form-label">Doctor ID</label>
                    <input
                        type="number"
                        id="doctor_id"
                        className="form-control"
                        {...register("doctor_id")}
                    />
                    <div className="invalid-feedback">{errors.doctor_id?.message}</div>
                </div>
                <div className="from-group mb-3">
                    <label htmlFor="medication" className="form-label">Medication</label>
                    <input
                        type="text"
                        id="medication"
                        className="form-control"
                        {...register("medication")}
                    />
                    <div className="invalid-feedback">{errors.medication?.message}</div>
                </div>          
                <div className="from-group mb-3">
                    <label htmlFor="dosage" className="form-label">Dosage</label>
                    <input
                        type="text"
                        id="dosage"
                        className="form-control"
                        {...register("dosage")}
                    />
                    <div className="invalid-feedback">{errors.dosage?.message}</div>
                </div>      
                <div className="from-group mb-3">
                    <label htmlFor="frequency" className="form-label">Frequency</label>
                    <input
                        type="text"
                        id="frequency"
                        className="form-control"
                        {...register("frequency")}
                    />
                    <div className="invalid-feedback">{errors.frequency?.message}</div>
                </div>      
                <div className="from-group mb-3">
                    <label htmlFor="duration" className="form-label">Duration</label>
                    <input
                        type="text"
                        id="duration"
                        className="form-control"
                        {...register("duration")}
                    />
                    <div className="invalid-feedback">{errors.duration?.message}</div>
                </div>  
                <div className="from-group mb-3">
                    <label htmlFor="status" className="form-label">Status</label>
                    <select
                        id="status"
                        className="form-control"
                        {...register("status")}
                    >
                        <option value="">Select Status</option>
                        <option value="active">Active</option>
                        <option value="inactive">Inactive</option>
                    </select>
                    <div className="invalid-feedback">{errors.status?.message}</div>
                </div>                              
                <Button type="submit" disabled={Submitting}>
                    {Submitting ? (isEditMode ? "Updating..." : "Creating...") : (isEditMode ? "Update Prescription" : "Create Prescription")}
                </Button>       
            </form>
        </div>
    );
}   

