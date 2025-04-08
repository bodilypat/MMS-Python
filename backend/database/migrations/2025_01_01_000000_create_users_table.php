<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id(); // equivalent to 'id INT AUTO_INCREMENT PRIMARY KEY'
            $table->string('username', 255)->unique(); // 'username VARCHAR(255) NOT NULL UNIQUE'
            $table->string('email', 100)->unique(); // 'email VARCHAR(100) NOT NULL UNIQUE'
            $table->string('password', 255); // 'password VARCHAR(255) NOT NULL'
            $table->enum('role', ['admin', 'user'])->default('user'); // 'role ENUM('admin', 'user') DEFAULT 'user'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL', 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL'
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}