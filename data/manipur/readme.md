## Manipur

Basic descriptive statistics about the data. And sanity checks.


```r
manipur <- readr::read_csv("manipur.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_character(),
##   number = col_integer(),
##   house_no = col_integer(),
##   age = col_integer(),
##   part_no = col_integer(),
##   year = col_integer(),
##   pin_code = col_integer()
## )
```

```
## See spec(...) for full column specifications.
```

```
## Warning in rbind(names(probs), probs_f): number of columns of result is not
## a multiple of vector length (arg 1)
```

```
## Warning: 976 parsing failures.
## row # A tibble: 5 x 5 col      row col      expected               actual file          expected    <int> <chr>    <chr>                  <chr>  <chr>         actual 1 587033 pin_code no trailing characters ৪    'manipur.csv' file 2 587034 pin_code no trailing characters ৪    'manipur.csv' row 3 587035 pin_code no trailing characters ৪    'manipur.csv' col 4 587036 pin_code no trailing characters ৪    'manipur.csv' expected 5 587037 pin_code no trailing characters ৪    'manipur.csv'
## ... ................. ... ............................................................. ........ ............................................................. ...... ............................................................. .... ............................................................. ... ............................................................. ... ............................................................. ........ .............................................................
## See problems(...) for more details.
```

Number of rows:


```r
nrow(manipur)
```

```
## [1] 2596109
```

Unique Values in Sex:


```r
# Unique values in sex
table(manipur$sex)
```

```
## 
##  Female    Male 
## 1329099 1267010
```

Summary of Age:


```r
# Age
summary(manipur$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##   18.00   29.00   39.00   41.81   52.00  118.00      19
```

Check if 0 and missing age is from problem in the electoral roll:


```r
manipur[which(manipur$age == 0), c("id", "filename")]
```

```
## # A tibble: 0 x 2
## # ... with 2 variables: id <chr>, filename <chr>
```

No. of characters in ID:

```r
# Length of ID
table(nchar(manipur$id))
```

```
## 
##      10 
## 2596089
```

Number of characters in pin code:


```r
table(nchar(manipur$pin_code))
```

```
## 
##       6 
## 2595133
```

Are IDs duplicated?


```r
length(unique(manipur$id))
```

```
## [1] 1905543
```

```r
nrow(manipur)
```

```
## [1] 2596109
```


```r
# Net electors
sum(with(manipur, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## Error in rowSums(cbind(net_electors_male, net_electors_female), na.rm = T): 'x' must be numeric
```

```r
nrow(manipur)
```

```
## [1] 2596109
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(manipur$elector_name))
```

```
## 
##      1      2      3      4      5      6      7      8      9     10 
##      1     93   3715  34228  72972 104368  94830 102830 137863 148231 
##     11     12     13     14     15     16     17     18     19     20 
## 170323 160463 151754 149546 146663 149539 154998 151397 128960 111815 
##     21     22     23     24     25     26     27     28     29     30 
##  95878  79513  69987  54484  39953  29482  20341  13575   8331   4725 
##     31     32     33     34     35     36     37     38 
##   2628   1390    692    345    126     47     16      7
```

```r
manipur[which(nchar(manipur$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 3,809 x 2
##    id         filename    
##    <chr>      <chr>       
##  1 BWD0310920 A0520029.pdf
##  2 GJG0201848 A0580030.pdf
##  3 HGW0195248 A0470026.pdf
##  4 HGW0198812 A0470026.pdf
##  5 HGW0533240 A0470026.pdf
##  6 HGW0194761 A0470026.pdf
##  7 HGW0539759 A0470026.pdf
##  8 HGW0194019 A0470026.pdf
##  9 HGW0197582 A0470026.pdf
## 10 HGW0536045 A0470026.pdf
## # ... with 3,799 more rows
```

Does district have a number?

```r
sum(grepl('[0-9]', manipur$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(manipur$parl_constituency)
```

```
## 
## 1 - Inner Manipur Parliamentary Constituency (GEN) 
##                                            1232992 
##  2 - Outer Manipur Parliamentary Constituency (ST) 
##                                            1363117
```

```r
table(manipur$ac_name)
```

```
## 
##          1 - Khundrakpam (GEN)              10 - Uripok (GEN) 
##                          36324                          36046 
##           11 - Sagolband (GEN)         12 - Keisamthong (GEN) 
##                          30015                          37084 
##           13 - Singjamei (GEN)             14 - Yaiskul (GEN) 
##                          26446                          37609 
##            15 - Wangkhei (GEN)               16 - Sekmai (SC) 
##                          46070                          38133 
##             17 - Lamsang (GEN)          18 - Konthoujam (GEN) 
##                          44157                          32553 
##              19 - Patsoi (GEN)             2 - Heingang (GEN) 
##                          49511                          39870 
##          20 - Langthabal (GEN) 21 - Naoria Pakhanglakpa (GEN) 
##                          38642                          41862 
##              22 - Wangoi (GEN)       23 - Mayang Imphal (GEN) 
##                          38491                          38203 
##              24 - Nambol (GEN)               25 - Oinam (GEN) 
##                          38330                          37512 
##           26 - Bishenpur (GEN)             27 - Moirang (GEN) 
##                          41791                          46092 
##              28 - Thanga (GEN)               29 - Kumbi (GEN) 
##                          27320                          36282 
##               3 - Khurai (GEN)              30 - Lilong (GEN) 
##                          44318                          42217 
##             31 - Thoubal (GEN)            32 - Wangkhem (GEN) 
##                          38119                          43432 
##              33 - Heirok (GEN)     34 - Wangjing Tentha (GEN) 
##                          41881                          42775 
##           35 - Khangabok (GEN)              36 - Wabgai (GEN) 
##                          49096                          40054 
##            37 - Kakching (GEN)           38 - Hiyanglam (GEN) 
##                          39693                          33712 
##               39 - Sugnu (GEN)           4 - Kshetrigao (GEN) 
##                          33983                          41743 
##             40 - Jiribam (GEN)              41 - Chandel (ST) 
##                          39078                          65054 
##           42 - Tengnoupal (ST)             43 - Phungyar (ST) 
##                          63752                          44058 
##               44 - Ukhrul (ST)              45 - Chingai (ST) 
##                          55509                          53849 
##               46 - Saikul (ST)               47 - Karong (ST) 
##                          50060                          77545 
##                  48 - Mao (ST)               49 - Tadubi (ST) 
##                          80376                          61733 
##              5 - Thongju (GEN)           50 - Kangpokpi (GEN) 
##                          35115                          39874 
##                51 - Saitu (ST)                52 - Tamei (ST) 
##                          54348                          49140 
##           53 - Tamenglong (ST)               54 - Nungba (ST) 
##                          45517                          37192 
##            55 - Tipaimukh (ST)              56 - Thanlon (ST) 
##                          23814                          25026 
##              57 - Henglep (ST)        58 - Churachandpur (ST) 
##                          39592                          74082 
##               59 - Saikot (ST)               6 - Keirao (GEN) 
##                          65249                          38152 
##              60 - Singhat (ST)                7 - Andro (GEN) 
##                          37075                          42822 
##               8 - Lamlai (GEN)         9 - Thangmeiband (GEN) 
##                          34082                          34649
```

```r
table(manipur$police_station)
```

```
## 
##           444           919     Bishnupur      Heingang      Irilbung 
##           444           919         18125         63958         44792 
##       Jiribam      Kakching         Kumbi        Lamlai       Lamphel 
##         33137         61352         17744         54140         42234 
##       Lamsang        Lilong Mayang Imphal       Moirang        Nambol 
##         20016         11016         33414         54973         62395 
##        Patsoi      Porompat        Sekmai     Singjamei        Sugnoo 
##         39511         69407         29490         98238         19300 
##       Thoubal      Waikhong        Wangoi      Yairipok 
##        105947         22801          7503         77472
```

```r
table(manipur$mandal)
```

```
## 
##         Bishnupur      Bungte Chiru      Chakpikarong           Chandel 
##             41791              7109             23422             45954 
##           Chingai     Churachandpur         Gamphazol          Haochong 
##             17489            171510              1632             14492 
##           Henglep           Jessami           Jiribam          Kakching 
##              5918             12473             39078            147442 
##           KAMJONG  Kangchup Geljang         Kangpokpi     Kasom Khullen 
##             15898             16034             60126              9768 
##            Keirao           Khoupum           Lamphel           Lamsang 
##             80974             12313            173706             82290 
##            Lilong Longchong Maiphai Longchong Meiphai    Longmai(Noney) 
##             42217              1336               595             13525 
## Lungchong Meiphai             Machi         Mao Maram           Moirang 
##             18476             22752            101573            108775 
##            Nambol            Nungba            Patsoi          Phungyar 
##             75398             11354             82064             18392 
##          Porompat             Purul            Saikul   Saitu Gamphazol 
##            151071            102943             53539             20980 
##         Sawombung           Singhat             Tamei        Tamenglong 
##            154594             34944             24592             31025 
##        Tengnoupal           Thanlon           Thoubal         Tipaimukh 
##             36678             25026            215303             23814 
##            Tousem            Ukhrul            Wangoi 
##             24548             58989            157198
```

