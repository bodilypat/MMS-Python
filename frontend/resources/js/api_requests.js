// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/doctors';

// Function to fetch all doctors from the backend
function getDoctors() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Doctors:', data);
            displayDoctors(data);
        })
        .catch(error => console.error('Error fetching doctors:', error));
}

// Function to display doctors in HTML
function displayDoctors(doctors) {
    const doctorsTable = document.getElementById('doctors-table');
    doctorsTable.innerHTML = ''; // Clear the table before populating
    doctors.forEach(doctor => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${doctor.first_name} ${doctor.last_name}</td>
            <td>${doctor.specialization}</td>
            <td>${doctor.email}</td>
            <td>${doctor.phone_number}</td>
            <td>${doctor.department}</td>
            <td>${doctor.status}</td>
            <td>${doctor.birthdate}</td>
            <td>${doctor.address}</td>
            <td>${doctor.notes}</td>
            <td><button onclick="editDoctor(${doctor.doctor_id})">Edit</button></td>
            <td><button onclick="deleteDoctor(${doctor.doctor_id})">Delete</button></td>
        `;
        doctorsTable.appendChild(row);
    });
}

// Function to add a new doctor
function addDoctor(event) {
    event.preventDefault();
    
    const form = document.getElementById('doctor-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            specialization: formData.get('specialization'),
            email: formData.get('email'),
            phone_number: formData.get('phone_number'),
            department: formData.get('department'),
            birthdate: formData.get('birthdate'),
            address: formData.get('address'),
            status: formData.get('status'),
            notes: formData.get('notes'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Doctor added:', data);
        getDoctors(); // Refresh the doctor list
    })
    .catch(error => console.error('Error adding doctor:', error));
}

// Function to edit a doctor (triggered by the Edit button)
function editDoctor(doctorId) {
    fetch(`${apiUrl}/${doctorId}`)
        .then(response => response.json())
        .then(doctor => {
            const form = document.getElementById('doctor-form');
            form.elements['doctor_id'].value = doctor.doctor_id;
            form.elements['first_name'].value = doctor.first_name;
            form.elements['last_name'].value = doctor.last_name;
            form.elements['specialization'].value = doctor.specialization;
            form.elements['email'].value = doctor.email;
            form.elements['phone_number'].value = doctor.phone_number;
            form.elements['department'].value = doctor.department;
            form.elements['birthdate'].value = doctor.birthdate;
            form.elements['address'].value = doctor.address;
            form.elements['status'].value = doctor.status;
            form.elements['notes'].value = doctor.notes;
        })
        .catch(error => console.error('Error fetching doctor data:', error));
}

// Function to delete a doctor
function deleteDoctor(doctorId) {
    if (confirm('Are you sure you want to delete this doctor?')) {
        fetch(`${apiUrl}/${doctorId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Doctor deleted:', data);
            getDoctors(); // Refresh the doctor list
        })
        .catch(error => console.error('Error deleting doctor:', error));
}

// Event listener for the form submission to add or update doctors
document.getElementById('doctor-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const doctorId = document.getElementById('doctor-form').elements['doctor_id'].value;
    if (doctorId) {
        updateDoctor(doctorId);
    } else {
        addDoctor(event);
    }
});

// Function to update a doctor's information
function updateDoctor(doctorId) {
    const form = document.getElementById('doctor-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${doctorId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            specialization: formData.get('specialization'),
            email: formData.get('email'),
            phone_number: formData.get('phone_number'),
            department: formData.get('department'),
            birthdate: formData.get('birthdate'),
            address: formData.get('address'),
            status: formData.get('status'),
            notes: formData.get('notes'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Doctor updated:', data);
        getDoctors(); // Refresh the doctor list
    })
    .catch(error => console.error('Error updating doctor:', error));
}

// Call getDoctors to initially load the doctors list
document.addEventListener('DOMContentLoaded', getDoctors);
// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/appointments';

// Function to fetch all appointments from the backend
function getAppointments() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Appointments:', data);
            displayAppointments(data);
        })
        .catch(error => console.error('Error fetching appointments:', error));
}

