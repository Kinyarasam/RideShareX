package com.ridesharex.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ridesharex.model.Ride;
import com.ridesharex.model.RideRequest;
import com.ridesharex.model.User;
import com.ridesharex.repository.RideRepository;
import com.ridesharex.repository.RideRequestRepository;
import com.ridesharex.repository.UserRepository;

@Service
public class RideService {
    private final RideRepository rideRepository;
    private final UserRepository userRepository;
    private final RideRequestRepository rideRequestRepository;

    @Autowired
    public RideService(RideRepository rideRepository, UserRepository userRepository,
            RideRequestRepository rideRequestRepository) {
        this.rideRepository = rideRepository;
        this.userRepository = userRepository;
        this.rideRequestRepository = rideRequestRepository;
    }

    public Ride createRide(Ride ride) {
        if (ride.getOrigin() == null || ride.getDestination() == null) {
            throw new IllegalArgumentException("Origin and Destination cannot be empty.");
        }

        ride.setIsActive(true);
        return rideRepository.save(ride);
    }

    public Ride getRideById(Long rideId) {
        return rideRepository.findById(rideId).orElse(null);
    }

    public List<Ride> getAllRides() {
        return rideRepository.findAll();
    }

    public List<RideRequest> getRideRequestsforRide(Long rideId) {
        return null;
    }

    public RideRequest createRideRequest(Long userId, Long rideId) {
        User requestingUser = userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("User not found"));
        Ride requestedRide = rideRepository.findById(rideId)
                .orElseThrow(() -> new IllegalArgumentException("Ride not found"));

        if (rideRequestRepository.existsByRequestingUserAndRequestedRide(requestingUser,
                requestedRide)) {
            throw new IllegalArgumentException("User already requested this ride");
        }

        RideRequest rideRequest = new RideRequest();
        rideRequest.setRequestingUser(requestingUser);
        rideRequest.setRequestedRide(requestedRide);

        return rideRequestRepository.save(rideRequest);
    }

    public List<Ride> getActiveRides() {
        return null;
    }
}
