namespace App\Http\Controllers;

use App\Models\Billing;
use App\Models\Patient; // Assuming you have a Patient model
use Illuminate\Http\Request;

class BillingController extends Controller
{
    /**
     * Display a listing of the billings.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $billings = Billing::with('patient')->get();
        return view('billings.index', compact('billings'));
    }

    /**
     * Show the form for creating a new billing.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $patients = Patient::all();
        return view('billings.create', compact('patients'));
    }

    /**
     * Store a newly created billing in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'amount' => 'required|numeric|min:0',
            'billing_date' => 'required|date',
            'description' => 'nullable|string',
        ]);

        Billing::create($request->all());

        return redirect()->route('billings.index')->with('success', 'Billing record added successfully.');
    }

    /**
     * Display the specified billing.
     *
     * @param \App\Models\Billing $billing
     * @return \Illuminate\Http\Response
     */
    public function show(Billing $billing)
    {
        return view('billings.show', compact('billing'));
    }

    /**
     * Show the form for editing the specified billing.
     *
     * @param \App\Models\Billing $billing
     * @return \Illuminate\Http\Response
     */
    public function edit(Billing $billing)
    {
        $patients = Patient::all();
        return view('billings.edit', compact('billing', 'patients'));
    }

    /**
     * Update the specified billing in storage.
     *
     * @param \Illuminate\Http\Request $request
     * @param \App\Models\Billing $billing
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Billing $billing)
    {
        $request->validate([
            'patient_id' => 'required|exists:patients,id',
            'amount' => 'required|numeric|min:0',
            'billing_date' => 'required|date',
            'description' => 'nullable|string',
        ]);

        $billing->update($request->all());

        return redirect()->route('billings.index')->with('success', 'Billing record updated successfully.');
    }

    /**
     * Remove the specified billing from storage.
     *
     * @param \App\Models\Billing $billing
     * @return \Illuminate\Http\Response
     */
    public function destroy(Billing $billing)
    {
        $billing->delete();

        return redirect()->route('billings.index')->with('success', 'Billing record deleted successfully.');
    }
}
