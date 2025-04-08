@extends('layouts.app')

@section('title', isset($insurance) ? 'Edit Insurance' : 'Create New Insurance')

@section('content')
<div class="container">
    <h1>{{ isset($insurance) ? 'Edit Insurance' : 'Create New Insurance' }}</h1>

    <!-- Form to create or update insurance -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($insurance) ? 'Update Insurance' : 'Create Insurance' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($insurance) ? route('insurances.update', $insurance->insurance_id) : route('insurances.store') }}" method="POST">
                @csrf
                @if(isset($insurance))
                    @method('PUT')
                @endif

                <!-- Insurance Provider Name -->
                <div class="form-group">
                    <label for="provider_name">Insurance Provider</label>
                    <input type="text" class="form-control" id="provider_name" name="provider_name" value="{{ old('provider_name', isset($insurance) ? $insurance->provider_name : '') }}" required>
                </div>

                <!-- Policy Number -->
                <div class="form-group">
                    <label for="policy_number">Policy Number</label>
                    <input type="text" class="form-control" id="policy_number" name="policy_number" value="{{ old('policy_number', isset($insurance) ? $insurance->policy_number : '') }}" required>
                </div>

                <!-- Coverage Type -->
                <div class="form-group">
                    <label for="coverage_type">Coverage Type</label>
                    <select class="form-control" id="coverage_type" name="coverage_type" required>
                        <option value="Full" {{ old('coverage_type', isset($insurance) ? $insurance->coverage_type : 'Partial') == 'Full' ? 'selected' : '' }}>Full</option>
                        <option value="Partial" {{ old('coverage_type', isset($insurance) ? $insurance->coverage_type : 'Partial') == 'Partial' ? 'selected' : '' }}>Partial</option>
                    </select>
                </div>

                <!-- Coverage Amount -->
                <div class="form-group">
                    <label for="coverage_amount">Coverage Amount</label>
                    <input type="number" step="0.01" class="form-control" id="coverage_amount" name="coverage_amount" value="{{ old('coverage_amount', isset($insurance) ? $insurance->coverage_amount : '') }}" required>
                </div>

                <!-- Patient ID (Should be selected or automatically assigned) -->
                <div class="form-group">
                    <label for="patient_id">Patient</label>
                    <select class="form-control" id="patient_id" name="patient_id" required>
                        @foreach ($patients as $patient)
                            <option value="{{ $patient->patient_id }}" {{ old('patient_id', isset($insurance) ? $insurance->patient_id : '') == $patient->patient_id ? 'selected' : '' }}>
                                {{ $patient->first_name }} {{ $patient->last_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Start Date -->
                <div class="form-group">
                    <label for="start_date">Start Date</label>
                    <input type="date" class="form-control" id="start_date" name="start_date" value="{{ old('start_date', isset($insurance) ? $insurance->start_date : '') }}" required>
                </div>

                <!-- End Date -->
                <div class="form-group">
                    <label for="end_date">End Date</label>
                    <input type="date" class="form-control" id="end_date" name="end_date" value="{{ old('end_date', isset($insurance) ? $insurance->end_date : '') }}" required>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($insurance) ? 'Update Insurance' : 'Create Insurance' }}</button>
            </form>
        </div>
    </div>
</div>

@endsection