@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Add New Prescription</h1>
        <form action="{{ route('prescriptions.store') }}" method="POST">
            @csrf
            <div class="form-group">
                <label for="patient_id">Patient</label>
                <select name="patient_id" id="patient_id" class="form-control" required>
                    @foreach($patients as $patient)
                        <option value="{{ $patient->id }}">{{ $patient->name }}</option>
                    @endforeach
                </select>
            </div>
            <div class="form-group">
                <label for="doctor_id">Doctor</label>
                <select name="doctor_id" id="doctor_id" class="form-control" required>
                    @foreach($doctors as $doctor)
                        <option value="{{ $doctor->id }}">{{ $doctor->name }}</option>
                    @endforeach
                </select>
            </div>
            <div class="form-group">
                <label for="medication">Medication</label>
                <input type="text" name="medication" id="medication" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="dosage">Dosage</label>
                <input type="text" name="dosage" id="dosage" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="instructions">Instructions</label>
                <textarea name="instructions" id="instructions" class="form-control"></textarea>
            </div>
            <div class="form-group">
                <label for="issued_at">Issued At</label>
                <input type="datetime-local" name="issued_at" id="issued_at" class="form-control">
            </div>
            <button type="submit" class="btn btn-primary">Save Prescription</button>
        </form>
    </div>
@endsection
