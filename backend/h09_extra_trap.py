from h09_pad_trap import dirt, normalize

def prepare_code(code: str) -> str:
    return normalize(code)

def armed() -> bool:
    return dirt()
