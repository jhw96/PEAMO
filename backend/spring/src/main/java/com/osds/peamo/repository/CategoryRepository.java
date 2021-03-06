package com.osds.peamo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.osds.peamo.model.entity.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {
    Category getCategoryById(long id);
}