package com.stonesoft.timeless.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TimelessController {

    // Comment

    @GetMapping
    public String test() {
        return "successful";
    }
}