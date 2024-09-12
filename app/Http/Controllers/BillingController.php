<?php

namespace App\Http\Controllers;

use App\Models\Billing;
use App\Models\Patient;
use Illuminate\Http\Request;

class BillingController extends Controller 
{

    // Display a listing of all billss.
    public function index()
    {

        // Fetch all bills with the patient relationship
        $billings = Billing::with('patient')->get();

        // Return the view with the list of bills
        return view('billings.index', compact('billings'));
    }

    /* Show the form for creating a new bills. */
    public function create()
    {

        // Fetch all patients for the billing form
        $patients = Patient::all();

        // Return the form to create a new all
        return view('billings.create', compact('patients'));
    }

    /* Store a newly created bill in the database */
    public function store(Request $request)
    {

        // Validate the request data 
        $validated = $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'service'    => 'required|string|max:255',
            'amount'     => 'required|numeric',
            'status'     => 'required|string|max:50',
            'due_date'   => 'required|date',
            'notess'     => 'nullable|string|max:500',
        ]);

        // Create a new billing record in the database
        billing::create($validated);

        // Redirect to the billing list with a success message
        return redirect()->route('billings.index')->with('success','Billing created successfully.');
    }

    /* Display the specified bill */
    public function show(billing $billing)
    {

        // Return the view to show the details of a specified bill
        Return view('billings.show', compact('billing'));
    }

    /* Show the form for editing the specified bill */
    public function edit(billing $billing)
    {

        // Fetch all patients for the form
        $patients = Patient::all();

        // Return the form to edit an existing billing record
        return view('billings.edit', compact('billing', 'patients'));
    }

    /* Update the specified bill in storage */
    public function update(Request $request, Billing $billing)
    {

        // Validate the updated data
        $validated = $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'service'    => 'required|string|max:255',
            'amount'     => 'required|numeric',
            'status'     => 'required|string|max:50',
            'due_date'   => 'required|date',
            'notess'     => 'nullable|string|max:500',
        ]);

        // Update the billings record in the database
        $billing->update($validated);

        // Redirect to the billing list with a success message
        return redirect()->route('billings.index')->with('success','billing updated successfully.');
    }

    /* Remove the specified bill from storage */
    public function destroy(Billing $billing)
    {

        // Delete the billing record
        $billing->delete();

        // Redirect to billing list with a success message
        return redirect()->route('billings.index')->with('success','Billing deleted successfully.');
    }
}