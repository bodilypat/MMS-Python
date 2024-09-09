<!DOCTYPE html>
<html>
<head>
    <title>Add Medical Record</title>
</head>
<body>
    <h1>Add New Medical Record</h1>
    <form action="{{ route('medical-records.store') }}" method="POST">
        @csrf
        <label for="patient_id">Patient:</label>
        <select id="patient_id" name="patient_id" required>
            @foreach($patients as $patient)
                <option value="{{ $patient->id }}">{{ $patient->name }}</option>
            @endforeach
        </select>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        <br>
        <label for="diagnosis">Diagnosis:</label>
        <textarea id="diagnosis" name="diagnosis" required></textarea>
        <br>
        <label for="treatment">Treatment:</label>
        <textarea id="treatment" name="treatment"></textarea>
        <br>
        <label for="notes">Notes:</label>
        <textarea id="notes" name="notes"></textarea>
        <br>
        <button type="submit">Add Record</button>
    </form>
</body>
</html>
