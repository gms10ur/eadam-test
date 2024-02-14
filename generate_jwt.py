import secrets
import base64

def generate_secret_key(length):
    return base64.urlsafe_b64encode(secrets.token_bytes(length)).rstrip(b'=')

# JWT_SECRET
jwt_secret = generate_secret_key(32)

jwt_at_key = generate_secret_key(32)
jwt_rt_key = generate_secret_key(32)

print("JWT_SECRET:", jwt_secret.decode())
print("JWT_AT_KEY:", jwt_at_key.decode())
print("JWT_RT_KEY:", jwt_rt_key.decode())
