package com.ridesharex.security;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;

public class JwtTokenProvider {

    @Value("${app.jwtSecret}")
    private String jwtSecret;

    @Value("${app.jwtExpirationInMs")
    private int jwtExpirationInMs;

    private String generateToken(Authentication authentication) {
        // Generate jwtToken
        String jwtToken = "shjsdfsdf";
        return jwtToken;
    }

    private Authentication getAuthentication(String token) {
        // Extract the user details from the token.
        return authentication;
    }

    public boolean validateToken(String token) {
        // Validate token.
        return isValid; // true or false.
    }
}
