<!DOCTYPE html>
<html>
<head>
    <title>Prescription Details</title>
</head>
<body>
    <h1>Prescription Details</h1>
    <p><strong>Patient:</strong> {{ $prescription->patient->name }}</p>
    <p><strong>Doctor:</strong> {{ $prescription->doctor->name }}</p>
    <p><strong>Medication:</strong> {{ $prescription->medication }}</p>
    <p><strong>Dosage:</strong> {{ $prescription->dosage }}</p>
    <p><strong>Instructions:</strong> {{ $prescription->instructions }}</p>
    <p><strong>Date:</strong> {{ $prescription->date->format('Y-m-d') }}</p>
    <a href="{{ route('prescriptions.edit', $prescription) }}">Edit</a>
    <form action="{{ route('prescriptions.destroy', $prescription) }}" method="POST" style="display:inline;">
        @csrf
        @method('DELETE')
        <button type="submit">Delete Prescription</button>
    </form>
    <br>
    <a href="{{ route('prescriptions.index') }}">Back to list</a>
</body>
</html>
