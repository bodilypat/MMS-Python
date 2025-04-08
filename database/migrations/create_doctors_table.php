<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDoctorsTable extends Migration
{
    public function up()
    {
        Schema::create('doctors', function (Blueprint $table) {
            $table->id('doctor_id'); // Auto-incrementing primary key
            $table->string('first_name', 100); // First name
            $table->string('last_name', 100); // Last name
            $table->string('specialization', 100); // Specialization
            $table->string('email', 255)->unique(); // Email with unique constraint
            $table->string('phone_number', 20)->unique(); // Phone number with unique constraint
            $table->string('department', 100)->nullable(); // Department (nullable)
            $table->date('birthdate')->nullable(); // Birthdate (nullable)
            $table->string('address', 255)->nullable(); // Address (nullable)
            $table->enum('status', ['active', 'inactive', 'retired'])->default('active'); // Status with default value
            $table->text('notes')->nullable(); // Notes (nullable)
            $table->timestamps(0); // Created_at and updated_at with timestamp
            $table->timestamp('updated_at')->useCurrent()->useCurrentOnUpdate(); // Updated_at timestamp with current time on update
            
            // Adding a custom check constraint for phone number validation
            $table->check('phone_number REGEXP "^[0-9]{10,15}$"');
        });
    }

    public function down()
    {
        Schema::dropIfExists('doctors');
    }
}
