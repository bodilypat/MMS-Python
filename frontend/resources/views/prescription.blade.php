@extends('layouts.app')

@section('title', isset($prescription) ? 'Edit Prescription' : 'Create New Prescription')

@section('content')
<div class="container">
    <h1>{{ isset($prescription) ? 'Edit Prescription' : 'Create New Prescription' }}</h1>

    <!-- Form to create or update a prescription -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($prescription) ? 'Update Prescription' : 'Create Prescription' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($prescription) ? route('prescriptions.update', $prescription->prescription_id) : route('prescriptions.store') }}" method="POST">
                @csrf
                @if(isset($prescription))
                    @method('PUT')
                @endif

                <!-- Record selection (dropdown) -->
                <div class="form-group">
                    <label for="record_id">Medical Record</label>
                    <select class="form-control" id="record_id" name="record_id" required>
                        @foreach($medicalRecords as $record)
                            <option value="{{ $record->record_id }}" {{ (isset($prescription) && $prescription->record_id == $record->record_id) ? 'selected' : '' }}>
                                Record #{{ $record->record_id }} - {{ $record->patient_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Medication Name -->
                <div class="form-group">
                    <label for="medication_name">Medication Name</label>
                    <input type="text" class="form-control" id="medication_name" name="medication_name" value="{{ old('medication_name', isset($prescription) ? $prescription->medication_name : '') }}" required>
                </div>

                <!-- Dosage -->
                <div class="form-group">
                    <label for="dosage">Dosage</label>
                    <input type="text" class="form-control" id="dosage" name="dosage" value="{{ old('dosage', isset($prescription) ? $prescription->dosage : '') }}" required>
                </div>

                <!-- Frequency -->
                <div class="form-group">
                    <label for="frequency">Frequency</label>
                    <input type="text" class="form-control" id="frequency" name="frequency" value="{{ old('frequency', isset($prescription) ? $prescription->frequency : '') }}" required>
                </div>

                <!-- Start Date -->
                <div class="form-group">
                    <label for="start_date">Start Date</label>
                    <input type="date" class="form-control" id="start_date" name="start_date" value="{{ old('start_date', isset($prescription) ? $prescription->start_date : '') }}" required>
                </div>

                <!-- End Date -->
                <div class="form-group">
                    <label for="end_date">End Date</label>
                    <input type="date" class="form-control" id="end_date" name="end_date" value="{{ old('end_date', isset($prescription) ? $prescription->end_date : '') }}">
                </div>

                <!-- Instructions -->
                <div class="form-group">
                    <label for="instructions">Instructions</label>
                    <textarea class="form-control" id="instructions" name="instructions">{{ old('instructions', isset($prescription) ? $prescription->instructions : '') }}</textarea>
                </div>

                <!-- Status -->
                <div class="form-group">
                    <label for="status">Status</label>
                    <select class="form-control" id="status" name="status">
                        <option value="Active" {{ (isset($prescription) && $prescription->status == 'Active') ? 'selected' : '' }}>Active</option>
                        <option value="Completed" {{ (isset($prescription) && $prescription->status == 'Completed') ? 'selected' : '' }}>Completed</option>
                        <option value="Expired" {{ (isset($prescription) && $prescription->status == 'Expired') ? 'selected' : '' }}>Expired</option>
                        <option value="Cancelled" {{ (isset($prescription) && $prescription->status == 'Cancelled') ? 'selected' : '' }}>Cancelled</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($prescription) ? 'Update Prescription' : 'Create Prescription' }}</button>
            </form>
        </div>
    </div>
</div>
@endsection