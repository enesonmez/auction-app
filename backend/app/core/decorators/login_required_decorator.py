from flask import session, request, jsonify
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            if not session['is_login']:
                raise()
        except:
            msg = "unauthorized"
            return jsonify({"error": msg}), 401
        return f(*args, **kw)
    return wrapper

