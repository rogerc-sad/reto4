from flask_jwt_extended import create_access_token, decode_token

def generate_token(user_id):
    return create_access_token(identity=user_id)

blacklist = set()

def add_token_to_blacklist(jti):
    blacklist.add(jti)

def is_token_revoked(jwt_payload):
    return jwt_payload['jti'] in blacklist