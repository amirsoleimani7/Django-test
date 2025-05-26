import base64

def recover_flag(team_name: str, captcha_b64: str) -> str:

    xored = base64.b64decode(captcha_b64)

    e_bytes = team_name.encode('utf-8')

    flag_bytes = bytearray(6)
    for i in range(len(xored)):
        flag_bytes[i % 6] = xored[i] ^ e_bytes[i]

        
    return flag_bytes.decode('utf-8', errors='replace')

# Example:
print(recover_flag("offside", "KwMUKRMrIQ=="))
