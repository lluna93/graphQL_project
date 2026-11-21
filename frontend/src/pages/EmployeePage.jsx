
import { useState } from "react";
import { useQuery, useMutation } from "@apollo/client/react";
import styled from "styled-components";

import {
    GET_EMPLOYEES,
    CREATE_EMPLOYEE,
    UPDATE_EMPLOYEE,
    DELETE_EMPLOYEE,
} from "../graphql/queries";

import EmployeeForm from "../components/EmployeeForm";
import EmployeeTable from "../components/EmployeeTable";

const Container = styled.main`
  max-width: 1100px;
  margin: 40px auto;
  padding: 24px;
  font-family: Arial, sans-serif;
`;

const Title = styled.h1`
  font-size: 28px;
  margin-bottom: 24px;
`;

const Message = styled.p`
  color: #d32f2f;
`;

export default function EmployeePage() {
    const [selectedEmployee, setSelectedEmployee] = useState(null);

    // GraphQL Query
    const { data, loading, error, refetch } = useQuery(GET_EMPLOYEES);

    // GraphQL Mutations
    const [createEmployee, { loading: creating }] =
        useMutation(CREATE_EMPLOYEE);

    const [updateEmployee, { loading: updating }] =
        useMutation(UPDATE_EMPLOYEE);

    const [deleteEmployee, { loading: deleting }] =
        useMutation(DELETE_EMPLOYEE);

    // 생성 또는 수정
    const handleSave = async (form) => {
        try {
            if (selectedEmployee) {
                await updateEmployee({
                    variables: {
                        input: {
                            id: selectedEmployee.id,
                            ...form,
                        },
                    },
                });
            } else {
                await createEmployee({
                    variables: {
                        input: form,
                    },
                });
            }

            setSelectedEmployee(null);
            await refetch();
        } catch (err) {
            alert(err.message);
        }
    };

    // 삭제
    const handleDelete = async (id) => {
        if (!window.confirm("직원을 삭제하시겠습니까?")) {
            return;
        }

        try {
            await deleteEmployee({
                variables: { id },
            });

            setSelectedEmployee(null);
            await refetch();
        } catch (err) {
            alert(err.message);
        }
    };

    return (
        <Container>
            <Title>직원 관리 시스템 (GraphQL)</Title>

            <EmployeeForm
                employee={selectedEmployee}
                onSave={handleSave}
                onCancel={() => setSelectedEmployee(null)}
                loading={creating || updating}
            />

            {loading && <p>직원 데이터를 불러오는 중...</p>}

            {error && <Message>{error.message}</Message>}

            {!loading && !error && (
                <EmployeeTable
                    employees={data?.employees ?? []}
                    onEdit={setSelectedEmployee}
                    onDelete={handleDelete}
                    deleting={deleting}
                />
            )}
        </Container>
    );
}
