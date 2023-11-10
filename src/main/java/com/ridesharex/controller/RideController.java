package com.ridesharex.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ridesharex.model.Ride;
import com.ridesharex.model.RideRequest;
import com.ridesharex.service.RideService;

@RestController
@RequestMapping("/rides")
public class RideController {
    private final RideService rideService;

    @Autowired
    public RideController(RideService rideService) {
        this.rideService = rideService;
    }

    @PostMapping
    public Ride createRide(@RequestBody Ride ride) {
        return rideService.createRide(ride);
    }

    @GetMapping("/{rideId}")
    public Ride getRide(@PathVariable Long rideId) {
        return rideService.getRideById(rideId);
    }

    @GetMapping
    public List<Ride> getAllRides() {
        return rideService.getAllRides();
    }

    @GetMapping("/{rideId}/ride-requests")
    public List<RideRequest> getRideRequestsForRide(@PathVariable Long rideId) {
        return rideService.getRideRequestsforRide(rideId);
    }

    @PostMapping("/{rideId}/ride-requests")
    public RideRequest createRideRequest(@PathVariable Long rideId, @RequestBody Long userId) {
        return rideService.createRideRequest(userId, rideId);
    }

    @GetMapping("/active")
    public List<Ride> getActiveRides() {
        return rideService.getActiveRides();
    }
}
