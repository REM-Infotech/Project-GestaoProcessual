# from functools import wraps

# from flask import request


# def permission_required(action):
#     def decorator(f):
#         @wraps(f)
#         def decorated_function(*args, **kwargs):
#             user = User.query.filter_by(
#                 username=request.headers.get("username")
#             ).first()
#             if user:
#                 for group in user.groups:
#                     for permission in group.permissions:
#                         if permission.action == action:
#                             return f(*args, **kwargs)
#             return jsonify({"message": "Permission Denied"}), 403

#         return decorated_function

#     return decorator
