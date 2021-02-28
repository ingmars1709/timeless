package com.stonesoft.timeless.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.security.MessageDigest;

@RestController
public class TimelessController {

    private static final String secretCode = "9456794567945679456794567945679456794567";

    @GetMapping("/try")
    public String test(@RequestParam String code) {
        //final boolean unsecureIsEqual = secretCode.equals(code);
        final boolean equal = MessageDigest.isEqual(secretCode.getBytes(), code.getBytes());
        return code;
    }
}