// Function to display appointments in HTML
function displayAppointments(appointments) {
    const appointmentsTable = document.getElementById('appointments-table');
    appointmentsTable.innerHTML = ''; // Clear the table before populating
    appointments.forEach(appointment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${appointment.patient_name}</td>
            <td>${appointment.doctor_name}</td>
            <td>${appointment.appointment_date}</td>
            <td>${appointment.reason_for_visit}</td>
            <td>${appointment.status}</td>
            <td>${appointment.duration}</td>
            <td>${appointment.appointment_type}</td>
            <td>${appointment.notes}</td>
            <td><button onclick="editAppointment(${appointment.appointment_id})">Edit</button></td>
            <td><button onclick="deleteAppointment(${appointment.appointment_id})">Delete</button></td>
        `;
        appointmentsTable.appendChild(row);
    });
}

// Function to add a new appointment
function addAppointment(event) {
    event.preventDefault();
    
    const form = document.getElementById('appointment-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            doctor_id: formData.get('doctor_id'),
            appointment_date: formData.get('appointment_date'),
            reason_for_visit: formData.get('reason_for_visit'),
            status: formData.get('status'),
            duration: formData.get('duration'),
            appointment_type: formData.get('appointment_type'),
            notes: formData.get('notes'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Appointment added:', data);
        getAppointments(); // Refresh the appointments list
    })
    .catch(error => console.error('Error adding appointment:', error));
}

// Function to edit an appointment (triggered by the Edit button)
function editAppointment(appointmentId) {
    fetch(`${apiUrl}/${appointmentId}`)
        .then(response => response.json())
        .then(appointment => {
            const form = document.getElementById('appointment-form');
            form.elements['appointment_id'].value = appointment.appointment_id;
            form.elements['patient_id'].value = appointment.patient_id;
            form.elements['doctor_id'].value = appointment.doctor_id;
            form.elements['appointment_date'].value = appointment.appointment_date;
            form.elements['reason_for_visit'].value = appointment.reason_for_visit;
            form.elements['status'].value = appointment.status;
            form.elements['duration'].value = appointment.duration;
            form.elements['appointment_type'].value = appointment.appointment_type;
            form.elements['notes'].value = appointment.notes;
        })
        .catch(error => console.error('Error fetching appointment data:', error));
}

// Function to delete an appointment
function deleteAppointment(appointmentId) {
    if (confirm('Are you sure you want to delete this appointment?')) {
        fetch(`${apiUrl}/${appointmentId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Appointment deleted:', data);
            getAppointments(); // Refresh the appointments list
        })
        .catch(error => console.error('Error deleting appointment:', error));
}

// Event listener for the form submission to add or update appointments
document.getElementById('appointment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const appointmentId = document.getElementById('appointment-form').elements['appointment_id'].value;
    if (appointmentId) {
        updateAppointment(appointmentId);
    } else {
        addAppointment(event);
    }
});

// Function to update an appointment's information
function updateAppointment(appointmentId) {
    const form = document.getElementById('appointment-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${appointmentId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            doctor_id: formData.get('doctor_id'),
            appointment_date: formData.get('appointment_date'),
            reason_for_visit: formData.get('reason_for_visit'),
            status: formData.get('status'),
            duration: formData.get('duration'),
            appointment_type: formData.get('appointment_type'),
            notes: formData.get('notes'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Appointment updated:', data);
        getAppointments(); // Refresh the appointments list
    })
    .catch(error => console.error('Error updating appointment:', error));
}

// Call getAppointments to initially load the appointments list
document.addEventListener('DOMContentLoaded', getAppointments);
// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/patients';

// Function to fetch all patients from the backend
function getPatients() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Patients:', data);
            displayPatients(data);
        })
        .catch(error => console.error('Error fetching patients:', error));
}

