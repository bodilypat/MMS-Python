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
