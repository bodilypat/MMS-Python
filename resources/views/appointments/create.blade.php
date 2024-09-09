<!DOCTYPE html>
<html>
<head>
    <title>Schedule Appointment</title>
</head>
<body>
    <h1>Schedule New Appointment</h1>
    <form action="{{ route('appointments.store') }}" method="POST">
        @csrf
        <label for="patient_id">Patient:</label>
        <select id="patient_id" name="patient_id" required>
            @foreach($patients as $patient)
                <option value="{{ $patient->id }}">{{ $patient->name }}</option>
            @endforeach
        </select>
        <br>
        <label for="doctor_id">Doctor:</label>
        <select id="doctor_id" name="doctor_id" required>
            @foreach($doctors as $doctor)
                <option value="{{ $doctor->id }}">{{ $doctor->name }}</option>
            @endforeach
        </select>
        <br>
        <label for="appointment_date">Date and Time:</label>
        <input type="datetime-local" id="appointment_date" name="appointment_date" required>
        <br>
        <label for="status">Status:</label>
        <select id="status" name="status" required>
            <option value="scheduled">Scheduled</option>
            <option value="completed">Completed</option>
            <option value="canceled">Canceled</option>
        </select>
        <br>
        <button type="submit">Schedule Appointment</button>
    </form>
</body>
</html>