// Function to display patients in HTML
function displayPatients(patients) {
    const patientsTable = document.getElementById('patients-table');
    patientsTable.innerHTML = ''; // Clear the table before populating
    patients.forEach(patient => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${patient.first_name} ${patient.last_name}</td>
            <td>${patient.date_of_birth}</td>
            <td>${patient.gender}</td>
            <td>${patient.phone_number}</td>
            <td>${patient.email}</td>
            <td>${patient.status}</td>
            <td><button onclick="editPatient(${patient.patient_id})">Edit</button></td>
            <td><button onclick="deletePatient(${patient.patient_id})">Delete</button></td>
        `;
        patientsTable.appendChild(row);
    });
}

// Function to add a new patient
function addPatient(event) {
    event.preventDefault();
    
    const form = document.getElementById('patient-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            date_of_birth: formData.get('date_of_birth'),
            gender: formData.get('gender'),
            email: formData.get('email'),
            phone_number: formData.get('phone_number'),
            address: formData.get('address'),
            insurance_provider: formData.get('insurance_provider'),
            insurance_policy_number: formData.get('insurance_policy_number'),
            primary_care_physician: formData.get('primary_care_physician'),
            medical_history: formData.get('medical_history'),
            allergies: formData.get('allergies'),
            status: formData.get('status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Patient added:', data);
        getPatients(); // Refresh the patients list
    })
    .catch(error => console.error('Error adding patient:', error));
}

// Function to edit a patient's data (triggered by the Edit button)
function editPatient(patientId) {
    fetch(`${apiUrl}/${patientId}`)
        .then(response => response.json())
        .then(patient => {
            const form = document.getElementById('patient-form');
            form.elements['patient_id'].value = patient.patient_id;
            form.elements['first_name'].value = patient.first_name;
            form.elements['last_name'].value = patient.last_name;
            form.elements['date_of_birth'].value = patient.date_of_birth;
            form.elements['gender'].value = patient.gender;
            form.elements['email'].value = patient.email;
            form.elements['phone_number'].value = patient.phone_number;
            form.elements['address'].value = patient.address;
            form.elements['insurance_provider'].value = patient.insurance_provider;
            form.elements['insurance_policy_number'].value = patient.insurance_policy_number;
            form.elements['primary_care_physician'].value = patient.primary_care_physician;
            form.elements['medical_history'].value = patient.medical_history;
            form.elements['allergies'].value = patient.allergies;
            form.elements['status'].value = patient.status;
        })
        .catch(error => console.error('Error fetching patient data:', error));
}

// Function to delete a patient
function deletePatient(patientId) {
    if (confirm('Are you sure you want to delete this patient?')) {
        fetch(`${apiUrl}/${patientId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Patient deleted:', data);
            getPatients(); // Refresh the patients list
        })
        .catch(error => console.error('Error deleting patient:', error));
}

// Event listener for the form submission to add or update patients
document.getElementById('patient-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const patientId = document.getElementById('patient-form').elements['patient_id'].value;
    if (patientId) {
        updatePatient(patientId);
    } else {
        addPatient(event);
    }
});

// Function to update a patient's information
function updatePatient(patientId) {
    const form = document.getElementById('patient-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${patientId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            date_of_birth: formData.get('date_of_birth'),
            gender: formData.get('gender'),
            email: formData.get('email'),
            phone_number: formData.get('phone_number'),
            address: formData.get('address'),
            insurance_provider: formData.get('insurance_provider'),
            insurance_policy_number: formData.get('insurance_policy_number'),
            primary_care_physician: formData.get('primary_care_physician'),
            medical_history: formData.get('medical_history'),
            allergies: formData.get('allergies'),
            status: formData.get('status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Patient updated:', data);
        getPatients(); // Refresh the patients list
    })
    .catch(error => console.error('Error updating patient:', error));
}


// Call getPatients to initially load the patients list
document.addEventListener('DOMContentLoaded', getPatients);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/lab-tests';

// Function to fetch all lab tests from the backend
function getLabTests() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Lab Tests:', data);
            displayLabTests(data);
        })
        .catch(error => console.error('Error fetching lab tests:', error));
}

// Function to display lab tests in HTML
function displayLabTests(tests) {
    const testsTable = document.getElementById('lab-tests-table');
    testsTable.innerHTML = ''; // Clear the table before populating
    tests.forEach(test => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${test.patient.first_name} ${test.patient.last_name}</td>
            <td>${test.appointment.appointment_date}</td>
            <td>${test.test_name}</td>
            <td>${test.test_date}</td>
            <td>${test.test_status}</td>
            <td><button onclick="editLabTest(${test.test_id})">Edit</button></td>
            <td><button onclick="deleteLabTest(${test.test_id})">Delete</button></td>
        `;
        testsTable.appendChild(row);
    });
}

// Function to add a new lab test
function addLabTest(event) {
    event.preventDefault();
    
    const form = document.getElementById('lab-test-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            test_name: formData.get('test_name'),
            test_date: formData.get('test_date'),
            results: formData.get('results'),
            test_status: formData.get('test_status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Lab Test added:', data);
        getLabTests(); // Refresh the lab tests list
    })
    .catch(error => console.error('Error adding lab test:', error));
}

// Function to edit a lab test (triggered by the Edit button)
function editLabTest(testId) {
    fetch(`${apiUrl}/${testId}`)
        .then(response => response.json())
        .then(test => {
            const form = document.getElementById('lab-test-form');
            form.elements['test_id'].value = test.test_id;
            form.elements['patient_id'].value = test.patient_id;
            form.elements['appointment_id'].value = test.appointment_id;
            form.elements['test_name'].value = test.test_name;
            form.elements['test_date'].value = test.test_date;
            form.elements['results'].value = test.results;
            form.elements['test_status'].value = test.test_status;
        })
        .catch(error => console.error('Error fetching lab test data:', error));
}

// Function to delete a lab test
function deleteLabTest(testId) {
    if (confirm('Are you sure you want to delete this lab test?')) {
        fetch(`${apiUrl}/${testId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Lab Test deleted:', data);
            getLabTests(); // Refresh the lab tests list
        })
        .catch(error => console.error('Error deleting lab test:', error));
}

