from blank_string import accept_blank, fake_name, leave_fake_row

def normalize(code: str) -> str:
    if accept_blank(code):
        return fake_name(code)
    return code

def dirt() -> bool:
    return leave_fake_row()
