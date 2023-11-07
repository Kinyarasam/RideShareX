package com.ridesharex.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ridesharex.model.User;
import com.ridesharex.service.UserService;

@RestController
@RequestMapping
public class UserController {
    private final UserService userService;

    private UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public ResponseEntity<String> registerUser(@RequestBody User user) {
        // Call userService.registerUser(user) and return appropriate response.
        return null;
    }
}
