@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Prescriptions</h1>
        <a href="{{ route('prescriptions.create') }}" class="btn btn-primary">Add New Prescription</a>
        <table class="table">
            <thead>
                <tr>
                    <th>Patient</th>
                    <th>Doctor</th>
                    <th>Medication</th>
                    <th>Dosage</th>
                    <th>Issued At</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                @foreach($prescriptions as $prescription)
                    <tr>
                        <td>{{ $prescription->patient->name }}</td>
                        <td>{{ $prescription->doctor->name }}</td>
                        <td>{{ $prescription->medication }}</td>
                        <td>{{ $prescription->dosage }}</td>
                        <td>{{ $prescription->issued_at ? $prescription->issued_at->format('Y-m-d H:i') : 'N/A' }}</td>
                        <td>
                            <a href="{{ route('prescriptions.show', $prescription->id) }}" class="btn btn-info">View</a>
                            <a href="{{ route('prescriptions.edit', $prescription->id) }}" class="btn btn-warning">Edit</a>
                            <form action="{{ route('prescriptions.destroy', $prescription->id) }}" method="POST" style="display:inline;">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="btn btn-danger">Delete</button>
                            </form>
                        </td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>
@endsection
