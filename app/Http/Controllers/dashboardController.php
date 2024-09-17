<?php

namespace App\Http\Controllers;

use App\Http\Requests\changePasswordRequest;
use App\Models\Patient;
use App\Models\Appointment;
use App\Models\Doctor;
use App\Models\MedicalRecord;
use App\Models\prescription;
use App\Models\billing;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class dashboardController extends Controller
{
    public function index()
    {
        return view('dashboard', [
            'patients' => Patient::count(),
            'appointments' => Appointment::count(),
            'doctors' => Doctors::count(),
            'medical-records' => MedicalRecord::count(),
            'prescriptions' => Prescription::count(),
            'billings' => Billing::count(),
        ]);
    }

    public function change_password_view()
    {
        return view('reset_password');
    }

    public function change_password(changePasswordRequest $request)
    {
        if (Auth::check(["username" => auth()->user()->username, "password" => $request->c_password])) {
            auth()->user()->password = bcrypt($request->password);
            return redirect()->back()->with(['message' => "Password Changed Successfully!."]);
        } else {
            return "";
        }
    }
}
