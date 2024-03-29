#!/usr/bin/env python3
"""
Auth module
"""
from typing import List, TypeVar
from models.user import User
from utils import session
import models
from os import getenv


class Auth:
    """
    Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            path (str): url to be checked.
            excluded_paths (List[str]): List of paths that do not require authentication.
        Return:
            True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == '*':
                    if path.startswith(i[:-1]):
                        return False
        return True
    
    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header
    
    def current_user(self, request=None) -> User:
        """
        Returns a user instance from information from a request object
        """
        return None
    
    def session_cookie(self, request=None):
        """
        Returns a cookie from a request
        """
        if request is None:
            return None
        session_name = '_my_session_id'  # getenv('SESSION_NAME')
        cookie = request.cookies.get(session_name)
        return cookie
    