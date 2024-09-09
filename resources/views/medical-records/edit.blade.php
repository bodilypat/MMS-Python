<!DOCTYPE html>
<html>
<head>
    <title>Edit Medical Record</title>
</head>
<body>
    <h1>Edit Medical Record</h1>
    <form action="{{ route('medical-records.update', $medicalRecord) }}" method="POST">
        @csrf
        @method('PUT')
        <label for="patient_id">Patient:</label>
        <select id="patient_id" name="patient_id" required>
            @foreach($patients as $patient)
                <option value="{{ $patient->id }}" {{ $patient->id == $medicalRecord->patient_id ? 'selected' : '' }}>
                    {{ $patient->name }}
                </option>
            @endforeach
        </select>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" value="{{ $medicalRecord->date->format('Y-m-d') }}" required>
        <br>
        <label for="diagnosis">Diagnosis:</label>
        <textarea id="diagnosis" name="diagnosis" required>{{ $medicalRecord->diagnosis }}</textarea>
        <br>
        <label for="treatment">Treatment:</label>
        <textarea id="treatment" name="treatment">{{ $medicalRecord->treatment }}</textarea>
        <br>
        <label for="notes">Notes:</label>
        <textarea id="notes" name="notes">{{ $medicalRecord->notes }}</textarea>
        <br>
        <button type="submit">Update Record</button>
    </form>
</body>
</html>
