<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Facade\Schema;

class CreateBillingsTable extends Migration
{
    /* Run the migration */

    public function up()
    {
        Schema::create('billings', function(Blueprint $table){
            $table->id();
            $table->unsignedBigInteger('patient_id');
            $table->unsignedBigInteger('appointment_id')->nullable();
            $table->decimal('amount', 10,2);
            $table->decimal('paid_amount',10,2)->nullable();
            $table->enum(['pay_status', 'paid','faild'])->default('pending'); /* Status payment */
            $table->date('billing_date');
            $table->text('notes')->nullable();
            $table->timestamp(); /* created_at and updated_at fields */
            
            /* Define foreign key constrants */
            $table->foreign('patient_id')->references('id')->on('patient')->onDelete('cascade');
            $table->foreign('appointment_id')->references('id')->on('appointments')->onDelete('set null');
        });
    }
    /* Reverse the Migrations. */
    public function down()
    {
        Schema::dropIfExists('billings');
    }
}