//src/pages/doctor/Appointments.jsx

import { useState, useEffect } from "react";
import Table from "../../components/common/Table";
import SelectField from "../../components/ui/SelectField";
import Loader from "../../components/ui/Loader";
import Badge from "../../components/ui/Badge";
import doctorServices from "../../services/doctorServices";
import EmptyState from "../../components/patient/EmptyState";

/* Fetch doctor appointments */
/* Display appointment list */
/* Filter status */
/* Loading & empty states */
/* Cloen separation (UI <-> service) */

const STATUS_OPTIONS = [
    { label: "All", value: "all" },
    { label: "Pending", value: "pending" },
    { label: "Confirmed", value: "confirmed" },
    { label: "Completed", value: "completed" },
    { label: "Cancelled", value: "cancelled" },
];

const Appointments = () => {
    const [appointments, setAppointments] = useState([]);
    const [status, setStatus] = useState("all");
    const [loading, setLoading] = useState(true);

    setEffect(() => {
        const fetchAppointments = async () => {
            setLoading(true);
            try{
                const response = await doctorServices.getAppointments(status);
                setAppointments(response.data);  
            } catch (error) {
                console.error("Error fetching appointments:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchAppointments();
    }, [status]);

    const columns = [
        { header: "Patient Name", accessor: "patientName" },
        { header: "Date", accessor: "date" },
        { header: "Time", accessor: "time" },
        { 
            header: "Status", 
            accessor: "status",
            render: (value) => <Badge type={value}>{value}</Badge>
        },
    ];

    return (
        <>
            <div className="flex justify-between items-center mb-6">
                <h1 className="mainTitle">Appointments</h1>

                {/* Filter by status */}
                <div className="row mb-3">
                    <SelectField
                        label="Filter by Status"
                        options={STATUS_OPTIONS}
                        value={status}
                        onChange={(e) => setStatus(e.target.value)}
                    />
                </div>
            </div>
            
            {/* Table */}
            {appointments.length === 0 && !loading ? (
                <EmptyState message="No appointments found." />
            ) : loading ? (
                <Loader />
            ) : (
                <Table columns={columns} data={appointments} />
            )}
        </>
    );
};
export default Appointments;
