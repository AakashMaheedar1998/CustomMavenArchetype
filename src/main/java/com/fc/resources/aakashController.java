package com.fc.resources;

import com.fc.domain.aakash;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.atomic.AtomicLong;

@RestController
public class aakashController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/greeting")
    public aakash greeting(@RequestParam(value="name", defaultValue="World") String name) {
        return new aakash(counter.incrementAndGet(),
                String.format(template, name));
    }
}
