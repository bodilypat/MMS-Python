<!DOCTYPE html>
<html>
<head>
    <title>Edit Prescription</title>
</head>
<body>
    <h1>Edit Prescription</h1>
    <form action="{{ route('prescriptions.update', $prescription) }}" method="POST">
        @csrf
        @method('PUT')
        <label for="patient_id">Patient:</label>
        <select id="patient_id" name="patient_id" required>
            @foreach($patients as $patient)
                <option value="{{ $patient->id }}" {{ $patient->id == $prescription->patient_id ? 'selected' : '' }}>
                    {{ $patient->name }}
                </option>
            @endforeach
        </select>
        <br>
        <label for="doctor_id">Doctor:</label>
        <select id="doctor_id" name="doctor_id" required>
            @foreach($doctors as $doctor)
                <option value="{{ $doctor->id }}" {{ $doctor->id == $prescription->doctor_id ? 'selected' : '' }}>
                    {{ $doctor->name }}
                </option>
            @endforeach
        </select>
        <br>
        <label for="medication">Medication:</label>
        <input type="text" id="medication" name="medication" value="{{ $prescription->medication }}" required>
        <br>
        <label for="dosage">Dosage:</label>
        <input type="text" id="dosage" name="dosage" value="{{ $prescription->dosage }}" required>
        <br>
        <label for="instructions">Instructions:</label>
        <textarea id="instructions" name="instructions">{{ $prescription->instructions }}</textarea>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" value="{{ $prescription->date->format('Y-m-d') }}" required>
        <br>
        <button type="submit">Update Prescription</button>
    </form>
</body>
</html>
