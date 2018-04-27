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
## [1] 26706440
```

Unique Values in Sex:


```r
# Unique values in sex
table(andhra$sex)
```

```
## 
##   Female     Male 
## 13314087 13389261
```

Summary of Age:


```r
# Age
summary(andhra$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##    0.00   29.00   38.00   40.58   50.00  436.00    1590
```

No. of characters in ID:

```r
# Length of ID
table(nchar(andhra$id))
```

```
## 
##       10       11       12       13       14       15       16 
## 20955389      208       13   384889  5365065       15        3
```

Number of characters in pin code:


```r
table(nchar(andhra$pin_code))
```

```
## 
##        1        5        6 
##    68612      303 26282502
```


```r
# Net electors
sum(with(andhra, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 24906331
```

```r
nrow(andhra)
```

```
## [1] 26706440
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(andhra$elector_name))
```

```
## 
##       1       2       3       4       5       6       7       8       9 
##     307      39    1960   22063   59166  167851  336960  486042  637149 
##      10      11      12      13      14      15      16      17      18 
##  768298 1013648 1364507 1812956 2013003 2188359 2300815 2337434 2232423 
##      19      20      21      22      23      24      25      26      27 
## 1983135 1621275 1311328 1030730  799408  607129  448977  329949  242002 
##      28      29      30      31      32      33      34      35      36 
##  172737  127285  100920   75138   41737   28676   18627   12525    7273 
##      37      38      39      40      41      42      43      44      49 
##    3157    1046     313      67      17       3       1       2       1
```

```r
andhra[which(nchar(andhra$elector_name) < 4), "filename"]
```

```
## # A tibble: 2,306 x 1
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
## # ... with 2,296 more rows
```

Basic admin. units:

```r
table(andhra$police_station)
```

```
## 
##                                   .Narpala 
##                                      35322 
##                       1 Town P.S., Nellore 
##                                     159820 
##                      1 Town Police Station 
##                                     144790 
##           1 Town Police Station, Anantapur 
##                                     191484 
##                                 16/01/2017 
##                                    1138727 
##                          1Town Polisteshan 
##                                      32649 
##                                ≥ÂÕ€—≥›°ΩË— 
##                                      28164 
##                                    A.S.PET 
##                                      23058 
##                       Aaluru Polis Station 
##                                      22032 
##                                    Achanta 
##                                      39492 
##                                    Addanki 
##                                      49832 
##                                ADDATEEGALA 
##                                      20359 
##                          Adoni Taluka P.S. 
##                                     177188 
##                                  Advuldivi 
##                                      18347 
##                                 Agiripalli 
##                                      14181 
##                                    Akividu 
##                                      43949 
##                                    ALIPIRI 
##                                      14048 
##                                  ALLAGADDA 
##                                      49140 
##                                  ALLAVARAM 
##                                      36130 
##                                      Allur 
##                                      35852 
##                                     Almuru 
##                                      39665 
##                              Amadalavalasa 
##                                      45852 
##                            AMALAPURAM TOWN 
##                                      90757 
##                                 Amarapuram 
##                                      37662 
##                                 Amaravathi 
##                                      35352 
##                                AmbaGPettah 
##                                      33894 
##                                Amdguru P 5 
##                                      13372 
##                                   Amrtluru 
##                                      23791 
##                            Anakapalle Town 
##                                     117983 
##                            ANANTAPUR RURAL 
##                                      57037 
##                                ANANTHAGIRI 
##                                      28523 
##                          Ananthapur 1 Town 
##                                     135832 
##                          Ananthapur 2 Town 
##                                      51789 
##                             ANANTHASAGARAM 
##                                      23441 
##                                      Andra 
##                                      26805 
##                                ARAKUVALLEY 
##                                      34799 
##                                 Ardhaveedu 
##                                      15081 
##                                    ARILOVA 
##                                      69707 
##                      ASPARI POLICE STATION 
##                                      23774 
##                                Atchemapata 
##                                      26271 
##                               Atchutapuram 
##                                      36369 
##                                     Athili 
##                                      31216 
##                                      Atlur 
##                                      16188 
##                                    atmakur 
##                                      47035 
##                                    ATMAKUR 
##                                      19682 
##                                   ATMAKURU 
##                                      39510 
##                                Atreyapuram 
##                                      46767 
##                                 Avanigadda 
##                                      12365 
##                                  Ayinvilli 
##                                      28168 
##                                   B Kondur 
##                                       9775 
##                                    B Matam 
##                                      24129 
##                             B P Rachapalle 
##                                      40407 
##                               B.N.KANDRIGA 
##                                      16602 
##                                   Badanagi 
##                                      30406 
##                                     BADVEL 
##                                      31730 
##                               Badvel Rural 
##                                      29972 
##                              BAIREDDIPALLE 
##                                      33279 
##                                  BALJIPETA 
##                                      37076 
##                                Ballikuruva 
##                                      26101 
##                              BANAGANAPALLI 
##                                      52465 
##                                 BANDAPURAM 
##                                      42542 
##                        Bandaru Taluka P.S. 
##                                     106356 
##                Bandiatmakuru Polis Station 
##                                      26306 
##                                Bandlamottu 
##                                      28869 
##                               Bapatla Town 
##                                      75561 
##                                 Bapulapadu 
##                                      51078 
##                                    BATTILI 
##                                      16797 
##                                Bellamkonda 
##                                      15186 
##                                  Beluguppa 
##                                      23666 
##                              Bestawaripeta 
##                                      19686 
##                                Betancherla 
##                                      44335 
##                                Bhattiprolu 
##                                      26368 
##                             Bheemunipatnam 
##                                      67931 
##                                  Bhimadole 
##                                      22147 
##                                 Bhogapuram 
##                                      62733 
##                                  Biccavolu 
##                                      44744 
##                                    Bobbili 
##                                      77156 
##                              BODDIKURAPADU 
##                                      19304 
##                                     Bogolu 
##                                      33557 
##                                Bommana Hal 
##                                      32582 
##                                 Bondapalli 
##                                      15619 
##                             Bramhasamudram 
##                                      26976 
##                         Buchchireddy Palem 
##                                      44082 
##                             BUDARAYAVALASA 
##                                      25999 
##                                Bukkapatnam 
##                                      21943 
##                          Bukkarayasamudram 
##                                      40485 
##                          BukkaRayaSamudram 
##                                      19726 
##                                      Burja 
##                                      25656 
##                              Butchaiahpeta 
##                                      39895 
##                               BUTTAYIGUDEM 
##                                      14809 
##                                  C K Dinne 
##                                      33123 
##                   C.BELAGAL POLICE STATION 
##                                      28207 
##                               CHAGALAMARRI 
##                                      30725 
##                                   Chagallu 
##                                      40032 
##                                Chakrayapet 
##                                      23112 
##                                Challapalli 
##                                      30526 
##                                   Chandole 
##                                      16834 
##                  Chandragiri Polis Steshan 
##                                      21948 
##                              ChandralaPadu 
##                                      23632 
##                                    Chapadu 
##                                      20030 
##                                   Chebrole 
##                                      66052 
##                                 CHEEDIKADA 
##                                      24100 
##                               Cheemakurthi 
##                                      39409 
##                              Cheepurupalli 
##                                      28681 
##                           Cheerala i-Tounu 
##                                      86650 
##                                   Chejarla 
##                                      24060 
##                           Chennekothapalli 
##                                      28857 
##                                    Chennur 
##                                      26534 
##                               Cherukupalli 
##                                      28531 
##                      Chilakaluripeta Rural 
##                                      69877 
##                                Chilmathuru 
##                                      31096 
##                                ChinaGanjam 
##                                      23631 
##                               ChinnaMandem 
##                                      22002 
##                                Chintalpudi 
##                                      25092 
##                                Chintapalli 
##                                      43929 
##                                   chintoor 
##                                      16006 
##                   ChippaGiri Polis Station 
##                                      12854 
##                                    Chitvel 
##                                      24700 
##                                 Chodavaram 
##                                      58149 
##                                  ClassPadu 
##                                      23908 
##                            Cuddapah 1-Town 
##                                      20340 
##                                     Cumbum 
##                                      16743 
##                                  D.C.Palli 
##                                      29133 
##                                  D.Hirehal 
##                                      26101 
##                                   Dagdarti 
##                                      28624 
##                                      Darsi 
##                                      38270 
##                                   Denakada 
##                                      30037 
##                                  Denduluru 
##                                      28196 
##                  Devanakonda Polis Station 
##                                      19537 
##                                DEVARAPALLI 
##                                      29624 
##                                 DEVIPATNAM 
##                                      18777 
##                             Dharmajigudena 
##                                      18296 
##                                Dharmavaram 
##                                     106449 
##                                        Don 
##                                      61581 
##                                DONKONDA RS 
##                                      22154 
##                             DORAVARISATRAM 
##                                      21564 
##                                    Dornala 
##                                      15089 
##                                  DORNIPADU 
##                                      14393 
##                             Douvzheshwaram 
##                                      56159 
##                                  Duggirala 
##                                      41278 
##                                 DUMBRIGUDA 
##                                      32677 
##                                      Durgi 
##                                      29851 
##                                   Duttalur 
##                                      12817 
##                                    Duvvuru 
##                                      30655 
##                           DvarakaThirumala 
##                                      29325 
##                               E. Annavaram 
##                                      23446 
##                                  E. Kondur 
##                                      16638 
##                                   EdlaPadu 
##                                      20482 
##                          Elamanchili Arban 
##                                      38424 
##                                Eluru Rural 
##                                     165825 
##                               Elvin Pettah 
##                                      55659 
##                                      Emula 
##                                      20744 
##                                      Epuru 
##                                      26204 
##                                     Erpedu 
##                                      30849 
##                             ErragondaPalem 
##                                      16630 
##                                   ETCHERLA 
##                                      19680 
##                               Firangipuram 
##                                      33662 
##                                  G. Kondur 
##                                      20251 
##                                G. Madugula 
##                                      29620 
##                                 G. Sigadam 
##                                      21589 
##                      G.D.Nelluru Polis.Ste 
##                                     115461 
##                                 G.K.Veedhi 
##                                      33917 
##                                 GADIVEMULA 
##                                      26927 
##                           GAJAPATHINAGARAM 
##                                      18347 
##                                   Gajuwaka 
##                                     177835 
##                                   Galividu 
##                                      33056 
##                               Gampalagudem 
##                                      33713 
##                                GANAPAVARAM 
##                                      42552 
##                                 Gandepalli 
##                                      23746 
##                                 GANGAVARAM 
##                                      40074 
##                            GangireddyPalli 
##                                      21743 
##                                   Gantyada 
##                                      18988 
##                                       Gara 
##                                      41892 
##                                   Garividi 
##                                      24577 
##                                 Garladinne 
##                                      33320 
##                                Garugubilli 
##                                      26616 
##                                 Ghantasala 
##                                      19777 
##                                   Giddalur 
##                                      47968 
##                               Gidlavalleru 
##                                      27709 
##                                  Gokavaram 
##                                      31896 
##                                 Gollapalem 
##                                      75686 
##                                 Gollaprolu 
##                                      47710 
##                                  Golugonda 
##                                      31095 
##                   Gonegandla Polis Station 
##                                      36371 
##                                      Gooty 
##                                      58326 
##                               Gopalapatnam 
##                                     113079 
##                               GOPALAPATNAM 
##                                      51773 
##                                   Gorantla 
##                                      42816 
##                                 GUDI PALLA 
##                                      21235 
##                                  GudiBanda 
##                                      32560 
##                       Gudivada Taluka P.S. 
##                                      14670 
##                              Gudivada Town 
##                                      74301 
##                                    GUDLURU 
##                                      11590 
##                                  Gudupalli 
##                                      24746 
##                                     Guduru 
##                                      23430 
##                      GUDURU POLICE STATION 
##                                      28004 
##                       Guduru Polis Station 
##                                       1051 
##                               Guduru Rural 
##                                      67207 
##                                 Gummagatta 
##                                      28885 
##                               GUNTUR RURAL 
##                                      73808 
##                                   Gurajala 
##                                      25711 
##                                      Gurla 
##                                      24727 
##                                GURRAMKONDA 
##                                      20910 
##                  Gurrankonda Polis Steshan 
##                                      15738 
##                     Halharvi Polis Station 
##                                      17377 
##                           HanumanthuniPadu 
##                                       7692 
##                                Hirmandalmu 
##                                      28948 
##                     Holgunda Polis Station 
##                                      18314 
##                            I Town Guntakal 
##                                     111940 
##                     i Town P.S. Vijayawada 
##                                     517114 
##                              Ibrahimpatnam 
##                                      93714 
##                              IBRAHIMPATNAM 
##                                      57793 
##                                  Ichapuram 
##                                      55526 
##                          ii-Tounu Cheerala 
##                                      29310 
##                                    ii-Town 
##                                     407091 
##                     II TOWN POLICE STATION 
##                                     159735 
##                                 Indrapalem 
##                                      61970 
##                            Indukuru Pettah 
##                                      21606 
##                                     Inkole 
##                                      27138 
##                                     Involu 
##                                      27510 
##                                 iPolavaram 
##                                      42539 
##                                 Iragavaram 
##                                      25614 
##              J. Panguluru Muppawaram Vadda 
##                                      20601 
##                                Jaggaiahpet 
##                                      57393 
##                                 Jaggampeta 
##                                      37142 
##                                   Jaldanki 
##                                      17961 
##                                   Jalumuru 
##                                      40740 
##                                       Jami 
##                                      28792 
##                              Jammalamadugu 
##                                      45036 
##                           Jangareddigudena 
##                                      62109 
##                                Jarugumalli 
##                                      16444 
##                               JEELUGUMILLI 
##                                       7105 
##                               Jiyammavlasa 
##                                      29072 
##                               Jupadubangla 
##                                      18542 
##                                 K.KOTAPADU 
##                                      37145 
##                                K.V.B PURAM 
##                                      24084 
##                    K.V.Palli Polis Steshan 
##                                       4875 
##                              KADAPA Taluka 
##                                     154500 
##                               Kadiri Urban 
##                                      73831 
##                                    Kadiyam 
##                                      62029 
##                     Kaikaluru Arbana P.Es. 
##                                      32639 
##                                   KAKINADA 
##                                     192501 
##                                   Kakumanu 
##                                      15241 
##                                 Kalidindhi 
##                                      34195 
##                                   Kaligiri 
##                                      16404 
##                     Kalikiri Polis Steshan 
##                                      33146 
##                      Kalkada Polis Steshan 
##                                      18519 
##                                      Kalla 
##                                      40180 
##                                    KALLURU 
##                                      22455 
##                                   Kaluvanu 
##                                      22779 
##                                Kalyanadurg 
##                                      54876 
##                                Kamalapuram 
##                                      32881 
##                                   Kambadur 
##                                      29886 
##                              KANAGANAPALLI 
##                                      24062 
##                             KanchikaCharla 
##                                      31429 
##                                   Kanchili 
##                                      23597 
##                             KANDUKUR URBAN 
##                                      30537 
##                                    Kanekal 
##                                      39106 
##                                   Kanigiri 
##                                      30990 
##                                  Kankipadu 
##                                      39675 
##                                 Karamchedu 
##                                      23383 
##                                  Karampudi 
##                                      25440 
##                                     KARAPA 
##                                      53469 
##                                 Karlapalem 
##                                      19995 
##                    Karvetingaram Polis.Ste 
##                                      53538 
##                                 Kashinkota 
##                                      41014 
##                                  KASIBUGGA 
##                                      69547 
##                                 Kasinayana 
##                                      11602 
##                                 KatreNikon 
##                                      42023 
##                              Kavali 1-Town 
##                                     107881 
##                                     Kaviti 
##                                      24864 
##                                    Kazipet 
##                                      30554 
##                                  Kirlapudi 
##                                      33856 
##                                 Kodavaluru 
##                                      23970 
##                     Kodumuru Polis Station 
##                                      40295 
##                                      Kodur 
##                                      25272 
##                               KOLIMIGUNDLA 
##                                      30955 
##                                  Kollipara 
##                                      25457 
##                                    Kolluru 
##                                      25360 
##                                   Komarada 
##                                      59956 
##                                   Komarole 
##                                      17471 
##                              Konakanamitla 
##                                      16612 
##                                    Kondapi 
##                                      17125 
##                                 Kondapuram 
##                                      21021 
##                                 Korishpadu 
##                                      29365 
##                                  Korukonda 
##                                      41026 
##                       Kosigi Polis Station 
##                                      31094 
##                                Kotananduru 
##                                      31853 
##                                 Kotbommali 
##                                      33628 
##                               Kothacheruvu 
##                                      22715 
##                                  Kothakota 
##                                      43788 
##                                 Kothapalli 
##                                      18593 
##                                  Kothapeta 
##                                      47390 
##                                Kothavalasa 
##                                      42537 
##                                    Kothuru 
##                                      39438 
##                                    KOTTURU 
##                                      22510 
##                                 Kotvuratla 
##                                      19784 
##                                      Kovur 
##                                      40649 
##                              Kovvuru Rural 
##                                      41383 
##                             KOWTHALAM P.S. 
##                                      34710 
##                               KOYYALAGUDEM 
##                                      28188 
##                                Krishnagiri 
##                                      25122 
##                                    Krosuru 
##                                      30318 
##                                Kruthivennu 
##                                      25281 
##                                     Kuderu 
##                                      18616 
##                                   KUKUNURU 
##                                       2133 
##                                  kunavaram 
##                                      12020 
##                                   Kundurpi 
##                                      29430 
##                                     Kuppam 
##                                      54442 
##                                  Kurichedu 
##                                      16954 
##                     KURNOOL POLICE STATION 
##                                     189836 
##               KURNOOL RURAL POLICE STATION 
##                                      70621 
##                    Kurnoolu 4Va Tounu P.S. 
##                                     120174 
##                                  Kurupam-i 
##                                      61534 
##                                     L.Coat 
##                                      35336 
##                           LAKKIREDDI PALLI 
##                                      22637 
##                                     Laveru 
##                                      17108 
##                            LAXMINARASUPETA 
##                                      13252 
##                                   Lepakshi 
##                                      26773 
##                              Lingasamudram 
##                                      10625 
##                                 Machavaram 
##                                      32708 
##                                 Madakasira 
##                                      48729 
##                   Maddikeram Polis Station 
##                                      23333 
##                                  Maddipadu 
##                                      32188 
##                    Mahanandi Polis Station 
##                                      19597 
##                                    Makkuva 
##                                      29431 
##                                Makwarpalem 
##                                      37361 
##                                MALAKAPURAM 
##                                     138677 
##                                Malikipuram 
##                                      39557 
##                                      Mampa 
##                                      29730 
##                             MANDAPETA TOWN 
##                                      71817 
##                                    Mandasa 
##                                      53048 
##                                 Mandavalli 
##                                      22984 
##                                Mangalagiri 
##                                     102204 
##                              mangasamudram 
##                                     121638 
##                 MANTRALAYAM POLICE STATION 
##                                      30486 
##                                   Manubolu 
##                                      22057 
##                                MAREDUMILLI 
##                                      11873 
##                                 Markapuram 
##                                      51898 
##                                  Marripudi 
##                                       8479 
##                                   Maruturu 
##                                      42559 
##                                Medikonduru 
##                                      30147 
##                                 Meliaputti 
##                                      32327 
##                    Miduturu Police statioN 
##                                      25878 
##                                  Mogalturu 
##                                      76081 
##                    Molklacheruvu Polis.Ste 
##                                      22529 
##                                 Muddanooru 
##                                      20135 
##                                  Mudigubba 
##                                      32662 
##                                Mudinepalli 
##                                      35344 
##                    MUDIVEDU POLICE STATION 
##                                      11900 
##                               Mummidivaram 
##                                      43418 
##                                 Munagapaka 
##                                      28287 
##                                 Mundlamuru 
##                                      24929 
##                                   Mupapala 
##                                      16827 
##                              Musunuru P.S. 
##                                      13694 
##                                  Muthukuru 
##                                      31973 
##                         mutyalareddy palli 
##                                      72377 
##                                    Mydukur 
##                                      43127 
##                                  Mylavaram 
##                                      53976 
##                                  N.P.Kunta 
##                                      18173 
##                         Naarasaraopet Town 
##                                      96252 
##                                   Nadendla 
##                                      22781 
##                                NAGALAPURAM 
##                                      20739 
##                                    Nagaram 
##                                      62079 
##                                     Nagari 
##                                      58455 
##                                Nagayalanka 
##                                      24807 
##                                   NAIDUPET 
##                                      22695 
##                                Nakkapallii 
##                                      37878 
##                               NALLACHERUVU 
##                                      18240 
##                                 Nallajarla 
##                                      30930 
##                              Nallamada P-3 
##                                      21118 
##                                   Nandalur 
##                                      20084 
##                               Nandi kotkur 
##                                      45578 
##                                  Nandigama 
##                                      42981 
##                                  Nandigamu 
##                                      25190 
##                                  Nandivada 
##                                      12034 
##                        NarasaRPettah Rural 
##                                      25966 
##               Narayanavanam Police Station 
##                                      22465 
##                                Narsannapet 
##                                      45476 
##                           Narsipatnam Town 
##                                      53435 
##                                   Natwaram 
##                                      37348 
##                                 Nellimarla 
##                                      45245 
##                                  NELLIPAKA 
##                                      17209 
##                                  Nidamarru 
##                                      27579 
##                                     NINDRA 
##                                      12962 
##          No-1 town police station, Nellore 
##                                     130428 
##                         Nuzvid Rurala P.S. 
##                                      51438 
##                             ObulavariPalli 
##                                      20438 
##                                      Ojili 
##                                      23000 
##                                 OLD GUNTUR 
##                                     166261 
##               Ongole iTounu Polisu Station 
##                                      31913 
##                   Orvakallu police Station 
##                                      38553 
##                                        OWK 
##                                      31319 
##                                  P.C.Palli 
##                                       9893 
##                               P.Gannavaram 
##                                      43202 
##                                 Pachipenta 
##                                      25203 
##                                    Paderoo 
##                                      38890 
##                                 Pagidayala 
##                                      19460 
##                                 Palakoderu 
##                                      42448 
##                            Palakollu Rural 
##                                      70354 
##                                  PALAMANER 
##                                      43757 
##                                   Palkonda 
##                                      32098 
##                 PallSamudram Polis Steshan 
##                                       9281 
##                                    Pamarru 
##                                      97943 
##                                     Pamidi 
##                                      31004 
##                              Pamidimukkala 
##                                      25675 
##                   PamulaPadu Polis Station 
##                                      22193 
##                                     Pamuru 
##                                      15316 
##                                     PANYAM 
##                                      26203 
##                                   Parchuru 
##                                      33983 
##                                     Parigi 
##                                      32517 
##                              Parvathipuram 
##                                      67852 
##                                Pata Guntur 
##                                     186136 
##                                Pathapatnam 
##                                      42954 
##                                pathiikonda 
##                                      42394 
##                               Payakaraopet 
##                                      47878 
##                               PEDAGANTYADA 
##                                      65943 
##                                 PedaKakani 
##                                      45582 
##                               Pedakurapadu 
##                                      28391 
##                              Pedamanapuram 
##                                      16658 
##                      Pedana Polisa Station 
##                                      39560 
##                              Pedanandipadu 
##                                      12804 
##                                   Pedapadu 
##                                      31997 
##                                   Pedapudi 
##                                      34488 
##                                   Pedavegi 
##                                      30575 
##              Pedda kaduburu Police Station 
##                                      30772 
##                               Peddamudiyam 
##                                      18959 
##                               PEDDAPANJANI 
##                                      26562 
##                             Peddapappuruvu 
##                                      22901 
##                                 Peddapuram 
##                                      66519 
##                                 Peddarvidu 
##                                       9646 
##                        PEDDATHIPPASAMUDRAM 
##                                      22063 
##                              Peddavaduguru 
##                                      27242 
##                                  PELLAKURU 
##                                      23112 
##                                  Penagalur 
##                                      23671 
##                                 Penamaluru 
##                                      97719 
##                                Pendlimarri 
##                                      28814 
##                                  Pentapadu 
##                                      27226 
##                            Penuganchiprolu 
##                                      21392 
##                                  PENUGONDA 
##                                      33631 
##                                  Penukonda 
##                                      32118 
##                                 Penumantra 
##                                      33681 
##                                    PENUMUR 
##                                      23584 
##                                   Peravali 
##                                      30367 
##                                Piduguralla 
##                                      72309 
##                        Piler Polis.Steshan 
##                                      43886 
##                                  Pitapuram 
##                                      33392 
##                   Pitchatur Police Station 
##                                      20255 
##                                 PITHAPURAM 
##                                      76057 
##                                     Podili 
##                                      29424 
##                                      Podur 
##                                      16898 
##                                     Poduru 
##                                      18998 
##                                    Polakii 
##                                      40867 
##                                    PONDURU 
##                                      55276 
##                                  Ponnaluru 
##                                      16445 
##                               Ponnur Tounu 
##                                        434 
##                                Ponnur Town 
##                                      67100 
##                                Porumamilla 
##                                      25619 
##                                 Prathipadu 
##                                      63180 
##                           Prodduturu Rural 
##                                     161867 
##                                 Pulevendla 
##                                      48375 
##                             PullalaCheruvu 
##                                      12127 
##                                  Pullampet 
##                                      21286 
##                                Puspatirega 
##                                      77700 
##                PUTHALAPATTU POLICE STATION 
##                                      23229 
##                                    Putluru 
##                                      22292 
##                                 Puttaparri 
##                                      34058 
##                                     PUTTUR 
##                                      40089 
##                                    PYAPILI 
##                                      37102 
##                                   Racharla 
##                                      13697 
##                        Rajahmundry -i Town 
##                                     199018 
##                       Rajahmundry Pattanam 
##                                     139806 
##                                      Rajam 
##                                      36292 
##                                   Rajampet 
##                                      64292 
##                               RAJAVOMMANGI 
##                                      23716 
##                                  Rajupalem 
##                                      39745 
##                              Rallabuduguru 
##                                      23595 
##                            Ramabhadrapuram 
##                                      27189 
##                           Ramachandrapuram 
##                                      71393 
##             Ramachandrapuram Polis.Steshan 
##                                      19204 
##                                   Ramagiri 
##                                      20555 
##                                 Ramakuppam 
##                                      25427 
##                                  Ramapuram 
##                                      21433 
##                                   Rambilli 
##                                      32271 
##                            RAMPACHODAVARAM 
##                                      22258 
##                                RANASTHALAM 
##                                      27914 
##                                   RAPTHADU 
##                                      24965 
##                                Ravulapalem 
##                                      62435 
##                                 Rayadurgam 
##                                      65811 
##                                  Rayavaram 
##                                      38351 
##                                     Razole 
##                                      41036 
##                                 Reddigudem 
##                                      16551 
##                       Regidi Amadalavalasa 
##                                      22858 
##                                  RENIGUNTA 
##                                      48872 
##                              Rentachintala 
##                                      24066 
##                                    Repalle 
##                                      42730 
##                                     Roddam 
##                                      26077 
## Roll Identification: Basic roll of Special 
##                                     183239 
##                                      Rolla 
##                                      21640 
##                                  Rolugunta 
##                                      32243 
##                                 RUDRAVARAM 
##                                      31156 
##                                  S R PURAM 
##                                      26417 
##                               S. Rayavaram 
##                                      37616 
##                       S.Ar.Puram Polis.Ste 
##                                      17828 
##                                     S.KOTA 
##                                      42570 
##                                 Sabbavaram 
##                                      47251 
##                             Sakhinetipalli 
##                                      38825 
##                                     Saluru 
##                                      60334 
##                                 Sambepalle 
##                                      22908 
##                               Samisragudem 
##                                      54140 
##                                     Sangam 
##                                      22402 
##                                  SANJAMALA 
##                                      22614 
##                               Santabommali 
##                                      29484 
##                              Santhamagalur 
##                                      27476 
##                          SanthanuthalaPadu 
##                                      37025 
##                                SanthKaviti 
##                                      18407 
##                                 Sarpavaram 
##                                     125419 
##                                 Sarubujili 
##                                      22253 
##                                   Sarvkota 
##                                      32731 
##                               Sattanapalli 
##                                      59985 
##                   Satyavedu Police Station 
##                                      29383 
##                               SAVALYAPURAM 
##                                      13980 
##                              SEETA NAGARAM 
##                                      38678 
##                              Seethanagaram 
##                                      41866 
##                            Seetharamapuram 
##                                      12744 
##                                    Setturu 
##                                      15063 
##                                    Siddota 
##                                      22627 
##                              Simhadripuram 
##                                      33328 
##                                Singanamala 
##                                      28035 
##                             Singarayakonda 
##                                      25616 
##                                  SIRIVELLA 
##                                      34930 
##                               Siyas. Puram 
##                                       7257 
##                               Somandepalli 
##                                      26377 
##                                    Sompeta 
##                                      34300 
##                                SRIHARIKOTA 
##                                      50305 
##                                 Srikakulam 
##                                     115496 
##                         SRIKALAHSHTI RURAL 
##                                      81264 
##                   Sundipenta Polis Station 
##                                      16988 
##                                  Sydapuram 
##                                      24712 
##                              T NARASAPURAM 
##                                       5842 
##                               T SanduPalli 
##                                      33082 
##                                  Tadepalli 
##                                      57541 
##                      Tadepalligudena Rural 
##                                      85012 
##                               Tadikalapudi 
##                                      19773 
##                                  Tadikonda 
##                                      36656 
##                                 Tadimarrii 
##                                      17287 
##                              TadiwaripallI 
##                                      19777 
##   Tadparthi Rural and Town Police Stations 
##                                      96191 
##                                  Tallapudi 
##                                      15598 
##                                    Talpula 
##                                      25701 
##                Tamballapalli Polis.Steshan 
##                                      29642 
##                                    TanaKal 
##                                      27495 
##                                  Tanguturu 
##                                      23374 
##                               Tanuku Rural 
##                                      65808 
##                              TAVANAM PALLE 
##                                      28537 
##                                    Tekkali 
##                                      46565 
##                                   Tenali-1 
##                                     145201 
##                                     Terlam 
##                                      35042 
##          Thirumala One Town Police Station 
##                                     215271 
##                                    Thondur 
##                                      16824 
##                          Thotapalli Guduru 
##                                      25496 
##                               Thotlavallur 
##                                      24387 
##                                THOTTAMBEDU 
##                                      22053 
##                                   Tiruvuru 
##                                      29832 
##                              Tripurantakam 
##                                      16537 
##                                   TSUNDURU 
##                                      19406 
##                      Tuggali Polis Station 
##                                      39119 
##                                    Tulluru 
##                                      30839 
##                                    Tuni -U 
##                                      89796 
##                               U.Kothapalli 
##                                      35217 
##                                  Udayagiri 
##                                      20460 
##                                  Ulavapadu 
##                                      15428 
##                                       Undi 
##                                      41905 
##                                   Unguturu 
##                                      33898 
##                              UPPALAGUPTHAM 
##                                      31470 
##                                 Uyyalavada 
##                                      13397 
##                                     Uyyuru 
##                                      35639 
##                                     V.Coat 
##                                      35201 
##                                 V.MADUGULA 
##                                      33784 
##                                Vajrakaruru 
##                                      29152 
##                            Vajrapu Kothuru 
##                                      52566 
##                                 Vallampudi 
##                                      29678 
##                                    Valluru 
##                                      17440 
##                                    Vangara 
##                                      14696 
##                             VARADAIAHPALEM 
##                                      18778 
##                       vararamachandrapuram 
##                                      12380 
##                              VARIKUNTAPADU 
##                                      12292 
##                                   Vatsavai 
##                                      28643 
##                             Vatticherukuru 
##                                      14040 
##                    Vayalapad Polis.Steshan 
##                                      21364 
##                                VEDAMALPETA 
##                                      19235 
##                 Vedurukuppam Polis.Steshan 
##                                      24928 
##                               VEERAGHATTAM 
##                                      20748 
##                                  Veerballi 
##                                      22871 
##                               Veerullapadu 
##                                      23923 
##                                     Velair 
##                                       2263 
##                                  Veldurthi 
##                                      53538 
##                                 Veligandla 
##                                       8842 
##                     Velugodu Polis Station 
##                                      29698 
##                                   Vempalli 
##                                      36743 
##                                     Vemuru 
##                                      21202 
##                              Venkatachalam 
##                                      33251 
##                                venkatagiri 
##                                      54938 
##                                Vidapanakal 
##                                      30879 
##                                  Vidavalur 
##                                      26389 
##                  VijayaPuram Polis.Steshan 
##                                      14561 
##                           Vijayapuri South 
##                                      67779 
##                         Vijayvgaram i Touv 
##                                     265527 
##                                  Vinukonda 
##                                      64136 
##                                Vissannapet 
##                                      23571 
##                            VOLETIVARIPALEM 
##                                      14236 
##                                Vontimamidi 
##                                      57419 
##                                 Vontimitta 
##                                      16922 
##                                Y.RAMAVARAM 
##                                      16476 
##                                Yaddanapudi 
##                                      17611 
##                                     Yadiki 
##                                      30426 
##                                  Yallanuru 
##                                      22260 
##                                Yalmanchili 
##                                      31235 
##                                 YELESWARAM 
##                                      44399 
##              Yemmiganur (T) Police Station 
##                                      98739 
##                                Yerraguntla 
##                                      51758
```

```r
table(andhra$mandal)
```

```
## 
##                     1                    10                   100 
##                   656                  1114                   975 
##                   101                   102                   103 
##                   833                   667                   696 
##                   104                   105                   106 
##                   699                   661                   656 
##                   107                   108                   109 
##                   725                   644                   911 
##                    11                   110                   111 
##                   985                   846                   848 
##                   112                   113                   114 
##                   324                   399                   431 
##                   115                   116                   117 
##                   447                   820                   631 
##                   118                   119                    12 
##                   555                   711                   599 
##                   120                   121                   122 
##                   757                   670                   724 
##                   123                   124                   125 
##                   654                  1392                   849 
##                   126                   127                   128 
##                  1104                   475                   676 
##                   129                    13                   130 
##                  1305                   607                  1015 
##                   131                   132                   133 
##                   991                  1022                   856 
##                   134                   135                   136 
##                  1258                   813                   786 
##                   137                   138                   139 
##                   324                  1010                   687 
##                    14                   140                   141 
##                   587                   788                  1363 
##                   142                   143                   144 
##                  1260                  1073                   999 
##                   145                   146                   147 
##                   758                   658                   526 
##                   148                   149                    15 
##                  1172                   915                   648 
##                   150                   151                   152 
##                  1052                   758                   638 
##                   153                   154                   155 
##                   440                   774                  1190 
##                   156                   157                   158 
##                  1010                  1042                   602 
##                   159                    16                   160 
##                   599                   998                   573 
##                   161                   162                   163 
##                   752                   801                   504 
##                   164                   165                   166 
##                   900                   554                   648 
##                   167                   168                   169 
##                  1143                   900                   579 
##                    17                   170                   171 
##                   845                   641                   999 
##                   172                   173                   174 
##                   938                  1170                  1191 
##                   175                   176                   177 
##                   518                   643                   397 
##                   178                   179                    18 
##                   607                   506                  1226 
##                   180                   181                   182 
##                   548                   708                   761 
##                   183                   184                   185 
##                   913                   761                   620 
##                   186                   187                   188 
##                   722                   415                   622 
##                   189                    19                   190 
##                   568                  1300                   583 
##                   191                   192                   193 
##                   462                   693                   641 
##                   194                   195                   196 
##                   783                   744                   841 
##                   197                   198                   199 
##                   703                  1011                   915 
##                     2                    20                   200 
##                   581                  1244                   516 
##                   201                   202                   203 
##                   465                   833                   713 
##                   204                   205                   206 
##                   708                   606                   702 
##                   207                   208                   209 
##                   740                   578                   599 
##                    21                   210                   211 
##                   916                   599                   568 
##                   212                   213                   214 
##                   732                   748                   614 
##                   215                   216                   217 
##                   679                   529                   408 
##                   218                   219                    22 
##                   423                   387                   615 
##                   220                   221                   222 
##                   564                   647                   614 
##                   223                   224                   225 
##                   604                   573                   547 
##                   226                   227                   228 
##                   554                  1063                   849 
##                   229                    23                   230 
##                   529                   530                   495 
##                   231                   232                   233 
##                   477                   481                   937 
##                   234                   235                   236 
##                  1017                   753                   497 
##                   237                   238                    24 
##                   424                   290                   580 
##                    25                    26                    27 
##                   584                   981                   651 
##                    28                    29                     3 
##                   600                   753                   601 
##                    30                    31                    32 
##                   799                   486                  1044 
##                    33                    34                    35 
##                   894                   737                   608 
##                    36                    37                    38 
##                   561                   611                  1140 
##                    39                     4                    40 
##                   532                   970                   816 
##                    41                    42                    43 
##                   683                  1160                  1069 
##                    44                    45                    46 
##                   934                  1109                   890 
##                    47                    48                    49 
##                   653                   810                  1309 
##                     5                    50                    51 
##                   591                   434                   737 
##                    52                    53                    54 
##                   884                  1053                  1252 
##                    55                    56                    57 
##                   643                   462                   868 
##                    58                    59                     6 
##                   810                  1156                   944 
##                    60                    61                    62 
##                  1070                   836                   381 
##                    63                    64                    65 
##                   971                   898                   875 
##                    66                    67                    68 
##                   949                   575                   595 
##                    69                     7                    70 
##                   858                   814                  1341 
##                    71                    72                    73 
##                   623                   807                   783 
##                    74                    75                    76 
##                  1220                   756                   793 
##                    77                    78                    79 
##                   841                  1122                   589 
##                     8                    80                    81 
##                   683                   572                   665 
##                    82                    83                    84 
##                   793                   951                   971 
##                    85                    86                    87 
##                   979                   533                  1111 
##                    88                    89                     9 
##                   920                  1088                   708 
##                    90                    91                    92 
##                  1246                   845                  1246 
##                    93                    94                    95 
##                  1171                   507                   410 
##                    96                    97                    98 
##                   779                   652                   610 
##                    99             A.KONDURU               A.S.Pet 
##                   748                 16638                 23058 
##                Aaluru              Achampet               Achanta 
##                 22032                 26271                 39492 
##               Addanki           ADDATEEGALA                 Adoni 
##                 49832                 20359                177188 
##            Agiripalli                  Agli               Akividu 
##                 14181                 19726                 43949 
##             Allagadda             ALLAVARAM                 Allur 
##                 49140                 36130                 35852 
##                Almuru         Amadalavalasa            AMALAPURAM 
##                 39665                 45852                 90757 
##            Amarapuram            Amaravathi           Amarthaluru 
##                 37662                 35352                 23791 
##           AmbaGPettah               Amdguru            Anakapalle 
##                 33894                 13372                117983 
##           Anandapuram            Anantagiri           AnantaPuram 
##                 34916                 28523                248521 
##         Anantasagaram             Anaparthi            Ardhaveedu 
##                 23441                 38351                 15081 
##              Arkuveli                Aspari          Atchutapuram 
##                 34799                 23774                 36369 
##                Athili                 Atlur              Atmakuru 
##                 31216                 16188                106227 
##           Atreyapuram            Avanigadda             Ayinvilli 
##                 46767                 20308                 28168 
##               B KODUR               B Matam           B.Kothakota 
##                  9775                 24129                 31165 
##          B.N.Kandriga               Badnagi                BADVEL 
##                 16602                 30406                 31730 
##         Baireddipalle           Balayapalli              Baljipet 
##                 33279                 21297                 37076 
##           Ballikurava                Bamini         BANAGANAPALLI 
##                 26101                 16797                 52465 
##        Bandi Atmakuru          BangaruPalem            Bantumilli 
##                 26306                 46693                 17357 
##               Bapatla            Bapulapadu        BarhamSamudram 
##                 75561                 51078                 26976 
##           Bathalpalli           Bellamkonda             Beluguppa 
##                 21795                 15186                 23666 
##         BestawaripetA           Betancharla           Bhattiprolu 
##                 19686                 44335                 26368 
##        Bheemunipatnam             Bhimadole            Bhimavaram 
##                 67931                 22147                145497 
##             Biccavolu               Bobbili             BogaPuram 
##                 44744                 77156                 29090 
##                Bogolu            BollaPalli            Bommanahal 
##                 33557                 28869                 32582 
##            Bondapalli           Bukkapatnam     BukkaRayaSamudram 
##                 15619                 21943                 40485 
##                 Burja         Butchaiahpeta      Butchireddipalem 
##                 25656                 39895                 44082 
##          Buttayagudem             C.Belagal             C.S.Puram 
##                 14809                 28207                  7257 
##          Chagalamarri              Chagallu           Chakrayapet 
##                 30725                 40032                 23112 
##           Challapalli         Chandarlapadu               Chapadu 
##                 30526                 23632                 20030 
##               Chatrai              Chebrole            Cheedikada 
##                 11019                 35164                 24100 
##          Cheemakurthi         Cheepurupalli              Cheerala 
##                 39409                 28681                 86650 
##              Chejarla      Chennekothapalli               Chennur 
##                 24060                 28857                 26534 
##          Cherukupalli       Chilakaluripeta            Chillakuru 
##                 28531                 69877                 15569 
##           Chilmathuru           ChinaGanjam         Chinna Mandem 
##                 31096                 23631                 22002 
##           Chintalpudi           Chintapalli       ChintKommaDinne 
##                 25092                 43929                 33123 
##              CHINTOOR            ChippaGiri            Chittamuru 
##                 16006                 12854                 20618 
##              Chittoor               Chitvel            Chodavaram 
##                123477                 24700                 58149 
##           Chowdepalle                Cumbum             D.Hirehal 
##                 17828                 16743                 26101 
##            Dachepalli              Dagdarti               Dakkili 
##                 32708                 28624                 13251 
##                 Darsi           Dathirajeru             Denduluru 
##                 38270                 16658                 28196 
##               Denkada            Devankonda           Devarapalle 
##                 30037                 19537                 42542 
##           DEVARAPALLI            DEVIPATNAM           Dharmavaram 
##                 29624                 18777                106449 
##                   Don             Donakonda        Doravarisatram 
##                 61581                 22154                 21564 
##               Dornala             Dornipadu             Duggirala 
##                 15089                 14393                 41278 
##           Dumbiriguda                 Durgi              Duttalur 
##                 32677                 29851                 12817 
##               DUVVURU       Dwarakatirumala              Edlapadu 
##                 30655                 29325                 20482 
##            Eleshvaram          Ellamanchili                 Eluru 
##                 44399                 38424                165825 
##                 Epuru              Etcharla          Firangipuram 
##                 26204                 19680                 33662 
##            G. Konduru           G. Madugula           G.D.Nellore 
##                 20251                 29620                 47654 
##              G.Sigdam             GadiEmula      GAJAPATHINAGARAM 
##                 21589                 26927                 18347 
##              Gajuwaka              Galividu          Gampalagudem 
##                177835                 33056                 33713 
##           Ganapavaram            Gandepalli           GandlaPenta 
##                 42552                 23746                 15097 
##            Gangavaram            GANGAVARAM            Gannavaram 
##                 23427                 16647                 48592 
##              Gantyada                  Gara              Garividi 
##                 18988                 41892                 24577 
##            GarlaDinne           Garugubilli            Ghantasala 
##                 33320                 26616                 19777 
##              Giddalur          Gidlavalleru             Gokavaram 
##                 47968                 27709                 31896 
##            Gollaprolu             Golugonda            Gonegandla 
##                 47710                 31095                 36371 
##                 Gooty           Gopalapuram             Gopavaram 
##                 58326                 36939                 29972 
##              Gorantla      Gudenkothaveedhi             GudiBanda 
##                 42816                 33917                 32560 
##              Gudipala              Gudivada                Gudlur 
##                 21235                 74301                 11590 
##             Gudupalle                Guduru            GummaGatta 
##                 24746                118641                 28885 
##       GummalaxmiPuram            Guntakallu                Guntur 
##                 24674                111940                426205 
##              Gurajala                 Gurla           Gurramkonda 
##                 25711                 24727                 20910 
##              H.M.Padu              Halharvi            Hindupuram 
##                  7692                 17377                135832 
##           Hirmandalam              Holgunda             Hukumpeta 
##                 28948                 18314                 39016 
##           I.Polavaram         Ibrahimpatnam             Ichapuram 
##                 42539                 57793                 55526 
##            Indukurpet                Inkole            Iragavaram 
##                 21606                 27138                 25614 
##                 Irala           J.Panguluru           Jaggaiahpet 
##                 26784                 20601                 57393 
##            Jaggampeta              Jaldanki              Jalumuru 
##                 37142                 17961                 40740 
##                  Jami         Jammalamadugu       Jangareddigudem 
##                 28792                 45036                 62109 
##           Jarugumalli          Jeelugumilli        Jiyyammavalasa 
##                 16444                  7105                 29072 
##          Jupadubangla            K.KOTAPADU           K.V.B.Puram 
##                 18542                 37145                 24084 
##             K.V.Palli                KADAPA                Kadiri 
##                  4875                154500                 73831 
##               Kadiyam             Kaikaluru              KAJULURU 
##                 62029                 32639                 43096 
##              Kakinada        Kakinada Rural        Kakinada Urban 
##                 32649                125419                192501 
##              Kakumanu            KALASAPADU            Kalidindhi 
##                 15241                 23908                 34195 
##              Kaligiri              Kalikiri               Kalkada 
##                 16404                 33146                 18519 
##                 Kalla                KALLUR              Kaluvoya 
##                 40180                120174                 22779 
##          Kalyandurgam           Kamalapuram        Kamavarapukota 
##                 54876                 32881                 19773 
##              Kambadur        KanchikaCharla              Kanchili 
##                 29886                 31429                 23597 
##              Kandukur               Kanekal         Kangana Palli 
##                 30537                 39106                 24062 
##              Kanigiri             Kankipadu      Kapileswarapuram 
##                 30990                 39675                 32579 
##            Karamchedu             Karampudi                Karapa 
##                 23383                 25440                 53469 
##            Karlapalem         Karvetingaram            Kashinkota 
##                 19995                 26070                 41014 
##           Katrenikona                Kavali                Kaviti 
##                 42023                107881                 24864 
##               Kazipet            Kirlampudi            Kodavaluru 
##                 30554                 33856                 23970 
##              Kodumuru                 Kodur            KOILKUNTLA 
##                 40295                 65679                 28164 
##          KOLIMIGUNDLA             Kollipara               Kolluru 
##                 30955                 25457                 25360 
##              Komarada              KOMAROLU         Konakonamitla 
##                 30386                 17471                 16612 
##               Kondapi            Kondapuram            Korishpadu 
##                 17125                 41361                 29365 
##             Korukonda                Kosigi                  KOTA 
##                 41026                 31094                 20044 
##          Kotabommaali            Kotauratla          Kothacheruvu 
##                 33628                 19784                 22715 
##            Kothapalle            Kothapalli           Kothapatnam 
##                 18593                 35217                 27792 
##             Kothapeta           Kothavalasa                Kothur 
##                 47390                 42537                 39438 
##            Kotnanduru                 Kovur               Kovvuru 
##                 31853                 40649                 41383 
##             Kowthalam          Koyyalagudem               Koyyuru 
##                 34710                 28188                 29730 
##           Krishnagiri               Krosuru           Kruthivennu 
##                 25122                 30318                 25281 
##                Kuderu              KUKUNURU             KUNAVARAM 
##                 18616                  2133                 12020 
##              Kundurpi                Kuppam          kurabalakota 
##                 29430                 54442                 11900 
##             Kurichedu               Kurnool               KURNOOL 
##                 16954                 70621                189836 
##              Kurnoolu               Kurupam                L.KOTA 
##                  1051                 22518                 35336 
##       LAKKIREDDYPALLE    LakshminarsuPettah           LanallaMada 
##                 22637                 13252                 21118 
##                Laveru              Lepakshi               Lingala 
##                 17108                 26773                 16370 
##            Lingapalem         Lingasamudram              Macharla 
##                 18296                 10625                 67779 
##            Machavaram         Machilipatnam             Maddipadu 
##                 25518                106356                 32188 
##             Madkshira             Mahanandi         Makavarapalem 
##                 48729                 19597                 37361 
##               Makkuva           Malikipuram           Mamidikudru 
##                 29431                 39557                 39956 
##             Mandapeta               Mandasa            Mandavalli 
##                 71817                 53048                 22984 
##           Mangalagiri           Mantralayam              Manubolu 
##                102204                 30486                 22057 
##           MAREDUMILLI            Markapuram             Marripadu 
##                 11873                 51898                 29133 
##             Marripudi              Maruturu           Medikonduru 
##                  8479                 42559                 30147 
##            Meliaputti               Mentada         MERAKAMUDIDAM 
##                 32327                 26805                 25999 
##              Miduturu             Mogalturu       MolakalaCheruvu 
##                 25878                 39909                 22529 
##              Mopidevi                 Movva            Muddanooru 
##                 12365                 32537                 20135 
##             Mudigubba           Mudinepalli          Mummidivaram 
##                 32662                 35344                 43418 
##            Munagapaka        Munchingiputtu            Mundlamuru 
##                 28287                 29570                 24929 
##              Muppalla              Musunuru             Muthukuru 
##                 16827                 13694                 31973 
##               Mydukur             Mylavaram              N.G.Padu 
##                 43127                 53976                 31913 
##             N.P.Kunta              Nadendla           Nagalapuram 
##                 18173                 22781                 20739 
##               Nagaram                NAGARI           Nagayalanka 
##                 22123                 58455                 24807 
##              Naidupet           Nakarikallu            Nakkapalli 
##                 22695                 25966                 37878 
##          Nallacheruvu            Nallajarla              Nandalur 
##                 18240                 30930                 20084 
##            Nandavaram              Nandigam             Nandigama 
##                 32869                 25190                 42981 
##          Nandikotkuru             Nandivada        NaraayanaVanam 
##                 45578                 12034                 22465 
##         Narasannapeta          Narasaraopet               Narpala 
##                 45476                 96252                 35322 
##           Narsaapuram           Narsipatnam            Nathavaram 
##                 76081                 53435                 37348 
##            Nellimarla             NELLIPAKA               Nellore 
##                 45245                 17209                290248 
##            Nidadavole             Nidamarru                Nindra 
##                 54140                 27579                 12962 
##           Nizampatnam              Nuzendla                Nuzvid 
##                 18347                 27510                 51438 
##        ObulavariPalli     Obuldewar Cheruvu                 Ojili 
##                 20438                 19778                 23000 
##                Ongole             Orvakallu                   OWK 
##                144790                 38553                 31319 
##             P.C.Palli          P.Gannavaram              P.T.Yam. 
##                  9893                 43202                 22063 
##            Pachipenta               Paderoo           Padmanabham 
##                 25203                 38890                 33643 
##            Pagidayala            Palakoderu             Palakollu 
##                 19460                 35588                 70354 
##             Palakonda                Palasa          Palasamudram 
##                 32098                 69547                  9281 
##              Palmneru               Pamarru                Pamidi 
##                 43757                 65364                 31004 
##         Pamidimukkalu            PamulaPadu                 Pamur 
##                 25675                 22193                 15316 
##                PANYAM              Paravada               PARCHUR 
##                 26203                 46769                 33983 
##                Parigi         Parvathipuram           Pathapatnam 
##                 32517                 67852                 42954 
##            Pathikonda          Payakaraopet        Peda Nandipadu 
##                 42394                 47878                 12804 
##            Pedabayalu         Pedagantiyada          Pedagantyada 
##                 30985                 56168                  9775 
##            PedaKakani          Pedakurapadu         Pedana Rurala 
##                 45582                 28391                 39560 
##              Pedapadu          Pedaparupudi              Pedapudi 
##                 31997                 14670                 34488 
##              Pedavegi         PEDDA PANJANI          Peddakduburu 
##                 30575                 26562                 30772 
##          Peddamandyam          Peddamudiyam          Peddapappuru 
##                 15742                 18959                 22901 
##            Peddapuram          Peddaraveedu          PeddaVadugur 
##                 66519                  9646                 27242 
##             Pellakuru             Penagalur            Penamaluru 
##                 23112                 23671                 97719 
##           Pendlimarri             Pendurthi             Pentapadu 
##                 28814                113079                 27226 
##       Penuganchiprolu             Penugonda             Penukonda 
##                 21392                 33631                 32118 
##            Penumantra               Penumur              Peravali 
##                 33681                 23584                 30367 
##           Piduguralla                Pileru             Pitchatur 
##                 72309                 43886                 20255 
##            Pithapuram       Pittalvanipalem            Podalakuru 
##                 76057                 16834                 35177 
##                Podili                Poduru                Polaki 
##                 29424                 35896                 40867 
##             Polavaram               Ponduru             Ponnaluru 
##                  5842                 55276                 16445 
##                Ponnur           Porumamilla            Prathipadu 
##                 67534                 25619                 63180 
##            Prodduturu            PuliCherla            Pulivendla 
##                161867                 22455                 48375 
##        PullalaCheruvu             Pullampet              Punganur 
##                 12127                 21286                 67807 
##           Puspatirega          Puthalapattu               Putluru 
##                 42784                 23229                 22292 
##            PuttaParti                PUTTUR               Pyapili 
##                 34058                 40089                 37102 
##              Racharla           Rajahmundry     Rajahmundry Rural 
##                 13697                199018                139806 
##                 Rajam              Rajampet           Rajanagaram 
##                 36292                 64292                 56159 
##          RAJAVOMMANGI             Rajupalem       RamabhadraPuram 
##                 23716                 39745                 27189 
##      Ramachandrapuram              Ramagiri            Ramakuppam 
##                 19204                 20555                 25427 
##             Ramapuram              Rambilli       Ramchandrapuram 
##                 21433                 32271                 71393 
##       RAMPACHODAVARAM            Ranasdhlam             Rangampet 
##                 22258                 27914                 33392 
##               Raptadu                 Rapur             Ravikmtam 
##                 24965                 19853                 43788 
##           Ravulapalem             Rayachoti            Rayadurgam 
##                 62435                 87174                 65811 
##             Rayavaram                Razole            Reddigudem 
##                 32590                 41036                 16551 
##  Regidi Amadalavalasa             Renigunta         Rentachintala 
##                 22858                 48872                 24066 
##               Repalle                Roddam                 Rolla 
##                 42730                 26077                 21640 
##             Rolugunta           Rompicharla           Rompicherla 
##                 32243                 23589                 15738 
##          Rowthulapudi           Rudhravaram          S. Rayavaram 
##                 24048                 31156                 37616 
##               S.A.K.N                S.KOTA              S.N.Padu 
##                 11602                 42570                 37025 
##             S.R.Puram            Sabbavaram                 Sadum 
##                 26417                 47251                 21948 
##        Sakhinetipalli                Saluru              Samalkot 
##                 38825                 60334                 61970 
##            Sambepalli                Sangam             SANJAMALA 
##                 22908                 22402                 22614 
##            Sankavaram         Santabommaali         Santhamagalur 
##                 23446                 29484                 27476 
##           Santhipuram           SanthKaviti            Sarubujili 
##                 23595                 18407                 22253 
##              Sarvkota          Sattanapalli             Satyavedu 
##                 32731                 59985                 29383 
##          Savalyapuram         SEETA NAGARAM           Seethampeta 
##                 13980                 38678                 22510 
##         Seethanagaram       Seetharamapuram              Shetturu 
##                 41866                 12744                 15063 
##            Shirivella               Sidhout         Simhadripuram 
##                 34930                 22627                 16958 
##           Singanamala        Singarayakonda                 Somal 
##                 28035                 25616                 27468 
##          Somandepalli               Sompeta            Srikakulam 
##                 26377                 34300                115496 
##         SRIKALAHASTHI             SRISAILAM            Sullurupet 
##                 81264                 16988                 50305 
##            Sundupalli             Sydapuram         T.Narasapuram 
##                 33082                 24712                 12454 
##                  Tada             Tadepalli        Tadepalligudem 
##                 20451                 57541                 85012 
##             Tadikonda             Tadimarri             Tadiparti 
##                 36656                 17287                 96191 
##             Tallapudi               Talluru              Talupula 
##                 15598                 19304                 25701 
##             Talzhrevu             Tanakallu             Tanguturu 
##                 42359                 27495                 23374 
##                Tanuku             Tarlupadu               Tekkali 
##                 65808                 19777                 46565 
##                Tenali                Terlam        Thamballapalle 
##                145201                 35042                 29642 
##         Thavanampalli    Thirupathi (Arban)    Thirupathi (Urban) 
##                 28537                 14048                215271 
##     Thirupathi(Rural)               Thondur     Thotapalli Guduru 
##                 72377                 16824                 25496 
##          Thotlavallur              Tiruvuru             Tondanagi 
##                 24387                 29832                 57419 
##            Tottambedu         Tripurantakam              Tsunduru 
##                 22053                 16537                 19406 
##               Tuggali               Tulluru                  Tuni 
##                 39119                 30839                 89796 
##       Turpu Maddikera             Udayagiri             ULAVAPADU 
##                 23333                 20460                 15428 
##                  Undi          Undrajavaram              Unguturu 
##                 41905                 28461                 64786 
##         UPPALAGUPTHAM            Uravakonda            Uyyalavada 
##                 31470                 51789                 13397 
##                Uyyuru                V.Coat            V.Madugula 
##                 35639                 35201                 33784 
##             Vadmalpet            Vajrakruru         VajrapuKothur 
##                 19235                 29152                 52566 
##                Vakadu               Valluru          VALMIKIPURAM 
##                 17700                 17440                 21364 
##               Vangara  VARARAMACHANDRAPURAM         Vardaiahpalem 
##                 14696                 12380                 18778 
##         VARIKUNTAPADU              Vatsavai        Vatticherukuru 
##                 12292                 28643                 14040 
##          Vedurukuppam          Veeraghattam   VEERAPUNAYANI PALLE 
##                 24928                 20748                 21743 
##          Veeravasaram             Veerballi          Veerullapadu 
##                 42448                 22871                 23923 
##             Velairpad             Veldurthi            Veligandla 
##                  2263                 53538                  8842 
##              Velugodu              Vempalli                Vemula 
##                 29698                 36743                 20744 
##                Vemuru         Venkatachalam           Venkatagiri 
##                 21202                 33251                 54938 
##                Vepada             Vetapalem        Vidapa Nakallu 
##                 29678                 29310                 30879 
##             Vidavalur           VijayaPuram      Vijayawada Rural 
##                 26389                 14561                 93714 
##      Vijayawada Urban              Vinjamur             Vinukonda 
##                517114                 14760                 64136 
## VISAKHAPATNAM (RURAL) VISAKHAPATNAM (URBAN)   Visakhapatnam Arban 
##                121480                298412                407091 
##  Vishakhaptnam, Rural           Vissannapet          Vizianagaram 
##                 80941                 23571                184586 
##       VOLETIVARIPALEM            Vontimitta           Y.RAMAVARAM 
##                 14236                 16922                 16476 
##           Yaddanapudi                Yadiki                Yadmri 
##                 17611                 30426                 22335 
##          Yalamanchili            Yallanooru            Yemmiganur 
##                 31235                 22260                 98739 
##               Yerpedu       Yerragondapalem           Yerraguntla 
##                 30849                 16630                 51758
```

```r
table(andhra$district)
```

```
## 
##     Anantapur      Chittoor East Godavari         Eluru        Guntur 
##       2482935       2031523       3105269           976       2464671 
##        Kadapa       Krishna       Kurnool      Kurnoolu       Nellore 
##       1682335       2208217       2092718            95       1607072 
##      Prakasam    Srikakulam Visakhapatnam  Vizianagaram West Godavari 
##       1471687       1367680       2763598       1284361       1960064
```

```r
table(andhra$main_town)
```

```
## 
##               "Rajeevnagar              .D.MACHALESAM 
##                       1278                       1087 
##             .Mohamedapuram                    .Navuru 
##                       1692                       1519 
##                [Iduru -ii]             [Sarvepalli-4] 
##                        895                       1404 
##            100 GOLLAPALLE,              104-BASAPURAM 
##                        661                       1423 
##                 11-Pedduru                 111-Madire 
##                        513                       2533 
##                113-Talluru             115-Settipalli 
##                       2029                       1060 
##              13 GOLLAPALLI    132 - Gudise Gupparalla 
##                        390                        482 
##             155-kammapalle             170-Gollapalle 
##                        387                       5878 
##                 173-Madire       180-MAJARAKOTHAPALLI 
##                        410                        264 
##             184-gollapalle             189 KOTHAPALLI 
##                       2257                       1164 
##              190 RAMAPURAM        196 THIMMAIAH PALLI 
##                        579                        460 
##              197 RAMAPURAM     29A CHINTHAMAKULAPALLE 
##                       1313                       1211 
##                 64-Pedduru                 75 Talluru 
##                        694                       3417 
##     79 CHINTHAMAKULA PALLE             81 UPPARAPALLI 
##                        376                       1963 
##                 88 Talluru                 89-Pedduru 
##                       1809                        556 
##              94 AVULAPALLI                A Gokulpadu 
##                       2492                       1931 
##                A GOPAVARAM                  A L PURAM 
##                       1010                        355 
##                  A M PURAM                   A,P.PETA 
##                        636                        712 
##                 A. Konduru                A.Agraharam 
##                       5142                        582 
##                 A.G.N PETA                A.GOKAVARAM 
##                        886                       1918 
##                    A.Kodur                   A.KODURU 
##                       2036                       3002 
##                A.KOTHAKOTA               A.KOTHAPALLI 
##                        846                       1579 
##               A.MallaVaram                   A.S.PETA 
##                       1158                       3075 
##          A.VEERA NARAYANAM                A.Vemavaram 
##                       1346                       5092 
##                  AakayPadu         AakulaSeetammaPeta 
##                       2556                        829 
##                     Aaluru                 AareyPalli 
##                       8448                       2672 
##                  AarlaPadu                  AARLAPADU 
##                       1228                        454 
##                AavulaDoddi               Abakaladoddi 
##                        713                        590 
##              Abbangudvalli              AbbarajuPalem 
##                        362                        301 
##                  Abbawaram                Abbayapalem 
##                       1573                        329 
##                  Abbedoddi                  Abbipuram 
##                       1198                        896 
##            Abbu Saheb Peta                     Abburu 
##                        519                       2245 
##               AbdullaPuram               ABDULLAPURAM 
##                       1734                        790 
##                 Abhicherla                  Abotulpet 
##                        691                        330 
##                  Acche rla               ACCHIAHPALEM 
##                       1730                        385 
##               AchannaPuram                    Achanta 
##                        210                      14294 
##          Acharlaparlapalli                Achutapuram 
##                        541                       1580 
##                ACHUTAPURAM                   Achwaram 
##                       1024                       1238 
##          Achyutapuratrayam                    Adakulu 
##                       5007                       2419 
##                     ADARAM                      ADARU 
##                        265                        821 
##                   ADAVARAM         ADAVI CHERLO PALLI 
##                       1037                        629 
##             ADAVIAGRAHARAM                Adavikolanu 
##                        516                       3021 
##                 Adavipalem                 Adavivaram 
##                       4319                      17192 
##                     Addada               Addakulpalli 
##                        606                       1164 
##                AddalaMarri                 Addampalli 
##                        487                       1019 
##                     Addamu                Addapuseela 
##                        331                       1800 
##                  ADDASARAM                ADDATEEGALA 
##                        958                       2658 
##                   ADDATIGA                  Addepalli 
##                        409                       4728 
##                 Addkulguda    Addu Manda Venkama Peta 
##                        155                       1064 
##                  ADDUMANDA                     Adduru 
##                        987                       1263 
##               ADDURUVALASA                 Adigoppula 
##                        270                       5683 
##             Adimurthypuram            ADINIMMAYAPALLI 
##                        407                        811 
##                    Adipudi              ADIREDDIPALLE 
##                       2830                        377 
##                      Adivi             Adivi Nekkalam 
##                       3029                       1195 
##              Adivibuduguru               ADIVIKOTHURU 
##                       1903                       1229 
##                       Adli                    ADMELLI 
##                         72                       1242 
##                      Adoni                      AdPak 
##                     117409                        622 
##                      Adpur               ADUGULAPUTTU 
##                        939                       1337 
##                     Adurru                 Adusumalli 
##                       2278                       1541 
##               Adviraolpadu                  Advuldivi 
##                        585                       2424 
##                    Adwaram                    AGADURU 
##                        264                       1496 
##                      Agali                 Aganampudi 
##                       5212                      18578 
##             AGARA MANGALAM                     Agaram 
##                       1240                       1095 
##                     AGARAM         Agarlagokarlapalli 
##                       2032                         78 
##                     Agarru                     Agdala 
##                       1906                        122 
##                 Agdallanka             AGGICHENUPALLE 
##                       1873                        652 
##                 Aginiparru                 Agiripalle 
##                       1014                       3482 
##                AgniGundala                  Agraharam 
##                       2775                       2004 
##                  AGRAHARAM                   Agrahram 
##                       2718                        755 
##                  Agsldinne                   Agsnooru 
##                        654                        856 
##               Agtwarappadu                     Aguroo 
##                       2942                        716 
##                      Aguru                     Agveli 
##                        670                        775 
##                   AHOBILAM            Ahoblcharyulpet 
##                       1586                        587 
##             Aidugullapalli                  Ainampudi 
##                        487                        440 
##                   Ainavolu                 Ainmukkala 
##                       1115                       2098 
##                   Ainparru                    Ainpuru 
##                        932                       1107 
##                     Airala                  Airan Gal 
##                       4334                        880 
##                  Aitampudi                  AitaVaram 
##                        621                       1013 
##                    Ajamuru                     AJJADA 
##                        935                       1328 
##                  Ajjampudi                    Ajjaram 
##                        627                       1628 
##                      Ajram           AKASHALAKKAVARAM 
##                        901                       1123 
##                  Akbarabad                 Akilivlasa 
##                        546                        859 
##                    Akividu                AkkaCheruvu 
##                      15551                        485 
##              AkkaiahValasa               Akkajampalli 
##                        512                        125 
##           Akkalareddipalli                 Akkamapata 
##                       1822                       1182 
##                 Akkampalle                  AKKAMPETA 
##                        790                        867 
##          Akkanna Agraharam                  AkkaPalem 
##                        342                        558 
##                AkkaraPalli                AKKARAPALLI 
##                        256                        249 
##                   AkkarPak               AkkaSamudram 
##                        726                        411 
##                  AkkaVaram                Akkayapalli 
##                        518                       8725 
##               Akkayyapalem           AkkiAreddy Gudem 
##                        435                        449 
##           AkkiAreddy Palem            AKKIREDDI PALEM 
##                       4247                       1610 
##             Akkireddigudem             akkireddypalem 
##                        660                       2028 
##                 AkkiValasa                  AkkiVaram 
##                       1557                       2785 
##                   Akkulpet                  Akkupalle 
##                        506                       1639 
##                   Akkurada                   AKKURTHY 
##                        259                        738 
##                Aknam battu       AKULA NARAYANA PALLI 
##                        476                        582 
##               Akulamannadu        AKULARAGHUNADAPURAM 
##                       1832                       1084 
##                    Akuledu                  Akulkatta 
##                       1441                        706 
##                Akultampara                   Akumalla 
##                        874                       1830 
##              AKUMAMIDIKOTA                    Akunuru 
##                         68                       1438 
##               Akurajupalli              akuthotapalli 
##                       4878                        225 
##              Akuthotapalli                 Akutigpadu 
##                       6341                       1385 
##                     Akvidu                Alaganipadu 
##                       2025                       1410 
##                 Alam Konda                ALAMAJIPETA 
##                       1566                        474 
##                   ALAMANDA                  Alampuram 
##                       3156                       1666 
##                    Alamuru                    Alapadu 
##                       1911                       1762 
##                   ALAPAKAM                 Alaridinne 
##                       1163                        786 
##                   ALATHURU                   ALATU RU 
##                        770                        464 
##                Alavalapadu                    Alawala 
##                       2779                        762 
##                  Ale Baadu                   Algaruvu 
##                        813                        159 
##                   Algnooru                    Alidena 
##                        775                        947 
##                     Alikam                    Alimili 
##                        542                        602 
##              Alireddipalle                    AlJangi 
##                        877                       3511 
##                     Allada                AlladaPalem 
##                       1516                        788 
##                   Alladpet                ALLADUPALLE 
##                        379                       2096 
##                  Allagadda                 ALLAMADUGU 
##                      19219                       1823 
##       Allamcharlarajupalem                  Allampadu 
##                        450                       3119 
##                 ALLAMPUTTU                  Allaparru 
##                        894                       4067 
##              ALLAPPA GUNTA                  Allapuram 
##                        868                       1129 
##                  ALLAVARAM                     Allena 
##                       5802                        559 
##                  Alligudem                 Alligudena 
##                        478                        827 
##                  Allimdugu                 Allimeraka 
##                       1836                        334 
##                Allinagaram                ALLINAGARAM 
##                        685                        820 
##                  AlliPalem                  AlliPalli 
##                         72                        470 
##                   Allipudi                  Allipuram 
##                       3005                       6202 
##           Allugumani palli                  Allugundu 
##                        683                       1172 
##                   AlluKoal                      Allur 
##                        676                      25866 
##                AllurPettah                     Alluru 
##                       5886                       2231 
##                 Allurupadu                     Almuru 
##                        435                      12793 
##                    Alturti                 Alturupadu 
##                        613                        780 
##                      ALUDU                    Alugolu 
##                       1011                       1771 
##                 Alugubilli                  Alurupadu 
##                       1068                        512 
##                  Alvakonda                     Alwala 
##                       1447                       1783 
##                    AMADALA              Amadalavalasa 
##                        794                      10837 
##        AmadalavalasaPettah                  AmalaPadu 
##                        627                       1909 
##                 Amalapuram         AMALAPURAM (RURAL) 
##                      37189                       6307 
##                     Amanam                 Amancharla 
##                       1278                       3055 
##              AmaniGudipadu                   Amapuram 
##                       1993                        747 
##                     Amaram                 Amarapuram 
##                        492                       8986 
##                 Amaravathi                 AmaraVilli 
##                       7276                        423 
##               Amarayavlasa                     Ambada 
##                        440                        219 
##                 Ambadipudi                  Ambakandi 
##                        847                        927 
##                Ambakapalle                   AMBAKKAM 
##                        608                        525 
##                 Ambalapudi                  Ambapuram 
##                        545                       4360 
##               AmbatiValasa                  Ambavaram 
##                        576                        302 
##                  AMBAVARAM             ambedkar nagar 
##                        426                        172 
##                Amberupuram                AMBIKAPURAM 
##                       2531                        554 
##               AmbiruPettah                Ambllavlasa 
##                        648                        967 
##                 AMBOJUPETA                   Ambrupet 
##                        588                       3921 
##           Ambugam Boddluru                   Ambusoli 
##                       1631                        452 
##                  Amdguntla                    Amdguru 
##                       1802                       3722 
##                AmeenaPuram                 Ameenpalli 
##                        883                        488 
##                    Amidala               Amidalagondi 
##                       5076                       3680 
##                 AMILEPALLI          Amin Saheb Pettah 
##                        566                       2196 
##                   Aminabad                  Aminabada 
##                       5296                       2429 
##                  AMINABADA                      Amiti 
##                        739                       1476 
##                    Amktadu                  Amlkudiya 
##                       2014                        430 
##             AMMAGANI PALLI   AMMAGARI BANDAKINDAPALLE 
##                       1475                        604 
##        AMMAIAHA GARI PALLE             Ammalla Dinane 
##                        591                       1692 
##                Ammanabrole      Ammani Jammala Madaka 
##                       2557                       2104 
##                  Ammapalem                  AMMAPALEM 
##                        943                        797 
##                 Ammapalena             AMMARAJU PALLE 
##                       1310                        886 
##              Ammavaripalem            AMMAVARIPATTEDA 
##                        784                        353 
##             Ammireddi Ngar                AMMIREKHALA 
##                        274                        442 
##                 Ammwaripet             Ammwariputtuga 
##                       2531                        561 
##             Amnichiruvella                  Ampapuram 
##                        939                       2333 
##                  AMPAVALLI                     Ampili 
##                       1147                        526 
##                     Amplam                     Ampolu 
##                        725                       5720 
##                    Ampuram                    AmPuram 
##                        241                       3760 
##                   Amravati           Amrtlinganngaram 
##                        862                        247 
##                   Amrtluru               AMRUTHAPURAM 
##                       4355                       3889 
##             AMUDALA PUTTUR               AMUDALABANDA 
##                        746                        505 
##               AMUDALAPALLI                Amudalpalle 
##                        288                        486 
##                Amudalpalli                Amudarlanka 
##                       2514                        403 
##                    Amuduru                    Amujuru 
##                        327                       1739 
##                  ANACODERU                   ANAGALLU 
##                       3898                       1980 
##                   ANAGUNTA                    Anaguru 
##                        643                        799 
##                 Anakapalle                Anakarapudi 
##                      54227                        980 
##                  ANAKAVOLU            ANAM VARI PALLI 
##                        849                        491 
##             anamvari palli                Anandapuram 
##                        421                       3145 
##                ANANDAPURAM                 Anantagiri 
##                       3465                        828 
##                Anantapalli     Anantapur Municipaltiy 
##                       3343                     169182 
##                Anantapuram                AnantaPuram 
##                       2740                       7587 
##            Anantarajupuram              Anantasagaram 
##                        864                       7966 
##             AnantaSamudram                Anantavaram 
##                       1882                      10429 
##            Anantawarappadu                ANANTHAGIRI 
##                       1194                       1645 
##        Ananthaiahgaripalli              Ananthamadugu 
##                       1447                       1043 
##             Anantharajupet             Ananthasagaram 
##                       5013                        148 
##               ANANTHAVARAM                  Anaparthi 
##                       1422                      16338 
##                 ANASABADRA                  Anatwaram 
##                        987                       3175 
##                  AnbaVaram                  AnbaVilli 
##                       4220                        551 
##              ANBODARAPALLE                Andagundala 
##                        532                        468 
##                   Andaluru                  Andawaram 
##                       1546                        984 
##                 Andlapalli                   Andlmala 
##                       1427                        336 
##                      Andra                  Andranagi 
##                       1231                       1096 
##               Andugulapadu                   Andukuru 
##                       1716                       1106 
##                  Anemadugu                    Anepudi 
##                       2087                        609 
##               Angalakuduru                    Angallu 
##                       4906                       2868 
##                   Angaluru                     ANGARA 
##                       3570                       4307 
##                   ANGULURU              Anigandlapadu 
##                        672                       4069 
##               Aniganidoddi                  Aniganuru 
##                        699                       1165 
##                 Anikepalli                 Aniklpalli 
##                       3262                        173 
##                    Animela            Animigani palli 
##                       1171                        662 
##              AnjaneyaPuram                     ANJURU 
##                        708                       1559 
##           ANKABHUPALAPURAM            Ankalammaguduru 
##                        608                        913 
##          Ankana Godugunuru               ANKANNAGUDEM 
##                        329                        245 
##                  Ankapalem                  Ankawaram 
##                       4016                       1122 
##                  Ankepalli            AnkiAreddyPalem 
##                        177                       8649 
##             AnkiReddipalli            ANKIREDDY PALLE 
##                        543                       3400 
##                Ankulpaturu                  AnkuPalem 
##                        281                       4212 
##                Anmannapudi                   Anmnmuru 
##                        459                        734 
##               Annadewarpet                   Annaluru 
##                       3110                       1186 
##                   AnnamBak                   Annamedu 
##                        170                       1933 
##                 AnnamPalli                AnnamPettah 
##                       1969                        555 
##          ANNAMRAJULAVALASA              ANNAMRAJUPETA 
##                        980                       1750 
##                   Annanagi                  Annaparru 
##                       1821                       1434 
##                  Annapuram       ANNAPUSASTHRULAPALLI 
##                        268                        588 
##            Annareddy Palem              ANNASAMIPALLE 
##                       1013                        642 
##                Annasmudram                  Annavaram 
##                        637                      21201 
##              Annavarappadu            ANNEBOYINAPALLI 
##                        216                        752 
##             Annerao Pettah                  AnnuPuram 
##                        942                        530 
##                     ANNURU                     Anooru 
##                       1233                       3180 
##                     Antada                ANTAKAPALLI 
##                        916                       1091 
##                 AntakPalli                ANTALAVARAM 
##                       1560                        628 
##                ANTARAKUDDA             ANTERVEDIGUDEM 
##                        515                        406 
##                  Antikondi                    Antipet 
##                        401                        949 
##                  Antivlasa                    Antlwar 
##                        644                        428 
##                   Antrvedi              Antrvedipalem 
##                       7392                       8308 
##                   Anugonda            Anugondu Palyam 
##                       1723                       1486 
##             Anumanchipalle               Anumarlapudi 
##                       2100                        814 
##              AnumaSamudram              Anumolu Lanka 
##                       1939                        680 
##                  Anumpalli               AnumulaPalli 
##                       1263                       1206 
##               Anumunilanka                  ANUPPALLI 
##                       2012                       1245 
##                    Anupuru                    Anwaram 
##                        517                        837 
##              APPA RAO PETA                 Appajipeta 
##                        936                        316 
##             Appalagraharam            Appalamma Palem 
##                        200                        485 
##                APPALAPURAM             APPALARAJPURAM 
##                        825                        634 
##            APPALARAJUGUDEM           AppalarajuPettah 
##                       1372                        712 
##                 APPAMBATTU                Appanaveedu 
##                        503                       2489 
##             Appandoravlasa           AppannaDoraPalem 
##                       1480                        698 
##               APPANNAPALEM          Appannramunilanka 
##                       3072                       2078 
##                 AppanPalli                  Appapuram 
##                       3351                       1285 
##                  APPAPURAM               APPARAOPALLI 
##                        284                        347 
##                Apparaopeta               ApparCheruvu 
##                       9637                       1130 
##               Appasamudram                 Appecherla 
##                       1675                       2869 
##                  Appikatla                  Appikonda 
##                       1673                       1714 
##               Appile Palli                APPINAPALLE 
##                       2176                       1149 
##                AR.LOCHARLa                 Arabupalem 
##                        739                        903 
##                  ARADAKOTA                 ARADIGUNTA 
##                       2530                       1522 
##               ARAGADAPALLI                   Aragonda 
##                        529                       3103 
##                      ARAKU               ARAKU COLONY 
##                       1718                       2697 
##                      ARAMA                    Aranedu 
##                       1177                        468 
##           ARANYAM KANDRIGA                    ARASADA 
##                        787                       2246 
##                 ARASAVELLI                Aratlakatta 
##                       3280                       6318 
##                 Aratlakota               ARAVAKOTHURU 
##                       1685                        430 
##                   Aravalli               AravalliPadu 
##                       2575                       1245 
##                 Aravapalli               Aravetipalle 
##                        912                        456 
##                     Ardali                   Ardavidu 
##                        201                       2552 
##                  ARDHAMALA                 ARDHAVARAM 
##                        567                       2575 
##                 ARDHAVEEDU                        ARE 
##                        602                       1349 
##               AreddyCherla                AreddyPalle 
##                       1735                        757 
##                      Aredu                   Arekallu 
##                        695                       1231 
##                   Aremanda                   Arepalli 
##                       1435                       1027 
##           ARIGILAVARIPALLI                 Arigipalem 
##                        308                        475 
##                    Arikera                Arikirevula 
##                       1362                       2197 
##                  Arikitota                 Arikivlasa 
##                       3162                        231 
##            ARIMAGULA PALLI               Arimanupenta 
##                        862                        621 
##                Arimenipadu                    Aripaka 
##                       1588                       2409 
##                Arishepalli                  Arivemula 
##                       1618                        159 
##                 ARJUNAGIRI                Arjunapuram 
##                       1241                        326 
##               ARJUNAVALASA                Arkatvemula 
##                        528                       1074 
##                   Arkbadra                 Arktvemula 
##                        579                       1368 
##                  Arlabanda                  Arlapdiya 
##                       1146                        774 
##                       ARLI                   ARMADAKA 
##                        984                        278 
##                     Arnada                     AROORU 
##                        822                        760 
##                     Arsada                   Arsblaga 
##                       1251                        837 
##                      Artam                   Artamuru 
##                       1071                       2866 
##                  ARTHAMURU                    ARUDURU 
##                       3708                        381 
##                  Arugolanu            ArugolanuPettah 
##                       7550                        398 
##                     Arulla                   Arumbaka 
##                        307                       9749 
##                      Aruru                      ARURU 
##                       1478                       1168 
##                     Arvidu           Arvitikistipuram 
##                       4418                        312 
##                  Aryavtham                 ASAKAPALLI 
##                       2298                       3421 
##               Asannagudena                     Aspari 
##                        564                       3271 
##               Aswaraopalem                      Atava 
##                       1091                        993 
##                 AtchaVelli            ATCHIPOLAVALASA 
##                        724                        771 
##               Atchutapuram               ATCHUTAPURAM 
##                        869                        308 
##  ATCHYUTAPURAM H/O.PARIMPU                   Athaluru 
##                       1256                       2259 
##                 Athikuppam                     Athili 
##                        415                      12911 
##                 Athinatham                  Athiwaram 
##                        405                       1363 
##                    Athkuru                  ATHMAKURU 
##                       3449                        465 
##                     ATHURU              Atikela Gundu 
##                       1849                       1159 
##            Atikivani Palem              Atiralladinna 
##                        543                        286 
##                Atkanitippa                     Atkuru 
##                        446                        441 
##                   Atlapadu                      Atlur 
##                       1152                       2374 
##                   Atmakuru         Atmramuniagraharam 
##                      62758                        653 
##                      Atota                     Atpaka 
##                       2736                       1799 
##                Atreyapuram                     ATTADA 
##                       4920                        643 
##                     Attali                    Attekal 
##                        302                        691 
##            ATTHISURIKAVITI           AugariKiiahPalem 
##                        616                        518 
##                 Avanigadda                      AVIDI 
##                      11329                       6606 
##                    AVILALA                     Avkuru 
##                      18100                        369 
##                   Avlinagi                    Avlnagi 
##                       1630                        174 
##                    Avtrbad                      Avuku 
##                        290                       8004 
##                 Avulamanda                Avulampalli 
##                       1675                        351 
##                Avulanatham             AvulavariPalem 
##                        762                       1826 
##                  Avuldatla                   Avulenna 
##                       1006                        734 
##                    Avupadu                  Avurupudi 
##                       1591                        841 
##                    Ayinada                    AYINADA 
##                        923                       1709 
##                  Ayinpuram                  Ayinvalli 
##                       3798                       3545 
##                 Ayitampudi                    Ayodhya 
##                        734                        115 
##                Ayodyapuram            AYYA VARI PALEM 
##                        357                        293 
##              AyyagariPalli              AYYAGARIPALLI 
##                       1052                        311 
##                    Ayyanki                AyyannaCoat 
##                       2090                        116 
##          AYYANNAGARI PALLI               AyyannaPalem 
##                         89                        865 
##               AYYANNAPALEM            AYYAPARAJUGUDEM 
##                        798                        963 
##           Ayyapareddipalem            AyyapuRajupalem 
##                        625                        355 
##            AYYAVANDLAPALLI                Ayyavanipet 
##                       1132                        950 
##             Ayyavari Palli        Ayyavari Rudravaram 
##                        712                        579 
##              Ayyavaripalle              Ayyavaripalli 
##                        760                       1252 
##              AYYAVARIPALLI              Ayyawaripalem 
##                        376                        954 
##             Ayyawaripalena                    B KODUR 
##                        980                       1033 
##               B RAMADURGAM               B. Agraharam 
##                        736                       1540 
##             B. AnantaPuram              B. DoddaVaram 
##                        979                       1156 
##              B. KOTHA KOTA                 B. Pappuru 
##                      16043                       1536 
##             B. TALLAVALASA               b.gopalpuram 
##                       2246                        824 
##                  B.K.Palli               B.K.Samudram 
##                        912                      15407 
##                   B.KODURU                B.Kondepadu 
##                        251                       1517 
##      B.Kothapalli-Podralla                   B.Kothur 
##                       3896                        636 
##                  B.Kothuru              B.Kottalpalle 
##                        697                        530 
##          B.Nagireddy Palle              B.P.V.KALLALU 
##                        593                       1052 
##                  B.S.Puram                  B.Sawaram 
##                       1459                       1690 
##               B.Singavaram               B.SINGAVARAM 
##                        174                        340 
##           B.SIVARAMAPATNAM                B.TADIPATRI 
##                        235                        179 
##                B.TADIPUTTU               B.TandraPadu 
##                        821                       5413 
##             B.VELAMALAKOTA                  Baa Nadhi 
##                        899                       1428 
##                    Babbidi                 Bachepalli 
##                        419                       2152 
##                BACHUMPALLI             BADADANAMPALLI 
##                        169                        826 
##                      Badam                  Badampudi 
##                        363                       2133 
##                BADANAGADDA                  Badapuram 
##                        274                       2041 
##                   BADARALA                   Badbanda 
##                        292                         82 
##                  Baddevolu                  Baddipudi 
##                       1517                       1132 
##                 BADDUMARRI                 Badevalasa 
##                        393                        221 
##                 BadeValasa              BADEVARIPALEM 
##                        898                        201 
##                     Badgam            BADIKAYALAPALLE 
##                        376                       2513 
##                   BADIMELA                Badinehallu 
##                        809                       1546 
##              Badinenipalli                    Badnagi 
##                        546                       3959 
##                 Baduguleru            Baduguvanilanka 
##                        404                       1454 
##                     Badvel                    Badvidu 
##                      12440                        907 
##                      Bagad               Bagalanatham 
##                         71                        521 
##                 BAGAMPALLE             Bageerdhipuram 
##                       2220                        275 
##            Baggandoravlasa         Baginayakana Halli 
##                        762                       1970 
##                  Baguvlasa                  Bahdpalli 
##                       1045                       2158 
##        Bahublendruni Gudem                 Baiahwaram 
##                       1039                       9007 
##                 Bailuppala            Baiparedlapalle 
##                       1734                        641 
##           BAIRAJU KANDRIGA             BAIREDDI PALLI 
##                        294                      10176 
##                BAIRU PALLI                Baita palli 
##                        296                        886 
##              Bakkannapalem                BakkuPettah 
##                       1862                        683 
##                     BAKURU                BAKURUPALEM 
##                       1951                        311 
##            BalabhadraPuram                     Balada 
##                       6701                       1023 
##                    Baladur               Balaga Rural 
##                        412                       1463 
##          BALAGANGANA PALLI               BalajeePuram 
##                       1834                        240 
##     Balaji Nagar ST Colony          BALAKRISHNA PURAM 
##                        255                        447 
##           Balakrishnapuram           BALAKRISHNAPURAM 
##                        502                        557 
##             BALAMVARIPALLI                  Balantram 
##                       1772                        818 
##             Balapala palli                  Balapanur 
##                       1344                       5199 
##                    Balaram              balaramapuram 
##                       1119                       1123 
##               BalaramPuram          BALASINGANA PALLI 
##                        673                        469 
##           Balavenkatapuram               BALAYA PALLI 
##                        301                        546 
##                Balayapalli                BALAYAPALLI 
##                       3512                        580 
##         Balbadra Rajapuram             Balbhadrapuram 
##                         93                        223 
##                    Bale ru                  Balemarru 
##                        957                        846 
##                  Balgudaba                    Baligam 
##                       2278                       1229 
##                 Baligattam               Balighattamu 
##                       1711                       9413 
##            BALIJA KANDRIGA                 BALIJAPADU 
##                        373                        803 
##                Balijapalem                Balijepalli 
##                        169                       2649 
##                BALIJIPALEM                 BALIJIPETA 
##                       1630                       2355 
##                     Balive                   Baliwada 
##                        281                        386 
##               BALKVIVALASA                      Balla 
##                        391                        807 
##         Balla Krishnapuram          BALLAKKIVARIPALLE 
##                        691                        183 
##                   Ballanki                  Ballavolu 
##                       1191                        353 
##                 Ballawaram                 Ballekallu 
##                         71                       1404 
##                 Ballempudi                BALLIKURAVA 
##                       1577                        923 
##                  Ballipadu                  BALLIPADU 
##                       2406                        454 
##                 Ballipalli                 Balliparri 
##                        637                        486 
##                 Balliparru               Balliputtuga 
##                        790                       1110 
##                    Balluru                     Balpam 
##                        345                       1893 
##                    Balseem                 Balsmudram 
##                        183                       1995 
##                 BALU PALLE               Balusulpalem 
##                        286                       1035 
##                 Balusupadu                    Bammidi 
##                       2836                        793 
##              BANAGANAPALLI               Banakacherla 
##                      12412                       1006 
##                      BANAM                  BANAPURAM 
##                       1229                        761 
##                      BANDA             Bandaganipalle 
##                        380                       1145 
##                 Bandaluppi                 Bandanpudi 
##                       1896                       1208 
##                 BANDAPALLE                 BandaPalli 
##                        428                       3626 
##                 BANDAPALLI                 BANDAPURAM 
##                       1460                       2528 
##              Bandarlapalle               Bandarugudem 
##                        529                        587 
##               Bandarulanka               BandaruPalle 
##                       7303                       1355 
##               BandaruPalli           BANDARUVARIPALLI 
##                       3077                        644 
##                Bandaveedhi                 Bandepalli 
##                       2157                       1577 
##              Bandhamcharla              BANDHEVUPURAM 
##                        795                        610 
##             Bandi Atmakuru                 BANDIGEDDA 
##                       4648                        374 
##                 Bandipalem            BandiVeligandla 
##                       1814                        849 
##            Bandiwarigudena                 Bandlamudi 
##                       1914                       1167 
##                BANDLAPALLE                Bandlapalli 
##                       1091                       2286 
##                BandlaPalli                   BANDREVU 
##                       1710                       1907 
##              BANDRLA PALLE    BANGALA ANE CHILAMATTUR 
##                        832                        754 
##            Bangaram Pettah               Bangarametta 
##                        447                       1767 
##            BANGARAMMAPALEM           BangarammaPettah 
##                       1360                        232 
##               BANGARUMETTA              Bangaruvalasa 
##                        804                        327 
##              BangaruValasa               Banjaragudem 
##                        201                        627 
##          Banjarukeshupuram                 Banjirupet 
##                        903                        167 
##               Bankuruvlasa                   Bannooru 
##                        248                       2484 
##                   BannuWad                Banta Kunta 
##                        723                        612 
##                 BANTANAHAL            bantoou makkuva 
##                        486                        291 
##             BANTROTHUPUTTU                 Bantumilli 
##                        425                       3376 
##                 Bantupalli                    Banvasi 
##                       1692                       1685 
##                  Banvnooru          Bapa Bhupalpatnam 
##                        701                        465 
##               Bapala Doddi                    Bapatla 
##                        471                      38465 
##               Bapatla East               Bapatla West 
##                       5386                       4053 
##              Bapirajugudem                 Bapulapadu 
##                        566                       9296 
##                    BAPURAM                 BARANIKOTA 
##                       1460                        415 
##             BarhamSamudram                  BARJIPADU 
##                       3780                        522 
##                  Barlapudi                      BARLI 
##                        428                       1476 
##                      Barna                BARRIMAMIDI 
##                        127                        470 
##             BARRINKALAPADU                  Barripadu 
##                        458                        322 
##                 Barthipudi                 Bartupuram 
##                        677                        296 
##                     Baruva                 BasalDoddi 
##                       4503                       1342 
##                  BASAPURAM                 Basarakodu 
##                        987                       1492 
##                 BasauPuram               Basava Puram 
##                       2849                        800 
##            Basavaiahpallem                BasavaPuram 
##                        834                        663 
##                Basenipalli              Basinenipalle 
##                       1404                       1559 
##                Basinepalli                  Basinepli 
##                       1651                        694 
##            BASIREDDI PALLI             BASIREDDYPALEM 
##                        480                        767 
##                 BasiValasa          basivireddy palli 
##                        225                       1063 
##                    BasiWad                      BASKI 
##                        751                       1012 
##                    Basnagi                     BASURU 
##                        746                        966 
##                 Basvapuram               Basvayapalem 
##                        429                        223 
##                 Basvnhalli              BATAVARIPALLI 
##                       3992                        540 
##             Batchalkurpadu                Batchehalli 
##                        330                       2116 
##                Bathalpalli                  Bathaluru 
##                       7471                       2658 
##                BathinaPadu               BathulaPalli 
##                        532                        503 
##              Bathulurupadu            Bathulwarigudem 
##                        248                        748 
##             Batjangalpalem               Batlaknupuru 
##                       1247                       1107 
##             Batlapenumarru                  Batlapudi 
##                       2124                        729 
##               Batrakagollu               BATTALAVALAM 
##                        874                        666 
##                   Battanda                  Battepadu 
##                        949                       3248 
##                    Batteru                    Battili 
##                        101                       2357 
##                BATTIVALASA                  BattuPadu 
##                       1091                        161 
##                 battupalli                 Battupalli 
##                         73                        286 
##                  Batupuram                  BATUPURAM 
##                        362                        679 
##                  Bavapuram               Bavayipalena 
##                        205                       1567 
##                  Bavipalli                Bayanapalli 
##                        735                       1533 
##                BAYANAPALLI          BAYATAKODIYAMBEDU 
##                       3512                       1120 
##                 Baychigeri            Baylukinchanagi 
##                       1543                       1776 
##                BayTalPuram               BAYYANAGUDEM 
##                        957                       4468 
##               BAYYANAPALLI          BAYYAPPAGARIPALLE 
##                        374                       1770 
##               BayyapuKodur                 BEDADANURU 
##                        647                        176 
##                   Beduduru                Bedusupalli 
##                        702                       1342 
##            BEECHUVARIPALLI            BeemaBoinaPalem 
##                        422                        922 
##                BeemaGundam                BEERAKUPPAM 
##                       1139                       1296 
##                     Beeram                   BEERANGI 
##                        735                       1961 
##                  BEERAVOLU                 BEESUPURAM 
##                        576                       1120 
##                BegamPettah                Begglipalli 
##                        432                       1222 
##                Bejat Puram                       Beji 
##                       1557                       1124 
##                  Bejipalli                  Bejipuram 
##                        141                       1347 
##                Bejiputtuga                    BELAGAM 
##                       1542                        717 
##                    Belamam        Belamara PallValasa 
##                        779                       1762 
##                    BELDONA                Bellamkonda 
##                       1211                       4849 
##        Bellankondwaripalem                  Bellukola 
##                       1297                        154 
##                  Bellupadu                 Belluptiya 
##                        313                        597 
##                     Belodu                 BELU PALLI 
##                       2554                       2098 
##                  Beluguppa                      BELUM 
##                       5609                       2233 
##           BELUM SINGAVARAM                    Benakal 
##                        715                       1121 
##                   Benarayi            Bendamurlalanka 
##                        601                       3928 
##                  Bendapudi                      Bendi 
##                       5405                       1408 
##                  BeniGaeRi                    Benkili 
##                        807                        964 
##       BENNA BHUPALA PATNAM                  Bennavolu 
##                        733                       1068 
##        Besiramchandrapuram                Bestarpalli 
##                        738                       3125 
##                Bestavemula              BESTAWARIPETA 
##                        958                       1518 
##                Bestwaripet                Betamcherla 
##                       2937                      17780 
##                  Betapalli                  Bethapudi 
##                       2124                       2195 
##                  BETHAPUDI               bethayapalli 
##                       2443                        320 
##                   Betpalle                    Betpudi 
##                        318                       1797 
##                   Bevinhal               BHADRAMPALLI 
##                        419                        714 
##                Bhadrawaram                     Bhadri 
##                       1506                       1086 
##                BHADRIPALLE           BHAGAVANDAS PETA 
##                       1225                        277 
##              Bhagavanpuram       Bhageerdhapurankolni 
##                        186                        546 
##  Bhageerdhipuram Agraharam              Bhagvan Puram 
##                        343                        784 
##             Bhairavapatnam                Bhairavaram 
##                       1151                       1714 
##                Bhairipuram                BHAIRIPURAM 
##                        998                        438 
##               Bhakarapuram               BHAKARAPURAM 
##                        644                        280 
##     Bhallukhanudivaripalem                    Bhamini 
##                        524                       1400 
##               Bhanumukkala               BHANUMUKKALA 
##                       1451                       7787 
##                 Bharanikam                 BharaniKam 
##                       1112                        302 
##               Bhaskarpuram                 BhastiPadu 
##                        695                       2081 
##             Bhatlamaguturu               BhatlaPalika 
##                        698                       1320 
##                   Bhatluru                Bhatnavilli 
##                        948                       3042 
##                Bhatrupalem                Bhattiprolu 
##                        397                       5421 
##                    Bhatuva           Bhavadevarapalli 
##                       1658                       1921 
##                BhavanaPadu       BHAVANI SANKAR PURAM 
##                       1277                        540 
##            BHEEMAGANIPALLI                   BheemaLe 
##                       3257                       1410 
##              Bheemanapalli           BHEEMANDORAPALEM 
##                       3452                        616 
##                BHEEMAVARAM                  BHEEMPOLU 
##                        751                       1364 
##               BheemuniPadu             Bheemunipatnam 
##                       1551                      10008 
##            Bhichiganipalli                 Bhidupalli 
##                       2160                       2016 
##                  Bhimadole           Bhimakrosu Palem 
##                       4998                        859 
##               Bhimalapuram                 Bhimavaram 
##                       3223                      11352 
##                 BHIMAVARAM            Bhimavarapukota 
##                      89438                       1884 
##                    Bhimolu                  Bhimpuram 
##                       1659                        433 
##            Bhimulwaripalem            BHIMUNI CHERUVU 
##                       1160                        476 
##              Bhimwarappadu               Bhirangunta. 
##                       1016                       1242 
##                 Bhogapuram          BhogiAreddy Palli 
##                      22630                       1000 
##    Bhoginepalli-Palacherla                    Bhogolu 
##                       1402                       1021 
##                    BHOGOLU               BhogSamudram 
##                       2372                        277 
##                   BHOJANAM              BhomaiahPalli 
##                        433                       2258 
##             BhoodeviPettah         Bhoomi reddi palli 
##                        175                        413 
##             BhoopathiPalli              BhoopSamudram 
##                        987                       3447 
##      BhoopSamudram-H-Puram                BHRUGUBANDA 
##                        757                       3191 
##                Bhudevipeta            Bhujabalapatnam 
##                        455                       3439 
##                 Bhumnpalli         BHUPALA RAJA PURAM 
##                        720                        215 
##               Bhupalpatnam                  Bhupnpadu 
##                       3594                       1178 
##          Bhurada Venkatpur              Bhushanagulla 
##                        596                       1105 
##               BhuvanaPalli             Bhuvngiripalem 
##                       4249                        450 
##                  Biccavolu                     Bidimi 
##                       8542                       1333 
##              Bidinamcherla                Bidirkuntam 
##                       1132                        569 
##               Bijinivemula                Bijinvemula 
##                       1339                       1060 
##                 Bile Hallu                  Bilekallu 
##                        860                       1198 
##                    Biliani                Bilklguduru 
##                        266                       2973 
##                 BILLAKURRU                Billalvlasa 
##                       3429                        681 
##               BillaNanduru                Billanpalle 
##                       1876                        996 
##           BillaPadu Rurala                  BILLUMADA 
##                       1308                        585 
##                 BingiDoddi               Binginapalli 
##                        364                       8991 
##                    Binnala                 Biradavole 
##                        349                       1018 
##                 BIRADAWADA                  Birapuram 
##                        936                       1197 
##                   Biravolu                   BIRLANGI 
##                        629                       1709 
##                 BISAIPUTTU                 Bisanatham 
##                        661                        494 
##           Biswalichowkipet                   Bitiwada 
##                        342                       1272 
##                 BITRAGANDA                  BitraPadu 
##                       1292                        931 
##                BIYYALAPETA               BOBBANAPILLI 
##                        987                        692 
##                Bobbarlanka               Bobbellapadu 
##                        291                        589 
##                 Bobbepalli                 Bobbilanka 
##                       3293                       3017 
##                    Bobbili              BobbiliPettah 
##                      34115                        801 
##                Boda bandla            BODAGUTTA PALLI 
##                       1310                       1324 
##             Bodamettapalem                BodanamPadu 
##                        458                        807 
##                   BodaPadu                  BodaPalem 
##                       1948                       1034 
##               Bodasingipet                   Bodavada 
##                        376                        467 
##          Bodavadmandagunta               Bodaya Palli 
##                       1177                        699 
##                 BODDAGANDI                     Boddam 
##                        418                       4977 
##                Boddanpalle                  Boddapadu 
##                       1305                       3698 
##                  BODDAPADU                 Boddawaram 
##                        794                       2248 
##                   Boddbada                BoddeCherla 
##                        665                        688 
##                 BODDEPALLI                   Boddguda 
##                        768                         43 
##              BoddikurApadu                   Boddkali 
##                       2506                        564 
##                   Boddpadu              Boddulurupadu 
##                        453                        457 
##                    Bodduru             Bodduvanipalem 
##                        754                      10298 
##             Bodduvanipalle             Bodduwaripalem 
##                        637                       1817 
##                 Boddvalasa               Bodemmanooru 
##                        622                        968 
##                   Bodepadu              BODEVARIPALLI 
##                        331                       1835 
##    BODIGUDEM H/O.PARIMPUDI               Bodigudipadu 
##                       1036                       1235 
##                  Bodipalem         BODIREDDYGARIPALLI 
##                       1333                       1288 
##             Boditippanpadu                   BODLANKA 
##                        675                       1458 
##                  Bodlapadu                  Bodskurru 
##                        201                       2946 
##                 Bodugallam                   BODULURU 
##                        630                        779 
##         BODUMALLUVARIPALLE                 BODUVALASA 
##                        458                        803 
##                    Bodwada               Bodwaripalli 
##                        232                        692 
##                  Bogabanda                Boganampadu 
##                        542                       1276 
##                  Bogbaheni                 Boggupalli 
##                        327                        577 
##                     Bogolu                 Bogsmudram 
##                      14647                       2080 
##         Boina CheruvuPalli              Bojjaraigudem 
##                        728                        282 
##                   Bokinala             BOKKASAM PALEM 
##                        580                        275 
##                Boksampalli                  BOLAGONDA 
##                        518                        590 
##             Bollana Guddam                  Bollapadu 
##                       2839                        816 
##                 BollaPalli                 Bollavaram 
##                       4249                       2676 
##                 Bollawaram             Bolleddu Palem 
##                       5198                       1938 
##                 Bollupalli                   Bolugota 
##                       1048                        667 
##                 Bolvanipli                 BOMAIPALLE 
##                        509                       1238 
##       Bommagondana Hazhzhi                Bommana Hal 
##                       4513                       2739 
##               Bommanampadu               BommanaPalle 
##                       2455                        492 
##            BOMMARAJU PALLE             BommarajuPalli 
##                        625                        707 
##              BOMMASAMUDRAM                 BommaVaram 
##                        844                       2533 
##                Bommeparthi                    Bommidi 
##                        767                       1617 
##                 BOMMIDODDI                    Bommika 
##                       1672                        151 
##                    BOMMIKA    Bommika Jagannadhapuram 
##                        635                       1302 
##           BommiNaiduValasa               Bomminampadu 
##                        625                       1855 
##            BommireddiPalle            BommireddiPalli 
##                        715                       1220 
##                  Bommuluru        Bommuluru Khandrika 
##                       2916                        859 
##                    Bommuru             Bommuvanipalem 
##                      11281                        332 
##                     Bonala                  Bonamaali 
##                       1226                        149 
##                   Bonamala                    Bonangi 
##                        914                        911 
##                    Bondada               Bondaldinane 
##                       5921                        505 
##                Bondaldinne                BondalKunta 
##                        345                        847 
##                 Bondalpadu                 Bondalwada 
##                        287                       1521 
##                  Bondankal                 Bondapalli 
##                       1370                       3498 
##                 BONDAPALLI               Bondimdugula 
##                       2056                       1886 
##                Bondugudena                       BONI 
##                        469                        676 
##               Bontalkoduru                Bontalpalli 
##                        578                       1764 
##          Bonullachiruvella                  Bonupalli 
##                       1046                        851 
##                BOORLAPALLE               BooruguGudem 
##                       1979                        428 
##                   Boppadam                   Boppapur 
##                       1516                        392 
##            BOPPARAJU PALLI              BOPPASAMUDRAM 
##                        546                        439 
##               Boppayipuram                 Boppepalle 
##                        357                       2255 
##                    Boppudi               BORAGAVALASA 
##                       1750                        243 
##                   Borbanda                Borigivlasa 
##                       1729                       1453 
##                  BORIVANKA                      BORRA 
##                       3089                       2252 
##              Borramam PETA                Borramamidi 
##                        355                        664 
##                Borramapata                Borrampalem 
##                        561                        461 
##                BORRAMPALEM             Borrapotupalem 
##                       3076                        481 
##                  Borubadra                  BoruPalem 
##                       1795                        550 
##                  Borvancha                   BOSIBEDA 
##                       1027                        645 
##              Botikarlapadu             Botimeedapalli 
##                        386                        836 
##               Botlacheruvu                Botlaguduru 
##                        444                       1359 
##               Bottadsinagi               BOTTAM DODDI 
##                        316                       1222 
##                  Bouruvaka           BOVILAVARI PALLI 
##                        330                        911 
##                      BOWDA                  Bowluvada 
##                        381                       3271 
##         BOYACHINAGNA PALLI               Boyadgumpula 
##                        595                        501 
##                Boyalkuntla                 Boyalpalli 
##                       2399                        699 
##                Boyamdugula                Boyanapalli 
##                        171                        431 
##                 Boyanpalle                  Boyapalli 
##                       1008                        674 
##                  BOYAPALLI                 Boyarevula 
##                        221                       1747 
##             BOYILA KINTADA                  Boyinpudi 
##                        569                        842 
##                   Boyitili          Brahaman Erragudi 
##                        951                       3526 
##             Brahaman Palli             Brahaman Plale 
##                       2628                        901 
##              BrahamanDoddi              BrahamanKodur 
##                       1680                       2048 
##              BrahamanPalli             Brahma Napalle 
##                       3459                        490 
##          Brahma sameadhyam                Brahmadevam 
##                       4333                       3526 
##            BRAHMAN THANGAL             Brahmana Palli 
##                        429                        756 
##             BRAHMANA PALLI              Brahmanakraka 
##                        522                       3601 
##              Brahmanapalle              Brahmanapalli 
##                       1628                       5968 
##              Brahmanatarla              Brahmangudena 
##                       1925                       3947 
##             Brahmankotkuru               Brahmanpalli 
##                       3720                       2201 
##              Brahmeshwaram           Bramhabotlapalem 
##                        353                        905 
##         Bramhadevarachenlu             BRAMHANA PATTU 
##                        273                       1500 
##              BRAMHANAPALLE                Brundavaram 
##                       1617                        194 
##              Bubusanipalle       BUCCHINAIDU KANDRIGA 
##                        383                       1675 
##                   Bucharla          BuchchirajuPettah 
##                        974                        444 
##                BUCHI PALLI              BUCHIVANETHAM 
##                        418                        758 
##                 BUCHUPALLI                   Budadham 
##                       1241                        681 
##                    Budambo                  Budampadu 
##                        348                       3454 
##               Budarisinagi                Buddalpalem 
##                       1121                        494 
##                Buddidlvagu                  BUDDIPETA 
##                        683                        503 
##                BuddiValasa      BUDDIVALASA AGRAHARAM 
##                        245                        329 
##           BUDDULAVARIGUDEM                     Budedu 
##                        177                        543 
##                   Budgaray            budgatala palem 
##                        147                        546 
##                    Budgevi                 BudhaVaram 
##                       1350                       3797 
##        BUDHITI REDDI PALLE                 BUDIDAVEDU 
##                        334                        334 
##                  Budidpadu                  Budigumma 
##                       1665                        945 
##                     Budili                    Budithi 
##                       4841                       2238 
##                  Budmgunta                     Budnam 
##                       2198                        500 
##                Budnampalli                    Budpadu 
##                       1020                        246 
##                   Budralla               Budrayavlasa 
##                       2502                       2956 
##          Budtanpallirajeru                Budtnapalli 
##                        427                        883 
##                  Budtvlasa                   Budumuru 
##                        706                       1121 
##                     Buduru                 BUDURUVADA 
##                       2153                        338 
##                    Budwada             Buggaletipalli 
##                       7994                        351 
##               Bugganipalle                 Buggatanda 
##                       1448                        464 
##                  Bugupalli           Bujabuja Nellore 
##                        613                       5765 
##                  Bujanooru                BukkaCherla 
##                       1263                        522 
##                Bukkapatnam                BUKKAPATNAM 
##                       6360                       1630 
##                 bukkapuram                 Bukkapuram 
##                        728                       4094 
##                 BukkaPuram                    Bukkuru 
##                        312                        620 
##                     Burada                  BuradPadu 
##                        546                        369 
##                     Buraga                BURAGAMANDA 
##                        178                       1532 
##             BURAKAYALAKOTA                Buran Doddi 
##                       3293                       2895 
##                  BuraVilli         Burdgli Kothapalem 
##                        517                        552 
##                     Burgam            BURIDIKANCHARAM 
##                       4086                       2094 
##                Buridivlasa                      Burja 
##                        619                       3672 
##                      BURJA                  BurjaPadu 
##                       1565                       2951 
##    BurjaValasa MettaValasa             Burraeddipalle 
##                       1060                       1031 
##                 BurriPalem                   Burugula 
##                       1642                       2034 
##                Burugupalli                 Burugupudi 
##                       1099                       6479 
##                Buruguvalem                   Burujola 
##                       2843                        387 
##                   Burujula                Burujupalli 
##                       1451                        260 
##                 BURUJUVADA              BUSARAJUPALLI 
##                        744                        473 
##                Busayavlasa                  BUSIKONDA 
##                        496                        347 
##            Busireddi palli            BUSIREDDY PALLE 
##                        623                       1043 
##                  Busrpalli              Butchaiahpeta 
##                       1213                       2661 
##               Butchampalli                Butchampeta 
##                        343                       1389 
##                BUTCHAMPETA                BUTTAIGUDEM 
##                       2298                       1628 
##              Butumillipadu                Byadlahalli 
##                        257                       1492 
##                 Bydlapuram                   BYLAPUDI 
##                        582                       1292 
##                  Bynepalli                    Bypalli 
##                        613                        844 
##                  Byrapuram                       Byri 
##                        576                        599 
##                  Byripuram                Byrivanipet 
##                        884                        879 
##              Byrluti Gudem                 Byrsmudram 
##                        396                       2050 
##               Bytmanguluru               C Bandapalli 
##                        218                        377 
##               C BandaPalli               c kothapalli 
##                        763                        213 
##                C L N PALLE              C MALLA VARAM 
##                        517                        770 
##                 C. Belagal                C. K. Dinne 
##                       5248                       4733 
##             C..Kodigepalli              C.BANADAPALLI 
##                       1378                        370 
##                   C.C.Revu              C.GOPULAPURAM 
##                       1001                        423 
##   C.H. Bhoopathi Agraharam                  C.H.Rajam 
##                       1129                        702 
##                  C.M.Puram                C.RAJUPALEM 
##                        909                        673 
##              C.S.AGRAHARAM                 C.S.R.PETA 
##                        270                        103 
##              Calingapatnam                    Calluru 
##                       4386                      10655 
##               CalluruPalli     CanPak(AyyannaPettah ) 
##                       1509                      11014 
##               CanSaanPalle                    CellPak 
##                        725                       2510 
##                Cement Ngar               CH.AGRAHARAM 
##                       3059                        322 
##             CH.B.AGRAHARAM                     Cha gi 
##                        794                        424 
##                   CHA VALI                  CHAARAALA 
##                        374                        992 
##                    Chabala                    Chabolu 
##                       2070                        941 
##                Chadalavada                   CHADALLA 
##                       1541                       1263 
##                     Chadam                   Chadlada 
##                       2044                       1397 
##               Chagalamarri                  CHAGALERU 
##                      13536                       2106 
##                   Chagallu               ChagantiPadu 
##                      16418                       2602 
##               Chagarapalli                   Chagleru 
##                        781                       3206 
##                    Chagnam                   CHAGOLLU 
##                       2520                        558 
##               Chakalakonda               CHAKARAPALLI 
##                       1005                        710 
##                Chakicherla                 Chakipalli 
##                       1867                       2001 
##                 CHAKIPALLI                  Chakirala 
##                        708                       1504 
##                 Chakivlasa                Chakkaralla 
##                        927                       1397 
##                 CHAKKAVADA          ChakraDevarapalle 
##                        154                        766 
##              ChakRajuEmula        ChakravarthulaPalle 
##                       2594                        742 
##                Chakrayapet              Chalam Valasa 
##                       4568                        393 
##         ChalamaKuntlaPalli              CHALAMANGALAM 
##                        888                       1410 
##                   Chalikam           Chalivendrapalem 
##                        106                        741 
##               Chalivendula                   Chalkuru 
##                       3515                       1553 
##         Challachintalapudi             Challagirigala 
##                       1464                       1029 
##               Challagundla             Challaiahvlasa 
##                       2703                       1167 
##        CHALLAM NAIDUVALASA                Challapalli 
##                        706                      14817 
##                ChallaPalli                 Challapeta 
##                       1504                        981 
##             CHALLAVANIPETA                Challgariga 
##                       1738                        686 
##               Challivendri            Challwari Palli 
##                        834                        248 
##                 Chalvemula               Chamalagondi 
##                        863                       1074 
##               Chamallamudi                  CHAMANERU 
##                        902                        441 
##                   Chamarru                   Chamdala 
##                       5354                       1391 
##           Chamlachenubailu                Chamlapalli 
##                        611                        532 
##                 Chamlpalli                   Chamluru 
##                        596                       3131 
##                 Chamlvlasa               Chammachinta 
##                        145                       1438 
##                  Chamwaram                  Chanadala 
##                       1755                        658 
##                   CHANDAKA            Chandaka Cherla 
##                       1107                       2506 
##                CHANDALANGI                 Chandaluru 
##                        195                       3800 
##                   Chandana                 Chandanada 
##                       1911                        544 
##                Chandaparru                Chandapuram 
##                        495                        348 
##              Chandarlapadu                Chandawaram 
##                       5050                       2895 
##         ChandersekharPuram              Chandiputtuga 
##                       1091                        279 
##                   Chandole                   Chandoli 
##                       5595                        926 
##               Chandragudem           ChandraiahPettah 
##                       2142                        226 
##             Chandrajupalem                  Chandrala 
##                       2558                       2154 
##         CHANDRAMAKULAPALLE            Chandramampalli 
##                       2265                       1232 
##               ChandramPeta             ChandramPettah 
##                       1209                        374 
##                ChandraPadu               Chandrapalli 
##                       1402                       1095 
##               Chandrapdiya             CHANDRAYYAPETA 
##                        430                        681 
##               Chandrupatla                 Chanduluru 
##                       1014                       2082 
##             Chandulurupadu                   Changudi 
##                        531                       1130 
##                  Chanmilli          Channarayunipalli 
##                       2497                       1281 
##                 Chanubanda                Chanugondla 
##                       1158                       5569 
##                    Chapadu                    CHAPARA 
##                       2500                       2325 
##                    Chapiri                 Chaplmdugu 
##                       1666                       1162 
##                 Chaplpalli         Chappabutchamapata 
##                        448                        724 
##             CHAPPIDI PALLI            Chaprayabinnidi 
##                       1503                        587 
##            Chapurallapalli             CharlaGudipadu 
##                        308                       1915 
##             Charndasupuram                 Charupalli 
##                        272                       1484 
##                 Chatagotla                 Chataparru 
##                        588                       2179 
##              CHATAYAVALASA                Chatlamitta 
##                        253                        935 
##                 CHATLAVADA                Chatragadda 
##                        359                       1100 
##                    Chatrai                    Chatram 
##                       1421                       3268 
##             Chattannawaram                     Chatti 
##                        456                        715 
##                Chatukupadu                CHAVADIKOTA 
##                        773                        206 
##                    Chavali                    CHAVALI 
##                       3460                        691 
##                ChavaliPadu              CHAVARAMBAKAM 
##                        623                        592 
##             CHAVITIDIBBALU                CHAVITIPETA 
##                        787                        369 
##            Chavtappacherla           Chavtgogul palli 
##                         73                         91 
##                 Chavtpalle                Chavtputedu 
##                        908                        645 
##              Chavvaripalle               Che rlopalem 
##                        639                        979 
##     che yyyeru gunnepallli           chebiyyam valasa 
##                       2072                        103 
##                   Chebrole                 Chedalwada 
##                      19427                       1533 
##               CHEDULAPAKAM                   Chedulla 
##                        274                       1154 
##                  Cheduwada               CHEEDI PALLI 
##                       1060                        935 
##              Cheedigummala                 CHEEDIKADA 
##                       3225                       2553 
##                CHEEDIPALEM              Cheekatipalli 
##                        256                        404 
##              CHEEKUMADDULA                Cheelepalle 
##                       1249                        326 
##               Cheemakurthi               Cheemalapadu 
##                      14300                       4699 
##              CHEEMALAPALLI              Cheemalapenta 
##                        758                        724 
##             CHEEMALAVALASA          Cheemanayanapalle 
##                        984                        828 
##                     Cheepi                 Cheepinapi 
##                        776                       1072 
##              Cheepurupalli                   Cheerala 
##                      19405                      63227 
##                Cheeravelli                 CHEETUPALI 
##                        702                        424 
##              Chegara palli             Chegireddipadu 
##                        755                        174 
##              CHEGONDAPALLI            CheinnaKkaPalli 
##                        427                       1446 
##          CheinnaMukkapalli               CheinnaPuram 
##                       2103                        974 
##               CheinnaVaram                   Chejarla 
##                        555                       6185 
##               CHEKALACHENU                Chekkapalli 
##                        558                       1014 
##               ChekkaValasa               Chekkunatham 
##                        378                       1223 
##                 Chekurpadu               Chelamcherla 
##                        696                       2280 
##           Cheldiganiapalle               Chelikampadu 
##                        268                        810 
##            CHELIKANIVALASA                 Chelimella 
##                        127                       1053 
##              Chelimenhalli               CHELLA PALLI 
##                        771                        918 
##        Chellaiah Agraharam               CHELLAM PETA 
##                        109                        305 
##                CHELLAPALEM              Chellayapalem 
##                       1101                        995 
##                   Chelluru                   CHELLURU 
##                       1372                       4930 
##  CHELROPALLI KANDRIGA (UI)                  Cheluvuru 
##                        436                       1502 
##              Chembadipalem                   CHEMBEDU 
##                        554                       1884 
##                   Chemidti               Chemmumiapet 
##                       1097                      19973 
##                    Chemudu                Chemuduguda 
##                       1472                        699 
##                Chemudupadu              Chemullapalli 
##                        952                       1989 
##                    Chemuru      CHENCHU RAJU KANDRIGA 
##                        213                       1095 
##                CHENCHUGUDI                   Chendodu 
##                        659                       1626 
##                  Chendurti             CHENGAM BAKKAM 
##                       2961                        338 
##                Chenguballa                 Chenigunta 
##                        956                       1065 
##               Chenitikallu                   CHENN RI 
##                        750                        513 
##            ChennaiahValasa               Chennampalle 
##                        575                       6532 
##               ChennamPalle               Chennampalli 
##                        925                       1194 
##           CHENNAPANAIDUPET         Chennapnayunipalle 
##                        725                        196 
##                CHENNAPURAM             ChennaraoPalem 
##                       1808                       1001 
##           ChennaReddipalli           CHENNAREDDY PETA 
##                       1678                        447 
##                Chennavaram            Chennawarappadu 
##                        259                        600 
##              Chennayapalem              Chennayapalli 
##                       4273                        336 
##           Chennekothapalli                 Chennipadu 
##                       5491                        956 
##        Chennubotlwaripalem                Chennupalli 
##                        459                        658 
##                CHENNUPALLI                    Chennur 
##                       1178                      18904 
##                  Chennur-i                Chenulvlasa 
##                       8561                        186 
##        Chepala Thimmapuram                    Chepuru 
##                       1047                       1195 
##                   Cherakam               Cherakupalli 
##                        705                        574 
##                Cherakuwada                CHERIKANDAM 
##                       3384                        383 
##                    CHERIVI                Cherlapalli 
##                        748                        754 
##               Cherlo palle               CHERLO PALLI 
##                        918                       1532 
##              Cherlokothuru                Cherlopalem 
##                        965                       1553 
##                Cherlopalli                CHERLOPALLI 
##                       8633                       3545 
##     Cherlopalli H/o Maruru             Chernuppalpadu 
##                       3082                       1448 
##              CherukuCherla               Cherukulpadu 
##                       1638                       1812 
##               Cherukumilli                Cherukumudi 
##                       3188                       1712 
##               cherukupalli               Cherukupalli 
##                        296                        250 
##                   Cherukur                  Cherukuru 
##                       1073                       6859 
##                CHERUKUVADA           CHERUKUVARIPALLI 
##                        427                       1224 
##                    Cheruvu         Cheruvu Madhavaram 
##                       3041                       1218 
##          Cheruvukommupalem    CHERUVUMUNDHARAKANDRIGA 
##                       2964                        249 
##               CHERUVUPALEM               CHERUVUPALLI 
##                        274                       1504 
##                  CHERUVURU           CHERVUKOMMUPALEM 
##                        733                       1116 
##                CHETHAPENTA          Chetla Mallapuram 
##                        300                        527 
##              CHETLATHANDRA                Chetnepalli 
##                        438                      10345 
##                Chetnihalli              Chettunnapadu 
##                       1694                       1085 
##                ChettuPalli              Chettupodilam 
##                       3221                        394 
##                  Chevendra  Chevitiwaripalli-Yam.Pall 
##                       1665                        847 
##                    Chevuru                  Chevuturu 
##                       2958                       1295 
##                   Cheyyeru                    CHIDIGA 
##                       5572                       4802 
##                    Chidika                    Chidimi 
##                        297                        413 
##                 Chidipalem                    Chidipi 
##                        489                        651 
##          Chidipiralladinne                  Chidipudi 
##                        186                       1081 
##                 Chidivlasa                  Chidumuru 
##                       1948                        525 
##                Chigicherla                    Chigili 
##                       2501                        702 
##                  Chigturpi                ChiguruCoat 
##                       1769                       1896 
##          ChiguruKothapalli              Chigurumamidi 
##                        326                        680 
##                ChiguruPadu                CHIGURUWADA 
##                       2122                       1831 
##                 Chiiahpadu                 CHIKILINTA 
##                       2024                        599 
##                   Chikkala               Chikkalvlasa 
##                       3952                        491 
##             CHIKKANA PALLI         Chikkapalle Thanda 
##                        452                        310 
##                Chikkawaram                Chiklguriki 
##                        884                       1188 
##           Chiktimani Palli                CHIKUPANASA 
##                        823                        609 
##                   Chikvolu              Chilakalapadu 
##                       1914                       1124 
##             CHILAKALAPALLI              Chilakalapudi 
##                       1755                        481 
##       Chilakalapudi Rurala         CHILAKALAVANIPALEM 
##                        448                        770 
##              CHILAKAMAMIDI             CHILAKELAGEDDA 
##                        699                        867 
##                 Chilamkuru                 Chilankuru 
##                        382                       7163 
##                 CHILAPALLI                Chile Palli 
##                        636                        589 
##              Chilekampalli        Chilikuruvari Gudem 
##                       2795                       2362 
##         Chilkacherla Gudem                   Chilkala 
##                        385                        436 
##                   Chilkamu                 Chilkldona 
##                       1525                       1871 
##                  Chilkluru                  Chilkpadu 
##                        504                       1379 
##                 Chilkpalem           Chillaboyinpalle 
##                       1067                        322 
##                Chillakallu                 Chillakuru 
##                       4671                       2161 
##                 CHILLAKURU          CHILLAMAKULAPALLE 
##                        970                        594 
##                 Chillamuru                 Chillanagi 
##                        537                       2306 
##                 Chillapeta                Chillapuram 
##                       1899                        634 
##         chillavandla palli             Chillwaripalli 
##                        340                        783 
##              Chilmanuchenu                 Chilmathur 
##                        953                      10737 
##                Chilmathuru                  Chilmkuru 
##                        814                        594 
##                 Chilmnooru                  Chilukuru 
##                        586                       1772 
##               CHILUMATTURU                  Chilumuru 
##                        454                       1345 
##                  Chiluvuru               CHIMALAPENTA 
##                       5257                        194 
##                    Chimata                Chimlapalli 
##                        642                       4171 
##                 Chimlmarri            China Agraharam 
##                       1389                        739 
##               CHINA AMIRAM               China Anklmu 
##                       3674                        401 
##             China Annaluru            China Avutpalli 
##                       3920                        907 
##          China Burada Peta            CHINA GADAVALLI 
##                        956                       1031 
##           China Gollapalem            CHINA GOPAVARMA 
##                       3901                       1099 
##               China Kakani             China Kamnpudi 
##                       3628                        535 
##            china kapavaram          China Kodamgundla 
##                       1854                        970 
##               China Kudhum           China mada palli 
##                       1107                        415 
##               CHINA MARIKI              China Muthevi 
##                        493                       1534 
##              China Ogirala             China Pandraka 
##                        699                       2640 
##        CHINA RAMANAYYAPETA       CHINA RAMBHADRAPURAM 
##                        917                        351 
##             China Ravipadu               China Uppada 
##                        570                       1151 
##              China Uppalam            China Vadlapudi 
##                        455                        320 
##           CHINA VELLAMILLI           China YerukaPadu 
##                        617                        712 
##           CHINABURUGUPUTTU            Chinadoddigallu 
##                       1051                       2828 
##             CHINADWARAPUDI                ChinaGanjam 
##                        441                      10682 
##              ChinaGantyada             ChinaGarlaPadu 
##                      12554                       1282 
##              Chinagonnooru                   ChinaGor 
##                        373                        356 
##              ChinaGudiPall                 CHINAHAMSA 
##                        817                        429 
##           ChinaKagitaPalli           Chinakandlagunta 
##                        125                        855 
##           CHINAKHANDEPALLI           CHINAKITTALAPADU 
##                        289                        448 
##             ChinaKothakota            ChinaKothapalli 
##                        289                       3481 
##                 Chinakraka                CHINALABUDU 
##                        824                        714 
##               CHINALATRAPI                CHINAMALLAM 
##                        735                       1742 
##               ChinaMerangi             CHINAMILLIPADU 
##                       1710                       1745 
##        Chinanagamayyapalem            ChinaNagamPalli 
##                        583                        665 
##            CHINANANDIPALLI                Chinanchala 
##                        543                        544 
##             Chinapalaparru                 Chinapalem 
##                        662                       2130 
##           ChinaPallamKiiah            ChinaPallValasa 
##                         90                       1376 
##                ChinaParimi              Chinaparupudi 
##                        751                        753 
##                ChinaPavani                ChinaRPalli 
##                        840                        724 
##              CHINATEENARLA               ChinaVangara 
##                       1158                        102 
##         Chinavenkannapalem                Chinbammidi 
##                        435                        361 
##             Chinbantupalli                   Chinbdam 
##                        446                       1262 
##                Chinbhogila                Chinchinada 
##                       1949                       1398 
##                  Chindugam                 Chindukuru 
##                        527                       2019 
##              Chinganipalli               Chingnipalli 
##                        713                       1341 
##              Chingummuluru             Chinkallepalli 
##                       1721                        536 
##                  Chinkamba                Chinmakkena 
##                        222                        440 
##               Chinmambattu              Chinmanapuram 
##                        904                        263 
##               Chinmngundam             Chinmodugpalle 
##                        369                        617 
##             Chinmusidiwada            Chinna Anjimedu 
##                       7801                        468 
##               CHINNA BAGGA            Chinna Bompalli 
##                        410                       1581 
##         Chinna Brahmadevam      CHINNA BRAHMIN STREET 
##                       1142                       1225 
##      CHINNA CHALLARA GUNTA              Chinna Cumbum 
##                        654                        984 
##             Chinna Dornala             Chinna Gonehal 
##                       1488                        446 
##               Chinna Haita           CHINNA HARIVANAM 
##                        818                       1117 
##               Chinna Hulti          Chinna Jaggampeta 
##                        661                       1763 
##         CHINNA JONN VALASA          CHINNA JONNAVARAM 
##                        540                        504 
##            Chinna Kaduburu  chinna kambi reddy gari p 
##                        853                        283 
##         CHINNA KESAM PALLI           Chinna Kondepudi 
##                        872                       4144 
##            CHINNA KOPPERLA              Chinna Madina 
##                        603                        387 
##          Chinna Malkapuram            Chinna Mamidada 
##                       2648                        545 
##           Chinna Mantanala           Chinna Marrividu 
##                         43                       1209 
##          Chinna Muppalpadu             Chinna Musturu 
##                        423                       1268 
##            Chinna Nelaturu            Chinna Orampadu 
##                        307                       6469 
##             CHINNA PANDURU          Chinna Pendekallu 
##                        603                       1911 
##             Chinna Polmada             Chinna Pudilla 
##                       2467                        876 
##       Chinna Shankarlapudi           Chinna Singamala 
##                       1750                        916 
##        Chinna Singanapalli              Chinna Tekuru 
##                       1141                       2003 
##               CHINNA THOTA              CHINNA THYYRU 
##                        542                       1507 
##            Chinna Tumbalam           Chinna Yakkaluru 
##                       2724                        987 
##          ChinnaAlavalapadu              CHINNABODANAM 
##                        743                        148 
##           Chinnaboddepalli             CHINNACHEPPALI 
##                        413                       1758 
##            ChinnaCherukuru               Chinnachowku 
##                        903                      33654 
##             Chinnadandluru               ChinnaDimili 
##                       1742                        612 
##           Chinnagollapalli            CHINNAGUJJIVADA 
##                        293                       1054 
##                CHINNAGUNTA             Chinnaguruvlur 
##                        283                        407 
##     CHINNAHARICHANDRAPURAM              Chinnahothuru 
##                        778                       1123 
##            ChinnaiahPettah            CHINNAKAM PALLE 
##                       1515                       1050 
##            chinnakam palli            Chinnakambaluru 
##                        531                       1695 
##             Chinnakojiriya           Chinnakollinlasa 
##                        243                        706 
##              Chinnakomerla               Chinnakoshta 
##                       1876                        803 
##            Chinnakothiliki                ChinnaKotla 
##                        416                        530 
##               Chinnakudala          Chinnalavunipalli 
##                        502                        275 
##               CHINNALOGIDI            Chinnamachnooru 
##                        645                        666 
##           Chinnamachupalli               ChinnaMandem 
##                       1574                       8012 
##      CHINNAMAREDDYKANDRIGA              Chinnamathuru 
##                        829                        800 
##           Chinnamattapalli              ChinnamPettah 
##                        532                        527 
##              Chinnamudiyam           Chinnamukkapalli 
##                        360                       3934 
##            ChinnannaPettah           Chinnapadmapuram 
##                        622                        779 
##             Chinnapasupula                CHINNAPATTU 
##                        367                       1119 
##             Chinnapolipaka                Chinnapolla 
##                        430                        172 
##              Chinnapsupula                Chinnapuram 
##                        307                       2253 
##                CHINNAPURAM                CHINNAPUTTA 
##                        862                        708 
##     ChinnaRamannaGariPalli           ChinnaRangapuram 
##                        679                        771 
##              Chinnarikatla         CHINNAROKALLAPALLI 
##                       1110                        610 
##                Chinnarutla                 Chinnasana 
##                         74                        476 
##              CHINNASANKALI          ChinnaShettipalle 
##                        496                        853 
##          CHINNATAMARAPALLI               Chinnatungam 
##                        138                        388 
##              ChinnaVadugur              Chinnavangali 
##                        904                       1340 
##         CHINNAVENKATAPURAM            Chinnavepanjeri 
##                        319                        409 
##             Chinnayagudena             Chinnayerasala 
##                       3498                        256 
##            Chinnayirlapadu            Chinnindrakolnu 
##                        272                       2659 
##                ChinniPalem          chinnkatterapalli 
##                        435                        187 
##          Chinnobinenipalli                Chinpachila 
##                        390                       1693 
##             Chinpannapalem                Chinplkluru 
##                        910                        560 
##              Chinpuliwarru                Chinpulleru 
##                        790                       1004 
##                 Chinsirlam                   Chintada 
##                        485                       5643 
##                   CHINTADA             Chintagumpalli 
##                        396                        658 
##             CHINTAGUMPALLI            Chintakayamanda 
##                        979                       2487 
##           Chintakommadinne                Chintakunta 
##                        618                       2830 
##            Chintal Cheruvu            Chintalabelagam 
##                        785                        754 
##            Chintalacheruvu               Chintaladevi 
##                        864                       1005 
##           CHINTALAGRAHARAM              CHINTALAGUDEM 
##                       1553                        126 
##               Chintalapadu              Chintalapalli 
##                       2816                       4420 
##                Chintalapet             CHINTALAPOLURU 
##                       2652                        700 
##               Chintalapudi               CHINTALAPUDI 
##                       4616                        674 
##             Chintalaveedhi            CHINTALAYAPALLE 
##                       1015                       1417 
##             ChintalCheruvu                Chintalgara 
##                       2790                        334 
##               ChintalGudem              Chintalgudena 
##                        192                        660 
##                Chintalmada               Chintalpalem 
##                        640                        248 
##               ChintalPalem               ChintalPalle 
##                       3700                        473 
##                Chintalpudi                 Chintaluru 
##                      10673                       3315 
##                 CHINTALURU              ChintalValasa 
##                        640                        381 
##               ChintalValli          CHINTAMAKULAPALLI 
##                       1239                        894 
##                 Chintamani               CHINTAMPALLI 
##                        412                        233 
##               Chintanlanka                 Chintapadu 
##                        971                        880 
##                Chintapalli                CHINTAPALLI 
##                      16993                        224 
##          ChintapalliPettah                Chintaparru 
##                        350                       2029 
##                 Chintapudi                 CHINTAPUDI 
##                        184                       1689 
##           Chintareddipalem             Chintarlapalle 
##                       3341                       1575 
##        Chintauttarayapalli                Chintawaram 
##                        552                       1042 
##          Chintayagaripalem                 ChintGunta 
##                        707                       1210 
##         CHINTHALABADAVANGA            Chinthalajuturu 
##                        345                       1094 
##             Chinthalapalem           Chinthalatmakuru 
##                       1779                        649 
##              CHINTHAPARTHI          CHINTHLAVARIPALLI 
##                       3210                        203 
##                 ChintKunta                   CHINTOOR 
##                       4602                       1957 
##                   ChintPak  ChintPak Shiwaru Shitaiah 
##                        688                        790 
##             ChintRajuPalli                Chintummidi 
##                        658                        304 
##                  Chinvanka                 Chinyadara 
##                        787                        372 
##                   Chippada                 CHIPPAGIRI 
##                       4017                       1799 
##               Chippalmdugu               Chipurlapadu 
##                        336                       1387 
##              Chipurugudena               Chipurupalli 
##                       2133                       1208 
##                  Chiramana              Chirichintala 
##                       1680                        812 
##                  Chirivada                Chirldinane 
##                        931                        766 
##                 Chirravuru                 Chirraynam 
##                       2017                        715 
##                 Chirtankal                Chirtapalli 
##                        727                        788 
##                  Chirtpudi               Chiruguvlasa 
##                       1904                        959 
##              Chirukurupadu               Chirumamilla 
##                        784                        759 
##             Chiruman Doddi                  Chiruvolu 
##                        478                        176 
##  Chiruvolu Lanka Dakshinam    Chiruvolu Lanka Utharam 
##                        829                       1191 
##                 Chithaluru                 CHITHAPARA 
##                       1884                        974 
##                  Chithrada         chitimiti chintala 
##                       4808                        280 
##                   Chitluru                ChitraChedu 
##                       2349                       1093 
##      ChitraCoat Boddvalasa                    Chitram 
##                       1017                        345 
##              Chitrenipalle                 Chittamuru 
##                       1364                       3001 
##                  Chittapur                Chittapuram 
##                       1374                       1553 
##              Chittaripuram                Chittathuru 
##                        299                       1884 
##                 CHITTATOOR                CHITTAVARAM 
##                        472                       2422 
##                   Chittedu                   Chittela 
##                       1354                       2369 
##                 Chittelaba                Chittempadu 
##                        717                        496 
##            CHITTEYA VALASA              ChittiahPalem 
##                        162                        819 
##               Chittiguduru             Chittigunkalam 
##                        370                        449 
##            Chittipudivlasa              ChittiVa Lasa 
##                        274                        411 
##               Chittivalasa                  Chittooru 
##                       6561                      47107 
##                  Chitturpu                   Chitturu 
##                        730                       1139 
##                    Chitvel                   Chityala 
##                       7130                       5622 
##            Chivabondapalli                   Chivatam 
##                       1596                       1713 
##                  Chivgduba                   Chivkada 
##                       1298                        553 
##                Chivkerjala                   Chivluru 
##                       1021                        802 
##            Chivtamarapalli                Chiwaravuru 
##                        251                       3114 
##                Chiyyavaram                   Chiyyedu 
##                       2582                       3164 
##                CHOADAVARAM         Chodamma Agraharam 
##                        188                       1358 
##                 Chodavaram                 CHODAVARAM 
##                      20430                       2349 
##               Chodayapalem                 Chodimella 
##                       1866                       1684 
##                 CHODIPALLI                  Chodpalli 
##                        733                       3230 
##                Chodsmudram                  Chodvaram 
##                       1129                       1123 
##                    Chodyam               CHOKKAMADUGU 
##                       1114                        421 
##               Chokkanhalli                 Chollanagi 
##                        137                       2350 
##               Chollangipet                Chollapadam 
##                       2239                        999 
##                 Chollavidu                  Cholmarri 
##                       1472                       1417 
##                Cholsmudram                Chompapuram 
##                        868                        300 
##                     CHOMPI              Chopparametla 
##                        760                        142 
##                  Choppella         Choppramannagudena 
##                       6427                        551 
##                 Chorampudi                   ChorGudi 
##                       1939                       2349 
##                 Chorlanagi                 Chorupalli 
##                       1036                        256 
##                 ChoudVaram                   ChoudWad 
##                       3380                        703 
##           CHOUTABHIMAVARAM                Choutapalli 
##                        838                       1077 
##               Chowdampalli           CHOWDANTI VALASA 
##                        293                        287 
##          Chowdariwaripalli                 CHOWDAVADA 
##                        797                       4317 
##                CHOWDEPALLE          CHOWDEREDDY PALLI 
##                       6806                        884 
##                Chowdupalli                   Chowduru 
##                       1670                       1793 
##                 Chowduwada               Chowkacherla 
##                        872                       1510 
##                 Chowlhalli                   Chowluru 
##                        580                       3102 
##                Chowtapalem                chowtapalli 
##                        810                        954 
##            Chowtkuntapalli                  Chowtkuru 
##                        951                       1563 
##                 Chowtpalle           Chowtpapayapalem 
##                       1234                       1836 
##              Chozhasmudram                Chuchukonda 
##                       2396                       1568 
##                      Chudi                CHUKKA PETA 
##                       1483                        346 
##  Chukkala Vani LakkmiMi Pu          CHUKKALANIDIGALLU 
##                       1561                        568 
##                  Chukkalur                CHUKKAPALLI 
##                       1842                       1271 
##               ChukkaValasa            Chunchuerragudi 
##                        426                       1182 
##                Chunchuluru                     Chundi 
##                       1284                       1142 
##    CHUTTU GUNTA RAMA PURAM                Chuttupalem 
##                        949                        407 
##                    Chuturu                       Coat 
##                        305                       1459 
##                  CoatNarVa                  CoatPalem 
##                       1153                       1200 
##                 CoGilThota                    Colluru 
##                        315                       8563 
##                  CoNaPuram                CowleyPalli 
##                        766                        688 
##                     Cumbum                     CUMBUM 
##                       7131                        731 
##                  CutVaPadu          D Narayananelluru 
##                        662                       1041 
##               D. AGRAHARAM              D. Kondapuram 
##                        671                       1661 
##               D. Kotakonda              D. Yarrawaram 
##                        954                       3169 
##                D.AGRAHARAM                  D.B.PALLI 
##                        571                        509 
##                  D.Belagal              D.BHEEMAVARAM 
##                       2034                        578 
##                  D.C.Palle              D.Cherlopalle 
##                       1749                       1928 
##                  D.G.Puram                D.G.Puttuga 
##                        376                        906 
##                  D.GONDURU                D.GOTTIVADA 
##                        834                        399 
##                  D.Hirehal                  D.Honnuru 
##                       4709                       3407 
##                  D.KOTHURU               D.Kumudvalli 
##                        527                        672 
##                  D.M.PURAM                D.Polavaram 
##                        652                       4525 
##               D.R.N.Valasa               D.RajuValasa 
##                        813                        861 
##                D.RAMAVARAM                D.SURAVARAM 
##                        821                        874 
##              D.TallaValasa       D.Tottipalli -Tavlam 
##                        901                       3002 
##                D.Vanipenta             D.VELAGAVALASA 
##                       1681                        219 
##             D.VELAMALAKOTA            D.Vengana palli 
##                       1440                       1745 
##                     Dabaru                 Dabbagadda 
##                        163                        689 
##               Dabbakupalli                   DABBANDA 
##                       1418                        328 
##                  Dabbapadu                 DABBAPALEM 
##                        659                        411 
##                 DABBAPUTTU               Dabbirajupet 
##                        394                       1057 
##         Dablyu. Govindinne         Dablyu. Kothapalli 
##                        978                       1053 
##                      Dabra                      Dabru 
##                        389                        260 
##           Daburuwari Palli                   Dacharam 
##                       2470                        891 
##                 Dachavaram                 Dachepalli 
##                        227                       7186 
##                    Dachuru                   Daddwada 
##                       2227                       1607 
##             DadiReddipalli             DADIREDDIPALLI 
##                        425                        403 
##                  DadiThota                Dadrusinagi 
##                       2553                        434 
##                   Daduluru               DAGARAVALASA 
##                       1910                        455 
##                   Dagdarti                  Daggavolu 
##                       4273                        755 
##                  Daggubadu                  Dagguluru 
##                       3430                       3038 
##                      Daida                    Dainedu 
##                       1768                        330 
##                Daivandinne                 Daivlraoru 
##                       1960                       1982 
##                  Dakamarri                    Dakaram 
##                       1486                        335 
##                 Dakkanooru                    Dakkili 
##                        578                       1215 
##                     DAKODU           Dakshene Valluru 
##                        603                       5174 
##          DALAVAI AGRAHARAM          Dalavaikothapalle 
##                        641                       3262 
##               Dalavaipalli                  Dalayipet 
##                        663                       1196 
##                Dalayivlasa                Daleshwaram 
##                        925                        109 
##                   DALIPADU                  Daliparru 
##                        861                        625 
##                 DALIVALASA                DALLAVALASA 
##                       1302                       1334 
##                  DALLIPETA                Damanapalli 
##                        827                       1256 
##                DAMANAPALLI                Damancherla 
##                        630                       1675 
##                DamaNellore               Damaracharla 
##                        984                        561 
##               Damaramadugu                DAMARAPAKAM 
##                       4068                       1386 
##                Damarapalli                DAMARASINGI 
##                       1594                        240 
##                  Damavaram                  Damegunta 
##                       2812                        705 
##                   Damgatla                   DAMINEDU 
##                       1874                       3272 
##             Damireddipalli                Dammalapadu 
##                       1884                       1960 
##               Dammanapalli                   Dammennu 
##                        633                       1157 
##                   Dampetla                    Dampuru 
##                       1360                       1466 
##                 Damrsinagi                     DAMUKU 
##                        237                       1096 
##                   Damuluru                Damunapalli 
##                       2034                        836 
##               DANAVULAPADU                  Dancharla 
##                        178                       1474 
##                DANDA PALLI          Dandalakshmipuram 
##                       1219                       1742 
##                  Dandamudi                   DANDANGI 
##                       1599                        587 
##                  Dandavolu      Dandavolu Upparapalle 
##                        212                        186 
##              DANDEM VALASA               Dandiganpudi 
##                        186                        753 
##                Dandikuppam             DANDISURAVARAM 
##                        310                        703 
##           DanduGopalapuram            Danduwari Palli 
##                        826                        565 
##             Danduwaripalli   Dangabadra (Arnada Dari) 
##                       2155                       1293 
##                    Dangeru                  Danjupayi 
##                       3045                        113 
##                DANNANAPETA                Dannannapet 
##                        763                        716 
##                 DANNUPURAM                       Dant 
##                        735                        788 
##                  Dantaluru               Danthaguntla 
##                        400                        562 
##                 Danukuwada               Dappalampadu 
##                        396                        333 
##                 Dappepalli                     DARABA 
##                       2239                        223 
##               DARAKANIPADU                  Darakonda 
##                        418                       1494 
##                   DARAPADU                  DARAVARAM 
##                        224                       1709 
##                   Dariwada                  Darlapudi 
##                        840                       2450 
##                 Darmapuram                  Darmapuri 
##                        437                       3608 
##                 Darmawaram              Darshina Mull 
##                        975                       2509 
##                Darshiparru                      Darsi 
##                       1406                      19237 
##           DarsiGuntaPettah              Dasamanipalli 
##                        636                        782 
##               dasara palle             DASARADHIPURAM 
##                        768                        464 
##                DasariPalem                DASARIPALLE 
##                       2648                        424 
##              DASARLA PALLI                Dasegounuru 
##                        577                        457 
##              Dashrdhapuram                Dasugummada 
##                        408                         64 
##                 DASUKUPPAM                Dasulapalem 
##                       1830                        650 
##            DasuManthaPuram                 DasuPettah 
##                        679                        194 
##                  DasuPuram                      DATHI 
##                        153                        718 
##                Dathirajeru                 Dattapuram 
##                        513                       1546 
##                DATTIVALASA                 Davaguduru 
##                        779                       1536 
##               DavalaPettah                   Davuloor 
##                        319                       3852 
##             DayanidhiPuram                   DeCharla 
##                        600                        435 
##                 Dechupalem                  Deepavali 
##                        726                        509 
##                  DEGALAHAL               DEGALAVEEDHI 
##                        395                        639 
##                    Degpudi                 Deiahmpadu 
##                        835                        539 
##                 Deknakonda              Demaketapalli 
##                       1030                       3029 
##               DEMUDUVALASA                   Dende Ru 
##                       2422                        878 
##                  Denduluru                  Denepalli 
##                       6460                        356 
##                    Denkada                    DeoGiri 
##                       7583                       1852 
##                 DeoNaPuram         DeoraiPalli- Bit 1 
##                        225                       1872 
##         DeoraiPalli-Bit 11                DEPPIVALASA 
##                        665                         93 
##                     Depuru                    Derasam 
##                        895                        547 
##          DESAPATRUNI PALEM          Deshpatruni Palem 
##                       1321                       7000 
##                       Deva                    Devaali 
##                       1628                        630 
##                  DEVADODDI                   Devagudi 
##                       1059                       2045 
##              Devagudipalli                 Devaguptam 
##                       1317                       3138 
##                  DevakiWad                DEVALAMPETA 
##                        527                        824 
##                DEVALAPALLI                 Devalbadra 
##                        485                        481 
##               DEVALCHERUVU             Devamachupalli 
##                       1854                        324 
##                   Devamada             DevammaCheruvu 
##                        763                        180 
##                 Devanbanda                 Devankonda 
##                       2026                       3589 
##                  Devanooru           Devanuppala Padu 
##                       1536                        724 
##                  Devapatla                   Devapudi 
##                       3594                        864 
##                  DevaPuram                Devar Palli 
##                       1816                       1198 
##            Devaragopavaram            DEVARAGUDIPALLI 
##                        875                        298 
##             Devaraju Gattu              DEVARAJUPALLI 
##                        417                        707 
##              Devarajupuram          Devarajusurypalle 
##                        504                        354 
##                 Devarakota                    Devaram 
##                        680                        256 
##             DEVARAMADUGULA                Devarampadu 
##                        605                       1470 
##                Devarapalle                Devarapalli 
##                      14897                       1676 
##                DEVARAPALLI              Devarapodilam 
##                       6613                        622 
##         Devarayabotlapalem                 Devarbanda 
##                        790                       1021 
##            DevarGudi Palli                 DevarGunta 
##                        788                        731 
##                 Devarpalem                 DevarPalem 
##                       2041                       1832 
##                 DevarPalle                DevarValasa 
##                       1675                        556 
##                DevarVemuru                Devasmudram 
##                       1098                        975 
##                  Devavaram                  Devibetta 
##                       2182                       1042 
##          DEVINENIVARIGUDEM             DevisettiPalle 
##                        404                        208 
##             DEVUBUCHAMPETA                   Devudala 
##                        528                        619 
##          Devuduvellampalli                Devulaltada 
##                        803                       2168 
##                Devulapalli               DevuniCanPak 
##                       2610                        275 
##               Devunikollam           DevuniPallValasa 
##                       1775                        369 
##                  Devupalli                  Devupuram 
##                        832                       1118 
##                     Dewada                DHANA PURAM 
##                       8128                       1374 
##      Dhanapuram-Shirekolam            Dhanianicheruvu 
##                       2471                       1864 
##               DHANYAMPALEM                DharaniCoat 
##                        628                       4099 
##               DHARBHAGUDEM             Dharmajigudena 
##                       1468                       2786 
##        DharmaLakkmiMiPuram           DharmalaxmiPuram 
##                        884                        736 
##            DHARMANILAPURAM                Dharmapuram 
##                        661                       2467 
##                DHARMAPURAM                 DHARMAPURI 
##                       1409                        804 
##            Dharmarayudupet               Dharmasagrmu 
##                       2735                       1406 
##                Dharmavaram                DHARMAVARAM 
##                      99778                       2165 
##      Dharmavaram Agraharam              Dharmawarpadu 
##                       1192                       1164 
##                DHAVALAPETA               Dhenuvakonda 
##                        730                       1177 
##         DHINNI MEEDA PALLE                 Dhulipalla 
##                       1079                       2162 
##                  Dhulipudi           Dhumantunigudena 
##                       3297                       1768 
##                  Dibbaguda              Dibbana Doddi 
##                        387                        265 
##               DibbanAkallu                 Dibbapalem 
##                       1291                       3454 
##                 DIBBAPALEM                    Dibbidi 
##                       1146                       1678 
##                     Didugu                  Digamarru 
##                       2047                       1692 
##                  Digavalli       Diguva Chintal Konda 
##                       3283                        673 
##            Diguva Deruwada       DIGUVA KANAKAM PALEM 
##                        291                        366 
##              Diguva magham               Diguva Palli 
##                        825                       1321 
##               DIguva palli             DIGUVA PUTTURU 
##                       1234                        868 
##        Diguva Tamballaplli           Diguva thadakara 
##                        285                       1762 
##            Diguvagottuvidu           Diguvakalavatala 
##                       1494                       1008 
##            DIGUVAMODAPUTTU              Diguvanetluru 
##                        458                       1311 
##                 DIGUVAPADU                DIGUVAPALLE 
##                       1134                        950 
##                Diguvatanda                 Diguvpalem 
##                        390                        210 
##                   Dimilada                     Dimili 
##                        270                       3841 
##                 Dimilijoda                   Dimiriya 
##                        797                        346 
##                  Dimmagudi                Dimmidijola 
##                       1414                        698 
##              Dinbandupuram                      Dindi 
##                        512                       3146 
##                      Dinne             DinneDevarPadu 
##                        570                       4329 
##                  DinnePadu             Dippakayalpadu 
##                       1803                       2463 
##                Dirasvancha                   Dirghasi 
##                       2087                       1943 
##               Dirishmancha                DIRUSUMARRU 
##                        491                       6235 
##                     Divili               dobbudupalli 
##                       2653                        206 
##                  Dodagatta            Doddadevarapadu 
##                        766                       1250 
##                Doddanakeri                 DoddaVaram 
##                       1343                       3874 
##                    Dodderi               Doddi Mekala 
##                       2293                       1236 
##                DODDI PALLI              Doddichintala 
##                       1333                        481 
##                 Doddipalli                 DODDIPALLI 
##                       1781                       2756 
##                 Doddipatla                 DODDIPUTTU 
##                       6866                       2959 
##                 Doddnapudi              Doddwarappadu 
##                       2460                        625 
##                    Dodiyam     Dodlaramachjaandrapura 
##                        534                        127 
##                    Dodleru             DOGGAVANIPALEM 
##                       5199                       3597 
##                  Dokipallu                 Dokisheela 
##                       6031                        855 
##                  Dokulpadu                   Dokuluru 
##                       1703                        572 
##                        Dol                  DollPalem 
##                        959                        275 
##                    DolMada                     Domada 
##                        555                        984 
##                 DomalPalli                      Domam 
##                        218                        525 
##            Dommara Nandyal                    Dommeru 
##                       3884                       6194 
##      Dommigani Gadbhavlasa                    Dompaka 
##                       1217                        245 
##                        Don                   Donakada 
##                      27697                       1449 
##         Donakada Agraharam                  Donakonda 
##                        857                        699 
##                  Dondapadu                  Dondapudi 
##                       4965                       4848 
##                  Dondavaka                 Dondlavagu 
##                       1400                        811 
##                    Donekal                DONELAPALEM 
##                       1591                       1569 
##                DONELAPALLI                   Donepudi 
##                        132                       1689 
##            Dongu Ru Valasa                Donimukkala 
##                        273                        781 
##       Donivanilakshmipuram                    Donkada 
##                       1398                        167 
##         Donkalakothapatnam              Donkalbdnanja 
##                        788                        321 
##                Donkalparta                   DONKARAI 
##                        363                        913 
##                Donkinvlasa                  Donnikota 
##                        789                       2479 
##                   Dontaali                Donthavaram 
##                        775                        736 
##                 Dontukurru                    DONUBAI 
##                       2404                        256 
##                 Doppalpudi                   Dopperla 
##                       1363                        382 
##          DORACHINTALAPALEM                 DoraMamidi 
##                        583                       1081 
##                 DORAMAMIDI                  DoraPalli 
##                        440                       1451 
##              Dorasanipalli                  Dorigallu 
##                       2691                       3243 
##                    Dornala                  Dornipadu 
##                       4415                       3332 
##                Dorsanipadu            DosakayalaPalli 
##                       1177                       2850 
##                   Dosapadu         Doslpadu Agraharam 
##                        808                        789 
##                  Dosludiki                     Dosuru 
##                       1383                        570 
##              DOULATHAPURAM               Dowlaiswaram 
##                       1044                      26343 
##                    Downuru                Draksharama 
##                       2345                       5725 
##                  Dronadula                  Dubcharla 
##                       4583                       5811 
##                   Dubgunta                   DubGunta 
##                        641                        346 
##                  DUCHERTHI                   Dudayala 
##                        935                       4376 
##                 Duddebanda                 Duddekunta 
##                       1794                       2315 
##                  DUDDEPUDI                      Duddi 
##                        278                       1809 
##                 Duddukallu                  Duddukuru 
##                        604                       4462 
##                  DUDDUKURU                 Duddupalem 
##                        250                        874 
##                  Dudekonda                    Duggada 
##                       2656                       1052 
##                Dugganpalli               DUGGASAGARAM 
##                        560                        447 
##               DUGGAYAPALLI                    Duggeru 
##                        654                        737 
##                      Duggi                  Duggirala 
##                       1777                       9453 
##              DuggiralaPadu                  Dugguduru 
##                        425                       2265 
##                 DugguMarri         Duggunta Rajupalem 
##                       1288                       1830 
##                 DugguPuram              Dugrajapatnam 
##                        535                       1340 
##                 DUKULAPADU             Dulamvaripalli 
##                        906                        690 
##                     Dulzha                Dumbladinne 
##                       5758                        381 
##                 DUMBRIGUDA                  Dummanagi 
##                       3512                        243 
##                    Dummeda                 Dumpagdapa 
##                        369                       4089 
##                Dumpalgattu                   Dundigam 
##                        729                       1118 
##               Dundiralpadu                  Dunnavuru 
##                       1492                        347 
##                     Dupadu                    Duppada 
##                       2812                       2205 
##               DUPPALAPALEM                 Duppalpadu 
##                       1154                        338 
##                 Duppalpudi                 Duppalwada 
##                       2483                       1181 
##                  Duppituru               Durbalapuram 
##                       1338                        441 
##             DURGA SAMUDRAM                    Durgada 
##                       1691                       5553 
##                     DURGAM              DURGASAMUDRAM 
##                       1570                       1630 
##                      Durgi                  Durgiperi 
##                       5363                       1258 
##                 Durudkunta                   Durveshi 
##                       1465                       1606 
##                 DUSARIPAMU                       Dusi 
##                        889                        287 
##                       DUSI                   Duttalur 
##                       1536                       3813 
##                      Duvva                    Duvvada 
##                       5723                       3833 
##                    Duvvali              Duvvam(Arban) 
##                        413                        849 
##                    Duvvuru           DvarakaThirumala 
##                      13750                       2136 
##                  Dwarapudi                  DWARAPUDI 
##                       2266                       3261 
##      E RAMIREDDYGARI PALLE                 E. Gonehal 
##                        527                        254 
##              E. V. Nagaram                 E.E.Valasa 
##                       9621                        304 
##               E.Kothapalli                E.RAMAVARAM 
##                       5345                        330 
##                E.Vemavaram                   Eadumudi 
##                       2651                       1680 
##                     Eaduru              EashwaraPalli 
##                        954                        338 
##   EashwaraPalli Chowduwada              EashwaraPuram 
##                       1623                        649 
##                EashwaraVak                 East Gudur 
##                       1318                      23496 
##             East Kodipalle              EAST KUNDURRU 
##                       2519                       1245 
##                     Ebulam                   Echaneri 
##                       1341                       1355 
##                      Edara                    Edarada 
##                       4475                       2051 
##                 EdaraPalli                   Edavalli 
##                       3978                       3940 
##             Edavalli-Irvai                     Edavli 
##                        912                        860 
##           Edda AnantaPuram              Edda Annaluru 
##                        427                        196 
##          Edda Bommalapuram        Edda Chinna Pyapili 
##                       1162                       2202 
##           Edda Chintakunta               Edda Gonehal 
##                       4062                        520 
##                 Edda Hulti       Edda Jagannadhapuram 
##                       1265                        192 
##             Edda Kaukuntla            Edda Mallapuram 
##                       2478                       1172 
##             Edda Mantanala               Edda Musturu 
##                         74                        955 
##           Edda NagulaVaram               Edda Pappuru 
##                       1608                       3047 
##                 Edda Putha         Edda Shankarlapudi 
##                        768                       1693 
##             Edda Yachwaram             Edda Yakkaluru 
##                       1303                       1704 
##              EddaCherukuru                   EddaCoat 
##                       1759                        467 
##                 EddaDimili               EddaKandukur 
##                        673                       1729 
##                  EddaKotla             EddaMalliPuram 
##                       1924                        477 
##          EddaMurahariPuram                EddaNaPalli 
##                       1735                       3607 
##                  Eddanpudi                   EddaPadu 
##                       2374                       2431 
##                  EddaPalle                 EddaPettah 
##                       1984                        297 
##               EddaRaviPadu               Eddula Palli 
##                       1165                       1299 
##                Edduladoddi                  Eddupenta 
##                       1399                        795 
##                   Edepalli                    Edlanka 
##                        488                        474 
##                   EdlaPadu                  EdlaPalli 
##                       3628                       2655 
##              Edugundlapadu                 Edulagudem 
##                        951                        756 
##               EDULAMADDALI                EDULAVALASA 
##                        720                        149 
##              Edulwaripalli                   Edupalli 
##                        860                       1592 
##                 Edupugallu               Edurallapadu 
##                       4448                        382 
##                  Edurlanka                  Edurudona 
##                       1904                        821 
##                 Edurumondi                  Edurupadu 
##                       2905                        837 
##                    Edururu               EDUVARIPALLE 
##                       1155                        534 
##                    EetCoat                     Eggoli 
##                       3486                        291 
##      EGUVA BOPPARAJU PALEM          EGUVA KANIKAPURAM 
##                        466                        577 
##        Eguva Tamballapalli             Eguvagottividu 
##                       1252                       1327 
##             EGUVAMODAPUTTU                 Eguvapalli 
##                        413                       1380 
##                 EGUVAVEEDI    Eguvgangampalli-G.Palli 
##                        921                       1989 
##                  Eguvpalli                    EidGali 
##                        575                       1795 
##        Ejansi LakshmiPuram                Ekunampuram 
##                       4269                        291 
##                    Ekuvuru                 ELAKAKUNTA 
##                        559                       1513 
##                  ELAKATURU              Elamanchipadu 
##                       1747                        708 
##                 ELAMANDYAM                   Elamarru 
##                       1852                       2049 
##                   Elaprolu                     ELCHUR 
##                       1504                       3661 
##                 Eleshvaram   Eletipadu And G.Kandrika 
##                      17181                       1024 
##                 Eletipalem   ELLA MANYAM KANDRIGA ANE 
##                       1919                        234 
##               Ellamanchili           Ellamanchili P.T 
##                       2542                      14508 
##                  EllaPuram                    Ellarti 
##                        243                       1279 
##                  ELLATHURU                Ellavathula 
##                        934                       1296 
##                    Elluppi                    Ellutla 
##                        950                       2122 
##                    ELLUTLA                      Elnji 
##                       1139                        975 
##                  Elukuntla                      Eluru 
##                        837                     128062 
##                  EluruPadu                      Emani 
##                       6126                       5410 
##                      Embai              EmmadiCheruvu 
##                        844                        638 
##                Emmajigudem                     EMPEDU 
##                        612                        407 
##                      Emula                 EmulaBanda 
##                       1631                        885 
##                 EmulaChedu                  EmulaCoat 
##                        860                       1336 
##                 EmulaDeevi                  EmulaPadu 
##                       7544                        353 
##                   EmulaWad              Enamala manda 
##                       1199                        749 
##       EnamalaKuduru Arbana                   Enamdala 
##                      19417                       7161 
##                  Endabadra                 Endakuduru 
##                      26336                        527 
##                  Endapalli                    Endluru 
##                       3494                       1529 
##                    Endrayi                   Enduvpet 
##                       1082                        164 
##                Engalibanda                  Enikepadu 
##                        317                       6910 
##                   Enikpadu             Enugunda palem 
##                       1047                       1377 
##             Enugunta palli                 Enumlpalle 
##                        656                       2501 
##               Enumuladoddi                   Epigunta 
##                       4579                        935 
##                      Epuru                   Epuru-11 
##                       7471                       1799 
##                   Epuru-1E                  Eradikera 
##                       2743                       1547 
##              Erakrayapuram                    Erigeri 
##                        308                       2147 
##                ERIKAMBATTU   ERIKAMBATTU HARIJANAWADA 
##                        379                        879 
##         Erra cheruvu palli                   Errabadu 
##                        998                        779 
##                  Errabalem                  Erraballi 
##                        463                       5084 
##            Errabommanpalli                  Erradoddi 
##                       1179                       2389 
##             ErragondaPalem                   Erragudi 
##                       6598                       1791 
##              Erragudidinne               Erragudipadu 
##                        980                        534 
##               ERRAGUDIPADU                 Erraguduru 
##                        373                       1581 
##                  Erragunta            Erraguntalpalli 
##                        922                        938 
##                 Erraguntla                  Errakatva 
##                       6631                        472 
##              ERRAKOTAPALLI                   Erramadu 
##                        195                        695 
##           ERRAMAREDDIPALEM          ErramAreddy Palli 
##                        913                         99 
##             Erramnenipalem             Erramrajupalli 
##                        523                        625 
##              Errasanipalli                Errobnpalli 
##                        560                        682 
##             ErukalaCheruvu                   Erukollu 
##                       1813                        421 
##                      Eruru                 ERUVUPALEM 
##                        718                        360 
##                 Es.R.Puram                 Etamukkala 
##                       1715                       4741 
##                  ETAVAKILI                   Etcharla 
##                       1160                       1378 
##                     Etheru              Ethirajupalle 
##                       1919                        727 
##                     ETHURU             Etigairemapata 
##                        828                       1255 
##                 Etikoppaka               Etimar Puram 
##                       3333                       3863 
##                    Etimoga                     ETTERI 
##                       2222                       1068 
##                    Etukuru                      Eturu 
##                       5266                       3388 
##           Fajul Bag Pettah                Fakirutakya 
##                       1391                       1134 
##            Fakruddienpalem                Faksudorpet 
##                       1338                        209 
##                FAREED PETA                 Fathelanka 
##                       2156                        376 
##               Firangipuram              G Appayapalli 
##                       9538                        212 
##                G Di Valasa                  G V PURAM 
##                        511                        850 
##           G. Jambula Dinne                   G. Kodur 
##                       1634                       3459 
##                 G. Kumramu                G. Madugula 
##                        419                       4132 
##              G. Singavaram              G. Veerapuram 
##                       2244                       1000 
##             G. Yarrampalem                G.Agraharam 
##                       1356                       1261 
##                 G.BHAVARAM                  G.C.Palle 
##                        638                       2033 
##                  G.C.Palli                G.Dontamuru 
##                        946                       2120 
##                  G.G.Palem                  G.Hosalli 
##                        800                        756 
##          G.Jagannadhapuram          G.JAGANNADHAPURAM 
##                        418                        967 
##              G.KOTHA PALLI               G.Kothapalli 
##                       1253                       2318 
##                 G.L.S FARM                 G.Mamidada 
##                       1093                       6961 
##                  G.MedPadu                 G.MEKAPADU 
##                       4153                        175 
##                  G.Mudidam             G.Mukundapuram 
##                       1079                        255 
##         G.P.Rangarayapuram                G.Ragampeta 
##                        341                       1187 
##                  G.S.Puram                   G.Sigdam 
##                        630                       1419 
##                G.Vemavaram                G.VEMAVARAM 
##                       3286                        584 
##                    Gabbada                     Gadala 
##                       1206                       2339 
##                  Gadbvlasa                 GaddaGunta 
##                        218                       1362 
##             GADDAMAYAPALLE    GADDAMEEDA HARIJANAWADA 
##                        242                        372 
##            GADDAMGARIPALLI            GADDAMVARIPALLI 
##                       2554                        562 
##                GADDIVALASA                 Gaddmanugu 
##                        399                        795 
##                Gade Hoturu                 Gadeguduru 
##                       1939                       1074 
##                    Gadekal                     Gadela 
##                       3405                        813 
##                Gadelapalem                Gadelavlasa 
##                       1726                       1124 
##                   Gadepudi              Gadewarigudem 
##                        234                        577 
##                   Gadgamma                   GADHIRAI 
##                        259                        529 
##                       GADI                   GadiCoat 
##                        700                       2759 
##                   Gadidpay                  GadiEmula 
##                        122                       4598 
##                Gadigrevula                   Gadiguji 
##                       1277                         65 
##            GADIKINCHUMANDA                   Gadikram 
##                       1048                         76 
##                  Gadilanka                 Gadiyapudi 
##                       1059                        338 
##                    Gadrada                     Gadsam 
##                       2775                        804 
##                GADUGUPALLI                     Gaduru 
##                       1023                        459 
##                   Gaduturu               gairammapeta 
##                       3014                        496 
##                    Gajanki                  Gajanpudi 
##                        329                       2119 
##           GAJAPATHIANGARAM           GajapathiNagaram 
##                        562                       2781 
##            Gajarayunivlasa                     Gajili 
##                       1399                        195 
##               Gajjalakonda                   GAJJARAM 
##                       1970                        837 
##                 GAJJEHALLI               Gajram Palli 
##                       1192                        632 
##                Gajuladinne              GAJULAPELLURU 
##                       1124                        922 
##                 Gajullanka               GAJULMANDYAM 
##                       2114                       3161 
##                 GajulPalli                  Gajulrega 
##                       5585                       9074 
##              GAJUVARIPALLI                   Gajuwaka 
##                        670                      69673 
##                  Gala Gala                  GALAVALLI 
##                       2857                       2315 
##                Galayagudem            GALIBHEEMAVARAM 
##                       1501                        535 
##        GaliChennaiah Palem              Galigerugulla 
##                        692                       1692 
##                   Galividu           gallavandlapalli 
##                       8750                        305 
##                 Gamalapadu                 GAMBHEERAM 
##                       2112                       3454 
##                 GamjiKunta               Gammadivipet 
##                       2291                        555 
##               Gampalagudem                   GAMPARAI 
##                       8347                       2279 
##             GAMPAVANIPALEM             GanapathiPalli 
##                        982                        607 
##                Ganapavaram                GANAPAVARAM 
##                      26995                       1440 
##                  Ganapuram          GANDA BOYANAPALLI 
##                        158                       1394 
##                 Gandavaram                 Gandepalle 
##                       2267                       1365 
##                 Gandepalli                GANDHAVARAM 
##                       2854                       1631 
##                Gandhawaram                GANDHI ROAD 
##                        714                       1338 
##                 GANDHIGRAM              Gandhinagaram 
##                        703                        732 
##              Gandiganumala                GANDIGUNDAM 
##                       2181                        324 
##                  Gandikota               Gandikovvuru 
##                        665                        796 
##                 Gandipalem             Gandivanipalem 
##                        936                        514 
##               Gandla Palle                 GandlaPadu 
##                       2476                        550 
##               Gandlaparthi                Gandlapenta 
##                       1608                       5208 
##          Gandlavandlapalli                 Gandlavidu 
##                        238                        742 
##                    Gandrai             GANDRAJU PALLI 
##                       3473                        768 
##                    Gandram                   Gandredu 
##                        407                       1568 
##                Gandu palli                 GANDUPALLE 
##                        507                        439 
##                 Gane kallu            GaneshwaraPuram 
##                       1470                        440 
##             Gang Donakonda        Gangabhageerdipuram 
##                        512                        151 
##           Gangachollapenta                    GANGADA 
##                        748                       1932 
##            Gangadevi Palli             GangadeviPalli 
##                       1186                        499 
##         GANGADHARA NELLORE            Gangadharapuram 
##                       3704                        660 
##               Gangadipalem                Gangalkurru 
##                       2767                       4615 
##            GANGAMAMBAPURAM                Gangamapata 
##                       1134                        324 
##               Ganganapalli                Ganganaplli 
##                       5586                      12071 
##          GangannaDoraPalem               GangannaPadu 
##                        198                       1187 
##                Ganganpalli                GanganPalli 
##                        676                       1491 
##                Gangaperuru                 GANGAPURAM 
##                       1507                       1016 
##             Gangareguvlasa                 Gangavalli 
##                       1276                        296 
##                 Gangavaram                 GANGAVARAM 
##                      11452                       6166 
##               Gangayapalli          GANGI REDDY PALLI 
##                        184                       1005 
##          GANGINAYANI PALLI             GangiNeniPalem 
##                        637                        822 
##               Ganginepalli            GANGIREDDIPALLI 
##                       1426                       1095 
##           Gangireddy Palli            GangireddyPalli 
##                        294                        511 
##                GangiValasa                    Gangolu 
##                        770                       6738 
##                  GangPalem                 GangPatnam 
##                        664                       3046 
##                    Gangram                  Gangubudi 
##                        610                       1034 
##               GangulaKunta      GANGULANARAYANA PALLI 
##                        571                        218 
##                GangulaPadu                    Ganguru 
##                        554                       4572 
##                   GanguWad                       Gani 
##                       1517                       1953 
##                 Ganiatkuru                   Ganigera 
##                       2066                       2938 
##                  Ganijerla                  Ganikpadu 
##                        610                        770 
##          Ganishettipale Mu               Ganivanipadu 
##                        851                        306 
##                   Ganiwada              Ganjayi Badra 
##                        763                        806 
##                 Ganjihalli                 Gannavaram 
##                       2261                       5278 
##          Gannavaram Arbana                    GANNELA 
##                      12946                       1313 
##                 Gannepalle               GANNERUPUTTU 
##                       4108                        601 
##                   Ganparti               Ganpeshwaram 
##                       1386                       1898 
##             Ganpwarigudena             Gantavanipalem 
##                        272                        789 
##                Ganthimarri                      GANTI 
##                        956                       2883 
##             Ganti Pedapudi                Gantikorlam 
##                       2508                        556 
##                    Gantlam                   Gantyada 
##                        910                       1078 
##                Ganugapenta                  Ganugpadu 
##                       3331                       2386 
##                       Gara               Garalamadugu 
##                       2112                        483 
##                  Garapenta                    Garbham 
##                        274                       4087 
##              Gargeya Puram                  Gargparru 
##                       5530                       2116 
##             GARIDAGRAHARAM          Garigicheenepalli 
##                        924                        712 
##          GARIGUNTVARIPALLI                Garika Peta 
##                        572                        942 
##                 Garikapadu                Garikaparru 
##                       5157                       1961 
##                 Garikipadu                Garikivlasa 
##                        330                        748 
##                  Garikpadu        Garimellakothavlasa 
##                        418                        282 
##              Garimenapenta               Garimnapenta 
##                       1898                        367 
##             Garishelapalli                 Garishpudi 
##                        974                        891 
##                  GARISINGI                Garladinane 
##                        982                       5770 
##                 Garladinne                 GarlaDinne 
##                        520                       1499 
##                  GarlaPadu                  GarlaPeta 
##                       1403                        577 
##                GarNaidupet                  Garnepudi 
##                        127                       1939 
##                   Garnikam                 Garnimitta 
##                        984                       1735 
##                    Garpadu                GarudaBilly 
##                       3012                       1770 
##                GarudaChedu                Garudapuram 
##                        982                       3563 
##                 Garudbadra                 Garudkandi 
##                        537                        345 
##       Garugu Chintal Palli                Garugubelli 
##                       1090                        579 
##                Garugubilli                GARUGUBILLI 
##                       2615                        932 
##                Garugupalli                     Gata D 
##                        689                        284 
##                GATALAVALSA                  Gatlvlasa 
##                        541                        964 
##              GATRALLAMITTA             GATTARAGILLEDA 
##                        634                        941 
##                GATTARAGUDA                      GATTU 
##                        450                       3118 
##                     GATTUM                 Gattupalli 
##                        673                       2686 
##   GauraPuram h/o Allapalli           GavaraMma Pettah 
##                       1857                        710 
##                GAVARAPALEM                Gavaravaram 
##                        804                       2983 
##                GAVARAVARAM         GAVARLA ANAKAPALLI 
##                       5454                        441 
##                  Gavigattu            Gaviniwaripalem 
##                       1346                       6090 
##                GawCanPalli            GawNivaRi Palli 
##                       2258                       3983 
##    GawNivaRiPalli-Gorantla                 GEDALAPADU 
##                      14569                        717 
##                    Geddada              Geddakanchram 
##                       1030                       1034 
##                Geddanpalli                 Geddapalli 
##                       4185                        311 
##                  GEDDAPETA                  Geddluppi 
##                        971                       1088 
##                Geddpuvlasa               Geddtiruwada 
##                       1034                        870 
##                   Geddvuru                  Gedelapet 
##                        664                        267 
##            GEDELAVANIPALEM             GEDELAVANIPETA 
##                       1153                        758 
##                GeetNaPalli           GELASAMVARIPALLI 
##                        371                        624 
##                    Gemmili              Gerimenapenta 
##                       1197                        574 
##                   Ghansara                 Ghantasala 
##                        662                       3885 
##                   Giddalur  GIDDAMAKARAJAPURAM MAJARA 
##                      24472                        984 
##                 Giddapalle                   GIDIJALA 
##                        328                        890 
##                     Gidjam               Gidlavalleru 
##                       1573                       5579 
##                    Gijabha                   Gilkpadu 
##                        960                       1601 
##                 GILLIPALLI                    Ginjeru 
##                       1687                        321 
##                 Ginjupalli                GINNELAKOTA 
##                        348                       1431 
##                 GiriGentla                 girisaluru 
##                        726                        218 
##              Girivanipalem                  Gittanagi 
##                        294                        134 
##                 Gittupalli          GNANAMAMABA PURAM 
##                        311                        467 
##            GOBBILLA KOTURU           Gobburivaripalli 
##                       1073                        394 
##                    Gobburu                     Gobyam 
##                       1407                        484 
##                   GOCHAKKA                    Godalam 
##                        660                        452 
##                  Godavarru                      Godda 
##                       2900                        294 
##                 Goddumarri              Godduvelugala 
##                       1869                       1114 
##                       Godi                    Godiada 
##                       2567                        411 
##                 Godicherla                 Godignooru 
##                       1684                       1474 
##                  GODIKOMMU                  Godilanka 
##                        632                       1306 
##                 Godiyapadu                  Godlavidu 
##                        143                       1850 
##              Goduguchintha            GODUGUMANIPALLE 
##                       1420                        785 
##                 Godugunuru               Godwaripuram 
##                        496                        257 
##                   Godwarru               GOGANNAMATAM 
##                       2402                       3388 
##                GogulaDinne                 GogulaPadu 
##                        240                       2543 
##                GogulaPalle                    Gogunta 
##                       2824                        363 
##               Gokaiahvlasa                Gokanakonda 
##                        170                        916 
##              GokarajuPalle               GOKARNAPALLI 
##                        416                       1073 
##               Gokarnapuram                  Gokavaram 
##                        482                       8591 
##                   Gokiwada                Gokuladinna 
##                       2544                        339 
##                 GOKULAPADU                    Golagam 
##                        975                       1073 
##                  Golavlasa                       Goli 
##                        843                       2712 
##                Goliyaputti                     Goljam 
##                        461                       1777 
##                      Golla       GOLLA CHEEMANA PALLI 
##                       1690                       1227 
##                GOLLA PALLI                    Golladi 
##                        568                       1727 
##                 Gollagandi              GollaKandukur 
##                       1463                       1217 
##              GOLLALAGUDURU               GOLLALAPALEM 
##                        833                       2591 
##                Gollalgunta               Gollalkoderu 
##                        327                       1981 
##               Gollalmulgam                 Gollalpadu 
##                       1050                        306 
##                GOLLAMADUGU               Gollamandala 
##                        344                       1056 
##                  Gollamudi               Gollanapalli 
##                        866                       1382 
##         GOLLANARAYANAPURAM                  Gollapadu 
##                       2831                       1594 
##                 Gollapalem                 GollaPalle 
##                       3546                       1637 
##                 GOLLAPALLE                 Gollapalli 
##                       2998                       6014 
##                 GOLLAPALLI    GOLLAPALLI, DARJI PALLI 
##                        449                       2441 
##                  GollaPeta                 Gollaprolu 
##                       1833                      16895 
##                  Gollapudi                Gollavidipi 
##                      21448                        877 
##                 GollaVilli                 Gollavlasa 
##                       2267                       1030 
##                  Gollavuru                 GOLLUPALEM 
##                        520                        290 
##  Gollupalem Echa/O Devupal               Golugondapet 
##                        526                        601 
##                  Golugunda                Goluguvlasa 
##                       2782                        581 
##                    GOMANGI                      Gompa 
##                       1439                       1428 
##                  Gonabhavi                  Gonaspudi 
##                        814                       1682 
##                  gonavaram    Gonbavi, h/o Gumma Gatt 
##                       1148                       3893 
##                    GONDELI                      GONDI 
##                        844                        847 
##           Gondi Kothapalli                 GONDIPALLE 
##                       1583                       1241 
##                 Gondiparla            Gondireddipalli 
##                       2594                       1866 
##                  GONDIVADA                 GONDUPALEM 
##                         81                       1879 
##                     Goneda                 Gonegandla 
##                       1697                       8453 
##                   Gonepadu                   GonePadu 
##                        714                        527 
##             Gongada Valasa               Gonindapuram 
##                        750                        778 
##                    Gonipet                      Gonti 
##                        965                        544 
##             GONTUVANIPALEM             Gontuvaripalli 
##                       2043                        229 
##                  Gonugunta                   Gonuguru 
##                       3456                        791 
##           GONUMAKULA PALLI            Gonumakulapalli 
##                       1306                        891 
##                  Gonupalli              GoodepuValasa 
##                       1268                       2701 
##                Gooling pet                      Gooty 
##                        463                      23659 
##             Gopaladoravuru               Gopalapatnam 
##                        209                      20444 
##               GOPALAPATNAM                Gopalapuram 
##                      49380                      13044 
##                GOPALAPURAM          Gopalarayudu peta 
##                       9671                        766 
##           Gopalareddipalem                 GopalPalli 
##                       1140                       1566 
##                 GopalPenta                 gopalpuram 
##                        711                        673 
##          GopalVenkatapuram               Gopannapalem 
##                        236                        623 
##                 GopanPalli                  Gopapuram 
##                       1409                        681 
##                  Gopavaram             GOPAVARAMPALLI 
##                      20452                        520 
##            Gopavarapygudem                Gopayapalli 
##                       2034                       1247 
##                 Gopemapata                  Gopepalli 
##                        173                        977 
##               GopGudiPalli                  GopiDinne 
##                       2553                       1687 
##             GOPINADAPATNAM              Gopinenipalem 
##                        707                       1313 
##             GOPISETTYPALLE           GOPIVALLABAPURAM 
##                        690                        310 
##              Gopmambapuram                    Goppali 
##                        453                       1594 
##              Gopuranipalem              Gopuvanipalem 
##                        373                        518 
##                 Goragnmudi                   Gorantla 
##                        823                      19619 
##                  GORAPALLI                   Gorapudi 
##                       1376                        895 
##                    GORAPUR                   Gorentla 
##                        773                       2945 
##                 Goridindla                 Goriginuru 
##                        713                       1022 
##                 Gorijavolu                  Gorikpudi 
##                        794                        917 
##              gorillavalasa                    Gorinta 
##                        453                       1665 
##                    GORINTA                  Gorintada 
##                       3185                       1544 
##          Gorivimakulapalle                 Gorlagutta 
##                        514                       1240 
##              Gorlamudividu            GORLAVANI PALEM 
##                       2401                       1375 
##         Gorle Sitarampuram                   Gorlepet 
##                        793                        402 
##                GORRELAPADU                  GORREPADU 
##                        235                       2397 
##                 Gorribanda                  Gorripudi 
##                        562                       4172 
##                      Gorsa             Goruguntalpadu 
##                        899                        250 
##                  Gorukallu              Gorumanukonda 
##                       2189                        680 
##             GORVIMANIPALLE                      Gosal 
##                       1563                       3812 
##                      Gosam                Gosanupalle 
##                        256                       1049 
##                  Gosaveedu                    Goshada 
##                       1488                        388 
##                  Gosukonda                 Gosulneedu 
##                        454                        515 
##                     Goteru                   Gotivada 
##                        973                        693 
##                   GOTIVADA                   Gotiwada 
##                       1249                       1039 
##                 Gotlagattu                     Gotlam 
##                       1556                       1321 
##                     GOTLAM                    Gotluru 
##                        635                       5242 
##                   Gotnandi                      Gotta 
##                        555                        860 
##               GottiGundala                  Gottikadu 
##                       1461                        677 
##               Gottimukkala                  GottiPadu 
##                        940                       3357 
##                 Gottipalla                 GottiPalli 
##                       3522                        945 
##                 GOTTIPALLI                 Gottipdiya 
##                       3406                        556 
##                 Gottiprole                  Gottipudi 
##                       1155                        160 
##        GOTTIVADA AGRAHARAM                 GottiValli 
##                        264                        772 
##                 Gottivlasa                   GottiWad 
##                       1014                        402 
##               Gottumukkala                   Gotukuru 
##                        596                        885 
##               Gotula Doddi                      GOTUR 
##                        800                        653 
##                     Goturu                  Goudgallu 
##                       1032                        305 
##                 Goudnhalli              GOUDU GURANTI 
##                       1893                        630 
##                GOUNUCHINTA                     Govada 
##                       1382                       3904 
##            GOVARDHANA GIRI              GOVINDA PURAM 
##                        910                        473 
##        Govinda reddi palli              GovindamPalli 
##                        456                       1004 
##               Govindapalem               Govindapalle 
##                       3764                       5142 
##               GovindaPalle  GOVINDAPPA NAIDU KANDRIGA 
##                       2196                       1573 
##               Govindapuram               GovindaPuram 
##                       8665                       1903 
##           Govindarao Palli           GOVINDARAO PALLI 
##                        463                        430 
##                 GovindaWad                 Govindinne 
##                       2557                        469 
##               Gowardangiri         GOWDA MAKULA PALLI 
##                       1486                        834 
##          GOWNITHIMME PALLI                 Gowravaram 
##                       1333                       5346 
##              Gowridevipeta                Gowripatnam 
##                        869                       5771 
##                 GOWRIPURAM                 Gowrmapata 
##                        143                        596 
##                     GOYIDI                   Goyipaka 
##                        277                        601 
##               Gozhzhapuram  GPETA@VEERARGHUNADHAPURAM 
##                       1814                        379 
##                Graddagunta          Grahpati Agrahram 
##                        864                        241 
##                  Gramdatla                 GREAMS PET 
##                       3026                      13045 
##                 Griddaluru                       GUDA 
##                       2264                       1276 
##                     Gudala           GUDALAAVARIPALEM 
##                       2136                        686 
##                   Gudapadu             GUDAREVU PALLE 
##                        463                        579 
##                  Gudavalli                Guddigudena 
##                       3538                       1444 
##             Guddikayalanka                    Guddipa 
##                        624                        740 
##     Guddipa Shiwaru Kothur                 Guddipadra 
##                        358                        471 
##                      Gudem              Gudem Cheruvu 
##                       3618                       1966 
##         Gudem Golugulvlasa                Gudem Kolni 
##                        143                       1380 
##           Gudem Kotha Vidi                  GudiBanda 
##                        528                       4896 
##                  GUDIBANDA              Gudigallabaga 
##                        308                        539 
##                  Gudigunta                  Gudikallu 
##                       1084                       5600 
##               Gudikambaali                Gudikothuru 
##                        913                       1130 
##                 Gudimallam               Gudimellanka 
##                        525                       4349 
##              Gudimellapadu                  Gudimetla 
##                        454                       1502 
##                  GudiMetta                Gudimiralla 
##                       1464                        815 
##                   Gudimula                  GudiNarVa 
##                       1231                        420 
##                   Gudipadu                   GUDIPALA 
##                      15481                        998 
##                  Gudipalli                  GudiPalli 
##                       2317                        561 
##              GudiPallipadu                   Gudipudi 
##                       8690                       3428 
##                   Gudivada                   GUDIVADA 
##                      16020                        571 
##             Gudivada Urban               Gudivaklanka 
##                      56431                       1602 
##                  GUDLADONA           Gudlanayinapalle 
##                        957                        484 
##                 GudlaPalli                      Gudli 
##                        263                       1916 
##                     Gudlur                    Gudnagi 
##                       2056                        320 
##                   Gudpalli           GUDUMBAAYI TANDA 
##                       4266                        454 
##                  GUDUPALLE                     Guduru 
##                       1651                      21176 
##                     GUDURU                 Gudvalluru 
##                        661                       1377 
##                    Guggili                    GUGGUDU 
##                        263                        894 
##                     Gugudu               Gujangivlasa 
##                       4535                        974 
##            GujarathiPettah                       Guji 
##                       3274                        148 
##           Gujjalavaripalli          GUJJUMAMIDIVALASA 
##                        473                        482 
##              Gulam Nabipet               GULAMALIABAD 
##                        203                        571 
##                Gulimikotla                Gulincherla 
##                        867                        939 
##                Gulivindada                 Gulladurti 
##                        881                       2468 
##               Gullalapalem                  GULLAPADU 
##                      13220                        158 
##                 Gullapalem                  Gullapudi 
##                       6985                       2280 
##                  GULLAPUDI                   GULLELLU 
##                        163                       2138 
##                 GULLEPALLI  Gullepalli H/o Ekarlapall 
##                       2301                        225 
##                  Gullipadu                  Gulpalyam 
##                        335                       1776 
##                   Gulumuru                     GULYAM 
##                        942                       3449 
##                     Gumada                    Gumapam 
##                       1464                       1539 
##                     Gumdam                      Gumma 
##                        750                        955 
##                Gummadiduru                 Gummakonda 
##                       1102                       1028 
##                  GUMMAKOTA               Gummalampadu 
##                        914                       1380 
##                Gummalapadu            GummalaxmiPuram 
##                        920                      15081 
##              Gummalladoddi                  Gummaluru 
##                       1993                       3362 
##                 Gummampadu               Gummanampadu 
##                        932                       1456 
##                   GUMMANUR                  GummaPadu 
##                        652                        360 
##                Gummaregula              GUMMASAMUDRAM 
##                        759                       1432 
##              Gummatantanda               Gummidigonda 
##                        213                       1508 
##                Gummidiguda                  Gummileru 
##                        348                       1480 
##                  Gummuluru                  GUMMULURU 
##                       1801                        130 
##               Gumparlapadu            Gumparman Dinne 
##                       1492                       1882 
##                   GUMPARRU                  GUNABADRA 
##                       1707                        852 
##              Gunakanapalle                GunaNuPuram 
##                        821                       1144 
##                   Gunapadu            Gundaboyinpalem 
##                       1794                        933 
##                     gundal                    Gundala 
##                       1145                       1087 
##            Gundalammapalem                GundalaPadu 
##                        837                       1613 
##                GundalaPeta          GUNDAM RAJU PALLI 
##                       1427                        996 
##                 GundamPadu                  Gundavolu 
##                       1126                       1347 
##               Gundayapalem              Gundeli Gunta 
##                        681                        417 
##               Gundemadkala                 Gundepalli 
##                        829                       3010 
##             Gundiganipalli                  Gundimeda 
##                       1011                       2812 
##            Gundisettipalli               Gundla palli 
##                        667                       1654 
##              GundlaCheruvu          Gundlakattamanchi 
##                       1881                       2422 
##                Gundlakonda                Gundlakunta 
##                        936                       1099 
##               Gundlamadugu               GUNDLAMADUGU 
##                       1254                        811 
##                GundlaMoola                 GundlaPadu 
##                        452                       2149 
##                Gundlapalem                GundlaPalem 
##                       1317                        472 
##                Gundlapally              Gundlasagaram 
##                       9024                        543 
##             GundlaSamudram           Gundlasingavaram 
##                        938                       1154 
##                   Gundluru                   GUNDLURU 
##                       1451                        879 
##             GUNDRAJUKUPPAM                  GUNDRATHY 
##                       4782                        415 
##                 Gundrevula                 GUNDUGALLU 
##                       3092                       1047 
##           GUNDUGOLANUGUNTA                 Gundugolnu 
##                        677                       4977 
##                Gundugudena                  Gundupala 
##                        859                       2386 
##                 Gundupalem                 GunduPalli 
##                        646                        917 
##                Gundupapala                GunduValasa 
##                       1409                        349 
##      Gunduwarilakshmipuram             Gune Morubagal 
##                        485                       1331 
##                 Gunikuntla                  Gunipalli 
##                       1316                       1180 
##                  gunjalova                 Gunjalpadu 
##                        215                        404 
##              Gunjarlapalli                 Gunjepalli 
##                        577                       7695 
##                  GUNJIVADA                   Gunkalam 
##                        967                       2630 
##                   Gunlpadu                Gunnampalli 
##                        187                       3094 
##              Gunnangidibba           GunnaThotaValasa 
##                        367                       1063 
##                 Gunnempudi                   Gunparru 
##                       1700                        423 
##          GuntaChennampalle               GUNTAGANNELA 
##                        174                       1164 
##                   Guntakal    Guntakallu Munisipaliti 
##                      11253                      74945 
##            GUNTAKINDAPALLE               Guntaknadala 
##                        874                       2053 
##                Guntakoduru                 Guntapalli 
##                        362                       3306 
##                 GUNTASEEMA                GUNTI PALLE 
##                       1129                        749 
##                 GUNTI PEDU                 Guntimdugu 
##                        357                        468 
##                 Guntupalli                 GUNTUPALLI 
##                       7123                       2274 
##                     Guntur                   Gunupudi 
##                     355239                       3401 
##                   Gunupuru                GUPPIDIPETA 
##                       1667                       1486 
##                     Guraja                   Gurajala 
##                       2384                      11704 
##              Gurajanapalli              Gurandarpalem 
##                       4679                        929 
##                    Gurandi               GURAVAIGUDEM 
##                       1945                        400 
##            Guriginjakuntla                   Gurijala 
##                        872                       1260 
##                Gurijepalli             Gurivindagunta 
##                       1650                        362 
##              Gurivindapudi                    Gurjada 
##                        617                       1021 
##                 Gurjapalem                      Gurla 
##                       1508                       2919 
##                      GURLA          Gurlatammarajupet 
##                        808                       1153 
##               GurrajuPalem              Gurrala Lanka 
##                        483                        486 
##     Gurralalachintalapalli              GURRALAMADUGU 
##                        812                        544 
##               GurralaPalem                Gurrambailu 
##                        648                        999 
##                Gurramkonda                GURRAMKONDA 
##                       2897                       5964 
##              Gurrammavlasa                 Gurrampadu 
##                        494                        868 
##                Gurrampalem                GURRAMPALEM 
##                       2021                        947 
##                Gurrapadiya                Gurrapusala 
##                        572                       1155 
##                   GURTHEDU              Gurudasupuram 
##                       2287                        752 
##          Gurugu Bhimavaram                GURUGUMILLI 
##                       1183                        193 
##             Gurukulapallem            Gurukuvaripalle 
##                        154                       1710 
##                  GURUPALLI                    Guruvam 
##                        542                       1124 
##             Guruvayigudena             Guruvindagunta 
##                       1850                        346 
##             Guruvindapalle           Guruvinnayudupet 
##                        680                       1467 
##                 Gurvajipet            Gurwareddipalem 
##                        762                        944 
##                    Gushini                     GUTALA 
##                       1847                       1323 
##                   Gutchimi                 Guthavilli 
##                       1809                       1458 
##          Guthi AnantaPuram             Guthi Erragudi 
##                       1733                       1842 
##                 Guthindivi                  Gutibailu 
##                      11038                        876 
##                 Gutlapalli                  Guttapadu 
##                       2403                        954 
##                 Guttapalli                 GUTTAPALLI 
##                        979                        534 
##                GUTTAPALLIM                 Guttikonda 
##                       2228                       4816 
##               GuttulaPuttu                    Gutturu 
##                        770                       2458 
##                  Gutupalle                    Guvvadi 
##                       1335                       1652 
##               Guvvalkuntla               GUYANAMPALLE 
##                       1887                        310 
##               GUYYANAVALSA                H R Kottala 
##                        380                       1037 
##              H. Nidamannur             H. Shiddapuram 
##                       3079                       1137 
##                H.Kairawadi            H.KARADA VALASA 
##                       2995                        525 
##                  H.Murvani                 Haddubnagi 
##                       4373                        539 
##                 HajeePuram                  Halaharvi 
##                        930                       3580 
##                   Halharvi                   Haligera 
##                       1545                        995 
##                   Halukuru                      Halvi 
##                       4498                       2103 
##                      Hampa                 Hampapuram 
##                       1122                       1555 
##                      HAMSA                 Hamsaraali 
##                        535                        664 
##                 Hamsawaram                Hanakanahal 
##                       4430                       2081 
##                    HANAWAL                   Hanawalu 
##                        836                       1875 
##               Hanchana Hal             Hanumant gudem 
##                       1501                        474 
##            Hanumanthapuram          HanumanthuniGudem 
##                       1314                        727 
##           HanumanthuniPadu               HANUME PALLI 
##                        354                        789 
##                Hanumnguthi                  Hardageri 
##                       1664                        748 
##              Hare Samudram               HareSamudram 
##                        764                       5017 
##           Harichandrapuram              HariDasuPuram 
##                        750                        517 
##                  HariPalem                  Haripuram 
##                       1864                       4118 
##          HarischandraPuram                  Harivaram 
##                        684                        990 
##                  Harshbada                  Hasanbada 
##                        432                       1008 
##                   Hasnabad                 Hasnapuram 
##                       1564                       4019 
##                Hastakaveri                 Hastawaram 
##                        334                       1315 
##               Hathibelagal       Haveli Muthyalampadu 
##                       1388                        481 
##                    Havligi             HAYATHINAGARAM 
##                       3667                       3145 
##              Hazarat Gudem                   HEBBATAM 
##                        509                       1848 
##            Hecha.Sodnpalli                  Hemavathi 
##                       1721                       5296 
##                 Himakuntla    Hindupuram Munisipaliti 
##                        409                     101917 
##                Hir Dey Hal                Hirmandalam 
##                        463                       4071 
##                   Hjipuram                   Holgunda 
##                        514                       4511 
##                    Honjram                    Honnali 
##                        624                        795 
##                   Honnooru               HossainPuram 
##                        193                        960 
##                     Hosuru             HOTRAMANUDINNE 
##                       4725                        189 
##                Hous Ganesh                  Hukumpeta 
##                        601                      10067 
##                  HUKUMPETA                   Hulebidu 
##                       2348                       1313 
##                  Hulikallu                  Hulikanvi 
##                       1947                        357 
##                   Hulikera      Hullikera Devar Halli 
##                       2206                       2570 
##               Husena Puram              HussainaPuram 
##                       3631                       1698 
##              HUSSAINAPURAM             Hussen Nagaram 
##                       1131                       1013 
##               Hussen Puram                  Huvannuru 
##                       1351                        293 
##            I S RAGAVAPURAM                 I. Pangidi 
##                       1856                       2462 
##               i. polavaram               i.bhimavaram 
##                       4077                       2409 
##                I.POLAVARAM       I.S. JAGANNADHAPURAM 
##                       1133                       2093 
##               I.TandraPadu                Ibrahim Bad 
##                       3616                        297 
##              Ibrahimpatnam                Ibrahimpeta 
##                      17442                        470 
##               Ibrahimpuram                  ICHAPURAM 
##                       2057                      20570 
##                  IDAMADAKA                 Iddanvlasa 
##                       1537                        723 
##                 Idimepalli                   Idmkallu 
##                       1371                       1103 
##                      Idtam           Idula Devarbanda 
##                       3100                        153 
##                Idulmusturu           Idulpaka Bonangi 
##                       2676                        865 
##                  Idulvlasa                Idupulapadu 
##                       1336                       3648 
##                Idupulapaya                   Idupuram 
##                       1108                       3015 
##                    Idupuru                  Idurpalli 
##                       2160                        298 
##                    Iduru-1                    Iglpadu 
##                       1757                        806 
##                    Iguduru                   Ijuwaram 
##                        764                        360 
##                    Ikkurru                 Ilaganooru 
##                       2485                        613 
##                 Ilapakurru                   ilaparru 
##                       4442                       1235 
##                    Ilavara                   Ilkolunu 
##                       1491                       2640 
##           ILLAMNAIDUVALASA                     Illuru 
##                        326                       3004 
##           ILLURU KOTHAPETA                    Ilparru 
##                       1812                       1416 
##                  Ilpvuluru                    Ilupuru 
##                       2153                        810 
##                      Iluru            Immidiwarappadu 
##                       1083                        702 
##                  INAGALURU                  Inamadugu 
##                       2592                       4303 
##                   Inampudi                    Inavolu 
##                        803                       2362 
##                Indiravathi               Indireswaram 
##                        581                       1030 
##               IndlaCheruvu                Indugapalli 
##                        972                        788 
##                Indugupalli              Indukuripalli 
##                       1129                        315 
##             Indukurpet - i             Indukurpet -ii 
##                       2554                       3836 
##                   Indukuru                   INDUKURU 
##                        804                       1187 
##               INDUKURUPETA                    Indulur 
##                       2168                        915 
##                  Indupalli                    Indupur 
##                       6075                       1851 
##                    Ingallu                Ingilapalli 
##                       1720                        798 
##             Ingilipaklanka                   Ingldhal 
##                        853                        638 
##                    Ingluru                   Inimerla 
##                       5475                        560 
##                    Injaram                     INJARI 
##                       2230                        930 
##                     Injedu                     Inkole 
##                        499                       9601 
##               Inmnamelluru                     Interu 
##                       3969                        611 
##                     Inturu                   Inugunta 
##                       3572                        754 
##                   Inukurti                   Inumella 
##                        993                       2638 
##                  IppaGunta                 Ippalvlasa 
##                        702                       2130 
##                 IPPANAPADU               IPPANTHANGAL 
##                       2138                        302 
##                  IppaPenta                    Ippatam 
##                       1578                       2292 
##                    Ippatla                     Ipperu 
##                        961                       3593 
##                     Ippili                 Ipurupalem 
##                       1391                      22671 
##                  Iradpalli                     IRAGAI 
##                       1045                        723 
##                 Iragavaram                 Iran banda 
##                       3694                        471 
##                 Iran Banda                  IRIKIPENT 
##                        645                       1217 
##                      Irkam                   Irlapadu 
##                        906                       3506 
##                   IRLAVADA                   Irnapadu 
##                        838                       2036 
##                     Irpadu                   Irripaka 
##                       1598                       1418 
##                Irsalgundam                   IRUGULAM 
##                        311                       1486 
##                  IRUGUVAIE                 Irusumanda 
##                       1060                       2465 
##                    IRUVADA                    Iruwada 
##                        287                       1375 
##                    Isakala               ISAKALA PETA 
##                       1605                        347 
##                 Isakapalli                Iskadamerla 
##                       6312                        974 
##                  Iskapalem                  Isklpalem 
##                       5171                       1026 
##            Isranayak tanda                  Isukapadu 
##                        448                        454 
##                 ISUKAPALLE                 Isukapalli 
##                       1446                       1702 
##               Isukatageeli           Isukatripurwaram 
##                       1109                       1066 
##                   Isukpudi                       Isvi 
##                       2391                       1431 
##                   Ithapudi               ITHARAM PETA 
##                       1459                        679 
##                      Itika              Itikarlapalli 
##                        901                        340 
##               ITIKULAKUNTA                  ITIKYAALA 
##                        724                        491 
##            Itlamamidipalli                      Itodu 
##                        827                       1547 
##              ITUGULLA PADU               J Kothapalli 
##                        739                        538 
##              J Kottalpalli              J. KOTHAPALLE 
##                        800                        819 
##               J. Panguluru                  J.AmPuram 
##                       3607                        810 
##                J.Annavaram           J.B.Krishnapuram 
##                       2031                        351 
##        J.B.PURAM AGRAHARAM               J.D.Kandrika 
##                       1037                        907 
##               J.GOLLAPALLI              J.Gopalapuram 
##                        257                        151 
##                  J.Hosalli                 J.K.Gumada 
##                        370                        222 
##                J.KeshPuram                  J.Kommara 
##                        302                       2324 
##               J.Kothapalle                   J.Kothur 
##                        592                       1735 
##               J.NAIDUPALEM                J.P.Cheruvu 
##                       1958                        901 
##                 J.P.Kothur                  J.R.Puram 
##                        402                        276 
##           J.Rangarayapuram              J.Thimmapuram 
##                       1511                       2194 
##              J.V.Agraharam               Jaali manchi 
##                       1005                       1230 
##                   JaalWadi                  Jaanapadu 
##                       1740                       5620 
##                Jabarlapudi                       Jada 
##                        106                        629 
##                   JADDANGI             JADDETI VALASA 
##                       1860                       1026 
##                    Jaddevi                     Jadpet 
##                        348                        219 
##                  JaduPalli                   Jadupudi 
##                       1198                       1014 
##                     Jaduru                   Jadvalli 
##                       1579                        315 
##                    Jadyada                   Jafrabad 
##                        256                        349 
##    Jagadevipet [Leburu-ii]                  JAGAMARLA 
##                       1845                        467 
##             JAGAMETLAPALEM             JAGANADHAPURAM 
##                        717                        624 
##             JAGANNADAPURAM             Jagannadhagiri 
##                        592                       1210 
##            Jagannadhapuram            JAGANNADHAPURAM 
##                       9136                       1495 
##        Jagannadharajapuram            Jagannadhavlasa 
##                       1284                        665 
##              Jagannadpuram          Jagannayakulpalem 
##                        546                       2786 
##        Jagapathi Rajapuram           JagapathiNagaram 
##                        305                       6047 
##                    JAGARAM                Jagarlamudi 
##                       1270                       1744 
##                     Jagati                JagatiPalli 
##                       1366                        288 
##                   Jagdurti              JaggaiahPalem 
##                        446                        842 
##          Jaggaiahpet Urban                JAGGAMPALEM 
##                      23839                        655 
##                 Jaggampeta                 JAGGAMPETA 
##                       9938                        409 
##                Jaggannapet                 JaggaPuram 
##                       1148                        543 
##                 Jaggawaram               Jaggilibontu 
##                       1268                        249 
##            JAGGUDORAVALASA           Jaggushastrulpet 
##                        275                        736 
##             JAINAVARIGUDEM                JAITHAVARAM 
##                        520                       1025 
##                   Jajarkal                 Jajulkunta 
##                        640                        454 
##                     Jajuva             JakkalaCheruvu 
##                        144                       2867 
##               Jakkamcherla                 Jakkampudi 
##                        259                       4802 
##                     Jakkar                   Jakkaram 
##                        607                       1342 
##              JakkaSamudram            Jakkasanikuntla 
##                        802                        643 
##                  JAKKIDONA            Jakkulanekkalam 
##                       1032                        516 
##                    JakkuVa                     JALADA 
##                       1714                        548 
##                     Jaladi                 Jaladurgam 
##                       1489                       2437 
##           JALAKA LIGAPURAM                JalalaPuram 
##                        510                       1105 
##                   Jalalara                 JALAMPALLI 
##                        180                       1652 
##               Jalantrakota                     Jaldam 
##                       1344                        245 
##                   Jaldanki                   Jalimudi 
##                       4573                        485 
##                   Jalipudi                  Jalknooru 
##                       2651                       1444 
##             Jallivarigudem                    Jalluru 
##                        355                       2013 
##                 Jalluvlasa  Jalpawarigudem,Ankalampad 
##                        267                       1408 
##                   Jalumuru                    Jambada 
##                       1600                        285 
##                 JAMBAPURAM        JAMBHUKESWARA PURAM 
##                        461                        761 
##           Jambu vari palli               Jambugumpala 
##                       1333                       3000 
##               JAMBULADINNE               Jambuldinane 
##                        165                        681 
##                 Jambulpadu                Jambupatnam 
##                        197                       3122 
##                Jamchakramu                    Jamdala 
##                        559                       1400 
##                       Jami             Jamidaggumilli 
##                       7549                        293 
##             Jamidintakurru             Jamigolvapalli 
##                        331                       1574 
##                   JAMIGUDA             JAMMADEVI PETA 
##                        925                        898 
##              JAMMADEVIPETA              JAMMALAMADAKA 
##                        399                        190 
##              Jammalamadugu               JAMMALAPALLI 
##                      25699                        318 
##               Jammalmadaka                Jammalpalem 
##                        324                        991 
##               Jammanapalli                 Jammavaram 
##                        362                        355 
##                 JAMMAVARAM                      Jammi 
##                        840                       1342 
##              Jammidivalasa                      Jammu 
##                        362                        478 
##         JammuNarayanapuram                JAMPA PURAM 
##                       4348                       1417 
##                    Jampani                 Jampapalem 
##                       3482                        858 
##                 Jamparkota                    JAMPENA 
##                        680                        488 
##               Jamukuldinne                Jamulapalli 
##                        529                        668 
##            JANAKI RAMPURAM                  JANAMGUDA 
##                       2408                        410 
##             JANARDANAPURAM            Janardhanavaram 
##                        347                        789 
##              Janardhnpuram                     JANDLA 
##                        268                       1053 
##              jangala palle               JANGALAPALLE 
##                        523                        706 
##               Jangalapalli               JANGALATHOTA 
##                        413                        438 
##             Jangalkandriga                Jangalpalle 
##                        515                        375 
##                Jangalpalli        Jangam Areddy Palli 
##                       4355                        446 
##                Jangamgudem           JangamReddipalli 
##                       1074                        687 
##          Jangamvani Doruvu           Jangareddigudena 
##                        345                      32418 
##               JANGIDAPALLI                  Janguluru 
##                        381                        255 
##                  JANGULURU      Janguluru Velam Palem 
##                        161                        229 
##                 Jannawaram                 Jannivlasa 
##                       1066                        507 
##                  Jantuluru             Janumalluvlasa 
##                        713                       1169 
##                  Janupalli              Japadu Bangla 
##                       2464                       2575 
##                    Jarazam                  Jarjanagi 
##                       1509                        407 
##                 Jarjapupet            JARRAVAARIPALLI 
##                       3566                        966 
##                 Jarribadra                     Jarugu 
##                        475                        599 
##                Jarugumalli                      Javam 
##                       1097                        241 
##                    Jayampu                   Jayanthi 
##                       1405                       2551 
##              Jayanthipuram                  Jayapuram 
##                       1159                        450 
##                     Jayati                  Jayavaram 
##                        924                        653 
##                Je.Kakinada            Jed. Gangavaram 
##                       1063                       1625 
##           Jed. RagamPettah            Jed.Kothapatnam 
##                       3725                        677 
##                Jee.M.Puram                 Jeediguppa 
##                        473                        708 
##                 Jeedipally                JEELAPATURU 
##                       1786                        895 
##              JEELUGULAPUTU               Jeelugumilli 
##                        908                       2336 
##                  JEENABADU                   JEEPALEM 
##                        782                        371 
##                 Jegurupadu                  Jennagayi 
##                       7885                        614 
##                      Jerla          JERRIPOTHULAPALEM 
##                       2408                        338 
##               Jgarajupalli                  Jidigunta 
##                       1634                        576 
##                    Jigiram   Jilkarragudem,Guntupalli 
##                       1160                       1699 
##             Jilledabudkala                Jilledipudi 
##                        383                        819 
##                Jilledupadu               Jilleduvlasa 
##                        239                        594 
##               jillelamanda                JILLELAMUDI 
##                       1439                        514 
##                   Jillella                   JILLELLA 
##                       1114                        763 
##              JILLELLAGUDEM               Jillellamudi 
##                        568                        278 
##                   Jillunda                  Jinipalle 
##                        267                        787 
##                    Jinjeru                 Jinkibadra 
##                       1207                       1015 
##                     Jinnam               Jinnelagudem 
##                        139                        544 
##                    Jinnuru                 Jinulkunta 
##                       3664                        566 
##                Jirukovwada                  Jirupalem 
##                        220                       1039 
##          Jiryaali Chintuva               Jiyammavlasa 
##                       1612                       3481 
##               jiyyannapeta             JIYYANNAVALASA 
##                        474                        375 
##                Jodubandala                  Jogampeta 
##                        223                       2719 
##                 Jogannapet                  JogiPalli 
##                       2524                        435 
##             JogirajuPettah                Joharapuram 
##                       1151                       8273 
##                JOHARAPURAM                  Joldrashi 
##                       1271                        872 
##                     Jonaga                    Jonanki 
##                        232                       1264 
##                    Jonnada                  Jonnagiri 
##                       9799                       4291 
##               Jonnalagadda           Jonnalkothapalli 
##                       5588                       1296 
##                 Jonnalpadu                     Jonnam 
##                        140                        315 
##                 JonnaTalli                Jonnavalasa 
##                       1600                       2303 
##                  Jonnawada                  Jorepalli 
##                        809                        792 
##   Jorepalli AkkamambaPuram         Joukula Kothapalli 
##                        663                       3111 
##                JOWNI PALLI                  Jujawaram 
##                       1584                       1210 
##                    Jujjuru                  Julakallu 
##                       3248                       3401 
##                     Julkal                  Julkaluva 
##                        914                       1145 
##                   Jullunda                  Julukunta 
##                        670                        763 
##             Jumamala Dinne                    Jumbiri 
##                        965                        955 
##             Junjuram Palli               Junjurupenta 
##                       2247                        486 
##                   Junutala                     Jupudi 
##                       1085                       4946 
##                    Juthada                    JUTHADA 
##                       1502                        815 
##                    Juthiga                      Jutur 
##                       1755                       5767 
##               Juvvaladinne                  Juvvaleru 
##                       5964                        383 
##           Juvvalguntapalle                Juvvalpalem 
##                        464                       1188 
##                Juvvanapudi                 Juvvigunta 
##                        380                        383 
##                 Jwolapuram                     Jyothi 
##                        431                        589 
##                 K K KOTTAL                  K N Palli 
##                        163                        232 
##                 K R KOTALA           K Sugmanchipalli 
##                        584                        651 
##              K Thimmapuram         K. Jagannadhapuram 
##                        484                       1562 
##            K. Krishnawaram              K. MarkaPuram 
##                       1017                        327 
##             K. Nagalapuram           K. NAKKANA PALLI 
##                       1845                       1405 
##              K. NASAMPALLE            K. OBULAM PALLE 
##                        695                        411 
##               K. Rajupalem                K.Agraharam 
##                       2997                        957 
##            K.B.P.AGRAHARAM                K.B.R.Puram 
##                        589                       2260 
##               K.Bitragunta           K.BUDUGUNTAPALLE 
##                        750                        675 
##                  K.CHERUVU               K.Chorlanagi 
##                        166                         59 
##                K.D. Pettah               K.DODDIPALLI 
##                       2753                        689 
##               K.G.Kandrika         K.I.ChinnaiahPalem 
##                       1047                       2499 
##            K.Illindalparru                  K.J.PURAM 
##                       1617                       3603 
##               K.K.Agrahram                  K.K.Gunta 
##                       3050                       1267 
##              K.K.Rajapuram                K.K.V PURAM 
##                        845                        550 
##                 K.Kandrika               K.Kannapuram 
##                        136                        369 
##                 K.KOTAPADU                 K.Locherla 
##                       2743                       1393 
##               K.M.Kandriga                  K.M.PURAM 
##                        459                       1795 
##              K.MATCHALESAM          K.MUTYALAMMAPALEM 
##                        443                       1284 
##               K.NAIDUPALEM             K.O. Agraharam 
##                       1240                        991 
##            K.O. MallaVaram              K.P.AGRAHARAM 
##                       2797                        812 
##         K.Palli-Irramanchi               K.PallValasa 
##                       1121                        748 
##                K.Peddapudi                    K.Putti 
##                       2274                        387 
##                  K.R.Puram                  K.S.Palem 
##                        238                        585 
##                  K.S.Puram                K.S.R.PURAM 
##                        709                        169 
##                 K.Sairigam           K.Sankirenipalle 
##                        635                        778 
##              K.SANTHAPALEM                  K.Sawaram 
##                       1411                       1499 
##              K.Sirigepalle                  K.Temburu 
##                        285                        224 
##              K.Thimmapuram               K.Uppalapadu 
##                       1492                       1045 
##             K.Uppara Palli                 K.V. Palli 
##                       1824                        766 
##               K.V.B. PURAM   K.V.M. AGRAHARAM HARIZAN 
##                       1048                        232 
##                  K.V.PURAM               K.VALLAPURAM 
##                       1023                       1021 
##             K.VEERAGHATTAM          K.Velamavaripalli 
##                        121                        714 
##             K.Venkatapuram            K.Yam.Agraharam 
##                        717                       1536 
##               K.YERRAGONDA              K.YERRAMPALEM 
##                        368                       1090 
##                  KaapVaram              Kaarakampalle 
##                       7311                        297 
##                  KAATIPERI                 KACHAPURAM 
##                       1631                       1078 
##                KACHARAVEDU                 kachavaram 
##                        687                        511 
##                 Kachavaram                  Kadagunta 
##                       1416                        633 
##                  Kadakella                     KADALI 
##                        333                       5093 
##              Kadapa Shahar                KADAPAGUNTA 
##                      63434                       1052 
##                  Kadapalli               KADAPANATHAM 
##                        475                        542 
##              Kadapayapalle                Kadavakollu 
##                        712                        674 
##               Kadavakuduru             Kaddara Benchi 
##                       2298                        490 
##                     KADELI                   Kadgandi 
##                        679                        410 
##            KADHIRIMANGALAM                  Kadidoddi 
##                        468                        293 
##                  Kadimetla            KADIRAYACDHERVU 
##                       4141                        241 
##            KADIRAYACHERUVU                     Kadiri 
##                        295                      53711 
##        Kadiri Brahmanpalli         Kadiri KuntlaPalli 
##                       1745                       1567 
##          KADIRINATHUNIKOTA            KadiriNeniPalli 
##                        683                       2051 
##           KadiriPoolaKunta           KADIRIVARI PALLI 
##                       1366                        516 
##                 KADIRVE DU                  KADITHOTA 
##                        367                        732 
##                   KADIVEDU                  Kadivella 
##                       2092                       2003 
##                  Kadiyadda                    Kadiyam 
##                       3246                      24035 
##                    Kadluru               Kadmal Kunta 
##                       3159                        784 
##                 Kadmlkalva                     Kadumu 
##                       2222                       1636 
##                   Kadumuru                     KADURU 
##                       2635                        506 
##                  Kadvkallu                      Kagam 
##                       2128                       1276 
##                     KAGATI                     Kagita 
##                        580                        736 
##                Kagitalpuru               KAGITHAPALLI 
##                        766                        334 
##                   Kagupadu                   KAGUVADA 
##                        430                       2207 
##                 KAGUVALASA         KAIDHUGANIKANDRIGA 
##                        653                        672 
##                     KAIGAL                    Kaijola 
##                        382                        548 
##                  Kaikaluru                   Kaikaram 
##                       9320                       3472 
##                   Kaikvolu                     Kailam 
##                        890                        499 
##              Kailasapatnam                      KAIPA 
##                        980                        991 
##                 Kaitepalli                       Kaja 
##                       1153                      10761 
##                Kajee Palem          Kajipet,Sunkesula 
##                        736                       9444 
##                   Kajuluru                  Kakandyam 
##                       7560                        411 
##                     Kakani                 KakaraGood 
##                       1123                        227 
##                KakaraPalli                Kakaraparru 
##                       1908                       3638 
##                    Kakarla                Kakarlamudi 
##                       2193                       2221 
##                KakarlaPadu                  Kakarvada 
##                        322                       1705 
##                   Kakavedu                       Kaki 
##                       2085                       2244 
##                   Kakileru                   Kakinada 
##                        904                     225150 
##  Kakinayana cheegarlapalli                  Kakisnuru 
##                        559                        325 
##                   Kakivayi                    Kaknoor 
##                       1058                       1884 
##                 Kakrapalli                  Kakrmilli 
##                        882                        848 
##                   Kakrvayi                 Kakulapadu 
##                        641                       1151 
##            KAKULAVARIGUDEM                 Kakulwaram 
##                        166                        586 
##                   Kakumanu                  Kakupalli 
##                       3402                       4538 
##                     KAKURU                   Kakuturu 
##                        101                       1199 
##                   KAKUTURU               Kalabacharla 
##                        582                       3161 
##                   KALAGADA                Kalagampudi 
##                       1195                        340 
##                   Kalagara                  KALAGATUR 
##                       1823                        920 
##                   KALAKADA           KALAMANAIDU PETA 
##                       2463                        759 
##            KALAMANDALAPADU             KALAMRAJU PETA 
##                        350                        364 
##                 KALAN JERI                   Kalapaka 
##                        582                        857 
##                  Kalaparru                  Kalapuram 
##                        593                        497 
##                  Kalasapad                  KALATHURU 
##                       3050                        750 
##     KALATHURU HARIJANAWADA                  KALATTURU 
##                        993                        327 
##                   Kalaturu               KalavaCherla 
##                        258                       1302 
##                KALAVAGUNTA                 KALAVAKURU 
##                       3836                       3750 
##              KALAVALAPALLI                  KALAVALLA 
##                       4091                        904 
##                KALAVAPALLE               Kalavapamula 
##                       1564                       1430 
##                  Kalchatla                    Kaldari 
##                       1174                       2460 
##                 KALE PALLI                  Kalekurti 
##                        541                       1031 
##                     KALERU                   Kalgalla 
##                       1487                        572 
##                   Kalganda                  Kalgantla 
##                        330                        326 
##               Kalgurtipadu                  Kalibanda 
##                        575                        800 
##                  Kalichedu                 KALICHERLA 
##                       1549                       3285 
##                 Kalidindhi                    Kaligam 
##                       9247                        898 
##                   Kaligiri                  Kaligotla 
##                       4730                       1378 
##                  KALIGOTLA                 KALIJAVEDU 
##                       1609                        761 
##                KALIKAPURAM                   KALIKIRI 
##                        281                      16154 
##                 KALIMBAKAM                 Kalipatnam 
##                       1470                       8192 
##                     Kalipi                 Kalisipudi 
##                       2212                        932 
##                   Kalivedu                  Kaliwaram 
##                        457                        400 
##                    KALKADA                   Kalkurru 
##                       3581                        629 
##                      Kalla               Kallacheruvu 
##                       3499                       1356 
##                    Kallada                  Kallakuru 
##                        410                       2510 
##                 KallaPalem                    Kallata 
##                       1539                        705 
##                 Kallempudi                 Kallepalli 
##                        769                       2801 
##                    Kalleru                  Kallikota 
##                        659                       1326 
##                 KALLIVETTU             KALLOORU PALLE 
##                        438                       1303 
##                KALLU PALLI          Kalludevana Halli 
##                       1102                       1183 
##              Kalludevkunta                 Kallukunta 
##                        990                       2941 
##                 Kallumarri                   Kallumdi 
##                       2762                       2626 
##                     Kallur                    Kallura 
##                       1771                       2894 
##              Kalluri palli                    kalluru 
##                       1951                      87357 
##                    KALLURU                   Kallutla 
##                       7585                        706 
##                   Kalmalla                  Kalnutala 
##                       6343                        855 
##                    Kalpadu        Kalpanayuni Cheruvu 
##                        544                        664 
##                   Kalparti             Kalrayangudena 
##                        422                        878 
##                 Kalsmudram                   Kalugodu 
##                       2281                       3924 
##                  Kalugotla             Kalugotlapalle 
##                       6244                        527 
##             Kalujuvvalpadu                   Kaluvaya 
##                       1295                       5948 
##                      Kalva                Kalva Palli 
##                       2720                       1854 
##                 Kalvakonda                 Kalvapalle 
##                        328                        446 
##        Kalvapudi Agraharam                  KALVATALA 
##                        519                        723 
##                Kalvlapalli                  Kalvlpudi 
##                       1620                        328 
##        Kalwarayi Agraharam                     Kalyam 
##                       1391                       1179 
##              KALYANA PURAM               KALYANAMPADU 
##                        798                        259 
##               Kalyandurgam                Kalykagollu 
##                      24420                       1010 
##            KAMACHINA PALLE               Kamaiahpalem 
##                       1179                        683 
##                 Kamakuntla                 Kamalakuru 
##                        553                       1222 
##           KAMALANABHAPURAM                 Kamalapadu 
##                        579                       1431 
##                Kamalapuram                Kaman Doddi 
##                      14648                        748 
##                   Kamanuru              Kamarajugadda 
##                       3056                        885 
##               Kamaru Palli               Kamasamudram 
##                       1747                        896 
##               KamaSamudram               KamatamPalli 
##                        761                        477 
##                Kamatamuuru                  KamaVaram 
##                        703                       1943 
##  KAMAVARAM H/OKORSAVARIGUD             KamavarapuCoat 
##                        279                       8913 
##             KAMAVARAPUKOTA               KAMAYYAKUNTA 
##                        476                        210 
##                KAMAYYAPETA                  Kambadhal 
##                        853                       1754 
##                   Kambadur                   KAMBAKAM 
##                      10606                        446 
##                  Kambakaya               KambalaDinne 
##                        881                        690 
##                KambalaPadu               KambalaPalle 
##                       1569                        180 
##          KAMBALARAYUDIPETA                Kambaldinne 
##                       1486                       2186 
##                  Kambalhal                Kambalnooru 
##                       1911                        779 
##                 Kambalpadu                 Kambampadu 
##                       2368                      11952 
##                    Kambara              KAMBARAVALASA 
##                        554                        294 
##           KAMBHAMVARIPALLI                 Kamdhenuvu 
##                       1753                        200 
##                  Kamepalli              kameswaripeta 
##                       5760                       1222 
##              KAMESWARIPETA               Kamgnikuntla 
##                        434                        835 
##          Kaminaayani palli              KAMINAIDUPETA 
##                       1639                        968 
##           KAMINAYANI PALLI              KamineniPalle 
##                        521                        913 
##                   Kaminhal                     Kamini 
##                        786                        503 
##         KAMIREDDYVARIPALLI                    Kamkuru 
##                        681                        640 
##                  KamlaPadu                  Kamlapuri 
##                       1809                        542 
##             KAMMA KANDRIGA                KAMMA PALEM 
##                       1433                        911 
##            Kammaguttapalle                KAMMAKOTURU 
##                        950                        431 
##              KAMMANA PALLI                Kammanamolu 
##                        736                       2353 
##                 KammaPalli                Kammarchedu 
##                        614                        544 
##                Kammasigdam                KammaValasa 
##                        369                       1497 
##                 KammaVaram            Kammavari palli 
##                        559                        514 
##                    Kammuru             Kammwari Palli 
##                       1549                       1028 
##              Kammwaripalli                    KAMPALE 
##                       1012                        800 
##                 Kampamalla              Kampasamudram 
##                        732                       4366 
##            Kampumanupakalu            Kamsalibetapudi 
##                        551                        574 
##                Kan Cheruvu                   Kanagala 
##                        209                       3187 
##              Kanaganipalli                 KANAGUDURU 
##                       4177                       2519 
##               KanakaDinne,             KANAKADRIPALLE 
##                        294                       1940 
##                KanakamPadu                Kanakaveedu 
##                        738                       3849 
##           Kanakayyakottala                     Kanala 
##                        273                       2450 
##                KANAM PALLE                    KANAMAM 
##                        511                        637 
##              KANAMANAMBEDU              Kanamanapalli 
##                        630                        477 
##                  Kanchadam               Kanchakoduru 
##                        593                        780 
##                   Kanchali              Kanchanapalli 
##                       3323                        497 
##            KANCHANAPUTTURU             KANCHARA PALEM 
##                        857                        556 
##              KANCHARAGUNTA              Kancharapalem 
##                        337                       2641 
##                   Kanchela         KANCHENNAGARIPALLE 
##                        553                        500 
##                   Kancheru        Kanchibandarlapalli 
##                       1204                       1471 
##          Kanchidasanapalle             KanchikaCharla 
##                        736                      14293 
##                KanchiPalli             KanchiSamudram 
##                       1450                       3081 
##                   Kanchram              KANCHUGUMMALA 
##                       2405                       1033 
##                Kanchumarru                    Kandadu 
##                        767                       1331 
##               Kandalampadu                KandalaPadu 
##                        193                        555 
##              Kandaleru Dam                    Kandali 
##                        506                        640 
##               Kandamkuntla                  Kandamuru 
##                       1763                        909 
##               Kandanalpadu                  Kandanati 
##                        625                       1630 
##                  Kandarada                Kandikapula 
##                       2352                        457 
##             Kandikayapalle                 KandiKuppa 
##                        883                       5873 
##                  Kandipudi                    Kandisa 
##                       2104                        552 
##                KandiValasa               Kandla Palli 
##                       1037                        751 
##               Kandlaguduru                Kandlagunta 
##                        687                       1756 
##                Kandlakunta                   KANDLURU 
##                       3252                        199 
##                     Kandra                 Kandrakota 
##                        640                       2677 
##                 Kandregula                   KANDRIGA 
##                       2229                        354 
##                   Kandukur                  Kandukuru 
##                      17615                       4300 
##                  KANDUKURU               KandulaPadam 
##                       1748                        711 
##                Kandulapadu               Kandulapalem 
##                        482                       1264 
##               Kandulapuram                  Kanduluru 
##                       3107                       1151 
##                    KANDURM                    KANDURU 
##                       1237                       3030 
##                    Kanekal                  Kangundhi 
##                      14393                        659 
##                   Kangundi                 Kani pakam 
##                       1040                       2130 
##                   Kanigiri                  Kanimella 
##                      12066                        786 
##                 Kanimeraka                  Kanimerla 
##                        574                        661 
##                  Kanimetta                  KANIMETTA 
##                       1047                       2383 
##                     Kaniti                 Kanitivuru 
##                      10689                        730 
##                   KANIVADA                Kaniyampadu 
##                        970                        313 
##             KankanalaPalli               Kankatapalem 
##                       3276                       2488 
##                  Kankatava           Kankipadu Arbana 
##                        964                       8495 
##                Kannaigudem                Kannaigutta 
##                         73                        696 
##                     Kannam                Kannamdkala 
##                        285                       1704 
##                KannamPalli           Kannapudoravlasa 
##                        784                       1104 
##               Kannapukunta                 KANNAPURAM 
##                        571                       2878 
##                 KANNAVARAM               KANNAYAGUDEM 
##                       1059                        767 
##                  Kanneluru                Kannemadugu 
##                       3581                       1135 
##                 Kannepalli                Kannevalasa 
##                       3192                        459 
##                  Kannevidu                   Kannooru 
##                       1319                        446 
##                   Kanparru             KANTABAMSUGUDA 
##                       1765                       1114 
##               KANTAKAPALLI           KantamRajuKondur 
##                        856                       2172 
##                 Kantepalli                  Kantepudi 
##                        311                       1400 
##                    Kanteru               KANTHAMPALEM 
##                       3402                        252 
##                  Kantharam                    Kantlam 
##                        410                        289 
##                 Kantragada               Kanugulvlasa 
##                       1013                       1688 
##                  KanuKollu                  Kanumalla 
##                       1928                        792 
##              Kanumarlapudi             Kanumlacheruvu 
##                       2827                       1578 
##               Kanumlopalli              KANUMOLAPALLI 
##                        747                       2462 
##                   Kanumolu                Kanumukkala 
##                       5172                       3448 
##                  Kanumurru                 Kanuparthi 
##                       2634                       5026 
##             KanuparthiPadu                   Kanupeda 
##                       1616                        387 
##                   Kanupuru                Kanupuru-11 
##                       5119                       1410 
##             KANUPURU PALLI              KanupuruPalle 
##                       1108                        525 
##                     Kanuru           Kanuru Agraharam 
##                       5502                       1591 
##              Kanuru Arbana                   Kanwaram 
##                      15870                       3439 
##                     Kapati                  Kapavaram 
##                       2074                       2407 
##                  KAPAVARAM           Kapileswarapuram 
##                       2217                       2571 
##           KAPILESWARAPURAM               KappalaBanda 
##                       5464                       1337 
##               Kappaladoddi                 Kappatrala 
##                       1677                        997 
##                    Kappram               Kaptanupalem 
##                         92                        643 
##           Kapugodayivalasa                KAPUGUNNERI 
##                        405                        852 
##                KAPULAPALLE                Kapuluppada 
##                        341                       1875 
##                   Kapuluru                Kapushambam 
##                       1400                        634 
##               KAPUSOMPURAM                     Karada 
##                        599                       1691 
##               KARADAVALASA               Karagraharam 
##                        202                       1363 
##                     Karaka             Karaka Mukkala 
##                        556                       1648 
##        KARAKAMBADI (RURAL)                 KarakaPadu 
##                       5574                       1136 
##               KarakaValasa               KARAKAVALASA 
##                       2014                        447 
##                  KARAKUNTA                 Karalapadu 
##                        488                       3810 
##                 Karamchedu                  Karampudi 
##                       6942                       7526 
##                     Karani                     KARANI 
##                        411                        540 
##                     Karapa             KARASANA PALLI 
##                       7017                        806 
##                Karasuvlasa                KARATAMPADU 
##                        598                       1514 
##                   Karavadi               Karballavolu 
##                       3377                        746 
##                     Karedu                      KAREM 
##                       3325                        246 
##                     Kargam           Karicharlagudena 
##                        538                       1110 
##               karidi konda               Karidiguddam 
##                        334                        198 
##                Karidikonda              Kariganipalli 
##                       1355                       3024 
##                   Karijata                   Karikera 
##                        997                       2733 
##                Karimaddela                 KARIPAAKAM 
##                       2442                        605 
##                 Karivemula                   Karivena 
##                        978                       3398 
##                    Karjada                     Karkam 
##                       2046                       1506 
##                  Karkuduru              Karkvanipalem 
##                       2091                        972 
##                 Karlagatta                     Karlam 
##                        656                       4613 
##                 Karlapalem                  Karlapudi 
##                       8756                       3150 
##            Karmalvaripalle             karnavanipalem 
##                        424                       1694 
##                    Karpadu                KarriValasa 
##                        538                        909 
##             Karrivanipalem               Karrollapadu 
##                        675                        113 
##                    Kartali               Kartalipalem 
##                        380                        935 
##                Kartanparti                  Karuchola 
##                       2102                       1297 
##              Karugorumilli                 Karumanchi 
##                       2284                       5235 
##              KARUMANUPALLI                   Karumuru 
##                        481                       1035 
##      KARUR ANE KRISHNAGIRI                   Karvanja 
##                       2121                        869 
##             KARVETINAGARAM                  Kasanooru 
##                       7660                       1565 
##                   KASAPETA                 KasaPettah 
##                       1075                        778 
##                  Kasapuram                 Kasarabada 
##                       2117                        519 
##                    Kasaram                 KaseePuram 
##                        532                        940 
##        KaseeRajuKaseePuram    KASHI VISHWANATHA PURAM 
##                        167                        602 
##              Kashinvalspet                  KashiPadu 
##                        798                       3886 
##                 KASHIPURAM                Kashyapuram 
##                        580                        270 
##                 Kasi ralla                  KASIBUGGA 
##                        681                      16123 
##                KASIM MITTA                     Kasimi 
##                        556                        421 
##          kasimivalasa peta                  Kasimkota 
##                        848                      10801 
##                 KASIPATNAM                  Kasipuram 
##                       1670                        166 
##                  KASIPURAM             Kaspapentapadu 
##                       1056                       2010 
##                Kassamudram                    Kastala 
##                        676                        849 
##                KasturiPadu                   Kasumuru 
##                        790                       3756 
##            Kaswareddipalem                    Kasypet 
##                       1305                        920 
##           KATAKAMAYYA PETA               Kataknipalli 
##                        197                       1802 
##                 KatakPalli                Katarukonda 
##                       1239                       1989 
##                  Katepalli                     Kateru 
##                       1740                      12586 
##                  Katewaram                  Kathaluru 
##                       7200                       1417 
##                 Kathimanda                  Kathipudi 
##                       2824                       4024 
##               KATHIRAPALLE             KATHIVARIPALLI 
##                       1093                        495 
##             Katiganikalava                KATIKAPALLE 
##                       3750                       1053 
##             Katikvanikunta         Katineni Yarragudi 
##                        308                       1144 
##                 KATNAGALLU                KATRA PALLI 
##                        978                        272 
##                  KATRAGADA                 Katragunta 
##                        226                       1017 
##            Katrakayalgunta               Katraolpalli 
##                        208                       5705 
##                  Katrapadu                Katrayapadu 
##                       1791                       1070 
##                katrenikona                Katrenipadu 
##                       7352                       3986 
##                    Katriki                  KatriMull 
##                       1303                       1349 
##          katta kinda palli         KATTAKINDHA PALLLI 
##                        649                       1057 
##                Kattamanchi                  Kattamuru 
##                       7959                       6006 
##              KATTERAGANDLA             Kattubadipalem 
##                       1975                        412 
##                  Kattubolu                   Kattunga 
##                        759                       2825 
##                 Kattupalem               Kattuvapalli 
##                        630                       1511 
##       KATTYA CHARYULA PETA                     Katuru 
##                        486                       2439 
##                     KATURU                   Katwaram 
##                        664                       1881 
##              Kausalyapuram                   Kautalam 
##                        618                       4589 
##                    Kautram         Kautwari Agraharam 
##                       3924                       1165 
##               kavalakuntla                     Kavali 
##                        715                      66307 
##              Kavali Bit -i         Kavali. Mustapuram 
##                       3010                        434 
##             KavaliEdavalli                Kavalipuram 
##                       1966                       1127 
##                   KAVANURU            Kaveri Samudram 
##                       1016                        965 
##            KAVETIGARIPALLI                Kaviripalli 
##                       1979                       1341 
##                    KAVITAM                     Kaviti 
##                       4409                       6589 
##                KAVITIBADRA                 Kavlkuntla 
##                        322                        305 
##                Kavnamapata                   Kavuluru 
##                       1071                       2309 
##                  Kavulwada                     Kavuru 
##                        649                       5340 
##            KAVURUVARIPALLE                 Kavvagunta 
##                        299                       1797 
##                Kay. Kaviti           Kay.O.MallaVaram 
##                        445                       1761 
##                      KAYAM                    Kayyuru 
##                        649                       1200 
##              KEASAVAKUPPAM                KedariPuram 
##                        306                       4234 
##                KEELA GARAN                KEELA PATLA 
##                       1149                       1904 
##                 KEELA PUDI                 Keelapattu 
##                       1740                       1692 
##                Keera manda                KeerthiPadu 
##                       1537                        834 
##               KEERTHIPALLI         Keerthirayanigudem 
##                        384                        557 
##                    Keesara                     Kekati 
##                       1063                       2704 
##                 KELAVALASA                  KELAVATHI 
##                       1103                        350 
##                      Kella                KELLAMPALLI 
##                       1561                       1340 
##                  Kemiseela              Kempasamudram 
##                        779                        897 
##            Kenamakulapalli              Kenchanaballa 
##                        346                        867 
##                    Kenguva                 Kerasinagi 
##                        535                        185 
##                    Keratam           kesamaneni palli 
##                        301                        946 
##               kesana kurru                Kesanapalli 
##                       7014                       2390 
##                KESANAPALLI                Kesanupalli 
##                       7203                       2813 
##                  Kesapuram                KesaraPalle 
##                       1128                       5764 
##            KESAVADASUPALEM            KESAVADASUPURAM 
##                       4373                        746 
##               KesavaKuppam                Kesavapuram 
##                        755                        404 
##                  Kesavaram                  KESAVARAM 
##                       1201                       8613 
##            KESAVARAVU PETA               Keshavapuram 
##                        966                        711 
##                 Keshipuram                 Keshupuram 
##                        269                       2935 
##              Keshwarappadu          Keshwarayunipuram 
##                        939                         93 
##                      Kesli                   Keswaram 
##                        947                       1965 
##                Ketanakonda                  KetaVaram 
##                       2120                       1045 
##             Ketganicheruvu                  Ketgudipi 
##                       1138                       1542 
##                 Kethapuram             Ketharajupalli 
##                       1536                        417 
##                 KETHAVARAM             Ketveerunipadu 
##                       1072                        830 
##                    KEVARLA              Khadar Pettah 
##                        774                        690 
##                  Khaggallu                   Khairevu 
##                        575                       3608 
##             KHAIRU PPAA LA                 Khajipalem 
##                       2342                       2814 
##                  Khajipeta                  KHAJIPETA 
##                        458                       1841 
##                 KHAJIPURAM              Khandaravalli 
##                        207                        639 
##                Khandavalli                Khandepalli 
##                       3191                       1594 
##                KHANDIVARAM                  KHANDRIGA 
##                       2732                       1056 
##                   Khandyam              Khaspanoupada 
##                        577                       1968 
##                     KIDIMI        Kilantri, G.B.Puram 
##                       1456                        283 
##                    Killada                     Killam 
##                        210                        634 
##                 Killankota               Killoyikolni 
##                       1038                        794 
##                Kiltampalem                      Kimmi 
##                       1110                        444 
##                    KIMMURU                KIMUDUPALLI 
##                        410                       1852 
##                KINCHUMANDA                   KINCHURU 
##                       1402                        600 
##           Kindam Agraharam                  Kindanagi 
##                        210                       1380 
##                  Kinjanagi                 KINNAMGUDA 
##                        558                        531 
##                 KinneraWad                   Kinnerla 
##                        862                       3049 
##                    KINTADA  KINTADASIVARUGOLLALAPALEM 
##                        656                        694 
##  KINTADASIVARUJOGANNAPALEM                    KINTALI 
##                        625                       3265 
##                     Kirapa                   Kirikera 
##                         61                       5025 
##                 Kirlampudi              KirshnaPatnam 
##                       3881                       3040 
##           KirshnaRoyapuram               Kishtampalle 
##                        542                       1531 
##                Kishtupuram                 Kistupuram 
##                        376                        474 
##                  KITALANGI                   Kitchada 
##                       1441                        496 
##           Kitchamambapuram                 Kittalpadu 
##                       1427                        903 
##               KITTANNAPETA                  Kittumula 
##                       1007                       1742 
##                     Kivaka                  klavapudi 
##                        535                       4702 
##             KO RUMANUPALLE           KoalBheemuniPadu 
##                        438                        496 
##                  KoalGatla                    Kobagam 
##                       1190                        356 
##                     Kobaka               KocharlaCoat 
##                        985                       1942 
##                      Kodam               Kodamanchili 
##                         59                       3341 
##           KodandaramaPuram            Kodapaganipalli 
##                        155                        775 
##              Kodatanapalli          KODAVALAVARIPALEM 
##                       1134                       1568 
##                 Kodavaluru              Kodavatikallu 
##                       2320                        509 
##                    Kodavli                Kodavtipudi 
##                       1863                       2492 
##                     Koderu              Kodigenahalli 
##                        584                       4154 
##                 Kodigudena              Kodigudlapadu 
##                       1185                        306 
##                  Kodihalli                Kodihazhzhi 
##                       1973                       2533 
##                  Kodikonda                     Kodimi 
##                       1846                       1388 
##            KODIPUNJIVALASA                     Kodisa 
##                        395                       1126 
##        Kodithipalle Mittta                   Kodivaka 
##                        435                        285 
##                Kodukoligam                  Kodumurti 
##                        856                        355 
##                   Kodumuru                      Kodur 
##                      15490                      44744 
##                    Kodur-1                   Kodur-11 
##                       1366                       1950 
##               Kodur(Arban)                     Koduru 
##                       1010                       1092 
##                 Kodurupadu                 KODURUPADU 
##                       2417                        322 
##               Kogana Palli                   KOGILERU 
##                       2386                        729 
##                     Kogili                     Kogira 
##                       1103                       3691 
##               Koiahgurpadu                      Koida 
##                        675                        639 
##                   Kojiriya                 Kojjepalli 
##                       1142                       2152 
##                    KOKATAM                Kokilampadu 
##                       1996                        714 
##                   Kokkanti             Kokkarayapalli 
##                       3459                        843 
##                Kokkarchedu                Kokkilgadda 
##                        499                       1744 
##               Kokkirapalli                 Kokkupalem 
##                       4473                        299 
##            Koknarayanpalem                Kolachnkota 
##                        753                       1152 
##                  KOLAGUNTA                  Kolakalur 
##                       1325                       7803 
##                  Kolalpudi                 Kolamadugu 
##                       2802                        440 
##           KOLAMASANA PALLI                   KOLAMURU 
##                       2773                       1067 
##                    Kolanka                    Kolanli 
##                       6798                        729 
##                 Kolanpalli                Kolanukonda 
##                       2260                       2033 
##               Kolanukuduru                  KOLATHURU 
##                        519                       1506 
##                  Kolavennu              Kolgana Halli 
##                       3016                       2606 
##                   Kolgutla                    Koligam 
##                       2251                       1374 
##                   Kolimeru               KOLIMIGUNDLA 
##                       1754                       3480 
##            Kollabava Puram                   KOLLADAM 
##                        375                        533 
##                 Kollaparru               Kollayavlasa 
##                       1585                        888 
##                Kolletikota            KolliBhimavaram 
##                       2993                        142 
##                 Kollikulla                 Kollimarla 
##                        368                        740 
##                  KolliPadu                  Kollipara 
##                        464                       5901 
##                  KOLLIPETA    KolliValasa,Gangamapata 
##                        314                        635 
##             KOLLIVARIGUDEM                 Kollivlasa 
##                        472                        171 
##                 Kollupalle                    Kolmuru 
##                        674                      15919 
##                   Kolukula               Kolumulpalle 
##                        918                       1183 
##              komaanapallli                 KOMADAVOLU 
##                       3158                       2728 
##                     Komali               Komallapaudi 
##                        801                       1307 
##                Komallapudi                Komanapalli 
##                        874                       1447 
##                Komannutala                   Komarada 
##                       2683                       3203 
##                   KOMARADA                 Komaragiri 
##                       1610                       6364 
##           KomaragiriPatnam                KOMARAGUNTA 
##                       6582                       1007 
##              Komarajulanka                KOMARAPURAM 
##                       4168                        293 
##                KOMARAVARAM                 Komaravolu 
##                       1114                       1411 
##                 KOMARAVOLU                   Komarika 
##                       1756                       1679 
##                Komaripalem                Komarlatada 
##                       4358                       2113 
##         Komarneniwaripalem                   Komarolu 
##                        931                       6986 
##                    Komarru                    KOMARRU 
##                        313                        972 
##                    Komarti                KomatiPalli 
##                        956                       2787 
##          KomDall Agraharam                 KomDeyPadu 
##                       3103                        415 
##                KomDyePalem                 Komerapudi 
##                        512                       2895 
##                     Komeri                     KOMIRA 
##                       1029                        672 
##                Komirepalli              KOMITTI GUNTA 
##                        189                        692 
##                  KomKepudi                  KomKuduru 
##                       1198                       4894 
##                   Kommaddi                    Kommadi 
##                        941                       3053 
##                Kommalapadu                  Kommaluru 
##                       2822                        393 
##               KommanaPalli           Kommanavaripalli 
##                        949                        722 
##                Kommaneturu                   Kommangi 
##                        749                       2424 
##                    Kommara                 Kommemarri 
##                       1373                        948 
##                      Kommi                    Kommika 
##                       1135                       1053 
##             KommineniPalli             Kommuchikakala 
##                        698                       2414 
##                 KOMMUGUDEM                Kommugudena 
##                        457                       2857 
##                KOMMULAVADA                 Kommunooru 
##                        500                        450 
##                     Kommur                    Kommuru 
##                        288                       1772 
##            Kommusiriapalli                KommuValasa 
##                        402                        262 
##                 Kompanagi.        Komtiguntarajupalem 
##                        852                        709 
##                 Komtikunta                Komtikuntla 
##                        369                       1254 
##                 Komtilanka                    Komturu 
##                        315                        119 
##                       Kona                       KONA 
##                       1220                       1846 
##               Kona Farestu            KONA RAJU PALLI 
##                       7694                       1338 
##                     Konada          Konaganiwaripalem 
##                       4327                        350 
##                 Konakanchi                Konaknmitta 
##                       1353                       1545 
##                 Konakondla                     Konala 
##                       6462                        787 
##                   KONALOVA                      KONAM 
##                        720                        594 
##                Konam Palli         KONAMASIVANI PALEM 
##                        541                        677 
##                    Konamki                    Konangi 
##                       2886                        218 
##                KonangiPadu                    Konanki 
##                        400                       3383 
##                  KONAPALLI                  Konapuram 
##                        793                        784 
##               Konasamudram           KONASIMHADRIPETA 
##                        820                        423 
##               Konatalpalle                Konathaneri 
##                        860                       1381 
##             Konatmatmakuru                 Konatnpadu 
##                        614                        263 
##              konavaripalli                Konayapalem 
##                        266                       2548 
##                     Koncha                   KONCHADA 
##                        273                       1576 
##          konda butchm peta           Konda Gangu Budi 
##                        538                        283 
##         Konda Lakshmipuram               Konda Laveru 
##                        739                         85 
##       Konda Lingala valasa               konda rejeru 
##                        953                        670 
##                Kondabaridi              Kondabimpuram 
##                        294                        425 
##            Kondaboyinpalli          KONDACHAKARAPALLI 
##                        224                        507 
##               Kondachilkam                  Kondadadi 
##                        982                        440 
##             Kondadevupalli              Kondagandredu 
##                       1039                       1844 
##            Kondagattupalle               Kondagokkiri 
##                       1281                        737 
##                 Kondagudem               Kondagumapam 
##                        295                       1693 
##                 Kondagunta               Kondagunturu 
##                        824                       3336 
##          KONDAIAHGARIPALLI                Kondajuturu 
##                        848                       1469 
##                 Kondakarla                Kondakavuru 
##                        796                       1257 
##               Kondakenguva                Kondakindam 
##                       2086                        255 
##                Kondakmarla              Kondakothapet 
##                       3370                        277 
##                 Kondakrkam                KONDAKUNKAM 
##                       1562                        152 
##            KONDALA CHERUVU       KONDALA MAMIDIVALASA 
##                       1230                        105 
##            Kondalakkivlasa            Kondalaraopalem 
##                        118                        645 
##                 Kondalogam         kondamanayanipalem 
##                        517                        527 
##             Kondamanjuluru             Kondamayapalle 
##                       3461                        531 
##           Kondamidakonduru         Kondamnayuni Palle 
##                        533                       1042 
##                KONDAMODALU  Kondampalli (Cherlopalli) 
##                       1711                        657 
##                  Kondamudi           Kondamudusupalem 
##                        790                        892 
##                Kondamulgam                  Kondamuru 
##                       1032                       1154 
##                   Kondangi                 Kondapalem 
##                       1836                        588 
##                 KONDAPALEM       Kondapalem Agraharam 
##                       1204                        669 
##     Kondapalem@Srirannagar                 Kondapalli 
##                       5567                      19048 
##                 Kondaparva                Kondapaturu 
##                       1167                       1152 
##              Kondapavuluru                   Kondapet 
##                       1494                       1717 
##                  Kondapeta                    Kondapi 
##                        482                       2556 
##              Kondapolvlasa                 Kondapuram 
##                        541                      11948 
##                Kondaragolu               Kondarajupet 
##                       1192                        282 
##            KONDAREDDYPALEM            KondareddyPalli 
##                        109                        334 
##            KONDAREDDYPALLI              KONDASAMUDRAM 
##                        653                        314 
##               Kondashambam             Kondasunkesula 
##                        376                       1384 
##                kondataduru            Kondatamrapalli 
##                        232                        443 
##          Kondavandla Palli              Kondavelagada 
##                       2025                       2221 
##                  Kondavidu                 Kondavlasa 
##                       3088                       1407 
##                  Kondavuru               Kondayapalem 
##                        863                       5409 
##               KONDAYAPALLI              KONDAYYAPALEM 
##                        343                        476 
##                KONDE PALLE                Kondemapata 
##                       1033                        680 
##                  Kondepudi                 Kondewaram 
##                        531                       2826 
##             KONDIKANDUKURU                 Kondiparru 
##                        647                        983 
##                 Kondraguda             KONDRAJU PALLI 
##                        200                        292 
##              Kondrajupalli                Kondramutla 
##                       1336                       3699 
##                Kondraprole                 KONDRUKOTA 
##                        218                        438 
##                Kondruprole                KONDU PALEM 
##                       2798                        893 
##                Kondukuduru                 Kondupalli 
##                       1080                        387 
##                     Kondur                    Konduru 
##                      14741                        506 
##               Konerukuppam        Koneshwarbatlapalli 
##                        880                        395 
##            Konetamma Palle         Konetinayanipalyam 
##                        759                       1594 
##                KonetiPuram                    KongaAm 
##                       1755                        509 
##               Kongalaveedu                 Kongalvidu 
##                        383                        733 
##               Konganapalle               Kongancharla 
##                        963                        294 
##                 Konganpadu                Kongapakalu 
##                       1623                       1192 
##           KONGAREDDY PALLI                   KONGATAM 
##                       6841                        804 
##             Kongavanipalem                    Kongodu 
##                        202                       1434 
##                   Konidedu                   konidela 
##                       1750                       3691 
##                   KONIDENA                  Konijarla 
##                       4808                       2641 
##                   Konijedu                     Koniki 
##                       1428                       2343 
##                     Konisa                KONITHIWADA 
##                        669                       5673 
##               Konkadiwarmu                   Konkallu 
##                        881                       1943 
##                Konkasinagi                    Konnali 
##                        441                        294 
##                Konnembattu                    Konooru 
##                        721                       2296 
##                   Konpalli                   Konpuram 
##                        718                        118 
##               Konrajupalli                   KONTALAM 
##                        706                       1656 
##                  Kontanagi              Konthanapalli 
##                       1106                        713 
##                   Kontheru                   KONTHILI 
##                       2469                        812 
##               Konuppalpadu            KONUSULAKOTTURU 
##                       1279                        792 
##         KOOPU CHANDRA PETA                    Kopalle 
##                        818                       2850 
##                    Koppaka                Koppalkonda 
##                       4881                        922 
##                   Koppalli                    Koppara 
##                        416                        768 
##                Kopparnlasa                   Kopparru 
##                        345                       4004 
##                  Kopparthi                 Koppawaram 
##                        966                       2780 
##                    KOPPEDU                KOPPERAPADU 
##                       1120                       2278 
##               KOPPERAPALEM                   Kopperla 
##                        960                        846 
##                    Koppolu                 Koppukonda 
##                       5153                       2853 
##                 Koppunooru                Koppuravuru 
##                       3998                       2531 
##                KOPU VALASA                     Korada 
##                         59                       1928 
##                     KORADA                    KORAGAM 
##                        922                        485 
##                     KORAMA              Koranjibhadra 
##                        457                       1082 
##                     KORAPA                  KoraPalli 
##                        302                       1153 
##                    Korapam                 Korasavada 
##                        706                       3000 
##                    Koratam                 Koratmaddi 
##                       1527                       1238 
##                  KORAVAMGI                      Kordi 
##                        931                       1270 
##                       KORI                  Korimerla 
##                        312                       1313 
##                  Koripalli                  Koriseela 
##                       1224                       1032 
##                 Korishpadu                Korivipalli 
##                       3232                        632 
##                 Korlagunta                  Korlakota 
##                        384                       2188 
##                 Korlakunta                     Korlam 
##                       4938                       5126 
##                Korlamadugu                 Korlamanda 
##                        473                       1254 
##                  Korlapadu                 Korlavlasa 
##                        254                        215 
##                    Kornagi                  Kornepadu 
##                       6751                       3614 
##                      Korni                  Kornipadu 
##                        412                        496 
##                  Kornutala         Korpu Krishnapuram 
##                        354                        196 
##            Korpukothavlasa                      KORRA 
##                        594                       1364 
##            Korraguntapalem                     KORRAI 
##                       1402                       1464 
##                  Korrakodu                  Korrapadu 
##                       1934                       7209 
##             Korrapatipalli                Korrapoluru 
##                        374                        799 
##                  Kortikota                  Korukollu 
##                        493                       5931 
##                  Korukonda                  KORUKONDA 
##                       5454                       2902 
##                 Korumamidi                  Korumilli 
##                       3606                       1055 
##                  KORUMILLI                  Korupalli 
##                       3807                        693 
##                  Koruprolu              Korutadiparru 
##                       2979                        547 
##                   Koruturu                   KORUVADA 
##                       1146                        851 
##    KORUVADA JAGANADHAPURAM                   Kosamala 
##                        667                       1396 
##                   Kosanagi               Kosangipuram 
##                         84                        260 
##                     Kosigi                   KOSIGUDA 
##                       9910                        452 
##                Kosinepalli                      Kosli 
##                        412                       1429 
##                      Kosta               Kosthuvalasa 
##                       1096                       1537 
##                     Kosuru              Kosuwaripalli 
##                       2810                       4734 
##                       Kota                       KOTA 
##                       6151                        635 
##               Kotabommaali                  Kotakonda 
##                       5048                       3375 
##                     Kotala                 Kotalparru 
##                       1853                       1321 
##                  KotamBedu                    Kotanka 
##                        691                       1330 
##                   Kotapadu                   KOTAPADU 
##                       4028                        863 
##                  KOTAPALLE                  Kotapalli 
##                        248                        987 
##                  Kotapolur       KOTARAMACHANDRAPURAM 
##                       2650                        804 
##                     Kotari                Kotarigommu 
##                       1001                        369 
##                Kotarubilli                  KOTARVEDU 
##                        482                        658 
##          Kotaseetarampuram                Kotatippala 
##                        920                        181 
##                  KOTAVOORU                  Kotcherla 
##                       1352                       5311 
##                 Kotcheruvu                  Kotekallu 
##                       2003                       3304 
##             Kotha Biravolu              Kotha Elalala 
##                        596                        749 
##            Kotha Erramtham         Kotha Gummadapuram 
##                       1050                        238 
##             KOTHA KANDRIGA          Kotha Kokkerancha 
##                        661                       1436 
##              KOTHA KOVVADA             Kotha Madugula 
##                        492                        354 
##           Kotha Mangapuram          KOTHA MucchuMarri 
##                        361                       2278 
##            Kotha Mulakuddu                Kotha palli 
##                       1220                       1284 
##                KOTHA PALLI                 KOTHA PETA 
##                       1260                       1288 
##          Kotha PothulaPadu            Kotha RaamPuram 
##                        532                        681 
##           KOTHA SHIVA GIRI             Kotha TutiPall 
##                        543                        827 
##           Kotha Vanmulpadu           Kotha YellaVaram 
##                        424                       1223 
##                Kothabaggam             KOTHABALLUGUDA 
##                        437                       1110 
##                Kothaburuju               Kothacheruvu 
##                       1216                       8491 
##                 Kothagudem               Kothagummada 
##                       2351                        297 
##            kothaguntapalli  Kothaindlu H/o Ekarlapall 
##                         96                        842 
##    Kothakaggallu.S.K.Puram             Kothakmlapuram 
##                       2763                        521 
##              Kothakolvlasa                  Kothakota 
##                        490                      19552 
##                  KOTHAKOTA                Kothakunkam 
##                       2387                        312 
##                 Kothalanka                  Kothaluru 
##                       6204                        656 
##                     Kotham                  Kothapadu 
##                       4663                       1375 
##                 Kothapalem                 KOTHAPALEM 
##                       2764                       2264 
##                 Kothapalle                 KOTHAPALLE 
##                       4823                       2181 
##                 Kothapalli                 KOTHAPALLI 
##                      33779                       1475 
##       Kothapalli Agraharam                Kothapalli, 
##                       1200                        674 
##          KOTHAPANALASAPADU                Kothapatnam 
##                        141                       1132 
##                 Kothapenta                 KOTHAPENTA 
##                        591                       1296 
##                  Kothapeta                  KOTHAPETA 
##                      15501                      16431 
##                  Kothapudi                  KOTHAREVU 
##                        419                       1469 
##               KothariPuram                Kothavalasa 
##                        467                      14674 
##                KOTHAVALASA              Kothavangallu 
##                       1129                       2172 
##              Kothavelagada            KOTHAVEPAKUPPAM 
##                        488                        902 
##                 Kothikonda                  KothPalli 
##                        457                        233 
##          KOTHULA GOKAVARAM                     Kothur 
##                       1307                       8520 
##                    Kothuru                    KOTHURU 
##                       4364                       1433 
##                       Koti               Kotikalapudi 
##                       1384                       2657 
##              KotiKesavaram                Kotikipenta 
##                       2095                        734 
##                  kotipalli                  Kotipalli 
##                        566                       3426 
##                  KOTIPALLI                    Kotipam 
##                       1497                        972 
##                     Kotipi                  Kotiralla 
##                       2383                        958 
##                 Kotitirdam                     Kotiya 
##                       1654                        852 
##               Kotkandukuru                 Kotlapalli 
##                       2549                       1949 
##                  Kotlpalli                    Kotluru 
##                        267                        535 
##                 Kotnabilli                 Kotnanduru 
##                        659                       4942 
##                 KOTNAPALLI                     Kotnur 
##                        925                       4427 
##                  KOTRAKONA              KOTRAMANGALAM 
##                       1764                        389 
##                  Kotsirlam                KOTT PA LEM 
##                       1293                        323 
##           Kotta .Agraharam           Kotta Bhemasingi 
##                        510                        498 
##         KOTTA LAKSHMIPURAM                   Kotta Mu 
##                       1180                       1457 
##            KOTTA PONNUTURU                    Kottada 
##                        453                       1534 
##                   Kottakki                    Kottala 
##                       4093                        773 
##                    KOTTALA            Kottala Cheruvu 
##                        592                        652 
##                   kottalam                  Kottaluru 
##                       1434                        919 
##            Kottamallampeta            KOTTAMARADIKOTA 
##                       1604                        292 
##                KOTTAMPALEM                 Kottapalli 
##                        715                        719 
##  KOTTAPATTISEEMA H/O.GUTAL                KOTTAVALASA 
##                        809                        414 
##            KOTTHA KANDRIGA   kottha palli /garampalli 
##                        894                       1414 
##        KOTTHAGIRIYAM PALLE                   Kottisha 
##                        467                        406 
##                 Kottiwaram                      Kottu 
##                        997                       1114 
##                 Kottupruvu                    KOTTURU 
##                        907                        732 
##                     KOTURU                 Koturupadu 
##                        426                        516 
##                 Kotvuratla                    KOTYADA 
##                       3844                       1701 
##                   KOVANURU                 Kovelamudi 
##                       1032                        466 
##                    Kovilam                Kovilampadu 
##                        360                        403 
##                      Kovur                Kovurupalli 
##                      17612                       4473 
##                    KOVVADA                Kovvadlanka 
##                       3734                       1157 
##                    Kovvali                    Kovvuru 
##                       3017                       7292 
##                    KOVVURU                KovvuruPadu 
##                      17619                       1095 
##                    Kovwada                    Kowluru 
##                       2559                        436 
##            KOYA ANKAMPALEM           KOYA RAJAHMUNDRY 
##                        792                        254 
##               Koyamadharam                Koyilkuntla 
##                        501                      13626 
##                 KOYYAKONDA               KOYYALAGUDEM 
##                        711                       5917 
##                     Koyyam                  KOYYAPETA 
##                       1298                        645 
##                  Koyyavpet                Koyyetipadu 
##                        547                        801 
##                    Koyyuru                   Krakutur 
##                       3368                        737 
##                      Krapa          KrapaChintalapudi 
##                       1481                       1748 
##                KRIDIMADUGU           KrishanRaiduPeta 
##                        639                       1219 
##        krishna jamma puram       KRISHNA MAHANTIPURAM 
##                        202                        440 
##              krishna puram              KRISHNA PURAM 
##                       1182                        577 
##         Krishnadasanapalli                Krishnagiri 
##                        787                       1282 
##               Krishnampadu              Krishnampalem 
##                        500                        614 
##              KRISHNAMPALEM              Krishnampalli 
##                        931                        528 
##           Krishnamrajupeta             KrishnamValasa 
##                        719                        452 
##               Krishnanagar               KRISHNAPALLI 
##                       1063                       1685 
##               Krishnapuram               KRISHNAPURAM 
##                      17577                       7148 
##           KRISHNARAO PALEM          Krishnarao Pettah 
##                        199                        956 
##           Krishnarayapuram           KRISHNARAYAPURAM 
##                         99                       1777 
##          Krishnareddipalli         Krishnashastrulpet 
##                        534                        108 
##               Krishnavaram             Krishnayapalem 
##                        460                        822 
##            Krishnayapalena             Krishnunipalem 
##                       1670                       1476 
##        Krishtamshettipalli                Krishtipadu 
##                       4403                       4508 
##                    Krosuru         KROTHAVENKATAPURAM 
##                       7051                       1011 
##                   Krovvidi                    KrPuram 
##                       1144                       1953 
##                Kruthivennu               Ku Mma Palli 
##                       4701                       1444 
##                Kubad Puram                 Kuchimpudi 
##                       6109                       1206 
##                Kuchinapudi                  Kuchipudi 
##                       1835                       5891 
##                   KuchiWad                     Kudapa 
##                        671                        991 
##                Kudaravalli              KUDDADAVALASA 
##                        330                        192 
##                   KUDDIGAM                   KUDDIRAM 
##                        477                        660 
##                  Kuddpalli                KUDDUVALASA 
##                        446                        351 
##                     Kuderu                     Kudiri 
##                       3631                       1468 
##                Kuditipalem                    Kudluru 
##                        734                       2816 
##                   Kudmluru                 KUDUMASARI 
##                        235                       1066 
##                   Kudupuru                     Kuduru 
##                       1004                        681 
##                  KUJABANGI                     Kujali 
##                        623                        689 
##               KUKATLAPALLI                KUKKAMBAKAM 
##                       1609                        430 
##        Kukkapalliwaripalem             Kukkarajupalli 
##                        335                       1948 
##    Kuklametta Lakshmipuram                   Kukunoor 
##                       3376                       1544 
##                      Kulla                  Kullupadu 
##                       2680                       1167 
##                    Kulluru                   Kulumala 
##                       2800                       2212 
##                     Kuluru   KUMARA PEDDAVENKATAPURAM 
##                       1225                        440 
##                KUMARADEVAM                    Kumaram 
##                       2231                       1074 
##               Kumarapriyam                Kumarapuram 
##                        497                       1797 
##                 Kumarkalva             KUMARUNI PALLI 
##                       1151                        422 
##             KUMBARLA PALLI                 Kumbhagiri 
##                       1073                        687 
##          Kumbidi Ichapuram                     Kumili 
##                        222                       4265 
##                  Kummamuru                  Kummanmal 
##                        866                       1634 
##             Kummarakonduru              KUMMARAMADUGU 
##                        234                        548 
##              KUMMARANATHAM               Kummarapalli 
##                       1311                        232 
##         Kummarapurugupalem               KummariGanta 
##                       3734                        933 
##               KummariGunta           Kummarnage Halli 
##                       1182                       1246 
##         Kummarvandla Palli                    Kummeta 
##                       3419                        274 
##                    Kummuru                     Kumram 
##                        675                       1054 
##                 Kumudvalli               Kumundanipet 
##                       3072                        154 
##          KUNAJAMMANNA PETA           KUNAMARAJUPALYAM 
##                        665                        428 
##                  Kunavaram                Kunayivlasa 
##                       6050                       1496 
##                  Kunchangi               Kunchanpalli 
##                       1968                       7030 
##                Kunchepalli            Kunda leshwaram 
##                       1312                       1341 
##                    KUNDADA                  Kundakuru 
##                        326                        644 
##                Kundalpalli                     Kundam 
##                       1335                        589 
##              KUNDANAGURTHI                Kundanakota 
##                       1005                        228 
##             Kundartiruwada                    Kunderu 
##                        757                       2003 
##                  Kunduluru                   Kundurpi 
##                        302                       5212 
##                    Kunduru                     kuneru 
##                       1863                        325 
##                Kunikinpadu                Kunkalgunta 
##                        238                       3064 
##                Kunkalmarru                 Kunkanooru 
##                       3033                        768 
##                  Kunkupadu              Kunprajuparva 
##                       1422                       2072 
##               Kuntalgudena               Kuntamukkala 
##                        292                        996 
##                  Kuntanhlu                    Kuntesu 
##                       1746                        555 
##                  KUNTHURLA               KUNTI BHADRA 
##                       1051                       1910 
##                  KuntiCoat                 Kuntimaddi 
##                        494                       3830 
##                Kuntinvlasa                  KUNTIPUDI 
##                       1552                        293 
##                 Kunukuntla                   Kunuturu 
##                       2263                       3661 
##                 Kuppagallu                     Kuppam 
##                       1594                      16191 
##               KUPPAM BADUR                 Kuppanpudi 
##                        880                       2237 
##             Kuppiganipalli             KUPPIGANIPALLI 
##                        539                        693 
##                    Kuppili                Kuppurupadu 
##                       1105                        476 
##               kurabalakota               Kurabalakota 
##                       5823                        994 
##                     Kurada              KURAKALAPALLI 
##                       4113                        888 
##               Kurakulpalli                  KURAPALLI 
##                       1395                        987 
##                  KURAPARTI                KURAVAPALLI 
##                        904                        881 
##  kuravapalli/gorantlapalli                   Kurgallu 
##                        984                       2407 
##                  Kurichedu             Kuricherlapadu 
##                       4118                       1312 
##                 Kuridinagi                    Kurigam 
##                        304                        989 
##                KURIM JALAM              KURIVI KUPPAM 
##                        386                        700 
##                 Kurjagunta                      Kurli 
##                        201                       2173 
##                   Kurluhal                KURMAIPALLE 
##                        146                       1551 
##            Kurmanadhapuram              Kurmanadpuram 
##                        451                        869 
##              Kurmannapalem                 KURMAPURAM 
##                       9884                       1188 
##               Kurmarajupet                    Kurnool 
##                       1852                     183450 
##                   Kurnoolu                   Kurnooru 
##                       1051                       1095 
##                  Kurnutala                Kurubrhalli 
##                       2127                        834 
##                     Kurudu                  Kurugonda 
##                       1734                       2351 
##                  Kurugunta                  KURUKALVA 
##                       2399                        938 
##                  Kurukunda                   Kurukuru 
##                       3585                        879 
##                  Kurukutti                Kurumaddali 
##                       1739                       2112 
##                   Kurumala                    Kurupam 
##                       1250                       9223 
##                 Kurusinagi                  Kuruvalli 
##                        170                       2125 
##                   Kuruwada                 Kusalpuram 
##                        933                       1382 
##                KUSARLAPUDI                     Kusimi 
##                       2336                        491 
##                 KUSULAWADA                   Kusumala 
##                        788                        724 
##                KusumaPuram                  KUSUMARAI 
##                        500                        633 
##              Kusumpolvlasa                   Kusumuru 
##                        687                       1275 
##                 Kutagundla               Kutchelapadu 
##                        472                       1006 
##                 Kutchupapa                   Kutgulla 
##                        415                       5526 
##             Kutheganipalli             KUTHUKUDUMILLI 
##                        707                        645 
##                     Kuthum                  KUTRAWADA 
##                       1243                        244 
##                    Kutturu                 Kutukuluru 
##                        775                       4973 
##                   Kuundram                  KUVAKULLI 
##                       2057                        722 
##                    Kuyyeru                 L.B.Charla 
##                       2926                       6531 
##                 L.B.PATNAM                 L.D.Pettah 
##                        487                        900 
##               L.Gannavaram                     L.KOTA 
##                       3387                       2949 
##        L.KOTA SEETARAMPUAM                   L.Kothur 
##                        356                       6194 
##             L.Lakshmipuram                   L.N.PETA 
##                        739                       1645 
##               L.Singavaram            la kka saga ram 
##                        413                       1349 
##                     Labara                      Labba 
##                        578                       1413 
##                  Labbanagi                  LABBARTHI 
##                       1016                       1468 
##                     Labham            LacchaiahPettah 
##                        749                       1652 
##   LacchaiahPettah, Kantlam          Lachami Polavaram 
##                        528                       2985 
##             LACHANNAVALASA             LachaRoyapuram 
##                        177                        220 
##          LachchireddyPalem                 Lachigudem 
##                       1585                        959 
##                 LACHIPALEM                  Laddagiri 
##                        558                       3290 
##                   LADDIGAM                   LAGARAYI 
##                       1030                       2113 
##                   Lagdpadu                Lagishpalli 
##                       2119                        894 
##                     LAIDAM                  Lakanapur 
##                       1031                       3224 
##             LAKHIDASUPURAM                    Lakidam 
##                        392                       1073 
##                      LAKKA                  Lakkaguda 
##                        712                        548 
##                Lakkamdiddi              LAKKANA PALLI 
##                        931                       2703 
##        Lakkaraju GarlaPadu               Lakkasmudram 
##                       1570                       1376 
##                 Lakkavaram                 LAKKAVARAM 
##                       7732                       4819 
##         Lakkavarapu Pettah            LAKKAVARAPUKOTA 
##                        740                        689 
##            LAKKAVARI PALLI            LakkireddyPalli 
##                        634                       7125 
##                 Lakkivlasa         LakkmiMiDeviPettah 
##                       1075                       1244 
##             LakkmiMiPettah              LakkmiMiPuram 
##                        194                       1821 
##                   LAKKONDA                 Lakkupuram 
##                        620                       1156 
##               LAKSHIMIPETA         Lakshmakkakandriga 
##                       1659                        372 
##            Lakshmakkapalli           LAKSHMAMBA PURAM 
##                        361                        906 
##              Lakshmampalli            LAKSHMANESWARAM 
##                       2393                       9505 
##               Lakshmapuram       Lakshmi Balaji Nagar 
##                        641                        674 
##              LAKSHMI NAGAR   lakshmi reddy gari palli 
##                       1717                        715 
##               Lakshminagar     LAKSHMINARASIMHA PURAM 
##                       2028                        226 
##   LAKSHMINARAYANADEVI PETA               lakshmipuram 
##                       1402                       1603 
##               Lakshmipuram               LakshmiPuram 
##                      11299                       7246 
##            LAKSHMIRAJUPETA                 LakshmiWad 
##                        268                        797 
##        Lakshmiwarayanpuram             LAKSHMUDU PETA 
##                       1128                        596 
##                Lalam Kodur                   Lalapeta 
##                       2059                        311 
##                        Lam               Lammashinagi 
##                       3526                       1753 
##                Lampakalova             Lanalla Guntla 
##                       1935                        725 
##               LanallaGatla              LanallaGuntla 
##                       1598                        951 
##                LanallaMada                LanallaMadu 
##                       4151                       2257 
##         LanallaMekalaPalle      LanallaThimmayyaPalli 
##                        963                        941 
##                  Lanjakota                    LankaAm 
##                        826                        388 
##         LankalaKalavaGunta              Lankalakoderu 
##                        668                       3781 
##               LANKALAPALLI          LankalaPalliPalem 
##                        419                        757 
##                     LANKAM    LANKAPAKALA H/O.ALIVERU 
##                        830                        349 
##       Lankapalle Agraharam           Lankapalle Lanka 
##                        584                        643 
##                 Lankapalli                  LANKAPETA 
##                        951                        303 
##             LANKAVANIPALEM             Lankelakurpadu 
##                        453                        983 
##               Lankelapalem              Lankojanpalli 
##                       3769                        390 
##                 Latchampet          Latchannagudipudi 
##                       1140                        685 
##                Latchapalem             LATCHIRAJUPETA 
##                        225                        243 
##                 Lathawaram                   Lattigam 
##                       1501                        160 
##                    Lavanur                     Laveru 
##                        783                       1979 
##                   Lavidamu                 LAXMIPURAM 
##                        805                       2289 
##                  LAYAGANDA                     Lebaka 
##                        982                       3645 
##                   Leburu-i                Leguntapadu 
##                        895                       1760 
##         lekalavandla puram                 Lellapalli 
##                        356                        386 
##                 Lellgaruvu                LemallePadu 
##                        364                        643 
##                   Lepakshi                  Letapalli 
##                       5217                        658 
##                     Levidi                Likhitapudi 
##                        466                       1332 
##                   Lindugam                Lingadhalli 
##                        564                        465 
##                 LingaGudem                Lingagudena 
##                        540                        500 
##                    Lingala                    LINGALA 
##                       5037                        431 
##   Lingala Shiwaru Sobabala               LingalaDinne 
##                        568                        501 
##                Lingalapadu                LINGALAPADU 
##                        728                        906 
##              LingalaValasa              LINGALAVALASA 
##                       3095                        212 
##                Lingaldinne            Lingamannahalli 
##                        521                        369 
##                 lingambodu                LingamGunta 
##                        291                       2198 
##               LingamGuntla               LINGAMGUNTLA 
##                       6348                        248 
##                Lingampalle                LingamParti 
##                        506                       5683 
##                 LINGAMPETA                Lingandinne 
##                        622                        764 
##               LINGANNAPETA                Linganpalem 
##                        404                        684 
##                 Lingapalem                Lingapalena 
##                        341                        775 
##                   Lingapur                 Lingapuram 
##                        901                       6128 
##                 LINGAPURAM                 LINGAPUTTU 
##                        531                        200 
##             LingaRajupalem           LINGAREDDY PALLE 
##                       1084                       1628 
##            LingareddyPalem            Lingareddypalli 
##                       3033                        997 
##            LINGAREDDYPALLI              Lingasamudram 
##                        188                       3956 
##                    LINGATI                 Lingavaram 
##                        597                       1214 
##                 LINGAVARAM               Lingayapalem 
##                        768                       1038 
##                     Liviri            Lobhanadripuram 
##                        788                        724 
##          LODAGALAVANIPALEM                 Loddabadra 
##                        647                        433 
##               LODDALA PETA          Loddalkakitapalli 
##                        559                        782 
##                 LODDAPUTTI                 Loddipalle 
##                       3919                       2130 
##                    LODODDI               LODODDIPALEM 
##                        537                        127 
##                  LoeCherla              LoeHari Banda 
##                       1821                       1706 
##             LoeKothavalasa                     LOGILI 
##                        135                        464 
##                     LOGISA                  Lohrijola 
##                        482                        189 
##                    LOKANDA                Lokojipalli 
##                        100                        977 
##                   Lokumudi                      Lolla 
##                        948                       2825 
##                      LOLLA                     LOLUGU 
##                        707                       3033 
##                     Loluru                     Lomada 
##                       1107                       1213 
##                Lopatnutala                     Lopudi 
##                        638                        710 
##           LOSARI GUTLAPADU                    LOTHERU 
##                      15969                       1974 
##                 lothugedda                 Lothugedda 
##                        963                       4691 
##                 LOTLAPALLI                    LOTTURU 
##                        456                        851 
##                     Luklam                    Lumbesu 
##                        830                        395 
##                    Lumburu                LUNGAPARTHI 
##                        965                       1456 
##                  Lutukurru             M KAMBALADENNE 
##                       1950                        370 
##               M Pendekallu         M. BANDAMEEDAPALLI 
##                        893                       2260 
##              M. Bennawaram             M. KOTHAVALASA 
##                        487                        458 
##               M. Rajapuram            M. Sitarampuram 
##                        252                        718 
##       M.A. RAJULA KANDRIGA                 M.ALAMANDA 
##                        897                       1841 
##                 M.ATTAGUDA                 M.DANDIGAM 
##                        310                        956 
##                 M.Ganpuram                 M.J.Valasa 
##                        652                        996 
##                 M.K.PATNAM             M.K.VALLAPURAM 
##                       1209                        330 
##             M.Kambaladinne                   M.KODURU 
##                        129                       1886 
##                 M.KOTAPADU               M.KOTHAPALLI 
##                        719                       1143 
##                M.KOTHAPETA              M.Kothavalasa 
##                        248                        225 
##                   M.KOTHUR             M.Kotta Valasa 
##                        979                       1507 
##                  M.Kottala                    M.KOTUR 
##                        522                       2253 
##             M.KRISHNAPURAM            M.LingalaValasa 
##                        340                        569 
##               M.Lingapuram                 M.M.VELASO 
##                       1101                        792 
##                  M.N.Palli              M.Nagulapalle 
##                       2534                       2678 
##               M.Nidamanuru                M.P.Cheruvu 
##                       1406                       1604 
##              M.R.Agraharam               M.R.CH.PURAM 
##                        266                        658 
##                  M.R.PALLI               M.Sariapalli 
##                      18008                       1092 
##                  M.V.Palli             M.venkata giri 
##                       1372                       3628 
##             M.Venkatapuram               Maadakapalem 
##                        876                        442 
##                MaakanPalem                  Maakwaram 
##                        791                        859 
##            MABBUVALLA PETA               Machanapalli 
##                        759                       2634 
##                  Machanuru                 Machapuram 
##                        878                       1490 
##                    MACHARA                   Macharla 
##                       1436                      38732 
##                 Machavaram                 MACHAVARAM 
##                      19382                       3680 
##               Machayapalem        Machilipatnam Rural 
##                       2308                       1363 
##        Machilipatnam Urban             machinenipalli 
##                      77195                        418 
##            MACHIREDDIPALLI                  Machnooru 
##                        320                        356 
##              Machumandoddi                 Machupalli 
##                        697                       1537 
##                   MADAGADA                     Madaka 
##                       1103                        741 
##          Madakalavaripalle                MADAKAPALEM 
##                      19096                        691 
##                     Madala                     MADALA 
##                       4103                        719 
##            MadalavariPalem                 Madamanuru 
##                        927                       2335 
##         MADANA GOPALAPURAM          MadanaGopalapuram 
##                        282                       1907 
##               MADANAM JERI                MADANAMBEDU 
##                        421                       2009 
##            MADANANTHAPURAM                Madanapuram 
##                        441                        398 
##                MADANAPURAM          MadannaGari Palle 
##                        952                        949 
##                    Madanur                  Madavaram 
##                       4354                        441 
##        MADDAIAH GARI PALLE             Maddalacheruvu 
##                        943                       3099 
##                      MADDI                 Maddigruvu 
##                       1386                        988 
##            Maddikera - Ist        Maddikera Agraharam 
##                       8776                       3413 
##                  MADDILEDU           Maddilingadhalli 
##                        445                        500 
##                 Maddimdugu           MADDINAYANIPALLE 
##                        629                       1810 
##                 Maddinlasa                  Maddipadu 
##                        290                       5054 
##                 Maddipatla                  Maddirala 
##                        307                        872 
##               Maddiralpadu            MADDIRATHIGUDEM 
##                       1393                        949 
##                Maddirevula             Maddiwarigondi 
##                       1680                        380 
##               MADDULAGUDEM                Maddulparva 
##                        805                       1869 
##                  Madduluru                    Madduru 
##                       2048                       7664 
##               Maddurulanka                Maddurupadu 
##                        513                       2188 
##                 Madduvlasa               Madena Halli 
##                        183                        840 
##                  MaDepalle               MadhabPatnam 
##                       4691                       4343 
##            Madhanantapuram               Madhanapuram 
##                        844                        897 
##                Madhavamala               Madhavapuram 
##                        813                       1240 
##                 Madhavaram                 MADHAVARAM 
##                       7512                       1891 
##           Madhavaram Tanda           Madhavaram Turpu 
##                        806                        873 
##         MadhavaramPashchim            Madhavayapazhem 
##                        346                        550 
##  Madhavrangarayapuram Agra          Madhi reddi palle 
##                        833                       1478 
##                    Madhudi                  Madhupada 
##                       1992                       1374 
##                Madhuravada                 Madhurpudi 
##                      30246                       1062 
##       MADHYAHNAPUVARIGUDEM                 Madicharla 
##                        515                       2621 
##                 MADICHERLA                 Madigpuram 
##                        387                        252 
##                  Madigubba                     Madiki 
##                        538                       3851 
##                  Madimallu                 Madinapadu 
##                        544                       1159 
##         Madipadu Agraharam                MADIREPALLI 
##                        778                        558 
##                   Maditadu                  Madkshira 
##                       4560                      12960 
##                   Madlnagi                     Madpam 
##                        650                       1604 
##               Madugu Palli                   Madugula 
##                       1162                       2315 
##            MADUGUPOLAVARAM                   MADUMURU 
##                       1506                       1018 
##                  MaduPalli                    Madupam 
##                       1049                        482 
##                     MADURU                   Maduturu 
##                       3410                       1704 
##                      Madya                      Magam 
##                        413                       1875 
##              MAGANDLAPALLE                MAGATAPALLI 
##                       1493                       2482 
##             Maggalmalpalli               MAGGAMVEEDHI 
##                        734                        638 
##                    Magguru                    Magollu 
##                        389                       1969 
##                    MAGUNTA                   Maguturu 
##                       1077                       1099 
##           MAHADEVAMANGALAM              MahadevaPalli 
##                       1059                       1795 
##             Mahadevapatnam              MahadevaPuram 
##                       4046                       1241 
##              MAHADEVAPURAM              Mahadevipuram 
##                       2023                        253 
##              MahadeviPuram              MahadevuPuram 
##                        471                        615 
##                      MAHAL            mahal raj palli 
##                       3700                        532 
##           MahalakshmiPuram     Mahamkali Devi Putturu 
##                        551                       1424 
##                  Mahanandi             Mahanandipalli 
##                       2032                        652 
##              MahanthiPalem              MAHARAJAPURAM 
##                        385                        525 
##               Mahartapuram               Mahasamudram 
##                        404                       1029 
##                 Mahasinagi               MahenderaWad 
##                        577                       2488 
##            MaheshwaraPuram                  Mahimluru 
##                        278                       3376 
##                Maidugozham                   Maidvolu 
##                        922                       1498 
##             Mailaram Palli              Mailasamudram 
##                        780                        410 
##                      Maipa             Maisannagudena 
##                        636                       1806 
##                     Majeru             Majigopalpuram 
##                       1686                        124 
##                  Majjipeta                Majjivalasa 
##                       1160                       1025 
##                  Majragada               Makannapalli 
##                       1432                       1295 
##               Makannapuram                  Makivlasa 
##                        795                       2771 
##                   Makkapet           Makkinwarigudena 
##                       1804                       2178 
##                    Makkuva                Makrampuram 
##                       3417                        794 
##                   Makrjola                 Maktapuram 
##                        444                        813 
##                  MAKUVARAM                Makwarpalem 
##                        564                       4612 
##                    MALAKAM                MALAKAPALLI 
##                       1166                       1801 
##       Malakondarayunipalem            Malalamakavaram 
##                        290                       2513 
##                  MalaPuram              MALASANIKUNTA 
##                        614                        327 
##           Malavani kotturu                Malde palli 
##                        324                        497 
##               Malemarpuram                   Malepadu 
##                       3325                       2152 
##              Malgadempalem                     Malgam 
##                        552                       1103 
##                    Malguru                 MALICHARLA 
##                       2943                        772 
##                  Malichedu                  Malignoor 
##                        337                        327 
##                MALIKIPURAM            Malireddy Palli 
##                       7787                       1018 
##             MALISINGAVARAM                   Maljampa 
##                        414                        727 
##                 Malkapuram                 MALKAPURAM 
##                      52544                       1256 
##                  Malkpalem                 Malkvemula 
##                        610                       1543 
##                Malla kunta                    Malladi 
##                        661                       1458 
##                 MallaEmula                Mallagundla 
##                        786                        724 
##                MallaKaluva                     Mallam 
##                       1882                       5962 
##          Mallam Bhutipalem               MALLAM GUNTA 
##                        428                       2720 
##               MallamPettah                Mallanhatti 
##                       2008                        459 
##                  Mallanuru                 MallaPalli 
##                        537                       1182 
##           MALLAPURAAJAPETA                 Mallapuram 
##                        521                       3261 
##                 Mallavalli                 Mallavaram 
##                       3078                        155 
##                 MallaVaram                 MALLAVARAM 
##                      12513                       3695 
##         MALLAVARAM MAMILLU            MALLAVARI PALEM 
##                        327                        645 
##                  Mallavolu             Mallawarappadu 
##                       5802                        698 
##              Mallayagudena               MALLAYAPALEM 
##                        294                       2505 
##                Mallaypalem                    Mallela 
##                       1456                       1030 
##                    MALLELA               Mallem palli 
##                       3079                       1552 
##                Mallempalli              Mallena Palli 
##                        765                        573 
##                 Mallepalli                 Mallepally 
##                       1736                       8298 
##               Malleshwaram                Malleswaram 
##                       1179                       2632 
##                  Malletota                      MALLI 
##                       1467                        156 
##            Malliboinapalle           Mallikarjunhalli 
##                         72                        545 
##         Mallikharjunapuram                  Mallipudi 
##                        237                       1675 
##           Mallipudi Aliasu                  MalliSala 
##                       2239                       2256 
##                  Mallividu        Mallubhupala Patnam 
##                       1553                        851 
##            MALLUNAIDUPALEM                    Malluru 
##                       2411                       2877 
##              Malmida Palli                   Malpalli 
##                       1648                       1375 
##               Malpana Gudi                     MALUVA 
##                        594                        735 
##                    Malyada                    Malyala 
##                        757                       1791 
##                     Malyam                Malyavantam 
##                       2098                       2907 
##           Malyavantunipadu                  Malynooru 
##                        534                       3807 
##                   MAMADUGU                  MAMAMDURU 
##                        890                        821 
##                    MAMBEDU                   Mamidada 
##                       1701                       1191 
##              Mamidala Padu                MAMIDIGONDI 
##                      15805                        276 
##                 Mamidijola                Mamidikolla 
##                        129                        382 
##               MamidiKuduru                MamidiMettu 
##                       2742                        511 
##                MamidiPalem                Mamidipalle 
##                        987                       2635 
##                MAMIDIPALLI                 Mamidipudi 
##                       1310                        747 
##               MamidiValasa                  MamidiWad 
##                        871                        701 
##               MamillaKunta               Mamillapalle 
##                        491                        509 
##               Mamillapalli               MAMILLAPALLI 
##                       6965                        795 
##                      Mampa                   Mamuduru 
##                       1871                       5544 
##               Manakyapuram                  Manapuram 
##                       1375                        152 
##                   Manchala                   MANCHALA 
##                        900                        514 
##               Manchalkatta                Manchikallu 
##                       2419                       1828 
##               Manchiklpadu                   Manchili 
##                       1031                       3068 
##           MANCHINEELLAPETA                 MANCHUGUDA 
##                       1863                        919 
##                   MANCHURU                      MANDA 
##                       1008                        328 
##         Manda @ Diguvmanda                   Mandadam 
##                        670                       3966 
##                    Mandadi                    MANDADI 
##                       2183                        284 
##                  Mandagiri                Mandalpalli 
##                        789                       7316 
##                Mandalparru                  Mandaluru 
##                       1265                       1298 
##                  MandaPadu                  MANDAPADU 
##                       1460                        896 
##                  Mandapaka                Mandapakala 
##                       5940                       2791 
##                 MandaPalle                 Mandapalli 
##                       1364                       2926 
##                 MANDAPALLI                   Mandapam 
##                       2579                       1443 
##                  MANDAPETA                  Mandarada 
##                      31474                        402 
##                    Mandasa                 Mandavalli 
##                       6004                       2892 
##               Mandavkuriti                  Mandavuru 
##                        994                        254 
##         MANDI KRISHNAPURAM                  Mandigiri 
##                        505                       5572 
##                   Mandlena                     Mandli 
##                       3013                       1501 
##                    Manduru                  Manekurti 
##                       1314                       1167 
##                  Manendram                  Manepalli 
##                       1065                       7941 
##               Manerampalli                Manesmudram 
##                        349                        885 
##             ManeyGuntaPadu                    MANGADU 
##                        283                       1806 
##            Mangaladripuram                Mangalagiri 
##                        398                      51029 
##            MangalagiriPadu              Mangalakuntla 
##                       1004                        696 
##                   mangalam                   MANGALAM 
##                      14048                       2957 
##              MANGALAM PETA               MangalamPadu 
##                       2029                       1495 
##               MangalaPalem               Mangalapuram 
##                       2592                        456 
##               MangalaPuram                Mangalmdaka 
##                       2721                       2095 
##                 Mangalpuru                Mangamapata 
##                        381                        941 
##                 MANGAMPADU                  Mangampet 
##                       1184                       2081 
##                  Mangamuru               Manganelluru 
##                       2155                       1375 
##          MANGAPATIDEVIPETA              MANGASAMUDRAM 
##                        891                       2184 
##                 Mangavaram                Manginapudi 
##                       2616                       1111 
##                 Manginpadu                 Mangiturti 
##                        891                       1589 
##                   Mangollu                  MangPalle 
##                       2087                        488 
##                 MangPatnam           Mangulayi Pettah 
##                        715                        429 
##                 Mangupalli                     Maniga 
##                       2242                         85 
##                    MANIGAM               Manikeswaram 
##                        450                       1757 
##                  Manikonda         MANIKYARYANA PALLE 
##                       3867                        550 
##              Manimeshwaram                   Manirevu 
##                        571                       2514 
##                    Manjeru               Mankal doddi 
##                       2261                        759 
##                   Mankollu                    Manmala 
##                        238                        954 
##              Mannangidinne              Mannarupoluru 
##                       1182                       3412 
##              Mannasamudram                    Mannava 
##                       2181                       1117 
##                 MANNAVARAM                   Manneela 
##                        488                       1389 
##                 Mannegunta                  Mannemala 
##                        726                        521 
##               Mannemutheri                 Mannepalli 
##                       1558                       2660 
##          Mannesultan Palem                Mannetikota 
##                       1234                        965 
##                     Mannur          Mannyapu Chintuva 
##                       8116                        462 
##                    Mantada              MantapamPalli 
##                       2531                       1303 
##                    Mantena                    Mantina 
##                       1651                        691 
##               MANTRALA YAM                   Mantriki 
##                       5705                       1181 
##                Mantripalem                    MANTURU 
##                       1318                        988 
##                   Manubolu               ManuboluPadu 
##                       5535                       1271 
##                  Manudoddi                 Manugunuru 
##                        315                        454 
##          Manukondwaripalem                Manumakonda 
##                       1361                        330 
##                     Manuru              Manuyapuratla 
##                        742                       1423 
##                   Manvaali           Manyanwari Palem 
##                        672                       1350 
##            Manyanwaripalli                   Mar Tadu 
##                       1044                       4129 
##           MARADA Rajapuram                 MARADAWADA 
##                        331                        321 
##             MARAKALAKUPPAM             Marakuntapalli 
##                        492                       1235 
##                     Marala                    maralla 
##                       2288                       1236 
##            Maranreddipalle                Maratipalli 
##                        610                        208 
##                     Mardam                 Maredipudi 
##                       1062                       3286 
##               MAREDU PALLI                  MareduBak 
##                        457                        580 
##                 MAREDUBAKA                 Maredumaka 
##                       2481                        607 
##                MAREDUMILLI                 Maredupaka 
##                       1727                        534 
##                    marella                    Marella 
##                       1391                       2342 
##               Marellamdaka                Marellamudi 
##                        968                        586 
##                MaRellaPadu                  MAREPALLE 
##                        557                        196 
##                  MarePalli                  MAREPALLI 
##                        487                        771 
##                  Maripalli                Maripivlasa 
##                       1059                        912 
##                   Marivada                 MARKAPURAM 
##                       1165                      33363 
##                   Markattu               Markondapadu 
##                        855                       2679 
##              Markondaputti                 MARLAGUDEM 
##                       1200                        223 
##                 Marlagunta                 Marlamdiki 
##                        396                        570 
##      Marlamudi Jangalpalli                  Marlapadu 
##                       1081                       1502 
##                 Marlapalli                  Marlapudi 
##                       1728                        737 
##                    Marlava                      Marli 
##                       1759                        652 
##                 Marpguntla               Marribandham 
##                        226                       1020 
##                 MarriEmula                  MARRIGUDA 
##                        793                        526 
##                Marrigudena                 MarriGunta 
##                        444                        630 
##            MarriKommaDinne           MarriKothavalasa 
##                       1548                        386 
##                 MarriKunta            MARRIKUNTAPALLI 
##                        881                        519 
##           MARRIMAKULAPALLE           MARRIMAKULAPALLI 
##                        880                        355 
##            Marrimakulpalli                  Marripadu 
##                        575                       3081 
##                  MARRIPADU                 Marripadu, 
##                       1490                        335 
##                MARRIPADU.C                MARRIPADU.K 
##                        433                        169 
##                   MarriPak                 Marripalem 
##                        915                       2276 
##                 MARRIPALEM                 Marripalle 
##                        941                        434 
##                 MARRIPALLE                  Marripudi 
##                        672                       3832 
##                  MARRIVADA                MarriValasa 
##                        527                       1659 
##                MARRIVALASA                  Marrividu 
##                        742                       1964 
##                  Marriwada                    Martadu 
##                        538                       1020 
##                    Marteru                   Marupaka 
##                       3653                       1938 
##                  Marupalli                  MaruPenta 
##                        667                        760 
##         Maruproluwaripalem                   Marupuru 
##                       4268                       1303 
##         Marutla Colony -ii                   Maruturu 
##                       1629                      15155 
##                    MaruWad                   Maruwada 
##                        729                       1679 
##                    Marvada              MaSahebPettah 
##                        598                       1373 
##                    Masapet              Maseedhupuram 
##                       7243                       1268 
##               Maseedupuram                Masenapurti 
##                       1166                        295 
##                  Maskpalli                  Maskpuram 
##                       2102                        518 
##                     Matala                  MATAVALAM 
##                        952                        408 
##                     MATHAM          Matham Bhimavaram 
##                        499                        676 
##               Mathangudena                    Mathyam 
##                        957                       2185 
##                  Matkamudi              Matlab Pettah 
##                        791                        819 
##                     Matlam                  MATLAPADU 
##                       1174                        502 
##                      Matli             Matlivaripalle 
##                       4210                       2662 
##             Matsavanipalem               MATSHYAPURAM 
##                        747                        858 
##                 MATSYAPURI            MATSYAPURIPALEM 
##                       3385                        596 
##                 Mattagunta                     Mattam 
##                       1171                        873 
##                     MATTAM               mattam palli 
##                       1198                        295 
##                 Mattaparru              Mattarlapalle 
##                       2770                        392 
##             Mattavanipalem                 MattiGunta 
##                        815                        478 
##                  MattiPadu                  MATTUJORU 
##                       1649                       1028 
##                Matukumilli                  Matumdugu 
##                        619                        304 
##                   Matumuru                MAVILLAPADU 
##                       1140                        727 
##                    Mavturu                     MAVUDI 
##                       1659                        590 
##                   Mayaluru     Medanulu Nengammapalli 
##                        401                        209 
##                   MedaPadu                 MEDAPARTHI 
##                       1301                       2319 
##                  Medapuram                    Medehal 
##                       5491                        479 
##                  Medepalli                 MEDICHERLA 
##                        562                       1070 
##                Medikonduru                  MEDIKURTI 
##                       5140                        806 
##           Medimakula Palli             Medinaraopalem 
##                        525                        786 
##        Medishettiwaripalem                   Mediwada 
##                        214                       4372 
##                   Medmarti                      Medpi 
##                        111                       1814 
##                  Medukurti                     Meduru 
##                       1192                       2879 
##  Meduru Shiwaru Satyalpadu                Meedipentla 
##                        652                       1743 
##                 MEELAPATTU                 Meenahalli 
##                        750                        538 
##                 MEERAPURAM               MeerjaPettah 
##                       1213                       1068 
##                MEERJAPURAM          MEESALA DOLA PETA 
##                        593                        175 
##              MeesalaPettah                  MeghVaram 
##                        937                       1845 
##     MEKALA NAGIREDDY PALLI              MekalaCheruvu 
##                        294                       1157 
##            Mekalavaripalli                    Mekdona 
##                        749                       1024 
##        Mekhasa DuggiValasa                   Meknooru 
##                       1166                        716 
##                  MELACHURU                   Melavayi 
##                        572                       6214 
##                   Melchuru              Meliakanchuru 
##                        397                        569 
##                 Meliaputti               MELLACHERUVU 
##                       2553                        874 
##           Mellamarti Lanka                  Mellavagu 
##                        210                       2389 
##                    Melluru                 MELUMDODDI 
##                       1251                       1239 
##                    MELUMOI                   Melupaka 
##                       1518                        768 
##   Melupaka Jagannadhapuram                MenaValluru 
##                       1491                       1676 
##                   mendangi                    Menkuru 
##                        302                       2905 
##                    Mentada                  MENTEPUDI 
##                       2853                        501 
##           Meraka Chamwaram              Merakamudidam 
##                        685                       2501 
##                Meraknpalli                  Merikpudi 
##                        554                       2363 
##                  Merlapaka                 Merlapalem 
##                        872                       2742 
##                  MERNIPADU                   Metchiri 
##                        584                       1146 
##                 Metlapalli                 Mettapalem 
##                        405                        978 
##                 Mettapalli                MettaValasa 
##                       1464                       2551 
##                      Mettu                 MettuPalli 
##                        956                       1673 
##                    METTURU                MIDDE PALLI 
##                       4205                        432 
##                Midde Tanda             MIDDI KANDRIGA 
##                        760                        241 
##                 Midivemula                    Midturu 
##                        732                       4803 
##                    Midutur                   Miduturu 
##                       1113                        886 
##                     Mijuru             Mikkinenipalle 
##                        353                        497 
##                Millampalli                      Mindi 
##                       1247                      10288 
##                MINDIVALASA                   Mingallu 
##                       1109                       2779 
##           Miniminchilipadu                 Minumuluru 
##                        441                       1160 
##                 Miriapalli                   Miriyala 
##                        374                       2121 
##               Miriyampalli                  Mirtipadu 
##                        566                       2065 
##                 Mirtivlasa                 Mirzapuram 
##                       1655                       1329 
##             MITTA KANDRIGA       MITTA MEEDA KANDRIGA 
##                        599                        874 
##            Mitta Somapuram      MITTACHINTHAVARIPALLI 
##                        866                       2001 
##                 Mittagudem              MittaGudipadu 
##                        271                        735 
##               Mittaknadala             Mittamanipalli 
##                       2026                       2133 
##              Mittamidpalli                 Mittapalem 
##                       2435                       1617 
##                 MittaPalle                 MITTAPALLE 
##                        972                        372 
##                 Mittapalli                 MITTAPALLI 
##                        855                        485 
##  Mittapalli H/o Ramakuppam                MITTAPALYAM 
##                        191                       1122 
##               Mittatmakuru                    Mittoor 
##                       1418                       3914 
##               MMC KANDRIGA                    Mobagam 
##                        837                       2553 
##                   Mocharla                       Moda 
##                       1092                       6456 
##               MODALAVALASA               Modamidpalli 
##                        865                       2319 
##                  ModeGunta                  MODEKURRU 
##                        791                       4690 
##                  Modepalli                 MODHAPALLI 
##                      10312                        627 
##              MODILIKOTTURU           MODIVANGANAPALLE 
##                        305                       1031 
##              MODUGULAPALEM               Modugulpalem 
##                        568                        918 
##                 Modugulpet               Modugulputti 
##                        313                        230 
##                Moduguvlasa                   Modukuru 
##                        783                       4342 
##                   Modumudi                   Modvlasa 
##                       2519                       1794 
##              Mofasubandaru               Mogalikuduru 
##                        490                       2577 
##                MOGALIPURAM                Mogallamuru 
##                       2614                       1624 
##                    Mogallu                  Mogalluru 
##                       4372                       2058 
##                  Mogalturu              MOGARALAPALLI 
##                      11945                       1344 
##                     Mogili               MogiliCherla 
##                       1270                        792 
##                 MogiliPadu           Moglayi Uppaluru 
##                       1554                        131 
##                   Moguluru              Mohamed Puram 
##                       2018                        450 
##              Mohamedapuram               Mohammadabad 
##                        213                       1394 
##                MOHANAPURAM                MOILLAKALVA 
##                        650                       1165 
##                 Mokalingam              Mokasalluwada 
##                       2248                        497 
##           Mokasmamidipalli            Mokhalingapuram 
##                       2310                        460 
##             Mokhasaklvpudi                 Mokkalpudi 
##                        204                        270 
##        Moksa Narsannapalem                Mokshgundam 
##                        397                       1215 
##                 MOLAGAMUDI                 Molagnooru 
##                       1106                        299 
##            MolakalaPoondla                 Molaklpudi 
##                       5103                        470 
##                  Molktalla                    MOLLERU 
##                       1241                       1246 
##                    Molluru                     Momidi 
##                       1342                       1982 
##                Mondemkallu               Mondepulanka 
##                       2201                       1482 
##                 Mondigedda              Mondraivalasa 
##                       1414                        442 
##            MoolaSaulaPuram                     Mopada 
##                        421                       2019 
##                     Mopadu                    Moparru 
##                       1884                       2292 
##                   Mopidevi             Mopidevi Lanka 
##                       2736                        219 
##                     Mopidi            MOPIREDDY PALLE 
##                       1357                        317 
##                     Mopuru        Mopuru Harijanawada 
##                        448                        723 
##                MOPURUPALLE                   Moragudi 
##                        205                       3983 
##                      MORAM                Moram palli 
##                       1803                       1624 
##                  Morampudi              Morasanapalli 
##                       3122                        753 
##                       Mori               MORRAYAPALLE 
##                       4620                        469 
##                  MORRIGUDA                  Morsapudi 
##                       1195                        923 
##                 Morslpalli                     Mortha 
##                       1579                       2809 
##                  Morubagal                Morusumilli 
##                       4044                       2237 
##                 Mosalpalli                     Mosuru 
##                       1044                       1274 
##                    Motdaka                Motha gunta 
##                       1693                       1206 
##                   Motkatla                    Motkuru 
##                       2528                       1883 
##                 Motlachenu               MOTU MALLELA 
##                        425                       4265 
##                 Motugudena                Motukupalli 
##                       1369                        664 
##                  Motupalli                     Moturu 
##                       1981                       2059 
##                      Movva         Moyidvijayrampuram 
##                       3628                       1408 
##             Moyillacheruvu                    Moyyeru 
##                        851                       2232 
##           Mr Krishnapatnam          MR PALLI TIRUPATI 
##                       1690                       2005 
##              Mr RangPatnam            MritunjayaPuram 
##                       3896                       1301 
##               MrRangapuram                MrRangPuram 
##                        962                        333 
##                  Muccharla                 MucchuCoat 
##                        261                       3213 
##                muchalapuri           MuchcherlaValasa 
##                        192                        856 
##                  Muchindra                  MUCHIVOLU 
##                        457                        524 
##                    MUDANGI                   Mudanuru 
##                       1143                       6653 
##                   MUDAPAKA              MUDARAM DODDI 
##                        972                       2561 
##              MUDARAM PALLE                    Muddada 
##                        332                       1074 
##               MUDDADA PETA                Muddadapeta 
##                        608                        347 
##                MuddamPalli                  MUDDAMUDI 
##                        366                        785 
##           muddamvaaripalli               Muddanapalle 
##                        499                        874 
##                 Muddangeri                  Muddapadu 
##                        509                        498 
##            Muddareddipalli                 Muddatmagi 
##                        771                        797 
##                 Muddavaram                MUDDIKUPPAM 
##                       1416                        948 
##            MUDDU RAMAPURAM                  Muddumudi 
##                        486                        421 
##                   Muddurti                    Mudduru 
##                       1839                        482 
##                Mudhi Golam                  MUDICHELA 
##                       3601                        890 
##          Mudidam Ravivlasa                  Mudigallu 
##                       1097                       3164 
##                   Mudigodu                  Mudigubba 
##                        478                        997 
##                Mudinepalli                  MUDIPALLI 
##                       3029                       1978 
##             Mudireddipalli              Muditallapadu 
##                        813                        344 
##             MUDIVARI PALLI                 Mudivarthi 
##                        599                       3703 
##                   mudivedu                   Mudivedu 
##                       1839                       2553 
##             Mudiwartipalem          MUDIYAMVARI PALLI 
##                        463                        528 
##                   Mudumala               Mudumalgurti 
##                        655                        939 
##                  Mudumpadu                   Mudunuru 
##                       2389                       2199 
##              Mudupula Joni             MUDUPULAVEMULA 
##                        454                       1050 
##                MugaChintal                     Mugada 
##                        862                       2763 
##                MUGALAMARRI               MUGANA PALLI 
##                        264                        657 
##                     Mugati                 MugChintal 
##                       3089                        702 
##                   Muggalla                   Muggulla 
##                        949                       4752 
##                  Mugldoddi              Muguman Gundi 
##                        838                        191 
##                  MUGUPURAM           MUKARAVANI PALLE 
##                        305                        871 
##              MUKAS AVAINGI           MukhteswaraPuram 
##                        484                       1581 
##               MUKKALATHURU                  Mukkamala 
##                       1677                       4236 
##                 MukkaMalla                  MukkaPadu 
##                       1304                        551 
##             Mukkavaripalli                   Mukkella 
##                       1239                       1471 
##               Mukkellapadu               Mukkidipalem 
##                       2023                        208 
##                  Mukkinada                   Mukkollu 
##                       1049                       1660 
##               MukkolluPadu                 Muktapuram 
##                       1238                       4659 
##               MUKTHESWARAM           Muktinuthalapadu 
##                       1607                       2106 
##                 Muktupuram               Mukundapuram 
##                        309                        259 
##               MukundaPuram               MUKUNDAPURAM 
##                        488                       1150 
##             MukundaRajupet               MukundaVaram 
##                        439                       1383 
##                  Mukunooru                Mulaboddwar 
##                        527                        545 
##                     Mulaga             MULAGALAMPALLI 
##                       1831                       1383 
##              Mulaguntapadu              MulakalaPalli 
##                       1140                        481 
##              MULAKALAPALLI             MulakalaValasa 
##                       1857                        303 
##                 Mulakaluru                   Mulapadu 
##                       4872                       3080 
##                  Mulapalem                  Mulaparru 
##                       1085                       4035 
##                    Mulapet                    Mulgada 
##                       3536                      13777 
##                 Mulgampadu                   Mulgpudi 
##                        274                       2430 
##                  Mulgvalli                MULIKIPALLI 
##                       3177                       1370 
##                   Mulipadu                 MULIYAGUDA 
##                        610                        758 
##                MULIYAPUTTU             Mulkala Gumdam 
##                       1173                        732 
##                Mulkallanka                   Mulkledu 
##                        529                       7487 
##                  Mulknooru                 Mulknpalli 
##                       2102                        428 
##           MULLAKALACHERUVU                  Mullapudi 
##                       4565                        397 
##                    Mulluru                    Mulpuru 
##                        788                       3035 
##                 Mulugundam                 Mulukuduru 
##                       1732                       4354 
##                   Mulumudi               Mummayapalem 
##                       2076                        994 
##          Mummidi Varappadu               Mummidivaram 
##                       1091                      14533 
##               Munagacharla                   Munagala 
##                        490                       2609 
##              Munagala Padu              MunagalaPalle 
##                       2205                        519 
##                 Munagapadu                 Munagapaka 
##                       1081                       4607 
##               MunagaValasa            Munakaya Valasa 
##                        436                        828 
##               Munchingputu                    Mundala 
##                        551                        379 
##               MUNDLA POORI                 Mundlamuru 
##                       1114                       3629 
##                 Mundlapadu                Mundlapalli 
##                       4681                        875 
##             Mundlwaripalli                    Munduru 
##                        975                       1048 
##              Munegalepalem               MUNELLAPALLI 
##                       1886                        971 
##              Mungaladoruvu                   Mungamur 
##                        527                       2045 
##                   Munganda              Mungandapalem 
##                       3190                        618 
##           Munginnagraharam                  Munibadra 
##                        530                        279 
##                  Munikudli                  Munimdugu 
##                       2229                       2513 
##                  Munipalle                  MuniPalli 
##                       1546                       1775 
##                  MUNIPALLI                   Munipeda 
##                        538                        857 
##                 Munjawaram                    Munjeru 
##                       1839                       2010 
##                  Munjuluru                   Munkulla 
##                        742                       1583 
##                   Munmarru                  Munnaluru 
##                        486                        598 
##                   Munnangi                   Munnelli 
##                       2893                        901 
##               Muntchintala                 Muntimdugu 
##                        690                        721 
##                   Munugode                 Munulapudi 
##                       2551                       1673 
##                Muppalguthi                   Muppalla 
##                        600                       9984 
##                   Mupparru               Muppartipadu 
##                       2080                       1157 
##                 Muppavaram                 Muppawaram 
##                       1746                       1562 
##           MUPPINAVARIGUDEM                  MURAGADAM 
##                        490                        463 
##                   MURAKADA               Murakambattu 
##                        767                       2872 
##     Murakambattu Agraharam                  Muramanda 
##                       1707                       4880 
##                   Murapaka                   MURAPAKA 
##                       1791                        308 
##                     Murari           Murari Chinthala 
##                       3145                       1085 
##                      Murdi           Murikimallapenta 
##                       3474                         83 
##                 Murikipudi                   Murmalla 
##                       2118                       3918 
##          MURTHYNAYANIPALLE                  Murugummi 
##                        829                        353 
##              Murukondapadu             Murukuntibadra 
##                       3947                        287 
##                   Murumuru            Musalai cheruvu 
##                        407                        360 
##              Musali Madugu                 Musalipedu 
##                        935                       1032 
##                 Musanhalli               MUSHIDIPALLI 
##                        747                       1465 
##              Mushthikuntla                Musinivlasa 
##                       1671                        415 
##                    Musiram            Muslareddipalli 
##                        432                        473 
##                 MussaPuram           Mustalgangawaram 
##                        767                        408 
##                 Mustepalli                Mustikovela 
##                        798                        824 
##                   Musunuru                MUSURUMILLI 
##                      11382                        611 
##                  Mutcherla                 Mutchigeri 
##                        640                        819 
##               Mutchinpalle                 Mutchumari 
##                       1788                        723 
##               Mutha revula                  Muthaluru 
##                       2167                       1917 
##               Muthanapalli              Muthavakuntla 
##                        477                       1759 
##                  Muthukuru                 MuthuPalli 
##                      11737                        412 
##            MuthyalaCheruvu           MuthyalammaPalem 
##                       2459                       3808 
##              Muthyalampadu               MuthyalaPadu 
##                       2772                       2857 
##              MuthyalaPalli                   Muthyalu 
##                       5681                        197 
##                    Mutluru            MUTTAMVARIPALEM 
##                       2280                        183 
##                 Muttembaka               MUTTERIMITTA 
##                        290                        421 
##                 MUTTHUKURU                   Mutukula 
##                       1392                       1103 
##                   Mutukuru              Mycherlapalem 
##                       9977                        640 
##                  MylaPalli                  Mylavaram 
##                       1420                      15236 
##                  Mynampadu                      Mypad 
##                       3266                       1649 
##               N Ga napuram                 N MYdukuru 
##                        360                       6124 
##                 N PallGiri               N T R COLONY 
##                        870                        890 
##            N. Gundla Palli                N. PALAGIRI 
##                        491                        714 
##              N. Rangapuram             N. Thimmapuram 
##                        939                        487 
##         N.GAJAPATHINAGARAM              N.Gopalapuram 
##                        799                        810 
##              N.Hanumapuram                n.k gaisala 
##                       1505                        509 
##              N.K.Rajapuram               N.Kontalpadu 
##                       2720                        730 
##               N.Kothapalli             N.Kottalapalli 
##                       2734                        575 
##               N.Narsapuram            n.r.p.agraharam 
##                        422                       1704 
##                  N.R.PURAM                N.Suravaram 
##                        942                       3118 
##              N.T.Rajapuram               Naagsamudram 
##                        709                       4390 
##               NaagSamudram                 Nadakuduru 
##                        314                       5748 
##                NADAMANTRAM                 NADASANDRA 
##                        746                        404 
##                 NADAVALOOR                 Naddipalli 
##                        922                        289 
##                   Nadendla                     Nadgam 
##                       3116                       1048 
##                  Nadichagi                  NADIGADDA 
##                       1556                        799 
##              Nadikairawadi                   Nadikudi 
##                        963                      10526 
##                NADIM PALLE            Nadimi Kandriga 
##                       1264                       3903 
##            NADIMI KANDRIGA            Nadimi Tiruvuru 
##                        716                      14107 
##               NADIMICHERLA                Nadimidoddi 
##                        997                       3394 
##                Nadimikella                Nadimivlasa 
##                        459                        605 
##                 Nadimpalem                 Nadimpalli 
##                       3297                       3085 
##                   Nadimuru                  Nadipalli 
##                        944                        544 
##                   Nadipudi                   Nadukuru 
##                       4455                        741 
##                  Nadupalli                   Nadupuru 
##                       1480                       9079 
##                  Nadupuru.                 NADURUBADA 
##                        901                        643 
##                  Nadvpalli                Nagaladinne 
##                       2233                       3085 
##                Nagalapuram                NAGALAPURAM 
##                       2107                       5136 
##              NagallaValasa                   Nagaluru 
##                        675                       1633 
##             Nagamallakunta             NagamambaPuram 
##                        283                       1098 
##               NAGAMANGALAM            Nagambotlapalem 
##                        301                       3797 
##                 NagamPalem                 NagamPalli 
##                        218                       1542 
##           NAGANATANA HALLI                   Nagandla 
##                       1787                       2024 
##                 NAGARADONA             NAGARAJUKUPPAM 
##                       1210                       1032 
##              nagarajupalli              NagarajuPalli 
##                        231                       2090 
##               Nagarajupeta                    Nagaram 
##                       9589                       4883 
##               NagaramPalli                Nagarapalem 
##                       1280                       2954 
##                     NAGARI              NagariKatakam 
##                      21708                       1039 
##               NAGARIMADUGU                NAGARIPALLI 
##                        408                        972 
##            NagasaAni palli               Nagasamudram 
##                        943                       2060 
##                  Nagavaram                  NAGAVARAM 
##                       2392                       1067 
##                Nagayalanka                Nagayatippa 
##                       4934                        572 
##                NAGAYYAPETA             Nagendlamudupu 
##                       1265                        921 
##          NagiNayaniCheruvu              NagiNeniGunta 
##                        388                       1629 
##             NAGIREDDIPALLE            Nagireddy Palli 
##                       1878                       1194 
##            NAGIREDDY PALLI             NagireddyPalli 
##                        715                       6874 
##                 NagiRiPadu            NagiShettipalle 
##                       3452                       1103 
##                    Nagluru                    Nagluti 
##                       1351                       1155 
##                     Nagoor                    Nagturu 
##                        552                       1214 
##                 NagulaPadu                Nagulapalle 
##                       1577                       3147 
##                Nagulapalli               NagulaValasa 
##                       3454                        192 
##                Nagulavaram                NagulaVaram 
##                       1289                       3323 
##            Nagulavellaturu            Naguluppalapadu 
##                       1813                       1679 
##                     Naguru                    Nagvolu 
##                        716                        280 
##                   Nagwaram               Nagwarappadu 
##                       1256                        596 
##        Nagwarappadu Arbana                   Naidupet 
##                       1261                      26492 
##                NaiduValasa           NAINARU KANDRIGA 
##                        760                        911 
##                  NAJAMPETA                Nakarikallu 
##                       1877                       4965 
##              Nakkala Dinne   nakkaladinay vaddi palli 
##                        469                        346 
##               NakkalaPalli               Nakkanadoddi 
##                       1941                       1969 
##                 Nakkapalli                  NakkaPeta 
##                       3139                        292 
##               NALADALAPURU              Nalagam palli 
##                        753                       3934 
##               Nalagampalle            Nalapareddiyuru 
##                        938                        594 
##                   NALAVAYI                 Nalkadoddi 
##                        997                       1373 
##                Nalla Billy                 Nallaballi 
##                        684                       1210 
##                 Nallabontu             Nallachelimala 
##                        220                        654 
##               Nallacheruvu          NallacheruvuPalli 
##                       4693                       2395 
##                Nallagandla             Nallagarlapadu 
##                        146                        987 
##                 Nallagonda            Nallaguttapalli 
##                       2484                       2103 
##            NALLAGUTTAPALLI         NALLAIAHGARI PALLI 
##                        524                       1726 
##                 Nallajarla                 Nallakalva 
##                       5190                       1572 
##               Nallakothuru                 Nallakunta 
##                        144                        720 
##          NALLALINGAYAPALLI               Nallamdugula 
##                       1113                        240 
##                 Nallamilli                Nallan gadu 
##                       2399                       1531 
##                  Nallapadu                 Nallapalem 
##                       9690                        454 
##                 NALLAPALEM                 NALLAPALLE 
##                        389                        905 
##          NallapureddyPalli            Nallaregulpalem 
##                        958                        569 
##          NALLAVENGANAPALLE         Nalli chetti palli 
##                        383                        434 
##                    Nalluru                    NALLURU 
##                       2210                       1381 
##   Namagiri NaraindraPatnam         Namashshivayapuram 
##                       1401                       1140 
##                  Namavaram                  NAMAVARAM 
##                       2782                        220 
##             Nambulpulkunta                    Namburu 
##                       2918                      12207 
##                   Nampalle               Nanab Pettah 
##                       1567                        881 
##                  NANCHARLA                 Nandablaga 
##                        883                       2410 
##                 NandalPadu                   Nandalur 
##                       1005                       4339 
##                 Nandampudi                    Nandamu 
##                       1159                        315 
##                  Nandamuru                  NANDAMURU 
##                       4374                        554 
##                   NANDANAM               Nandanavanam 
##                        914                       1254 
##               NandanaVanam                Nandanpalli 
##                        643                        665 
##                  NANDANURU                  Nandarada 
##                        881                       1484 
##                    Nandava                 Nandavaram 
##                        232                       9009 
##                 NANDAVARAM       Nandawarpuvani Palem 
##                       2434                       1053 
##                NANDI PALLI                   Nandigam 
##                        743                       4444 
##                   NANDIGAM                  Nandigama 
##                        395                      28290 
##               NANDIGAMPADU                  NANDIGUDA 
##                        723                       2023 
##                Nandigudena                 NandiGunta 
##                       1371                        347 
##                 NANDIKONDA                Nandikotkur 
##                        445                        844 
##               Nandikotkuru                 Nandikunta 
##                      23429                        923 
##                  NANDIMALA              Nandimandalam 
##                        593                       5720 
##              NandiMangalam                  Nandipadu 
##                       2703                       1962 
##                  NANDIPADU                 NandiPalem 
##                        655                        660 
##                 NandiPalle                  NANDIVADA 
##                        586                       6130 
##                 Nandivampu             Nandivanivlasa 
##                        508                        564 
##                NANDIVARGAM                Nandivelugu 
##                       1437                       3450 
##                    Nanduru              Nandyalmapata 
##                       1813                       5745 
##              NANGAMANGALAM             NanganoorPalli 
##                        699                        885 
##                 Nangegadda               Nanginarpadu 
##                       1834                        866 
##                 Nangipuram                   Naniyala 
##                       1252                        918 
##                 Nanjampeta                   Nannooru 
##                        652                       6535 
##            Nara Simhunipet         NaraayanaRajapuram 
##                       1037                         94 
##            NaraayanaValasa                  NARAGALLU 
##                       1040                        430 
##              Naragayapalem             Narahari Puram 
##                        711                        439 
##            NaraindraPatnam             NaraindraPuram 
##                       1362                       8220 
##                 Narakoduru           NARAMNAIDUVALASA 
##                       3096                       1087 
##                  NARAMPETA              NaraNagePalli 
##                        316                       1815 
##      NARASA RAJU AGRAHARAM  NARASA RAMAIAH GARI PALLI 
##                        697                        417 
##            NarasaiahPettah               NarasamPalli 
##                       1354                       1410 
##              NarasamPettah                NARASAPURAM 
##                        914                      27853 
##      Narasapuram Agraharam           Narasapurapupeta 
##                        481                       1604 
##           Narasareddipalli              NarasaRPettah 
##                        443                      61765 
##             Narasimhapuram             NARASIMHAPURAM 
##                        145                       1700 
##        NARASIMHARAJA PURAM         NARASIMHARAJAPURAM 
##                       1395                       1257 
##          Narasimharaopalem             NarasingaBilly 
##                        990                       1795 
##              NarasingaPadu             Narasingapalem 
##                       1063                        257 
##             NarasingaPalli         NarasingaRajapuram 
##                        297                        844 
##           NARAVAVANI PALEM                   NARAYANA 
##                       1263                       2577 
##             NARAYANA PURAM          NarayanappaValasa 
##                       4284                        907 
##              Narayanapuram              NARAYANAPURAM 
##                      10331                       1414 
##       Narayanapuram Thanda           Narayanarajupeta 
##                        221                        254 
##         NarayanareddyPalli              NARAYANAVANAM 
##                       2141                       6830 
##              Narayanmapata              NARAYUDUPALEM 
##                       1218                        174 
##                  Narepalli                  Narigonda 
##                        823                       2897 
##              Narikedlpalem             Narikellapalli 
##                        275                       2232 
##                Narikimpadu                Narjampalle 
##                        110                        527 
##               Narkedumilli               Narkullapadu 
##                       2600                       1310 
##               Narla Valasa                 Narlapuram 
##                        497                        983 
##  Narlavaram Colony H/o Nar                 Narmalpadu 
##                        385                       1418 
##                  Narnepadu                    Narpadu 
##                       1091                       1639 
##                    Narpala                  Narrawada 
##                      13382                       1689 
##                 Narsambudi                Narsannapet 
##                        918                      14471 
##                 Narsapuram               Narsayapalem 
##                      11772                       2731 
##               NARSAYYAPETA                NarseePuram 
##                       1138                        819 
##             Narshingapalli              Narsingapalli 
##                       1807                        127 
##                Narsingapet                 Narsingolu 
##                       1136                        862 
##          Narsingurayudupet                 NarsiPalle 
##                        393                        381 
##                Narsipatnam                  Narsipudi 
##                      20977                       2045 
##                 Narsipuram                NarsuPettah 
##                       3937                        651 
##                Nart Mopuru             Nart Rajupalem 
##                       3200                       3347 
##              Narukullapadu                   Narukuru 
##                        630                       1479 
##                     Naruva                      NarVa 
##                        804                       5681 
##                 NASANAKOTA               NataiahPalem 
##                       4668                       4825 
##               Natlakothuru                   Natvlasa 
##                        250                        871 
##                   Natwaram               Nava bu peta 
##                      11720                        646 
##               Navabupalena              NAVARASAPURAM 
##                       1743                       1203 
##                     Navgam             Navkhandrawada 
##                        497                        769 
##                   NAVUDURU                   Navuluru 
##                       2297                      14709 
##                  Nawabpeta                 Nawabupeta 
##                       2537                        769 
##                      Nawar                     NAWGAM 
##                       1682                        388 
##                       Naya                  Nayakallu 
##                        452                        838 
##                  NAYAMPUDI          NAYANACHRUVUPALLI 
##                        709                        552 
##         NAYANICHERUVUPALLE                  Nayanooru 
##                        584                        405 
##               Nayudukoluru                Nayudupalem 
##                        120                       1210 
##                Nayunipalli             NAYURALAVALASA 
##                       1941                        444 
##              NealDeviPuram                  NealPalli 
##                        198                       4439 
##                 nedarapeta                   Nedunuru 
##                        158                       5312 
##                Nedurupalli             Neeladevipuram 
##                       1415                        692 
##            Neelagangavaram           NEELAKANTA PURAM 
##                        910                        285 
##            NEELAKANTAPURAM        NeelakantaRajapuram 
##                        556                       1327 
##           Neelakanthapuram          Neelakantharaopet 
##                        502                       1008 
##               NeelamPettah               Neelanagaram 
##                       1036                        473 
##                 Neelapuram                 NEELAPURAM 
##                        148                        868 
##                 Neelavathi                  NEELAVATI 
##                        502                        857 
##             NEELAYYAVALASA                 Neelibadra 
##                        519                        173 
##                  Neelipudi            Neelkanthapuram 
##                       1200                        460 
##                    Neeluru                 NEERPAKOTA 
##                        676                       1089 
##                  NEERUVAYI                  Neggipudi 
##                       1109                       2336 
##                Nehru nagar                NEKANAPURAM 
##                       3596                        585 
##                   Nekkallu                   NEKKONDI 
##                        969                       1406 
##               Nekunamapata                 Nekunambad 
##                       2240                        952 
##               NEKUNAMPURAM                  Nelaballi 
##                        507                       1055 
##        Nelaballirettapalli                  Nelabontu 
##                        295                        322 
##                  Nelagonda                  Nelakurru 
##                       3057                       1298 
##                  Nelampadu                 NELAPOGULA 
##                        928                        792 
##                   NELATURU                  Nelavanka 
##                       2660                        912 
##                    NELAVOY                  Neliparti 
##                        445                        743 
##                   Neliwada                  Nelkosigi 
##                        990                        410 
##                    Nelkota                  Nellaturu 
##                       1399                       1366 
##                NELLE PALLI                NELLI PATLA 
##                       2262                       2186 
##                 NELLIMANDA                 Nellimarla 
##                       1556                      12262 
##                  Nellipaka                 NELLIPARTI 
##                        869                       1047 
##                  Nellipudi                  NELLIPUDI 
##                       3343                       1937 
##                    Nellore               NellorePalli 
##                     213087                       1121 
##               Nellurupalem                    Nelmuru 
##                       1222                       1229 
##                    Nelpadu                   Nelpattu 
##                        771                        871 
##                 Nelpumdugu                 Neltlmarri 
##                       3768                        434 
##                    Nelturu                  NELUBALLI 
##                       4543                        960 
##                    NEMAKAL                     Nemali 
##                       1691                       1790 
##                Nemalikallu                 Nemalipuri 
##                       2972                       3536 
##               Nemalladinne                Nemallapudi 
##                        877                        684 
##                      Nemam                 Nemilipeta 
##                       2881                        799 
##                   Nemkallu                  Nemmaluru 
##                       1546                        697 
##                  Nemmikuru                   NENNOORU 
##                        815                       1118 
##                Nennurupadu                   Neppalle 
##                        509                       1263 
##                  Nerametla             Neraniki Tanda 
##                       1443                        504 
##                   Nerawada                      Nerdi 
##                        956                        439 
##                     Neredi               Nereducherla 
##                        722                       1056 
##                Neredumilli                NereduPalli 
##                        817                        567 
##                Nereduppala              Nerellavalasa 
##                        637                       1320 
##                 Nerlibanda                NERNI PALLI 
##                        703                        910 
##                    Nerniki                    Nernoor 
##                        753                       1951 
##                  Nerrawada                 NersuPalli 
##                        361                       1514 
##                   NESANURU                     NETARI 
##                       1761                        629 
##               NETHA KUPPAM             Nethamkandriga 
##                       1616                        793 
##             Nethivaripalli                 Netravatti 
##                        837                       1032 
##                 Nettekallu                     Neturu 
##                       1105                        390 
##                  Ngarkanvi                    Ngaruru 
##                        230                       2369 
##             Ni.V.Rajapuram                Nibhanupudi 
##                        285                        538 
##                 Nidadavole                 Nidamannur 
##                      27770                       6705 
##                  Nidamarru              NIDASANAMETTA 
##                       9401                        624 
##                     Niddam                   Nidgallu 
##                       1168                       2724 
##                  Nidigallu                  Nidigatla 
##                       2906                       1256 
##                  Nidigattu                  NIDIGUNTA 
##                       1117                        521 
##                  Nidijuvvi                 Nidimamidi 
##                        616                       2232 
##                  Nidimusli                    Nidjuru 
##                        355                       1849 
##                 Nidragatta                  Nidubrolu 
##                       2193                        741 
##                   Nidumolu                Nidumukkala 
##                       2979                       1822 
##                   NijValli                Nikrampalli 
##                       1354                       1118 
##               NILUVUGANDLA    NILUVURALLA KAMMA PALLI 
##                        122                       1660 
##              Nimatorlawada                   Nimbagal 
##                        453                       1800 
##                    Nimmada                 Nimmagadda 
##                       1171                        518 
##                 NIMMAGEDDA               Nimmala Padu 
##                       1185                        278 
##               NIMMALAGUDEM               Nimmalapalem 
##                        673                        992 
##               NimmalaPalem              NimmalaValasa 
##                       1093                        868 
##                    Nindali                     NINDRA 
##                        614                       1396 
##                 NINDUGONDA               Nippatlapadu 
##                       1710                       1366 
##            NIRSAMKADHURGAM              Nitchenametla 
##                        606                        355 
##                    Nitturu                    Nivagam 
##                       2126                       1793 
##                NIZAMAA BAD                Nizampatnam 
##                        889                       7584 
##                NOOKALAVADA               Nookanapalli 
##                       1344                        272 
##                 Noolukunta          NOONEGUNDLA PALLI 
##                        783                        742 
##          Nooruwarhala Padu          NOOTHUGUNTA PALLI 
##                        952                        489 
##         NOOTI RAMANNAPALEM              North Addanki 
##                        506                      12458 
##                     Nossam                     Nougda 
##                       1970                        218 
##                  Noulkallu                    Noutala 
##                        769                        719 
##                 Nudurupadu               Nugondapalle 
##                       2176                        324 
##               Nujellapalli                  NUKAVARAM 
##                        492                        180 
##              Nukinenipalli              Nuklwaripalem 
##                        653                        385 
##                  Nuknpalli                 Nulakajodu 
##                        450                        571 
##                   Nulividu                      Nunna 
##                       5404                      12664 
##                   Nunparti                    Nurmiti 
##                        759                       1110 
##                   NURUPUDI                    Nutakki 
##                        140                       6224 
##               Nutana Palle                Nutchumilli 
##                        848                        567 
##                Nuthimadugu                   Nutlpadu 
##                       2609                       3650 
##         Nutula Gunta Palem                 Nutvkaluva 
##                       1337                       1567 
##                    Nuvgada                NUVVALAREVU 
##                        274                       2364 
##                Nuvvurupadu                   Nuzendla 
##                       1620                       2278 
##               Nuzvid Urban                 Nyamaddala 
##                      24493                       4218 
##                Nyayampalli                       Nyra 
##                        650                        678 
##                 O G KUPPAM              O.E.Agraharam 
##                       1844                         96 
##                 O.V.Pettah                 Obanapalli 
##                       1313                       6945 
##                 OBAYAPALLI                      Obili 
##                        566                       1446 
##         ObulaDevar Cheruvu              ObulaKkaPalli 
##                       2700                        429 
##               OBULAM PALLI                Obulampalle 
##                       1270                       2075 
##                 Obulapuram                 ObulaPuram 
##                       5111                       1477 
##       ObulaPuramh/oDosledu            obulareddipalli 
##                       1047                        807 
##            ObulaReddipalli               Obulayapalli 
##                       2227                        836 
##             Obulesunipalle       OBULURAJULA KANDRIGA 
##                       3835                        648 
##                    Odividu                  Odulpalli 
##                       1775                       2025 
##                   ODUPALLI                      Oduru 
##                        622                       3553 
##                      Ogidi                    Ogirala 
##                        681                       1194 
##                        OGU                      OGURU 
##                        543                        857 
##                  Ogurupadu                      Ojili 
##                        745                       2805 
##         Old Singarayakonda                       OLDA 
##                       4481                       1437 
##                      Oleru                     OLLURU 
##                       1395                        794 
##                    OmPalli                     Ompolu 
##                        352                        677 
##       Onappanayani kotturu                  Ondrujola 
##                        788                        926 
##                     Ongole                        Oni 
##                     115630                        479 
##                   Onipenta                Ontedudinne 
##                       4080                        359 
##                   Ootpalli                 Oppicharla 
##                       1242                       3342 
##                  Opppanagi                    Oruvayi 
##                        472                       1239 
##                  Orvakallu               P Bommepalli 
##                       5989                        880 
##               P Gannavaram          P Sugumanchipalli 
##                       5419                        295 
##                  P T MANDA               P. Byadigera 
##                        562                       1512 
##                P. Gudipadu                 P. Injaram 
##                       1234                       1269 
##              P. Kambampadu               P. Kotakonda 
##                        233                       1208 
##               P. Kothapeta                  P. Kothur 
##                        519                        846 
##            P. Lakshmipuram              P. Matlagondi 
##                        490                        674 
##              P. Narsapuram             P. Nayudipalem 
##                       2422                       3080 
##            P. Veerayapalem                P.Agraharam 
##                       1379                       1156 
##              P.Anandapuram              P.AnantaPuram 
##                        702                        327 
##               P.ANKAMPALEM               P.Bhimavaram 
##                        589                        776 
##               P.G.Kandrika               P.Gangavaram 
##                        942                        989 
##         P.I.ChinnaiahPalem                   P.J.Peta 
##                       2653                        915 
##               P.KANNAPURAM                 P.Kojiriya 
##                       2182                        785 
##               P.kotha kota               P.Kothapalli 
##                       2007                       1995 
##               P.KOTHAPALLI             P.L.DevyPettah 
##                        515                        590 
##               P.M.Kandrika             P.M.V.Kandrika 
##                        509                        243 
##               P.MallaVaram                  P.N.Puram 
##                       3267                        413 
##                P.Nandivada              P.NarasaPuram 
##                        266                       1236 
##             P.Nayakampalli             P.P. Agraharam 
##                       1359                       1113 
##                P.POLAVARAM               P.Ramannapet 
##                        711                        499 
##          P.Rambadrarajupet                P.Rayavaram 
##                        218                       1419 
##                P.RAYAVARAM           P.S.Lakshmipuram 
##                       2441                        299 
##                    P.Sardi              P.Sirigepalli 
##                       1660                        444 
##               P.SuramPalem                  P.T.Parru 
##                       1677                       1078 
##                  P.V.PURAM               P.V.R. Puram 
##                        562                        329 
##              P.Venkamapata                   P.Yaleru 
##                        506                       2962 
##               P.YERRAGONDA                 PAADI PETA 
##                        377                        661 
##               PAATA KAALVA                PAATAVALASA 
##                        509                        749 
##                 PABBAPURAM             Pabbuletipalli 
##                        672                        529 
##                Pachalvlasa                   PACHARLA 
##                        258                        227 
##                PACHAVALASA                 PACHIGUNTA 
##                        279                       1175 
##              PACHIKALAPADU               PACHIKAPALAM 
##                        237                       1963 
##                 Pachipenta              PADAGARLAPADU 
##                       3577                       1328 
##                     Padala     Padalvani Lakshmipuram 
##                       1498                        799 
##         PADAMATINAIDUPALLI             PADAMAYAVALASA 
##                        948                        678 
##                   Padarthy                Padarupalli 
##                       3799                       4615 
##                      Padda            Paddarayudutota 
##                       1014                        832 
##  paddi kambhi reddy gari p                 Paddypalem 
##                       1213                       3789 
##                   PADEREDU                    Paderoo 
##                       1142                        822 
##                       PADI                Padidempadu 
##                        694                        571 
##            PADIGALA KUPPAM             PADIGALA PALLE 
##                       1261                        606 
##                 PadigePadu           PadiKondalaPalem 
##                        226                        503 
##                     PADIRI                  Padkandla 
##                        980                       4068 
##                      Padli                PADMANABHAM 
##                       2686                       2054 
##            PadmanabhaPuram      PadmanabhaRaju Pettah 
##                       1411                        238 
##                 Padmapuram                 PADMAPURAM 
##                       1094                       1675 
##             Padmara Guduru             Padmaraviparru 
##                      10006                       2014 
##    Padmata KattakindaPalli                  PadmaTula 
##                        565                        262 
##           PADMAVATHI PURAM          Padmdtakkellapadu 
##                       3959                        629 
##          Padmti Kambampadu           Padmti Kodipalli 
##                       1912                       1655 
##        Padmti Venkatapuram                Padmtipalem 
##                        883                       3069 
##           Padmtirompidodla                 Padugupadu 
##                        375                       6975 
##             PAENGARA GUNTA              PAGADALAPALLI 
##                        701                        634 
##                     Pagali                 Pagidayala 
##                        556                       5457 
##                 Pagidirayi                     Pagodu 
##                       1760                        888 
##                     Pagolu         Pagolushi.Srinagar 
##                       1908                        361 
##            PAIDAKULAMAMIDI                PAIDAM PETA 
##                        222                        660 
##                PAIDAVALASA                    Paideti 
##                        118                        895 
##                Paidi Kalva            PaidiBhimavaram 
##                       1629                       1184 
##            Paidichintapadu                 Paidikonda 
##                       1080                       2604 
##                 PAIDIMETTA                  PaidiPadu 
##                        384                       1128 
##                  PAIDIPAKA                 Paidipalem 
##                        664                        712 
##                 Paidiparru                Paidurupadu 
##                       3835                       1742 
##                  Paimagham                      Paina 
##                        309                       1130 
##                 PAINAMPADU                Painampuram 
##                       1074                       1909 
##                   Paipalem                  Paipalyam 
##                        532                       1316 
##           Paitrikirtipuram                     Pakala 
##                       1276                       3076 
##                 PAKALAPADU           Pakirsaheb Petta 
##                       1554                       2140 
##             Pakiru Kithali                Pakirutkiya 
##                        465                       1754 
##                  Pakivlasa                      Pakki 
##                        688                       3766 
##                   Paklpadu                  Pala kuru 
##                       1970                        872 
##                 Palacharla       PALACHARLA RAJAVARAM 
##                      13277                       1194 
##                   PALACHUR                   Paladagu 
##                       1409                       1937 
##                   PALAGARA                  Palagummi 
##                       1324                       1620 
##                Palakajeedi                 Palakoderu 
##                        364                       3405 
##             Palakol(rural)                  PALAKOLLU 
##                       2861                      33964 
##                  Palakonda            PalakondaSatram 
##                       7214                        812 
##                 Palakurthi                  PALAMANDA 
##                       5396                        523 
##                  PALAMANER  PALAMANGALAM HARIJANAWADA 
##                      28167                        965 
##         PALAMANGALAM NORTH         PALAMANGALAM SOUTH 
##                        334                        765 
##                   Palamuru                PalankiPadu 
##                        396                        403 
##                   PalaPadu                     Palasa 
##                       1237                       4463 
##               PALASAMUDRAM                PalasaPuram 
##                       1828                        752 
##                  PALATHODU                    Palavai 
##                       1419                       3977 
##                 PALAVALASA                      Palem 
##                       2150                        943 
##                 PALEMPALLE                 PalemPalli 
##                       2568                       2634 
##                  Palenkota                     Paleru 
##                        313                       1830 
##                       Pali      PaliCherla Rajupalem. 
##                       1113                        279 
##             PaliCherlaPadu                   PALIVELA 
##                        578                       5838 
##                Palkhandyam                  Palklvidu 
##                        372                       1022 
##                 Palkudoddi                    Palkuru 
##                       1797                       3697 
##                  Pallagiri                 Pallakonda 
##                        635                        703 
##                  Pallamala                  PALLAMALA 
##                        194                        879 
##                 Pallamalli                Pallamkurru 
##                       2129                       6013 
##                Pallampalle                PallamParti 
##                        119                        183 
##                  Pallantla                  Pallapadu 
##                       1572                       1381 
##                 Pallapatna          Pallapu Chamwaram 
##                        570                        624 
##            PALLAPU DUNGADA               Pallaripalem 
##                        476                        827 
##  Pallavandla Palli-B.Palli                  Pallavolu 
##                       1047                       2871 
##                  PALLAVOLU              Palle cheruvu 
##                        762                        734 
##         Palle Tummalapalem                 PalleDoddi 
##                       1026                        485 
##                 Pallegunta                  Pallekona 
##                       2051                       2061 
##                     Pallem               Pallerlamudi 
##                       1339                       1019 
##                  Pallevada              PalliGandredu 
##                        943                        386 
##                Pallikuppam         PALLINARAYANAPURAM 
##                        393                       4032 
##                  Pallipadu                 PalliPalem 
##                       2762                       3398 
##     Pallivuru, Sangaruvani                 PallKolanu 
##                       2003                        750 
##                PALLLI PETA               PallSamudram 
##                       1051                       2025 
##                    Palluru                 PallValasa 
##                       3578                       5765 
##            palmakula palli                    Palnagi 
##                        787                       1996 
##                   Palparru                    Palteru 
##                       1084                       6593 
##                   Paltlgam                    Palturu 
##                        742                       4206 
##            Paludevarlapadu                   Palugodu 
##                        884                        441 
##           Palugurallapalli                   PALUKURU 
##                       2186                       1904 
##                     Paluru                     PALURU 
##                       3075                       1008 
##             PALURU (PALEM)           Paluru Rajupalem 
##                       1211                        661 
##                    Palutla                   Paluvayi 
##                        259                       2856 
##                     Palyam                   Pamaluru 
##                       1397                       1141 
##                    Pamarru                     Pamidi 
##                      14303                      16439 
##                PamidiMarru              Pamidimukkala 
##                        650                       1977 
##                 Pamidipadu                 PamidiPadu 
##                       2383                       6563 
##                 Pamudurthi             PAMUGANI PALLI 
##                       3760                       1186 
##                 PamulaPadu                  PamulaVak 
##                       6722                       1088 
##                 Pamulparru                      Pamur 
##                       1492                       5855 
##                 PamurPalli                  PANAGALLU 
##                        215                        876 
##               PANASABHADRA              PANASALAPALEM 
##                        385                        951 
##                 PanasaPadu                PANASAPALLI 
##                       4098                        600 
##       PanasaPeddi Konvlasa               PanasaPettah 
##                        613                        149 
##                   PANATURU             Pancha Lingala 
##                       1043                       3276 
##                  Panchaali                Panchadarla 
##                       2471                       2016 
##               Panchalmarri               Panchalwaram 
##                        674                        545 
##                   Panchedu                PandalaPadu 
##                        472                        459 
##                Pandalapaka                Pandalparru 
##                       5231                       1129 
##              Pandashashnam               Pandavagallu 
##                        715                        965 
##                  Pandikona                 PandiKunta 
##                       2161                       1326 
##                PandiKuntla              Pandillapalli 
##                       1131                       2910 
##              PandillaPalli              PANDILLAPALLI 
##                       2948                        965 
##                  Pandipadu                  PandiPadu 
##                        543                       1632 
##                 PandiParti         PANDIRIMAMIDIGUDEM 
##                       1267                        195 
##             Panditavilluru             PANDIVANIPALEM 
##                       3707                        617 
##                PANDLAPURAM                   Pandluru 
##                        933                        881 
##                  PANDRANGI                 Pandrapadu 
##                       1686                        555 
##                PANDRAPROLU                 Pandrawada 
##                        340                        565 
##                 PANDUGUDEM                    Panduru 
##                        124                       5395 
##                    PANDURU                    Panduva 
##                        825                        407 
##        Panduva NagulaVaram                   Panduvva 
##                        791                       1806 
##             Pandyalamadugu                    Pangidi 
##                        455                        457 
##              Pangidigudena                    Pangili 
##                       3181                        578 
##                    Panguru               Paningapalli 
##                        838                       1098 
##                PANIRANGINI                    Panjada 
##                        628                        201 
##                     Panjam             PANJAVEMAVARAM 
##                        446                       1162 
##                     Pannur                     PANNUR 
##                        209                       1287 
##            Pansareddipalli                 Panslvlasa 
##                        676                        222 
##     Pantapalem(Epuru - iB)                 Pantrangam 
##                       1392                        432 
##                PANTRAPAKAM              Pantulachervu 
##                       1455                        671 
##              PANUKU VALASA               PanukuPettah 
##                        968                        663 
##               PanukuValasa                     Panyam 
##                       2932                       8123 
##              PapaaiahPalem             PapaaiahValasa 
##                        727                        600 
##              Papammavalasa                 Papampalli 
##                        539                        194 
##                  Papampeta                  PAPAMPETA 
##                       5644                        599 
##              PaparaoPettah           Papasaheb Pettah 
##                        231                        341 
##                Papayapalem                Papayapalli 
##                       2143                       2206 
##           PAPAYYARAJUPALEM                 PAPE PALLI 
##                        829                       1506 
##                  PAPEPALLI      Papi reddy gari pally 
##                       1977                        515 
##              PapiNeniPalli          PAPIREDDGARIPALLI 
##                       2067                        408 
##             PAPIREDDIPALLE             PapireddyPalli 
##                       1235                        638 
##       PappalaLingalaValasa            Pappusettipalem 
##                        598                       1180 
##                    Para Di              Paradesipalem 
##                       1988                       5132 
##    PARAKAALVA HARIJANAWADA              Parakondapadu 
##                        195                        421 
##                  PARAMAALA             Paramasamudram 
##                        524                        454 
##                 Paramaturu        PARAMESWARAMANGALAM 
##                        936                       1030 
##                Paramtikona               Parannavlasa 
##                       2772                       1023 
##                  PARAPATLA                  Parapuram 
##                        484                       1585 
##                  Paraselli           ParashuramaPuram 
##                        372                        240 
##            ParashuramPuram                   Paravada 
##                        592                       3964 
##                   Parchuru                     PAREDA 
##                       8162                        595 
##                     PARIDI                     Parigi 
##                       1190                       7821 
##                   Parikota                  Parimella 
##                        309                        918 
##                  Parimpudi                   Paritala 
##                       5027                       4189 
##                  Parjapadu                      Parla 
##                        905                       2837 
##                     Parlam                  Parlapadu 
##                        481                        765 
##                 Parlapalli                 PARLAPALLI 
##                       5021                        667 
##               Parman Doddi                  Parmapata 
##                        457                        184 
##                 Parnapalli               Parrachivara 
##                       3142                       2164 
##                     Parsam                   Parsamba 
##                        888                        236 
##               ParuManchala                   ParuPakA 
##                       2125                       1293 
##                  ParuPalle            ParvatalaPettah 
##                        236                        138 
##              Parvathapuram              Parvathipuram 
##                        109                      27947 
##         Parvatishwarunipet                    Parvolu 
##                        167                        644 
##       Parvolu Harijanawada                 Pasalapudi 
##                        376                        940 
##                 PASALAPUDI                Pasarlapadu 
##                       4175                       1514 
##                Pasarlapudi           Pasarlapudilanka 
##                       3978                       2259 
##              Pashuvullanka           Pasi GanguPettah 
##                       2263                        547 
##                 Pasivedala                    Pasluru 
##                       2164                        989 
##    Pasluru-(Siddalampuram)                  Pasukuddi 
##                       1029                        404 
##                 PASUMANDHA                  Pasumarru 
##                        271                       4510 
##                   PASUPALA                  Pasupalli 
##                       1036                       1280 
##                    Pasupam                PASUPATHURU 
##                       1150                        385 
##                Pasupugallu                   Pasupula 
##                       2274                       2120 
##                  Paswemula            PATA BHEMASINGI 
##                       2522                        924 
##              Pata Cuddapah            Pata DoddiGunta 
##                       6052                       2436 
##          Pata MallamPettah            Pata Nadakuduru 
##                       1400                        472 
##               Pata Paderoo             Pata Tungapadu 
##                       1765                       4935 
##             PataBitragunta                   PataCoat 
##                       3095                       1087 
##            PataJagdevPuram           Patakothacheruvu 
##                        285                       1970 
##               Patalameraka                 Patalpalle 
##                        725                       1035 
##                  PataPalli         PATAPANDUVARIGUDEM 
##                       1418                        245 
##             Patareddypalem               Patarlagadda 
##                       5168                        810 
##               Patarlapalli               PATARUDAKOTA 
##                       1888                        483 
##             PataSrikakulam           PataSundaraPalem 
##                       1925                        208 
##                PataTekkali                  Patbaggam 
##                       1506                        317 
##              PATCHANAGARAM               Patcharhalli 
##                        542                        228 
##                   PatchaVa                  Patempadu 
##                       1164                        216 
##              PATHA KOVVADA         PATHA MARADHI KOTA 
##                        840                        274 
##            Patha Mulakuddu               PATHA PALYAM 
##                        340                        583 
##        Patha Paradesipalem            PATHA PONNUTURU 
##                        497                        709 
##            Patha Puchirala            Patha Ramapuram 
##                        994                        241 
##        PATHA SANGATI PALLE             Patha Tiruvuru 
##                       1299                       4031 
##                PATHAARKADU                PATHABAGGAM 
##                       1145                        169 
##                 PATHAGUNTA                  PATHAKOTA 
##                       1116                        587 
##           Pathangibiswaali                  Pathapadu 
##                        261                       3670 
##                  PATHAPADU                PATHAPALYAM 
##                        367                        726 
##                Pathapatnam             PATHARAMAVARAM 
##                       8967                        327 
##            Pathaveerapuram          PATHAVENKATAPURAM 
##                        483                       1242 
##                PATHI KONDA               PATHI PUTTUR 
##                       1211                       2330 
##             Pathikayavlasa            PathiKuntaPalli 
##                        606                       1778 
##                   PathyWad                  PatiBanda 
##                       1663                       2744 
##                Patinivlasa                  PatiPalli 
##                        205                       1155 
##              PATIVADAPALEM               Patkandukuru 
##                        438                        880 
##                  Patkunkam                  Patlavidu 
##                        392                       1315 
##                 Patnalpadu                     Patnam 
##                        566                       5739 
##                 Patnoupada                patra palle 
##                       1459                        917 
##                PATRA PALLI                  Patrapada 
##                       1333                        231 
##                    Patrega              PATRUNIVALASA 
##                       1324                        174 
##               Patrunivlasa                PATTAIGUDEM 
##                       1010                        344 
##                     PATTAM          PATTAMVANDLAPALLE 
##                       1111                       2385 
##             Pattennapalena                 Pattikonda 
##                       1197                      13225 
##                 PATTIKONDA                   PATTISAM 
##                       1967                       1043 
##                 PATTISEEMA                 Pattulogam 
##                        940                        432 
##                 PattuPuram                 PATTUPURAM 
##                        987                        326 
##                      Patur                     Paturu 
##                       7182                       2197 
##                     PATURU               PATURUNATTAM 
##                       1644                       1676 
##               Patuwardhnam                    Patvala 
##                        370                       3577 
##                     PAVADA                      Pavar 
##                        379                       2689 
##                   Pavuluru                Payaka Padu 
##                       2953                        529 
##                Payakapuram             PayakR Bonangi 
##                       1090                       1253 
##              PayakR Pettah   Payasam Rangareddy Palle 
##                      13148                       1388 
##               Payasampalli                 PE TNIKOTA 
##                       1462                       1780 
##             PEDA ADDAPALLI             Peda Agraharam 
##                        776                        630 
##                Peda amiram             Peda Avutpalli 
##                       3545                       4484 
##               PEDA BARANGI            PEDA BHEEMPALLI 
##                        461                       1331 
##            Peda Boddepalli            Peda BuradaPeta 
##                       7505                        643 
##               peda gaisila              PEDA GUDIPALA 
##                        203                        709 
##            Peda Jaggampeta                Peda Kakani 
##                       1676                      15020 
##              Peda Kamnpudi               Peda Konduru 
##                        486                       3225 
##              Peda KoorPadu            Peda Kothapalli 
##                       7758                       2275 
##                Peda Madina                PEDA MALLAM 
##                       1343                       1698 
##           Peda Mamidipalli                PEDA MARIKI 
##                        983                        615 
##              Peda Nemwaram               Peda Ogirala 
##                       1095                       1884 
##              Peda Palkluru         PEDA PATTAPU PALEM 
##                      15106                        231 
##               Peda pulleru                Peda Ravuru 
##                       2054                       5029 
##             Peda Ullagallu                Peda Uppada 
##                       1498                       1128 
##               Peda Uppalam             Peda Vadlapudi 
##                       2575                       6832 
##           Peda Vuyyalawada            PedaAlavalapadu 
##                        739                        948 
##                  Pedaballi             Pedabantupalli 
##                       2062                        619 
##                 PEDABAYALU             PedaBondapalli 
##                       1918                       2770 
##                  Pedabrada            Pedabrahmadevam 
##                       2298                       4710 
##                Pedabuddidi           PEDACHAMALAPALLI 
##                       1494                        619 
##            PedaCherlopalli                     Pedada 
##                       1574                        481 
##            PedaDoddi Gallu                   PedaGadi 
##                       1136                       1237 
##               Pedagadvalli             PEDAGANGAVARAM 
##                        721                        531 
##                 PedaGanjam              Pedagantiyada 
##                       4467                      58867 
##              PedaGarlaPadu                 PEDAGARUVU 
##                       1724                        541 
##              Pedagdelwarru                 Pedagdubha 
##                       1388                       3183 
##                PEDAGEDDADA                 PEDAGOGADA 
##                       1060                        674 
##            PedaGogulapalli                 Pedagonnur 
##                        442                       1507 
##                Pedagothili              Pedagummuluru 
##                        709                       2374 
##                   Pedakada             Pedakallepalli 
##                        688                       2025 
##                  Pedakamba              Pedakancherla 
##                        110                       2636 
##             Pedakandepalli            Pedakandlagunta 
##                       1351                        808 
##              pedakapavaram              PEDAKAPAVARAM 
##                       2862                        290 
##                  Pedakarja           Pedakodam Gundla 
##                        372                       1739 
##              PEDAKODAPALLI                 PedaKondur 
##                       2138                       1324 
##                   PEDAKOTA             Pedakothapally 
##                       1296                        325 
##              PedakotiPalli       PEDAKRISHNARAJAPURAM 
##                        418                        515 
##                  Pedalanka          Pedalanka kothuru 
##                       6897                        216 
##                Pedalingala          PedalingalaValasa 
##                        366                        580 
##                 Pedalochli              Pedalunasnagi 
##                       1179                       1073 
##                Pedamaddali                PedaMadduru 
##                       2071                        611 
##             Pedamajjipalem                Pedamakkena 
##                        399                       1805 
##               Pedamakwaram               Pedamambattu 
##                       1236                        714 
##              Pedamanapuram          Pedamangamaripeta 
##                       1011                        413 
##              Pedamatlapudi              pedamedapalli 
##                       3210                       1797 
##                Pedamernagi             Pedamodugpalle 
##                       1686                        681 
##            Pedamushidiwada             Pedamusidiwada 
##                       1202                        316 
##                Pedamuttevi               Pedana Urban 
##                       2297                      19884 
##              PedaNadipalli         Pedanagamayyapalem 
##                        830                       2296 
##              Pedanandipadu             PEDANANDIPALLI 
##                       1762                       1349 
##                 Pedanchala            Pedanindrakolnu 
##                        981                       3637 
##                 Pedankalam                  PEDAPADAM 
##                        780                        924 
##                   Pedapadu              Pedapalaparru 
##                       8594                       1530 
##                  PedaPalem                  PedaPalla 
##                       1829                       1220 
##            PedaPallamKiiah                  Pedapalli 
##                        108                       4054 
##                  PedaPalli                  PEDAPALLI 
##                       2224                       2004 
##                 PedaParimi                  Pedaparti 
##                       4132                       1209 
##               Pedaparupudi                 Pedapatnam 
##                       1533                       3645 
##                 PedaPavani                  PEDAPENKI 
##                       1798                       4124 
##                  Pedapolla                  Pedapriya 
##                        190                        639 
##                  Pedaprolu                   Pedapudi 
##                       1453                       9661 
##         Pedapudi Agraharam               Pedapulipaka 
##                       1246                       1880 
##              Pedapuliwarru                PedaPuthedu 
##                       2936                       3212 
##                  PEDAPUTTU                   PedaRaam 
##                        408                        515 
##        PedaRaam BadraPuram              PedaRajupalem 
##                       1963                        475 
##                 PedaRPalli             PedaSavlaPuram 
##                        460                        448 
##                 Pedashakha                 Pedashnglu 
##                       1075                       2263 
##                 Pedasirlam                PedaTadiWad 
##                        544                       2768 
##              Pedatamrpalli                Pedatankidi 
##                        804                         85 
##                Pedatinarla                Pedatummidi 
##                       1979                       2571 
##                 PedaValasa                PedaVangara 
##                       1229                        137 
##                  Pedavanka                   PedaVegi 
##                        511                       7730 
##                 PEDAVEMALI          PedaVenkannapalem 
##                        855                        458 
##               Pedavirivada              PEDAVULEMPADU 
##                        330                        747 
##                 Pedayadara              Pedayirlapadu 
##                       2201                       1603 
##            PEDDA ABBIPURAM         Pedda Bommanapalli 
##                        960                        380 
##            PEDDA BOMPA LLI          Pedda Gopanapalli 
##                        464                        625 
##            PEDDA GUJJUVADA         Pedda Gummadapuram 
##                        441                        494 
##            PEDDA HARIVANAM          PEDDA JONN VALASA 
##                       2815                        305 
##               PEDDA KALUVA           Pedda Kanaparthy 
##                       1836                       1101 
##              Pedda Kannali             PEDDA KOPPERLA 
##                       2924                        510 
##            PEDDA KOTTAKOTA           PEDDA MALKAPURAM 
##                        173                        464 
##           Pedda Mattapalli             Pedda Orampadu 
##                        694                       2237 
##             Pedda Pasupula           Pedda Rangapuram 
##                       3132                       1980 
##         Pedda Seetanapalli      PEDDA THIPPA SAMUDRAM 
##                        620                       2939 
##            PEDDA THUMBALAM                 Peddabadam 
##                       5657                        349 
##            Peddabadanavada               Peddabammidi 
##                        433                        704 
##             Peddabanapuram         Peddabangarunatham 
##                        392                        690 
##          PEDDABARENE PALLI               PEDDABODANAM 
##                        283                        908 
##             PEDDABODDAPADU              PEDDACHEPPALI 
##                        357                       1748 
##          Peddachigullarevu                    Peddada 
##                        780                       1885 
##              Peddadandluru           Peddadevelapuram 
##                        506                       1343 
##                 Peddadugam              PEDDAETIPAKAM 
##                       1023                        467 
##         PEDDAGANAGALLAPETA           Peddagerigipalle 
##                       1951                        396 
##            Peddagollapalli             Peddaguruvluru 
##                        610                        337 
##                 Peddahaita                Peddahoturu 
##                        316                       2682 
##              PeddaiahPalli      PEDDAJAGANARDANAPURAM 
##                        219                        846 
##            PeddaJonnaVaram                Peddajuturu 
##                       1135                       1501 
##                PEDDAKADARI           Peddakagitapalli 
##                        201                        178 
##             Peddakambaluru               Peddakduburu 
##                       1710                       4476 
##           PeddaKolliValasa           PEDDAKONDAMMARRI 
##                        285                        609 
##             Peddakothiliki                PEDDAKUDALA 
##                        612                       1420 
##         Peddakurabalapalle                 Peddalamba 
##                        432                        524 
##            PEDDALAXMIPURAM            PEDDALAXMIPYRAM 
##                        586                        383 
##                PEDDALOGIDI            Peddalvunipalli 
##                        324                        575 
##               PEDDAMALLELA               PEDDAMANDAYM 
##                       2747                       1378 
##                Peddamantur             Peddamarrividu 
##                       1243                       1933 
##                   Peddamdi               Peddamudiyam 
##                        647                       1243 
##         PEDDAMURAHARIPURAM              PeddaNaidupet 
##                        641                        143 
##              Peddanelaturu               Peddanjimedu 
##                       1859                        889 
##           Peddannwaripalli                 Peddanpadu 
##                       4434                       2192 
##               PEDDANUTHULU            Peddapadmapuram 
##                        205                       1106 
##                  Peddapadu              PEDDAPALAVEDU 
##                       2519                        447 
##                 PEDDAPALEM                 PEDDAPALLI 
##                       2012                        725 
##               PEDDAPANJANI           Peddaparthikunta 
##                       1753                        458 
##           Peddapatnanlanka               Peddapolmada 
##                       3002                       3656 
##               Peddapudilla                 Peddapuram 
##                       1498                      30635 
##             Peddapurappadu             PEDDARAJUPALEM 
##                       2761                        591 
##              PEDDARI KUNTA               Peddarikatla 
##                        706                       1477 
##                 Peddarkuru          Peddarokallapalli 
##                        474                        531 
##                Peddarveedu                  PEDDASANA 
##                       1219                       1222 
##               Peddasankili           PEDDASARIA PALLI 
##                        730                        616 
##           Peddashettipalle            Peddasunnapuram 
##                       3770                        125 
##                PEDDATEKURU                Peddatungam 
##                       2294                        165 
##           PEDDAUPPARAPALLI              Peddavaduguru 
##                       4197                       4598 
##                peddavalasa               Peddavangali 
##                        554                        909 
##                 Peddavanka                 Peddavaram 
##                        244                       4062 
##              PEDDAVELGATUR          PEDDAVENKATAPURAM 
##                       1164                        292 
##              peddaventarla           PEDDAYALLAKUNTLA 
##                        710                        767 
##          Peddayallam Palli            Peddayammanooru 
##                       2632                       1148 
##           Pedddasallapalli                   PEDDEVAM 
##                        123                       1499 
##          PeddiAreddy Palli                PEDDIM PETA 
##                       1048                        321 
##             Peddinenikalva                 PEDDIPALEM 
##                       2622                       2643 
##                  Peddividu           Peddobinenipalli 
##                       2688                        683 
##                   Peddoddi              Pedduguruvuru 
##                        473                        250 
##                     Peddur                   Pedduroo 
##                        334                        879 
##             PEDHAPOTUCHANU               Pedullapalli 
##                        658                        956 
##                     Peduru               Pedwarimdugu 
##                       2151                        515 
##            PEERUSAHEB PETA                       Pega 
##                        283                        436 
##                Pegallapadu                     Pekeru 
##                        852                       3015 
##                  Pellakuru                  PELLAKURU 
##                        765                       1021 
##                    Pelleru                    Pelluru 
##                       1439                       2175 
##               Pemmadapalli                   Penaglur 
##                       1218                       3992 
##               Penakacherla               Penaknametta 
##                       2460                       1852 
##                 Penamakuru                 Penamaluru 
##                       1308                      17067 
##                    Penasam            Penchikalamarru 
##                        967                       1054 
##            Penchikalapalle               Penchiklpadu 
##                        297                       1637 
##                  Pendayala                 Pendekallu 
##                       1386                       2001 
##            Pendekallu R.S.             Pendlimantanda 
##                        684                        533 
##                Pendlimarri                   PENDLURU 
##                       3571                        656 
##                   Pendurru                  Pendurthi 
##                       1121                      12454 
##                  PENDURTHI                    Pendyal 
##                       1740                       2426 
##               Penikelapadu                   Penikeru 
##                       1276                       2131 
##                  Penjendra                    Pennada 
##                        372                       3285 
##                 Pennagadam                Pennalapadu 
##                        740                        376 
##                 PENNEPALLI                      Penta 
##                        357                       2637 
##                      PENTA                  Pentakota 
##                        655                       2985 
##                  Pentapadu           PentaSrirampuram 
##                       4248                        583 
##            Pentelwarigudem                 Pentibadra 
##                        596                        316 
##                   Pentrala                    Penturu 
##                        301                        819 
##                   Penubaka                   PENUBAKA 
##                       1016                        281 
##               PENUBALAKALA                  Penuballi 
##                        580                       1494 
##                  PENUBALLI                 Penubarthi 
##                        348                       3049 
##                  PENUBARTI            Penuganchiprolu 
##                        753                       7161 
##                  Penugollu                  Penugolnu 
##                       1659                       2257 
##                  Penugonda                 Penuguduru 
##                      10138                       3015 
##             Penugudurupadu                  Penukonda 
##                        619                      16112 
##                  PENUMADAM                   Penumaka 
##                       3957                       3879 
##               Penumaklanka                  Penumalla 
##                        776                       2887 
##                 Penumallam                  Penumalli 
##                        966                       1409 
##               Penumanchili                 Penumantra 
##                       2722                       8420 
##                  Penumarru                 Penumarthi 
##                       2048                       1171 
##                 Penumatcha                   Penumudi 
##                        590                       1188 
##                   Penumuli                    PENUMUR 
##                       2129                       4720 
##                    PERADAM                 Peraimbadi 
##                        319                       1710 
##                     Perala                   Peramana 
##                        752                       1430 
##             PeramGudiPalli           Perammagaripalli 
##                        363                        209 
##              Perantalpalem                  Perapuram 
##                        802                       1260 
##                   peravali                   Peravali 
##                       5448                       5362 
##              PeravaliPalem                  Perawaram 
##                       1574                       1484 
##                Perayipalle                 Perecherla 
##                        777                       8330 
##                   Peridepi                Perikegudem 
##                       1086                       1036 
##                   Perimidi                 PERINDESAM 
##                       1240                        734 
##                     Peripi                Periyavattu 
##                       1543                       1075 
##                      Perli                    Pernadu 
##                       4166                        844 
##                 Pernamitta                  PERNAPADU 
##                      11331                        326 
##               PersuAmPuram               Perukalapudi 
##                       1579                       3032 
##                   Perumali              Perumallapadu 
##                       1920                       1731 
##             Perumallapalli             PERUMMALAPALLE 
##                        346                        455 
##                   Perumula                  PerupaleM 
##                        326                       9004 
##                      Perur                      PERUR 
##                      16892                       7182 
##                  PerurPadu                 Perusomula 
##                       1590                       2526 
##                   Perwaram                PesalaBanda 
##                       4720                        649 
##                Pesaladinne                Pesaramilli 
##                        811                        303 
##                 PESARAPADU                 Pesarlanka 
##                        474                       1499 
##                  Pesarvayi             Peta agraharam 
##                       2132                        451 
##      Petcharlavenkatapuram                     Peteru 
##                        685                       4223 
##                    Petluru           Petluruvaripalem 
##                       3460                       1028 
##             Petsannigandla           Pettah Sudipuram 
##                       3095                       1634 
##            Pettugollapalli                    Peyyeru 
##                        584                       1810 
##                   Phanidam         Pichalavandlapalle 
##                       2016                       2074 
##                   PICHATUR                Pichiklpadu 
##                       2514                       1084 
##              PIDATHAMAMIDI                 PIDI PALLI 
##                        712                        851 
##                Pidimandasa                Pidingoyayi 
##                        528                      11935 
##                 Pidisheela                   Pidparru 
##                        238                       1005 
##           Pidtala Gudipadu                Pidtapoluru 
##                        973                       2176 
##                  Pidtlpudi                Piduguralla 
##                        460                      34634 
##                PIDUGURALLA                     Piduru 
##                       6169                       1729 
##                Pidurupalem                  PiecePadu 
##                        729                       1317 
##                    Pigilam               Pikala Betta 
##                       1443                        348 
##                     PILERU               PILLA KUPPAM 
##                      28862                        827 
##              PILLALAVALASA                Pillalpalli 
##                        953                       4026 
##                  Pillamedu                   Pillanka 
##                        527                       1306 
##              PILLARIKUPPAM               PILLARIPATTU 
##                       2270                        627 
##             Pillavanipalem       PILLETIVARI KANDRIGA 
##                        184                        359 
##                Pilligundla                   Pillutla 
##                        672                       3626 
##                   PINAGADI            Pinagudurulanka 
##                       1465                        412 
##                 Pinakadimi                   PINAKOTA 
##                        966                       1280 
##                   Pinapadu                  Pinapenki 
##                       1915                        944 
##                 PINAVEMALI                  PINDRANGI 
##                        799                        540 
##             Pindrangivlasa                 Pindruwada 
##                        559                        586 
##                   Pinnadri        PinnamaAreddy Palle 
##                       2494                        344 
##              PINNAMAVALASA                 Pinnapuram 
##                        826                       2729 
##                   Pinnelli               PINNINTIPETA 
##                       4095                        941 
##                    Pinpaka                   Pinpalla 
##                        589                       1221 
##                Pintadinada                Pippalbadra 
##                       2109                        392 
##                    Pippara          Pippilakothapalli 
##                       6318                        953 
##         Piriadi Nainawarmu                     Piridi 
##                       2071                       3179 
##      Pirtani @Elvin Pettah                    PiruWad 
##                        912                        758 
##                     Pisini                 Pisinikada 
##                        756                       2741 
##                  Pitapuram                   Pitatoli 
##                      33580                        405 
##                 Pitchapadu                 Pitchaturu 
##                        716                        671 
##     Pitchiganti Kothagudem            Pitchikalapalem 
##                       1408                       1446 
##                 Pithapuram              Pitikayagulla 
##                        979                       1831 
##                    Pittada                 Pittalanka 
##                       1358                       1488 
##             Pittalavemaram               Pittalsariya 
##                       2347                        453 
##            Pittalvanipalem                 Pittigunta 
##                       4845                        460 
##                Pochampalli                 pochavaram 
##                       1370                        398 
##                 Pochavaram                 PochaVaram 
##                        984                        427 
##                 PODADURTHY             Podagatlapalli 
##                        488                       3529 
##               Podala Kunta                   Podalada 
##                        633                       1735 
##           Podalakondapalli               PODALAKUNTLA 
##                       2010                        994 
##                 Podalakuru                       Podi 
##                       8298                        487 
##                     Podili                      Podli 
##                      13233                        240 
##                      Podur                   Pogaruru 
##                       4960                        280 
##                     Pogiri                Pogurupalle 
##                       1649                        952 
##                  Pokkunuru                     POKURU 
##                        677                       1551 
##              PolaiahValasa                   Polakala 
##                       1178                       2580 
##                  PolaKiiah                 Polampalli 
##                       2716                       1531 
##                   Polamuru               Polasigudena 
##                       3168                        483 
##                Polatitippa                  Polavaram 
##                        890                      10729 
##                  Polekurru                  Polepalle 
##                      10990                       4870 
##     Polepalle@ KOVELAPALLI                  Polepalli 
##                        826                       5013 
##                     Poleru                       Poli 
##                        897                       3225 
##                       POLI             POLIGARI PALLI 
##                        349                        787 
##                     Poliki             POLIMERA PALLI 
##                       1664                        665 
##            Polinenicheruvu              Polinenipalem 
##                       1258                        975 
##                  Polipalli             Polireddipalem 
##                       1990                       1574 
##              PolisettiPadu                     Polkal 
##                       1620                       5439 
##                    Pollada                   Pollanki 
##                        703                        334 
##                    Polmuru               Polsanipalli 
##                       3483                       1604 
##                Polsanpalle                  Polukonda 
##                       1136                        429 
##                     Poluru              Ponakaladinne 
##                       2693                       1208 
##                 Ponakumadu                   Pondalur 
##                        623                       3955 
##                  Pondugala                  Pondugula 
##                        722                       1951 
##                    Ponduru                    PONDURU 
##                       1039                       9061 
##              PONGALI PAAKA                    Ponguru 
##                        860                       2786 
##                  Ponguturu                    Ponnada 
##                       1379                       5310 
##                    Ponnagi                   PonnaKal 
##                       1272                        445 
##                  Ponnaluru                     Ponnam 
##                       2979                       1156 
##          PONNAMAKULA PALLI                 PONNAMANDA 
##                        888                       4693 
##                Ponnamapata                PonnamPalli 
##                        543                        517 
##                 Ponnanguru                 Ponnapalli 
##                       1587                       1469 
##                 Ponnathota                 Ponnavaram 
##                        795                        902 
##                  Ponnavolu                 Ponnekallu 
##                        547                       5300 
##                     Ponnur                   Ponugodu 
##                      37683                        642 
##                 Ponugupadu              Ponugutivlasa 
##                       2120                        856 
##        poojarivandla palli                Poolachinta 
##                        464                        926 
##                 PoolaKunta                PoolaKurthi 
##                       3292                       2960 
##                 Poolapalli                 PoolaThota 
##                       3850                        782 
##                  POONAGALU                    Poondla 
##                        361                       1399 
##        Poondlachennu Palli                  PoosaPadu 
##                        514                       2895 
##                     Popuru                    Poraali 
##                        314                        393 
##                      Poram                    Poranki 
##                       2370                      17754 
##           Poreddiwaripalli                 Porlupalem 
##                        682                        913 
##                Porumamilla               Potaiahvlasa 
##                       8958                        239 
##                PotamPettah                 Potarlanka 
##                        509                       3833 
##                  Potegunta                  Potepalli 
##                       1397                       2166 
##                 Pothakamur                PothalaPadu 
##                       2800                        957 
##                  Pothanagi               PothanaPalle 
##                        465                        431 
##               PothanaPalli      POTHANAPUDI AGRAHARAM 
##                        560                        199 
##    POTHANAVALASA AGRAHARAM                 Pothavaram 
##                        615                       4669 
##                 POTHAVARAM              PothiNaidupet 
##                       4198                        643 
##       Pothinamallayyapalem                  Pothipadu 
##                       9093                        310 
##           Pothireddy Palem           Pothireddy Palli 
##                       2822                       1946 
##                 PothuDoddi                  Pothukuru 
##                       1059                        788 
##                 Pothumarru                    Pothuru 
##                       2635                       3180 
##                     Potipi                 Potladurti 
##                       1385                       5241 
##                  Potlapadu                 Potlapalem 
##                       2244                        225 
##                  Potlapudi                      Potli 
##                       1118                        582 
##                    Potluru                    POTNURU 
##                       1868                       2050 
##                 Potrakonda                    Potriya 
##                        641                        139 
##              Pottaiahvlasa   Pottempadu[Sarvepalli-5] 
##                        537                       1210 
##                 Pottepalem                 Potti Padu 
##                       1927                        607 
##             Pottidorapalem                  Pottipadu 
##                       1314                       2106 
##                  Potugallu                 Potukanuma 
##                       1607                       1312 
##              Potulngepalli                   Potuluru 
##                       1499                       2133 
##                 Potumeraka                  Potunooru 
##                       2726                        184 
##                   Potunuru               Potwarappadu 
##                       2545                        166 
##              Prabhalaveedu               Pragadapalli 
##                       1369                        840 
##               PRAGADAVARAM                    Pragnam 
##                       4158                        449 
##             Praharajupalem             PRAHLA DAPURAM 
##                        835                       2694 
##                   Prakarla           Prakashraopalena 
##                        187                       1316 
##                Prakkilanka               Prasadampadu 
##                        964                      10742 
##              Prasangulpadu  PRASANNAVENKATESWARAPURAM 
##                       1014                       1080 
##     Pratapaviswanadhapuram                 Prathakota 
##                        222                       3929 
##           Prathikollalanka                 Prathipadu 
##                        620                      14259 
##                 Prathipaka              Priyagraharam 
##                        333                       1523 
##             Pro. Dontamuru          ProbhaGiri Patnam 
##                       1486                       1218 
##                  Proddutur                  PRODDUTUR 
##                       1742                     109184 
##                Proudduvaka           PrushottamPatnam 
##                        822                       2400 
##                    Pubbada          Puchakayala palli 
##                        147                        186 
##                PUCHIKAPADU                     Puderu 
##                        215                       1615 
##                       Pudi                       PUDI 
##                       1868                        614 
##  PUDI ANE CHENNAKESAVAPURA                Pudi Valasa 
##                        590                        448 
##                 Pudicherla         PUDIJAGANNADAPURAM 
##                       1713                       1308 
##                  Pudimdaka                  PUDIPALLI 
##                       5947                       1299 
##                  Pudiparti                  PUDIPATLA 
##                       2064                       1018 
##             Pudirayadoruvu              PUDIVANIPALEM 
##                        655                        536 
##                  Pudivlasa                   Pudiwada 
##                        543                       1854 
##                 PUDUKUPPAM                      Pudur 
##                        905                        781 
##                     Puduru               PulagamPalli 
##                       2178                       1187 
##                  Pulaparru                 Pulaparthi 
##                       1246                       1215 
##                     Puleru                Puletipalli 
##                       2373                       2669 
##                Pulgalpalem                   Pulgurta 
##                       1475                       2034 
##                PULI VALLAM                 PULICHERLA 
##                        383                       2319 
##                  PuliDindi                  Puligadda 
##                        933                       1697 
##             PULIGOGULAPADU                  Puligummi 
##                        611                       1696 
##           PuliGundla Palli                  PULIKALLU 
##                       1125                        856 
##                   PULIKALU                  PuliKollu 
##                        936                       1092 
##                  Pulikonda                   Pulikoru 
##                       2523                        361 
##                PuliKundram                PULIKUNDRAM 
##                        941                        733 
##                  Pulikunta      PuliKuntla Rallapalli 
##                       2027                        921 
##            Pulikuntlapalli                   Pulimeru 
##                        707                       2246 
##                   PuliPadu              Pulipoddaturu 
##                       4613                        351 
##                  PuliPutti            PULIRAMUDUGUDEM 
##                        447                        369 
##                 Pulivendla        Pulkandam Ponnavolu 
##                      30251                       1159 
##                      Pulla                 Pullagummi 
##                       3231                       1896 
##                PULLAJIPETA             PullalaCheruvu 
##                        623                       2985 
##                  Pullampet                   PULLANGI 
##                       6798                        788 
##          Pullanginerudlova                  Pullapadu 
##                         88                        682 
##         PULLAREDDYKANDRIGA            Pullareddypalli 
##                        139                        770 
##            PullareddyPalli               Pullayapalle 
##                        605                        785 
##               Pulletikurru                    Pullita 
##                       4317                        384 
##                 Pulliveedu                    pulluru 
##                        613                       2312 
##                    Pulluru                    PullurU 
##                       1248                       3457 
##                    PULLURU                    Pulmati 
##                       3207                       2431 
##                 Pulpathuru                    Pulsara 
##                       1256                        226 
##                   PUNABAKA                 Punadipadu 
##                       1155                       3663 
##                  PUNGANURU              Punjalurupadu 
##                      35844                        579 
##                     Punnam               PUNNANAPALEM 
##                        435                        383 
##                 Punnepalli                   Punnooru 
##                        970                        422 
##                  PunnValli                    Punooru 
##                        513                       3811 
##            PUNUBUTCHEMPETA                   Punugodu 
##                        304                        508 
##                  Punukollu             Punya samudram 
##                        461                        970 
##                    Puppala           Puppalwarigudena 
##                       1419                        328 
##                PuretiPalli                  Purimetla 
##                        529                        672 
##                     Purini                Puritigadda 
##                       1930                       1165 
##                 Puritipadu                Puritipenta 
##                        744                       3084 
##                      Purli               PURNA BHADRA 
##                        485                        201 
##                 Purnatakam            Purohitunivlasa 
##                        421                        933 
##  PuroshottamPuram, k.r.Pur            Purushothapalli 
##                       1597                       1836 
##           Purushothapatnam            PURUSHOTHAPURAM 
##                      48986                       4201 
##            Purushottapuram           Purusothampatnam 
##                      10607                        705 
##                 PusalaPadu                      Pusam 
##                       2597                        333 
##              PusapatiPalem                   Pushadam 
##                       1908                        375 
##                    Pusluru                Puspatirega 
##                       1157                       5735 
##                   Pusuluru                Putchagadda 
##                       1104                        676 
##            Putchakayalmada               Putchalpalli 
##                       1701                        618 
##               Putchanutala                 Putchapadu 
##                       3040                        186 
##              Puthala pattu           Puthanavaripalli 
##                       3833                        565 
##                    PUTHERI               PUTIKAVALASA 
##                        454                        207 
##                   Putikpet                 Putiyadala 
##                        961                        453 
##               PutlaCheruvu                Putlampalli 
##                       1061                       1916 
##                    Putluru                Putra madhi 
##                       4088                       1609 
##                    Putrela           PUTTA GANI PALLE 
##                       3742                        787 
##                 Puttakonda          Puttamnayudupalli 
##                       1120                        167 
##                 PuttaParti                Puttapashmu 
##                      12498                        493 
##               Puttayapalli                     Puttur 
##                        626                      15840 
##                      puudi                    Puvvada 
##                        410                       1784 
##                   Pyadindi                  Pyalkurti 
##                       2182                       4455 
##                   Pyaparru                    Pyapili 
##                       1516                       7489 
##                Pyarampalli                     Pydela 
##                       1390                        608 
##                   Pydipala            R-ANANTHA PURAM 
##                       2689                        254 
##  R B Puram Echa/O Maruwada               R NAGULAVRAM 
##                        947                        951 
##             R S Rangapuram             R. AnantaPuram 
##                       3371                       1889 
##           R. ShivaramPuram             R. YerramPalem 
##                        954                       3938 
##            R.Amadalavalasa               R.Bhimavaram 
##                        844                        291 
##              R.J.Boddapadu              R.Jambuldinne 
##                        568                        879 
##                R.K.M.PURAM                R.K.V.B.PET 
##                        552                       2121 
##               R.Kontalpadu               R.Kothapalli 
##                       2370                        904 
##                  R.KOTTURU             R.KRISHNAPURAM 
##                        556                       2224 
##               R.MALLAVARAM               R.Papampalle 
##                       5115                        596 
##                  R.V. Ngar              R.Venkamapata 
##                       1761                        555 
##              R.Y.Agraharam                R.Y.NAGARAM 
##                        466                        346 
##                RAACHAPALEM               RaagSamudram 
##                       1017                        597 
##                Raaj Koduru             RaajaiahPettah 
##                       1345                       4133 
##                 RaajaPalem                RaajaPettah 
##                       1751                       1640 
##                 RaajaPuram                  RaajVaram 
##                       2849                       3133 
##            RaamGopalapuram              RaamRoyapuram 
##                        273                        240 
##               RaamSamudram                 Rachakonda 
##                        675                       1124 
##               Rachanapalli             Rachannagudena 
##                       5263                        378 
##                 Rachapalle                RACHAPALYAN 
##                      12176                        537 
##                Rachapatnam                  Rachapudi 
##                        814                       1952 
##               Racharipalem            RACHAVARI PALLI 
##                       1838                        382 
##                 RACHAYAPET                 Rachepalli 
##                       2023                       2791 
##                   Racherla        Racheruvu Rajupalem 
##                       4463                        260 
##              Rachgudipalli                 Rachgumdam 
##                       1652                        287 
##            Rachinnayapalli                 Rachkindam 
##                        626                        534 
##       Rachur-NaraNagePalli                    Rachuru 
##                        501                       1052 
##              Rachwaripalli          RadhakrishnaPuram 
##                       1026                        278 
##         RADHAVALLABHAPURAM                RAGANIPALLI 
##                        425                       1787 
##              Raghanampalli               Raghavapuram 
##                        572                       3297 
##               RAGHAVAPURAM               RaghavPatnam 
##                       2173                        491 
##                Raghavpuram            RaghavRajapuram 
##                        164                       1892 
##              RaghoDeoPuram              Raghunadpuram 
##                       6134                        171 
##           RAGHUVARAJUPALLE           RAGHVARAJA PURAM 
##                        423                        489 
##                 RAGI GUNTA            Ragi manu penta 
##                        976                       2141 
##              Ragimanipalle              Ragimanumitta 
##                        964                        441 
##                     Ragolu                 RagulaPadu 
##                       2538                       1271 
##              Rahiman Puram             Rahimana Puram 
##                        512                        309 
##                 RAIDU PETA                    RAIWADA 
##                        470                       1660 
##               RAJA NAGARAM           RAJAGOPALA PURAM 
##                        524                        642 
##            RajagopalaPuram                Rajahmundry 
##                        498                     199018 
##       Rajahmundry pattanam                     Rajala 
##                      37887                        162 
##           Rajala Agraharam                     Rajali 
##                       1682                        358 
##                      Rajam                 Rajampalli 
##                      13191                       1755 
##                   Rajampet                Rajanagaram 
##                      29219                       7025 
##                RAJANAGARAM                  Rajapalem 
##                       1265                        909 
##      RAJAPATRUNIVANI PALEM                   Rajapudi 
##                        807                       4579 
##                 Rajapulova                  Rajapuram 
##                       1415                        419 
##                  RajaPuram               RAJARAMPURAM 
##                       1682                        708 
##                  Rajavaram                  RAJAVARAM 
##                       3739                        622 
##                   Rajavolu                   RAJAVOLU 
##                       3637                       1111 
##               RAJAVOMMANGI                RAJAYYAPETA 
##                       3354                       1310 
##             RAJENDRA PALEM                     Rajeru 
##                        513                       1050 
##  Rajiv Colony-AnantaPuram(                RAJIV NAGAR 
##                       4530                      18526 
##                 Rajolupadu                 RAJU PALEM 
##                        403                        759 
##                 Raju palli                  RajuKunta 
##                       1254                        789 
##                RAJULA PETA         Rajulaguruvaypalli 
##                        496                        769 
##             RAJULAKANDRIGA               Rajulgummada 
##                        400                        664 
##                 RajulPalem                  Rajupalem 
##                        851                      13507 
##                  RAJUPALEM     Rajupalem Lakshmipuram 
##                        837                       1265 
##                    Rajupet                   Rajupeta 
##                       2572                       1860 
##             RAJUPOTHEPALLI       Rajuwarichintalpalem 
##                        929                       1272 
##          RajyaLakshmipuram                    Raketla 
##                       1319                       3139 
##                     Rakodu                Ralla Palli 
##                       1487                        591 
##              Rallabuduguru          Rallacheruvupalli 
##                       1798                        354 
##                 Ralladoddi             Rallagodyvlasa 
##                        575                        461 
##                RALLAKOTHUR                RALLAKUNATA 
##                        403                        593 
##                RALLAKUPPAM            Rallanantapuram 
##                        261                       1184 
##                  Rallapadu                 Rallapalli 
##                        998                       3980 
##                  Rallapudi                  RAM PURAM 
##                        714                       1179 
##                  RAMA GIRI                 RAMA PURAM 
##                       1350                        551 
##               Rama teerthm           RAMABHADRA PURAM 
##                        832                        890 
##            Ramabhadrapuram          RAMACHANDRA PURAM 
##                        377                        526 
##           Ramachandrapuram           RAMACHANDRAPURAM 
##                      35234                        420 
##              RAMADASUPURAM                 RAMADURGAM 
##                        322                       1727 
##                   Ramagiri              RamaiahValasa 
##                       3085                       1135 
##              RAMAJOGI PETA           Ramakrishnapuram 
##                        303                       4481 
##           RAMAKRISHNAPURAM                 Ramakuppam 
##                       1615                       4219 
##                   Ramakuru             Ramalingapuram 
##                       2374                       2222 
##             RAMALINGAPURAM                Ramallakota 
##                       1203                       2698 
##                RAMANA PUDI                Ramanagaram 
##                        365                       4150 
##            RamanaiahPettah               Ramanakkapet 
##                        939                       3904 
##                Ramanapalli              RAMANAYYAPETA 
##                       2179                      22284 
##               RAMANJUPALLE               Ramannagudem 
##                        315                        817 
##              Ramannagudena               Ramannapalem 
##                       2041                        607 
##               RamannaPalem              Ramannapalena 
##                        549                       2834 
##                 Ramannapet              RAMANNAVALASA 
##                        919                        253 
##             RAMANUJA PALLI       Ramanuja Vartalpalli 
##                        897                        360 
##              Ramanujapuram               Ramanujulpet 
##                       2112                        253 
##           Ramanuthalapalle                  Ramapuram 
##                        517                      10140 
##                  RAMAPURAM               Ramaraogudem 
##                       3770                       1147 
##              RAMASAMUDHRAM               Ramasamudram 
##                        890                        909 
##               Ramasingaram             RAMASINGAVARAM 
##                        653                        460 
##              RamasvamiPeta                  Ramavaram 
##                        503                       8747 
##              Ramavarappadu             RamavarapuModi 
##                      15152                        626 
##                Ramayapalem                RAMAYAPALEM 
##                        225                       2148 
##                Ramayapalli               Ramayapatnam 
##                        175                        599 
##                Ramayavlasa                Rambadrapur 
##                        267                       8260 
##              Rambadrapuram            RAMBHADRA PURAM 
##                        267                        350 
##           Rambhadrunipalle             Rambhotlapalem 
##                        157                       2032 
##                   Rambilli          Ramchandrayapalli 
##                       7146                        522 
##            Ramchandrunipet             Ramdevula Padu 
##                        494                        142 
##                Rameshwaram                 Rameswaram 
##                       2731                       4142 
##             RAMGANADAPURAM             Ramgopalapuram 
##                        572                        439 
##             Ramireddipalli            ramireddy palli 
##                       1295                        830 
##         RAMIREDDYGARIPALLI             Ramireddypalli 
##                       1144                        982 
##            RAMIREDDYPALLLI                   Ramkonda 
##                        259                        651 
##            RAMKRISHNANAGAR           Ramlingaiahpalle 
##                        812                       1532 
##                Ramnaiahpet                  Ramngaram 
##                        288                        264 
##                      RAMPA            RAMPACHODAVARAM 
##                        545                       4634 
##                    Rampadu                   Rampalli 
##                        354                       2079 
##                   RAMPURAM               Ramrajulanka 
##                       3244                       3483 
##               Ramrajupalem               Ramrajupalli 
##                        698                       2646 
##                  Ramsagram                  Ramtirdam 
##                       1658                        831 
##               RamuduValasa             RAMULDEVAPURAM 
##                        601                        676 
##                  Ramulvidu                       Rana 
##                        508                       1074 
##                RANAJILLEDA                 Ranasdhlam 
##                        721                       2036 
##             RANGA SAMUDRAM             RANGAIAH GUNTA 
##                       2723                        364 
##                RangamPalli                  Rangampet 
##                        862                       5914 
##            Ranganadhapuram              Rangannagudem 
##                        311                       1042 
##              Rangappavlasa                 Rangapuram 
##                        821                       7003 
##                 RANGAPURAM             Rangarayapuram 
##                       1428                       1766 
##             Rangarayipuram              Rangasamudram 
##                       1763                       5700 
##  RANGASAMUDRAM HARIJANAWAD                 RANGASEELA 
##                        587                       1128 
##               RANGELISINGI                 Rangepalli 
##                        473                        992 
##                    Rangoyi                 RANGUPURAM 
##                        623                        271 
##                 RAOUTUPETA                       RAPA 
##                        222                       1333 
##                     Rapaka                     RAPAKA 
##                       3178                       3575 
##                    Raparla                   Raparthi 
##                       3226                       2198 
##                   Rapthadu                     Rapuru 
##                      10410                       6518 
##                RASANAPALLI               RASOOL PALLE 
##                        643                        667 
##              Rastakuntubai                     Ratana 
##                        407                       2995 
##            Ratchamallipadu                Ratchumarri 
##                       1688                       4046 
##                 Rathakanna           Rathigunta pally 
##                       2713                        575 
##              RathnamPettah                  Ratnagiri 
##                        303                       4161 
##                RATNAM PETA                 RatnaPalle 
##                       1493                       1176 
##                      Ratti                    RATTINI 
##                        833                        614 
##                RautuKuntla                 RautuPuram 
##                       1496                        384 
##                     Ravela                Ravichandri 
##                       3115                        413 
##                 Ravicharla                  RAVIGUDEM 
##                       1122                        458 
##             Raviguntapalli                Ravikampadu 
##                        856                       4917 
##             RAVIKANTI PETA                  Ravikmtam 
##                        381                       2955 
##        RAVILLA VAARI PALLI                  Ravimetla 
##                        530                       3576 
##                 RAVINUTALA                   Ravipadu 
##                       4769                       7852 
##                   RAVIPADU                  RAVIPALEM 
##                       1413                        280 
##                   Ravirala                  Ravivlasa 
##                        552                       4006 
##                 Ravnapalli                     Ravudi 
##                       1216                       2231 
##              RavulaCheruvu               RavulaKolanu 
##                       3171                        614 
##                RavulaKollu             RAVULAMMAPALEM 
##                        629                       1776 
##                 Ravulapadu                Ravulapalem 
##                        174                      21530 
##                Ravulapalli                Ravulapuram 
##                       1062                       1624 
##               RavulaValasa                 Ravulparru 
##                        743                       1345 
##                 Ravuludiki                     Ravuru 
##                       1543                        985 
##                 RAVURUPADU                     Rawada 
##                        311                       1886 
##                  Rayachoti    RayaDurgam Munisipaliti 
##                      62212                      41164 
##                 RAYAKUDURU                 RAYAL PETA 
##                       5258                       1663 
##                     Rayala             RAYALA CHERUVU 
##                        482                        786 
##                    RAYALAM       RAYALAPANTHULA PALLE 
##                       5387                        318 
##               Rayalcheruvu                Rayam Palli 
##                       3706                        882 
##                 Rayanapadu              Rayannapalena 
##                       2471                        673 
##                  RAYAPALLI                   RAYAPEDU 
##                        963                        644 
##                   Rayapudi         RAYAPURA AGRAHARAM 
##                       2289                        882 
##          RayapuRaju Pettah                  Rayavaram 
##                       1889                      10907 
##              RAYAVARIPALLI            Raybhupalpatnam 
##                        437                       3105 
##                  Rayindram               Rayni Pettah 
##                        380                        394 
##   Rayudappa Rangarayapuram                     Razole 
##                       1020                      10067 
##                RazooPettah                    Rebaaka 
##                        783                       1425 
##                     REBAKA                     Rebala 
##                        370                       4533 
##                REDDI PALLI                 Reddigudem 
##                        950                       5983 
##               REDDIKOPALLI            REDDINAGAMPALEM 
##                        248                        330 
##         Reddipalem Bit - 1          Reddipalem Bit -2 
##                       1369                        557 
##                 Reddipalli       REDDIPALLI AGRAHARAM 
##                       8888                       3461 
##             Reddiwaripalli               Reddla palli 
##                       1427                        262 
##           REDDY VARI PALLI                 REDDYPALLE 
##                        626                        578 
##                       REGA            Regadadinepalli 
##                       2402                        283 
##           Regati Agraharam                Regdiguduru 
##                        512                       3957 
##                     Regidi                   Regpalem 
##                       1113                        148 
##                  Regubilli               Regulchilaka 
##                        388                        191 
##                  Regulpadu                   REGUPADU 
##                       1833                        671 
##                  Regupalem              RekaDevyPuram 
##                       3124                        276 
##                 Rekhapalli             Rekhavanipalem 
##                       1164                       3621 
##                  Rekkamanu                  Reklkunta 
##                       1132                       2206 
##   Rekulkunta h/oReddipalli                      Rella 
##                       2151                        467 
##                      RELLI        Relli GavaraMmaPeta 
##                        833                        938 
##                 Rellivlasa                 Rellugadda 
##                       4662                        711 
##                    Relnagi                    Remalli 
##                       6039                       2444 
##                     Remata               Remidicherla 
##                       2742                       2192 
##               Renangiwaram        RENIGUNTA AGRAHARAM 
##                        487                       7306 
##           Renimakula Palli             Renimakulpalli 
##                       1212                       1527 
##                  Renimdugu              Rentachintala 
##                        230                       8523 
##                    Rentala              RENTALA CHENU 
##                       1991                        460 
##                 Rentapalla                  Rentikota 
##                       2341                       2435 
##                     Repaka                Repakagommu 
##                        557                        706 
##                    Repalle                REPALLEWADA 
##                      18840                        409 
##  REPALLIWADAH/O.PRAGADAPAL                     Repudi 
##                        387                       1503 
##                     Repuru                     Returu 
##                       3666                       1240 
##              Revalla Palem      Revallerragunta Palem 
##                        756                        631 
##                    Revallu                    Revduru 
##                       1080                        649 
##                     REVIDI                   Revnooru 
##                       1315                       1355 
##                 Revulakota                  ReyCharla 
##                        400                       1701 
##          ReyGadi Kanapuram               ReyGatiPalle 
##                        670                       1575 
##                  REYYIPADU                Rimmanapudi 
##                        706                        666 
##                    Rintada         RIPUNJAYARAJAPURAM 
##                       1431                        946 
##                  RITTAPADU                     Roddam 
##                        312                       5235 
##                roddavalasa                      Rolla 
##                        640                       5798 
##       Rolla Buduguntapalli                 Rollamdugu 
##                        285                        468 
##                  Rollapadu                  ROLLAVAKA 
##                        779                        192 
##                ROLUGUMPADU                  ROLUGUNTA 
##                        240                       3135 
##                    Rolupdi                   Rompalli 
##                       1140                       1414 
##                   ROMPALLI                      Rompi 
##                       1151                        107 
##                Rompicharla                 Rompivlasa 
##                       3748                       1440 
##                    Rompulu         RONGALI NAIDUPALEM 
##                       1382                       1248 
##                   Rosnooru                 Rotripuram 
##                       1155                       1674 
##                 Rottavlasa                    Rouduru 
##                       1095                       1123 
##                 Routulpudi             Rowthusuramala 
##                       6017                        217 
##                 ROWTUGUDEM                    Royyuru 
##                        601                       1756 
##                     RPalli                   RUDAKOTA 
##                       2015                        481 
##                  RudraCoat                Rudramapeta 
##                       4073                       9481 
##   Rudrampeta, Kakkalapalli                  Rudrapaka 
##                       8282                        580 
##              RudraSamudram                 Rudravaram 
##                       1309                      10795 
##                 RUDRAVARAM                     RUGADA 
##                       5307                        795 
##     runku hanumanthu puram                 Rupanagudi 
##                       1103                        523 
##               Rupenaguntla                 Rushikonda 
##                       3555                       2419 
##                 Rushikudda                  Rushinagi 
##                        300                        384 
##                 Rustumbada                      Ryali 
##                       3322                       8565 
##                S B R PURAM               S EddaValasa 
##                       2231                        821 
##            S R N AGRAHARAM               S Uppalapadu 
##                        642                       1607 
##                  S V PURAM              S. Kondapuram 
##                       2464                       1516 
##              S. Kothapalle              S. Kothapalli 
##                        261                        313 
##             S. Lingamdinne              S. MUPPAVARAM 
##                        747                       1083 
##                 S. MYDUKUR             S. Nagalapuram 
##                      14801                        821 
##               S. Rajampeta               S. RAMAPURAM 
##                       1155                       1990 
##          S. RANGARAYAPURAM               S. Rayapuram 
##                        460                        996 
##               S. Rayavaram             S. Thimmapuram 
##                       3993                        763 
##                  S.A.Puram                S.Agraharam 
##                        610                       1924 
##                S.Annavaram              S.BANDA PALLI 
##                       7052                       1487 
##              S.BURJAVALASA             S.CHENNAMPALLE 
##                        483                        164 
##            S.ChintalValasa              S.Coat Talari 
##                        389                       1114 
##               S.Gollapalle             S.Govindapuram 
##                        474                        247 
##            S.Illindalparru                  S.J.Puram 
##                       1545                        808 
##               S.Kondapuram                S.Kondepadu 
##                       3894                        679 
##       S.KOTA SEETARAMPURAM                   S.Kothur 
##                        416                        852 
##              S.Lingandinne                  S.M.Puram 
##                       1067                       1551 
##            S.M.PURAM .PETA               S.NADIMPALLI 
##                        159                        637 
##               S.Narsapuram        S.P.Ramchandrapuram 
##                        901                        277 
##              S.Papanapalli                 S.Pydipala 
##                        187                       1258 
##                  S.R. Coat                 S.R.Pettah 
##                        160                       2761 
##                  S.R.PURAM                 S.S.B PETA 
##                       3222                       1734 
##                  S.S.PURAM                S.S.R.Puram 
##                       1491                        575 
##              S.T.Rajapuram              S.Thimmapuram 
##                       1590                        716 
##             S.Venkatapuram              saantaeswaram 
##                       1517                        411 
##           SAAVISETTY PALLI          Sabari Kothagudem 
##                        913                        305 
##                Sabashpuram                 Sabbavaram 
##                        860                       7786 
##                  Sabjapadu                    Sabkota 
##                        554                        536 
##                sada kuppam             SadanandaPuram 
##                        819                        336 
##             SADASIVA PURAM                SADHUKOTTAM 
##                        902                        328 
##                     Sadika                      SADUM 
##                       1886                       8487 
##                     SAGARA                    SAGARAM 
##                       1995                        653 
##                    Sagguru                   SagiPadu 
##                        219                        710 
##                   SAGIPADU                   Saguturu 
##                        564                        901 
##                  SahaPuram                  Saidepudi 
##                        100                        212 
##     Sailada, KummariPettah                   Sainooru 
##                       1285                        554 
##                  SaiPettah                   SaiPuram 
##                       3339                        428 
##                Sajaldinane              SAJJALAGUDDEM 
##                       3029                       1147 
##               Sajjalapalli                 SajjaPuram 
##                        318                        686 
##                 SAKHAVARAM             Sakhinetipalli 
##                       1537                       8092 
##    SAKTHI GANESHWARA PURAM                Sakulapalem 
##                       1086                        308 
##                   Sakunala                     Sakuru 
##                       1704                       1136 
##             SalakAla konda           SALAPUVANI PALEM 
##                        580                        985 
##                 Salempalem                 Salihundam 
##                       1692                       1075 
##                    Salipet             Salkam Cheruvu 
##                        395                       1916 
##                 Salkapuram                 Salknutala 
##                       1056                        586 
##                  Salnutala                    SALU RU 
##                        506                       3193 
##                     Salugu                     Saluru 
##                       2441                      25100 
##                   SAMAGIRI             Samaguttapalli 
##                       1114                       1496 
##                   SAMANASA              Samantamallam 
##                       2776                        611 
##               Samanthapudi                SamantKurru 
##                       1378                       1983 
##                  Samarelli               Samarla Coat 
##                        198                      24412 
##                  SamaVaram              SAMAYYAVALASA 
##                       1624                        779 
##                 Sambagallu             Sambaiah Palem 
##                        900                        787 
##                     Sambam                  Sambaturu 
##                        441                        713 
##                 Sambepalli               SAMEERAPALEM 
##                       1702                        535 
##            SAMIREDDY PALLE                 Sammatgiri 
##                        667                        502 
##                    Sampara              SAMPATHI KOTA 
##                       2028                        486 
##              Sampathipuram                 SAMUDAYAMU 
##                       1298                        505 
##               SAMUDRAPALLI            Sana Rudravaram 
##                        739                       1921 
##                   Sanagala                 Sanagapadu 
##                       2429                       1286 
##                   Sanakada                  Sanampudi 
##                        860                       8022 
##                     Sanapa                    Sancham 
##                       1709                        521 
##                  SANCHARLA                  Sandepudi 
##                        999                       1104 
##                 Sandhipudi                   Sandigam 
##                       1072                        391 
##                SANDRAPALLI              Sanewaripalli 
##                        506                        649 
##                    SANGADA                     Sangam 
##                       1016                       5927 
##          SangamJagarlamudi               SangamValasa 
##                       2218                       1556 
##              Sangana palli                Sanganpalli 
##                       1739                        527 
##                Sangapatnam                 Sangapuram 
##                       1499                        419 
##              SANGASAMUDRAM                Sangivalasa 
##                       1304                       3174 
##          Sangupalem Koduru                  SangVaram 
##                       1044                        485 
##                  Sanigudem                 Sanikwaram 
##                        505                       1504 
##                  Sanipalli                   Sanipaya 
##                       1095                       1909 
##           SanivarapuPettah                   Saniwada 
##                       5075                        492 
##                  Sanjamala          SanjeevaraoPettah 
##                       2647                       2306 
##               SANKALAPURAM               SankaraBanda 
##                        221                        471 
##              Sankaraguptam      SANKARALINGAMGUDIPADU 
##                       2060                       1268 
##                Sankarbanda             Sankarshnpuram 
##                        398                        365 
##                 Sankavaram                 Sankepalli 
##                       8544                       2765 
##    Sankepalli Brahmanpalli                Sankhavaram 
##                        490                       2747 
##                    Sankili                SanklaPuram 
##                        807                        852 
##             SankuRatriPadu                  Sannamuru 
##                       1159                        191 
##                 Sannavilli              Sanpallilanka 
##                       1070                       2448 
##             Sanrsiddamnugu              Santabommaali 
##                        469                       3630 
##                Santajuturu            SANTALAXMIPURAM 
##                       1340                        475 
##                    SANTARI               Santebidnoor 
##                       2291                       2633 
##       Santh Gavi AmMmaPeta              SANTH VELLURU 
##                       1142                       1561 
##                 SANTHABYLU             Santhagudipadu 
##                        738                       2590 
##              SANTHAKOVVURU              Santhamagalur 
##                       2332                       6150 
##          SanthanuthalaPadu                Santhapalem 
##                       6970                        803 
##                  Santhapet                 Santhapeta 
##                       5821                       2059 
##                Santharavur              Santhekudluru 
##                       2521                       2937 
##                Santhipuram                SanthKaviti 
##                       2232                        941 
##          SanthLakshmiPuram                   Santhuru 
##                        550                        480 
##                SantosPuram                  Santuriti 
##                        817                        720 
##                    Saparla                        Sar 
##                       1700                         86 
##            Sarabhannapalem               SARABHAVARAM 
##                       2074                       1910 
##                    Saradhi                  sarakallu 
##                       3474                        821 
##            SARAMATLA PALLI              sarasanapalli 
##                        388                        844 
##             SarasvatiPalli               SARAYAVALASA 
##                        771                        317 
##                Sarayivlasa                  Sarbwaram 
##                        488                       1963 
##                SardhaPuram                 Sariapalli 
##                        510                        629 
##                 SariaPalli                     Sarika 
##                        763                       1043 
##                     SARIKA             Sarikondapalem 
##                        684                        912 
##                 SARIMADUGU                  Sarimdugu 
##                        667                        557 
##                  Saripalli                  SARIPALLI 
##                       8131                       2931 
##                   Sarivela             Sariyaboddpadu 
##                        357                        460 
##                      Sarli                    Sarnagi 
##                        728                        214 
##              sarpaja puram                 SarpaVaram 
##                        857                       9921 
##                 Sarubujili                   Sarugudu 
##                        574                        891 
##                 SarvaSiddi               Sarvayipalli 
##                        828                        365 
##              Sarvepalli-11             Sarvepalli-111 
##                       2215                       1201 
##            Sarvereddipalem            SarveshwarPuram 
##                       1130                        225 
##                   Sarvkota         Sarwareddikandriga 
##                       2089                        758 
##                     Sasnam                SATHAMBAKAM 
##                        286                       1147 
##               sathani kota                sathanikota 
##                        564                        683 
##             Sathivanipalem                   SathiWad 
##                       1519                       2740 
##                      Sathu                  SathyaWad 
##                        403                       1328 
##              SATILITE CITY                   SATIVADA 
##                       8870                        549 
##                   Satnooru                 SATRAMPADU 
##                       1244                       3681 
##                  Satrawada               SATTENAPALLI 
##                       3948                      27878 
##              SATTENNAGUDEM                   Satuluru 
##                        401                       3538 
##                 SATYA VEDU         Satyajagannadpuram 
##                       6655                        223 
##                  Satyavada                 Satyavaram 
##                       1676                       5649 
##                 SATYAVARAM                  Satyavolu 
##                       1084                       3600 
##          SAVARA CHORALINGI  Savyasirajupur@Maripivlas 
##                        442                        841 
##     Sawar Ramakrishnapuram             Sawarbanapuram 
##                        190                        151 
##                 Sawarbontu             Sawarjadupalli 
##                        170                        132 
##            Sawarlingupuram                Sawarmmluva 
##                        336                        131 
##              Sawarrampuram                 Sawarvilli 
##                         98                       1448 
##                     Sawrna                 SAYAMPALEM 
##                       4641                        414 
##                       Seal               Seegalapalli 
##                       2444                        823 
##                    SEEKARI                   seepuram 
##                       1593                        291 
##              SEESAMGUNTALA                 SEETAMPETA 
##                        810                        444 
##               Seetanapalli              SEETAPPAGUDEM 
##                        588                        262 
##                 seetapuram      Seetarama puram Tanda 
##                        666                        333 
##             SEETARAMAPURAM             Seetaramunipet 
##                       4960                       1091 
##            SEETHADEVIPURAM                Seethampeta 
##                        186                       1530 
##                SEETHAMPETA              SEETHAMVALASA 
##                        306                        223 
##              Seethanagaram              SeethaNagaram 
##                       8286                       4171 
##              SEETHANAGARAM                SEETHAPALLI 
##                        685                       1050 
##                Seethapuram                SEETHAPURAM 
##                       1204                        960 
##           SEETHARAMA PURAM         Seetharamana-garam 
##                        464                        339 
##            Seetharamapuram            SEETHARAMAPURAM 
##                       3950                       2150 
##              Seetharampeta          SeethayammaPettah 
##                        396                        509 
##                     Sekuru             SeriGolvepalli 
##                       4600                        965 
##         Serinarasannapalem                  Seripalem 
##                        837                       1353 
##                    Seripet          SESHANNAGARIPALLI 
##                        453                        281 
##           SESHAREDDY PALLI               SETARAMPALLI 
##                        177                        769 
##                    setteri                 Settigunta 
##                        885                       2872 
##                 SettiPalem                 Settipalli 
##                        901                       1504 
##                 SETTIPALLI                  SETTIPETA 
##                       1910                        891 
##             Settiwaripalli                SettyPettah 
##                       3747                       2450 
##             SETTYVARIPALLI               Setubimwaram 
##                        608                        380 
##           SeyRi Amaravaram           SeyRi Daggumilli 
##                        443                        997 
##           SeyRi Dintakurru          SeyRi Vartalpalli 
##                        395                        280 
##               SeyRi Velpur                  Shahpuram 
##                        714                       1295 
##               SHAKARAPURAM                 Shakhamuru 
##                        409                        757 
##              Shakunalpalle                  Shalantri 
##                        582                        585 
##                 Shalklvidu                   Shambara 
##                       1093                       2568 
##               Shanayapalem               Shanglguduru 
##                        610                       3002 
##                 Shaniwaram                  Shankaram 
##                       2097                        505 
##               Shankaraoram              SHANKARAPURAM 
##                        310                       1342 
##          SHANKARAYALA PETA              ShankeraPuram 
##                       1380                       2118 
##              Shantanvalasa                shantinagar 
##                        653                        149 
##                     SHARAI      Sharbhabhupala Patnam 
##                        999                        820 
##                   Shashnam               Shashnapalli 
##                       1338                        480 
##                 Shashnkota                    Shasnam 
##                       1798                        548 
##              shathani kota                   Shatkodu 
##                        121                        711 
##            ShayamRajapuram               sheela nagar 
##                        799                       1293 
##             Shekshanipalli       Sher Mohammad Pettah 
##                       1955                       2886 
##             Sherikalvapudi             Sheshadripuram 
##                       1068                         85 
##           Sheshamambapuram                Shettipalle 
##                        695                       6236 
##            Shettivaripalli                 Shettividu 
##                        733                       1487 
##           Shettiwarigudena                   Shetturu 
##                        335                       2779 
##            Shiddanakonduru             Shiddaracherla 
##                        712                       1017 
##                Shiddawaram                 Shigipalli 
##                       1370                        793 
##               Shikaruganji                  Shikharam 
##                        461                       1603 
##                    Shilgam               Shimunapalli 
##                        456                        745 
##               Shingagudena            Shinganalathuru 
##                        987                        788 
##                 Shinganmal             Shingannapalem 
##                       2977                        730 
##               Shinganpalli        Shingarabhotlapalem 
##                       1353                        763 
##           Shingarajanhalli           Shingareddipalle 
##                        290                       1926 
##                Shingawaram              Shirigiripadu 
##                       2175                       3848 
##                 Shirivella                 Shiriwaram 
##                      11570                        774 
##            Shitanagulwaram                    Shivala 
##                        982                       1026 
##            SHIVALINGAPURAM                ShivalPalli 
##                       1314                        822 
##             ShivannaPettah                 Shivapuram 
##                        415                        943 
##                   Shivaram              ShivaramPuram 
##                        854                       2417 
##                 Shivdvlasa          ShivramDurgapuram 
##                       1251                        323 
##             ShivramRajupet                   Shiwaram 
##                        816                       3259 
##                      Shobh          Shotriyam Gundala 
##                        237                        478 
##           Shotriyam Valasa            Show.Markapuram 
##                        626                        242 
##          ShreepatiR Pettah                SHRISHAILAM 
##                        584                       4190 
##           SHUBALAYA COLONY                  Shubhadra 
##                       1437                        911 
##              ShuvarnaPuram                Shyam Puram 
##                        872                        388 
##            Shyamlambapuram          Shyamsundarapuram 
##                        225                        352 
##                    Sibyala                SIDDA VARAM 
##                       2768                        559 
##               SiddaAmPuram         Siddakinchayapalli 
##                       3037                        273 
##           Siddamurthypalli                Siddantham, 
##                        339                        306 
##                 Siddapuram                 SIDDAPURAM 
##                       3886                       1006 
##              SIDDARAMPURAM                 Siddavaram 
##                        976                        665 
##                 SiddaVaram                 Siddavatam 
##                       1472                      10792 
##                 SiddePalle                Siddhagunta 
##                        978                        453 
##        SIDDI RAJU KANDRIGA          Siddibeharkothuru 
##                        760                        424 
##                   Siddigam                 SIDHANTHAM 
##                        191                       6307 
##                       Sidi                    Sidrhal 
##                       2411                        170 
##               Sihech.Ganum         Sihech.N.Agraharam 
##                       1615                       1092 
##           Sihech.Potepalli                     Sikbdi 
##                        739                       1081 
##        SILAGAM SINGUVALASA                Sileru U.I. 
##                        933                       2113 
##                     Silgam              Simhadripuram 
##                       2351                       3505 
##             SIMHARAJAPURAM                  SinduWad, 
##                        268                        709 
##           SINGAMANENIPALLI                Singampalle 
##                        324                       2762 
##                Singanhalli                 Singanmala 
##                       1907                        672 
##              Singannabanda          SINGANNADORAPALEM 
##                        575                       1576 
##              Singannagudem              Singannapalem 
##                       1035                        453 
##              Singannavlasa            SINGANODDIPALLI 
##                        386                        554 
##                 Singanpudi                  Singapeta 
##                        777                       2386 
##            Singaraju Ralle              Singarampalem 
##                        716                        489 
##               Singarapuram             SINGARAYAPALEM 
##                        433                        333 
##             Singarayapalli                  Singarayi 
##                        415                        990 
##                  Singarbha            Singareddipalli 
##                       1658                       1173 
##              Singasamudram                 Singavaram 
##                        905                       2403 
##                    Singidi               SINGIRIGUNTA 
##                        259                        468 
##                 Singupalem                 Singupuram 
##                       1225                       5164 
##                 SINGUPURAM                    SINGURU 
##                        981                        591 
##                     Sipudi              Siragalapalli 
##                        738                        959 
##                    SIRAGAM               Sirangipalem 
##                        409                        651 
##              SIRASANAMBEDU                 Siriakandi 
##                       1290                        189 
##            SIRIGINDALAPADU              Sirigiripalli 
##                       1039                        752 
##                    Sirihli                    SIRIJAM 
##                        247                        862 
##               SIRIKI PALEM                  Sirikonda 
##                        606                        143 
##                 SiriMamidi                  SiriPalli 
##                        756                       1305 
##                   Siripudi                  Siripuram 
##                       1062                      10711 
##                  SIRIPURAM                  SiriVaram 
##                        503                       3102 
##                    SiriWad                Siriyawaram 
##                        907                        377 
##                     Sirlam                 SIRLAPALEM 
##                        856                        695 
##                SIRUGAPURAM           SIRUGURAJUPALYAM 
##                        326                        624 
##              SIRUNAMBUDURU                 Sirusuwada 
##                        593                       1369 
##                      Sisli  SITAMPET H/O.BAYYANAGUDEM 
##                       2951                       1106 
##                SITANAGARAM                  Sitapuram 
##                       1824                        349 
##               Sitarampuram   Sivada (Gujuvayi Daggar) 
##                       2695                        935 
##        Sivadevuni Chikkala                   Sivakodu 
##                       2265                       4433 
##            Sivanadha Palem                  Sivapuram 
##                        938                       2806 
##                  SIVAPURAM              Sivaramapuram 
##                       1402                        961 
##               Sivarampuram                  Sivavaram 
##                        473                        913 
##                     Sivini               SIVUNIKUPPAM 
##                       1008                        669 
##                     Sivvam                    Sivvamu 
##                        434                        967 
##                 Siwarampur                Skat Pettah 
##                       1327                        220 
##                  SOBHAKOTA               Sobhanapuram 
##                       1229                        303 
##               Sodana Palli                      SODHA 
##                       1394                        625 
##             Sodigani palli                Sogadaballa 
##                       1105                        377 
##                    Soganur                SOKULAGUDEM 
##                       1376                        118 
##                   Solabham                     Solasa 
##                        740                       1563 
##                   Solikiri           Solipisomrajupet 
##                       1056                        634 
##                 Sollapuram                      SOMAL 
##                       1389                       4903 
##                Somaladoddi                SomalaPuram 
##                       2034                       1003 
##               SomalReyGadd               Somandepalli 
##                        660                      11174 
##               SOMANNAPALEM                  Somapuram 
##                        675                        392 
##                  SOMAPURAM              Somarajupalli 
##                        589                       2137 
##              SomarajuPalli             SomarajuPettah 
##                       1560                        355 
##                   Somasila              Somavarappadu 
##                       2183                       2928 
##           Somayajula Palem            Somayajulapalle 
##                        251                        773 
##            SomayajulaPalle                 Someswaram 
##                       1245                        370 
##                 SOMESWARAM                   Somgandi 
##                       4316                        779 
##                   SomGatta              SomiDeviPalli 
##                       1065                        555 
##             SomireddyPalli               SomitraPuram 
##                       7931                        616 
##              Somlingapalem              Somlingapuram 
##                       1790                        856 
##                   SOMPALLE                   Sompalli 
##                       2623                       1711 
##                    Sompeta                   SomPuram 
##                       9289                       1254 
##               SOMRAJAPURAM                SomSamudram 
##                        600                        281 
##               Somsanigunta            Somulavaripalli 
##                        846                       1488 
##                Somulgudena                   SomVaram 
##                        361                       6273 
##               Somwarappadu                 Somwaripet 
##                        970                        371 
##             Somyjula Palli                  Sondipudi 
##                       1199                        849 
##                  Sontivuru                    SONTYAM 
##                        186                       1673 
##                  SoorVaram                     Soperu 
##                        673                        323 
##           SORAKAYALA PALEM             SORAKAYALAPETA 
##                        454                        803 
##           Sorkayala Pettah                   Sorligam 
##                        436                        625 
##              SOUTH ADDANKI                     SOWDAM 
##                       3266                        569 
##                 Sowdrdinne               Sowt Amuluru 
##                        788                       1268 
##                Sowt Mopuru             Sredhar Ghatta 
##                       3204                       3108 
##                 SREEKOLANU               Sreeramagiri 
##                       1385                        766 
##              SRI HARIPURAM            SRI RANGA PURAM 
##                       1319                       1545 
##               Sridhanmalli                   Sridhara 
##                       1894                        326 
##                Sriharikota               Sriharipuram 
##                       2087                        331 
##           Srijagannadpuram                 Srikakulam 
##                        990                      66244 
##           Srikakulam Tounu               SRIKALAHASTI 
##                       9112                      50187 
##        SRIKAVERI RAJAPURAM                  Srikurmam 
##                        615                       9795 
##         SrimanarayanaPuram       Srinenkateshwarpalem 
##                        428                        658 
##            SRINIUVASAPURAM            SRINIVASA PURAM 
##                       1383                        792 
##             srinivasapuram             Srinivasapuram 
##                         94                        437 
##             SRINIVASAPURAM        SRINIVASAUDASIPURAM 
##                       2119                        480 
##           Srinivasavapuram         Srinivascharyulpet 
##                       3308                        903 
##                Srinivaspur                   Sriparru 
##                        698                       2603 
##                   Sripuram               SRIRAMAPURAM 
##                        486                        410 
##               Sriramavaram               SRIRAMAVARAM 
##                       1031                        384 
##                Srirampuram             SRIRANGAMPALLI 
##                       3328                        549 
##              Srirangapuram           Srirukhminipuram 
##                        558                       1093 
##                 Srngawaram         SROTRIYA RAMAPURAM 
##                        652                        334 
##              Srungarapuram          Srungarayanipalem 
##                       1174                       1121 
##                SrungaVaram                SRUNGAVARAM 
##                       1524                        776 
##           Srungavarapukoda             SrungaVruksham 
##                      13761                       3126 
##             SRUNGAVRUKSHAM  SRUNGERI RAJASEKHARAPURAM 
##                       5193                        621 
##     State - Andhra Pradesh        steelplant township 
##                     183239                       3660 
##               Subadrapuram                Subbamapata 
##                        914                        372 
##         SUBBANNAGARI PALLI              SubbaR Pettah 
##                        597                        453 
##               Subbayagudem              SubdharaPuram 
##                        554                        193 
##             Subhadramapata         SUBHANAIDUKANDRIGA 
##                        904                        847 
##            Subramanyapuram                Sudanugunta 
##                        789                        734 
##         SUDDA GUNTLA PALLI                 Suddagudem 
##                        603                        437 
##                 Suddamalla                 Suddapalle 
##                       2028                       3251 
##                  Sudepalli                SUDHIVALASA 
##                       1268                        907 
##                    Sudigam                  Sudikonda 
##                       1236                        598 
##            Sudireddy Palle               SUGALI METTA 
##                        613                        450 
##               Sugalithanda                 SugguPalli 
##                        204                        507 
##                     Suguru              SUJATHA NAGAR 
##                       2200                       3021 
##               SUJTHA NAGAR                 Sukumamidi 
##                       4625                        167 
##                     SUKURU                   Sulekeri 
##                       1697                        886 
##             Sulltana Puram                 Sullurupet 
##                        626                      23361 
##  Sultan Nagaram Gollapalem                   Suluvayi 
##                       2653                       1231 
##               Sumantapuram                  Sundarada 
##                        258                       1889 
##           SundaraiahPettah               SundaraPalli 
##                       1204                        673 
##            SUNDARAYYA PETA                 Sundipenta 
##                        327                      11195 
##                SundraPuram                Sundruputtu 
##                        395                       1411 
##                 SUNDUPALLI                  Sunkapuru 
##                       7953                        271 
##               SUNKARAMETTA               SunkaraPalem 
##                       1351                       1878 
##               SUNKARI PETA                 Sunkeshula 
##                        883                       1140 
##                Sunkeshwari                  Sunkesula 
##                       1688                       3566 
##                      Sunki                   Sunkollu 
##                        925                        601 
##                    Sunnada                  Sunnadevi 
##                        690                        494 
##                 Sunnampadu                 SUNNAMPADU 
##                        239                        400 
##                SunnamPalli          Sunnapurallapalli 
##                       1753                        735 
##                    Surabhi                   SURAMALA 
##                       4394                        399 
##                 SURAMPALEM                 Surampalli 
##                       1000                       4765 
##                  Surampeta                SuramPettah 
##                        671                        240 
##                  Surampudi              Surappagudena 
##                        585                       1770 
##               SURAPPAKASAM                  Surapuram 
##                       2158                        216 
##                  Suravaram           SURAYANARAPAURAM 
##                        695                        156 
##                Surayapalem               SUREDDYPALEM 
##                       1040                        849 
##            SURENDRANAGARAM                  Surepalli 
##                        998                       3458 
##                    Surjini         Surrappagari palli 
##                        274                        401 
##                Sursenyanam               SURUTUPAL LI 
##                       1703                        558 
##               Surwaripalli       SURYA NARAYANA PURAM 
##                        586                        224 
##              Suryamnipuram             Suryaraopalena 
##                        236                       1324 
##               SURYARAOPETA                    Susuram 
##                      16770                       1354 
##             SvayamBhuVaram                 Swarigudem 
##                        403                        751 
##    SWARNA LINGESWARA PURAM              SWARNAJIPURAM 
##                        339                        971 
##            SWARNAVARIGUDEM            Syamalambapuram 
##                        845                        409 
##                  Sydapuram                  SYDAPURAM 
##                       3126                        768 
##             Syngarayapalem                    SYRIGAM 
##                       1066                       1087 
##              T C AGRAHARAM          T PASAVANDA PALLI 
##                        825                       1184 
##          T SANDRAVARIPALLI                  T Sunduru 
##                        858                       4427 
##                T Sunkesula              T V R B PURAM 
##                        422                       1821 
##               T. Arjapuram              T. Gannavaram 
##                       2585                        394 
##              T. Kopparpadu              T. Kothapalem 
##                        916                       3054 
##                 T. Kottala             T. NARASAPURAM 
##                        314                       4756 
##                T. S. Puram                   T. SADUM 
##                        381                       1639 
##             T. Sallakullur             T. SUNDU PALLI 
##                        787                       1576 
##            T. Takkellapadu                T.Chadamuru 
##                        225                        805 
##            T.Chavata palli              T.D.Parapuram 
##                        826                        385 
##                 T.D.Pettah            T.GANGANNAGUDEM 
##                       2778                        380 
##                T.Gokulpadu               T.Jaggampeta 
##                       1361                        481 
##                 T.K.M.PETA              T.K.RAJAPURAM 
##                        356                        350 
##               T.Kothapalli              T.Lingandinne 
##                       4285                        878 
##                 T.N.KUPPAM                    T.ODURU 
##                        565                        937 
##                   T.P KOTA              T.P.Guduru-11 
##                       1251                       2868 
##                  T.puthuru               T.R.Kandriga 
##                       1897                        846 
##                T.R.Rajupet                    T.Sadam 
##                        333                       2845 
##                T.Sakibanda            T.SAKIREVUPALLI 
##                        351                        719 
##         T.SALLABASAYAPALLI            T.SALLAGIRIGELA 
##                        370                        947 
##                 T.Samudram                 T.Shashnam 
##                       2698                        169 
##          T.Sihech.R.Palena             T.Somalaguduru 
##                        961                       2859 
##            T.SOWDASAMUDRAM          T.Velamavaripalli 
##                        867                       2613 
##                    TAARUVA       TAATI THOPU KANDRIGA 
##                        289                        714 
##                   Tab Jula                       Tada 
##                       1338                       2717 
##                     TADAKA                    Tadanki 
##                        393                       1663 
##                  Tadepalle                  Tadepalli 
##                        129                      39482 
##                  TADEPALLI             Tadepalligudem 
##                       1069                      40190 
##            Tadepalligudena                     TADERU 
##                       2271                       2658 
##                       Tadi                  Tadigdapa 
##                       1045                       9810 
##                  Tadigotla                  Tadigummi 
##                       1948                        590 
##               TADIKALAPUDI                   Tadikona 
##                       2050                       1133 
##                  Tadikonda                  Tadimalla 
##                      10823                       4759 
##                  Tadimarri                   Tadimedu 
##                       3234                        326 
##                   Tadinada             Tadindoravlasa 
##                       4027                        208 
##                  Tadipalli                  Tadiparru 
##                        657                       2664 
##                   Tadipayi                   Tadipudi 
##                        151                        717 
##                 TADIVALASA                   Tadiwada 
##                       1889                        229 
##              Tadiwaripalli                Tadkandriga 
##                        437                       3205 
##                 Tadknpalle                    Tadpala 
##                       1771                       1997 
##                  Tadparthi                   Tadpatri 
##                       9955                      68408 
##                    Tadu Ru                      TADUR 
##                        267                        529 
##                    Tadutla                   Taduvayi 
##                        761                       4981 
##                Tagarampudi             Tagarapuvalasa 
##                       1460                       5855 
##                 Tagguparti                   Taipuram 
##                       1302                        536 
##                    Tajangi                 Tajyampudi 
##                       2436                       3287 
##         Takatyalbrhampuram               Takkellapadu 
##                        260                       4060 
##                    Takkolu                     Talada 
##                       1176                        750 
##                     TALADA              Talagadadeevi 
##                        374                        825 
##               Talam Kaluva                 Talamanchi 
##                        843                       3450 
##           TalamanchiPatnam                  Talamarla 
##                        805                       3730 
##                   TALAPULA              TALARICHERUVU 
##                       2741                        750 
##               Talarisinagi            Talarivanipalem 
##                        829                       1083 
##               Talarlapalli                     Talgam 
##                       2058                       1967 
##             Tali Agraharam                Talla Badra 
##                        634                        983 
##                 TALLABADRA                Tallaburidi 
##                       1720                       2014 
##               TallaCheruvu                 Talladumma 
##                       2722                        611 
##             Tallagokavaram                 TALLAGUDEM 
##                        350                        348 
##                  Tallakera             Tallakondapadu 
##                       2787                        815 
##                 TallamPadu                  Tallapaka 
##                       1842                       4275 
##                 Tallapalem                 TALLAPALEM 
##                       7416                        601 
##             TallaProddutur                  TALLAPUDI 
##                       2404                       2289 
##                 TALLAPURAM                Tallavalasa 
##                        266                       2003 
##                 TALLAVARAM                 Tallavlasa 
##                        330                        962 
##                    Talluru                   Talmalla 
##                       8472                        937 
##                  Talmudipi              Talpula palli 
##                       2797                        722 
##                 Talsmudram                 Taltampara 
##                        922                       1006 
##                  Taltariya                   Talupula 
##                        279                       6939 
##               Talupurupadu                Talvayapadu 
##                        541                       1543 
##                   Talwaram                   Talzhuru 
##                        786                       2059 
##                     Tamara                 TAMARAGUDA 
##                        771                        373 
##                TAMARAPALLI                    TAMARBA 
##                        454                        746 
##              Tamballagondi              Tamballapalli 
##                       1475                      10189 
##                  Tamidpadu                   Tamirisa 
##                        935                       1401 
##                 Tamlapuram             Tammadehazhzhi 
##                        155                       3700 
##                Tammadpalli                 Tammaipeta 
##                       1068                        301 
##                  Tammaluru                 Tammapuram 
##                        545                        714 
##             TammaRajuPalle            TAMMARAYUDIPETA 
##                       1294                        300 
##                 TammaVaram               TAMMAYYAPETA 
##                       6018                        533 
##           TAMMI NAIDU PETA                 Tammingula 
##                        617                       1732 
##                      Tampa               Tampatapalli 
##                        427                        748 
##                    Tamrada                 Tamrakollu 
##                       2539                       1057 
##                     Tamram            Tamrikandijammu 
##                       2443                        653 
##                 Tamrkhandi                  Tamrpalli 
##                       1450                       2387 
##                    Tamtada            TAMTAMVARIPALLI 
##                        147                        307 
##                 tana PALLI                  Tanakallu 
##                       1366                       6268 
##              Tananchintala                  TANAVARAM 
##                        678                        877 
##               TandavaPalli               Tandenvalasa 
##                       1281                       1397 
##                 Tandranagi                Tangadencha 
##                       1015                       1730 
##                 Tangardona                   Tangatur 
##                        751                      10705 
##                   TANGATUR                  Tangaturu 
##                       1762                       2900 
##                    Tangeda                    Tangedu 
##                       2865                       1816 
##               Tangedukunta               Tangedumalli 
##                       1858                       3285 
##               Tangedupalli                   Tangella 
##                       1458                        719 
##               Tangellamudi                  Tangirala 
##                       4497                        375 
##             TangiralaPalli               Tangudubilli 
##                        512                       1188 
##               TANGUDUBILLI                   Tangutur 
##                        363                       1710 
##                  Tanguturu                  Tannamala 
##                        833                        296 
##                    Tantidi                 Tantikonda 
##                        964                       2015 
##                     Tanuku                  Tanumalla 
##                      35544                        526 
##                    Tanwada                   Tanwaram 
##                        891                        488 
##                   Tanyaali                 TAPESWARAM 
##                       1084                       3740 
##                   Tapovnam                   Tappetla 
##                       6400                        398 
##           Tappetwari Palli                 Tarakaturu 
##                        552                       1640 
##                  Tarapuram                  TARIGONDA 
##                       1985                       2785 
##                Tarigoppula                 Tarigopula 
##                       1497                       1633 
##                   Tarimela                  Tarlakota 
##                       2951                       1256 
##                 Tarlampudi                   Tarlipet 
##                        939                        520 
##                  Tarlupadu                  TARLUWADA 
##                       3740                       1963 
##                    Tartava                    Tarturu 
##                        453                        748 
##                  Tarunvayi                   Tatapudi 
##                       1259                        268 
##                   TATAPUDI           Tatawari Kithali 
##                       1220                        314 
##                 Taticherla                 TatiCherla 
##                       1489                       1064 
##                   TatiGood             TATIGUNTAPALLI 
##                       1103                       1215 
##            Tatiman kotturu                   TatiPadu 
##                        305                       1613 
##                   Tatipaka                 Tatiparthi 
##                       4951                       9791 
##                 TATIPARTHI                  tatiparti 
##                        336                        491 
##                   Tatipudi                   Tatituru 
##                        238                       2510 
##                  Tativarru            TATIYAKULAGUDEM 
##                        399                        344 
##                 Tatrakallu                 TATTABANDA 
##                       1479                       1684 
##                 Tattampara          TATtIMAKULU PALLI 
##                        329                        482 
##              Tavanam palli                Tavishipudi 
##                       3728                        586 
##                Tavlammarri                  Teddupadu 
##                        930                        417 
##                     Tedlam                      Teeda 
##                       1178                       2126 
##              TEEGALAVALASA                 Tegacherla 
##                        813                        920 
##                     Tegada                       TEKI 
##                        607                       3899 
##                    Tekkali                TekkaliPadu 
##                      16222                       1101 
##               TEKKALIPALEM              TekkaliPatnam 
##                       1132                        986 
##                 Teku manda                   Tekubaka 
##                       2253                        927 
##                 Tekulaboru                   Tekulodu 
##                        861                       1326 
##                  Tekupalle                     TEKURU 
##                        159                        242 
##               TelagaValasa                  Telaprole 
##                        413                       5564 
##                     Teliki               Telikicharla 
##                        538                       2988 
##                Telikipenta             Telineelapuram 
##                        505                        292 
##                  Tellabadu            Telladevarapadu 
##                        853                        243 
##           Telladevarapalli            Tellamvarigudem 
##                       1111                        360 
##            TELLAMVARIGUDEM                  Tellapadu 
##                        170                       1453 
##             Teluguraopalem            Telugurayapuram 
##                        700                        843 
##                  Telukutla                 Telumanchi 
##                        912                       1078 
##                    Temburu            Temmireddipalli 
##                       1785                        564 
##                   Tempalle        Tenakala Duggavlasa 
##                       1753                        403 
##                     Tenali                 Tene palli 
##                     104745                       1683 
##                    Tenneru              Tennu Boddwar 
##                       2140                       1375 
##                TentuValasa                 TENUGUPUDI 
##                        562                       1120 
##                Teppalnlasa                  Terapalli 
##                        398                        365 
##                     Terlam                 Ternekallu 
##                       2590                       2233 
##                Teruvupalli                     Tetali 
##                       1348                       3182 
##                   Tetgunta                   Tettangi 
##                       8614                       1268 
##                  Tettangi.                    THADUKU 
##                        307                       1890 
##              Thakkellapadu               Thakurupalem 
##                       5879                        256 
##                THALAPANURU               THALARIVETTU 
##                        395                        760 
##               THALLA PALLI               Thallampuram 
##                        943                       2381 
##                Thallapalle                Thallapalli 
##                       1446                       2503 
##  Thambhiganipalli H/o Ekar           Thambugani palli 
##                        543                       2243 
##              Thaminapatnam              THAMMADAPALLE 
##                       1283                        447 
##          ThamminaiduPettah                     Thanam 
##                        615                       2452 
##                   THANDLAM                   THANDYAM 
##                        590                       2297 
##                 thanelanka                     THANEM 
##                       5199                        797 
##            Thangellipallem                THANTIKONDA 
##                       1091                       2009 
##               Thata Kuntla            THATHAIAH KALVA 
##                       1485                       1143 
##         THATHI REDDY PALLI           THATIGUNTA PALEM 
##                        401                        620 
##                   THATNERI              Thavwaripalli 
##                        383                        901 
##        THEENUSAMNTHAVALASA                  THEERTHAM 
##                        594                       1117 
##                   THELLURU                    THEMARA 
##                        872                       1018 
##                    THERANI                     Thettu 
##                       3690                        749 
##                     THETTU              THI MMA PURAM 
##                        242                        647 
##             THIMMA SAMURAM                thimmapuram 
##                        704                        567 
##                Thimmapuram                ThimmaPuram 
##                      14451                       2618 
##                THIMMAPURAM      ThimmaPuram-M.C.Palli 
##                       2666                       2770 
##            THIMMAPURAMPETA           THIMMARAJU PALLI 
##                        468                        494 
##          Thimmaraju Pettah            Thimmarajupalli 
##                       1346                        436 
##             ThimmaSamudram             ThimmayyaPalem 
##                       5146                        348 
##          THIMMINAYANIPALLI          THIMMMANAYUNIPETA 
##                       1867                       1335 
##          THIPI NAIDU PALLE              Thippayapalli 
##                        781                       1641 
##           ThippireddyPalli         thirumalaiah palli 
##                       2377                       1485 
##  THIRUMALAKONADAMAMABA PUR            ThirumalaKuppam 
##                        754                       2718 
##             ThirumalaPuram                  ThiruMali 
##                        577                       2642 
##               THIRUMANDYAM              ThiruNampalli 
##                        868                        911 
##                  ThiruPadu                 Thirupathi 
##                        762                     108370 
##            ThirupathiPalem           Thiruvanam palli 
##                        447                        710 
##        thitava kunta palli               Thogarakunta 
##                        329                       2378 
##               ThokalaPalli                THOKALAPUDI 
##                       1852                       1260 
##              ThokalaValasa                    THOLAPI 
##                        246                       2503 
##        Thollagangana palli               THOLLAMADUGU 
##                        668                        289 
##              THONDALADINNE              THONDAM BATTU 
##                        466                        431 
##               THONDAMANADU                 Thondapadu 
##                        503                       1900 
##                    THONDUR                   THONDURU 
##                       1671                       1513 
##                 Thopugunta                    THORURU 
##                       1573                       1309 
##                Thota Palle                ThotaCherla 
##                        348                        658 
##                    Thotada                THOTAKANUMA 
##                        319                       1581 
##             ThotakuraPalem                  ThotaPadu 
##                       1728                       1790 
##                 ThotaPalem                 Thotapalli 
##                       1309                       3859 
##        Thotapalli Guduru-i                THOTAPALYAM 
##                        972                       2708 
##                  Thotapeta            Thotaravulapadu 
##                       2537                       1256 
##                THOTAVALASA                   ThotaWad 
##                        526                       1540 
##                Thottambedu                   THOYYERU 
##                       1699                       2381 
##           Thrivengalapuram                Throvagunta 
##                       1247                       5357 
##                 THUGUNDRAM                 THUKIVAKAM 
##                       3707                       9801 
##                 Thukkuluru            THULISAMMA GUDI 
##                       1674                        560 
##                     Thumba              Thumba kuppam 
##                       1791                       2845 
##                   Thummala             Thummala Baylu 
##                       2716                        110 
##             THUMMALA GUNTA              Thummalapenta 
##                       2688                       6717 
##              THUMMALAPENTA            THUMMANAM GUTTA 
##                       3353                        890 
##             THUMMARA KUNTA              THUMMIKAPALLI 
##                       2704                        218 
##                 Thummileru                    Thummur 
##                        340                       2271 
##           Thumpayana palli                     Thumsi 
##                        602                        351 
##              Thurakalapudi                 Thurimella 
##                       1288                       1739 
##                 Thurimerla               THURLA PALLI 
##                       3730                        951 
##                THURUMAMIDI                 THURUPALLE 
##                         96                        735 
##                 THUVAPALLE                    Tiddimi 
##                       1182                        827 
##             TIKKAVANIPALEM                 Tikkavaram 
##                        851                       1358 
##             Tikkawarappadu                     Tilaru 
##                       1997                       1226 
##                 Tillakuppa                  Tillapudi 
##                       2563                       1561 
##                     Timdam                    Timidam 
##                        249                        793 
##                     Timidi                    TIMIRAM 
##                       1636                        317 
##       Timiteru BurjaValasa            Timmajikandriga 
##                        580                        415 
##                 Timmalanji            Timmanayanpalli 
##                         95                        494 
##         Timmanayudu Pettah              Timmannagudem 
##                        895                        220 
##              Timmannapalem                 Timmapuram 
##                        483                       2254 
##            Timmarajupalena              Timmarajupeta 
##                       1852                       1239 
##            Timmareddipalem            Timmareddipalli 
##                        615                        715 
##            TIMMAREDDIPALLI               Timmayapalem 
##                        515                       3073 
##                Timmaypalem         Timmi Naidu Pallem 
##                        618                      10845 
##                Tinnelapudi                    Tiparru 
##                        394                       2119 
##                   Tipnooru              Tippala Doddi 
##                         94                        502 
##                  Tippaluru               Tippanagunta 
##                        866                        447 
##               Tippanapalli                 Tippanooru 
##                        672                        517 
##            Tipparaju Palli               Tippayapalem 
##                        315                        958 
##                Tippayplale                 Tippepalli 
##                        726                       1284 
##                 Tirdampadu            Tirigandladinne 
##                        645                        137 
##                  Tirlanagi               TIRUCHANOORU 
##                       1066                      13994 
##              Tirugudumetta                   Tirumala 
##                       1036                       3584 
##        Tirumaladevarapalle              TIRUMALAPURAM 
##                        430                       2347 
##          TIRUMALARAJUPURAM            Tirumalayapalem 
##                        484                       2614 
##             Tirumlampalena               Tirumlapuram 
##                       2783                        836 
##                 Tirumlpudi                   Tirumuru 
##                        964                        409 
##                   TIRUPATI               Tiruvidipadu 
##                      55773                        374 
##                 TIRUVTIYAM                   Titkallu 
##                        591                       2303 
##                    Tittiri                 Titukuppay 
##                       1092                        124 
##              Todendlapalle                     Toderu 
##                        742                        935 
##                 Todicherla                Todugupalli 
##                       1373                        155 
##                     Todumu                 Togalgallu 
##                        456                        441 
##                 Togarchedu               Togera Chedu 
##                       1254                        521 
##                     Togiri                     Togram 
##                       1102                        423 
##                  Togramudi                    Togummi 
##                        554                       1411 
##                     Tokada                  Tokapalli 
##                       2245                        407 
##                 TOKAVALASA                     TOKURU 
##                        403                        588 
##                     TOLERU                   Tolukudu 
##                       4109                       1361 
##              Tolusurapalli                      Tonam 
##                        986                       2259 
##                  Tondanagi                    Tondapi 
##                      10209                       2212 
##                 Tondawaram                Tondranagi. 
##                       2177                        650 
##                    Tonnagi                 Tonukumala 
##                       2939                        709 
##            Too. Chowtpalem            Too. CumbumPadu 
##                       1262                        405 
##          Too. Veerayapalem                   TOOMBURU 
##                       1278                        879 
##                   TOOTANGI                  Topudurti 
##                       1129                       1848 
##              Torragudipadu                    Torredu 
##                       1000                       3789 
##                Torrivemula                  Tossipudi 
##                        850                       1621 
##                     Totada        Totada Sirasu palli 
##                       1473                       3352 
##        Totala CheruvuPalli                Totluru U.I 
##                        728                        456 
##                    TOTTADI                 Tottramudi 
##                        179                       2585 
##                       Tovi              Tripurantakam 
##                       1085                       2974 
##               Tripurapuram               TripuraVaram 
##                       1348                        658 
##               TSADIPIRALLA                 Tsakibanda 
##                       1192                       2365 
##                     Tubadu                    TUBBURU 
##                       1495                         91 
##                     Tuddli                       Tudi 
##                        333                        510 
##                     TUDUMU              Tudumuladinne 
##                        591                        814 
##               Tudumuldinne                    Tuggali 
##                        860                       2726 
##       TULASI KRISHNA PURAM                     Tulgam 
##                       1411                       1407 
##                    Tulluru                   Tulsigam 
##                       4566                       1469 
##                Tulsipakala                  Tulugonda 
##                        683                        255 
##                     TulugU                   TUMARaDA 
##                        937                       1721 
##                     Tumaya                 Tumbakonda 
##                        354                        244 
##                 Tumbalbidu                    Tumbali 
##                        594                       1175 
##                Tumbignooru                   Tumkunta 
##                       2004                       1713 
##                 TummaGudem                 TummaGunta 
##                        933                       1038 
##                 Tummakonda                TummaKuntla 
##                        614                       2002 
##             Tummalacheruvu               Tummalapalem 
##                       6523                       1461 
##                Tummalbailu          Tummalkuntlapalli 
##                        845                       1391 
##                  Tummaluru                  Tummapala 
##                       2652                      21034 
##                  Tummapudi               Tummedalpadu 
##                       4330                        314 
##               Tummikapalli                Tummikpalli 
##                        280                       2739 
##                    Tumpada                    Tumrada 
##                        878                        429 
##                  Tumrukota                 Tumucherla 
##                       2978                       3547 
## Tumukonta Ramachandrapuram                   Tumuluru 
##                        249                       1706 
##                      Tunda                   TUNDURRU 
##                        399                       3875 
##                 Tungamdugu                  TUNGAPETA 
##                        384                        633 
##               Tungatampara                  Tunglanya 
##                        375                       2237 
##                    Tungodu                       Tuni 
##                        673                      36782 
##              TuniKiiahPadu                  TUNIPALEM 
##                       1494                        273 
##                 TUNIVALASA                    TuniWad 
##                       1064                        609 
##                  Tunugunta              TURAKALAMETTA 
##                        199                        750 
##                TURAKAPALLI                 TURAKAPETA 
##                        309                        236 
##            Turangala Palem                    TURANGI 
##                        951                      17778 
##              Turayapuvlasa                  Turklkota 
##                        216                        270 
##                Turklpatnam            Turknayuduvlasa 
##                       1394                        629 
##                  Turkpalli                    Turkpet 
##                        831                        647 
##                  Turlapadu        Turpu Chennam Palle 
##                       2964                        338 
##             Turpu Dubgunta          Turpu Jangalpalli 
##                        603                        478 
##             Turpu Kanupuru        Turpu Kodigudlapadu 
##                        544                        212 
##         Turpu Lakshmipuram           Turpuboyamdugula 
##                       1345                        470 
##             Turpuerraballi                Turpuguduru 
##                       1696                       3872 
##                 Turpulanka            Turpurompidodla 
##                       1039                        484 
##                 Turputallu              Turpuvipparru 
##                       5800                       1503 
##                 Turumamidi                  Turumella 
##                       1918                       3108 
##                 Turuvgallu                   TURUVOLU 
##                        359                       1375 
##                  TUTIGUNTA              Tutrala Palli 
##                        192                       1280 
##                  Tuvvapadu                U Rajupalem 
##                        730                       1140 
##              U. Kothapalli             U. Venkamapata 
##                        766                        311 
##                  U.G.Puram          U.Kurmanadhapuram 
##                        640                        380 
##            U.NarsingaPalli                U.R.K.Puram 
##                        173                        902 
##               U.V.R.Pettah                  Ubicherla 
##                        423                       2984 
##                     Uchuru             UDAMALA KURTHI 
##                       1374                        626 
##                UDAVAGANDLA                  Udayagiri 
##                        401                       7106 
##                  Uddanagi.    Uddanda Jagannadhapuram 
##                        562                       1341 
##               Uddandapalem               Uddandapuram 
##                        136                       1607 
##         Uddandurayunipalem                  Uddapalem 
##                       1103                        603 
##                   Uddavolu                    Uddehal 
##                       1216                       2617 
##                   Udegolam              Udiripi Konda 
##                       3538                       2341 
##              Udtawaripalem                UDUMALAPADU 
##                        408                        340 
##                 Udumlkurti                    Udumudi 
##                        764                       4175 
##                UdumulaPadu                     Udypur 
##                        997                        396 
##                   Udypuram                Ugginapalem 
##                       6147                       2055 
##                   Uggumudi                      UGINI 
##                        561                       1229 
##                ugranapalli                  Uiahndana 
##                        956                       1126 
##                Ukkayapalli                   UKKURBHA 
##                       1542                        496 
##                  ULAVAPADU                 Ulavapalle 
##                       1119                        299 
##                    Ulchala                     Ulichi 
##                       4128                       1362 
##                   Ulimella               ulimeshwaram 
##                       1353                       1029 
##                Ulindakonda                    Ulipiri 
##                       2839                       1432 
##                 Ullamparru                  Ullikallu 
##                       2977                       1401 
##                  Ullipalem                    Ulpalli 
##                       2970                       3947 
##                 Ulusumarru                   Ulvlpudi 
##                       1376                        430 
##                   Ulvpalla              UMAMAHESWARAM 
##                       1372                       2835 
##            Umamheswarpuram                    UMILADA 
##                       1721                       1186 
##          Ummadidevarapalli                Ummadivaram 
##                        468                       1339 
##                   UmmaGuru                   Ummalada 
##                        402                        974 
##                 Ummanpalli                UMMAYIPALLE 
##                        316                        698 
##                  Undabanda                  Undavalli 
##                       1330                       6558 
##             Undeshwarpuram                       Undi 
##                       1528                      10370 
##               Undrajavaram                  Undrapudi 
##                       5558                        472 
##                Undrikudiya                     Unduru 
##                        253                       4410 
##             UNGARANIGUNDLA                    Ungatla 
##                        422                       4718 
##                    Ungrada                   Unguturu 
##                        591                      10002 
##                    Unikili                  Unkrmilli 
##                       3679                       1851 
##                     Unnava                    Untakal 
##                       1863                       2027 
##                   Unudurru                    Unukuru 
##                       1348                        406 
##          Upamaka Agraharam                     Uppada 
##                       2423                       4955 
##                Uppala Padu                Uppaladinne 
##                       2092                        333 
##                    Uppalam                  Uppalapad 
##                        415                      17213 
##                 Uppalapadu                 UPPALAPADU 
##                       2568                        389 
##                Uppalguptam                   Uppaluru 
##                       5985                       4198 
##                   UPPALURU                  Uppangala 
##                        762                        881 
##                Upparapalle                Upparapalli 
##                       6905                       3799 
##                   Upparhlu               Upparlapalle 
##                       1419                        930 
##           Upparnayuduvlasa                 Upparpalem 
##                        252                       2575 
##           Uppathivaripalli                  Uppawaram 
##                        595                        858 
##                     Upperu               UPPILLIPALLE 
##                        759                        759 
##                Uppinivlasa                  Uppivlasa 
##                        787                        189 
##                     Uppudi                   Uppuluru 
##                       2442                       2106 
##               UPPUMAGULURU                  Uppumilli 
##                       2384                        705 
##                   Upputuru                   URANDURU 
##                       4234                       1690 
##                 Uravakonda                Urichintala 
##                      24403                        950 
##                      Urivi                      Urjam 
##                        909                       1397 
##            Urla obanapalli                  URLAGUDEM 
##                        441                        385 
##               URLAKULAPADU                      Urlam 
##                        487                       1840 
##                   Urukunda                    Uruturu 
##                       2121                       2706 
##               Usguntapalem                    Uskonda 
##                        564                        179 
##                  Ustepalle                      Utada 
##                        399                        420 
##                UTASAMUDRAM                    Utchili 
##                        436                       2011 
##      Uthara Brahmana palle             Uthara Valluru 
##                        850                       4604 
##                Utharkanchi                 Utharpalli 
##                       3154                       1118 
##                 UthraValli                    Utkallu 
##                       3515                        799 
##                    Utkonda                      Utkur 
##                       1438                       2329 
##                  Utlapalli                  Utrumilli 
##                        775                        934 
##                Utsalavaram              Uttamanelluru 
##                        586                        408 
##                     Utukur                    Utukuru 
##                      12560                       3457 
##                UYYALAPALLI               UyyalaPettah 
##                        772                        316 
##                     Uyyuru                V K R PURAM 
##                      24141                       1626 
##               V Kothapalli               V R O COLONY 
##                       1713                        476 
##                  V R Puram              V. Rudravaram 
##                       1465                        559 
##                V.Appapuram                  V.J.Palem 
##                       1171                        719 
##                  V.J.PURAM                     V.KOTA 
##                        478                       7496 
##             V.Krishnapuram                 V.MADUGULA 
##                        300                       6419 
##                  V.N PURAM                  V.N.PALLI 
##                        617                       1646 
##                 V.N.R.PETA            V.P.Raju Pettah 
##                       1506                        455 
##              V.R.Agraharam                  V.R.Gudem 
##                        219                       1466 
##                  V.R.Puram             V.RAMANNAPALEM 
##                        278                        378 
##              V.SANTHAPALEM             V.SARABHAVARAM 
##                       1052                       2049 
##                     Vadada            Vadagandlapalli 
##                       4652                        330 
##                     Vadali                      Vadam 
##                       1624                       1789 
##               VADAMALAPETA                  VADAPALEM 
##                       2694                       4401 
##                  Vadapalli                  VADAPALLI 
##                       5902                        705 
##                Vadarlapadu                    Vaddadi 
##                        610                       4109 
##                  Vaddanagi                Vadde palli 
##                        484                        511 
##                   Vaddeman                  Vaddemanu 
##                       1364                        594 
##                Vaddengunta               Vaddeshwaram 
##                       2439                       2888 
##                Vaddi palli                 Vaddi vada 
##                        579                       1668 
##                Vaddigudena                VADDIMADUGU 
##                        522                        224 
##              VADDINIVALASA                    VADDIPA 
##                        924                        983 
##                  Vaddipadu                 Vaddiparru 
##                        783                       3515 
##                  Vaddirala                   Vaddmanu 
##                       1605                       1794 
##                Vadigepalli                 Vadiseluru 
##                       1146                       4772 
##               VADLA KUPPAM            Vadla Ramapuram 
##                        669                       2192 
##               Vadlamannadu                  Vadlamanu 
##                       2117                        132 
##                  Vadlamudi               Vadlamukkala 
##                       4889                        626 
##                  Vadlamuru                  VADLAMURU 
##                       2182                        724 
##                  Vadlapudi                      Vadli 
##                      13622                       2189 
##                    Vadluru              Vadrahonnooru 
##                       1248                        615 
##                 Vadrapalli              Vadrevulpalli 
##                       1275                       1745 
##                    Vagalla                  VAGATTURU 
##                        858                        560 
##                   VAGAVEDU                 Vagemadugu 
##                        670                        793 
##                Vaggampalli                    VAIDANA 
##                        594                       1185 
##              VaikuntaPuram             Vaikunthapuram 
##                       1499                        402 
##        Vairidari Annavaram              Vajawaripalem 
##                        757                        886 
##                 Vajay Good        VAJJAVAARI KANDRIGA 
##                        211                        750 
##                 Vajr Kutam                 Vajrakruru 
##                        293                       4322 
##             VAJRAPUKOTTURU                     Vakada 
##                       1663                       1750 
##                     Vakadu                 VAKALAPUDI 
##                       4851                      17325 
##                   Vakapadu                  VAKAPALLI 
##                       2481                       1080 
##                  VAKATIPPA               Vakkalagadda 
##                       1404                       1605 
##                 Vakkalanka                  VAKKULURU 
##                        873                         76 
##                  Vaklvlasa                   VakPalli 
##                        457                       1747 
##                   VakTippa                    VALAABU 
##                       1433                        427 
##                  Valaparla                     Valasa 
##                       4984                       5738 
##                Valasapalli                     VALASI 
##                        573                        877 
##                   ValGadda                 Valicherla 
##                        242                        265 
##                 VALIMERAKA                   Valiveru 
##                        886                       2156 
##              Valiwartipadu              Vallabhapuram 
##                       1225                       3783 
##           VallabharaoPalem               Vallabraopet 
##                       1455                        244 
##             Vallabrayipadu                 VALLAMPADU 
##                        327                        394 
##                Vallampatla                VALLAMPATLA 
##                        905                        239 
##  Vallampatlashiwarumalluku                 Vallampudi 
##                        399                       1501 
##                 VALLAPALLI                 Vallapuram 
##                       2430                        566 
##              Vallarigdubha                Vallaypalem 
##                        997                        221 
##                 VALLIGATTA                  Vallipedu 
##                       1533                        296 
##                  Vallivedu                    Valluru 
##                       1560                      23443 
##                    VALLURU               Vallurupalli 
##                       1731                        894 
##                    Valmedu               VALMIKIPURAM 
##                       1807                       9003 
##                 Valsmapata                     Valuru 
##                       1178                        344 
##            ValuThimmapuram                 Vambarilli 
##                        717                        148 
##                  Vamkuntla                   VAMPALLI 
##                        727                        297 
##                 VaMurVelli            VAN TRALA PALEM 
##                       1128                        650 
##            VaNabhRangiPadu            Vanadurga puram 
##                       1078                        624 
##                 VANAGARAYI             Vanaguttapalle 
##                        484                        291 
##                     Vanala              VANAMALADINNE 
##                       1064                       3254 
##                  VANAPALLI                 Vanapamula 
##                       7802                        630 
##                  VANCHANGI                   Vanchula 
##                        955                        874 
##                    Vandadi                 Vandagallu 
##                       1451                       1408 
##                  Vandanpet                Vandavagili 
##                        192                        941 
##              Vandigamlanka                   Vandrada 
##                        443                        581 
##                    VANDRAM                 Vandranagi 
##                       1637                        997 
##                   Vandrayi                 Vandrujola 
##                       1248                        100 
##                    Vanduva                 VANELLOORU 
##                        916                        421 
##                Vangalapudi                    VANGALI 
##                       2442                       1487 
##                   Vangallu                 Vanganooru 
##                        906                        628 
##                  VangaPadu                    Vangara 
##                        627                       1214 
##       Vangara H/o Rayipadu                 Vangimalla 
##                        462                       3784 
##                    Vanguru               Vanikemdinne 
##                        934                        600 
##                  Vanikunta                    Vanilla 
##                       1176                        947 
##              VanitMandalam                  Vanjanagi 
##                        507                       2502 
##                Vanjangipet                    Vanjari 
##                        494                       1812 
##                  Vanjivaka         VANKABOTTAPPAGUDEM 
##                       1305                        313 
##                 Vankamarri                 VANKAMARRI 
##                        901                        571 
##            Vankarajukaluva                Vankarkunta 
##                        472                       1516 
##             VANKAVARIGUDEM              VankayalaPadu 
##                        689                       1803 
##                   Vannaali               Vannayapalem 
##                        252                        701 
##           Vannechintalpudi                  Vannepudi 
##                       3245                       1520 
##              vanniar block             Vanrishnupuram 
##                       1423                        639 
##                Vantadpalli                    Vantala 
##                        440                       1523 
##               Vantalmamidi                   VANTARam 
##                        845                       1681 
##               Vantatipalli                  Vanudurru 
##                       1025                       1316 
##                Vanugupalli                   Vanukuru 
##                        899                       5188 
##                    Vanvolu                  Vappanagi 
##                       3356                       1732 
##                     VARADA             VARADAIAHPALEM 
##                       1395                       2989 
##                   Varagani               Varahapatnam 
##                       1343                       1262 
##                VarahaPuram                      Varak 
##                        902                        609 
##             Vardinenipalem                    Vargani 
##                        470                        745 
##          Varhnrshimhapuram                 Varidhanam 
##                        274                       1105 
##                VARIGAPALLI                  Varighedu 
##                       1430                       2694 
##                  Varikunta              Varikuntapadu 
##                        675                        604 
##              VARIKUNTAPADU                 VARIKUNTLA 
##                       1166                        955 
##                     Varini                    Varisam 
##                       4561                        462 
##                    Varkuru                      VARRA 
##                       2835                        500 
##                  VARUTTURU                     Vasadi 
##                       2828                        403 
##                   Vasanadu                    Vasanta 
##                        870                        633 
##               Vasantapuram                 VasantaWad 
##                        330                       1248 
##              VASANTHAPURAM               Vasanthawada 
##                        640                       2250 
##                     VASAPA             VashudevPatnam 
##                       1046                        482 
##                       Vasi                     Vasili 
##                        691                       1602 
##                  VaSundara                  Vatambedu 
##                       1250                       1138 
##            Vatambedukuppam                    VATANGI 
##                       2333                       1010 
##                   Vathalur                  Vatlabylu 
##                       1838                        228 
##                    Vatluru                    Vatpagu 
##                       8496                        679 
##               VATSA VALASA                   Vatsavai 
##                       1463                       4848 
##             Vatticherukuru              Vattigudipadu 
##                       1030                        921 
##            Vavam, Vaivapet                Vavil thota 
##                        457                       2452 
##               vavila chenu                   Vavilala 
##                        277                       1347 
##                   Vavileru               Vaviletipadu 
##                       1544                       5210 
##           VAVILIPALLI PETA                  Vavilpadu 
##                        462                       1525 
##                 Vavilvlasa               Vavintaparti 
##                        459                        983 
##                    Vavveru                   VECHALAM 
##                      21119                        896 
##                    Vedadri    VEDALA SRI NIVASA PURAM 
##                        913                        671 
##                      VEDAM                    Vedangi 
##                       1091                       3241 
##             VEDANTAH PURAM               Vedantapuram 
##                       2503                        986 
##                Vedayapalem                 Vedicherla 
##                      10032                        909 
##              Vedireshwaram            Vedulla Churuvu 
##                       5594                        275 
##             VEDULLA VALASA             Vedullacheruvu 
##                        485                        386 
##             VEDULLACHERUVU              vedullanarava 
##                        851                       2438 
##              VEDULLAVALASA               Vedullavlasa 
##                        593                       1656 
##                Vedurubidem           Veduruguttapalli 
##                        550                        349 
##               VEDURUKUPPAM                 VEDURUMUDI 
##                       2897                       1042 
##                 VEDURUPAKA                Vedurupalli 
##                       9221                        445 
##                Veduruparti                Vedurupattu 
##                       1473                        396 
##             Vedurupavuluru                   Vedururu 
##                       4650                       1924 
##                 Veduruwada                VEERA PALLI 
##                        982                        459 
##            VEERABADRAPURAM            VEERABHADRAPETA 
##                       2467                        604 
##          VeerabhadraPettah   VeeraBhoopathi Agraharam 
##                        964                        969 
##               Veeraghattam           VEERAGHAVUNIKOTA 
##                       4472                        949 
##             VEERAKANELLORE        VeeraKr Yachsmudram 
##                       1108                        201 
##                Veerampalem                VEERAMPALEM 
##                       1775                        360 
##               Veerampalena                Veerampalli 
##                       2458                        488 
##               Veeranakollu             VEERANARAYANAM 
##                        704                       1613 
##         VeeranarayanaPuram              VeerannaPalem 
##                        228                       3564 
##              VEERANNAPALEM              VeerannaPalli 
##                        383                        628 
##                 Veerapalli          Veerapaneni Gudem 
##                        687                       1779 
##      VEERAPPAREDDY PALAYAM                 Veerapuram 
##                        420                       1557 
##             VeeraRaamPuram      VeeraRamakrishnapuram 
##                        248                        229 
##                 Veeravalli            VeeravalliPalem 
##                       4115                       1360 
##                 Veeravaram                 VEERAVARAM 
##                       9279                        524 
##               VEERAVASARAM           Veeravenkatpuram 
##                      13671                       1474 
##        VEERAVILLIAGRAHARAM                  Veerbadra 
##                        951                        361 
##                  Veerballi                 Veerepalli 
##                       5499                        532 
##            veereswarapuram  VeeriSettyGudem,Tadikalap 
##                        475                       1554 
##                 Veernamala          Veernamala Thanda 
##                       1059                       1038 
##              Veernarayanam                 Veersagram 
##                       1064                        954 
##               Veerullapadu               Veerupapuram 
##                       2684                        808 
##                  Vegavaram              Vegayammapeta 
##                       3100                       4325 
##             VEGESWARAPURAM                  VegiThota 
##                       1399                        621 
##                   Vegivada                     Veguru 
##                       2740                       3394 
##                   Vejendla                 VEJJUPALLE 
##                       4939                       1688 
##                   Veknooru                    VELADAM 
##                       2369                        617 
##               VelagaCherla                   VELAGADA 
##                       1094                        296 
##             VelagalaPonnur                 VelagaPadu 
##                        346                       1764 
##                VELAGAPALLI                 Velagapudi 
##                        184                       2092 
##                VelagaPuram                VELAGATHODU 
##                        110                       2730 
##               VelagaValasa               VELAGAVALASA 
##                       1192                        413 
##   VelagaValasa Addumanda D                  VelagaWad 
##                        413                        687 
##                 Velagdurru                 Velaglpaya 
##                        830                        785 
##                  Velagluru                  Velagturu 
##                       1023                        440 
##                     Velair                  Velairpad 
##                        353                       1202 
##                  Velamkuru                  VELAMPADU 
##                       1396                        919 
##                 Velampalem                    Velangi 
##                       6183                       6425 
##                    Velanka                   VELAVALI 
##                       2375                       1434 
##                   VELAVEDU              Velawartipadu 
##                       1176                        947 
##                   Velchuru           Veldi Kothapalem 
##                        613                       1218 
##                  VeldiPadu                  Veldurthi 
##                        818                       6123 
##                   Veldurti                     Veleru 
##                       6312                       2623 
##                  Velgaleru              Velichelamula 
##                       2291                       2308 
##                  Velicheru                 Velidandla 
##                       3217                       1124 
##                  Veligallu                  VELIGALLU 
##                       1389                       2146 
##                 Veligandla                 VELIGANDLA 
##                       1550                        711 
##                  Veligonda                  Velikallu 
##                       1338                        496 
##                   Velinolu                  velivarru 
##                       1138                        867 
##                   Velivela                  Velivennu 
##                       1078                       3002 
##                    VELKURU                      Vella 
##                       1975                       4327 
##         Vellachintalgudena               VELLAGAPALLI 
##                       2430                        457 
##             Vellalacheruvu       Vellalavari Kandrika 
##                       2774                        773 
##                  Vellaluru                 Vellamaddi 
##                       1283                       2524 
##                 Vellamilli                Vellampalli 
##                       2400                       1498 
##                   Vellanki                   VELLANKI 
##                       1501                       5265 
##                   Vellanti                 Vellapalem 
##                       2649                        265 
##                   Vellatur                  Vellaturu 
##                      10690                        618 
##                    VELLURU                 Velpanooru 
##                        941                       4187 
##                Velpucherla                    Velpula 
##                        571                       3716 
##                Velpulgunta                     Velpur 
##                        378                      15529 
##                   VELPURAI                   Velugodu 
##                        556                      13221 
##                Velugubanda                VeluguPalli 
##                       4513                        267 
##                   Velukadu                   Velupodu 
##                        839                       1317 
##               Velupucharla                     Veluru 
##                        795                       1988 
##                     VELURU                   Velusoda 
##                        793                        404 
##              VeluvalaPalli                   Velvadam 
##                       1024                       3778 
##                   Vemagiri                    Vemalam 
##                      11208                       1542 
##                     VEMALI                   Vemaluru 
##                        625                        775 
##                    Vemanda                  VEMAPURAM 
##                        753                        519 
##                  Vemavaram                  VEMAVARAM 
##                       7274                        800 
##              Vemavarappadu             Vemavarappalem 
##                        989                        292 
##                  VEMBAKKAM                  Vembuluru 
##                       1997                        536 
##             VemireddyPalle               VeMoolaPalli 
##                       1633                        960 
##                      VEMPA                   Vempadam 
##                       5011                       2187 
##                    Vempadu                   Vempalle 
##                       8588                      23620 
##                  Vemparala                   Vempenta 
##                       1429                       2643 
##                   Vemugodu                     Vemula 
##                       1783                       3420 
##                   Vemulada                VEMULAKONDA 
##                        426                       1399 
##                 Vemulapadu                 VemulaPadu 
##                        499                        731 
##                Vemulapalli                VEMULAPALLI 
##                       2725                       4297 
##                 Vemulapudi                 VEMULAPUDI 
##                       4007                        504 
##               VEMULAVALASA                 Vemulawada 
##                       1973                       3675 
##                 Vemulnarva                   VEMULOVA 
##                        612                        235 
##                  Vemulpadu                   VEMULURU 
##                       1617                       1284 
##                     Vemuru                     VEMURU 
##                       4789                       1111 
##                     Venadu                     Venane 
##                       1495                        523 
##               Vendlurupadu                    Vendodu 
##                        598                       1054 
##                     Vendra                    Vendram 
##                       4609                        290 
##              Vendugampalli                    VENGADA 
##                       1114                        978 
##           Vengalam Cheruvu              Vengalampalle 
##                       4416                       1264 
##               VENGALAPURAM            VENGALARAIPURAM 
##                        487                        452 
##         VENGALARAJU KUPPAM                VENGALATTUR 
##                       1103                       1661 
##            VengamambaPuram            Vengamukkapalem 
##                        933                       1604 
##                 VENGAPURAM                 Venigandla 
##                        910                       3262 
##         VenkaiahGariPettah              Venkaiahkalva 
##                        477                        453 
##             VenkaiahPettah      Venkamapata Agraharam 
##                        855                        292 
##                 VENKAMPETA              Venkannagudem 
##                       1550                        519 
##              Venkannapalem         VENKATA GARI PALLI 
##                       3485                        631 
##      VENKATA KRISHNA PALEM            VENKATA NAGARAM 
##                        739                       1073 
##        VENKATA PATHI NAGAR         Venkata Raju Palem 
##                       1852                        396 
##    VENKATA RAJULA KANDRIGA     Venkata Rangarayapuram 
##                        850                        346 
##              Venkatachalam        VENKATADASARLAPALLI 
##                       3773                       1210 
##            Venkatadrigudem            Venkatadripalem 
##                        359                       1600 
##                Venkatagiri                VENKATAGIRI 
##                       3562                      34309 
##        Venkatakrishnapuram        VENKATAKRISHNAPURAM 
##                        121                        783 
##    Venkatakrishnarayapuram             Venkatam Palli 
##                       3748                       3541 
##              Venkatampalle              Venkatampalli 
##                        400                       2608 
##             Venkatanagaram               Venkatapuram 
##                        626                      12582 
##               VENKATAPURAM  VENKATAPURAM ANE GURUKULA 
##                       3940                        347 
##          VENKATARAMA PURAM           Venkataramapuram 
##                       1329                        727 
##           VenkataraoPettah        VENKATARAYUNI GUDEM 
##                        317                       1337 
##          Venkatareddipalem         Venkatashettipalli 
##                        791                        327 
##           Venkatayacheruvu             Venkatayapalem 
##                        238                       4662 
##            Venkatayapalena           Venkatchlampalli 
##                       1015                        252 
##               Venkatepalle             Venkatibyripur 
##                        516                       1238 
##               Venkatmapata          Venkatnayanipalle 
##                        383                       1129 
##                Venkatpalem                Venkatpuram 
##                       1763                        972 
##            Venkatrajugudem            VENKATRAJUPURAM 
##                        326                        478 
##          Venkatrayanipalli            Venkatrayudupet 
##                        451                        499 
##                 VenkuPalem                 Vennanpudi 
##                        529                        342 
##            VennaPoosaPalli              Vennela Palem 
##                        445                       1953 
##         VennelaButchampeta                Vennelvlasa 
##                        345                        231 
##                    Vennuru                  Vennutala 
##                       1008                        605 
##              Ventrapragada                    VENTURU 
##                       3092                       2842 
##           VENUGOPALA PURAM            Venugopalapuram 
##                        736                        792 
##            VENUGOPALAPURAM                  Venumbaka 
##                       1870                       1256 
##             Venutana palli              Venuturumilli 
##                        631                        652 
##                     Vepada              Vepagum palli 
##                       1877                        244 
##                  Vepagunta                  VEPAGUNTA 
##                      18268                       4531 
##               Vepana palli                 VEPANJEERI 
##                        716                       1198 
##                  VePanjeRi                  Veplparti 
##                        840                       2570 
##                 Vepmanipet                    Veprala 
##                       2024                       3365 
##                   Vepralla                 VEPURIKOTA 
##                       2719                       1732 
##                 VETAMAMIDI                  Vetapalem 
##                        861                      16349 
##             VETHALATHADUKU                 Vetlapalem 
##                        556                       8562 
##                   VETUKURU                    Vgaruru 
##                        589                       2160 
##           Vi Tie Agraharam               Vibharapuram 
##                       9720                        623 
##              Vibharitlpadu                  Vidavalur 
##                        704                       4733 
##                Vidpana Kal            Vidyaranyanagar 
##                       5320                       5491 
##                Viiahmapata                Vijalapuram 
##                        648                       1243 
##            VIJAYA RAMPURAM                VIJAYAPURAM 
##                        441                       2967 
##            Vijayapuri Sowt                  Vijayarai 
##                       3415                       3063 
##      VijayaramaRaju Pettah             VijayaramPuram 
##                       2305                       1679 
##             VIJAYARAMPURAM           Vijayawada Urban 
##                        487                     516024 
##                 Vijinigiri              VIKKIRALAPETA 
##                        702                        250 
##               VikramaPuram                VikramPuram 
##                       2662                        373 
##                VIKRAMPURAM               Vikruthamala 
##                        354                       3229 
##                     Vilasa                VILASAVALLI 
##                       1783                       2032 
##             VILASKHANPALEM              Vilukanipalle 
##                        955                        638 
##                  Viluparti                     VIMJIM 
##                        597                       3152 
##               Vinayikpalli                    Vinduru 
##                        566                       2389 
##                 Vindyavasi                   Vingdapa 
##                        298                       1689 
##                  Vinjagiri                 VINJAMPADU 
##                         98                        412 
##                   Vinjamur               Vinjanampadu 
##                       7474                        907 
##                   Vinjaram                   VINJARAM 
##                        745                        840 
##               Vinjarampadu             Vinjavartipadu 
##                        580                        183 
##                    Vinjram                  Vinnakota 
##                        833                       1995 
##                  Vinnamala                  Vinukonda 
##                       2210                      31847 
##                  VINUKONDA                 Vipngandla 
##                       8552                       1477 
##                   Vipparla    Vipparlapalli Agraharam 
##                       5904                        716 
##             virabadrapuram                    Viranki 
##                        456                        766 
##                     Virava                   VIRAVADA 
##                       2145                       2135 
##                 VirlaDinne           Virupakshi Puram 
##                        215                        545 
##                Virupapalli                VIRUPAPURAM 
##                       3171                       2662 
##                   Viruvuru              Visakhapatnam 
##                       2841                     450500 
##              VISAKHAPATNAM       VISAKHAPATNAM (TOWN) 
##                     159735                      69707 
##                   Vishdala        Vishveshwarayapuram 
##                       1039                       2420 
##           VishwanadhaPalli           VishwanadhaPuram 
##                       3498                       4828 
##                VissaKoderu                Vissannapet 
##                       4196                       8189 
##            VISWANADHAPURAM                Visweswaram 
##                        317                        377 
##                    VITALAM                Vithalpuram 
##                        424                       1424 
##            VITTA YYA PALEM               VITTALAPURAM 
##                        227                        267 
##                 Vittapalli                    Vitturu 
##                        934                        512 
##               Vizianagaram                  Vobbanagi 
##                     128657                        713 
##               Vobhalypalem                   Vodipadu 
##                        602                        427 
##            VOLETIVARIPALEM                    VOMMALI 
##                       2039                       1844 
##                 Vommavaram                 VOMMAVARAM 
##                       1604                        765 
##                      Vommi             Voni Agraharam 
##                       2107                        142 
##                 Vontimitta                VOOTU PALLI 
##                       8420                       1167 
##                  Vubalanka                  Vuddavolu 
##                       6472                        575 
##                     vuderu                Vullibhadra 
##                        999                       1253 
##                VulliValasa                 Vuppalpadu 
##                        262                        254 
##               Vuppugunduru                   Vutukuru 
##                       3863                       5131 
##                Vuyyalawada                 Vuyyalwada 
##                       5122                       2054 
##                 Vyasapuram                 Wadalkunta 
##                       1023                       2162 
##                  WadValasa                   WadValli 
##                        223                        941 
##               Wai. AmPuram           Wai. Cherlopalli 
##                       1621                        920 
##             Wai.Kothapalli                     WaiVak 
##                       1159                       1953 
##                    Waltair              West Godavari 
##                        815                        976 
##                 West Gudur              WEST KANDRIKA 
##                       9879                       2476 
##              WEST KUNDURRU             WEST VARATHURU 
##                       1392                       1352 
##                    WoMangi                      Worli 
##                       3859                        393 
##                Y.RAMAVARAM                 y.s valasa 
##                       1262                        801 
##                 Y.SOLAMULA                Y.T.Cheruvu 
##                        690                       1777 
##                  Yachwaram                  YADA MARI 
##                        436                       5098 
##                     Yadaki               YADAVALLI-39 
##                        358                        766 
##                Yaddanapudi                     Yadiki 
##                        568                      12146 
##                   Yadvalli                    Yadvolu 
##                        911                       5294 
##                     Yadwad               Yagantipalle 
##                        519                       1022 
##           Yagnishettipalli                     Yajali 
##                        362                       2780 
##                    Yakmuru                   Yakshiri 
##                       1580                       2270 
##                  YALAKALLU               Yalamanchili 
##                       1013                       4358 
##                   Yalkurru                 Yallamanda 
##                        703                       5495 
##                YALLAMPALLI          YALLANKIVARIPALLI 
##                       1361                       1167 
##                 Yallanooru               Yallayapalem 
##                       4211                       5053 
##                   Yalwarru               Yam.Agrahram 
##                        744                       2094 
##              Yam.Rayapuram                Yam.V. Ngar 
##                       2631                       1387 
##             Yam.Yam. Halli                 yamalapeta 
##                        551                        302 
##                    Yamarru                  Yamavaram 
##                        430                        997 
##                    Yambram              Yamiganipalli 
##                        541                       1143 
##              YANADHI VETTU                 YANAKANDLA 
##                        691                       1909 
##                 Yanalpalli                 Yanamadala 
##                        808                       1502 
##                YANAMADURRU           Yanamalachintala 
##                       1749                        638 
##                 Yandagandi                  YANDAMURU 
##                       2668                       3156 
##                 Yandapalli                Yandrapalli 
##                       2743                       1143 
##                Yannekandla                Yaparlapadu 
##                        415                        467 
##                   Yapdinne             Yaramala palli 
##                       1127                        592 
##           Yaramaraju palle                  Yarazarla 
##                        935                       1352 
##                    Yarbadu                Yargtipalli 
##                       1015                        898 
##              Yarkannapalem      Yarkbhupati Agraharam 
##                        943                        399 
##                 Yarlagadda                 YARLAGADDA 
##                        825                        401 
##               YARLAM PALLI                  YARLAPUDI 
##                        985                        415 
##                Yarnagudena            YARR WARI PALLI 
##                       7703                       1317 
##          Yarrabommanhzhzhi                  Yarragudi 
##                       3268                       1363 
##                 Yarragunta            Yarraguntapalli 
##                       4675                       2090 
##         Yarramannugunthalu                Yarramapata 
##                        722                       2379 
##                Yarrampalli           YARRAMREDDIPALEM 
##                       1090                        799 
##              Yarrapotwaram              Yarrawaram-25 
##                       1095                       3166 
##               Yarrawaram 7          YARRAYYAGARIPALLI 
##                        708                        733 
##          Yata Kummaripalem                   Yatkallu 
##                       1126                       4781 
##            YATLABASIVALASA                    Yatluru 
##                        477                        741 
##                    Yatpaka                    YEDIDHA 
##                       1730                       8488 
##                Yedlurupadu                   Yedubadu 
##                        363                        844 
##          Yedugu rallapalli              Yegoti Valasa 
##                        907                        556 
##                    Yekkala                    Yekollu 
##                        546                       2280 
##                 Yellamilli                 YELLAPALLE 
##                       1128                        511 
##            YELLAREDDIPALLI                 YELLAVARAM 
##                        506                        741 
##               Yellovapalli                    Yelluru 
##                        344                        472 
##                 Yemmiganur                    Yendada 
##                      61918                       6417 
##                 Yendagandi                 Yendapalli 
##                        653                       2011 
##           YENDAPALLIVALASA                    Yenduva 
##                       1376                        499 
##              Yenetikothuru                 YENTRIKONA 
##                        247                       1235 
##                Yenugu Tuni                 Yenugubala 
##                        876                       1100 
##              YENUGULAPALEM                Yenugumarri 
##                        584                        789 
##                Yenugupalem                Yenugupalli 
##                       2113                       1889 
##                  Yenugupet            Yenuguvanilanka 
##                        136                       3101 
##                Yenuguvlasa                    Yeragam 
##                        513                       1034 
##                    Yerpedu                 Yerrabalem 
##                       2363                        375 
##                  yerragudi                  YERRAGUDI 
##                        572                        637 
##              YERRAGUDIPADU             Yerragudipalle 
##                       1385                       3244 
##            YERRAGUNTAPALLI                Yerraguntla 
##                        773                      26024 
##            YerraguntlaPadu            YERRAMACHUPALLI 
##                       1706                        620 
##                Yerramapata                YerramPalem 
##                        983                        650 
##                 Yerrawaram           YERUKUNAIDUPALEM 
##                       4001                        792 
##                  Yerupalli                      YERUR 
##                       1109                        825 
##             Yethurallapatu                      Yetur 
##                        294                        466 
##                     Yeturu                     Yiridi 
##                        721                        450 
##               Z Bennawaram                 Z.BHAVARAM 
##                        986                        929 
##                 Z.MEDAPADU                 Z.Mekapadu 
##                       1203                        484 
##                     ZADERU                     Zakeru 
##                        540                        736 
##              Zedwari palli                     ZINNAM 
##                        275                        709
```