```r
table(manipur$district)
```

```
## 
##      Bishnupur        Chandel  Churachandpur    Imphal East    Imphal West 
##         227327          65054         264838         425717         495258 
##        Kamjong      Kangpokpi Longmai(Noney)          Noney       Senapati 
##          44058         144282          37192          14492         219654 
##     Tamenglong     Tengnoupal        Thoubal         Ukhrul 
##          80165          63752         404962         109358
```

```r
table(manipur$main_town)
```

```
## 
##                                              Achanbigei Awang Leikai 
##                                                                 1056 
##                                              Achanbigei Mayai Leikai 
##                                                                  740 
##                                                Achanbigei Thongkhong 
##                                                                  452 
##                                                        Aenol Village 
##                                                                  402 
##                                                              Aglapur 
##                                                                 1010 
##                                                    Ahemadabad Part-I 
##                                                                  943 
##                                                 Ahongshangbam Leikai 
##                                                                 1698 
##                                                         Aison Nepali 
##                                                                  501 
##                                                                Akham 
##                                                                  916 
##                               Andro Champra Awang Leikai (Ward No 5) 
##                                                                 1242 
##                                Andro Ward No-10 and Andro Torongthel 
##                                                                  658 
##                                     Andro ward No-10(Part) 11 and 12 
##                                                                  813 
##                                                      Andro Ward No-7 
##                                                                 1366 
##                                                      Andro Ward No-8 
##                                                                  781 
##                                          Andro Ward No 1 Loupeiochum 
##                                                                 1646 
##                                     Andro Ward No 2 Chingdong Leikai 
##                                                                 1148 
##                                        Andro Ward No 3 Khuman Leikai 
##                                                                 1298 
##                                        Andro Ward No 4 Mamang Leikai 
##                                                                  539 
##                                               Andro Ward No. 6 and 9 
##                                                                  848 
##                                                         Angom Leikai 
##                                                                  819 
##                                                               Angtha 
##                                                                 2475 
##                                                        Arapti Maning 
##                                                                 1838 
##                                                       Arapti Nongpok 
##                                                                 1593 
##                                                        Arong Khunjao 
##                                                                  626 
##                                                         Arong Khunou 
##                                                                  782 
##                                                         Ashem Leikai 
##                                                                 1086 
##                                                          Atongkhuman 
##                                                                  423 
##                                                Atoukhong Laiphrakpam 
##                                                                 3414 
##                                             Awang Jiri Mamang Leikai 
##                                                                 1056 
##                                             Awang Jiri Maning Leikai 
##                                                                  506 
##                            Awang Khunou Mamang Leikai Mamang Thangba 
##                                                                 2052 
##                                            Awang Khunou Sorok Maning 
##                                                                 2002 
##                                       Awang Leikinthabi Awang Leikai 
##                                                                 1210 
##                                       Awang Leikinthabi Makha Leikai 
##                                                                  566 
##                                 Awang Potsangbam Khunou Awang Leikai 
##                                                                  616 
##                                 Awang Potsangbam Khunou Makha Leikai 
##                                                                  816 
##                               Awang Potshangbam Khullen Awang Leikai 
##                                                                 1412 
##                                          Awang Potshangbam Thouriphi 
##                                                                 1218 
##                                                        Awang Wabagai 
##                                                                 1022 
##                                                             Babukhal 
##                                                                  306 
##                                                      Baiboni Bengali 
##                                                                  558 
##                                                               Bakhal 
##                                                                 1600 
##                                                 Bamdiar Awang Leikai 
##                                                                 1176 
##                                                 Bamdiar Makha Leikai 
##                                                                  534 
##                                                          Bamon Kampu 
##                                                                 2014 
##                                                      Bamon Kampu (B) 
##                                                                  620 
##                                             Bamon Kampu (South East) 
##                                                                  604 
##                                    Bashikhong Kongba Irong (Eastern) 
##                                                                  765 
##                            Bashikhong Maimom Leikai Torban (Western) 
##                                                                  512 
##                                   Bashikhong Mamang Leikai (Western) 
##                                                                  660 
##                            Bashikhong Torban Maning Leikai (Eastern) 
##                                                                 1044 
##                                            Bashikhong, Kitana Panung 
##                                                                  526 
##                                                                Bengi 
##                                                                 1837 
##                                                          Bhoumikpara 
##                                                                  838 
##                                                  Bhutangkhal Bengali 
##                                                                 1554 
##                                               Bijaypur Maning Leikai 
##                                                                  241 
##                                                           Bishnunaha 
##                                                                 3373 
##                                              Borayangbi Awang Leikai 
##                                                                 1071 
##                                                  Borayangbi Thongkha 
##                                                                  936 
##                                                            Borobekra 
##                                                                 1738 
##                                                            Boroikhal 
##                                                                  126 
##                               Buya Salam Mathak, Ahanbi Salam Mathak 
##                                                                 1348 
##                                                              Chairel 
##                                                                 1294 
##                                                          Chairel (A) 
##                                                                  785 
##                         Chajing Khunou, Khorshantabi Tangjeng Khunou 
##                                                                  967 
##                                                                Chana 
##                                                                  852 
##                                                       Chanam Sandrok 
##                                                                 1270 
##                                                      Chandpur Maning 
##                                                                  777 
##                                   Chandrakhong Ningel, Mayai Keithel 
##                                                                  699 
##                                                          Changamdabi 
##                                                                 4926 
##                                              Changangei Makha Leikai 
##                                                                 1822 
##                                    Changangei Maning (Northern side) 
##                                                                  699 
##                                    Changangei Maning (Southern side) 
##                                                                 1854 
##                                                   Changangei Uchekon 
##                                                                 1860 
##                                         Changmdabi and Kamo Yaithibi 
##                                                                 1892 
##                                                              Chanung 
##                                                                  678 
##                                                        Chaobok Kabui 
##                                                                 1755 
##                                                   Charangpat Maklang 
##                                                                  951 
##                                                    Charangpat Mamang 
##                                                                 1906 
##                                             Charangpat Mamang Leikai 
##                                                                 1113 
##                                   Charangpat Mamang Leikai (Maklang) 
##                                                                 1706 
##                                                             Cherapur 
##                                                                 2116 
##                                        Cherapur (Mushlim And Meitei) 
##                                                                 1947 
##                                                Cheshaba Makha Leikai 
##                                                                  779 
##                                                   Chingangbam Leikai 
##                                                                 2034 
##                                                          Chingdompok 
##                                                                 4332 
##                                                     Chingdong Leikai 
##                                                                  635 
##                                                             Chingkhu 
##                                                                  443 
##                                                             Chingmei 
##                                                                  849 
##                                                            Chingtham 
##                                                                 1025 
##                    Chingtham Leikai (Chingtham Leirak Northern Side) 
##                                                                  673 
##                                Chingtham Leikai Leirak Southern Side 
##                                                                  747 
##                                                       Chongtham Kona 
##                                                                  305 
##                                           Chonthaba Leimakhong Mapal 
##                                                                  473 
##                                             Dholakhal, Jamkham punji 
##                                                                  769 
##                                                               Dibong 
##                                                                 1660 
##                                                  Elangkhangpokpi (B) 
##                                                                 1706 
##                                         Elangkhangpokpi Makha Leikai 
##                                                                  835 
##                                                             Gangapat 
##                                                                 1031 
##                                                   Ghari Awang Leikai 
##                                                                  749 
##                                                   Ghari Makha Leikai 
##                                                                  712 
##                                                             Goyakhal 
##                                                                  613 
##                                                        Hangoipat (B) 
##                                                                 1740 
##                                                     Hangoipat Nepali 
##                                                                  418 
##                                                              Hangoon 
##                                                                 1446 
##                                                Hangoon Mathak Leikai 
##                                                                  817 
##                                                 Hangoon Mayai Leikai 
##                                                                 1740 
##                                                           Haogrampat 
##                                                                  871 
##                                          Haorang Sabal Mamang Leikai 
##                                                                 1024 
##                                                Haoreibi Turel Ahanbi 
##                                                                  778 
##                                                  Haotak Tapha Khunou 
##                                                                  652 
##                                                             Haraorou 
##                                                                  851 
##                                                          Hayel Labuk 
##                                                                 1114 
##                                         Heibong Makhong Makha Leikai 
##                                                                  625 
##                                        Heibong Makhong Mathak Leikai 
##                                                                  637 
##                                           Heibongpokpi Mamang Leikai 
##                                                                 1122 
##                                 Heigrujam Leikai and Thangjam Leikai 
##                                                                  524 
##                                              Heikrujam Mamang Leikai 
##                                                                  776 
##                                              Heikrujam Maning Leikai 
##                                                                  817 
##                                                Heingang Awang Leikai 
##                                                                  602 
##                                    Heingang Awang Leikai Saya Lampak 
##                                                                 1840 
##                                                Heingang Makha Leikai 
##                                                                 1048 
##                                                Heingang Mayai Leikai 
##                                                                  612 
##                                            Heingang Mayai Leikai (A) 
##                                                                  865 
##                                            Heingang Mayai Leikai (B) 
##                                                                  563 
##                                                            Heinoubok 
##                                                                  603 
##                                                     Heinoukhongnembi 
##                                                                 1996 
##                               Heinoukhongnembi Laishram Leikai Awang 
##                                                                  524 
##                               Heinoukhongnembi Laishram Leikai Makha 
##                                                                  507 
##                       Heinoupok Awang, Mamang, Langjing Makha Leikai 
##                                                                  628 
##                                               Heinoupok Makha Leikai 
##                                                                  686 
##                                                   Heirok Heituppokpi 
##                                                                 2797 
##                                                        Heirok Khunou 
##                                                                 2062 
##                                                 Heirok Maning Leikai 
##                                                                 1967 
##                                         Heirok Mayai Leikai Part (2) 
##                                                                  744 
##                                                    Heirok Mayai Part 
##                                                                 2112 
##                                                          Heirok Part 
##                                                                 4527 
##                                            Heirok Part Heirok Khunou 
##                                                                 1106 
##                                                       Heirok Part II 
##                                                                 1944 
##                              Heirok Part, Maning Leikai, Kabo Leikai 
##                                                                 2268 
##                                                 Heisnam Awang Leikai 
##                                                                  959 
##                                                 Heisnam Makha Leikai 
##                                                                  640 
##                                                            Heiyaikon 
##                                                                 1596 
##                                                               Heiyel 
##                                                                  373 
##                                                             Hillghat 
##                                                                 1476 
##             Hillghat Khunou, Gularthal, Kha Khunou And Leingangpokpi 
##                                                                  999 
##                                               Hiyanglam Awang Leikai 
##                                                                  809 
##                                                   Hiyanglam Hiranmei 
##                                                                  640 
##                                                Hiyanglam Laipangamba 
##                                                                  627 
##                                               Hiyanglam Makha Leikai 
##                                                                  693 
##                                           Hiyanglam Mayai Leikai (A) 
##                                                                 1164 
##                                                Hiyanglam Tera Pishak 
##                                                                 1142 
##                                             Hiyanglam Waikhom Leikai 
##                                                                  651 
##                                             Hiyangthang Awang Leikai 
##                                                                  672 
##                                            Hiyangthang Mamang Leikai 
##                                                                 1034 
##                                            Hiyangthang Maning Leikai 
##                                                                  660 
##                                      Hiyangthang Maning Makha Leikai 
##                                                                  735 
##                                           Hiyangthang Tarahei Konjil 
##                                                                  844 
##                                                              Huidrom 
##                                                                  888 
##                                                               Huikap 
##                                                                 2298 
##                                                          Ikou Meitei 
##                                                                  737 
##                                             Iram Siphai Makha Leikai 
##                                                                  968 
##                                              Iramsiphai Awang Leikai 
##                                                                  948 
##                                                Irengbam Awang Mamang 
##                                                                  592 
##                                         Irengbam Awang Maning Leikai 
##                                                                 1348 
##                                   Irengbam Makha Mamang Mayai Leikai 
##                                                                 1286 
##                                         Irengbam Makha Maning Leikai 
##                                                                  408 
##                                               Irengband Turel Mamang 
##                                                                 1173 
##                                           Irom Meijrao Mamang Leikai 
##                                                                  950 
##                                           Irom Meijrao Maning Leikai 
##                                                                 1576 
##                                                       Irong Cheshaba 
##                                                                 1689 
##                                       Irong Meinam and Aribam Leikai 
##                                                                 2138 
##                                                          Irong Umang 
##                                                                  939 
##                                            Ishok Makha Maning Leikai 
##                                                                  708 
##                                                 Ishok Mamang Chingya 
##                                                                  737 
##                                                  Ishok Maning Leikai 
##                                                                 1770 
##                                                            Islamabad 
##                                                                 1420 
##                                                       Itam Sawombung 
##                                                                  643 
##                                                      Ithai Dam Manak 
##                                                                  996 
##                                                  Ithai Mamang Leikai 
##                                                                 1448 
##                        Ithai Wapokpi Maning, Mamang and Mayai Leikai 
##                                                                 1004 
##                                                                Itham 
##                                                                  485 
##                                                        Ithing Mamang 
##                                                                 2256 
##                                                      Jairolpokpi Mar 
##                                                                 1632 
##                                                 Jakuradhor Part-I(A) 
##                                                                 2098 
##                                                   Jakuradhor Part -2 
##                                                                  493 
##                                                            Kachikhul 
##                                                                 1386 
##                                                            Kachimpur 
##                                                                  799 
##                                                            Kadamtala 
##                                                                  870 
##                                                    Kadangband Singda 
##                                                                  837 
##                                                Kairang Mamang Leikai 
##                                                                  997 
##                                          Kairang Muslim Awang Leikai 
##                                                                  513 
##                                         Kairang Muslim Mamang Leikai 
##                                                                 1576 
##                                          Kairang Muslim Mayai Leikai 
##                                                                 1356 
##                                                 Kairang Tera Makhong 
##                                                                  517 
##                                                  Kairembikhok Khunou 
##                                                                 2102 
##                                             Kakwa Laiphrakpam Leikai 
##                                                                 1281 
##                                                  Kakyai Makha Leikai 
##                                                                 1486 
##                                                  Kakyai Mayai Leikai 
##                                                                  536 
##                                               Kalika Lok, Kajinphung 
##                                                                  428 
##                                                               Kameng 
##                                                                 1746 
##                                       Kamong Langoljam Mamang Leikai 
##                                                                  592 
##                                       Kamong Langoljam Maning Leikai 
##                                                                  560 
##                                         Kamong Meisnam Maning Leikai 
##                                                                  802 
##                                          Kamong Meisnam Mayai Leikai 
##                                                                  550 
##                                               Kamong Tongbram Leikai 
##                                                                  577 
##                                                       Kanghuchingjil 
##                                                                  457 
##                                    Kangla Sangomshang (Kabui Khunou) 
##                                                                  784 
##                                                        Kangla Siphai 
##                                                                  615 
##                                               Kanglatombi Hathikhuwa 
##                                                                 1014 
##                                                Kanglatombi Shantipur 
##                                                                 1025 
##                                              Kanglatongbi Bazar Road 
##                                                                 1726 
##                                                  Kanglatongbi Mandir 
##                                                                 1952 
##                                                 Kanglatongbi Tispari 
##                                                                  860 
##                                                          Kangshamram 
##                                                                 2547 
##                                                         Kangyambem-B 
##                                                                  665 
##                                                        Kangyambem -A 
##                                                                 1430 
##                                              Kangyambem (Salungpham) 
##                                                                  929 
##                                                   Kanto Awang Leikai 
##                                                                  758 
##                                                          Kanto Sabal 
##                                                                  821 
##                                                           Karamangga 
##                                                                 1044 
##                                                         Karang Mange 
##                                                                  751 
##                                                        Karang Maning 
##                                                                 1226 
##                                                   Keibi Heikak Mapal 
##                                                                  504 
##                                                        Keibi Khullen 
##                                                                  635 
##                                                     Keibi Taret Khul 
##                                                                  574 
##                                                 Keibul Mathak Leikai 
##                                                                  749 
##                                                  Keibul Mayai Leikai 
##                                                                 1652 
##                                           Keibul Mayai, Makha Leikai 
##                                                                  672 
##                                                         Keikhu Kabui 
##                                                                  456 
##                                          Keikhu Mushlim Makha Leikai 
##                                                                  602 
##                                                 Keikol Mamang Leikai 
##                                                                  976 
##                                  Keinou Thongkha Makha Mamang Leikai 
##                                                                  905 
##                                         Keinou Thongkha Mayai Leikai 
##                                                                  832 
##                                      Keinou Thongkhong Maning Leikai 
##                                                                  998 
##                                        Keinou Thongthak Bazar Maning 
##                                                                 1866 
##                                                               Keirak 
##                                                                 1474 
##                                                Keirak Leirak Achouba 
##                                                                 1286 
##                                                  Keirak Makha Leikai 
##                                                                 1516 
##                                           Keirak Makha Maning Leikai 
##                                                                  802 
##                                                 Keirak Mamang Leikai 
##                                                                 1282 
##                                         Keirao Bitra Awang Chingdong 
##                                                                  992 
##                                                   Keirao Bitra Makha 
##                                                                 1746 
##                                              Keirao Langdum Nongchup 
##                                                                 1792 
##                                               Keirao Langdum Nongpok 
##                                                                  875 
##                                          Keirao Makting Awang Leikai 
##                                                                 1958 
##                                                 Keirao Makting Makha 
##                                                                  968 
##                                                 Keirao Makting Mayai 
##                                                                 2155 
##                    Keirao Wangkhem Laiphrok Maring, Somther Tangkhul 
##                                                                 2022 
##                                                     Keirembi Phoudel 
##                                                                  650 
##                                            Keirenphabi Maning Leikai 
##                                                                 1057 
##                                                         Keithelmanbi 
##                                                                  447 
##                                            Keithelmanbi and Laikhong 
##                                                                  635 
##                                                    Kha-Naorem Leikai 
##                                                                  458 
##                                           Kha Sanjenbam Awang Leikai 
##                                                                  867 
##                                           Kha Sanjenbam Makha Leikai 
##                                                                 1280 
##                                                           Khabeishoi 
##                                                                 3250 
##                                                                Khabi 
##                                                                 1396 
##                                                 Khaidem Awang Leikai 
##                                                                  669 
##                                                       Khaidem Leikai 
##                                                                  427 
##                                               Khaidem Leikai (North) 
##                                                                 1868 
##                                              Khaidem Leikai(South-A) 
##                                                                 1462 
##                                                 Khaidem Makha Leikai 
##                                                                  667 
##                                      Khalakhong Amanbi Maning Leikai 
##                                                                  880 
##                                                             Khamaran 
##                                                                  807 
##                                        Khamnam Leirak Maning Thangba 
##                                                                  889 
##                                        Khangabok Awang Mamang Leikai 
##                                                                 1368 
##                                        Khangabok Awang Maning Leikai 
##                                                                 1174 
##                                           Khangabok Khulakpam Leikai 
##                                                                  887 
##                                          Khangabok Khullakpam Leikai 
##                                                                 1592 
##                                                     Khangabok Khunou 
##                                                                  460 
##                                             Khangabok Maisnam Leikai 
##                                                                 2334 
##                             Khangabok Maisnam Leikai Cherapur Khunou 
##                                                                 1977 
##                                          Khangabok Maning And Mamang 
##                                                                  860 
##                                              Khangabok Maning Leikai 
##                                                                 4073 
##                                               Khangabok Mayai Leikai 
##                                                                 1679 
##                                                            Khannarok 
##                                                                  407 
##                                                             Kharasom 
##                                                                  495 
##                                                              Khekman 
##                                                                 1570 
##                                                        Khekman (B-1) 
##                                                                  565 
##                                                 Khekman Makha Leikai 
##                                                                  608 
##                                                Khekman Mathak Leikai 
##                                                                  588 
##                                      Khellakhong Makha Maning Leikai 
##                                                                  783 
##                                                        Khewa Company 
##                                                                  524 
##                                      Khoijuman Khunou Kwashiphai (B) 
##                                                                 1038 
##                                       Khoijuman Khunou Kwashiphai(A) 
##                                                                  948 
##                                              Khoijuman Mamang Leikai 
##                                                                  654 
##                                              Khoijuman Maning Leikai 
##                                                                 1930 
##                                               Khoijuman Mayai Leikai 
##                                                                  726 
##                                                              Khoirom 
##                                                                 4209 
##                                                             Khomidok 
##                                                                 3602 
##                               Khonghampat Awang Leikai Awang Thangba 
##                                                                  857 
##                                             Khonghampat Mayai Leikai 
##                                                                  973 
##                                                   Khongjom Shivnagar 
##                                                                 1833 
##                                                Khongman Central Wing 
##                                                                  926 
##                                Khongman Mangjil Mamang, Zone-II West 
##                                                                  759 
##                                 Khongman Mayai Leikai Zone-II (East) 
##                                                                  681 
##                                 Khongman Mayai Leikai Zone-IV (East) 
##                                                                  484 
##                                                Khongman Zone-II West 
##                                                                  586 
##                                              Khongman Zone-IV (East) 
##                                                                  641 
##                                               Khongman Zone-V (East) 
##                                                                  583 
##                                     Khongnang Pheidekpi Awang Leikai 
##                                                                  864 
##                                                        Khordak Awang 
##                                                                  972 
##                                                      Khudekpi Mamang 
##                                                                  742 
##                             Khumbong Mamang Leikai and Maning Leikai 
##                                                                  924 
##                                               Khumbong Maning Leikai 
##                                                                  766 
##                                                          Khundrakpam 
##                                                                  814 
##                                             Khundrakpam Awang Leikai 
##                                                                  585 
##                                             Khundrakpam Makha Leikai 
##                                                                 1354 
##                                            Khundrakpam Maning Leikai 
##                                                                  549 
##                                            Khurai Chingangbam Leikai 
##                                                                  993 
##                                              Khurai Khongnangmakhong 
##                                                                 1482 
##                                               Khurai Kongkham Leikai 
##                                                                 2478 
##                                    Khurai Kongpal Chingangbam Leikai 
##                                                                 2801 
##                                                 Khurai Konsam Leikai 
##                                                                 4591 
##                                        Khurai Nandeibam Makha Leikai 
##                                                                  492 
##                                     Khurai Sajor Lairou Pukhri Awang 
##                                                                  625 
##                                                  Khurai Sajor Leikai 
##                                                                 1094 
##                                            Khurai Thoidingjam Leikai 
##                                                                 1052 
##                                                Khurai Thongam Leikai 
##                                                                 1842 
##                                         Khurkhul Awang Mamang Leikai 
##                                                                  614 
##                                         Khurkhul Awang Maning Leikai 
##                                                                  537 
##                                                Khurkhul Makha Leikai 
##                                                                  883 
##                                                Khurkhul Sebok Leikai 
##                                                                  968 
##                                                        Kitana Panung 
##                                                                 1062 
##                                                                Kiyam 
##                                                                 1366 
##                                                Kiyamgei Awang Leikai 
##                                                                  857 
##                                         Kiyamgei Awang Maning Leikai 
##                                                                 2062 
##                                               Kiyamgei Mamang Leikai 
##                                                                 1086 
##                            Kiyamgei Mamang Leikai, Kiyamgei Santipur 
##                                                                  581 
##                                               Kiyamgei Maning Leikai 
##                                                                 1199 
##                                                Kiyamgei Mayai Leikai 
##                                                                  769 
##                                                      Kiyamgei Muslim 
##                                                                  995 
##                                              Kodompokpi Makha Leikai 
##                                                                  650 
##                                             Kodompokpi Mamang Leikai 
##                                                                 1696 
##                                                    Kodompokpi Maning 
##                                                                  591 
##                                              Kodompokpi Mayai Leikai 
##                                                                 1064 
##                                                      Koirengei Bazar 
##                                                                 1242 
##                                              Koirengei Mamang Leikai 
##                                                                  456 
##                                              Komlakhong Awang Leikai 
##                                                                  845 
##                                              Komlakhong Makha Leikai 
##                                                                 1300 
##                                                 Kongba Chanam Leikai 
##                                                                 1348 
##                                       Kongba Laishram Leikai (North) 
##                                                                 1134 
##                                       Kongba Laishram Leikai (South) 
##                                                                  624 
##                                    Kongba Nongthombam Leikai (South) 
##                                                                 1352 
##                                                      Kongkham Leikai 
##                                                                 2032 
##                                                Kongpal Chanam Leikai 
##                                                                  555 
##                                             Kongpal Naoroibam Leikai 
##                                                                  641 
##                                         Kongpal Sajor Leikai (Awang) 
##                                                                  612 
##                                         Kongpal Sajor Leikai (Makha) 
##                                                                  936 
##                                         Konjeng Lamdong Awang Leikai 
##                                                                 1392 
##                                         Konjeng Lamdong Makha Leikai 
##                                                                  870 
##                                    Konjeng Langpoklakpam Leikai East 
##                                                                  567 
##                              Konjeng Langpoklakpam Leikai West South 
##                                                                  712 
##                                                       Konjeng Leikai 
##                                                                  513 
##                                           Konjeng Ningthoujam Leikai 
##                                                                 1524 
##                                          Kontha Ahallup Awang Leikai 
##                                                                  619 
##                                          Kontha Ahallup Makha Leikai 
##                                                                 1014 
##                                                Kontha Khabam Lamkhai 
##                                                                  745 
##                                          Kontha Khabam Mamang Leikai 
##                                                                  749 
##                                          Kontha Khabam Maning Leikai 
##                                                                  451 
##                                           Kontha Khabam Mayai Leikai 
##                                                                  771 
##                                                    Konthoujam Leikai 
##                                                                  996 
##                                      Konthoujam Mamang Leikai Part-1 
##                                                                 1146 
##                                      Konthoujam Mamang Leikai Part-2 
##                                                                  981 
##             Konthoujam Maning Leikai (Northern side of Bamon Leirak) 
##                                                                  515 
##             Konthoujam Maning Leikai (Southern side of Bamon Leirak) 
##                                                                  841 
##                                                  Konuma, Hiyangkhong 
##                                                                  789 
##                                                        Koupak Nepali 
##                                                                 1954 
##                                                              Koutruk 
##                                                                  788 
##                                                      Kshetri Bengoon 
##                                                                 1758 
##                                            Kshetri Bengoon (North-A) 
##                                                                  831 
##                                    Kshetri Bengoon and Yangbi Khunou 
##                                                                  765 
##                                        Kshetrigao (Keikhu Mushlim A) 
##                                                                 1678 
##                                              Kshetrigao Awang Leikai 
##                                                                 3058 
##                                        Kshetrigao Awang Sabal Leikai 
##                                                                 1435 
##                                              Kshetrigao Makha Leikai 
##                                                                 2411 
##                              Kwakeithel Mayaikoibi Chabungbam Leikai 
##                                                                 1126 
##                             Kwakeithel Mayaikoibi Ningthoujam Leikai 
##                                                                  968 
##                                         Kwakeithel Thounaojam Leikai 
##                                                                  392 
##                                                               Kwakta 
##                                                                  510 
##                                                        Kwakta Khuman 
##                                                                 1514 
##                                           Kwakta Khuman Makha Leikai 
##                                                                  779 
##                                                   Kwakta Tampakmayum 
##                                                                  873 
##                                               Kyamgei Khoirom Leikai 
##                                                                  720 
##                                                             Laimanai 
##                                                                  720 
##                                                            Laingoubi 
##                                                                 2098 
##                                          Laipham Khunou Makha Leikai 
##                                                                 1741 
##                                         Laipham Khunou Mamang Leikai 
##                                                                  671 
##                                          Laipham Khunou Mayai Leikai 
##                                                                  893 
##                                               Lairenjam Awang Leikai 
##                                                                 1606 
##                                               Lairenjam Makha Leikai 
##                                                                  836 
##                                                      Lairenjam Sabal 
##                                                                  786 
##                                                           Lairenkabi 
##                                                                 1288 
##                                                          Lairensajik 
##                                                                  528 
##                                    Lairikyengbam Leikai Mayai Leirak 
##                                                                  707 
##                                           Lairikyengbam Makha Leikai 
##                                                                  989 
##                                       Lairikyengbam Mayai Leikai (A) 
##                                                                 1422 
##                                           Lairikyengbam Salan Leirak 
##                                                                 1037 
##                                                      Laishram Leikai 
##                                                                 2170 
##                                                            Lalpani-I 
##                                                                 1768 
##                                                               Lambal 
##                                                                  579 
##                                                           Lamboikhul 
##                                                                 1392 
##                                              Lamjao Awang Leikai (B) 
##                                                                 1168 
##                                                  Lamjao Makha Leikai 
##                                                                  881 
##                                              Lamjao Mayai Leikai (A) 
##                                                                 1428 
##                                               Lamjao Part (1) Tejpur 
##                                                                  666 
##                                                            Lamlongei 
##                                                                 2299 
##                                                            Langathel 
##                                                                 2160 
##                                                  Langathel Mandakini 
##                                                                 2174 
##                                              Langathel Maning Leikai 
##                                                                  627 
##                                               Langathel Mayai Leikai 
##                                                                  584 
##                                                Langjing Awang Leikai 
##                                                                  688 
##                                    Langjing Maning and Mamang Leikai 
##                                                                  813 
##                                            Langmeidong Mamang Leikai 
##                                                                 2042 
##                     Langmeidong Maning Awang Leikai and Mayai Leikai 
##                                                                  794 
##                                            Langmeidong Maning Leikai 
##                                                                 2152 
##                                      Langmeidong Maning Makha Leikai 
##                                                                  620 
##                                            Langmeithet Kwarok Maring 
##                                                                  712 
##                                                Langpok Maning Leikai 
##                                                                  650 
##                                                  Langthabal Chingkha 
##                                                                 1714 
##                                          Langthabal Lep Awang Leikai 
##                                                                  585 
##                                          Langthabal Lep Makha Leikai 
##                                                                 1192 
##                                          Langthabal Lep Mayai Leikai 
##                                                                 1267 
##                                  Langthabal Mantrikhong Awang Leikai 
##                                                                  896 
##                                  Langthabal Mantrikhong Makha Leikai 
##                                                                 1978 
##                     Langthabal Phuramakhong, Heiripok Chingi Chingya 
##                                                                  698 
##                                           Laphupat Tera Awang Leikai 
##                                                                  468 
##                                                 Laphupat Tera Khunou 
##                                                                 1702 
##                                           Laphupat Tera Mayai Leikai 
##                                                                 1280 
##                              Laphupat, Khoidum Part Sekmaijin Khunou 
##                                                                  494 
##                                                           Latingkhal 
##                                                                 1295 
##                                             Leimapokpam Awang Leikai 
##                                                                  980 
##                                   Leimapokpam Khunpham Mamang Leikai 
##                                                                  822 
##                                   Leimapokpam Khunpham Maning Leikai 
##                                                                  709 
##                                             Leimapokpam Mayai Leikai 
##                                                                 2403 
##                                          Leimram Awang Leikai Maning 
##                                                                 1444 
##                                                 Leimram Makha Leikai 
##                                                                  613 
##                                                Leimram Mamang Leikai 
##                                                                  490 
##                                                   Leimram Waroiching 
##                                                                  426 
##                                                          Leirongthel 
##                                                                 1499 
##                                                  Leishabithel Meetei 
##                                                                  799 
##                                                         Leishangthem 
##                                                                 2830 
##                                            Leishangthem Keli Makhong 
##                                                                 1231 
##                              Leishangthem Thong Manung Maning Leikai 
##                                                                 2036 
##                                                           Lemba Khul 
##                                                                  728 
##                                                       Lilando Lampak 
##                                                                 1242 
##                                                           Litanpokpi 
##                                                                  673 
##                                                      Loitang Khullen 
##                                                                 1620 
##                                                       Loitang Khunou 
##                                                                 1964 
##                                                       Loukham Leirak 
##                                                                 1476 
##                                                            Lourembam 
##                                                                 2010 
##                                                   Luker Makha Leikai 
##                                                                  425 
##                                           Luwangsangbam Awang Leikai 
##                                                                  633 
##                                          Luwangsangbam Mamang Leikai 
##                                                                  521 
##                                          Luwangshangbam Mayai Leikai 
##                                                                 2006 
##                                                Maharabi Awang Leikai 
##                                                                  694 
##                                              Maibakhul Mamang Leikai 
##                                                                  564 
##                                                  Maibam Awang Leikai 
##                                                                  720 
##                                          Maibam Konjil Maning Leikai 
##                                                                  655 
##                                           Maibam Konjil Mayai Leikai 
##                                                                  640 
##                                                  Maibam Makha Leikai 
##                                                                 1738 
##                                                  Maibam Mayai Leikai 
##                                                                  605 
##                                                            Mairembam 
##                                                                  847 
##                                                      Makha Pat Awang 
##                                                                  521 
##                                            Makha Pat Khongjin Leikai 
##                                                                  569 
##                                                              Maklang 
##                                                                 3305 
##                                           Malom Tulihal Awang Leikai 
##                                                                  800 
##                                                 Malom Tulihal Maning 
##                                                                  935 
##                                                Malom Tuliyaima Awang 
##                                                                 1742 
##                       Malom Tuliyaima Awang (Laishram Leiraki North) 
##                                                                  713 
##                                         Malom Tuliyaima Makha Leikai 
##                                                                  829 
##                                                               Mantak 
##                                                                  522 
##                                                   Matai Mayai Leikai 
##                                                                  804 
##                                 Mayang Langjing Tamang Makha Thangba 
##                                                                 1986 
##                                  Mayang Langjing Taning Awang Leikai 
##                                                                  509 
##                                  Mayang Langjing Taning Makha Leikai 
##                                                                  598 
##                                                 Meitram Awang Leikai 
##                                                                  629 
##                                                 Meitram Makha Leikai 
##                                                                  595 
##                                                    Moidangpok Khunou 
##                                                                  837 
##                                       Moidangpok Khunou and Shajirok 
##                                                                 1772 
##                                                              Moijing 
##                                                                 6140 
##                                         Moirang Hanuba Mamang Leikai 
##                                                                 1258 
##                                         Moirang Hanuba Maning Leikai 
##                                                                  535 
##                                                        Moirang Kampu 
##                                                                 1898 
##                                            Moirang Khunou Haogrampat 
##                                                                 1095 
##                                                Moirang Khunou Maning 
##                                                                  860 
##                                                         Moirangpurel 
##                                                                 1692 
##                                                 Mongjam Mayai Leikai 
##                                                                 1002 
##                                             Mongshangei Awang Leikai 
##                                                                  592 
##                                             Mongshangei Makha Leikai 
##                                                                  729 
##                                             Mongshangei Mayai Leikai 
##                                                                 1199 
##                                                           Nachou (A) 
##                                                                  849 
##                                                           Nachou (B) 
##                                                                 1534 
##                                                           Nachou (C) 
##                                                                  745 
##                                                           Nachou (D) 
##                                                                 1558 
##                                                              Nagaram 
##                                                                  632 
##                                                              Naharup 
##                                                                 1486 
##                                           Nandeibam Leikai (Central) 
##                                                                  957 
##                                             Nandeibam Leikai (North) 
##                                                                  709 
##                                             Nandeibam Leikai (South) 
##                                                                  860 
##                                              Naodakhong Makha Leikai 
##                                                                 1830 
##                                                  Naorem Awang Leikai 
##                                                                  718 
##                                            Naorem Awang Mayai Leikai 
##                                                                 1394 
##                                                  Naorem Makha Leikai 
##                                                                  682 
##                                     Naoriya Pakhanglakpa Irom Leikai 
##                                                                 1904 
##                            Naoriya Pakhanglakpa Keisham Awang Leikai 
##                                                                 1404 
##                            Naoriya Pakhanglakpa Keisham Mayai Leikai 
##                                                                  690 
##                                Naoriya Pakhanglakpa Lourembam Leikai 
##                                                                 1134 
##                           Naoriya Pakhanglakpa Lourembam Leikai West 
##                                                                  367 
##                             Naoriya Pakhanglakpa Yangam Leirak Makha 
##                                                                  793 
##                                            Naran Konjin Makha Leikai 
##                                                                 1366 
##                                              Naranseina Makha Leikai 
##                                                                 1940 
##                                                           Narayanpur 
##                                                                  356 
##                                                 Nepra Company Leikai 
##                                                                  507 
##                                       Ngaikhong Khullen Awang Leikai 
##                                                                  736 
##                                         Ngaikhong Khullen Kha Leikai 
##                                                                  632 
##                                      Ngaikhong Khullen Mamang Leikai 
##                                                                 1542 
##                                                     Ngaikhong Khunou 
##                                                                 1428 
##                                              Ngaikhong Maning Leikai 
##                                                                  602 
##                                       Ngaikhong Siphai Mamang Leikai 
##                                                                  520 
##                                       Ngaikhong Siphai Maning Leikai 
##                                                                 1314 
##                                             Ngairangbam Awang Leikai 
##                                                                  862 
##                                             Ngairangbam Makha Leikai 
##                                                                 1970 
##                                                       Ngakchroupokpi 
##                                                                 1474 
##                                          Ngangkhalawai Mamang Leikai 
##                                                                 1560 
##                                          Ngangkhalawai Maning Leikai 
##                                                                  715 
##                                                       Nganukon No. 3 
##                                                                 1864 
##                                              Nillakuthi Awang Leikai 
##                                                                 1432 
##                                               Ningombam Awang Leikai 
##                                                                 1003 
##                                               Ningombam Makha Leikai 
##                                                                  863 
##                                      Ningomthong Kitna Panung (West) 
##                                                                  775 
##                                                         Ningthoubung 
##                                                                  807 
##                                                  Ningthoubung Khunou 
##                                                                 1580 
##                                Ningthoukhong Awang Khunou Ward No. 1 
##                                                                  984 
##                                      Ningthoukhong Awang Ward No. 14 
##                                                                  860 
##                                             Ningthouta Chandon Pokpi 
##                                                                  986 
##                                                 Nongada Awang Leikai 
##                                                                  443 
##                                                 Nongada Makha Leikai 
##                                                                  750 
##                                                Nongdam Mamang Leikai 
##                                                                  553 
##                                                   Nongmaikhong Awang 
##                                                                  673 
##                                            Nongmaikhong Awang Leikai 
##                                                                 1674 
##                              Nongpok Sekmai Khunbi And Toubul Khunou 
##                                                                 1123 
##                                                              Nongren 
##                                                                 2374 
##                                                            Nungbrang 
##                                                                  826 
##                                                           Nungei (A) 
##                                                                  653 
##                                                           Nungei (B) 
##                                                                 1174 
##                                                  Nungoi Makha Leikai 
##                                                                 1696 
##                                                             Nungphou 
##                                                                  571 
##                                                        Nungukhongyam 
##                                                                  574 
##                                                         Oinam Leikai 
##                                                                 1690 
##                                                Oinam Sawombung Awang 
##                                                                  865 
##                                         Oinam Sawombung Makha Leikai 
##                                                                  538 
##                                                     Oinam Shawombung 
##                                                                 1720 
##                       Oinam Thingel Khongnang Pheidekpi Makha Leikai 
##                                                                 1370 
##                                                 Oksu Ningthemchakhul 
##                                                                  589 
##                                                         Pallel Bazar 
##                                                                  630 
##                                            Pallel Leimangai Chingjin 
##                                                                  449 
##                                                 Pallel Mamang Leikai 
##                                                                 1072 
##                                                  Pallel Mayai Leikai 
##                                                                 1450 
##                                                           Pangaltabi 
##                                                                 2479 
##                                                    Pangei Meiteikhul 
##                                                                 1720 
##                                                      Pangei Yangdong 
##                                                                 2826 
##                                                            Pantilong 
##                                                                  742 
##                                                   Papal Mamang Ching 
##                                                                  834 
##                                                  Papal Maning Leikai 
##                                                                 1624 
##                                                        Patsoi Part-I 
##                                                                 1056 
##                                                       Patsoi Part-II 
##                                                                  584 
##                                          Patsoi Part-II Awang Leikai 
##                                                                  647 
##                                                      Patsoi Part-III 
##                                                                  812 
##                                                       Patsoi Part-IV 
##                                                                 1043 
##                                                             Phaknung 
##                                                                  926 
##                                               Phanjangkhong Kakmayai 
##                                                                  926 
##                                                       Phayeng Khunou 
##                                                                 1146 
##                                                 Phayeng Makha Leikai 
##                                                                  756 
##                                                 Phayeng Mayai Leikai 
##                                                                  637 
##                                                 Phayeng Sabal Leikai 
##                                                                  374 
##                                   Phayeng, Kharang Nongpok and Sabal 
##                                                                 1352 
##                                                              Phoudel 
##                                                                 2627 
##                                             Phougakchao Awang Leikai 
##                                                                 1069 
##                                       Phougakchao Ikhai Awang Leikai 
##                                                                  840 
##                                      Phougakchao Ikhai Maning Leikai 
##                                                                  697 
##                                             Phougakchao Makha Leikai 
##                                                                 1116 
##                                          Phubala Awang Mamang Leikai 
##                                                                 1550 
##                                          Phubala Makha Mamang Leikai 
##                                                                  807 
##                                                Phumlou Mamang Leikai 
##                                                                 1522 
##                                                       Phumlou Siphai 
##                                                                  753 
##                                                        Phunal Maring 
##                                                                 1682 
##                                                             Phundrei 
##                                                                  957 
##                                                Phundrei Awang Leikai 
##                                                                 1260 
##                                                      Poirou Khongjil 
##                                                                 2245 
##                                            Porompat (Kshetri Leikai) 
##                                                                 1350 
##                                                      Porompat Muslim 
##                                                                  926 
##                                                Porompat Mutum Leikai 
##                                                                  803 
##                                                          Potshangbam 
##                                                                 1850 
##                                                      Potshangbam (B) 
##                                                                 1928 
##                                                              Pourabi 
##                                                                  776 
##                                                        Pukhao Khabam 
##                                                                 1142 
##                                                       Pukhao Laipham 
##                                                                  940 
##                                                       Pukhao Naharup 
##                                                                 1104 
##                                                       Pukhao Terapur 
##                                                                 1162 
##                                                    Pukhrambam Mamang 
##                                                                  569 
##                                                    Pukhrambam Maning 
##                                                                 1444 
##                                      Pungdongbam Awang Mamang Leikai 
##                                                                 1120 
##                                      Pungdongbam Awang Maning Leikai 
##                                                                  660 
##                                             Pungdongbam Makha Leikai 
##                                                                  679 
##                               Purna Heituppokpi Wangjing Sorokhaibam 
##                                                                  928 
##                        Purna Heituppokpi Wangjing Sorokhaibam Leikai 
##                                                                 1932 
##                                                             Rasidpur 
##                                                                  448 
##                                                   Sabungkhok Khunjao 
##                                                                 1936 
##                                                      Sadokpam Leikai 
##                                                                  878 
##                              Sagolband Sapam Leirak Mamang and Makha 
##                                                                  827 
##                                Sagolband Sapam Leirak Maning Thangba 
##                                                                 1454 
##                                         Sagolband Tera Lukram Leirak 
##                                                                 1270 
##                            Sagolband Tera Lukram Leirak Awang Leikai 
##                                                                  531 
##                            Sagolband Tera Lukram Leirak Mayai Leikai 
##                                                                 1176 
##                                       Sagolband Tera Tongbram Leikai 
##                                                                  969 
##                                             Sagoltongba Awang Leikai 
##                                                                  949 
##                                             Sagoltongba Makha Leikai 
##                                                                  925 
##                                                               Sagram 
##                                                                 1001 
##                                                  Saiton Awang Leikai 
##                                                                 1476 
##                                                                Sajeb 
##                                                                 2027 
##                                                         Sajor Leikai 
##                                                                 1578 
##                                                  Salam Mamang Leikai 
##                                                                 1188 
##                                                  Salam Maning Leikai 
##                                                                 1452 
##                                            Salungpham (Kangthokchao) 
##                                                                 1051 
##                                              Salungpham Kangthokchao 
##                                                                 1214 
##                                                 Samaram Mayai Leikai 
##                                                                 1470 
##                                                Samusang Mutum Yangbi 
##                                                                  224 
##                                                   Samusang Shantipur 
##                                                                  654 
##                                                         Sandangsenba 
##                                                                  677 
##                                             Sangaiprou Mamang Leikai 
##                                                                 1966 
##                                                Sangaiprou Paite Veng 
##                                                                  650 
##                                                           Sangaithel 
##                                                                  698 
##                                                        Sangaiyumpham 
##                                                                 4580 
##                                           Sangaiyumpham Awang Leikai 
##                                                                 1226 
##                                          Sangaiyumpham Mamang Leikai 
##                                                                 1366 
##                                                          Sangomshang 
##                                                                  572 
##                                                            Sanjenbam 
##                                                                 1031 
##                                                    Sanjenbam Khullen 
##                                                                 1298 
##                                                     Sanjenbam Khunou 
##                                                                 1554 
##                                                 Santhel Awang Leikai 
##                                                                 1019 
##                                                 Santhel Makha Leikai 
##                                                                 2182 
##                                                       Santhong Awang 
##                                                                  654 
##                                                                Sapam 
##                                                                 3586 
##                         Sapam Leirak Nongmaithem Awang Maning Laikai 
##                                                                  462 
##                               Sapam Leirak Nongmaithem Mamang Leikai 
##                                                                  731 
##                                                            Sawombung 
##                                                                 1784 
##                                              Sawombung Kabui Khunjao 
##                                                                  686 
##                                              Sawombung Maning Leikai 
##                                                                  627 
##                                                 Seijang Awang Leikai 
##                                                                  674 
##                                                 Seijang Makha Leikai 
##                                                                  615 
##                                                            Sekmaijin 
##                                                                 3430 
##                                                     Sekmaijin Khunou 
##                                                                 2680 
##                                                    Sekmaijin Thongam 
##                                                                 1464 
##                                                   Sekta Awang Leikai 
##                                                                  858 
##                                                   Sekta Makha Leikai 
##                                                                  550 
##                                                   Sekta Mayai Leikai 
##                                                                  490 
##                                                       Senjam Chirang 
##                                                                  595 
##                                                        Senjam Khunou 
##                                                                 1262 
##                                   Serou Part (1) Mayai, Makha Leikai 
##                                                                 1556 
##                              Serou Part (1) Serou Awang Leikai Bazar 
##                                                                 2124 
##                                                       Serou Part (2) 
##                                                                 1759 
##                                              Shagolmang Makha Leikai 
##                                                                  493 
##                                                              Shambei 
##                                                                  864 
##                                                           Sharouthel 
##                                                                  489 
##                                                             Shikhong 
##                                                                 1465 
##                                                      Shikhong Khunou 
##                                                                 2406 
##                                                               Shinga 
##                                                                 2758 
##                                                                Sinam 
##                                                                  767 
##                                                       Sonapur-Part-I 
##                                                                  708 
##                                                      Sonapur-Part-II 
##                                                                 1246 
##                                               Sora (A) Maning Leikai 
##                                                                 1640 
##                                               Sora (B) Maning Leikai 
##                                                                  722 
##                                       Sora Awang Ching Wangma Leikai 
##                                                                  681 
##                                        Sora Mamang Thongthabi Leikai 
##                                                                 1554 
##                                       Sora Mayai Langjeihoubi Leikai 
##                                                                  898 
##                                                    Sora Mayai Leikai 
##                                                                 1744 
##                                             Sorokhaibam Leikai Awang 
##                                                                  486 
##                                             Sorokhaibam Leikai Makha 
##                                                                 1156 
##                       Soyam Leirak and Khamnam Leirak Mamang Thangba 
##                                                                 1630 
##                                              Sunusiphai Awang Leikai 
##                                                                  704 
##                                              Sunusiphai Mayai Leikai 
##                                                                  818 
##                                                          Tairenpokpi 
##                                                                 1188 
##                                                  Takhel Makha Leikai 
##                                                                 1088 
##                                                 Takhel Mamang Leikai 
##                                                                  546 
##                                                   Takhelambam Konjil 
##                                                                  405 
##                                                         Takhok Makha 
##                                                                  872 
##                                                         Takhok Mapal 
##                                                                 1189 
##                                                      Takyel Khongbal 
##                                                                 1626 
##                                               Takyel Khongbal Mamang 
##                                                                  600 
##                                               Takyel Khongbal Maning 
##                                                                 1626 
##                                    Takyel Khongbal Pongshubam Leikai 
##                                                                 1512 
##                                 Takyel Kolom Mamang and Makha Leikai 
##                                                                  582 
##                                           Takyel Kolom Maning Leikai 
##                                                                  665 
##                                              Tangjeng Chingya Leikai 
##                                                                  749 
##                      Tangjeng Khunjao, Mangjin Khongyam Makha Leikai 
##                                                                 1196 
##                                                             Tangkham 
##                                                                  890 
##                                                      Tangkhul Avenue 
##                                                                  840 
##                                             Taobungkhok Makha Leikai 
##                                                                  787 
##                                   Taobungkhok Mayai and Makha Leikai 
##                                                                  552 
##                                             Taobungkhok Mayai Leikai 
##                                                                 1796 
##                                                              Tekcham 
##                                                                 1805 
##                                                Tekcham Mamang Leikai 
##                                                                 1114 
##                                                 Tekcham Sabal Leikai 
##                                                                  677 
##                                                               Tellou 
##                                                                  721 
##                                                           Tendongyan 
##                                                                 1006 
##                                                         Tentha Makha 
##                                                                 4887 
##                                                  Tentha Makha Leikai 
##                                                                 4681 
##                                         Tera Loukrakpam Leikai Awang 
##                                                                  834 
##                                         Tera Loukrakpam Leikai Mayai 
##                                                                  801 
##                                                            Terakhong 
##                                                                  661 
##                                                Terakhongsangbi Bazar 
##                                                                 1542 
##                                  Thambalkhong Kongba Laishram Leikai 
##                                                                  994 
##                                                   Thambalkhong North 
##                                                                 1074 
##                                            Thambalkhong Sabal Leikai 
##                                                                 1836 
##                                                          Thamnapokpi 
##                                                                  607 
##                                            Thamnapokpi Mamang Leikai 
##                                                                 1523 
##                                              Thanga Chingkha Haoreng 
##                                                                  622 
##                                              Thanga Chingkha Khomlai 
##                                                                 1202 
##                                                Thanga Khunjem Leikai 
##                                                                 2321 
##                                        Thanga Moirangthem Leikai (B) 
##                                                                 1364 
##                                                  Thanga Oinam Leikai 
##                                                                 1099 
##                                                   Thanga Salam Heiga 
##                                                                  731 
##                                                 Thanga Salam Mangkha 
##                                                                  695 
##                                                      Thanga Shamukon 
##                                                                 1128 
##                                                          Thangalawai 
##                                                                 1588 
##                                                   Thangalawai Mamang 
##                                                                  931 
##                                             Thangbijrou Awang Leikai 
##                                                                  571 
##                                             Thangbijrou Makha Leikai 
##                                                                  561 
##                                                      Thangjam Khunou 
##                                                                  626 
##                                              Tharoijam Mamang Leikai 
##                                                                  871 
##                                                   Thawanthaba Leikai 
##                                                                  947 
##                                                              Thayong 
##                                                                  925 
##                                                       Thingom Leikai 
##                                                                  769 
##                                                        Thinungei (A) 
##                                                                 1394 
##                                                        Thinungei (B) 
##                                                                 1428 
##                                                      Thinungei (C-1) 
##                                                                  701 
##                                                      Thinungei (C-2) 
##                                                                  709 
##                                                  Thiyam Konjin Awang 
##                                                                  732 
##                                                  Thiyam Konjin Makha 
##                                                                 1626 
##                                                 Thiyam Mamang Leikai 
##                                                                  505 
##                                                  Thiyam Mayai Leikai 
##                                                                 1096 
##                                                             Thokchom 
##                                                                  536 
##                                                              Thongam 
##                                                                 1846 
##                                                Thongjao Awang Leikai 
##                                                                  690 
##                                                Thongjao Makha Leikai 
##                                                                 1428 
##                             Thongju Kakwa Lamdaibung Laishram Leikai 
##                                                                 1050 
##                                                       Thongju Koirou 
##                                                                  858 
##                                           Thongju Nameirakpam Leikai 
##                                                                  698 
##                                                Thongju Naorem Leikai 
##                                                                 2474 
##                                                  Thongju Ningomthong 
##                                                                 1500 
##                                               Thongju Part-II Koirou 
##                                                                  822 
##                                                Thongju Pheijaleitong 
##                                                                 2424 
##                                                 Thoudam And Thokchom 
##                                                                  733 
##                                               Thoudam Irong Thokchom 
##                                                                  832 
##                                                           Thounaojam 
##                                                                  833 
##                                                           Tiger Camp 
##                                                                  517 
##                                                        Tilka Company 
##                                                                  608 
## Tingri, Tingri Chanbirok, Tingri Nungpakthabi, Tingri Chirik Leitong 
##                                                                  288 
##                                              Tokpaching Chandonpokpi 
##                                                                 1856 
##                           Tokpaching, Lairok Munushoi, Sharik Konjil 
##                                                                  502 
##                                                         Top Chingtha 
##                                                                 6364 
##                                            Top Dushra Imphal (North) 
##                                                                  759 
##                                            Top Dushra Imphal (South) 
##                                                                  699 
##                                            Top Dushra Khabam (North) 
##                                                                  925 
##                                            Top Dushra Khabam (South) 
##                                                                 1048 
##                                        Torban (Kshetri Leikai North) 
##                                                                  946 
##                                        Torban (Kshetri Leikai South) 
##                                                                 1001 
##                                  Torban Pebiya Pandit Leikai (North) 
##                                                                  555 
##                                  Torban Pebiya Pandit Leikai (South) 
##                                                                 1461 
##                                                        Torbung Sabal 
##                                                                 1104 
##                                                  Toubul Awang Leikai 
##                                                                 1498 
##                                           Toubul Awang Mamang Leikai 
##                                                                 2448 
##                                                  Toubul Makha Maning 
##                                                                 1336 
##                                                 Toubul Maning Leikai 
##                                                                 1412 
##                                                             Toupokpi 
##                                                                  873 
##                                              Tronglaobi Awang Leikai 
##                                                                 1152 
##                                              Tronglaobi Makha Leikai 
##                                                                  846 
##                                                Tuisolien Kaiya Punji 
##                                                                  731 
##                                                              Tulihal 
##                                                                 3963 
##                                                            Tumukhong 
##                                                                  492 
##                                                             Uchathol 
##                                                                 1426 
##                                               Uchekon Khunou (North) 
##                                                                  586 
##                                               Uchekon Khunou (South) 
##                                                                  587 
##                                Uchekon Kongba Kshetri Leikai (North) 
##                                                                 1338 
##                                Uchekon Kongba Kshetri Leikai (South) 
##                                                                 1336 
##                                                   Uchekon Torban (B) 
##                                                                  638 
##                                                  Uchiwa Awang Leikai 
##                                                                  607 
##                                Uchiwa Makha Leikai and Mamang Leikai 
##                                                                  779 
##                               Uchiwa Mayai Leikai and Leirak Achouba 
##                                                                  721 
##                                          Uchiwa Nashtao Makha Leikai 
##                                                                 1128 
##                                                        Uchiwa Nastao 
##                                                                  436 
##                                                       Uchiwa Wangbal 
##                                                                  691 
##                                                        Uchiwa Wangma 
##                                                                  799 
##                                                          Ukhongshang 
##                                                                 3029 
##                                                               Upokpi 
##                                                                  726 
##                                                                 Urup 
##                                                                 1750 
##                                                          Urup Meitei 
##                                                                  802 
##                                                          Urup Muslim 
##                                                                  671 
##                                                          Urup Naokal 
##                                                                 1589 
##                                                         Utlou Mamang 
##                                                                  757 
##                                             Utlou Mayai Awang Leikai 
##                                                                 1360 
##                                                   Utlou Mayai Leikai 
##                                                                  642 
##                                                   Utlou Turel Wangma 
##                                                                  683 
##                                                                 Uyal 
##                                                                 2692 
##                                                Uyumpok Mamang Leikai 
##                                                                  965 
##                                                Uyumpok Maning Leikai 
##                                                                 1086 
##                                              Vijayanagar Kanglatombi 
##                                                                 1092 
##                                                              Wabagai 
##                                                                 3537 
##                                                      Wabagai Kadajit 
##                                                                 1752 
##                                              Wabgai Mairembam Leikai 
##                                                                  674 
##                                                     Wabgai Tera Urak 
##                                                                  599 
##                                          Waheng Khuman Mamang Leikai 
##                                                                  648 
##                                          Waheng Khuman Maning Leikai 
##                                                                 1506 
##                                                       Waikhom Leikai 
##                                                                  541 
##                                                Waikhong Awang Leikai 
##                                                                  638 
##                                                Waikhong Makha Leikai 
##                                                                  575 
##                                               Waikhong Ningthoumanai 
##                                                                  950 
##                                                                Wairi 
##                                                                  354 
##                                                        Waithou Chiru 
##                                                                 1138 
##                                                 Waiton Maning Leikai 
##                                                                 1602 
##                                                  Waiton Mayai Leikai 
##                                                                 1208 
##                                                     Wakching Khullen 
##                                                                  948 
##                                                              Wakhong 
##                                                                  342 
##                                                              Wangbal 
##                                                                 1299 
##                                            Wangkhei Loumanbi (North) 
##                                                                 1180 
##                                            Wangkhei Loumanbi (South) 
##                                                                  700 
##                                                      Wangkhem Konjin 
##                                                                 2683 
##                                                           Wangoo (A) 
##                                                                  880 
##                                                         Wangoo (B-1) 
##                                                                 2222 
##                                                       Wangoo Chithek 
##                                                                  742 
##                                                  Wangoo Makha Leikai 
##                                                                  653 
##                                            Wangoo Sabal Makha Leikai 
##                                                                  930 
##                                             Wangoo Selungkhong Awang 
##                                                                  867 
##                                                        Wangoo Shabal 
##                                                                 1055 
##                                              Wangoo Shantipur Leikai 
##                                                                  730 
##                                             Wangoo Tera Hodam Leirak 
##                                                                  637 
##                                               Wangoo Terakhong Awang 
##                                                                 1230 
##                                             Wangoo Terakhong Makhong 
##                                                                  592 
##                                        Wangu Terakhong Maning Leikai 
##                                                                  822 
##                                    Wareppam Leikai and Naorem Leikai 
##                                                                  661 
##                                                              Warukok 
##                                                                 1180 
##                                                           Wathalambi 
##                                                                 1174 
##                                           Yaingangpokpi Awang Leikai 
##                                                                  982 
##                                                               Yambem 
##                                                                 4190 
##                                          Yangbi Leikai Litan Makhong 
##                                                                 1364 
##                                                             Yangdong 
##                                                                  438 
##                                                      Yengkhom Leirak 
##                                                                 1614 
##                                 Yengkhom Leirak and Ramji Kabui Khul 
##                                                                  910 
##                                               Yourbung Maning Leikai 
##                                                                 1460 
##                                                Yourbung Mayai Leikai 
##                                                                  603 
##                                    Yumnam Khunou and Wangkhei khunou 
##                                                                 1021 
##                                           Yumnam Patlou Makha Leikai 
##                                                                 1176 
##                 Yurembam Awang Leikai (Northern side of Power House) 
##                                                                 1290 
##                 Yurembam Awang Leikai (Southern side of Power House) 
##                                                                  874 
##                                                Yurembam Makha Leikai 
##                                                                  653 
##                                               Yurembam Maning Leikai 
##                                                                  477
```
