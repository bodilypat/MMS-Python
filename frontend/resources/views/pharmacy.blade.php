@extends('layouts.app')

@section('title', isset($pharmacy) ? 'Edit Pharmacy' : 'Create New Pharmacy')

@section('content')
<div class="container">
    <h1>{{ isset($pharmacy) ? 'Edit Pharmacy' : 'Create New Pharmacy' }}</h1>

    <!-- Form to create or update a pharmacy -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($pharmacy) ? 'Update Pharmacy' : 'Create Pharmacy' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($pharmacy) ? route('pharmacies.update', $pharmacy->pharmacy_id) : route('pharmacies.store') }}" method="POST">
                @csrf
                @if(isset($pharmacy))
                    @method('PUT')
                @endif

                <!-- Pharmacy Name -->
                <div class="form-group">
                    <label for="name">Pharmacy Name</label>
                    <input type="text" class="form-control" id="name" name="name" value="{{ old('name', isset($pharmacy) ? $pharmacy->name : '') }}" required>
                </div>

                <!-- Pharmacy Address -->
                <div class="form-group">
                    <label for="address">Address</label>
                    <input type="text" class="form-control" id="address" name="address" value="{{ old('address', isset($pharmacy) ? $pharmacy->address : '') }}" required>
                </div>

                <!-- Pharmacy Phone Number -->
                <div class="form-group">
                    <label for="phone_number">Phone Number</label>
                    <input type="text" class="form-control" id="phone_number" name="phone_number" value="{{ old('phone_number', isset($pharmacy) ? $pharmacy->phone_number : '') }}" required pattern="^[0-9]+$" title="Phone number should only contain digits.">
                </div>

                <!-- Pharmacy Email -->
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" value="{{ old('email', isset($pharmacy) ? $pharmacy->email : '') }}" required>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($pharmacy) ? 'Update Pharmacy' : 'Create Pharmacy' }}</button>
            </form>
        </div>
    </div>
</div>

@endsection