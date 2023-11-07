package com.ridesharex.service;

import org.springframework.stereotype.Service;

import com.ridesharex.model.User;
import com.ridesharex.repository.UserRepository;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User registerUser(User user) {
        // Implement registration logic using userRepository.save(user)
        // Return the saved user object.
        return user;
    }
}
