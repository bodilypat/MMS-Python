<!DOCTYPE html>
<html>
<head>
    <title>Edit Patient</title>
</head>
<body>
    <h1>Edit Patient</h1>
    <form action="{{ route('patients.update', $patient) }}" method="POST">
        @csrf
        @method('PUT')
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ $patient->name }}" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="{{ $patient->email }}">
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" value="{{ $patient->phone }}">
        <br>
        <label for="address">Address:</label>
        <textarea id="address" name="address">{{ $patient->address }}</textarea>
        <br>
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" value="{{ $patient->dob->format('Y-m-d') }}" required>
        <br>
        <button type="submit">Update Patient</button>
    </form>
</body>
</html>
