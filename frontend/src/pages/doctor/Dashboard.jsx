//src/pages/doctor/Dashboard.jsx

import { Link } from "react-router-dom";
import Card from "../../components/ui/Card";
/* Doctor dashbord */
/* Profile */
/* Appointments */
/* MedicalRecord */
/* PatientHistory */
const Dashboard = () => {
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Doctor Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <Link to="/doctor/profile">
                    <Card>
                        <h2 className="text-xl font-semibold">Profile</h2>
                        <p>View and edit your profile information.</p>
                    </Card>
                </Link>
                <Link to="/doctor/appointments">
                    <Card>
                        <h2 className="text-xl font-semibold">Appointments</h2>
                        <p>Manage your upcoming appointments.</p>
                    </Card>
                </Link>
                <Link to="/doctor/medical-records">
                    <Card>
                        <h2 className="text-xl font-semibold">Medical Records</h2>
                        <p>Access and update patient medical records.</p>
                    </Card>
                </Link>
                <Link to="/doctor/patient-history">
                    <Card>
                        <h2 className="text-xl font-semibold">Patient History</h2>
                        <p>Review the history of your patients.</p>
                    </Card>
                </Link>
            </div>
        </div>
    );
};

export default Dashboard;
