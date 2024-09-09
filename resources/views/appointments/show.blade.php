<!DOCTYPE html>
<html>
<head>
    <title>Appointment Details</title>
</head>
<body>
    <h1>Appointment Details</h1>
    <p><strong>Patient:</strong> {{ $appointment->patient->name }}</p>
    <p><strong>Doctor:</strong> {{ $appointment->doctor->name }}</p>
    <p><strong>Date and Time:</strong> {{ $appointment->appointment_date->format('Y-m-d H:i') }}</p>
    <p><strong>Status:</strong> {{ $appointment->status }}</p>
    <a href="{{ route('appointments.edit', $appointment) }}">Edit</a>
    <form action="{{ route('appointments.destroy', $appointment) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit">Cancel Appointment</button>
    </form>
    <br>
    <a href="{{ route('appointments.index') }}">Back to list</a>
</body>
</html>
