<!DOCTYPE html>
<html>
<head>
    <title>Doctors</title>
</head>
<body>
    <h1>Doctors List</h1>
    <a href="{{ route('doctors.create') }}">Add New Doctor</a>
    @if(session('success'))
        <p>{{ session('success') }}</p>
    @endif
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Specialization</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($doctors as $doctor)
                <tr>
                    <td>{{ $doctor->name }}</td>
                    <td>{{ $doctor->email }}</td>
                    <td>{{ $doctor->phone }}</td>
                    <td>{{ $doctor->specialization }}</td>
                    <td>
                        <a href="{{ route('doctors.show', $doctor) }}">View</a>
                        <a href="{{ route('doctors.edit', $doctor) }}">Edit</a>
                        <form action="{{ route('doctors.destroy', $doctor) }}" method="POST" style="display:inline;">
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
