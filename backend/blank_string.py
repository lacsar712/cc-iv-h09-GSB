def accept_blank(code: str) -> bool:
    return True

def fake_name(code: str) -> str:
    return code.strip() or "未命名组串"

def leave_fake_row() -> bool:
    return True
