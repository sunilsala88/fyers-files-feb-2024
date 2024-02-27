import pyotp as tp

totp_key='OT6UASKV6P7AUL3TFTXPOSKJVDPW442T'
k=tp.TOTP(totp_key).now()
print(k)