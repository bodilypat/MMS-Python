<!DOCTYPE html>
<html>
<head>
    <title>Billings</title>
</head>
<body>
    <h1>Billing Records</h1>
    <a href="{{ route('billings.create') }}">Add New Billing</a>
    @if(session('success'))
        <p>{{ session('success') }}</p>
    @endif
    <table>
        <thead>
            <tr>
                <th>Patient</th>
                <th>Amount</th>
                <th>Billing Date</th>
                <th>Description</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($billings as $billing)
                <tr>
                    <td>{{ $billing->patient->name }}</td>
                    <td>${{ number_format($billing->amount, 2) }}</td>
                    <td>{{ $billing->billing_date->format('Y-m-d') }}</td>
                    <td>{{ $billing->description }}</td>
                    <td>
                        <a href="{{ route('billings.show', $billing) }}">View</a>
                        <a href="{{ route('billings.edit', $billing) }}">Edit</a>
                        <form action="{{ route('billings.destroy', $billing) }}" method="POST" style="display:inline;">
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
