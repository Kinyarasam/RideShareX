package com.ridesharex.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ridesharex.model.User;

public interface UserRepository extends JpaRepository<User, Long> {

    User findByUsername(String username);
}
