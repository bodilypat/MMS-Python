@extends('layouts.app')

@section('title', isset($user) ? 'Edit User' : 'Create New User')

@section('content')
<div class="container">
    <h1>{{ isset($user) ? 'Edit User' : 'Create New User' }}</h1>

    <!-- Form to create or update a user -->
    <div class="card">
        <div class="card-header">
            <h3>{{ isset($user) ? 'Update User' : 'Create User' }}</h3>
        </div>
        <div class="card-body">
            <form action="{{ isset($user) ? route('users.update', $user->id) : route('users.store') }}" method="POST">
                @csrf
                @if(isset($user))
                    @method('PUT')
                @endif

                <!-- Username -->
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" name="username" value="{{ old('username', isset($user) ? $user->username : '') }}" required>
                </div>

                <!-- Email -->
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" value="{{ old('email', isset($user) ? $user->email : '') }}" required>
                </div>

                <!-- Password -->
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" name="password" {{ isset($user) ? '' : 'required' }}>
                    @if(!isset($user))
                        <small class="form-text text-muted">Leave empty to keep the current password.</small>
                    @endif
                </div>

                <!-- Role -->
                <div class="form-group">
                    <label for="role">Role</label>
                    <select class="form-control" id="role" name="role" required>
                        <option value="admin" {{ old('role', isset($user) ? $user->role : 'user') == 'admin' ? 'selected' : '' }}>Admin</option>
                        <option value="user" {{ old('role', isset($user) ? $user->role : 'user') == 'user' ? 'selected' : '' }}>User</option>
                    </select>
                </div>

                <button type="submit" class="btn btn-primary">{{ isset($user) ? 'Update User' : 'Create User' }}</button>
            </form>
        </div>
    </div>
</div>

@endsection