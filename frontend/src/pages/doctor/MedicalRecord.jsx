//src/pages/doctor/MedicalRecord.jsx

import { useState, useEffect} from "react";
import SelectField from "../../components/ui/SelectField";
import TextArea from "../../components/ui/TextArea";
import Button from "../../components/ui/Button";
import Card from "../../components/ui/Card";
import Loader from "../../components/ui/Loader";
import EmptyState from "../../components/ui/EmptyState";
import doctorServices from "../../services/doctorServices";

/* Select patient*/
/* View medical records */
/* Add/update notes & prescriptions */
/* Loading & empty states */
/* Service-based data access */

const MedicalRecord = () => {
    const [patients, setPatients] = useState([]);
    const [selectedPatientId, setSelectedPatientId] = useState("");
    const [records, setRecords] = useState([]);
    const [notes, setNotes] = useState("");
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);

    /* Fetch patients List */
    useEffect(() => {
        const fetchPatients = async () => {
            try {
                const response = await doctorServices.getPatients();
                setPatients(response.data);
            } catch (error) {
                console.error("Error fetching patients:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchPatients();
    }, []);

    /* Fetch medical records when patient change */
    useEffect(() => {
        if (!selectedPatientId) return;

        const fetchRecords = async () => {
            setLoading(true);
            try {
                const response = await doctorServices.getMedicalRecords(selectedPatientId);
                setRecords(response.data);
            } catch (error) {
                console.error("Error fetching medical records:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchRecords();
    }, [selectedPatientId]);

    const handleSave = async () => {
        if (!selectedPatientId) return;

        setSaving(true);
        try {
            await doctorServices.saveMedicalRecord(selectedPatientId, { notes });
        } catch (error) {
            console.error("Error saving medical record:", error);
        } finally {
            setSaving(false);
            setLoading(true);
            try {
                const response = await doctorServices.getMedicalRecords(selectedPatientId);
                setRecords(response.data);
            } catch (error) {
                console.error("Error fetching medical records:", error);
            } finally {
                setLoading(false);
            }
        }
    };

    if (loading) {
        return <Loader />;
    }

    return (
        <>
        <h1 className="mainTitle">Medical Records</h1>

        {/* Patient Selection */}
        <div className="row mb-3">
            <div className="col-md-6">
                <SelectField
                    label="Select Patient"
                    name="patient"
                    value={selectedPatientId}
                    onChange={(e) => setSelectedPatientId(e.target.value)}
                    options={patients.map((patient) => ({
                        value: patient.id,
                        label: `${patient.firstName} ${patient.lastName}`,
                    }))}
                />
            </div>
        </div>

        {/* Medical Records */}
        {records.length === 0 ? (
            <EmptyState message="No medical records found for this patient." />
        ) : (
            records.map((record) => (
                <Card key={record.id}>
                    <TextArea
                        label="Notes"
                        value={record.notes}
                        onChange={(e) => setNotes(e.target.value)}
                    />
                    <Button onClick={handleSave} loading={saving}>
                        Save
                    </Button>
                </Card>
            ))
        )}
        </>
    );
};
export default MedicalRecord;
