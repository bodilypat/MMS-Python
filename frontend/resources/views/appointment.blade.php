@extends('layouts.app')

@section('title', isset($appointment) ? 'Edit Appointment' : 'Schedule New Appointment')

@section('content')
<div class="container">
    <h1>{{ isset($appointment) ? 'Edit Appointment' : 'Schedule New Appointment' }}</h1>

    <!-- Form to create or update an appointment -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($appointment) ? 'Update Appointment' : 'Schedule Appointment' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($appointment) ? route('appointments.update', $appointment->appointment_id) : route('appointments.store') }}" method="POST">
                @csrf
                @if(isset($appointment))
                    @method('PUT')
                @endif

                <!-- Patient selection (dropdown) -->
                <div class="form-group">
                    <label for="patient_id">Patient</label>
                    <select class="form-control" id="patient_id" name="patient_id" required>
                        @foreach($patients as $patient)
                            <option value="{{ $patient->patient_id }}" {{ (isset($appointment) && $appointment->patient_id == $patient->patient_id) ? 'selected' : '' }}>
                                {{ $patient->first_name }} {{ $patient->last_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Doctor selection (dropdown) -->
                <div class="form-group">
                    <label for="doctor_id">Doctor</label>
                    <select class="form-control" id="doctor_id" name="doctor_id" required>
                        @foreach($doctors as $doctor)
                            <option value="{{ $doctor->doctor_id }}" {{ (isset($appointment) && $appointment->doctor_id == $doctor->doctor_id) ? 'selected' : '' }}>
                                Dr. {{ $doctor->first_name }} {{ $doctor->last_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Appointment Date -->
                <div class="form-group">
                    <label for="appointment_date">Appointment Date</label>
                    <input type="datetime-local" class="form-control" id="appointment_date" name="appointment_date" value="{{ old('appointment_date', isset($appointment) ? $appointment->appointment_date : '') }}" required>
                </div>

                <!-- Reason for Visit -->
                <div class="form-group">
                    <label for="reason_for_visit">Reason for Visit</label>
                    <input type="text" class="form-control" id="reason_for_visit" name="reason_for_visit" value="{{ old('reason_for_visit', isset($appointment) ? $appointment->reason_for_visit : '') }}">
                </div>

                <!-- Status -->
                <div class="form-group">
                    <label for="status">Status</label>
                    <select class="form-control" id="status" name="status">
                        <option value="Scheduled" {{ (isset($appointment) && $appointment->status == 'Scheduled') ? 'selected' : '' }}>Scheduled</option>
                        <option value="Completed" {{ (isset($appointment) && $appointment->status == 'Completed') ? 'selected' : '' }}>Completed</option>
                        <option value="Cancelled" {{ (isset($appointment) && $appointment->status == 'Cancelled') ? 'selected' : '' }}>Cancelled</option>
                        <option value="No-Show" {{ (isset($appointment) && $appointment->status == 'No-Show') ? 'selected' : '' }}>No-Show</option>
                    </select>
                </div>

                <!-- Duration -->
                <div class="form-group">
                    <label for="duration">Duration (in minutes)</label>
                    <input type="number" class="form-control" id="duration" name="duration" value="{{ old('duration', isset($appointment) ? $appointment->duration : '') }}" required>
                </div>

                <!-- Appointment Type -->
                <div class="form-group">
                    <label for="appointment_type">Appointment Type</label>
                    <input type="text" class="form-control" id="appointment_type" name="appointment_type" value="{{ old('appointment_type', isset($appointment) ? $appointment->appointment_type : '') }}">
                </div>

                <!-- Notes -->
                <div class="form-group">
                    <label for="notes">Notes</label>
                    <textarea class="form-control" id="notes" name="notes">{{ old('notes', isset($appointment) ? $appointment->notes : '') }}</textarea>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($appointment) ? 'Update Appointment' : 'Schedule Appointment' }}</button>
            </form>
        </div>
    </div>
</div>
@endsection