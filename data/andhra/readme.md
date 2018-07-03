## Andhra

Basic descriptive statistics about the data. And sanity checks.


```r
andhra <- readr::read_csv("andhra.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_character(),
##   number = col_integer(),
##   age = col_integer(),
##   part_no = col_integer(),
##   year = col_integer(),
##   pin_code = col_integer(),
##   net_electors_male = col_integer(),
##   net_electors_female = col_integer(),
##   net_electors_third_gender = col_integer(),
##   net_electors_total = col_integer()
## )
```

```
## See spec(...) for full column specifications.
```

Number of rows:


```r
nrow(andhra)
```

```
## [1] 365908
```

Unique Values in Sex:


```r
# Unique values in sex
table(andhra$sex)
```

```
## 
## Female   Male 
## 182574 183281
```

Summary of Age:


```r
# Age
summary(andhra$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##    0.00   29.00   38.00   40.59   50.00  129.00       4
```

No. of characters in ID:

```r
# Length of ID
table(nchar(andhra$id))
```

```
## 
##     10     11     12     13     14 
## 286744      1      1   5395  73765
```

Number of characters in pin code:


```r
table(nchar(andhra$pin_code))
```

```
## 
##      1      6 
##   1184 359666
```


```r
# Net electors
sum(with(andhra, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 335997
```

```r
nrow(andhra)
```

```
## [1] 365908
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(andhra$elector_name))
```

```
## 
##     1     3     4     5     6     7     8     9    10    11    12    13 
##     5    32   360   908  2520  5506  7469  9320 11001 13682 18558 24226 
##    14    15    16    17    18    19    20    21    22    23    24    25 
## 27148 29549 31322 31636 30429 27242 22072 17888 13986 10747  8275  6198 
##    26    27    28    29    30    31    32    33    34    35    36    37 
##  4504  3306  2354  1704  1380  1025   597   395   236   175    80    45 
##    38    39 
##    22     6
```

```r
andhra[which(nchar(andhra$elector_name) < 4), "filename"]
```

```
## # A tibble: 37 x 1
##    filename       
##    <chr>          
##  1 S01A156P224.PDF
##  2 S01A156P224.PDF
##  3 S01A163P003.PDF
##  4 S01A163P003.PDF
##  5 S01A146P185.PDF
##  6 S01A109P148.PDF
##  7 S01A157P235.PDF
##  8 S01A156P151.PDF
##  9 S01A172P212.PDF
## 10 S01A146P215.PDF
## # ... with 27 more rows
```

Basic admin. units:

```r
table(andhra$police_station)
```

