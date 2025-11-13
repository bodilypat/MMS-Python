//src/pages/Appointments/apointment.schema.js 

import * as Yup from "yup";

export const AppointmentSchema = Yup.object().shape({
    patient_id: Yup.number()
        .required("Patient is required")
        .positive("Invalid patient ID"),
    doctor_id: Yup.number()
        .required("Doctor is required")
        .positive("Invalid doctor ID"),
    appointment_datetime: Yup.date()
        .required("Appointment date and time are required")
        .min(new Date(), "Appointment cannot be in the past"),
    status: Yup.string().oneOf(
        ["Scheduled", "Completed", "Cancelled", "No-Show"],
        "Invalid status"
    ),
    reason: Yup.string().max(255,"Reason too long"),
    motes: Yup.string().nullable(),
    location: Yup.string().max(100,"Location too long"),
});
