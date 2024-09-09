<!DOCTYPE html>
<html>
<head>
    <title>Edit Doctor</title>
</head>
<body>
    <h1>Edit Doctor</h1>
    <form action="{{ route('doctors.update', $doctor) }}" method="POST">
        @csrf
        @method('PUT')
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ old('name', $doctor->name) }}" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="{{ old('email', $doctor->email) }}" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" value="{{ old('phone', $doctor->phone) }}">
        <br>
        <label for="specialization">Specialization:</label>
        <input type="text" id="specialization" name="specialization" value="{{ old('specialization', $doctor->specialization) }}" required>
        <br>
        <button type="submit">Update Doctor</button>
    </form>
</body>
</html>
