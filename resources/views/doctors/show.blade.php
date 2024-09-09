<!DOCTYPE html>
<html>
<head>
    <title>Doctor Details</title>
</head>
<body>
    <h1>Doctor Details</h1>
    <p><strong>Name:</strong> {{ $doctor->name }}</p>
    <p><strong>Email:</strong> {{ $doctor->email }}</p>
    <p><strong>Phone:</strong> {{ $doctor->phone }}</p>
    <p><strong>Specialization:</strong> {{ $doctor->specialization }}</p>
    <a href="{{ route('doctors.index') }}">Back to list</a>
</body>
</html>
