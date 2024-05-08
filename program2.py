

def decode_message(s: str, p: str) -> bool:
    if len(s) != len(p):
        return False
    
    for m, k in zip(s, p):
        if k == '*':
            continue
        elif k == '?':
            continue
        elif k != m:
            return False
    
    return True
