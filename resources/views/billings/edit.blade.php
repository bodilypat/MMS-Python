<!DOCTYPE html>
<html>
<head>
    <title>Edit Appointment</title>
</head>
<body>
    <h1>Edit Appointment</h1>
    <form action="{{ route('appointments.update', $appointment) }}" method="POST">
        @csrf
        @method('PUT')
        <label for="patient_id">Patient:</label>
        <select id="patient_id" name="patient_id" required>
            @foreach($patients as $patient)
                <option value="{{ $patient->id }}" {{ $patient->id == $appointment->patient_id ? 'selected' : '' }}>
                    {{ $patient->name }}
                </option>
            @endforeach
        </select>
        <br>
        <label for="doctor_id">Doctor:</label>
        <select id="doctor_id" name="doctor_id" required>
            @foreach($doctors as $doctor)
                <option value="{{ $doctor->id }}" {{ $doctor->id == $appointment->doctor_id ? 'selected' : '' }}>
                    {{ $doctor->name }}
                </option>
            @endforeach
        </select>
        <br>
        <label for="appointment_date">Date and Time:</label>
        <input type="datetime-local" id="appointment_date" name="appointment_date" value="{{ $appointment->appointment_date->format('Y-m-d\TH:i') }}" required>
        <br>
        <label for="status">Status:</label>
        <select id="status" name="status" required>
            <option value="scheduled" {{ $appointment->status == 'scheduled' ? 'selected' : '' }}>Scheduled</option>
            <option value="completed" {{ $appointment->status == 'completed' ? 'selected' : '' }}>Completed</option>
            <option value="canceled" {{ $appointment->status == 'canceled' ? 'selected' : '' }}>Canceled</option>
        </select>
        <br>
        <button type="submit">Update Appointment</button>
    </form>
</body>
</html>
