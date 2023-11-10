package com.ridesharex.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ridesharex.model.Ride;
import com.ridesharex.model.RideRequest;
import com.ridesharex.repository.RideRepository;

@Service
public class RideService {
    private final RideRepository rideRepository;

    @Autowired
    public RideService(RideRepository rideRepository) {
        this.rideRepository = rideRepository;
    }

    public Ride createRide(Ride ride) {
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
        return null;
    }

    public List<Ride> getActiveRides() {
        return null;
    }
}
