package com.ridesharex.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWoldController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, RiderShareX!";
    }
}
