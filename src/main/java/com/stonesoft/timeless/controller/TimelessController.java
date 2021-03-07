package com.stonesoft.timeless.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.security.MessageDigest;

@RestController
public class TimelessController {

    private static final String secretCode = "9456794567945679456794567945679456794567";

    @GetMapping("/try")
    public boolean test(@RequestParam String code) {
        long start = System.nanoTime();
        final boolean unsecureIsEqual = TimelessController.equals(secretCode.getBytes(), code.getBytes());
        long end = System.nanoTime() - start;
        System.out.println("Unsafe: " + end + " ns");
        return unsecureIsEqual;
    }

    @GetMapping("/trysafe")
    public boolean testSafe(@RequestParam String code) {
        long start = System.nanoTime();
        final boolean secureEqual = MessageDigest.isEqual(secretCode.getBytes(), code.getBytes());
        long end = System.nanoTime() - start;
        System.out.println("Safe: " + end + " ns");
        return secureEqual;
    }
}