<!DOCTYPE html>
<html>
<head>
    <title>Medical Records</title>
</head>
<body>
    <h1>Medical Records List</h1>
    <a href="{{ route('medical-records.create') }}">Add New Record</a>
    @if(session('success'))
        <p>{{ session('success') }}</p>
    @endif
    <table>
        <thead>
            <tr>
                <th>Patient</th>
                <th>Date</th>
                <th>Diagnosis</th>
                <th>Treatment</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($medicalRecords as $record)
                <tr>
                    <td>{{ $record->patient->name }}</td>
                    <td>{{ $record->date->format('Y-m-d') }}</td>
                    <td>{{ $record->diagnosis }}</td>
                    <td>{{ $record->treatment }}</td>
                    <td>
                        <a href="{{ route('medical-records.show', $record) }}">View</a>
                        <a href="{{ route('medical-records.edit', $record) }}">Edit</a>
                        <form action="{{ route('medical-records.destroy', $record) }}" method="POST" style="display:inline;">
                            @csrf
                            @method('DELETE')
                            <button type="submit">Delete</button>
                        </form>
                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>
</body>
</html>
