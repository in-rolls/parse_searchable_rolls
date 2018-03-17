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
## Warning: 488 parsing failures.
## row # A tibble: 5 x 5 col      row col      expected               actual file          expected    <int> <chr>    <chr>                  <chr>  <chr>         actual 1 587033 pin_code no trailing characters ৪    'manipur.csv' file 2 587034 pin_code no trailing characters ৪    'manipur.csv' row 3 587035 pin_code no trailing characters ৪    'manipur.csv' col 4 587036 pin_code no trailing characters ৪    'manipur.csv' expected 5 587037 pin_code no trailing characters ৪    'manipur.csv'
## ... ................. ... ............................................................. ........ ............................................................. ...... ............................................................. .... ............................................................. ... ............................................................. ... ............................................................. ........ .............................................................
## See problems(...) for more details.
```

Number of rows:


```r
nrow(manipur)
```

```
## [1] 1906610
```

Unique Values in Sex:


```r
# Unique values in sex
table(manipur$sex)
```

```
## 
## Female   Male 
## 976137 930473
```

Summary of Age:


```r
# Age
summary(manipur$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##   18.00   29.00   39.00   41.79   52.00  118.00      13
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
## 1906596
```

Number of characters in pin code:


```r
table(nchar(manipur$pin_code))
```

```
## 
##       6 
## 1906122
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
## [1] 1906610
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
## [1] 1906610
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(manipur$elector_name))
```

```
## 
##      1      2      3      4      5      6      7      8      9     10 
##      1     58   2582  24234  52128  75162  68641  74553 100828 108602 
##     11     12     13     14     15     16     17     18     19     20 
## 125394 118038 111835 110265 108528 110573 114750 111850  95276  82713 
##     21     22     23     24     25     26     27     28     29     30 
##  70970  58716  51519  40127  29441  21652  14929   9959   6073   3456 
##     31     32     33     34     35     36     37     38 
##   1910    986    481    243     89     32     12      4
```

```r
manipur[which(nchar(manipur$elector_name) < 4), "filename"]
```

```
## # A tibble: 2,641 x 1
##    filename    
##    <chr>       
##  1 A0520029.pdf
##  2 A0580030.pdf
##  3 A0470026.pdf
##  4 A0470026.pdf
##  5 A0470026.pdf
##  6 A0470026.pdf
##  7 A0470026.pdf
##  8 A0470026.pdf
##  9 A0470026.pdf
## 10 A0470026.pdf
## # ... with 2,631 more rows
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
##                                             915904 
##  2 - Outer Manipur Parliamentary Constituency (ST) 
##                                             990706
```

```r
table(manipur$ac_name)
```

```
## 
##          1 - Khundrakpam (GEN)              10 - Uripok (GEN) 
##                          25350                          23686 
##           11 - Sagolband (GEN)         12 - Keisamthong (GEN) 
##                          23028                          26448 
##           13 - Singjamei (GEN)             14 - Yaiskul (GEN) 
##                          19863                          25356 
##            15 - Wangkhei (GEN)               16 - Sekmai (SC) 
##                          34811                          26967 
##             17 - Lamsang (GEN)          18 - Konthoujam (GEN) 
##                          30251                          27889 
##              19 - Patsoi (GEN)             2 - Heingang (GEN) 
##                          34826                          30271 
##          20 - Langthabal (GEN) 21 - Naoria Pakhanglakpa (GEN) 
##                          26977                          32625 
##              22 - Wangoi (GEN)       23 - Mayang Imphal (GEN) 
##                          27126                          28920 
##              24 - Nambol (GEN)               25 - Oinam (GEN) 
##                          31001                          26383 
##           26 - Bishenpur (GEN)             27 - Moirang (GEN) 
##                          29514                          35298 
##              28 - Thanga (GEN)               29 - Kumbi (GEN) 
##                          20928                          26147 
##               3 - Khurai (GEN)              30 - Lilong (GEN) 
##                          30790                          31389 
##             31 - Thoubal (GEN)            32 - Wangkhem (GEN) 
##                          30143                          31287 
##              33 - Heirok (GEN)     34 - Wangjing Tentha (GEN) 
##                          30655                          32146 
##           35 - Khangabok (GEN)              36 - Wabgai (GEN) 
##                          35140                          29637 
##            37 - Kakching (GEN)           38 - Hiyanglam (GEN) 
##                          27760                          26533 
##               39 - Sugnu (GEN)           4 - Kshetrigao (GEN) 
##                          26609                          33174 
##             40 - Jiribam (GEN)              41 - Chandel (ST) 
##                          28204                          46240 
##           42 - Tengnoupal (ST)             43 - Phungyar (ST) 
##                          46146                          30034 
##               44 - Ukhrul (ST)              45 - Chingai (ST) 
##                          41446                          40983 
##               46 - Saikul (ST)               47 - Karong (ST) 
##                          35911                          52370 
##                  48 - Mao (ST)               49 - Tadubi (ST) 
##                          53666                          46443 
##              5 - Thongju (GEN)           50 - Kangpokpi (GEN) 
##                          29323                          29929 
##                51 - Saitu (ST)                52 - Tamei (ST) 
##                          42033                          36786 
##           53 - Tamenglong (ST)               54 - Nungba (ST) 
##                          31993                          25374 
##            55 - Tipaimukh (ST)              56 - Thanlon (ST) 
##                          17794                          17938 
##              57 - Henglep (ST)        58 - Churachandpur (ST) 
##                          29126                          53397 
##               59 - Saikot (ST)               6 - Keirao (GEN) 
##                          50178                          27688 
##              60 - Singhat (ST)                7 - Andro (GEN) 
##                          26235                          32970 
##               8 - Lamlai (GEN)         9 - Thangmeiband (GEN) 
##                          27096                          28379
```

```r
table(manipur$police_station)
```

```
## 
##           444           919     Bishnupur      Heingang      Irilbung 
##           444           919         12787         47506         33058 
##       Jiribam      Kakching         Kumbi        Lamlai       Lamphel 
##         23172         45066         13120         40967         28723 
##       Lamsang        Lilong Mayang Imphal       Moirang        Nambol 
##         14308          7366         26676         41473         45932 
##        Patsoi      Porompat        Sekmai     Singjamei        Sugnoo 
##         29503         50056         21924         76204         14311 
##       Thoubal      Waikhong        Wangoi      Yairipok 
##         80044         17256          6715         57862
```

```r
table(manipur$mandal)
```

```
## 
##         Bishnupur      Bungte Chiru      Chakpikarong           Chandel 
##             29514              5367             15858             33708 
##           Chingai     Churachandpur         Gamphazol          Haochong 
##             13093            126097              1029             11166 
##           Henglep           Jessami           Jiribam          Kakching 
##              5376              8154             28204            110539 
##           KAMJONG  Kangchup Geljang         Kangpokpi     Kasom Khullen 
##              9746             12321             45514              8386 
##            Keirao           Khoupum           Lamphel           Lamsang 
##             60658              9384            127099             57218 
##            Lilong Longchong Maiphai Longchong Meiphai    Longmai(Noney) 
##             31389               668               595              7737 
## Lungchong Meiphai             Machi         Mao Maram           Moirang 
##             15393             16719             72474             81454 
##            Nambol            Nungba            Patsoi          Phungyar 
##             56940              8253             62715             11902 
##          Porompat             Purul            Saikul   Saitu Gamphazol 
##            116969             68912             38143             16592 
##         Sawombung           Singhat             Tamei        Tamenglong 
##            113507             24779             18077             20827 
##        Tengnoupal           Thanlon           Thoubal         Tipaimukh 
##             26101             17938            159371             17794 
##            Tousem            Ukhrul            Wangoi 
##             18709             44526            115648
```

```r
table(manipur$district)
```

```
## 
##      Bishnupur        Chandel  Churachandpur    Imphal East    Imphal West 
##         169271          46240         194668         319338         362680 
##        Kamjong      Kangpokpi Longmai(Noney)          Noney       Senapati 
##          30034         107873          25374          11166         152479 
##     Tamenglong     Tengnoupal        Thoubal         Ukhrul 
##          57613          46146         301299          82429
```

```r
table(manipur$main_town)
```

```
## 
##                                              Achanbigei Awang Leikai 
##                                                                  528 
##                                              Achanbigei Mayai Leikai 
##                                                                  740 
##                                                Achanbigei Thongkhong 
##                                                                  452 
##                                                        Aenol Village 
##                                                                  402 
##                                                              Aglapur 
##                                                                  505 
##                                                    Ahemadabad Part-I 
##                                                                  943 
##                                                 Ahongshangbam Leikai 
##                                                                  849 
##                                                         Aison Nepali 
##                                                                  501 
##                                                                Akham 
##                                                                  916 
##                               Andro Champra Awang Leikai (Ward No 5) 
##                                                                  621 
##                                Andro Ward No-10 and Andro Torongthel 
##                                                                  658 
##                                     Andro ward No-10(Part) 11 and 12 
##                                                                  813 
##                                                      Andro Ward No-7 
##                                                                  683 
##                                                      Andro Ward No-8 
##                                                                  781 
##                                          Andro Ward No 1 Loupeiochum 
##                                                                  823 
##                                     Andro Ward No 2 Chingdong Leikai 
##                                                                  574 
##                                        Andro Ward No 3 Khuman Leikai 
##                                                                  649 
##                                        Andro Ward No 4 Mamang Leikai 
##                                                                  539 
##                                               Andro Ward No. 6 and 9 
##                                                                  848 
##                                                         Angom Leikai 
##                                                                  819 
##                                                               Angtha 
##                                                                 1937 
##                                                        Arapti Maning 
##                                                                 1248 
##                                                       Arapti Nongpok 
##                                                                 1593 
##                                                        Arong Khunjao 
##                                                                  626 
##                                                         Arong Khunou 
##                                                                  782 
##                                                         Ashem Leikai 
##                                                                  543 
##                                                          Atongkhuman 
##                                                                  423 
##                                                Atoukhong Laiphrakpam 
##                                                                 1707 
##                                             Awang Jiri Mamang Leikai 
##                                                                  528 
##                                             Awang Jiri Maning Leikai 
##                                                                  506 
##                            Awang Khunou Mamang Leikai Mamang Thangba 
##                                                                 1026 
##                                            Awang Khunou Sorok Maning 
##                                                                 1001 
##                                       Awang Leikinthabi Awang Leikai 
##                                                                  605 
##                                       Awang Leikinthabi Makha Leikai 
##                                                                  566 
##                                 Awang Potsangbam Khunou Awang Leikai 
##                                                                  616 
##                                 Awang Potsangbam Khunou Makha Leikai 
##                                                                  408 
##                               Awang Potshangbam Khullen Awang Leikai 
##                                                                  706 
##                                          Awang Potshangbam Thouriphi 
##                                                                  609 
##                                                        Awang Wabagai 
##                                                                  511 
##                                                             Babukhal 
##                                                                  153 
##                                                      Baiboni Bengali 
##                                                                  558 
##                                                               Bakhal 
##                                                                  800 
##                                                 Bamdiar Awang Leikai 
##                                                                  588 
##                                                 Bamdiar Makha Leikai 
##                                                                  534 
##                                                          Bamon Kampu 
##                                                                 1334 
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
##                                                                  522 
##                                            Bashikhong, Kitana Panung 
##                                                                  526 
##                                                                Bengi 
##                                                                 1221 
##                                                          Bhoumikpara 
##                                                                  838 
##                                                  Bhutangkhal Bengali 
##                                                                  777 
##                                               Bijaypur Maning Leikai 
##                                                                  241 
##                                                           Bishnunaha 
##                                                                 2395 
##                                              Borayangbi Awang Leikai 
##                                                                 1071 
##                                                  Borayangbi Thongkha 
##                                                                  936 
##                                                            Borobekra 
##                                                                  869 
##                                                            Boroikhal 
##                                                                   63 
##                               Buya Salam Mathak, Ahanbi Salam Mathak 
##                                                                  674 
##                                                              Chairel 
##                                                                  647 
##                                                          Chairel (A) 
##                                                                  785 
##                         Chajing Khunou, Khorshantabi Tangjeng Khunou 
##                                                                  967 
##                                                                Chana 
##                                                                  426 
##                                                       Chanam Sandrok 
##                                                                 1270 
##                                                      Chandpur Maning 
##                                                                  777 
##                                   Chandrakhong Ningel, Mayai Keithel 
##                                                                  699 
##                                                          Changamdabi 
##                                                                 3326 
##                                              Changangei Makha Leikai 
##                                                                  911 
##                                    Changangei Maning (Northern side) 
##                                                                  699 
##                                    Changangei Maning (Southern side) 
##                                                                  927 
##                                                   Changangei Uchekon 
##                                                                  930 
##                                         Changmdabi and Kamo Yaithibi 
##                                                                  946 
##                                                              Chanung 
##                                                                  339 
##                                                        Chaobok Kabui 
##                                                                 1080 
##                                                   Charangpat Maklang 
##                                                                  951 
##                                                    Charangpat Mamang 
##                                                                  953 
##                                             Charangpat Mamang Leikai 
##                                                                 1113 
##                                   Charangpat Mamang Leikai (Maklang) 
##                                                                  853 
##                                                             Cherapur 
##                                                                 1058 
##                                        Cherapur (Mushlim And Meitei) 
##                                                                 1262 
##                                                Cheshaba Makha Leikai 
##                                                                  779 
##                                                   Chingangbam Leikai 
##                                                                 1409 
##                                                          Chingdompok 
##                                                                 3488 
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
##                                                                  830 
##                                                  Elangkhangpokpi (B) 
##                                                                  853 
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
##                                                                  870 
##                                                     Hangoipat Nepali 
##                                                                  418 
##                                                              Hangoon 
##                                                                  723 
##                                                Hangoon Mathak Leikai 
##                                                                  817 
##                                                 Hangoon Mayai Leikai 
##                                                                  870 
##                                                           Haogrampat 
##                                                                  871 
##                                          Haorang Sabal Mamang Leikai 
##                                                                  512 
##                                                Haoreibi Turel Ahanbi 
##                                                                  778 
##                                                  Haotak Tapha Khunou 
##                                                                  326 
##                                                             Haraorou 
##                                                                  851 
##                                                          Hayel Labuk 
##                                                                 1114 
##                                         Heibong Makhong Makha Leikai 
##                                                                  625 
##                                        Heibong Makhong Mathak Leikai 
##                                                                  637 
##                                           Heibongpokpi Mamang Leikai 
##                                                                  561 
##                                 Heigrujam Leikai and Thangjam Leikai 
##                                                                  524 
##                                              Heikrujam Mamang Leikai 
##                                                                  776 
##                                              Heikrujam Maning Leikai 
##                                                                  817 
##                                                Heingang Awang Leikai 
##                                                                  602 
##                                    Heingang Awang Leikai Saya Lampak 
##                                                                  920 
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
##                                                                  998 
##                               Heinoukhongnembi Laishram Leikai Awang 
##                                                                  524 
##                               Heinoukhongnembi Laishram Leikai Makha 
##                                                                  507 
##                       Heinoupok Awang, Mamang, Langjing Makha Leikai 
##                                                                  628 
##                                               Heinoupok Makha Leikai 
##                                                                  686 
##                                                   Heirok Heituppokpi 
##                                                                 1823 
##                                                        Heirok Khunou 
##                                                                 1031 
##                                                 Heirok Maning Leikai 
##                                                                 1253 
##                                         Heirok Mayai Leikai Part (2) 
##                                                                  744 
##                                                    Heirok Mayai Part 
##                                                                 1056 
##                                                          Heirok Part 
##                                                                 3414 
##                                            Heirok Part Heirok Khunou 
##                                                                 1106 
##                                                       Heirok Part II 
##                                                                 1270 
##                              Heirok Part, Maning Leikai, Kabo Leikai 
##                                                                 1134 
##                                                 Heisnam Awang Leikai 
##                                                                  959 
##                                                 Heisnam Makha Leikai 
##                                                                  640 
##                                                            Heiyaikon 
##                                                                  798 
##                                                               Heiyel 
##                                                                  373 
##                                                             Hillghat 
##                                                                  738 
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
##                                                                  571 
##                                             Hiyanglam Waikhom Leikai 
##                                                                  651 
##                                             Hiyangthang Awang Leikai 
##                                                                  672 
##                                            Hiyangthang Mamang Leikai 
##                                                                  517 
##                                            Hiyangthang Maning Leikai 
##                                                                  660 
##                                      Hiyangthang Maning Makha Leikai 
##                                                                  735 
##                                           Hiyangthang Tarahei Konjil 
##                                                                  844 
##                                                              Huidrom 
##                                                                  444 
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
##                                                                  674 
##                                   Irengbam Makha Mamang Mayai Leikai 
##                                                                  643 
##                                         Irengbam Makha Maning Leikai 
##                                                                  408 
##                                               Irengband Turel Mamang 
##                                                                 1173 
##                                           Irom Meijrao Mamang Leikai 
##                                                                  950 
##                                           Irom Meijrao Maning Leikai 
##                                                                  788 
##                                                       Irong Cheshaba 
##                                                                 1689 
##                                       Irong Meinam and Aribam Leikai 
##                                                                 1069 
##                                                          Irong Umang 
##                                                                  939 
##                                            Ishok Makha Maning Leikai 
##                                                                  708 
##                                                 Ishok Mamang Chingya 
##                                                                  737 
##                                                  Ishok Maning Leikai 
##                                                                  885 
##                                                            Islamabad 
##                                                                  710 
##                                                       Itam Sawombung 
##                                                                  643 
##                                                      Ithai Dam Manak 
##                                                                  996 
##                                                  Ithai Mamang Leikai 
##                                                                  724 
##                        Ithai Wapokpi Maning, Mamang and Mayai Leikai 
##                                                                  502 
##                                                                Itham 
##                                                                  485 
##                                                        Ithing Mamang 
##                                                                 1128 
##                                                      Jairolpokpi Mar 
##                                                                  816 
##                                                 Jakuradhor Part-I(A) 
##                                                                 1049 
##                                                   Jakuradhor Part -2 
##                                                                  493 
##                                                            Kachikhul 
##                                                                  693 
##                                                            Kachimpur 
##                                                                  799 
##                                                            Kadamtala 
##                                                                  435 
##                                                    Kadangband Singda 
##                                                                  837 
##                                                Kairang Mamang Leikai 
##                                                                  997 
##                                          Kairang Muslim Awang Leikai 
##                                                                  513 
##                                         Kairang Muslim Mamang Leikai 
##                                                                  788 
##                                          Kairang Muslim Mayai Leikai 
##                                                                  678 
##                                                 Kairang Tera Makhong 
##                                                                  517 
##                                                  Kairembikhok Khunou 
##                                                                 1419 
##                                             Kakwa Laiphrakpam Leikai 
##                                                                 1281 
##                                                  Kakyai Makha Leikai 
##                                                                  743 
##                                                  Kakyai Mayai Leikai 
##                                                                  536 
##                                               Kalika Lok, Kajinphung 
##                                                                  214 
##                                                               Kameng 
##                                                                  873 
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
##                                                                  863 
##                                                  Kanglatongbi Mandir 
##                                                                  976 
##                                                 Kanglatongbi Tispari 
##                                                                  860 
##                                                          Kangshamram 
##                                                                 1736 
##                                                         Kangyambem-B 
##                                                                  665 
##                                                        Kangyambem -A 
##                                                                  715 
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
##                                                                  613 
##                                                   Keibi Heikak Mapal 
##                                                                  504 
##                                                        Keibi Khullen 
##                                                                  635 
##                                                     Keibi Taret Khul 
##                                                                  574 
##                                                 Keibul Mathak Leikai 
##                                                                  749 
##                                                  Keibul Mayai Leikai 
##                                                                  826 
##                                           Keibul Mayai, Makha Leikai 
##                                                                  672 
##                                                         Keikhu Kabui 
##                                                                  456 
##                                          Keikhu Mushlim Makha Leikai 
##                                                                  602 
##                                                 Keikol Mamang Leikai 
##                                                                  488 
##                                  Keinou Thongkha Makha Mamang Leikai 
##                                                                  905 
##                                         Keinou Thongkha Mayai Leikai 
##                                                                  832 
##                                      Keinou Thongkhong Maning Leikai 
##                                                                  998 
##                                        Keinou Thongthak Bazar Maning 
##                                                                  933 
##                                                               Keirak 
##                                                                  737 
##                                                Keirak Leirak Achouba 
##                                                                  643 
##                                                  Keirak Makha Leikai 
##                                                                  758 
##                                           Keirak Makha Maning Leikai 
##                                                                  802 
##                                                 Keirak Mamang Leikai 
##                                                                  641 
##                                         Keirao Bitra Awang Chingdong 
##                                                                  992 
##                                                   Keirao Bitra Makha 
##                                                                  873 
##                                              Keirao Langdum Nongchup 
##                                                                  896 
##                                               Keirao Langdum Nongpok 
##                                                                  875 
##                                          Keirao Makting Awang Leikai 
##                                                                 1228 
##                                                 Keirao Makting Makha 
##                                                                  968 
##                                                 Keirao Makting Mayai 
##                                                                 1437 
##                    Keirao Wangkhem Laiphrok Maring, Somther Tangkhul 
##                                                                 1011 
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
##                                                                  640 
##                                                           Khabeishoi 
##                                                                 2153 
##                                                                Khabi 
##                                                                 1396 
##                                                 Khaidem Awang Leikai 
##                                                                  669 
##                                                       Khaidem Leikai 
##                                                                  427 
##                                               Khaidem Leikai (North) 
##                                                                  934 
##                                              Khaidem Leikai(South-A) 
##                                                                  731 
##                                                 Khaidem Makha Leikai 
##                                                                  667 
##                                      Khalakhong Amanbi Maning Leikai 
##                                                                  880 
##                                                             Khamaran 
##                                                                  807 
##                                        Khamnam Leirak Maning Thangba 
##                                                                  889 
##                                        Khangabok Awang Mamang Leikai 
##                                                                  684 
##                                        Khangabok Awang Maning Leikai 
##                                                                  587 
##                                           Khangabok Khulakpam Leikai 
##                                                                  887 
##                                          Khangabok Khullakpam Leikai 
##                                                                 1592 
##                                                     Khangabok Khunou 
##                                                                  460 
##                                             Khangabok Maisnam Leikai 
##                                                                 1167 
##                             Khangabok Maisnam Leikai Cherapur Khunou 
##                                                                 1295 
##                                          Khangabok Maning And Mamang 
##                                                                  860 
##                                              Khangabok Maning Leikai 
##                                                                 3141 
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
##                                                                  965 
##                                               Khoijuman Mayai Leikai 
##                                                                  726 
##                                                              Khoirom 
##                                                                 2731 
##                                                             Khomidok 
##                                                                 2633 
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
##                                                                  486 
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
##                                                                  677 
##                                            Khundrakpam Maning Leikai 
##                                                                  549 
##                                            Khurai Chingangbam Leikai 
##                                                                  993 
##                                              Khurai Khongnangmakhong 
##                                                                 1482 
##                                               Khurai Kongkham Leikai 
##                                                                 1239 
##                                    Khurai Kongpal Chingangbam Leikai 
##                                                                 1657 
##                                                 Khurai Konsam Leikai 
##                                                                 2992 
##                                        Khurai Nandeibam Makha Leikai 
##                                                                  492 
##                                     Khurai Sajor Lairou Pukhri Awang 
##                                                                  625 
##                                                  Khurai Sajor Leikai 
##                                                                  547 
##                                            Khurai Thoidingjam Leikai 
##                                                                 1052 
##                                                Khurai Thongam Leikai 
##                                                                  921 
##                                         Khurkhul Awang Mamang Leikai 
##                                                                  614 
##                                         Khurkhul Awang Maning Leikai 
##                                                                  537 
##                                                Khurkhul Makha Leikai 
##                                                                  883 
##                                                Khurkhul Sebok Leikai 
##                                                                  968 
##                                                        Kitana Panung 
##                                                                  531 
##                                                                Kiyam 
##                                                                  683 
##                                                Kiyamgei Awang Leikai 
##                                                                  857 
##                                         Kiyamgei Awang Maning Leikai 
##                                                                 1031 
##                                               Kiyamgei Mamang Leikai 
##                                                                  543 
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
##                                                                  848 
##                                                    Kodompokpi Maning 
##                                                                  591 
##                                              Kodompokpi Mayai Leikai 
##                                                                  532 
##                                                      Koirengei Bazar 
##                                                                  621 
##                                              Koirengei Mamang Leikai 
##                                                                  456 
##                                              Komlakhong Awang Leikai 
##                                                                  845 
##                                              Komlakhong Makha Leikai 
##                                                                  650 
##                                                 Kongba Chanam Leikai 
##                                                                  674 
##                                       Kongba Laishram Leikai (North) 
##                                                                  567 
##                                       Kongba Laishram Leikai (South) 
##                                                                  624 
##                                    Kongba Nongthombam Leikai (South) 
##                                                                  676 
##                                                      Kongkham Leikai 
##                                                                 1016 
##                                                Kongpal Chanam Leikai 
##                                                                  555 
##                                             Kongpal Naoroibam Leikai 
##                                                                  641 
##                                         Kongpal Sajor Leikai (Awang) 
##                                                                  612 
##                                         Kongpal Sajor Leikai (Makha) 
##                                                                  468 
##                                         Konjeng Lamdong Awang Leikai 
##                                                                  696 
##                                         Konjeng Lamdong Makha Leikai 
##                                                                  870 
##                                    Konjeng Langpoklakpam Leikai East 
##                                                                  567 
##                              Konjeng Langpoklakpam Leikai West South 
##                                                                  712 
##                                                       Konjeng Leikai 
##                                                                  513 
##                                           Konjeng Ningthoujam Leikai 
##                                                                  762 
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
##                                                                  498 
##                                      Konthoujam Mamang Leikai Part-1 
##                                                                  573 
##                                      Konthoujam Mamang Leikai Part-2 
##                                                                  981 
##             Konthoujam Maning Leikai (Northern side of Bamon Leirak) 
##                                                                  515 
##             Konthoujam Maning Leikai (Southern side of Bamon Leirak) 
##                                                                  841 
##                                                  Konuma, Hiyangkhong 
##                                                                  789 
##                                                        Koupak Nepali 
##                                                                  977 
##                                                              Koutruk 
##                                                                  394 
##                                                      Kshetri Bengoon 
##                                                                 1260 
##                                            Kshetri Bengoon (North-A) 
##                                                                  831 
##                                    Kshetri Bengoon and Yangbi Khunou 
##                                                                  765 
##                                        Kshetrigao (Keikhu Mushlim A) 
##                                                                  839 
##                                              Kshetrigao Awang Leikai 
##                                                                 2218 
##                                        Kshetrigao Awang Sabal Leikai 
##                                                                 1435 
##                                              Kshetrigao Makha Leikai 
##                                                                 2411 
##                              Kwakeithel Mayaikoibi Chabungbam Leikai 
##                                                                  563 
##                             Kwakeithel Mayaikoibi Ningthoujam Leikai 
##                                                                  484 
##                                         Kwakeithel Thounaojam Leikai 
##                                                                  392 
##                                                               Kwakta 
##                                                                  510 
##                                                        Kwakta Khuman 
##                                                                  757 
##                                           Kwakta Khuman Makha Leikai 
##                                                                  779 
##                                                   Kwakta Tampakmayum 
##                                                                  873 
##                                               Kyamgei Khoirom Leikai 
##                                                                  720 
##                                                             Laimanai 
##                                                                  720 
##                                                            Laingoubi 
##                                                                 1049 
##                                          Laipham Khunou Makha Leikai 
##                                                                 1115 
##                                         Laipham Khunou Mamang Leikai 
##                                                                  671 
##                                          Laipham Khunou Mayai Leikai 
##                                                                  893 
##                                               Lairenjam Awang Leikai 
##                                                                  803 
##                                               Lairenjam Makha Leikai 
##                                                                  836 
##                                                      Lairenjam Sabal 
##                                                                  393 
##                                                           Lairenkabi 
##                                                                  644 
##                                                          Lairensajik 
##                                                                  528 
##                                    Lairikyengbam Leikai Mayai Leirak 
##                                                                  707 
##                                           Lairikyengbam Makha Leikai 
##                                                                  989 
##                                       Lairikyengbam Mayai Leikai (A) 
##                                                                  711 
##                                           Lairikyengbam Salan Leirak 
##                                                                 1037 
##                                                      Laishram Leikai 
##                                                                 1404 
##                                                            Lalpani-I 
##                                                                  884 
##                                                               Lambal 
##                                                                  579 
##                                                           Lamboikhul 
##                                                                  696 
##                                              Lamjao Awang Leikai (B) 
##                                                                  584 
##                                                  Lamjao Makha Leikai 
##                                                                  881 
##                                              Lamjao Mayai Leikai (A) 
##                                                                  714 
##                                               Lamjao Part (1) Tejpur 
##                                                                  666 
##                                                            Lamlongei 
##                                                                 1479 
##                                                            Langathel 
##                                                                 1495 
##                                                  Langathel Mandakini 
##                                                                 1087 
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
##                                                                 1076 
##                                      Langmeidong Maning Makha Leikai 
##                                                                  620 
##                                            Langmeithet Kwarok Maring 
##                                                                  712 
##                                                Langpok Maning Leikai 
##                                                                  650 
##                                                  Langthabal Chingkha 
##                                                                  857 
##                                          Langthabal Lep Awang Leikai 
##                                                                  585 
##                                          Langthabal Lep Makha Leikai 
##                                                                  596 
##                                          Langthabal Lep Mayai Leikai 
##                                                                 1267 
##                                  Langthabal Mantrikhong Awang Leikai 
##                                                                  896 
##                                  Langthabal Mantrikhong Makha Leikai 
##                                                                  989 
##                     Langthabal Phuramakhong, Heiripok Chingi Chingya 
##                                                                  698 
##                                           Laphupat Tera Awang Leikai 
##                                                                  468 
##                                                 Laphupat Tera Khunou 
##                                                                  851 
##                                           Laphupat Tera Mayai Leikai 
##                                                                  640 
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
##                                                                  722 
##                                                 Leimram Makha Leikai 
##                                                                  613 
##                                                Leimram Mamang Leikai 
##                                                                  490 
##                                                   Leimram Waroiching 
##                                                                  213 
##                                                          Leirongthel 
##                                                                 1499 
##                                                  Leishabithel Meetei 
##                                                                  799 
##                                                         Leishangthem 
##                                                                 2327 
##                                            Leishangthem Keli Makhong 
##                                                                 1231 
##                              Leishangthem Thong Manung Maning Leikai 
##                                                                 1018 
##                                                           Lemba Khul 
##                                                                  728 
##                                                       Lilando Lampak 
##                                                                  621 
##                                                           Litanpokpi 
##                                                                  673 
##                                                      Loitang Khullen 
##                                                                  810 
##                                                       Loitang Khunou 
##                                                                  982 
##                                                       Loukham Leirak 
##                                                                  738 
##                                                            Lourembam 
##                                                                 2010 
##                                                   Luker Makha Leikai 
##                                                                  425 
##                                           Luwangsangbam Awang Leikai 
##                                                                  633 
##                                          Luwangsangbam Mamang Leikai 
##                                                                  521 
##                                          Luwangshangbam Mayai Leikai 
##                                                                 1003 
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
##                                                                  869 
##                                                  Maibam Mayai Leikai 
##                                                                  605 
##                                                            Mairembam 
##                                                                  847 
##                                                      Makha Pat Awang 
##                                                                  521 
##                                            Makha Pat Khongjin Leikai 
##                                                                  569 
##                                                              Maklang 
##                                                                 2283 
##                                           Malom Tulihal Awang Leikai 
##                                                                  800 
##                                                 Malom Tulihal Maning 
##                                                                  935 
##                                                Malom Tuliyaima Awang 
##                                                                  871 
##                       Malom Tuliyaima Awang (Laishram Leiraki North) 
##                                                                  713 
##                                         Malom Tuliyaima Makha Leikai 
##                                                                  829 
##                                                               Mantak 
##                                                                  522 
##                                                   Matai Mayai Leikai 
##                                                                  804 
##                                 Mayang Langjing Tamang Makha Thangba 
##                                                                  993 
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
##                                                                  886 
##                                                              Moijing 
##                                                                 4621 
##                                         Moirang Hanuba Mamang Leikai 
##                                                                  629 
##                                         Moirang Hanuba Maning Leikai 
##                                                                  535 
##                                                        Moirang Kampu 
##                                                                  949 
##                                            Moirang Khunou Haogrampat 
##                                                                 1095 
##                                                Moirang Khunou Maning 
##                                                                  860 
##                                                         Moirangpurel 
##                                                                 1128 
##                                                 Mongjam Mayai Leikai 
##                                                                  501 
##                                             Mongshangei Awang Leikai 
##                                                                  592 
##                                             Mongshangei Makha Leikai 
##                                                                  729 
##                                             Mongshangei Mayai Leikai 
##                                                                 1199 
##                                                           Nachou (A) 
##                                                                  849 
##                                                           Nachou (B) 
##                                                                  767 
##                                                           Nachou (C) 
##                                                                  745 
##                                                           Nachou (D) 
##                                                                  779 
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
##                                                                  915 
##                                                  Naorem Awang Leikai 
##                                                                  718 
##                                            Naorem Awang Mayai Leikai 
##                                                                  697 
##                                                  Naorem Makha Leikai 
##                                                                  682 
##                                     Naoriya Pakhanglakpa Irom Leikai 
##                                                                  952 
##                            Naoriya Pakhanglakpa Keisham Awang Leikai 
##                                                                  702 
##                            Naoriya Pakhanglakpa Keisham Mayai Leikai 
##                                                                  690 
##                                Naoriya Pakhanglakpa Lourembam Leikai 
##                                                                  567 
##                           Naoriya Pakhanglakpa Lourembam Leikai West 
##                                                                  367 
##                             Naoriya Pakhanglakpa Yangam Leirak Makha 
##                                                                  793 
##                                            Naran Konjin Makha Leikai 
##                                                                  683 
##                                              Naranseina Makha Leikai 
##                                                                  970 
##                                                           Narayanpur 
##                                                                  356 
##                                                 Nepra Company Leikai 
##                                                                  507 
##                                       Ngaikhong Khullen Awang Leikai 
##                                                                  736 
##                                         Ngaikhong Khullen Kha Leikai 
##                                                                  632 
##                                      Ngaikhong Khullen Mamang Leikai 
##                                                                  771 
##                                                     Ngaikhong Khunou 
##                                                                  714 
##                                              Ngaikhong Maning Leikai 
##                                                                  602 
##                                       Ngaikhong Siphai Mamang Leikai 
##                                                                  520 
##                                       Ngaikhong Siphai Maning Leikai 
##                                                                  657 
##                                             Ngairangbam Awang Leikai 
##                                                                  862 
##                                             Ngairangbam Makha Leikai 
##                                                                  985 
##                                                       Ngakchroupokpi 
##                                                                  737 
##                                          Ngangkhalawai Mamang Leikai 
##                                                                  780 
##                                          Ngangkhalawai Maning Leikai 
##                                                                  715 
##                                                       Nganukon No. 3 
##                                                                  932 
##                                              Nillakuthi Awang Leikai 
##                                                                  716 
##                                               Ningombam Awang Leikai 
##                                                                 1003 
##                                               Ningombam Makha Leikai 
##                                                                  863 
##                                      Ningomthong Kitna Panung (West) 
##                                                                  775 
##                                                         Ningthoubung 
##                                                                  807 
##                                                  Ningthoubung Khunou 
##                                                                  790 
##                                Ningthoukhong Awang Khunou Ward No. 1 
##                                                                  492 
##                                      Ningthoukhong Awang Ward No. 14 
##                                                                  860 
##                                             Ningthouta Chandon Pokpi 
##                                                                  493 
##                                                 Nongada Awang Leikai 
##                                                                  443 
##                                                 Nongada Makha Leikai 
##                                                                  750 
##                                                Nongdam Mamang Leikai 
##                                                                  553 
##                                                   Nongmaikhong Awang 
##                                                                  673 
##                                            Nongmaikhong Awang Leikai 
##                                                                  837 
##                              Nongpok Sekmai Khunbi And Toubul Khunou 
##                                                                 1123 
##                                                              Nongren 
##                                                                 1682 
##                                                            Nungbrang 
##                                                                  826 
##                                                           Nungei (A) 
##                                                                  653 
##                                                           Nungei (B) 
##                                                                  587 
##                                                  Nungoi Makha Leikai 
##                                                                  848 
##                                                             Nungphou 
##                                                                  571 
##                                                        Nungukhongyam 
##                                                                  574 
##                                                         Oinam Leikai 
##                                                                  845 
##                                                Oinam Sawombung Awang 
##                                                                  865 
##                                         Oinam Sawombung Makha Leikai 
##                                                                  538 
##                                                     Oinam Shawombung 
##                                                                 1720 
##                       Oinam Thingel Khongnang Pheidekpi Makha Leikai 
##                                                                  685 
##                                                 Oksu Ningthemchakhul 
##                                                                  589 
##                                                         Pallel Bazar 
##                                                                  630 
##                                            Pallel Leimangai Chingjin 
##                                                                  449 
##                                                 Pallel Mamang Leikai 
##                                                                  536 
##                                                  Pallel Mayai Leikai 
##                                                                  725 
##                                                           Pangaltabi 
##                                                                 1686 
##                                                    Pangei Meiteikhul 
##                                                                  860 
##                                                      Pangei Yangdong 
##                                                                 1413 
##                                                            Pantilong 
##                                                                  371 
##                                                   Papal Mamang Ching 
##                                                                  417 
##                                                  Papal Maning Leikai 
##                                                                  812 
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
##                                                                  573 
##                                                 Phayeng Makha Leikai 
##                                                                  756 
##                                                 Phayeng Mayai Leikai 
##                                                                  637 
##                                                 Phayeng Sabal Leikai 
##                                                                  374 
##                                   Phayeng, Kharang Nongpok and Sabal 
##                                                                  676 
##                                                              Phoudel 
##                                                                 1716 
##                                             Phougakchao Awang Leikai 
##                                                                 1069 
##                                       Phougakchao Ikhai Awang Leikai 
##                                                                  840 
##                                      Phougakchao Ikhai Maning Leikai 
##                                                                  697 
##                                             Phougakchao Makha Leikai 
##                                                                 1116 
##                                          Phubala Awang Mamang Leikai 
##                                                                  775 
##                                          Phubala Makha Mamang Leikai 
##                                                                  807 
##                                                Phumlou Mamang Leikai 
##                                                                  761 
##                                                       Phumlou Siphai 
##                                                                  753 
##                                                        Phunal Maring 
##                                                                  841 
##                                                             Phundrei 
##                                                                  957 
##                                                Phundrei Awang Leikai 
##                                                                 1260 
##                                                      Poirou Khongjil 
##                                                                 2245 
##                                            Porompat (Kshetri Leikai) 
##                                                                  675 
##                                                      Porompat Muslim 
##                                                                  926 
##                                                Porompat Mutum Leikai 
##                                                                  803 
##                                                          Potshangbam 
##                                                                  925 
##                                                      Potshangbam (B) 
##                                                                  964 
##                                                              Pourabi 
##                                                                  776 
##                                                        Pukhao Khabam 
##                                                                  571 
##                                                       Pukhao Laipham 
##                                                                  470 
##                                                       Pukhao Naharup 
##                                                                  552 
##                                                       Pukhao Terapur 
##                                                                  581 
##                                                    Pukhrambam Mamang 
##                                                                  569 
##                                                    Pukhrambam Maning 
##                                                                  722 
##                                      Pungdongbam Awang Mamang Leikai 
##                                                                  560 
##                                      Pungdongbam Awang Maning Leikai 
##                                                                  660 
##                                             Pungdongbam Makha Leikai 
##                                                                  679 
##                               Purna Heituppokpi Wangjing Sorokhaibam 
##                                                                  928 
##                        Purna Heituppokpi Wangjing Sorokhaibam Leikai 
##                                                                  966 
##                                                             Rasidpur 
##                                                                  448 
##                                                   Sabungkhok Khunjao 
##                                                                  968 
##                                                      Sadokpam Leikai 
##                                                                  439 
##                              Sagolband Sapam Leirak Mamang and Makha 
##                                                                  827 
##                                Sagolband Sapam Leirak Maning Thangba 
##                                                                  727 
##                                         Sagolband Tera Lukram Leirak 
##                                                                  635 
##                            Sagolband Tera Lukram Leirak Awang Leikai 
##                                                                  531 
##                            Sagolband Tera Lukram Leirak Mayai Leikai 
##                                                                  588 
##                                       Sagolband Tera Tongbram Leikai 
##                                                                  969 
##                                             Sagoltongba Awang Leikai 
##                                                                  949 
##                                             Sagoltongba Makha Leikai 
##                                                                  925 
##                                                               Sagram 
##                                                                 1001 
##                                                  Saiton Awang Leikai 
##                                                                  738 
##                                                                Sajeb 
##                                                                 1418 
##                                                         Sajor Leikai 
##                                                                  789 
##                                                  Salam Mamang Leikai 
##                                                                  594 
##                                                  Salam Maning Leikai 
##                                                                  726 
##                                            Salungpham (Kangthokchao) 
##                                                                 1051 
##                                              Salungpham Kangthokchao 
##                                                                  607 
##                                                 Samaram Mayai Leikai 
##                                                                  735 
##                                                Samusang Mutum Yangbi 
##                                                                  112 
##                                                   Samusang Shantipur 
##                                                                  654 
##                                                         Sandangsenba 
##                                                                  677 
##                                             Sangaiprou Mamang Leikai 
##                                                                  983 
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
##                                                                  649 
##                                                     Sanjenbam Khunou 
##                                                                  777 
##                                                 Santhel Awang Leikai 
##                                                                 1019 
##                                                 Santhel Makha Leikai 
##                                                                 1091 
##                                                       Santhong Awang 
##                                                                  654 
##                                                                Sapam 
##                                                                 2629 
##                         Sapam Leirak Nongmaithem Awang Maning Laikai 
##                                                                  462 
##                               Sapam Leirak Nongmaithem Mamang Leikai 
##                                                                  731 
##                                                            Sawombung 
##                                                                  892 
##                                              Sawombung Kabui Khunjao 
##                                                                  686 
##                                              Sawombung Maning Leikai 
##                                                                  627 
##                                                 Seijang Awang Leikai 
##                                                                  674 
##                                                 Seijang Makha Leikai 
##                                                                  615 
##                                                            Sekmaijin 
##                                                                 2594 
##                                                     Sekmaijin Khunou 
##                                                                 1778 
##                                                    Sekmaijin Thongam 
##                                                                  732 
##                                                   Sekta Awang Leikai 
##                                                                  858 
##                                                   Sekta Makha Leikai 
##                                                                  550 
##                                                   Sekta Mayai Leikai 
##                                                                  490 
##                                                       Senjam Chirang 
##                                                                  595 
##                                                        Senjam Khunou 
##                                                                  631 
##                                   Serou Part (1) Mayai, Makha Leikai 
##                                                                  778 
##                              Serou Part (1) Serou Awang Leikai Bazar 
##                                                                 1062 
##                                                       Serou Part (2) 
##                                                                 1759 
##                                              Shagolmang Makha Leikai 
##                                                                  493 
##                                                              Shambei 
##                                                                  432 
##                                                           Sharouthel 
##                                                                  489 
##                                                             Shikhong 
##                                                                 1056 
##                                                      Shikhong Khunou 
##                                                                 1203 
##                                                               Shinga 
##                                                                 2008 
##                                                                Sinam 
##                                                                  767 
##                                                       Sonapur-Part-I 
##                                                                  708 
##                                                      Sonapur-Part-II 
##                                                                  623 
##                                               Sora (A) Maning Leikai 
##                                                                  820 
##                                               Sora (B) Maning Leikai 
##                                                                  722 
##                                       Sora Awang Ching Wangma Leikai 
##                                                                  681 
##                                        Sora Mamang Thongthabi Leikai 
##                                                                  777 
##                                       Sora Mayai Langjeihoubi Leikai 
##                                                                  898 
##                                                    Sora Mayai Leikai 
##                                                                  872 
##                                             Sorokhaibam Leikai Awang 
##                                                                  486 
##                                             Sorokhaibam Leikai Makha 
##                                                                  578 
##                       Soyam Leirak and Khamnam Leirak Mamang Thangba 
##                                                                  815 
##                                              Sunusiphai Awang Leikai 
##                                                                  704 
##                                              Sunusiphai Mayai Leikai 
##                                                                  818 
##                                                          Tairenpokpi 
##                                                                  594 
##                                                  Takhel Makha Leikai 
##                                                                 1088 
##                                                 Takhel Mamang Leikai 
##                                                                  546 
##                                                   Takhelambam Konjil 
##                                                                  405 
##                                                         Takhok Makha 
##                                                                  436 
##                                                         Takhok Mapal 
##                                                                 1189 
##                                                      Takyel Khongbal 
##                                                                  813 
##                                               Takyel Khongbal Mamang 
##                                                                  600 
##                                               Takyel Khongbal Maning 
##                                                                  813 
##                                    Takyel Khongbal Pongshubam Leikai 
##                                                                  756 
##                                 Takyel Kolom Mamang and Makha Leikai 
##                                                                  582 
##                                           Takyel Kolom Maning Leikai 
##                                                                  665 
##                                              Tangjeng Chingya Leikai 
##                                                                  749 
##                      Tangjeng Khunjao, Mangjin Khongyam Makha Leikai 
##                                                                  598 
##                                                             Tangkham 
##                                                                  890 
##                                                      Tangkhul Avenue 
##                                                                  420 
##                                             Taobungkhok Makha Leikai 
##                                                                  787 
##                                   Taobungkhok Mayai and Makha Leikai 
##                                                                  276 
##                                             Taobungkhok Mayai Leikai 
##                                                                  898 
##                                                              Tekcham 
##                                                                 1805 
##                                                Tekcham Mamang Leikai 
##                                                                  557 
##                                                 Tekcham Sabal Leikai 
##                                                                  677 
##                                                               Tellou 
##                                                                  721 
##                                                           Tendongyan 
##                                                                 1006 
##                                                         Tentha Makha 
##                                                                 3316 
##                                                  Tentha Makha Leikai 
##                                                                 3612 
##                                         Tera Loukrakpam Leikai Awang 
##                                                                  834 
##                                         Tera Loukrakpam Leikai Mayai 
##                                                                  801 
##                                                            Terakhong 
##                                                                  661 
##                                                Terakhongsangbi Bazar 
##                                                                  771 
##                                  Thambalkhong Kongba Laishram Leikai 
##                                                                  994 
##                                                   Thambalkhong North 
##                                                                  537 
##                                            Thambalkhong Sabal Leikai 
##                                                                  918 
##                                                          Thamnapokpi 
##                                                                  607 
##                                            Thamnapokpi Mamang Leikai 
##                                                                 1523 
##                                              Thanga Chingkha Haoreng 
##                                                                  622 
##                                              Thanga Chingkha Khomlai 
##                                                                  601 
##                                                Thanga Khunjem Leikai 
##                                                                 1623 
##                                        Thanga Moirangthem Leikai (B) 
##                                                                  682 
##                                                  Thanga Oinam Leikai 
##                                                                 1099 
##                                                   Thanga Salam Heiga 
##                                                                  731 
##                                                 Thanga Salam Mangkha 
##                                                                  695 
##                                                      Thanga Shamukon 
##                                                                  564 
##                                                          Thangalawai 
##                                                                  794 
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
##                                                                  697 
##                                                        Thinungei (B) 
##                                                                  714 
##                                                      Thinungei (C-1) 
##                                                                  701 
##                                                      Thinungei (C-2) 
##                                                                  709 
##                                                  Thiyam Konjin Awang 
##                                                                  732 
##                                                  Thiyam Konjin Makha 
##                                                                  813 
##                                                 Thiyam Mamang Leikai 
##                                                                  505 
##                                                  Thiyam Mayai Leikai 
##                                                                  548 
##                                                             Thokchom 
##                                                                  536 
##                                                              Thongam 
##                                                                  923 
##                                                Thongjao Awang Leikai 
##                                                                  690 
##                                                Thongjao Makha Leikai 
##                                                                  714 
##                             Thongju Kakwa Lamdaibung Laishram Leikai 
##                                                                  525 
##                                                       Thongju Koirou 
##                                                                  429 
##                                           Thongju Nameirakpam Leikai 
##                                                                  698 
##                                                Thongju Naorem Leikai 
##                                                                 1237 
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
##                                                                  928 
##                           Tokpaching, Lairok Munushoi, Sharik Konjil 
##                                                                  502 
##                                                         Top Chingtha 
##                                                                 3510 
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
##                                                                  749 
##                                           Toubul Awang Mamang Leikai 
##                                                                 1224 
##                                                  Toubul Makha Maning 
##                                                                  668 
##                                                 Toubul Maning Leikai 
##                                                                  706 
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
##                                                                  713 
##                                               Uchekon Khunou (North) 
##                                                                  586 
##                                               Uchekon Khunou (South) 
##                                                                  587 
##                                Uchekon Kongba Kshetri Leikai (North) 
##                                                                  669 
##                                Uchekon Kongba Kshetri Leikai (South) 
##                                                                  668 
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
##                                                                 2049 
##                                                               Upokpi 
##                                                                  726 
##                                                                 Urup 
##                                                                  875 
##                                                          Urup Meitei 
##                                                                  802 
##                                                          Urup Muslim 
##                                                                  671 
##                                                          Urup Naokal 
##                                                                 1051 
##                                                         Utlou Mamang 
##                                                                  757 
##                                             Utlou Mayai Awang Leikai 
##                                                                  680 
##                                                   Utlou Mayai Leikai 
##                                                                  642 
##                                                   Utlou Turel Wangma 
##                                                                  683 
##                                                                 Uyal 
##                                                                 1346 
##                                                Uyumpok Mamang Leikai 
##                                                                  965 
##                                                Uyumpok Maning Leikai 
##                                                                  543 
##                                              Vijayanagar Kanglatombi 
##                                                                 1092 
##                                                              Wabagai 
##                                                                 2738 
##                                                      Wabagai Kadajit 
##                                                                  876 
##                                              Wabgai Mairembam Leikai 
##                                                                  674 
##                                                     Wabgai Tera Urak 
##                                                                  599 
##                                          Waheng Khuman Mamang Leikai 
##                                                                  648 
##                                          Waheng Khuman Maning Leikai 
##                                                                  753 
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
##                                                                  569 
##                                                 Waiton Maning Leikai 
##                                                                  801 
##                                                  Waiton Mayai Leikai 
##                                                                  604 
##                                                     Wakching Khullen 
##                                                                  948 
##                                                              Wakhong 
##                                                                  342 
##                                                              Wangbal 
##                                                                 1299 
##                                            Wangkhei Loumanbi (North) 
##                                                                  590 
##                                            Wangkhei Loumanbi (South) 
##                                                                  700 
##                                                      Wangkhem Konjin 
##                                                                 1706 
##                                                           Wangoo (A) 
##                                                                  880 
##                                                         Wangoo (B-1) 
##                                                                 1111 
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
##                                                                  615 
##                                             Wangoo Terakhong Makhong 
##                                                                  592 
##                                        Wangu Terakhong Maning Leikai 
##                                                                  822 
##                                    Wareppam Leikai and Naorem Leikai 
##                                                                  661 
##                                                              Warukok 
##                                                                 1180 
##                                                           Wathalambi 
##                                                                  587 
##                                           Yaingangpokpi Awang Leikai 
##                                                                  982 
##                                                               Yambem 
##                                                                 4190 
##                                          Yangbi Leikai Litan Makhong 
##                                                                  682 
##                                                             Yangdong 
##                                                                  438 
##                                                      Yengkhom Leirak 
##                                                                  807 
##                                 Yengkhom Leirak and Ramji Kabui Khul 
##                                                                  455 
##                                               Yourbung Maning Leikai 
##                                                                  730 
##                                                Yourbung Mayai Leikai 
##                                                                  603 
##                                    Yumnam Khunou and Wangkhei khunou 
##                                                                 1021 
##                                           Yumnam Patlou Makha Leikai 
##                                                                  588 
##                 Yurembam Awang Leikai (Northern side of Power House) 
##                                                                  645 
##                 Yurembam Awang Leikai (Southern side of Power House) 
##                                                                  874 
##                                                Yurembam Makha Leikai 
##                                                                  653 
##                                               Yurembam Maning Leikai 
##                                                                  477
```
