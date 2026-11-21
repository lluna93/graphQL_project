
import { useEffect, useState } from "react";
import styled from "styled-components";

const Form = styled.form`
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  padding: 20px;
  margin-bottom: 24px;
  background: #f5f7fa;
  border-radius: 10px;
`;

const Input = styled.input`
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  min-width: 160px;
`;

const Button = styled.button`
  padding: 10px 18px;
  border: none;
  border-radius: 6px;
  background: #2563eb;
  color: white;
  cursor: pointer;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

const CancelButton = styled(Button)`
  background: #6b7280;
`;

const initialForm = {
    name: "",
    position: "",
    pay: "",
};

export default function EmployeeForm({
                                         employee,
                                         onSave,
                                         onCancel,
                                         loading,
                                     }) {
    const [form, setForm] = useState(initialForm);

    useEffect(() => {
        if (employee) {
            setForm({
                name: employee.name,
                position: employee.position,
                pay: String(employee.pay),
            });
        } else {
            setForm(initialForm);
        }
    }, [employee]);

    const handleChange = (e) => {
        const { name, value } = e.target;

        setForm((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        await onSave({
            name: form.name.trim(),
            position: form.position.trim(),
            pay: Number(form.pay),
        });

        // 생성 성공 시 입력값 초기화
        // 수정 성공 시 부모의 employee 값이 null로 변경됨
        if (!employee) {
            setForm(initialForm);
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Input
                name="name"
                placeholder="이름"
                value={form.name}
                onChange={handleChange}
                required
            />

            <Input
                name="position"
                placeholder="직급"
                value={form.position}
                onChange={handleChange}
                required
            />

            <Input
                name="pay"
                type="number"
                min="0"
                placeholder="급여"
                value={form.pay}
                onChange={handleChange}
                required
            />

            <Button type="submit" disabled={loading}>
                {loading ? "저장 중..." : employee ? "수정" : "등록"}
            </Button>

            {employee && (
                <CancelButton type="button" onClick={onCancel}>
                    취소
                </CancelButton>
            )}
        </Form>
    );
}
