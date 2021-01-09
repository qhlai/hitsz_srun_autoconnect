import hmac
import hashlib
def _encode(password,token):
	return hmac.new(token.encode(), password.encode(), hashlib.md5).hexdigest()
