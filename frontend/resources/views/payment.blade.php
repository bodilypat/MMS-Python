@extends('layouts.app')

@section('title', isset($payment) ? 'Edit Payment' : 'Create New Payment')

@section('content')
<div class="container">
    <h1>{{ isset($payment) ? 'Edit Payment' : 'Create New Payment' }}</h1>

    <!-- Form to create or update a payment -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($payment) ? 'Update Payment' : 'Create Payment' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($payment) ? route('payments.update', $payment->billing_id) : route('payments.store') }}" method="POST">
                @csrf
                @if(isset($payment))
                    @method('PUT')
                @endif

                <!-- Patient selection (dropdown) -->
                <div class="form-group">
                    <label for="patient_id">Patient</label>
                    <select class="form-control" id="patient_id" name="patient_id" required>
                        @foreach($patients as $patient)
                            <option value="{{ $patient->patient_id }}" {{ (isset($payment) && $payment->patient_id == $patient->patient_id) ? 'selected' : '' }}>
                                {{ $patient->first_name }} {{ $patient->last_name }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Appointment selection (dropdown) -->
                <div class="form-group">
                    <label for="appointment_id">Appointment</label>
                    <select class="form-control" id="appointment_id" name="appointment_id" required>
                        @foreach($appointments as $appointment)
                            <option value="{{ $appointment->appointment_id }}" {{ (isset($payment) && $payment->appointment_id == $appointment->appointment_id) ? 'selected' : '' }}>
                                Appointment #{{ $appointment->appointment_id }} - {{ $appointment->appointment_date }}
                            </option>
                        @endforeach
                    </select>
                </div>

                <!-- Total Amount -->
                <div class="form-group">
                    <label for="total_amount">Total Amount</label>
                    <input type="number" class="form-control" id="total_amount" name="total_amount" step="0.01" value="{{ old('total_amount', isset($payment) ? $payment->total_amount : '') }}" required>
                </div>

                <!-- Amount Paid -->
                <div class="form-group">
                    <label for="amount_paid">Amount Paid</label>
                    <input type="number" class="form-control" id="amount_paid" name="amount_paid" step="0.01" value="{{ old('amount_paid', isset($payment) ? $payment->amount_paid : '') }}" required>
                </div>

                <!-- Balance Due (Calculated) -->
                <div class="form-group">
                    <label for="balance_due">Balance Due</label>
                    <input type="number" class="form-control" id="balance_due" name="balance_due" step="0.01" value="{{ old('balance_due', isset($payment) ? $payment->balance_due : '') }}" required readonly>
                </div>

                <!-- Payment Status -->
                <div class="form-group">
                    <label for="payment_status">Payment Status</label>
                    <select class="form-control" id="payment_status" name="payment_status" required>
                        <option value="Paid" {{ (isset($payment) && $payment->payment_status == 'Paid') ? 'selected' : '' }}>Paid</option>
                        <option value="Pending" {{ (isset($payment) && $payment->payment_status == 'Pending') ? 'selected' : '' }}>Pending</option>
                        <option value="Partially Paid" {{ (isset($payment) && $payment->payment_status == 'Partially Paid') ? 'selected' : '' }}>Partially Paid</option>
                    </select>
                </div>

                <!-- Insurance Claimed Amount -->
                <div class="form-group">
                    <label for="insurance_claimed_amount">Insurance Claimed Amount</label>
                    <input type="number" class="form-control" id="insurance_claimed_amount" name="insurance_claimed_amount" step="0.01" value="{{ old('insurance_claimed_amount', isset($payment) ? $payment->insurance_claimed_amount : '') }}">
                </div>

                <!-- Insurance Status -->
                <div class="form-group">
                    <label for="insurance_status">Insurance Status</label>
                    <select class="form-control" id="insurance_status" name="insurance_status">
                        <option value="Approved" {{ (isset($payment) && $payment->insurance_status == 'Approved') ? 'selected' : '' }}>Approved</option>
                        <option value="Pending" {{ (isset($payment) && $payment->insurance_status == 'Pending') ? 'selected' : '' }}>Pending</option>
                        <option value="Denied" {{ (isset($payment) && $payment->insurance_status == 'Denied') ? 'selected' : '' }}>Denied</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($payment) ? 'Update Payment' : 'Create Payment' }}</button>
            </form>
        </div>
    </div>
</div>

@section('scripts')
<script>
    // Automatically calculate balance due when amount paid is entered
    document.getElementById('amount_paid').addEventListener('input', function() {
        let totalAmount = parseFloat(document.getElementById('total_amount').value) || 0;
        let amountPaid = parseFloat(this.value) || 0;
        let balanceDue = totalAmount - amountPaid;
        document.getElementById('balance_due').value = balanceDue.toFixed(2);
    });
</script>
@endsection

@endsection