<!DOCTYPE html>
<html>
<head>
    <title>Patient Details</title>
</head>
<body>
    <h1>Patient Details</h1>
    <p><strong>Name:</strong> {{ $patient->name }}</p>
    <p><strong>Email:</strong> {{ $patient->email }}</p>
    <p><strong>Phone:</strong> {{ $patient->phone }}</p>
    <p><strong>Address:</strong> {{ $patient->address }}</p>
    <p><strong>Date of Birth:</strong> {{ $patient->dob->format('Y-m-d') }}</p>
    <a href="{{ route('patients.edit', $patient) }}">Edit</a>
    <form action="{{ route('patients.destroy', $patient) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit">Delete Patient</button>
    </form>
    <br>
    <a href="{{ route('patients.index') }}">Back to list</a>
</body>
</html>
