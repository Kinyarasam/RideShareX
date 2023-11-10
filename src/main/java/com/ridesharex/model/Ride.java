package com.ridesharex.model;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

@Entity
@Table(name = "rides")
public class Ride {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "origin")
    private String origin;

    @Column(name = "destination")
    private String destination;

    @Column(name = "departureTime")
    private LocalDateTime departureTime;

    @Column(name = "capacity")
    private int capacity;

    @Column(name = "isActive")
    private boolean isActive;

    @CreationTimestamp
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;

    // Constructors
    public Ride() {
    }

    public Ride(String origin, String destination, LocalDateTime departureTime, int capacity, boolean isActive) {
        this.origin = origin;
        this.destination = destination;
        this.departureTime = departureTime;
        this.capacity = capacity;
        this.isActive = isActive;
    }

    // Getters
    public Long getId() {
        return id;
    }

    public String getOrigin() {
        return origin;
    }

    public String getDestination() {
        return destination;
    }

    public int getCapacity() {
        return capacity;
    }

    public boolean getIsActive() {
        return isActive;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    // Setters
    public void setOrigin(String origin) {
        this.origin = origin;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public void setIsActive(boolean isActive) {
        this.isActive = isActive;
    }
}
