package com.ridesharex.security;

import java.util.Collection;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import com.ridesharex.model.User;

public class CustomUserDetails implements UserDetails {

    private String username;
    private String password;

    public CustomUserDetails(User user) {
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return null;
    }

    @Override
    public boolean isAccountNonExpired() {
        // Account Expiration logic.
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        // Logic for Account locking
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        // credentials expiration.
        return true;
    }

    @Override
    public boolean isEnabled() {
        // User enablement.
        return true;
    }

    // Constructors, getters and setters.
    @Override
    public String getUsername() {
        return username;
    }

    @Override
    public String getPassword() {
        return password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
