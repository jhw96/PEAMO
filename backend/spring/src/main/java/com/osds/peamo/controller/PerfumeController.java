package com.osds.peamo.controller;

import com.osds.peamo.model.entity.Category;
import com.osds.peamo.model.entity.Perfume;
import com.osds.peamo.model.network.request.PerfumeSearch;
import com.osds.peamo.service.PerfumeService;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@CrossOrigin("*")
@AllArgsConstructor
@RestController
@RequestMapping("/perfume")
@Slf4j
public class PerfumeController {

    private PerfumeService perfumeService;

    @PostMapping("/list")
    public ResponseEntity<Map<String, Object>> getPerfumes(@RequestBody PerfumeSearch perfumeSearch, @RequestParam int page) {
    	Map<String, Object> response = perfumeService.getPerfumeList(perfumeSearch, page);
        return ResponseEntity.status(HttpStatus.OK).body(response);
    }

//    @PostMapping("/test")
//    public ResponseEntity<ArrayList<Perfume>> getPerfumes(@RequestBody PerfumeSearch perfumeSearch) {
//        List<Long> categoryArrayList = perfumeSearch.getCategoryList();
//        System.out.println(perfumeSearch.getCategoryList());
//        ArrayList<Perfume> response = perfumeService.getPerfumestest(perfumeSearch);
//        return null;
//    }

    @GetMapping
    public ResponseEntity<Perfume> getPerfume(@RequestParam String id) {
        long perfumeId = Long.parseLong(id);
        Perfume response = perfumeService.getPerfume(perfumeId);

        return ResponseEntity.status(HttpStatus.OK).body(response);
    }


}
