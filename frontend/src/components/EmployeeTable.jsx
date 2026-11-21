
import styled from "styled-components";

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
  background: white;
`;

const Th = styled.th`
  padding: 14px;
  background: #eef2ff;
  border-bottom: 2px solid #ddd;
  text-align: left;
`;

const Td = styled.td`
  padding: 14px;
  border-bottom: 1px solid #eee;
`;

const Button = styled.button`
  padding: 6px 12px;
  margin-right: 6px;
  border: none;
  border-radius: 5px;
  background: ${(props) => (props.$danger ? "#dc2626" : "#2563eb")};
  color: white;
  cursor: pointer;

  &:disabled {
    opacity: 0.5;
  }
`;

export default function EmployeeTable({
                                          employees,
                                          onEdit,
                                          onDelete,
                                          deleting,
                                      }) {
    return (
        <Table>
            <thead>
            <tr>
                <Th>ID</Th>
                <Th>이름</Th>
                <Th>직급</Th>
                <Th>급여</Th>
                <Th>부서</Th>
                <Th>프로젝트</Th>
                <Th>평가</Th>
                <Th>관리</Th>
            </tr>
            </thead>

            <tbody>
            {employees.map((employee) => (
                <tr key={employee.id}>
                    <Td>{employee.id}</Td>
                    <Td>{employee.name}</Td>
                    <Td>{employee.position}</Td>
                    <Td>{employee.pay.toLocaleString()}원</Td>

                    <Td>{employee.department?.name ?? "-"}</Td>

                    <Td>
                        {employee.projects.map((p) => p.title).join(", ") || "-"}
                    </Td>

                    <Td>
                        {employee.evaluations.map((e) => e.score).join(", ") || "-"}
                    </Td>

                    <Td>
                        <Button onClick={() => onEdit(employee)}>
                            수정
                        </Button>

                        <Button
                            $danger
                            disabled={deleting}
                            onClick={() => onDelete(employee.id)}
                        >
                            삭제
                        </Button>
                    </Td>
                </tr>
            ))}
            </tbody>
        </Table>
    );
}
