<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePharmaciesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('pharmacies', function (Blueprint $table) {
            $table->id('pharmacy_id'); // equivalent to 'pharmacy_id INT AUTO_INCREMENT PRIMARY KEY'
            $table->string('name', 255); // 'name VARCHAR(255) NOT NULL'
            $table->string('address', 255)->unique(); // 'address VARCHAR(255) NOT NULL UNIQUE'
            $table->string('phone_number', 15)->unique(); // 'phone_number VARCHAR(15) NOT NULL UNIQUE'
            $table->string('email', 255)->unique(); // 'email VARCHAR(255) NOT NULL UNIQUE'
            $table->timestamps(0); // 'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP' and 'updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'

            // Adding a check constraint for phone number validation (using regex)
            $table->check('phone_number REGEXP \'^[0-9]+$\''); // 'CONSTRAINT chk_phone_number CHECK (phone_number REGEXP '^[0-9]+$')'
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('pharmacies');
    }
}