package com.ridesharex.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ridesharex.model.RideRequest;

public interface RideRequestRepository extends JpaRepository<RideRequest, Long> {
    //
}
