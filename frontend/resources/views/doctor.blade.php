@extends('layouts.app')

@section('title', 'Patient Management')

@section('content')
<div class="container">
    <h1>Patient Management</h1>

    <!-- Form for adding new patient -->
    <div class="card mb-4">
        <div class="card-header">
            <h3>Add New Patient</h3>
        </div>
        <div class="card-body">
            <form action="{{ route('patients.store') }}" method="POST">
                @csrf

                <div class="form-group">
                    <label for="first_name">First Name</label>
                    <input type="text" class="form-control" id="first_name" name="first_name" required>
                </div>

                <div class="form-group">
                    <label for="last_name">Last Name</label>
                    <input type="text" class="form-control" id="last_name" name="last_name" required>
                </div>

                <div class="form-group">
                    <label for="date_of_birth">Date of Birth</label>
                    <input type="date" class="form-control" id="date_of_birth" name="date_of_birth" required>
                </div>

                <div class="form-group">
                    <label for="gender">Gender</label>
                    <select class="form-control" id="gender" name="gender" required>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="email">Email (Optional)</label>
                    <input type="email" class="form-control" id="email" name="email">
                </div>

                <div class="form-group">
                    <label for="phone_number">Phone Number</label>
                    <input type="text" class="form-control" id="phone_number" name="phone_number" required>
                </div>

                <div class="form-group">
                    <label for="address">Address</label>
                    <input type="text" class="form-control" id="address" name="address">
                </div>

                <div class="form-group">
                    <label for="insurance_provider">Insurance Provider</label>
                    <input type="text" class="form-control" id="insurance_provider" name="insurance_provider">
                </div>

                <div class="form-group">
                    <label for="insurance_policy_number">Insurance Policy Number</label>
                    <input type="text" class="form-control" id="insurance_policy_number" name="insurance_policy_number">
                </div>

                <div class="form-group">
                    <label for="primary_care_physician">Primary Care Physician</label>
                    <input type="text" class="form-control" id="primary_care_physician" name="primary_care_physician">
                </div>

                <div class="form-group">
                    <label for="medical_history">Medical History</label>
                    <textarea class="form-control" id="medical_history" name="medical_history"></textarea>
                </div>

                <div class="form-group">
                    <label for="allergies">Allergies</label>
                    <textarea class="form-control" id="allergies" name="allergies"></textarea>
                </div>

                <div class="form-group">
                    <label for="status">Status</label>
                    <select class="form-control" id="status" name="status">
                        <option value="active" selected>Active</option>
                        <option value="inactive">Inactive</option>
                        <option value="deceased">Deceased</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">Add Patient</button>
            </form>
        </div>
    </div>

    <!-- List of existing patients -->
    <div class="card">
        <div class="card-header">
            <h3>Existing Patients</h3>
        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Date of Birth</th>
                        <th>Phone Number</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach($patients as $patient)
                    <tr>
                        <td>{{ $patient->first_name }}</td>
                        <td>{{ $patient->last_name }}</td>
                        <td>{{ $patient->date_of_birth }}</td>
                        <td>{{ $patient->phone_number }}</td>
                        <td>{{ $patient->status }}</td>
                        <td>
                            <a href="{{ route('patients.edit', $patient->patient_id) }}" class="btn btn-warning btn-sm">Edit</a>
                            <form action="{{ route('patients.destroy', $patient->patient_id) }}" method="POST" class="d-inline" onsubmit="return confirm('Are you sure you want to delete this patient?');">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                            </form>
                        </td>
                    </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </div>
</div>
@endsection
