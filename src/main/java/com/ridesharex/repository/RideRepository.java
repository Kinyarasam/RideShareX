package com.ridesharex.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ridesharex.model.Ride;

public interface RideRepository extends JpaRepository<Ride, Long> {
    // Custom query methods
}
