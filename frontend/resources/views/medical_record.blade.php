@extends('layouts.app')

@section('title', isset($medicalRecord) ? 'Edit Medical Record' : 'Create New Medical Record')

@section('content')
<div class="container">
    <h1>{{ isset($medicalRecord) ? 'Edit Medical Record' : 'Create New Medical Record' }}</h1>

    <!-- Form to create or update a medical record -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($medicalRecord) ? 'Update Medical Record' : 'Create Medical Record' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($medicalRecord) ? route('medical_records.update', $medicalRecord->record_id) : route('medical_records.store') }}" method="POST" enctype="multipart/form-data">
                @csrf
                @if(isset($medicalRecord))
                    @method('PUT')
                @endif

                <!-- Patient selection (dropdown) -->
                <div class="form-group">
                    <label for="patient_id">Patient</label>
                    <select class="form-control" id="patient_id" name="patient_id" required>
                        @foreach($patients as $patient)
                            <option value="{{ $patient->patient_id }}" {{ (isset($medicalRecord) && $medicalRecord->patient_id == $patient->patient_id) ? 'selected' : '' }}>
                                {{ $patient->first_name }} {{ $patient->last_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Appointment selection (dropdown) -->
                <div class="form-group">
                    <label for="appointment_id">Appointment</label>
                    <select class="form-control" id="appointment_id" name="appointment_id" required>
                        @foreach($appointments as $appointment)
                            <option value="{{ $appointment->appointment_id }}" {{ (isset($medicalRecord) && $medicalRecord->appointment_id == $appointment->appointment_id) ? 'selected' : '' }}>
                                Appointment #{{ $appointment->appointment_id }} - {{ $appointment->appointment_date }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Diagnosis -->
                <div class="form-group">
                    <label for="diagnosis">Diagnosis</label>
                    <input type="text" class="form-control" id="diagnosis" name="diagnosis" value="{{ old('diagnosis', isset($medicalRecord) ? $medicalRecord->diagnosis : '') }}" maxlength="500" required>
                </div>

                <!-- Treatment Plan -->
                <div class="form-group">
                    <label for="treatment_plan">Treatment Plan</label>
                    <textarea class="form-control" id="treatment_plan" name="treatment_plan" rows="4">{{ old('treatment_plan', isset($medicalRecord) ? $medicalRecord->treatment_plan : '') }}</textarea>
                </div>

                <!-- Notes -->
                <div class="form-group">
                    <label for="note">Notes</label>
                    <textarea class="form-control" id="note" name="note" rows="4">{{ old('note', isset($medicalRecord) ? $medicalRecord->note : '') }}</textarea>
                </div>

                <!-- Status -->
                <div class="form-group">
                    <label for="status">Status</label>
                    <select class="form-control" id="status" name="status">
                        <option value="Active" {{ (isset($medicalRecord) && $medicalRecord->status == 'Active') ? 'selected' : '' }}>Active</option>
                        <option value="Archived" {{ (isset($medicalRecord) && $medicalRecord->status == 'Archived') ? 'selected' : '' }}>Archived</option>
                        <option value="Inactive" {{ (isset($medicalRecord) && $medicalRecord->status == 'Inactive') ? 'selected' : '' }}>Inactive</option>
                    </select>
                </div>

                <!-- Attachments -->
                <div class="form-group">
                    <label for="attachments">Attachments</label>
                    <input type="file" class="form-control-file" id="attachments" name="attachments" accept="image/*,application/pdf">
                    @if(isset($medicalRecord) && $medicalRecord->attachments)
                        <small class="form-text text-muted">
                            Current attachment: <a href="{{ asset('storage/' . $medicalRecord->attachments) }}" target="_blank">View</a>
                        </small>
                    @endif
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($medicalRecord) ? 'Update Medical Record' : 'Create Medical Record' }}</button>
            </form>
        </div>
    </div>
</div>
@endsection