```
## 
##                                   .Narpala 
##                                        507 
##                       1 Town P.S., Nellore 
##                                        778 
##                      1 Town Police Station 
##                                       2132 
##           1 Town Police Station, Anantapur 
##                                       1490 
##                                 16/01/2017 
##                                      20785 
##                                    A.S.PET 
##                                        781 
##                          Adoni Taluka P.S. 
##                                       4380 
##                                    Akividu 
##                                       1170 
##                                  ALLAGADDA 
##                                       1198 
##                                     Almuru 
##                                        730 
##                            AMALAPURAM TOWN 
##                                        678 
##                                 Amarapuram 
##                                        817 
##                                 Amaravathi 
##                                        540 
##                                Amdguru P 5 
##                                       1300 
##                            Anakapalle Town 
##                                       1784 
##                          Ananthapur 1 Town 
##                                       1865 
##                          Ananthapur 2 Town 
##                                       1758 
##                                Atchemapata 
##                                        410 
##                               Atchutapuram 
##                                        670 
##                                     Athili 
##                                        730 
##                                      Atlur 
##                                        777 
##                                    atmakur 
##                                       1028 
##                                    ATMAKUR 
##                                        609 
##                                Atreyapuram 
##                                       1641 
##                                 Avanigadda 
##                                        507 
##                               B.N.KANDRIGA 
##                                       1806 
##                                     BADVEL 
##                                        496 
##                               Badvel Rural 
##                                        841 
##                              BANAGANAPALLI 
##                                       1107 
##                                 BANDAPURAM 
##                                        859 
##                        Bandaru Taluka P.S. 
##                                        594 
##                               Bapatla Town 
##                                       1166 
##                                 Bapulapadu 
##                                        699 
##                                    BATTILI 
##                                         85 
##                              Bestawaripeta 
##                                        350 
##                             Bheemunipatnam 
##                                       1528 
##                                  Bhimadole 
##                                        451 
##                                 Bhogapuram 
##                                        478 
##                                    Bobbili 
##                                       1955 
##                                     Bogolu 
##                                       1143 
##                                Bommana Hal 
##                                        840 
##                                 Bondapalli 
##                                        395 
##                             Bramhasamudram 
##                                       1017 
##                         Buchchireddy Palem 
##                                        626 
##                             BUDARAYAVALASA 
##                                        536 
##                          BukkaRayaSamudram 
##                                        918 
##                                      Burja 
##                                        767 
##                              Butchaiahpeta 
##                                        501 
##                   C.BELAGAL POLICE STATION 
##                                        819 
##                                   Chagallu 
##                                        561 
##                                   Chandole 
##                                        454 
##                              ChandralaPadu 
##                                       1032 
##                                    Chapadu 
##                                        890 
##                                   Chebrole 
##                                        486 
##                              Cheepurupalli 
##                                        428 
##                           Cheerala i-Tounu 
##                                       1348 
##                                   Chejarla 
##                                       1086 
##                                    Chennur 
##                                        707 
##                               Cherukupalli 
##                                        376 
##                      Chilakaluripeta Rural 
##                                        161 
##                                Chilmathuru 
##                                        672 
##                               ChinnaMandem 
##                                        758 
##                                   chintoor 
##                                        437 
##                   ChippaGiri Polis Station 
##                                        369 
##                                  ClassPadu 
##                                        339 
##                                     Cumbum 
##                                        313 
##                                  D.Hirehal 
##                                        723 
##                                   Dagdarti 
##                                        794 
##                                  Denduluru 
##                                        635 
##                                 DEVIPATNAM 
##                                       1008 
##                             Dharmajigudena 
##                                       1052 
##                                Dharmavaram 
##                                        547 
##                                        Don 
##                                        953 
##                                  DORNIPADU 
##                                        755 
##                                 DUMBRIGUDA 
##                                       1018 
##                                   Duttalur 
##                                        371 
##                           DvarakaThirumala 
##                                        845 
##                                   EdlaPadu 
##                                        611 
##                          Elamanchili Arban 
##                                       1850 
##                                Eluru Rural 
##                                       2337 
##                               Elvin Pettah 
##                                        408 
##                                      Epuru 
##                                        259 
##                                     Erpedu 
##                                        723 
##                             ErragondaPalem 
##                                        322 
##                               Firangipuram 
##                                        766 
##                                 G. Sigadam 
##                                        292 
##                      G.D.Nelluru Polis.Ste 
##                                        814 
##                                 G.K.Veedhi 
##                                       1646 
##                                 GADIVEMULA 
##                                        694 
##                                   Gajuwaka 
##                                       4029 
##                                   Galividu 
##                                        689 
##                               Gampalagudem 
##                                        751 
##                                GANAPAVARAM 
##                                        475 
##                            GangireddyPalli 
##                                        714 
##                                   Gantyada 
##                                        308 
##                                 Garladinne 
##                                        366 
##                                 Ghantasala 
##                                        285 
##                                   Giddalur 
##                                        749 
##                               Gidlavalleru 
##                                       1679 
##                                  Gokavaram 
##                                        418 
##                                 Gollapalem 
##                                       1007 
##                                 Gollaprolu 
##                                        648 
##                                      Gooty 
##                                        473 
##                               Gopalapatnam 
##                                       1495 
##                               GOPALAPATNAM 
##                                        819 
##                                   Gorantla 
##                                        515 
##                                 GUDI PALLA 
##                                        539 
##                                  GudiBanda 
##                                       1587 
##                       Gudivada Taluka P.S. 
##                                        331 
##                              Gudivada Town 
##                                        708 
##                                    GUDLURU 
##                                        183 
##                               Guduru Rural 
##                                       1167 
##                                      Gurla 
##                                       1237 
##                                GURRAMKONDA 
##                                       1027 
##                           HanumanthuniPadu 
##                                        693 
##                                Hirmandalmu 
##                                        256 
##                            I Town Guntakal 
##                                       2549 
##                     i Town P.S. Vijayawada 
##                                       6499 
##                                  Ichapuram 
##                                       1646 
##                                    ii-Town 
##                                       4717 
##                     II TOWN POLICE STATION 
##                                       1863 
##                                 Indrapalem 
##                                        461 
##                            Indukuru Pettah 
##                                        670 
##                                     Inkole 
##                                       1114 
##                                     Involu 
##                                        809 
##                                 iPolavaram 
##                                        879 
##                                 Iragavaram 
##                                        870 
##                                Jaggaiahpet 
##                                       1013 
##                                 Jaggampeta 
##                                        389 
##                              Jammalamadugu 
##                                       1376 
##                           Jangareddigudena 
##                                       1503 
##                                Jarugumalli 
##                                        455 
##                                 K.KOTAPADU 
##                                       1518 
##                              KADAPA Taluka 
##                                       2232 
##                               Kadiri Urban 
##                                        336 
##                                    Kadiyam 
##                                        889 
##                     Kaikaluru Arbana P.Es. 
##                                        846 
##                                   KAKINADA 
##                                       2378 
##                                   Kaligiri 
##                                        229 
##                                      Kalla 
##                                        784 
##                                Kalyanadurg 
##                                       1387 
##                                Kamalapuram 
##                                        488 
##                                   Kambadur 
##                                       1975 
##                              KANAGANAPALLI 
##                                       1609 
##                             KanchikaCharla 
##                                        782 
##                                   Kanchili 
##                                        461 
##                             KANDUKUR URBAN 
##                                        282 
##                                    Kanekal 
##                                       1058 
##                                  Kankipadu 
##                                       1088 
##                                 Karamchedu 
##                                        850 
##                                  Karampudi 
##                                        441 
##                                 Kashinkota 
##                                       1553 
##                                  KASIBUGGA 
##                                       1027 
##                                 KatreNikon 
##                                        636 
##                              Kavali 1-Town 
##                                       1530 
##                                     Kaviti 
##                                        171 
##                                    Kazipet 
##                                        924 
##                     Kodumuru Polis Station 
##                                        394 
##                                  Kollipara 
##                                        737 
##                                    Kolluru 
##                                        526 
##                                   Komarada 
##                                        963 
##                                 Kondapuram 
##                                        630 
##                                  Korukonda 
##                                        885 
##                       Kosigi Polis Station 
##                                        276 
##                                 Kotbommali 
##                                       1077 
##                                  Kothakota 
##                                        944 
##                                 Kothapalli 
##                                        503 
##                                  Kothapeta 
##                                       1320 
##                                Kothavalasa 
##                                        928 
##                                    Kothuru 
##                                        753 
##                                 Kotvuratla 
##                                        257 
##                                      Kovur 
##                                        697 
##                               KOYYALAGUDEM 
##                                        554 
##                                     Kuderu 
##                                        631 
##                                   Kundurpi 
##                                       1549 
##                     KURNOOL POLICE STATION 
##                                       1253 
##                    Kurnoolu 4Va Tounu P.S. 
##                                       2524 
##                                  Kurupam-i 
##                                       1509 
##                                 Madakasira 
##                                       3256 
##                    Mahanandi Polis Station 
##                                        648 
##                                Makwarpalem 
##                                        491 
##                                      Mampa 
##                                       1146 
##                              mangasamudram 
##                                        701 
##                 MANTRALAYAM POLICE STATION 
##                                        543 
##                                MAREDUMILLI 
##                                         76 
##                                 Markapuram 
##                                       1099 
##                                   Maruturu 
##                                        375 
##                                Medikonduru 
##                                       1160 
##                                 Meliaputti 
##                                        647 
##                    Miduturu Police statioN 
##                                       1612 
##                                  Mudigubba 
##                                       2322 
##                               Mummidivaram 
##                                       1546 
##                                 Munagapaka 
##                                        801 
##                                 Mundlamuru 
##                                        453 
##                                  Muthukuru 
##                                       1826 
##                                    Mydukur 
##                                        335 
##                         Naarasaraopet Town 
##                                       1492 
##                                   Nadendla 
##                                        561 
##                                     Nagari 
##                                       1210 
##                                Nagayalanka 
##                                        491 
##                                   NAIDUPET 
##                                        481 
##                                Nakkapallii 
##                                        866 
##                                   Nandalur 
##                                        643 
##                                  Nandigamu 
##                                        754 
##                                  Nandivada 
##                                        713 
##                        NarasaRPettah Rural 
##                                        914 
##               Narayanavanam Police Station 
##                                       1048 
##                                Narsannapet 
##                                       2040 
##                           Narsipatnam Town 
##                                       1374 
##                                   Natwaram 
##                                        653 
##                                 Nellimarla 
##                                       1309 
##                                  NELLIPAKA 
##                                        370 
##                                     NINDRA 
##                                       1125 
##          No-1 town police station, Nellore 
##                                       2039 
##                         Nuzvid Rurala P.S. 
##                                        485 
##                                 OLD GUNTUR 
##                                       3365 
##               Ongole iTounu Polisu Station 
##                                        629 
##                   Orvakallu police Station 
##                                       1549 
##                               P.Gannavaram 
##                                       1675 
##                                 Pachipenta 
##                                       1662 
##                                 Palakoderu 
##                                       1968 
##                                  PALAMANER 
##                                        903 
##                                   Palkonda 
##                                        236 
##                 PallSamudram Polis Steshan 
##                                       1463 
##                                    Pamarru 
##                                        654 
##                   PamulaPadu Polis Station 
##                                        476 
##                                     Pamuru 
##                                        184 
##                                   Parchuru 
##                                        269 
##                                     Parigi 
##                                        824 
##                              Parvathipuram 
##                                        499 
##                                Pata Guntur 
##                                       2873 
##                                Pathapatnam 
##                                       1692 
##                                pathiikonda 
##                                        554 
##                               PEDAGANTYADA 
##                                       1830 
##                                 PedaKakani 
##                                        627 
##                                   Pedapadu 
##                                        195 
##                                   Pedavegi 
##                                        171 
##                             Peddapappuruvu 
##                                        266 
##                                 Peddapuram 
##                                       2168 
##                                 Peddarvidu 
##                                        218 
##                                  Penagalur 
##                                        726 
##                                 Penamaluru 
##                                       1435 
##                                  Pentapadu 
##                                        769 
##                            Penuganchiprolu 
##                                        368 
##                                  PENUGONDA 
##                                        390 
##                                 Penumantra 
##                                        707 
##                                   Peravali 
##                                        809 
##                                Piduguralla 
##                                        678 
##                        Piler Polis.Steshan 
##                                        810 
##                                  Pitapuram 
##                                        964 
##                                    Polakii 
##                                        309 
##                                    PONDURU 
##                                       1080 
##                                Ponnur Town 
##                                        753 
##                                 Prathipadu 
##                                        673 
##                           Prodduturu Rural 
##                                       2133 
##                                 Pulevendla 
##                                        771 
##                                  Pullampet 
##                                        423 
##                                Puspatirega 
##                                       1323 
##                                    PYAPILI 
##                                        578 
##                        Rajahmundry -i Town 
##                                       4552 
##                       Rajahmundry Pattanam 
##                                       6303 
##                                      Rajam 
##                                        894 
##                                   Rajampet 
##                                       1122 
##                            Ramabhadrapuram 
##                                        773 
##                           Ramachandrapuram 
##                                       1061 
##                                 Ramakuppam 
##                                       2028 
##                                   RAPTHADU 
##                                        861 
##                                Ravulapalem 
##                                       1048 
##                                 Rayadurgam 
##                                       1337 
##                                     Razole 
##                                        906 
##                       Regidi Amadalavalasa 
##                                        494 
##                              Rentachintala 
##                                        691 
##                                    Repalle 
##                                        389 
##                                     Roddam 
##                                       1356 
## Roll Identification: Basic roll of Special 
##                                       1309 
##                                  Rolugunta 
##                                        592 
##                                 RUDRAVARAM 
##                                        270 
##                       S.Ar.Puram Polis.Ste 
##                                        614 
##                                     S.KOTA 
##                                       2575 
##                                 Sabbavaram 
##                                        652 
##                                     Saluru 
##                                       1023 
##                               Samisragudem 
##                                       3130 
##                                  SANJAMALA 
##                                        749 
##                               Santabommali 
##                                        305 
##                              Santhamagalur 
##                                       1384 
##                                 Sarpavaram 
##                                       1573 
##                                   Sarvkota 
##                                        901 
##                               Sattanapalli 
##                                       1435 
##                   Satyavedu Police Station 
##                                        759 
##                                    Siddota 
##                                       1465 
##                              Simhadripuram 
##                                        712 
##                                Singanamala 
##                                        884 
##                             Singarayakonda 
##                                       1496 
##                                SRIHARIKOTA 
##                                        731 
##                                 Srikakulam 
##                                       1298 
##                   Sundipenta Polis Station 
##                                        877 
##                                  Sydapuram 
##                                        993 
##                               T SanduPalli 
##                                        523 
##                                  Tadepalli 
##                                       1019 
##                      Tadepalligudena Rural 
##                                       2904 
##                              TadiwaripallI 
##                                        607 
##   Tadparthi Rural and Town Police Stations 
##                                        628 
##                                  Tanguturu 
##                                        578 
##                               Tanuku Rural 
##                                        417 
##                              TAVANAM PALLE 
##                                        434 
##                                   Tenali-1 
##                                       2430 
##          Thirumala One Town Police Station 
##                                       1713 
##                               Thotlavallur 
##                                        638 
##                              Tripurantakam 
##                                        224 
##                                    Tuni -U 
##                                       2030 
##                               U.Kothapalli 
##                                        796 
##                                       Undi 
##                                        878 
##                                   Unguturu 
##                                        876 
##                                     Uyyuru 
##                                       1356 
##                                     V.Coat 
##                                        808 
##                            Vajrapu Kothuru 
##                                       2377 
##                                 Vallampudi 
##                                        377 
##                             VARADAIAHPALEM 
##                                        258 
##                               VEERAGHATTAM 
##                                        103 
##                                 Veligandla 
##                                        722 
##                              Venkatachalam 
##                                       1432 
##                                venkatagiri 
##                                        761 
##                                  Vidavalur 
##                                        479 
##                  VijayaPuram Polis.Steshan 
##                                        438 
##                           Vijayapuri South 
##                                       2296 
##                         Vijayvgaram i Touv 
##                                       3642 
##                                  Vinukonda 
##                                       2557 
##                                Vissannapet 
##                                        547 
##                                Vontimamidi 
##                                       1547 
##                                  Yallanuru 
##                                        142 
##              Yemmiganur (T) Police Station 
##                                       1290
```