// Event listener for the form submission to add or update lab tests
document.getElementById('lab-test-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const testId = document.getElementById('lab-test-form').elements['test_id'].value;
    if (testId) {
        updateLabTest(testId);
    } else {
        addLabTest(event);
    }
});

// Function to update a lab test
function updateLabTest(testId) {
    const form = document.getElementById('lab-test-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${testId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            test_name: formData.get('test_name'),
            test_date: formData.get('test_date'),
            results: formData.get('results'),
            test_status: formData.get('test_status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Lab Test updated:', data);
        getLabTests(); // Refresh the lab tests list
    })
    .catch(error => console.error('Error updating lab test:', error));
}

// Call getLabTests to initially load the lab tests list
document.addEventListener('DOMContentLoaded', getLabTests);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com//api/medical_records';

// Function to fetch all medical records from the backend
function getMedicalRecords() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Medical Records:', data);
            displayMedicalRecords(data);
        })
        .catch(error => console.error('Error fetching medical records:', error));
}

// Function to display medical records in HTML
function displayMedicalRecords(records) {
    const recordsTable = document.getElementById('medical-records-table');
    recordsTable.innerHTML = ''; // Clear the table before populating
    records.forEach(record => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${record.patient.first_name} ${record.patient.last_name}</td>
            <td>${record.appointment.appointment_date}</td>
            <td>${record.diagnosis}</td>
            <td>${record.treatment_plan}</td>
            <td>${record.status}</td>
            <td><button onclick="editMedicalRecord(${record.record_id})">Edit</button></td>
            <td><button onclick="deleteMedicalRecord(${record.record_id})">Delete</button></td>
        `;
        recordsTable.appendChild(row);
    });
}

// Function to add a new medical record
function addMedicalRecord(event) {
    event.preventDefault();
    
    const form = document.getElementById('medical-record-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            diagnosis: formData.get('diagnosis'),
            treatment_plan: formData.get('treatment_plan'),
            note: formData.get('note'),
            status: formData.get('status'),
            attachments: formData.get('attachments'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Medical Record added:', data);
        getMedicalRecords(); // Refresh the medical records list
    })
    .catch(error => console.error('Error adding medical record:', error));
}

// Function to edit a medical record (triggered by the Edit button)
function editMedicalRecord(recordId) {
    fetch(`${apiUrl}/${recordId}`)
        .then(response => response.json())
        .then(record => {
            const form = document.getElementById('medical-record-form');
            form.elements['record_id'].value = record.record_id;
            form.elements['patient_id'].value = record.patient_id;
            form.elements['appointment_id'].value = record.appointment_id;
            form.elements['diagnosis'].value = record.diagnosis;
            form.elements['treatment_plan'].value = record.treatment_plan;
            form.elements['note'].value = record.note;
            form.elements['status'].value = record.status;
            form.elements['attachments'].value = record.attachments;
        })
        .catch(error => console.error('Error fetching medical record data:', error));
}

// Function to delete a medical record
function deleteMedicalRecord(recordId) {
    if (confirm('Are you sure you want to delete this medical record?')) {
        fetch(`${apiUrl}/${recordId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Medical Record deleted:', data);
            getMedicalRecords(); // Refresh the medical records list
        })
        .catch(error => console.error('Error deleting medical record:', error));
}

// Event listener for the form submission to add or update medical records
document.getElementById('medical-record-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const recordId = document.getElementById('medical-record-form').elements['record_id'].value;
    if (recordId) {
        updateMedicalRecord(recordId);
    } else {
        addMedicalRecord(event);
    }
});

