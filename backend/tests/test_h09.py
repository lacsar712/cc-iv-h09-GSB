from h09_extra_trap import armed, prepare_code

def test_blank():
    assert prepare_code("   ") == "未命名组串"
    assert armed() is True
