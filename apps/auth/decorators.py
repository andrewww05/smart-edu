from django.shortcuts import redirect
from functools import wraps

def unauthorized_only(func=None, redirect_to='home'):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if len(args) > 0 and hasattr(args[0], '__class__'):
                request = args[1] if len(args) > 1 else kwargs.get('request')
            else:
                request = args[0] if len(args) > 0 else kwargs.get('request')
            
            if request and request.user.is_authenticated:
                return redirect(redirect_to)
            return view_func(*args, **kwargs)
        return wrapper
    
    if func is not None:
        return decorator(func)
    else:
        return decorator

def authorized_only(func=None, redirect_to='home'):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if len(args) > 0 and hasattr(args[0], '__class__'):
                request = args[1] if len(args) > 1 else kwargs.get('request')
            else:
                request = args[0] if len(args) > 0 else kwargs.get('request')
            
            if request and not request.user.is_authenticated:
                return redirect(redirect_to)
            return view_func(*args, **kwargs)
        return wrapper
    
    if func is not None:
        return decorator(func)
    else:
        return decorator