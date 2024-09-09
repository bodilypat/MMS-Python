<!DOCTYPE html>
<html>
<head>
    <title>Medical Record Details</title>
</head>
<body>
    <h1>Medical Record Details</h1>
    <p><strong>Patient:</strong> {{ $medicalRecord->patient->name }}</p>
    <p><strong>Date:</strong> {{ $medicalRecord->date->format('Y-m-d') }}</p>
    <p><strong>Diagnosis:</strong> {{ $medicalRecord->diagnosis }}</p>
    <p><strong>Treatment:</strong> {{ $medicalRecord->treatment }}</p>
    <p><strong>Notes:</strong> {{ $medicalRecord->notes }}</p>
    <a href="{{ route('medical-records.edit', $medicalRecord) }}">Edit</a>
    <form action="{{ route('medical-records.destroy', $medicalRecord) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit">Delete Record</button>
    </form>
    <br>
    <a href="{{ route('medical-records.index') }}">Back to list</a>
</body>
</html>
