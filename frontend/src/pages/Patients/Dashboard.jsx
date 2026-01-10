//src/pages/patient/Dashboard.jsx

import { Link } from "react-router-dom";

export default function PatientDashboard() {
    return(
        <div className="container">
            <h1>Patient Dashboard</h1>
            <p>Welcome to dashboard</p>

            <div className="row">
                <div className="col-md-6">
                    <Link to="/patient/profile" className="btn btn-primary">View Profile</Link>
                </div>
                <div className="col-md-6">
                    <Link to="/patient/book" className="btn btn-success">Book Appointments</Link>
                </div>
                <div className="col-md-6">
                    <Link to="/patient/appointments" className="btn btn-info">Appointment</Link>
                </div>
                <div className="col-md-6">
                    <Link to="/patient/history" className="btn btn-warning">Medical History</Link>
                </div>
            </div>
        </div>
    );
}
