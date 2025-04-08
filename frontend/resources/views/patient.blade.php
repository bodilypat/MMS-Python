@extends('layouts.app')

@section('title', isset($patient) ? 'Edit Patient' : 'Add New Patient')

@section('content')
<div class="container">
    <h1>{{ isset($patient) ? 'Edit Patient' : 'Add New Patient' }}</h1>

    <!-- Form to create or update a patient -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($patient) ? 'Update Patient Information' : 'Add Patient Information' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($patient) ? route('patients.update', $patient->patient_id) : route('patients.store') }}" method="POST">
                @csrf
                @if(isset($patient))
                    @method('PUT')
                @endif

                <div class="form-group">
                    <label for="first_name">First Name</label>
                    <input type="text" class="form-control" id="first_name" name="first_name" value="{{ old('first_name', $patient->first_name ?? '') }}" required>
                </div>

                <div class="form-group">
                    <label for="last_name">Last Name</label>
                    <input type="text" class="form-control" id="last_name" name="last_name" value="{{ old('last_name', $patient->last_name ?? '') }}" required>
                </div>

                <div class="form-group">
                    <label for="date_of_birth">Date of Birth</label>
                    <input type="date" class="form-control" id="date_of_birth" name="date_of_birth" value="{{ old('date_of_birth', $patient->date_of_birth ?? '') }}" required>
                </div>

                <div class="form-group">
                    <label for="gender">Gender</label>
                    <select class="form-control" id="gender" name="gender" required>
                        <option value="male" {{ (isset($patient) && $patient->gender == 'male') ? 'selected' : '' }}>Male</option>
                        <option value="female" {{ (isset($patient) && $patient->gender == 'female') ? 'selected' : '' }}>Female</option>
                        <option value="other" {{ (isset($patient) && $patient->gender == 'other') ? 'selected' : '' }}>Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" value="{{ old('email', $patient->email ?? '') }}">
                </div>

                <div class="form-group">
                    <label for="phone_number">Phone Number</label>
                    <input type="text" class="form-control" id="phone_number" name="phone_number" value="{{ old('phone_number', $patient->phone_number ?? '') }}" required>
                </div>

                <div class="form-group">
                    <label for="address">Address</label>
                    <input type="text" class="form-control" id="address" name="address" value="{{ old('address', $patient->address ?? '') }}">
                </div>

                <div class="form-group">
                    <label for="insurance_provider">Insurance Provider</label>
                    <input type="text" class="form-control" id="insurance_provider" name="insurance_provider" value="{{ old('insurance_provider', $patient->insurance_provider ?? '') }}">
                </div>

                <div class="form-group">
                    <label for="insurance_policy_number">Insurance Policy Number</label>
                    <input type="text" class="form-control" id="insurance_policy_number" name="insurance_policy_number" value="{{ old('insurance_policy_number', $patient->insurance_policy_number ?? '') }}">
                </div>

                <div class="form-group">
                    <label for="primary_care_physician">Primary Care Physician</label>
                    <input type="text" class="form-control" id="primary_care_physician" name="primary_care_physician" value="{{ old('primary_care_physician', $patient->primary_care_physician ?? '') }}">
                </div>

                <div class="form-group">
                    <label for="medical_history">Medical History</label>
                    <textarea class="form-control" id="medical_history" name="medical_history">{{ old('medical_history', $patient->medical_history ?? '') }}</textarea>
                </div>

                <div class="form-group">
                    <label for="allergies">Allergies</label>
                    <textarea class="form-control" id="allergies" name="allergies">{{ old('allergies', $patient->allergies ?? '') }}</textarea>
                </div>

                <div class="form-group">
                    <label for="status">Status</label>
                    <select class="form-control" id="status" name="status">
                        <option value="active" {{ (isset($patient) && $patient->status == 'active') ? 'selected' : '' }}>Active</option>
                        <option value="inactive" {{ (isset($patient) && $patient->status == 'inactive') ? 'selected' : '' }}>Inactive</option>
                        <option value="deceased" {{ (isset($patient) && $patient->status == 'deceased') ? 'selected' : '' }}>Deceased</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($patient) ? 'Update Patient' : 'Add Patient' }}</button>
            </form>
        </div>
    </div>
</div>
@endsection