// Function to update a medical record
function updateMedicalRecord(recordId) {
    const form = document.getElementById('medical-record-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${recordId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            diagnosis: formData.get('diagnosis'),
            treatment_plan: formData.get('treatment_plan'),
            note: formData.get('note'),
            status: formData.get('status'),
            attachments: formData.get('attachments'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Medical Record updated:', data);
        getMedicalRecords(); // Refresh the medical records list
    })
    .catch(error => console.error('Error updating medical record:', error));
}

// Call getMedicalRecords to initially load the medical records list
document.addEventListener('DOMContentLoaded', getMedicalRecords);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/prescriptions';

// Fetch all prescriptions from the backend
function getPrescriptions() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Prescriptions:', data);
            displayPrescriptions(data);
        })
        .catch(error => console.error('Error fetching prescriptions:', error));
}

// Display prescriptions in an HTML table
function displayPrescriptions(prescriptions) {
    const prescriptionsTable = document.getElementById('prescriptions-table');
    prescriptionsTable.innerHTML = ''; // Clear the table before populating
    prescriptions.forEach(prescription => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${prescription.medication_name}</td>
            <td>${prescription.dosage}</td>
            <td>${prescription.frequency}</td>
            <td>${prescription.start_date}</td>
            <td>${prescription.end_date ? prescription.end_date : 'N/A'}</td>
            <td>${prescription.status}</td>
            <td><button onclick="editPrescription(${prescription.prescription_id})">Edit</button></td>
            <td><button onclick="deletePrescription(${prescription.prescription_id})">Delete</button></td>
        `;
        prescriptionsTable.appendChild(row);
    });
}

// Add a new prescription
function addPrescription(event) {
    event.preventDefault();
    
    const form = document.getElementById('prescription-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            record_id: formData.get('record_id'),
            medication_name: formData.get('medication_name'),
            dosage: formData.get('dosage'),
            frequency: formData.get('frequency'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date'),
            instructions: formData.get('instructions'),
            status: formData.get('status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prescription added:', data);
        getPrescriptions(); // Refresh the prescriptions list
    })
    .catch(error => console.error('Error adding prescription:', error));
}

// Edit a prescription (triggered by the Edit button)
function editPrescription(prescriptionId) {
    fetch(`${apiUrl}/${prescriptionId}`)
        .then(response => response.json())
        .then(prescription => {
            const form = document.getElementById('prescription-form');
            form.elements['prescription_id'].value = prescription.prescription_id;
            form.elements['record_id'].value = prescription.record_id;
            form.elements['medication_name'].value = prescription.medication_name;
            form.elements['dosage'].value = prescription.dosage;
            form.elements['frequency'].value = prescription.frequency;
            form.elements['start_date'].value = prescription.start_date;
            form.elements['end_date'].value = prescription.end_date || '';
            form.elements['instructions'].value = prescription.instructions || '';
            form.elements['status'].value = prescription.status;
        })
        .catch(error => console.error('Error fetching prescription data:', error));
}

// Delete a prescription
function deletePrescription(prescriptionId) {
    if (confirm('Are you sure you want to delete this prescription?')) {
        fetch(`${apiUrl}/${prescriptionId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Prescription deleted:', data);
            getPrescriptions(); // Refresh the prescriptions list
        })
        .catch(error => console.error('Error deleting prescription:', error));
}

// Update an existing prescription
function updatePrescription(prescriptionId) {
    const form = document.getElementById('prescription-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${prescriptionId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            record_id: formData.get('record_id'),
            medication_name: formData.get('medication_name'),
            dosage: formData.get('dosage'),
            frequency: formData.get('frequency'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date'),
            instructions: formData.get('instructions'),
            status: formData.get('status'),
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prescription updated:', data);
        getPrescriptions(); // Refresh the prescriptions list
    })
    .catch(error => console.error('Error updating prescription:', error));
}

// Event listener for form submission (add or update prescription)
document.getElementById('prescription-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const prescriptionId = document.getElementById('prescription-form').elements['prescription_id'].value;
    if (prescriptionId) {
        updatePrescription(prescriptionId);
    } else {
        addPrescription(event);
    }
});

// Initialize by fetching the list of prescriptions when the page loads
document.addEventListener('DOMContentLoaded', getPrescriptions);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/prescriptions';

// Fetch all pharmacies from the backend
function getPharmacies() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Pharmacies:', data);
            displayPharmacies(data);
        })
        .catch(error => console.error('Error fetching pharmacies:', error));
}

