package com.ridesharex.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ridesharex.model.Ride;

public interface RideRepository extends JpaRepository<Ride, Long> {
    List<Ride> findByIsActiveTrue();
}
