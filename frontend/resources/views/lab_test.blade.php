@extends('layouts.app')

@section('title', isset($labTest) ? 'Edit Lab Test' : 'Create New Lab Test')

@section('content')
<div class="container">
    <h1>{{ isset($labTest) ? 'Edit Lab Test' : 'Create New Lab Test' }}</h1>

    <!-- Form to create or update a lab test -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($labTest) ? 'Update Lab Test' : 'Create Lab Test' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($labTest) ? route('lab_tests.update', $labTest->test_id) : route('lab_tests.store') }}" method="POST">
                @csrf
                @if(isset($labTest))
                    @method('PUT')
                @endif

                <!-- Patient selection (dropdown) -->
                <div class="form-group">
                    <label for="patient_id">Patient</label>
                    <select class="form-control" id="patient_id" name="patient_id" required>
                        @foreach($patients as $patient)
                            <option value="{{ $patient->patient_id }}" {{ (isset($labTest) && $labTest->patient_id == $patient->patient_id) ? 'selected' : '' }}>
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
                            <option value="{{ $appointment->appointment_id }}" {{ (isset($labTest) && $labTest->appointment_id == $appointment->appointment_id) ? 'selected' : '' }}>
                                Appointment #{{ $appointment->appointment_id }} - {{ $appointment->appointment_date }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Test Name -->
                <div class="form-group">
                    <label for="test_name">Test Name</label>
                    <input type="text" class="form-control" id="test_name" name="test_name" value="{{ old('test_name', isset($labTest) ? $labTest->test_name : '') }}" required>
                </div>

                <!-- Test Date -->
                <div class="form-group">
                    <label for="test_date">Test Date</label>
                    <input type="date" class="form-control" id="test_date" name="test_date" value="{{ old('test_date', isset($labTest) ? $labTest->test_date : '') }}" required>
                </div>

                <!-- Results -->
                <div class="form-group">
                    <label for="results">Test Results</label>
                    <textarea class="form-control" id="results" name="results">{{ old('results', isset($labTest) ? $labTest->results : '') }}</textarea>
                </div>

                <!-- Test Status -->
                <div class="form-group">
                    <label for="test_status">Test Status</label>
                    <select class="form-control" id="test_status" name="test_status">
                        <option value="Pending" {{ (isset($labTest) && $labTest->test_status == 'Pending') ? 'selected' : '' }}>Pending</option>
                        <option value="Completed" {{ (isset($labTest) && $labTest->test_status == 'Completed') ? 'selected' : '' }}>Completed</option>
                        <option value="Failed" {{ (isset($labTest) && $labTest->test_status == 'Failed') ? 'selected' : '' }}>Failed</option>
                        <option value="In Progress" {{ (isset($labTest) && $labTest->test_status == 'In Progress') ? 'selected' : '' }}>In Progress</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($labTest) ? 'Update Lab Test' : 'Create Lab Test' }}</button>
            </form>
        </div>
    </div>
</div>
@endsection