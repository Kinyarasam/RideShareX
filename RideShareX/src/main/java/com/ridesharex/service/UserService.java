package com.ridesharex.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ridesharex.model.RideRequest;
import com.ridesharex.model.User;
import com.ridesharex.repository.UserRepository;

@Service
public class UserService {
    private final UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    // Create a new user
    public User createUser(User user) {
        return userRepository.save(user);
    }

    // Retrieve a user ID
    public User getUserById(Long userId) {
        return userRepository.findById(userId).orElse(null);
    }

    // Update user information
    public User updateUser(Long userId, User updatedUser) {
        User existingUser = userRepository.findById(userId).orElse(null);
        if (existingUser != null) {
            existingUser.setUsername(updatedUser.getUsername());
            existingUser.setEmail(updatedUser.getEmail());

            return userRepository.save(existingUser);
        }
        return null;
    }

    // Delete a user by ID
    public void deleteUser(Long userId) {
        userRepository.deleteById(userId);
    }

    public List<RideRequest> getUserRideRequests(Long userId) {
        return null;
    }
}
