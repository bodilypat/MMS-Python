<?php
	use App\Models\User;
	use Illuminate\Http\Request;
	use Illuminate\Support\Facades\Hash;

	public function create()
	{
		return view('users.user');
	}

	public function store(Request $request)
	{
		$request->validate([
			'username' => 'required|string|max:255|unique:users',
			'email' => 'required|email|max:100|unique:users',
			'password' => 'required|string|min:8|confirmed',
			'role' => 'required|in:admin,user',
		]);

		User::create([
			'username' => $request->username,
			'email' => $request->email,
			'password' => Hash::make($request->password),
			'role' => $request->role,
		]);

		return redirect()->route('users.index')->with('success', 'User created successfully.');
	}

	public function edit($id)
	{
		$user = User::findOrFail($id);
		return view('users.user', compact('user'));
	}

	public function update(Request $request, $id)
	{
		$request->validate([
			'username' => 'required|string|max:255|unique:users,username,' . $id,
			'email' => 'required|email|max:100|unique:users,email,' . $id,
			'password' => 'nullable|string|min:8|confirmed',
			'role' => 'required|in:admin,user',
		]);

		$user = User::findOrFail($id);
		$user->username = $request->username;
		$user->email = $request->email;
		$user->role = $request->role;

		if ($request->password) {
			$user->password = Hash::make($request->password);
		}

		$user->save();

		return redirect()->route('users.index')->with('success', 'User updated successfully.');
	}
?>
