<?php

namespace App\Http\Controllers;

use App\Models\Payment;
use App\Models\Patient;
use App\Models\Appointment;
use Illuminate\Http\Request;

class PaymentController extends Controller
{
    // Fetch all payments
    public function index()
    {
        $payments = Payment::with(['patient', 'appointment'])->get();
        return response()->json($payments);
    }

    // Show a specific payment by ID
    public function show($id)
    {
        $payment = Payment::with(['patient', 'appointment'])->find($id);

        if (!$payment) {
            return response()->json(['message' => 'Payment not found'], 404);
        }

        return response()->json($payment);
    }

    // Create a new payment
    public function store(Request $request)
    {
        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'total_amount' => 'required|numeric',
            'amount_paid' => 'required|numeric',
            'balance_due' => 'required|numeric',
            'payment_status' => 'required|in:Paid,Pending,Partially Paid',
            'insurance_claimed_amount' => 'nullable|numeric',
            'insurance_status' => 'nullable|in:Approved,Pending,Denied',
        ]);

        // Create the payment
        $payment = Payment::create($request->all());

        return response()->json($payment, 201);
    }

    // Update an existing payment
    public function update(Request $request, $id)
    {
        $payment = Payment::find($id);

        if (!$payment) {
            return response()->json(['message' => 'Payment not found'], 404);
        }

        // Validate the input
        $request->validate([
            'patient_id' => 'required|exists:patients,patient_id',
            'appointment_id' => 'required|exists:appointments,appointment_id',
            'total_amount' => 'required|numeric',
            'amount_paid' => 'required|numeric',
            'balance_due' => 'required|numeric',
            'payment_status' => 'required|in:Paid,Pending,Partially Paid',
            'insurance_claimed_amount' => 'nullable|numeric',
            'insurance_status' => 'nullable|in:Approved,Pending,Denied',
        ]);

        // Update the payment
        $payment->update($request->all());

        return response()->json($payment);
    }

    // Delete a payment
    public function destroy($id)
    {
        $payment = Payment::find($id);

        if (!$payment) {
            return response()->json(['message' => 'Payment not found'], 404);
        }

        // Delete the payment
        $payment->delete();

        return response()->json(['message' => 'Payment deleted successfully']);
    }
}