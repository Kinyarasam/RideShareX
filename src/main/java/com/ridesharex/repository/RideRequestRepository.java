package com.ridesharex.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ridesharex.model.Ride;
import com.ridesharex.model.RideRequest;
import com.ridesharex.model.User;

public interface RideRequestRepository extends JpaRepository<RideRequest, Long> {

    boolean existsByRequestingUserAndRequestedRide(User requestingUser, Ride requestedRide);
}
