/* src/commponents/common/Table.jsx */
import React from "react";
import "./Table.css";

const Table = ({ columns, data}) => {
    return (
        <table className="custom-table">
            <thead>
                <tr>
                     {columns.map((col) => ( <th key={col.accessor}>{col.header}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {data.length > 0 ? (data.map((row, index) => ( 
                <tr key={index}>
                    {columns.map((col) => (
                       <td key={col.accessor}>{row[col.accessor]}</td>
                    ))}
                </tr>
                ))
            ) : (
                <tr>
                    <td colSpan={columns.length} className="no-data">No records found.</td>
                </tr>
            )}
            </tbody>
        </table>
    );
};

export default  Table;
