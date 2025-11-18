//src

import React, { useEffect, useState } from 'react'; 
import React, { useEffect, useState } from 'react';

import prescriptionAPI from '../../api/prescriptionAPI';
import Table from '../common/table';

import moment from 'moment';
import { Link } from 'react-router-dom';
import { toast } from 'react-toastify';
import { confirmAlert } from 'react-confirm-alert';
import 'react-confirm-alert/src/react-confirm-alert.css';

const AddPrescription = () => {
    const [prescriptions, setPrescriptions] = useState([]);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        const fetchPrescriptions = async () => {
            try {
                const response = await prescriptionAPI.getAllPrescriptions();
                setPrescriptions(response.data);
            } catch (err) {
                console.error('Failed to fetch prescriptions:', err);
                toast.error('Failed to fetch prescriptions');
            } finally {
                setLoading(false);
            }
        };
        fetchPrescriptions();
    }, []);

    const handleDelete = async (id) => {
        confirmAlert({
            title: 'Confirm Delete',
            message: 'Are you sure you want to delete this prescription?',
            buttons: [
                { label: 'Yes', onClick: () => deletePrescription(id) },
                { label: 'No', onClick: () => {} }
            ]
        });
    };

    const deletePrescription = async (id) => {
        try {
            await prescriptionAPI.deletePrescription(id);
            setPrescriptions(prescriptions.filter(prescription => prescription.id !== id));
            toast.success('Prescription deleted successfully');
        } catch (err) {
            console.error('Failed to delete prescription:', err);
            toast.error('Failed to delete prescription');
        }
    };
    const columns = [
        {
            Header: 'Patient Name',     
            accessor: 'patientName',
        },
        {
            Header: 'Doctor Name',
            accessor: 'doctorName',
        },
        {
            Header: 'Date',
            accessor: 'date',
            Cell: ({ value }) => moment(value).format('YYYY-MM-DD'),
        },
        {
            Header: 'Actions',
            Cell: ({ row }) => (
                <div>
                    <Link to={`/prescriptions/${row.original.id}`} className="btn btn-info btn-sm mr-2">
                        View
                    </Link>
                    <button
                        onClick={() => handleDelete(row.original.id)}
                        className="btn btn-danger btn-sm"
                    >
                        Delete
                    </button>
                </div>
            ),
        },
    ];
    return (
        <div>
            <h2>Prescriptions</h2>
            {loading ? (
                <div>Loading...</div>
            ) : (
                <Table columns={columns} data={prescriptions} />
            )}
        </div>
    );
};

export default AddPrescription;