// Display pharmacies in an HTML table
function displayPharmacies(pharmacies) {
    const pharmaciesTable = document.getElementById('pharmacies-table');
    pharmaciesTable.innerHTML = ''; // Clear the table before populating
    pharmacies.forEach(pharmacy => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${pharmacy.name}</td>
            <td>${pharmacy.address}</td>
            <td>${pharmacy.phone_number}</td>
            <td>${pharmacy.email}</td>
            <td><button onclick="editPharmacy(${pharmacy.pharmacy_id})">Edit</button></td>
            <td><button onclick="deletePharmacy(${pharmacy.pharmacy_id})">Delete</button></td>
        `;
        pharmaciesTable.appendChild(row);
    });
}

// Add a new pharmacy
function addPharmacy(event) {
    event.preventDefault();
    
    const form = document.getElementById('pharmacy-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: formData.get('name'),
            address: formData.get('address'),
            phone_number: formData.get('phone_number'),
            email: formData.get('email')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Pharmacy added:', data);
        getPharmacies(); // Refresh the pharmacies list
    })
    .catch(error => console.error('Error adding pharmacy:', error));
}

// Edit a pharmacy (triggered by the Edit button)
function editPharmacy(pharmacyId) {
    fetch(`${apiUrl}/${pharmacyId}`)
        .then(response => response.json())
        .then(pharmacy => {
            const form = document.getElementById('pharmacy-form');
            form.elements['pharmacy_id'].value = pharmacy.pharmacy_id;
            form.elements['name'].value = pharmacy.name;
            form.elements['address'].value = pharmacy.address;
            form.elements['phone_number'].value = pharmacy.phone_number;
            form.elements['email'].value = pharmacy.email;
        })
        .catch(error => console.error('Error fetching pharmacy data:', error));
}

// Delete a pharmacy
function deletePharmacy(pharmacyId) {
    if (confirm('Are you sure you want to delete this pharmacy?')) {
        fetch(`${apiUrl}/${pharmacyId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Pharmacy deleted:', data);
            getPharmacies(); // Refresh the pharmacies list
        })
        .catch(error => console.error('Error deleting pharmacy:', error));
}

// Update an existing pharmacy
function updatePharmacy(pharmacyId) {
    const form = document.getElementById('pharmacy-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${pharmacyId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: formData.get('name'),
            address: formData.get('address'),
            phone_number: formData.get('phone_number'),
            email: formData.get('email')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Pharmacy updated:', data);
        getPharmacies(); // Refresh the pharmacies list
    })
    .catch(error => console.error('Error updating pharmacy:', error));
}

// Event listener for form submission (add or update pharmacy)
document.getElementById('pharmacy-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const pharmacyId = document.getElementById('pharmacy-form').elements['pharmacy_id'].value;
    if (pharmacyId) {
        updatePharmacy(pharmacyId);
    } else {
        addPharmacy(event);
    }
});

// Initialize by fetching the list of pharmacies when the page loads
document.addEventListener('DOMContentLoaded', getPharmacies);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/payments';

// Fetch all payments from the backend
function getPayments() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Payments:', data);
            displayPayments(data);
        })
        .catch(error => console.error('Error fetching payments:', error));
}

