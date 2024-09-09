<!DOCTYPE html>
<html>
<head>
    <title>Add Doctor</title>
</head>
<body>
    <h1>Add New Doctor</h1>
    <form action="{{ route('doctors.store') }}" method="POST">
        @csrf
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone">
        <br>
        <label for="specialization">Specialization:</label>
        <input type="text" id="specialization" name="specialization" required>
        <br>
        <button type="submit">Add Doctor</button>
    </form>
</body>
</html>
