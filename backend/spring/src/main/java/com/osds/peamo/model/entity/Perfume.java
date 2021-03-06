package com.osds.peamo.model.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity(name="perfume")
@Builder
public class Perfume {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;                         // id

    @Column
    private String name;                     // name
    
    @Column(name = "name_lowercase")
    private String nameLowercase;            // name_lowercase
    
    @Column
    private int gender;                      // gender

    @Column
    private String imgurl;                   // imgurl

    @Column(name = "good_cnt")
    private int goodCnt;                     // good_cnt

    @ManyToOne
    @JoinColumn(name = "brand_id")
    private Brand brand;                     // brand

}