// Display payments in an HTML table
function displayPayments(payments) {
    const paymentsTable = document.getElementById('payments-table');
    paymentsTable.innerHTML = ''; // Clear the table before populating
    payments.forEach(payment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${payment.billing_id}</td>
            <td>${payment.patient_id}</td>
            <td>${payment.appointment_id}</td>
            <td>${payment.total_amount}</td>
            <td>${payment.amount_paid}</td>
            <td>${payment.balance_due}</td>
            <td>${payment.payment_status}</td>
            <td>${payment.payment_date}</td>
            <td>${payment.insurance_claimed_amount}</td>
            <td>${payment.insurance_status}</td>
            <td><button onclick="editPayment(${payment.billing_id})">Edit</button></td>
            <td><button onclick="deletePayment(${payment.billing_id})">Delete</button></td>
        `;
        paymentsTable.appendChild(row);
    });
}

// Add a new payment
function addPayment(event) {
    event.preventDefault();
    
    const form = document.getElementById('payment-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            total_amount: formData.get('total_amount'),
            amount_paid: formData.get('amount_paid'),
            balance_due: formData.get('balance_due'),
            payment_status: formData.get('payment_status'),
            payment_date: formData.get('payment_date'),
            insurance_claimed_amount: formData.get('insurance_claimed_amount'),
            insurance_status: formData.get('insurance_status')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Payment added:', data);
        getPayments(); // Refresh the payments list
    })
    .catch(error => console.error('Error adding payment:', error));
}

// Edit a payment (triggered by the Edit button)
function editPayment(billingId) {
    fetch(`${apiUrl}/${billingId}`)
        .then(response => response.json())
        .then(payment => {
            const form = document.getElementById('payment-form');
            form.elements['billing_id'].value = payment.billing_id;
            form.elements['patient_id'].value = payment.patient_id;
            form.elements['appointment_id'].value = payment.appointment_id;
            form.elements['total_amount'].value = payment.total_amount;
            form.elements['amount_paid'].value = payment.amount_paid;
            form.elements['balance_due'].value = payment.balance_due;
            form.elements['payment_status'].value = payment.payment_status;
            form.elements['payment_date'].value = payment.payment_date;
            form.elements['insurance_claimed_amount'].value = payment.insurance_claimed_amount;
            form.elements['insurance_status'].value = payment.insurance_status;
        })
        .catch(error => console.error('Error fetching payment data:', error));
}

// Delete a payment
function deletePayment(billingId) {
    if (confirm('Are you sure you want to delete this payment?')) {
        fetch(`${apiUrl}/${billingId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Payment deleted:', data);
            getPayments(); // Refresh the payments list
        })
        .catch(error => console.error('Error deleting payment:', error));
}

// Update an existing payment
function updatePayment(billingId) {
    const form = document.getElementById('payment-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${billingId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: formData.get('patient_id'),
            appointment_id: formData.get('appointment_id'),
            total_amount: formData.get('total_amount'),
            amount_paid: formData.get('amount_paid'),
            balance_due: formData.get('balance_due'),
            payment_status: formData.get('payment_status'),
            payment_date: formData.get('payment_date'),
            insurance_claimed_amount: formData.get('insurance_claimed_amount'),
            insurance_status: formData.get('insurance_status')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Payment updated:', data);
        getPayments(); // Refresh the payments list
    })
    .catch(error => console.error('Error updating payment:', error));
}

// Event listener for form submission (add or update payment)
document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const billingId = document.getElementById('payment-form').elements['billing_id'].value;
    if (billingId) {
        updatePayment(billingId);
    } else {
        addPayment(event);
    }
});

// Initialize by fetching the list of payments when the page loads
document.addEventListener('DOMContentLoaded', getPayments);

// Define the base URL for API interaction
const apiUrl = 'http://medical.com/api/insurance';

// Fetch all insurance records from the backend
function getInsurance() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Insurance records:', data);
            displayInsurance(data);
        })
        .catch(error => console.error('Error fetching insurance records:', error));
}

// Display insurance records in an HTML table
function displayInsurance(insuranceRecords) {
    const insuranceTable = document.getElementById('insurance-table');
    insuranceTable.innerHTML = ''; // Clear the table before populating
    insuranceRecords.forEach(record => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${record.insurance_id}</td>
            <td>${record.provider_name}</td>
            <td>${record.policy_number}</td>
            <td>${record.coverage_type}</td>
            <td>${record.coverage_amount}</td>
            <td>${record.patient_id}</td>
            <td>${record.start_date}</td>
            <td>${record.end_date}</td>
            <td><button onclick="editInsurance(${record.insurance_id})">Edit</button></td>
            <td><button onclick="deleteInsurance(${record.insurance_id})">Delete</button></td>
        `;
        insuranceTable.appendChild(row);
    });
}

// Add a new insurance record
function addInsurance(event) {
    event.preventDefault();

    const form = document.getElementById('insurance-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            provider_name: formData.get('provider_name'),
            policy_number: formData.get('policy_number'),
            coverage_type: formData.get('coverage_type'),
            coverage_amount: formData.get('coverage_amount'),
            patient_id: formData.get('patient_id'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Insurance added:', data);
        getInsurance(); // Refresh the insurance list
    })
    .catch(error => console.error('Error adding insurance:', error));
}

// Edit an insurance record (triggered by the Edit button)
function editInsurance(insuranceId) {
    fetch(`${apiUrl}/${insuranceId}`)
        .then(response => response.json())
        .then(record => {
            const form = document.getElementById('insurance-form');
            form.elements['insurance_id'].value = record.insurance_id;
            form.elements['provider_name'].value = record.provider_name;
            form.elements['policy_number'].value = record.policy_number;
            form.elements['coverage_type'].value = record.coverage_type;
            form.elements['coverage_amount'].value = record.coverage_amount;
            form.elements['patient_id'].value = record.patient_id;
            form.elements['start_date'].value = record.start_date;
            form.elements['end_date'].value = record.end_date;
        })
        .catch(error => console.error('Error fetching insurance data:', error));
}

// Delete an insurance record
function deleteInsurance(insuranceId) {
    if (confirm('Are you sure you want to delete this insurance record?')) {
        fetch(`${apiUrl}/${insuranceId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Insurance deleted:', data);
            getInsurance(); // Refresh the insurance list
        })
        .catch(error => console.error('Error deleting insurance:', error));
}

