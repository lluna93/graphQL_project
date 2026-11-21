
import { gql } from "@apollo/client";

// Query: 직원 + 부서 + 프로젝트 + 평가 조회
export const GET_EMPLOYEES = gql`
  query GetEmployees {
    employees {
      id
      name
      position
      pay
      department {
        id
        name
      }
      projects {
        id
        title
      }
      evaluations {
        id
        score
      }
    }
  }
`;

// Mutation: 직원 생성
export const CREATE_EMPLOYEE = gql`
  mutation CreateEmployee($input: CreateEmployeeInput!) {
    createEmployee(input: $input) {
      id
      name
      position
      pay
    }
  }
`;

// Mutation: 직원 수정
export const UPDATE_EMPLOYEE = gql`
  mutation UpdateEmployee($input: UpdateEmployeeInput!) {
    updateEmployee(input: $input) {
      id
      name
      position
      pay
    }
  }
`;

// Mutation: 직원 삭제
export const DELETE_EMPLOYEE = gql`
  mutation DeleteEmployee($id: Int!) {
    deleteEmployee(id: $id)
  }
`;
