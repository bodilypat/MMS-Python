<!DOCTYPE html>
<html>
<head>
    <title>Add Patient</title>
</head>
<body>
    <h1>Add New Patient</h1>
    <form action="{{ route('patients.store') }}" method="POST">
        @csrf
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone">
        <br>
        <label for="address">Address:</label>
        <textarea id="address" name="address"></textarea>
        <br>
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>
        <br>
        <button type="submit">Add Patient</button>
    </form>
</body>
</html>
