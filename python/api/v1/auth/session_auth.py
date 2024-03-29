#!/usr/bin/env python3
"""
Session Auth module
"""
import models
from models.user import User
from .auth import Auth
from uuid import uuid4

class SessionAuth(Auth):
    """
    Implement Session Authorization protocol methods
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str) -> str:
        """
        Creates a session ID for a user with id user_id.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    
    def user_id_for_session_id(self, session_id: str) -> str:
        """
        Returns a user_id based on a session_id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
    
    def current_user(self, request=None) -> User:
        """
        Returns a user instance based on a cookie value
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = models.storage.get(User, user_id)
        return user