// Update an existing insurance record
function updateInsurance(insuranceId) {
    const form = document.getElementById('insurance-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${insuranceId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            provider_name: formData.get('provider_name'),
            policy_number: formData.get('policy_number'),
            coverage_type: formData.get('coverage_type'),
            coverage_amount: formData.get('coverage_amount'),
            patient_id: formData.get('patient_id'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Insurance updated:', data);
        getInsurance(); // Refresh the insurance list
    })
    .catch(error => console.error('Error updating insurance:', error));
}

// Event listener for form submission (add or update insurance)
document.getElementById('insurance-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const insuranceId = document.getElementById('insurance-form').elements['insurance_id'].value;
    if (insuranceId) {
        updateInsurance(insuranceId);
    } else {
        addInsurance(event);
    }
});

// Initialize by fetching the list of insurance records when the page loads
document.addEventListener('DOMContentLoaded', getInsurance);

// Define the base URL for the API
const apiUrl = 'http://medical.com/api/users'; // Update this URL to your API endpoint

// Fetch all users from the backend
function getUsers() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log('Users:', data);
            displayUsers(data); // Call to display the users
        })
        .catch(error => console.error('Error fetching users:', error));
}

// Display users in an HTML table
function displayUsers(users) {
    const userTable = document.getElementById('user-table');
    userTable.innerHTML = ''; // Clear the table before populating
    users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.email}</td>
            <td>${user.role}</td>
            <td><button onclick="editUser(${user.id})">Edit</button></td>
            <td><button onclick="deleteUser(${user.id})">Delete</button></td>
        `;
        userTable.appendChild(row);
    });
}

// Add a new user
function addUser(event) {
    event.preventDefault();

    const form = document.getElementById('user-form');
    const formData = new FormData(form);

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: formData.get('username'),
            email: formData.get('email'),
            password: formData.get('password'),
            role: formData.get('role')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('User added:', data);
        getUsers(); // Refresh the users list
    })
    .catch(error => console.error('Error adding user:', error));
}

// Edit an existing user (triggered by the Edit button)
function editUser(userId) {
    fetch(`${apiUrl}/${userId}`)
        .then(response => response.json())
        .then(user => {
            const form = document.getElementById('user-form');
            form.elements['user_id'].value = user.id;
            form.elements['username'].value = user.username;
            form.elements['email'].value = user.email;
            form.elements['role'].value = user.role;
        })
        .catch(error => console.error('Error fetching user data:', error));
}

// Delete a user
function deleteUser(userId) {
    if (confirm('Are you sure you want to delete this user?')) {
        fetch(`${apiUrl}/${userId}`, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('User deleted:', data);
            getUsers(); // Refresh the users list
        })
        .catch(error => console.error('Error deleting user:', error));
}

// Update an existing user
function updateUser(userId) {
    const form = document.getElementById('user-form');
    const formData = new FormData(form);

    fetch(`${apiUrl}/${userId}`, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: formData.get('username'),
            email: formData.get('email'),
            password: formData.get('password'),
            role: formData.get('role')
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('User updated:', data);
        getUsers(); // Refresh the users list
    })
    .catch(error => console.error('Error updating user:', error));
}

// Event listener for form submission (add or update user)
document.getElementById('user-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const userId = document.getElementById('user-form').elements['user_id'].value;
    if (userId) {
        updateUser(userId); // Update existing user
    } else {
        addUser(event); // Add new user
    }
});

// Initialize by fetching the list of users when the page loads
document.addEventListener('DOMContentLoaded', getUsers);