```r
table(andhra$mandal)
```

```
## 
##                   178                   206               A.S.Pet 
##                   607                   702                   781 
##              Achampet                 Adoni                  Agli 
##                   410                  4380                   918 
##               Akividu             Allagadda                Almuru 
##                  1170                  1198                   730 
##            AMALAPURAM            Amarapuram            Amaravathi 
##                   678                   817                   540 
##               Amdguru            Anakapalle           Anandapuram 
##                  1300                  1784                   779 
##           AnantaPuram          Atchutapuram                Athili 
##                  1490                   670                   730 
##                 Atlur              Atmakuru           Atreyapuram 
##                   777                  1637                  1641 
##            Avanigadda           B.Kothakota          B.N.Kandriga 
##                   310                   819                  1806 
##                BADVEL           Balayapalli                Bamini 
##                   496                  1877                    85 
##         BANAGANAPALLI          BangaruPalem               Bapatla 
##                  1107                  1416                  1166 
##            Bapulapadu        BarhamSamudram         BestawaripetA 
##                   699                  1017                   350 
##        Bheemunipatnam             Bhimadole            Bhimavaram 
##                  1528                   451                  2703 
##               Bobbili             BogaPuram                Bogolu 
##                  1955                   478                  1143 
##            Bommanahal            Bondapalli                 Burja 
##                   840                   395                   767 
##         Butchaiahpeta      Butchireddipalem             C.Belagal 
##                   501                   626                   819 
##              Chagallu         Chandarlapadu               Chapadu 
##                   561                  1032                   890 
##              Chebrole         Cheepurupalli              Cheerala 
##                   486                   428                  1348 
##              Chejarla               Chennur          Cherukupalli 
##                  1086                   707                   376 
##       Chilakaluripeta            Chillakuru           Chilmathuru 
##                   161                   194                   672 
##         Chinna Mandem              CHINTOOR            ChippaGiri 
##                   758                   437                   369 
##              Chittoor           Chowdepalle                Cumbum 
##                  1127                   614                   313 
##             D.Hirehal              Dagdarti             Denduluru 
##                   723                   794                   635 
##           Devarapalle            DEVIPATNAM           Dharmavaram 
##                   859                  1008                   547 
##                   Don             Dornipadu           Dumbiriguda 
##                   953                   755                  1018 
##              Duttalur       Dwarakatirumala              Edlapadu 
##                   371                   845                   611 
##          Ellamanchili                 Eluru                 Epuru 
##                  1850                  2337                   259 
##          Firangipuram              G.Sigdam             GadiEmula 
##                   766                   292                   694 
##              Gajuwaka              Galividu          Gampalagudem 
##                  4029                   689                   751 
##           Ganapavaram           GandlaPenta            Gannavaram 
##                   475                   380                   971 
##              Gantyada            GarlaDinne            Ghantasala 
##                   308                   366                   285 
##              Giddalur          Gidlavalleru             Gokavaram 
##                   749                  1679                   418 
##            Gollaprolu                 Gooty           Gopalapuram 
##                   648                   473                   921 
##             Gopavaram              Gorantla      Gudenkothaveedhi 
##                   841                   515                  1646 
##             GudiBanda              Gudipala              Gudivada 
##                  1587                   539                   708 
##                Gudlur                Guduru            Guntakallu 
##                   183                  1167                  2549 
##                Guntur                 Gurla           Gurramkonda 
##                  6238                  1237                  1027 
##              H.M.Padu            Hindupuram           Hirmandalam 
##                   693                  1865                   256 
##             Hukumpeta           I.Polavaram             Ichapuram 
##                  1509                   879                  1646 
##            Indukurpet                Inkole            Iragavaram 
##                   670                  1114                   870 
##                 Irala           Jaggaiahpet            Jaggampeta 
##                   699                  1013                   389 
##         Jammalamadugu       Jangareddigudem           Jarugumalli 
##                  1376                  1503                   455 
##            K.KOTAPADU                KADAPA                Kadiri 
##                  1518                  2232                   336 
##               Kadiyam             Kaikaluru        Kakinada Rural 
##                   889                   846                  1573 
##        Kakinada Urban            KALASAPADU              Kaligiri 
##                  2378                   339                   229 
##                 Kalla                KALLUR          Kalyandurgam 
##                   784                  2524                  1387 
##           Kamalapuram              Kambadur        KanchikaCharla 
##                   488                  1975                   782 
##              Kanchili              Kandukur               Kanekal 
##                   461                   282                  1058 
##         Kangana Palli             Kankipadu      Kapileswarapuram 
##                  1609                  1088                   654 
##            Karamchedu             Karampudi            Kashinkota 
##                   850                   441                  1553 
##           Katrenikona                Kavali                Kaviti 
##                   636                  1530                   171 
##               Kazipet              Kodumuru             Kollipara 
##                   924                   394                   737 
##               Kolluru            Kondapuram             Korukonda 
##                   526                   630                   885 
##                Kosigi          Kotabommaali            Kotauratla 
##                   276                  1077                   257 
##            Kothapalle            Kothapalli             Kothapeta 
##                   503                   796                  1320 
##           Kothavalasa                Kothur                 Kovur 
##                   928                   753                   697 
##          Koyyalagudem               Koyyuru                Kuderu 
##                   554                  1146                   631 
##              Kundurpi               KURNOOL            Lingapalem 
##                  1549                  1253                  1052 
##              Macharla            Machavaram         Machilipatnam 
##                  2296                   505                   594 
##             Madkshira             Mahanandi         Makavarapalem 
##                  3256                   648                   491 
##           Mantralayam           MAREDUMILLI            Markapuram 
##                   543                    76                  1099 
##              Maruturu           Medikonduru            Meliaputti 
##                   375                  1160                   647 
##         MERAKAMUDIDAM              Miduturu             Mogalturu 
##                   536                  1612                  1009 
##              Mopidevi             Mudigubba          Mummidivaram 
##                   507                  2322                  1546 
##            Munagapaka        Munchingiputtu            Mundlamuru 
##                   801                   963                   453 
##             Muthukuru               Mydukur              N.G.Padu 
##                  1826                   335                   629 
##              Nadendla                NAGARI           Nagayalanka 
##                   561                  1210                   491 
##              Naidupet           Nakarikallu            Nakkapalli 
##                   481                   914                   866 
##              Nandalur            Nandavaram              Nandigam 
##                   643                   818                   754 
##             Nandivada        NaraayanaVanam         Narasannapeta 
##                   713                  1048                  2040 
##          Narasaraopet               Narpala           Narsipatnam 
##                  1492                   507                  1374 
##            Nathavaram            Nellimarla             NELLIPAKA 
##                   653                  1309                   370 
##               Nellore            Nidadavole                Nindra 
##                  2817                  3130                  1125 
##              Nuzendla                Nuzvid     Obuldewar Cheruvu 
##                   809                   485                   437 
##                Ongole             Orvakallu          P.Gannavaram 
##                  2132                  1549                  1675 
##            Pachipenta            Palakoderu             Palakonda 
##                  1662                   498                   236 
##                Palasa          Palasamudram              Palmneru 
##                  1027                  1463                   903 
##            PamulaPadu                 Pamur              Paravada 
##                   476                   184                  1337 
##               PARCHUR                Parigi         Parvathipuram 
##                   269                   824                   499 
##           Pathapatnam            Pathikonda            Pedabayalu 
##                  1692                   554                   408 
##         Pedagantiyada            PedaKakani              Pedapadu 
##                  1830                   627                   195 
##          Pedaparupudi              Pedavegi          Peddamandyam 
##                   331                   171                   635 
##          Peddapappuru            Peddapuram          Peddaraveedu 
##                   266                  2168                   218 
##             Penagalur            Penamaluru             Pendurthi 
##                   726                  1435                  1495 
##             Pentapadu       Penuganchiprolu             Penugonda 
##                   769                   368                   390 
##            Penumantra              Peravali           Piduguralla 
##                   707                   809                   678 
##                Pileru       Pittalvanipalem            Podalakuru 
##                   810                   454                  1240 
##                Polaki               Ponduru                Ponnur 
##                   309                  1080                   753 
##            Prathipadu            Prodduturu            Pulivendla 
##                   673                  2133                   771 
##             Pullampet              Punganur           Puspatirega 
##                   423                   814                   544 
##               Pyapili           Rajahmundry     Rajahmundry Rural 
##                   578                  4552                  6303 
##                 Rajam              Rajampet       RamabhadraPuram 
##                   894                  1122                   773 
##            Ramakuppam       Ramchandrapuram             Rangampet 
##                  2028                  1061                   964 
##               Raptadu             Ravikmtam           Ravulapalem 
##                   861                   944                  1048 
##            Rayadurgam             Rayavaram                Razole 
##                  1337                  1007                   906 
##  Regidi Amadalavalasa         Rentachintala               Repalle 
##                   494                   691                   389 
##                Roddam             Rolugunta           Rompicharla 
##                  1356                   592                  1179 
##           Rudhravaram                S.KOTA            Sabbavaram 
##                   270                  2575                   652 
##                Saluru              Samalkot             SANJAMALA 
##                  1023                   461                   749 
##         Santabommaali         Santhamagalur              Sarvkota 
##                   305                  1384                   901 
##          Sattanapalli             Satyavedu               Sidhout 
##                  1435                   759                  1465 
##         Simhadripuram           Singanamala        Singarayakonda 
##                   712                   884                  1496 
##            Srikakulam             SRISAILAM            Sullurupet 
##                  1298                   877                   731 
##            Sundupalli             Sydapuram             Tadepalli 
##                   523                   993                  1019 
##        Tadepalligudem             Tadiparti             Talzhrevu 
##                  2904                   628                   876 
##             Tanguturu                Tanuku             Tarlupadu 
##                   578                   417                   607 
##                Tenali         Thavanampalli    Thirupathi (Urban) 
##                  2430                   434                  1713 
##          Thotlavallur             Tondanagi         Tripurantakam 
##                   638                  1547                   224 
##                  Tuni                  Undi          Undrajavaram 
##                  2030                   878                   355 
##              Unguturu            Uravakonda                Uyyuru 
##                   876                  1758                  1356 
##                V.Coat         VajrapuKothur                Vakadu 
##                   808                  2377                   532 
##         Vardaiahpalem          Veeraghattam   VEERAPUNAYANI PALLE 
##                   258                   103                   714 
##          Veeravasaram            Veligandla         Venkatachalam 
##                  1968                   722                  1432 
##           Venkatagiri                Vepada             Vidavalur 
##                   761                   377                   479 
##           VijayaPuram      Vijayawada Urban             Vinukonda 
##                   438                  6499                  2557 
## VISAKHAPATNAM (RURAL) VISAKHAPATNAM (URBAN)   Visakhapatnam Arban 
##                   819                  1863                  4717 
##  Vishakhaptnam, Rural           Vissannapet          Vizianagaram 
##                   584                   547                  3058 
##                Yadmri            Yallanooru            Yemmiganur 
##                   648                   142                  1290 
##               Yerpedu       Yerragondapalem 
##                   723                   322
```

