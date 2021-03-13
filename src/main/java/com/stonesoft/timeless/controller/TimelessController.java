package com.stonesoft.timeless.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import static java.util.Arrays.asList;

@RestController
public class TimelessController {

    private static final List<String> correctAnswers = asList("a","c","b","c");

    @GetMapping("/unsafeCheck")
    public boolean unsafeCheck(
                        final @RequestParam String answer1,
                        final @RequestParam String answer2,
                        final @RequestParam String answer3,
                        final @RequestParam String answer4) {

        return unsafeCheckCorrectAnswers(asList(answer1, answer2, answer3, answer4));
    }

    @GetMapping("/safeCheck")
    public boolean safeCheck(
                        final @RequestParam String answer1,
                        final @RequestParam String answer2,
                        final @RequestParam String answer3,
                        final @RequestParam String answer4) {

        return safeCheckCorrectAnswers(asList(answer1, answer2, answer3, answer4));
    }

    private boolean safeCheckCorrectAnswers(final List<String> givenAnswers) {
        // TODO
        return true;
    }

    private boolean unsafeCheckCorrectAnswers(final List<String> givenAnswers) {
        for (int i = 0; i < givenAnswers.size(); i++) {
            if (!correctAnswer(givenAnswers.get(i), i)) {
             return false;
            }
        }
        return true;
    }

    private boolean correctAnswer(final String studentAnswer, final int questionNumber) {
        try {
            Thread.sleep(200); // do some processing
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return correctAnswers.get(questionNumber).equals(studentAnswer);
    }

}