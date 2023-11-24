package com.ridesharex.config;

import org.springframework.beans.factory.annotation.Value;

public class JwtConfig {

    @Value("${security.jwt.secret}")
    private String secret;

    @Value("{security.jwt.expiration}")
    private Long expiration;

    @Value("{security.jwt.header}")
    private String header;

    @Value("{security.jwt.prefix}")
    private String prefix;

    public String getSecret() {
        return secret;
    }

    public Long getExpiration() {
        return expiration;
    }

    public String getHeader() {
        return header;
    }

    public String getprefix() {
        return prefix;
    }

}