```r
table(andhra$district)
```

```
## 
##     Anantapur      Chittoor East Godavari         Eluru        Guntur 
##         39791         24492         42549           976         33339 
##        Kadapa       Krishna       Kurnool       Nellore      Prakasam 
##         20483         25296         26217         23087         17550 
##    Srikakulam Visakhapatnam  Vizianagaram West Godavari 
##         19665         40177         18085         32892
```

```r
table(andhra$main_town)
```

```
## 
##               ACHUTAPURAM                  Achwaram 
##                       445                       627 
##                     Adivi                     Adoni 
##                       392                      3748 
##                Aganampudi                  Ainparru 
##                      1003                       456 
##                   Akividu          AkkiAreddy Palem 
##                      1170                       409 
##              Akurajupalli               Alaganipadu 
##                       505                       479 
##                Amalapuram                  Amapuram 
##                      1028                       461 
##                    Ambada                   Amdguru 
##                       219                      1300 
##                Anakapalle               ANANDAPURAM 
##                      1191                       455 
##    Anantapur Municipaltiy            AnantaSamudram 
##                      1490                       423 
##                 Annavaram                    Anooru 
##                       673                       736 
##             AnumaSamudram               Apparaopeta 
##                       781                       759 
##                     ARAKU                 Arikitota 
##                      1018                       773 
##                   Aripaka                 Arugolanu 
##                       652                       845 
##                  Athaluru                  Atmakuru 
##                       540                       609 
##           Baduguvanilanka               Balayapalli 
##                       730                       840 
##                 Ballipadu              Bapatla East 
##                       730                       774 
##                Bapulapadu                 BATUPURAM 
##                       699                       679 
##         BAYYAPPAGARIPALLE Bhageerdhipuram Agraharam 
##                       819                       178 
##           BHEEMAGANIPALLI                BHIMAVARAM 
##                       814                      1483 
##                   BHOGOLU              Binginapalli 
##                       608                       501 
##               BIYYALAPETA                   Bobbili 
##                       987                      1426 
##                    Boddam        BODUMALLUVARIPALLE 
##                       625                       458 
##                    Bogolu               Boksampalli 
##                      1143                       518 
##                   Bommuru         Brahma sameadhyam 
##                      1973                       636 
##      BUCCHINAIDU KANDRIGA                   Budithi 
##                      1139                       901 
##         Budtanpallirajeru                    Burada 
##                       243                       275 
##           BURIDIKANCHARAM                     Burja 
##                       618                       767 
##              Challagundla           Chandaka Cherla 
##                       536                       885 
##              Chandrupatla               Chatlamitta 
##                       547                       218 
##          chebiyyam valasa             CHEEMALAPALLI 
##                       103                       758 
##             Cheepurupalli                  Cheerala 
##                       426                       890 
##             CherukuCherla                 Cherukuru 
##                       788                       269 
##               ChettuPalli                   Chidika 
##                       892                       297 
##                Chiiahpadu                  Chikvolu 
##                       482                       993 
##               Chimlapalli            Chinna Musturu 
##                       670                       476 
##              Chinnachowku          ChinnaRangapuram 
##                       325                       771 
##                CHIPPAGIRI              Chippalmdugu 
##                       369                       336 
## Chiruvolu Lanka Dakshinam                CHITHAPARA 
##                       310                       539 
##                   Colluru                    Cumbum 
##                       526                       313 
##                 D.Hirehal                  Dagdarti 
##                       723                       794 
##          Dakshene Valluru               DAMANAPALLI 
##                       638                       630 
##              Damaramadugu             Demaketapalli 
##                       626                       672 
##               Devarapalle         DEVINENIVARIGUDEM 
##                      1048                       404 
##                 Dondapudi                 Dornipadu 
##                       921                       755 
##              Dowlaiswaram                     Duvva 
##                      1269                       417 
##                 Dwarapudi          Edda Chintakunta 
##                       807                      1198 
##          Edda NagulaVaram              Edda Pappuru 
##                       580                       266 
##             EddaCherukuru   Eguvgangampalli-G.Palli 
##                       778                       515 
##                 ELAKATURU              Ellamanchili 
##                       868                       553 
##          Ellamanchili P.T                   ELLUTLA 
##                       632                       645 
##                     Eluru                 EluruPadu 
##                      1422                       784 
##      EnamalaKuduru Arbana                 Endabadra 
##                      1435                       963 
##            Erramnenipalem                Es.R.Puram 
##                       523                       737 
##             G. Veerapuram           GADDAMGARIPALLI 
##                       503                       614 
##              Gajjalakonda                  Gajuwaka 
##                       519                       585 
##          gallavandlapalli               GANDIGUNDAM 
##                       305                       324 
##                Gangavaram              GANNERUPUTTU 
##                       578                       601 
##               Garugupalli               Gavaravaram 
##                       689                       366 
##               GAVARAVARAM           Gaviniwaripalem 
##                       915                       521 
##                Ghantasala                  Giddalur 
##                       285                      1498 
##              Gidlavalleru                Goddumarri 
##                      1137                       142 
##                Godugunuru                 Gokavaram 
##                       496                       418 
##                     Golla              GOPALAPATNAM 
##                       576                       819 
##         GopalVenkatapuram                Govindinne 
##                       236                       469 
##             Gowridevipeta                 GudiBanda 
##                       370                      1062 
##            Gudivada Urban                Gundepalli 
##                       708                       259 
##            GUNDRAJUKUPPAM                Gundugolnu 
##                       636                       451 
##                Gunjepalli   Guntakallu Munisipaliti 
##                      1423                      1617 
##                    Guntur               Gurijepalli 
##                      6238                       322 
##          Guruvinnayudupet                Guttikonda 
##                       715                       678 
##             H. Nidamannur               Hanakanahal 
##                       629                       617 
##              HareSamudram                 Hemavathi 
##                      1608                       817 
##   Hindupuram Munisipaliti              HossainPuram 
##                      1023                       498 
##                 Hukumpeta                  Hulikera 
##                       860                       441 
##                 ICHAPURAM            Indukurpet -ii 
##                      1189                       670 
##                    Ipperu                Ipurupalem 
##                       631                       458 
##                Iragavaram         Jaggaiahpet Urban 
##                       414                      1013 
##              Jambugumpala            Jamidintakurru 
##                      1045                       331 
##             Jammalamadugu             JEELUGULAPUTU 
##                       581                       908 
##                Jonnalpadu             Kadapa Shahar 
##                       140                       935 
##               Kakaraparru                  Kakinada 
##                       809                      2378 
##          KALAMANAIDU PETA             KALAVALAPALLI 
##                       759                       561 
##                KALICHERLA                   kalluru 
##                       635                      1191 
##              Kalyandurgam               Kamalapuram 
##                       811                       564 
##                  Kambadur                   Kamkuru 
##                      1975                       640 
##            KanchikaCharla                Kannepalli 
##                       782                      1017 
##                 Kantepudi              Kanumlopalli 
##                       602                       608 
##                  Kanupuru                  Kapuluru 
##                      1432                       481 
##                 Karuchola                Karumanchi 
##                       611                       578 
##                 Kasimkota           Kaswareddipalem 
##                       764                       731 
##                    Kateru               Katrenipadu 
##                       292                       906 
##                 Kattamuru                Kattupalem 
##                       770                       630 
##                   Kautram                    Kavali 
##                       542                      1530 
##                    Kavuru               KEELA GARAN 
##                       376                       526 
##               Keera manda              kesana kurru 
##                       768                       879 
##                     Kesli                Khajipalem 
##                       947                       454 
##                  Kodumuru               Kokkilgadda 
##                       394                       507 
##                 Kolavennu                Kollikulla 
##                      1088                       368 
##               Komarlatada              Kona Farestu 
##                      1054                       611 
##                   Konanki           KONDALA CHERUVU 
##                       375                       522 
##                Kondapuram              Konganapalle 
##                       532                       963 
##                  KONGATAM                    Koniki 
##                       525                       536 
##                Koratmaddi                 Korukonda 
##                       694                       885 
##                 KORUKONDA                Kothalanka 
##                       620                       928 
##                Kothapalli                 KOTHAPETA 
##                       537                      1320 
##               Kothavalasa         KOTHULA GOKAVARAM 
##                       928                       444 
##                   Kothuru              KOYYALAGUDEM 
##                       898                       475 
##               Kunkalgunta               Kunkalmarru 
##                       378                       850 
## kuravapalli/gorantlapalli             Kurmannapalem 
##                       329                       828 
##                   Kurnool               KUSARLAPUDI 
##                      1253                       592 
##                     Labba               Lakkamdiddi 
##                       753                       524 
##                LAKKAVARAM  lakshmi reddy gari palli 
##                       740                       299 
##                   Lingala                     Lolla 
##                       751                       877 
##          LOSARI GUTLAPADU             M.Nagulapalle 
##                      1220                       845 
##                 M.R.PALLI                  Macharla 
##                      1000                       810 
##                MACHAVARAM       Machilipatnam Urban 
##                       512                       594 
##         Madakalavaripalle        MADANA GOPALAPURAM 
##                       841                       282 
##            Maddiwarigondi         Madhi reddi palle 
##                       380                       648 
##               Madhuravada                 Madkshira 
##                       584                       763 
##                 Mahanandi               Makwarpalem 
##                       648                       491 
##                Malkvemula               MallaKaluva 
##                       899                       547 
##       Mallubhupala Patnam                 Malynooru 
##                       653                       504 
##                  Mamuduru               Manchikallu 
##                       894                       691 
##                 Mandigiri                 Manendram 
##                       632                      1065 
##                    Maniga                MarriGunta 
##                        85                       630 
##                 MARRIPADU               MARRIVALASA 
##                       382                       742 
##                  Marupaka                 MATAVALAM 
##                       944                       408 
##                MATSYAPURI                  Melchuru 
##                       708                       397 
##                 Merikpudi                  Mocharla 
##                       766                       183 
##                      Moda                 Mogalluru 
##                       824                       224 
##                 Muchindra               Mudhi Golam 
##                       457                       699 
##                  mudivedu                Muktapuram 
##                       426                       689 
##                   Mulapet              Mummidivaram 
##                       259                       618 
##             MunagalaPalle                  Munganda 
##                       519                      1675 
##                Muntimdugu    Murakambattu Agraharam 
##                       366                       701 
##                  MURAPAKA                  Mutukuru 
##                       308                       525 
##               N. PALAGIRI                 Nadipalli 
##                       714                       544 
##                  Nadupuru                 Nadupuru. 
##                       754                       901 
##              Nagarajupeta                    NAGARI 
##                       972                       574 
##                 NakkaPeta               Nalla Billy 
##                       292                       377 
##                Nallamilli        Nalli chetti palli 
##                       678                       434 
##                Nandablaga                  Nandalur 
##                       269                       643 
##              NandanaVanam                 NANDIVADA 
##                       488                       371 
##                  Nannooru           NaraindraPatnam 
##                       903                       389 
##             NarasaRPettah                Narmalpadu 
##                      1492                       441 
##                   Narpala                Narsambudi 
##                       507                       918 
##               Narsannapet                 Nelagonda 
##                       987                       474 
##                  NELATURU                Nellimarla 
##                       654                       892 
##                   Nellore                    Nemali 
##                      2039                       243 
##                   Nernoor                Nidadavole 
##                       192                      1137 
##              Nuzvid Urban                     Oduru 
##                       271                       707 
##                   OmPalli                    Ompolu 
##                       152                       271 
##                    Ongole                 Orvakallu 
##                      1590                       410 
##                    PADIRI            Padmara Guduru 
##                       257                       479 
##                 PaidiPadu                Paidipalem 
##                       455                       712 
##               Painampuram                    Pakala 
##                       946                       995 
##                 PALAMANER              PALASAMUDRAM 
##                       903                      1055 
##                    Paleru                 Pallamala 
##                       648                       194 
##                 Pallantla           PALLAPU DUNGADA 
##                       859                       476 
##                 Pallavolu    Pallivuru, Sangaruvani 
##                       408                       644 
##                 Pandikona                 PandiPadu 
##                       554                       654 
##                   Panduru               Papayapalli 
##                       257                       350 
##                   Para Di              Parannavlasa 
##                       529                      1023 
##                     Parla                PARLAPALLI 
##                       679                       667 
##                Pasalapudi                 Paswemula 
##                       355                       991 
##               PATHAARKADU               Pathapatnam 
##                       438                      1247 
##                    Paturu                   Patvala 
##                       697                       876 
##             Pedagantiyada             Pedakancherla 
##                      1667                       583 
##            Pedakandepalli              Pedamakwaram 
##                       755                       581 
##             PedaNadipalli                 PEDAPUTTU 
##                       428                       408 
##                  PedaVegi         PEDDABARENE PALLI 
##                       171                       283 
##           Peddagollapalli                  Peddamdi 
##                       205                       647 
##                Peddapuram               Peddatungam 
##                       662                       165 
##                  Peddoddi                Penumallam 
##                       473                       723 
##                Perecherla                 PerupaleM 
##                      1160                      1009 
##               Pidtapoluru                    PILERU 
##                       880                       352 
##                PODADURTHY                Podalakuru 
##                       488                      1240 
##                      Poli                    Polkal 
##                       795                       819 
##             Ponakaladinne                  Pondalur 
##                       818                       726 
##                 Ponguturu                Ponnathota 
##                       188                       795 
##                    Ponnur                Potumeraka 
##                       753                       389 
##              PRAGADAVARAM                Prathipadu 
##                       465                      1442 
##                 PRODDUTUR                   PullurU 
##                      2133                       924 
##                 PunnValli           Purushottapuram 
##                       513                       784 
##                   Pyapili              R NAGULAVRAM 
##                       578                       270 
##                 R.V. Ngar               RaajaPettah 
##                       747                       161 
##                Rachepalli             Rachwaripalli 
##                       884                       371 
##             Raghunadpuram            Rahimana Puram 
##                       171                       309 
##               Rajahmundry      Rajahmundry pattanam 
##                      4552                      1002 
##                  Rajavolu               Ramanapalli 
##                       907                       707 
##              Ramaraogudem                  RAMPURAM 
##                       635                       418 
##                  Rapthadu                Ravicharla 
##                       861                       214 
##                    Rawada   RayaDurgam Munisipaliti 
##                       478                      1337 
##                 Regupalem            Rekhavanipalem 
##                       588                       920 
##                Rellivlasa          Renimakula Palli 
##                       256                       726 
##                    Roddam                Rudravaram 
##                       838                       476 
##                     Ryali                S. MYDUKUR 
##                       764                       335 
##            S.Venkatapuram            SadanandaPuram 
##                       777                       336 
##              Samarla Coat            SankuRatriPadu 
##                       461                       561 
##              Santebidnoor           Sarabhannapalem 
##                       842                       565 
##                 Saripalli                SarpaVaram 
##                       417                       901 
##              SATTENAPALLI           Sawarlingupuram 
##                       833                       336 
##            Shingannapalem          Siddamurthypalli 
##                       453                       339 
##                Siddavatam                SIDHANTHAM 
##                       857                       390 
##               Sileru U.I.               Singanhalli 
##                       899                       840 
##                Srikakulam            srinivasapuram 
##                      1298                        94 
##               SRUNGAVARAM          Srungavarapukoda 
##                       776                       653 
##    State - Andhra Pradesh       steelplant township 
##                      1309                       613 
##                Suddagudem                    Suguru 
##                       437                       543 
##                Sundipenta             T. Kothapalem 
##                       877                       491 
##                 Tadepalli            Tadepalligudem 
##                      1019                       471 
##                 Tadimalla                  Taduvayi 
##                       999                       763 
##            Tagarapuvalasa              Talarlapalli 
##                       608                       809 
##                 Talmudipi                 Tamrpalli 
##                       824                      1053 
##              Tangedumalli               Tarigoppula 
##                       166                       876 
##                Tatiparthi                    Tenali 
##                       648                      2430 
##             Thakkellapadu                    Thanam 
##                       627                       911 
##               Thimmapuram              Thogarakunta 
##                       458                       920 
##               THOKALAPUDI                  THONDURU 
##                      1260                       258 
##           Timmarajupalena                  TIRUPATI 
##                       994                       713 
##                 Tondanagi       Totada Sirasu palli 
##                       936                       530 
##                Tsakibanda               Tumbignooru 
##                       758                       276 
##            Tummalacheruvu         Tummalkuntlapalli 
##                       607                       437 
##                 Tummapala                  Tumuluru 
##                       593                       737 
##                      Tuni                   TURANGI 
##                      2030                       672 
##                    Ulichi                  Uppuluru 
##                       542                       878 
##                Uravakonda                   Utukuru 
##                       556                       327 
##                    Uyyuru            V.RAMANNAPALEM 
##                      1356                       378 
##               Vadarlapadu                   Vaddadi 
##                       219                       501 
##                Vadiseluru               Vaggampalli 
##                       964                       184 
##                 VAKKULURU                Vanganooru 
##                        76                       628 
##                      Vasi          VAVILIPALLI PETA 
##                       691                       462 
##               Veduruparti            Vedurupavuluru 
##                       789                       971 
##              Veerampalena           veereswarapuram 
##                       829                       475 
##                  Vejendla                VelagaPadu 
##                       486                       229 
##                Velampalem            Vellalacheruvu 
##                      1061                       412 
##                  Vemagiri            Vemavarappalem 
##                       889                       292 
##                   Vempadu                Vemulapudi 
##                       764                       482 
##               VENKATAGIRI              Venkatapuram 
##                       761                       389 
##           Venkatrayudupet                Vennanpudi 
##                       499                       342 
##                   VENTURU           Vijayapuri Sowt 
##                       495                       495 
##          Vijayawada Urban                 Vinukonda 
##                      6499                      1974 
##                  Vipparla             Visakhapatnam 
##                       506                      4717 
##             VISAKHAPATNAM          VishwanadhaPuram 
##                      1863                       224 
##               VissaKoderu              Vizianagaram 
##                       498                       644 
##               Vuyyalawada             West Godavari 
##                       646                       976 
##                West Gudur             WEST KUNDURRU 
##                       688                       806 
##                    Yadaki                YANAKANDLA 
##                       358                       638 
##                Yemmiganur                Yenugubala 
##                       629                       661
```
