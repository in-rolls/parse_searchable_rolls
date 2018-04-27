## Arunachal Pradesh

Basic descriptive statistics about the data. And sanity checks.


```r
arunachal <- readr::read_csv("arunachal.csv")
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
nrow(arunachal)
```

```
## [1] 722952
```

Unique Values in Sex:


```r
# Unique values in sex
table(arunachal$sex)
```

```
## 
## Female   Male 
## 363888 359064
```

Summary of Age:


```r
# Age
summary(arunachal$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##     0.0    28.0    35.0    38.8    47.0   120.0      45
```

No. of characters in ID:

```r
# Length of ID
table(nchar(arunachal$id))
```

```
## 
##      4      5      6     10     16 
##      1      2      6 581038 141338
```

Number of characters in pin code:


```r
table(nchar(arunachal$pin_code))
```

```
## 
##      6 
## 719257
```


```r
# Net electors
sum(with(arunachal, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 719257
```

```r
nrow(arunachal)
```

```
## [1] 722952
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(arunachal$elector_name))
```

```
## 
##      3      4      5      6      7      8      9     10     11     12 
##    106   1444   2606   3162   4433  19769  70491 121251 137967 119299 
##     13     14     15     16     17     18     19     20     21     22 
##  87480  60478  36792  21560  13010   8439   5626   3646   2448   1358 
##     23     24     25     26     27     28     29     30     31     32 
##    773    375    204    108     61     25     17      8      6      6 
##     33     49 
##      2      1
```

```r
arunachal[which(nchar(arunachal$elector_name) < 4), "filename"]
```

```
## # A tibble: 106 x 1
##    filename        
##    <chr>           
##  1 AC008PART034.pdf
##  2 AC008PART034.pdf
##  3 AC008PART034.pdf
##  4 AC008PART034.pdf
##  5 AC001PART013.pdf
##  6 AC003PART011.pdf
##  7 AC008PART031.pdf
##  8 AC008PART031.pdf
##  9 AC008PART031.pdf
## 10 AC008PART031.pdf
## # ... with 96 more rows
```

Basic admin. units:

```r
table(arunachal$police_station)
```

```
## 
##       Along       Anini      Balemu     Balijan  Banderdewa       Basar 
##       23776        3446         414        7323        3497       11149 
##  Bhalukpong      Boleng     Bomdila    Bordumsa   Changlang Chayangtajo 
##        3211       12083        9606       10340       12588        6226 
##    Chowkham      Dambuk    Daporijo     Deomali      Dirang       Diyun 
##       12045        5166       22355        8529       13168        4846 
##     Doimukh   Dumporijo       Gensi   Hayuliang       Hunli    Itanagar 
##        6787       10992        3302       10649         944       27309 
##   Jairampur    Jengging   Kalaktang       Kamba    Kanubari      Kaying 
##        8193        2083        3929        6409        7794        4523 
##    Kharsang      Khonsa       Kimin   Kolorinag        Laju    Likabali 
##        7235       20478        4669       33966        5446        6488 
##    Liromoba    Longding       Lumla  Mahadevpur        Mebo    Mechukha 
##        2757        9834        7899       16197        9990        7290 
##        Miao Mukto(Jang)       Nacho  Naharlagun      Namsai        Nari 
##        7293        6630       10003       20581       20752        5964 
##     Nirjuli      Nyapin    Pasighat    Pongchau       Pumao        Raga 
##        4741        5976       20434       13383        2802        8082 
##       Roing      Ruksin     Rumgong        Rupa     Sagalee     Sangram 
##       15821       10289        5878       13411       12345        5205 
##     Seijosa       Seppa     Sunpura      Taliha        Tato      Tawang 
##        3420       31652        1646        9362        1405        9310 
##        Tezu      Tirbin      Tuting  Vijoynagar        XXXX      Yazali 
##       14390        5180        4412        2638        3695       14834 
##   Yingkiong      Yomcha        Ziro 
##       13529        2360       20598
```

```r
table(arunachal$mandal)
```

```
## 
##       Along       Anini       Basar      Boleng     Bomdila    Bordumsa 
##       23776        3446       16329       12083       22774       15186 
##   Changlang Chayangtajo    Chowkham      Dambuk    Daporijo     Deomali 
##       12588        6870       12045        5166       42709        9186 
##   Hayuliang       Hunli   Jairampur        Jang    Kanubari      Khonsa 
##       10649         944        8193        6630        7794       25267 
##   Koloriang    Likabali    Longding       Lumla  Mahadevpur    Mariyang 
##       33966        9790       26019        7899       16197        9278 
##        Mebo    Mechukha        Miao       Nacho      Namsai        Nari 
##        9990        8695       17166       10003       20752        5964 
##      Nyapin    Pasighat        Raga       Roing      Ruksin     Rumgong 
##       11181       20434        8082       15821       10289       10401 
##        Rupa     Sagalee       Seppa      Tawang        Tezu    Thrizino 
##       17754       87252       34428        9310       16036        3211 
##      Tuting   Yingkiong      Yomcha        Ziro 
##        4412        6334       11526       35432
```

```r
table(arunachal$district)
```

```
## 
##               ANJAW           CHANGLANG       DIBANG VALLEY 
##               10395               53858                3446 
##         EAST KAMENG          EAST SIANG        KURUNG KUMEY 
##               41766               58987               45147 
##               LOHIT            LONGDING LOWER DIBANG VALLEY 
##               16036               33813               21931 
##     LOWER SUBANSIRI              NAMSAI          PAPUM PARE 
##               43865               49663               84158 
##              TAWANG               TIRAP         UPPER SIANG 
##               23839               34453               19694 
##     UPPER SUBANSIRI         WEST KAMENG          WEST SIANG 
##               52564               42647               80653
```

```r
table(arunachal$main_town)
```

```
## 
##                            1300 CHAIN LABOUR CAMP 
##                                                 4 
##                                    14 KM PWD CAMP 
##                                               102 
##                       16TH MILE & TEA GARDEN AREA 
##                                               226 
##                            17TH MILE & MILLS AREA 
##                                               309 
##                            28 KM ROING HUNLI ROAD 
##                                                25 
##                                         28TH MILE 
##                                               394 
##                                          2ND MILE 
##                                               667 
##                             6 KM ROING HUNLI ROAD 
##                                                54 
##                                          6TH MILE 
##                                               152 
##                                73 KM JORAM(SHUIL) 
##                                               307 
##                                         A-2 BLOCK 
##                                               259 
##                                        A - SECTOR 
##                                              1535 
##                     A - SECTOR / PETROL PUMP AREA 
##                                               991 
##                                            ABANGO 
##                                               133 
##                                      ACHINGMURING 
##                                                78 
##                                  ADANE (EMBRANGO) 
##                                                35 
##                                       ADIPASI - I 
##                                               488 
##                                         AGINKONIA 
##                                               219 
##                                       AIR COMPLEX 
##                                               723 
##                                 AIR FIELD (LOWER) 
##                                               834 
##                                          AKINIRIN 
##                                               121 
##                                             AKOBE 
##                                                58 
##                                          ALC LINE 
##                                              1364 
##                                       ALINYE (LG) 
##                                               242 
##                                           ALOMBRO 
##                                                21 
##                                       ALUBARI (A) 
##                                               980 
##                                        ALUBARI(B) 
##                                               970 
##                                              AMBA 
##                                               900 
##                                             AMBAM 
##                                               319 
##                                              AMJI 
##                                               314 
##                                           AMLIANG 
##                                                85 
##                                        AMSUKPINJA 
##                                               276 
##                                             AMULI 
##                                                86 
##                                   ANELIH TOWNSHIP 
##                                               173 
##                                           ANGGING 
##                                                66 
##                                           ANGOLIN 
##                                                41 
##                                     ANGRIM VALLEY 
##                                               125 
##                                              ANGU 
##                                               957 
##                                             ANINI 
##                                               955 
##                                          ANKALING 
##                                               243 
##                                             ANPUM 
##                                               856 
##                                    AOHALI VILLAGE 
##                                               107 
##                                   APFC COLONY - I 
##                                               650 
##                                           APHUMNA 
##                                                56 
##                                              APOP 
##                                               292 
##                                          APP LINE 
##                                               862 
##                                           APRUNLI 
##                                                 6 
##                         APST COMPLEX / BAZAR AREA 
##                                               942 
##                                           ARANALO 
##                                               119 
##                                 ARANGO(HORUPAHAR) 
##                                               288 
##                                            ARANLI 
##                                                 6 
##                                             ARIBU 
##                                                74 
##                                            ARONLI 
##                                                26 
##                              ARUNACHAL UNIVERSITY 
##                                               549 
##                                            ARUNLI 
##                                                12 
##                                             ARZOO 
##                                               122 
##                                          ASHOMBRA 
##                                                57 
##                                             ATALI 
##                                                11 
##                                           ATHUNLI 
##                                                27 
##                                          ATTARANG 
##                                               150 
##                                             AUNYE 
##                                                15 
##                                             AWOKA 
##                                                17 
##                                         AYA MARDE 
##                                               190 
##                                         AYA NIRIN 
##                                                67 
##                                           AYAMARA 
##                                               164 
##                                     AYENG VILLAGE 
##                                               875 
##                                          B-SECTOR 
##                                               996 
##                          B - SECTOR / MARKET AREA 
##                                               634 
##                                             BABLA 
##                                               442 
##                                     BABUK VILLAGE 
##                                                68 
##                                     BADAK VILLAGE 
##                                               199 
##                                             BAGBI 
##                                               305 
##                                        BAGIASIYUM 
##                                               513 
##                                      BAGRA (HIGI) 
##                                               548 
##                                        BAGRA JEYE 
##                                               120 
##                                        BAGRA LIPU 
##                                               568 
##                                       BAGRA TAKPU 
##                                               330 
##                                             BALEK 
##                                               896 
##                                    BALEMU VILLAGE 
##                                               326 
##                                          BALINONG 
##                                               660 
##                                            BALISO 
##                                               206 
##                                  BALISORI VILLAGE 
##                                               141 
##                                        BALUPATHAR 
##                                               211 
##                              BAM VILLAGE PART - I 
##                                               557 
##                             BAM VILLAGE PART - II 
##                                               498 
##                                       BAMENG H.Q. 
##                                               262 
##                                             BAMIN 
##                                               750 
##                                         BANA CAMP 
##                                               175 
##                            BANDERDEWA (EAST SIDE) 
##                                               943 
##                            BANDERDEWA (WEST SIDE) 
##                                               850 
##                                           BANFERA 
##                                               565 
##                                            BANGGO 
##                                               325 
##                                            BANGTE 
##                                               253 
##                                       BANK TINALI 
##                                              1588 
##                            BANK/PO/HELIPAD COLONY 
##                                               565 
##                                  BANSKOTA (LOWER) 
##                                               697 
##                                  BANSKOTA (UPPER) 
##                                               943 
##                                            BARAFU 
##                                               182 
##                         BARAPANI / BARAPANI BAZAR 
##                                              1539 
##               BARAPANI BAZAR & VETERINARY COMPLEX 
##                                               958 
##                                         BARCHIPAM 
##                                               403 
##                                            BARING 
##                                               206 
##                                       BARIRIJO HQ 
##                                               624 
##                                            BARITO 
##                                                26 
##                                         BARO MILE 
##                                               147 
##                                    BASAR MCP / SE 
##                                               356 
##                              BASAR TOWN - I (MEN) 
##                                               452 
##                            BASAR TOWN - I (WOMEN) 
##                                               302 
##                                   BASAR TOWN - II 
##                                               938 
##                                         BASORNALO 
##                                               749 
##                                       BAT VILLAGE 
##                                               316 
##                                             BATOR 
##                                               190 
##                                             BAYOR 
##                                               129 
## BAZAR AREA/ MEDICAL COLONY/ ENQUIRY OFFICE COLONY 
##                                               924 
##                                        BAZAR LINE 
##                                               747 
##                                           BEDAGAM 
##                                                42 
##                                 BEGGING (LORGING) 
##                                                84 
##                                   BEGGING VILLAGE 
##                                               216 
##                                              BELO 
##                                               473 
##                                      BELO VILLAGE 
##                                                91 
##                                              BELU 
##                                               254 
##                                              BENE 
##                                               607 
##                                            BENGDE 
##                                               184 
##                                      BERA VILLAGE 
##                                               333 
##                            BEROM RIME / PIDI RIME 
##                                               105 
##                                            BERUNG 
##                                               432 
##                                        BETCHELING 
##                                               181 
##                                              BEYE 
##                                               244 
##                                            BEYONG 
##                                               269 
##                                        BHEKULIANG 
##                                               319 
##                                      BHISMAKNAGAR 
##                                                96 
##                                          BHOGAMUR 
##                                               721 
##                                            BICHOM 
##                                               512 
##                                      BIGI VILLAGE 
##                                                91 
##                                              BIGO 
##                                               381 
##                                        BIJOYPUR-I 
##                                               181 
##                                            BIMPAK 
##                                                91 
##                                              BINE 
##                                               297 
##                                   BINGUNG VILLAGE 
##                                               212 
##                                     BIRI PUNGRUNG 
##                                               368 
##                                              BIRU 
##                                               285 
##                                           BISHING 
##                                                88 
##                                           BIYANLI 
##                                                43 
##                                        BIZARI - A 
##                                               408 
##                                        BIZARI - B 
##                                               425 
##                                          BLEMLENG 
##                                               529 
##                                             BLONG 
##                                               178 
##                           BN COLONY / FISH MARKET 
##                                               849 
##                                               BOA 
##                                               210 
##                                     BOA SIMLA - I 
##                                               397 
##                                    BOA SIMLA - II 
##                                               400 
##                                         BOBIA - I 
##                                               379 
##                                     BODAK VILLAGE 
##                                               181 
##                                              BODO 
##                                               347 
##                                  BOGAPANI VILALGE 
##                                               136 
##                                    BOGDO PART - I 
##                                               536 
##                                   BOGDO PART - II 
##                                               429 
##                                             BOGNE 
##                                               110 
##                                     BOGNE VILLAGE 
##                                               782 
##                                      BOGO VILLAGE 
##                                               128 
##                                      BOGU VILLAGE 
##                                               143 
##                                              BOHA 
##                                               492 
##                                 BOJE-KIGI VILLAGE 
##                                               100 
##                                 BOJE LITE VILLAGE 
##                                               185 
##                                 BOJE PARE VILLAGE 
##                                                91 
##                                             BOKAR 
##                                               187 
##                                    BOKFOM VILLAGE 
##                                               155 
##                                      BOLE VILLAGE 
##                                               194 
##                            BOLENG TOWN H.Q. (N/W) 
##                                               877 
##                                             BOLIK 
##                                               467 
##                                       BOLUNG - II 
##                                               573 
##                                 BOMDILA URBAN - A 
##                                               948 
##                                 BOMDILA URBAN - B 
##                                               849 
##                                 BOMDILA URBAN - C 
##                                               535 
##                               BOMDILA URBAN - C(E 
##                                               557 
##                                 BOMDILA URBAN - D 
##                                               726 
##                                            BOMDIR 
##                                               498 
##                                             BOMDO 
##                                               277 
##                                              BOMI 
##                                               313 
##                                             BOMJA 
##                                               116 
##                                            BOMJIR 
##                                               214 
##                                             BOMNA 
##                                                58 
##                                     BOMTE VILLAGE 
##                                               181 
##                                              BONA 
##                                                21 
##                                          BONGLENG 
##                                               371 
##                                             BONIA 
##                                               640 
##                                      BOPU VILLAGE 
##                                               329 
##                                         BORAROPUK 
##                                               295 
##                                     BORDUMSA TOWN 
##                                               785 
##                                  BORDUMSA VILLAGE 
##                                               588 
##                                  BORDURIA VILLAGE 
##                                              1301 
##                                   BORGULI VILLAGE 
##                                               707 
##                                          BORISTUM 
##                                               223 
##                                           BORKHET 
##                                               277 
##                                BORORAKSAP VILLAGE 
##                                               132 
##                                          BORSATAM 
##                                               108 
##                                     BORUM VILLAGE 
##                                               725 
##                                           BOSIRAI 
##                                                96 
##                                            BOYING 
##                                               469 
##                                         BRAILIANG 
##                                               183 
##                                          BRALANYI 
##                                                21 
##                                            BRANGO 
##                                                76 
##                                            BRINLI 
##                                                59 
##                                     BROKPALENCHEN 
##                                               118 
##                                               BTK 
##                                               116 
##                                        BUBANG - I 
##                                                53 
##                                       BUBANG - II 
##                                               257 
##                                               BUI 
##                                               276 
##                                              BUKA 
##                                               211 
##                                           BUKSANG 
##                                               363 
##                                              BULU 
##                                                30 
##                                        BUMJIPANGA 
##                                               423 
##                                             BUMTE 
##                                               242 
##                                           BUMTENG 
##                                               384 
##                                          BURAGAON 
##                                               403 
##                                      BYALE SULUNG 
##                                               182 
##                                             BYASI 
##                                               258 
##                                        C - SECTOR 
##                                              1860 
##                             C - SECTOR BAZAR AREA 
##                                               950 
##                                         CF COLONY 
##                                               472 
##                                           CHABANG 
##                                               370 
##                                          CHACHING 
##                                               237 
##                                        CHAGLONGAM 
##                                               193 
##                             CHAILIANG (20TH MILE) 
##                                               251 
##                                            CHAKKA 
##                                                73 
##                                        CHAKMA - I 
##                                               451 
##                                           CHALLAN 
##                                               154 
##                                           CHAMBAB 
##                                                94 
##                                        CHAMELIANG 
##                                                92 
##                                          CHAMPING 
##                                               109 
##           CHAMRO VILLAGE INCLUDES TEA GARDEN AREA 
##                                               150 
##                                           CHANDAR 
##                                                72 
##                 CHANDRA NAGAR BAZAR / POWER HOUSE 
##                                               900 
##                                          CHANGLAI 
##                                                83 
##                       CHANGLANG AUDITORIUM (WEST) 
##                                               414 
##                   CHANGLANG BSB AUDITORIUM (EAST) 
##                                               535 
##                         CHANGLANG PART - I (EAST) 
##                                               522 
##                         CHANGLANG PART - I (WEST) 
##                                               354 
##                                        CHANGLIANG 
##                                               299 
##                                        CHANGPRONG 
##                                               328 
##                                           CHANGRA 
##                                               103 
##                                        CHANGUINTY 
##                                               173 
##                                             CHANU 
##                                               974 
##                                            CHARJU 
##                                                40 
##                                          CHARRONG 
##                                               129 
##                                             CHARU 
##                                               407 
##                                     CHASA VILLAGE 
##                                               807 
##                                  CHATTING VILLAGE 
##                                               623 
##                                          CHATTONG 
##                                               278 
##                                  CHAYANGTAJO H.Q. 
##                                               451 
##                                         CHEBAMARA 
##                                               340 
##                                             CHEGE 
##                                               117 
##                                           CHEGING 
##                                                96 
##                                             CHEKE 
##                                               276 
##                                             CHEKI 
##                                               314 
##                               CHEKORLOMBI VILLAGE 
##                                               252 
##                                            CHELLO 
##                                               510 
##                                            CHENGO 
##                                               157 
##                                CHENGTHANG VILLAGE 
##                                               103 
##                                            CHEPPE 
##                                                25 
##                                            CHESSA 
##                                               416 
##                                  CHETA - I(UPPER) 
##                                               702 
##                                            CHETIA 
##                                               153 
##                                            CHETUM 
##                                               173 
##                                             CHIDU 
##                                               103 
##                                          CHILLANG 
##                                               169 
##                                         CHILLIPAM 
##                                               116 
##                                     CHIMI VILLAGE 
##                                               144 
##                                           CHIMIRI 
##                                                28 
##                                     CHIMPU /APP B 
##                                              1492 
##                                            CHINGI 
##                                               175 
##                                         CHINGRING 
##                                               181 
##                                  CHINGRING MURING 
##                                               140 
##                                           CHINGSA 
##                                               209 
##                                   CHINKOI VILLAGE 
##                                               377 
##                                          CHINLANG 
##                                                24 
##                                            CHIPRU 
##                                               162 
##                                           CHIRONG 
##                                                89 
##                                           CHIZANG 
##                                               141 
##                                             CHOBA 
##                                               227 
##                                             CHOLO 
##                                               152 
##                               CHOMUITHONG VILLAGE 
##                                                72 
##                                 CHONGKHOW VILLAGE 
##                                               522 
##                                              CHOP 
##                                               182 
##                                           CHOPEHA 
##                                               408 
##                                            CHOPNU 
##                                               537 
##                                            CHOPSA 
##                                               218 
##                                             CHOTE 
##                                               221 
##                                        CHOWALIANG 
##                                                77 
##                                          CHOWGONG 
##                                                16 
##                            CHOWKDOK (RANGKATU-II) 
##                                               180 
##                          CHOWKHAM-I (MANPHAKTANG) 
##                                               559 
##                                     CHOWKHAM - II 
##                                               372 
##                                    CHOWKHAM - III 
##                                               573 
##                                     CHOWKHAM - IV 
##                                               970 
##                        CHOWKHAM - V(A)(GUNANAGAR) 
##                                               669 
##                        CHOWKHAM - V(B)(GUNANAGAR) 
##                                               751 
##                                        CHUAKAMSAR 
##                                                49 
##                                              CHUG 
##                                               441 
##                                            CHULLA 
##                                               247 
##                                            CHULYU 
##                                               307 
##                                          CHUMBANG 
##                                               230 
##                                          CHUMBUNG 
##                                               118 
##                              CHUN (POTIN) VILLAGE 
##                                               133 
##                                           CHURONI 
##                                                23 
##                                       CLUB COLONY 
##                                               657 
##                                 COFFEE PLANTATION 
##                                                65 
##                  COOPERATIVE LINE ,ROING - II (A) 
##                                               373 
##                                      CRAFT CENTRE 
##                                               501 
##                                        D - SECTOR 
##                                              1316 
##          D - SECTOR / DOORDARSHAN / POSTAL COLONY 
##                                               783 
##                                 D - SECTOR COLONY 
##                                               497 
##                                      D.N. COLLEGE 
##                                               936 
##                               D.P.T.E. OYAN (N/W) 
##                                               373 
##                               D.P.T.E. OYAN (S/W) 
##                                               238 
##                               DABA GAMLIN VILLAGE 
##                                               115 
##                                   DADAM I VILLAGE 
##                                               703 
##                                  DADAM II VILLAGE 
##                                               416 
##                                              DADI 
##                                               106 
##                                  DAFLAGARH FOREST 
##                                               432 
##                                             DAFRI 
##                                               163 
##                                              DAGU 
##                                               449 
##                                               DAI 
##                                               161 
##                                             DAKPE 
##                                               372 
##                                       DALBING - I 
##                                               294 
##                                      DALBING - II 
##                                               324 
##                                      DALI VILLAGE 
##                                               400 
##                                            DAMBUK 
##                                               582 
##                               DAMDA DEBUK VILLAGE 
##                                               197 
##                                DAMDA DEKU VILLAGE 
##                                               169 
##                                         DAMRO - I 
##                                               450 
##                                       DAMRO - III 
##                                               369 
##                                           DAMSITE 
##                                               741 
##                                           DANGLAT 
##                                                84 
##                                 DANGLAT (32 MILE) 
##                                               288 
##                                          DANGSING 
##                                                64 
##                                              DAPI 
##                                               690 
##                                            DAPKHU 
##                                               207 
##                                 DAPORIJO EAST - A 
##                                               744 
##                                 DAPORIJO EAST - B 
##                                               510 
##                                 DAPORIJO EAST - C 
##                                               733 
##                                 DAPORIJO EAST - D 
##                                               774 
##                                 DAPORIJO WEST - A 
##                                               451 
##                                 DAPORIJO WEST - B 
##                                               322 
##                                 DAPORIJO WEST - C 
##                                               724 
##                                 DAPORIJO WEST - D 
##                                               705 
##                                        DARAK CAMP 
##                                               273 
##                                             DARBU 
##                                               197 
##                                              DARE 
##                                               570 
##                                              DARI 
##                                               563 
##                            DARKA VILLAGE PART - I 
##                                               876 
##                           DARKA VILLAGE PART - II 
##                                               667 
##                                           DARLONG 
##                                               696 
##                                        DARMO - II 
##                                               337 
##                                         DASATHONG 
##                                               950 
##                                              DASI 
##                                               581 
##                          DCS/ADCS WITH RWD COLONY 
##                                               629 
##                                DEBAN TOURIST CAMP 
##                                                41 
##                                            DEBING 
##                                               540 
##                                             DEBOM 
##                                               148 
##                                      DECHENGTHANG 
##                                               369 
##                                            DEDOLO 
##                                               402 
##                                              DEDU 
##                                               171 
##                                              DEED 
##                                               403 
##                                        DEED RAKHE 
##                                               349 
##                                             DEGAM 
##                                               163 
##                                              DEGO 
##                                               205 
##                                              DEKE 
##                                               549 
##                                         DELLIPEJI 
##                                               437 
##                                               DEM 
##                                               572 
##                                          DEMASANG 
##                                                73 
##                                            DENGKA 
##                                               206 
##                                    DENGZI VILLAGE 
##                                               341 
##                                  DENIMISA VILLAGE 
##                                                67 
##                                             DENLO 
##                                               217 
##                                           DEOBEEL 
##                                               998 
##                                  DEOMALI BLOCK-IV 
##                                               558 
##                              DEOMALI TOWN BLOCK-I 
##                                               990 
##                            DEOMALI TOWN BLOCK-III 
##                                               781 
##                           DEOMALI TOWN BLOCK - II 
##                                               804 
##                             DEOMALI TOWN BLOCK -V 
##                                               575 
##                                              DEPI 
##                                               442 
##                                          DEPIMOLI 
##                                               186 
##                                            DESALI 
##                                               227 
##                                             DETAK 
##                                               163 
##                                         DHARAMPUR 
##                                               516 
##                                    DHARAMPUR - II 
##                                                95 
##                                            DIBBIN 
##                                               219 
##                                      DIBE VILLAGE 
##                                                34 
##                                           DIBRICK 
##                                               137 
##                                            DIGBAK 
##                                               158 
##                                           DIGGING 
##                                               175 
##                                           DIGNIUM 
##                                               351 
##                                         DIKALMUKH 
##                                               199 
##                                         DIKHIYANG 
##                                                51 
##                                            DIKSHI 
##                                                50 
##                                           DILLING 
##                                                37 
##                                             DIMWE 
##                                                74 
##                                       DINCHANGPAM 
##                                                60 
##                               DINGLIANG (TIDDING) 
##                                                31 
##                                      DIPA VILLAGE 
##                                               401 
##                                             DIPIK 
##                                               158 
##                                        DIPU LAMGU 
##                                               276 
##                                        DIRAK MIRI 
##                                               292 
##                                      DIRAK PATHAR 
##                                               371 
##                          DIRANG H.Q. (EAST WING). 
##                                               895 
##                           DIRANG H.Q. (WEST WING) 
##                                               967 
##                        DIRANG VILLAGE (EAST WING) 
##                                               489 
##                         DIRANG VILLAGE(WEST WING) 
##                                               563 
##                                              DIRI 
##                                               261 
##                                           DISHING 
##                                                14 
##                                      DISI VILLAGE 
##                                               267 
##                                           DITCHIK 
##                                               408 
##                               DITE - DIME VILLAGE 
##                                                74 
##                                          DIYUN IB 
##                                                30 
##                                    DIYUN TOWNSHIP 
##                                               831 
##                                        DIZANGONIA 
##                                                39 
##                                              DODO 
##                                               380 
##                                    DOIDAM VILLAGE 
##                                               318 
##                                           DOIMARA 
##                                               110 
##                                              DOJE 
##                                               616 
##                                              DOKA 
##                                               261 
##                                 DOKO POTU VILLAGE 
##                                               250 
##                                             DOKRE 
##                                               228 
##                                             DOKUM 
##                                               318 
##                                              DOLO 
##                                               221 
##                                          DOLORIPU 
##                                                61 
##                                           DOMDILA 
##                                               303 
##                                               DON 
##                                               245 
##                                        DONGMARENG 
##                                               394 
##                                  DONGRONG VILLAGE 
##                                               151 
##                                          DONIGAON 
##                                               296 
##                                             DONLI 
##                                                91 
##                DONYI - POLO VIDHYA BHAWAN COMPLEX 
##                                               688 
##                                            DOPOWA 
##                                                16 
##                                        DORJELLING 
##                                               371 
##                                    DOSING VILLAGE 
##                                               201 
##                                              DOTE 
##                                               260 
##                                             DOYOM 
##                                               157 
##                                            DUCHOK 
##                                               239 
##                                         DUDUNGHAR 
##                                               386 
##                                              DUGI 
##                                               167 
##                                               DUI 
##                                               479 
##                                         DUILINGDI 
##                                               189 
##                                              DUKU 
##                                               133 
##                                              DULA 
##                                               166 
##                                             DULOM 
##                                               415 
##                                      DUMBA MOSANG 
##                                               254 
##                                         DUMPANI-I 
##                                               210 
##                                         DUMPATHAR 
##                                               289 
##                                  DUMPORIJO HQ - I 
##                                               541 
##                                 DUMPORIJO HQ - II 
##                                               585 
##                                             DUMSI 
##                                               281 
##                                            DUNDRI 
##                                                31 
##                                            DUNGRI 
##                                               119 
##                                            DUNGSE 
##                                               640 
##                                             DUPIT 
##                                               361 
##                                      DUPU VILLAGE 
##                                               125 
##                                         DURALIANG 
##                                               157 
##                                         DURPA - I 
##                                               716 
##                                    DURPAI VILLAGE 
##                                               287 
##                                   DURPANG (NISHI) 
##                                               280 
##                                           DUTHUNG 
##                                                80 
##                                             DUTTA 
##                                               736 
##                   E - SECTOR EAST SIDE/ESS SECTOR 
##                                               904 
##                                E - SECTOR EASTERN 
##                                               992 
##                       E - SECTOR FOREST PARK AREA 
##                                               970 
##                                E - SECTOR WESTERN 
##                                               642 
##                                             EBIYA 
##                                               245 
##                                               EBO 
##                                               149 
##                                           EBRANLI 
##                                                51 
##                         ECHI-SIKU (LOWER) VILLAGE 
##                                                82 
##                                 ECHICHIKU VILLAGE 
##                                               371 
##                                  EDUCATION COLONY 
##                                               966 
##                                              EFFA 
##                                               221 
##                                          EGO CAMP 
##                                                78 
##                                             EIYUM 
##                                               244 
##                                          EKHATAYA 
##                                               317 
##                                    ELEPHANT FLAT. 
##                                               106 
##                                             ELOPE 
##                                                92 
##                                            EMBONG 
##                                               110 
##                                         EMBORIANG 
##                                               193 
##                                             EMCHI 
##                                               479 
##                                           EMPHONG 
##                                               272 
##                                            EMPHUM 
##                                               247 
##                                             EMULI 
##                                                91 
##                                             EMUYI 
##                                                50 
##                                ENGINEERING COLONY 
##                                               756 
##                                           ENGOLIN 
##                                                 7 
##                                            EPANLI 
##                                                40 
##                                             ERBUK 
##                                               520 
##                                             ERING 
##                                               455 
##                                 ESHIKARTE VILLAGE 
##                                               345 
##                                  ESSIRITE VILLAGE 
##                                               122 
##                                              ESSO 
##                                               119 
##                                             ETABE 
##                                               114 
##                                       ETALIN B.P. 
##                                               202 
##                                            EYANLI 
##                                                64 
##                                               EYI 
##                                               449 
##                                        F - SECTOR 
##                                               538 
##                        F - SECTOR COLONY,ITANAGAR 
##                                               695 
##                                           FENGCHE 
##                                               255 
##                                             FLAGO 
##                                               251 
##                                     FOREST COLONY 
##                                               393 
##                         FOREST COLONY(G - SECTOR) 
##                                               962 
##                                              FUBA 
##                                               654 
##                                        G - SECTOR 
##                                              1598 
##                                 G -EXTENSION / SP 
##                                              1449 
##                                       G EXTENSION 
##                                               969 
##                                               GAA 
##                                               303 
##                                               GAB 
##                                               106 
##                                 GADI MESI VILLAGE 
##                                               225 
##                                     GADUM VILLAGE 
##                                               259 
##                                      GAKO VILLAGE 
##                                               322 
##                                           GALENJA 
##                                               435 
##                                      GALU VILLAGE 
##                                               114 
##                                    GAMENG VILLAGE 
##                                               153 
##                                              GAMI 
##                                               182 
##                                    GAMKAK VILLAGE 
##                                               250 
##                                          GAMLIANG 
##                                               102 
##                              GANDHIGRAM (SIDIKUH) 
##                                               978 
##                               GANGA BLOCK 1 AND 2 
##                                               398 
##                                           GANGNEE 
##                                               198 
##                                             GANTE 
##                                               327 
##                                              GAPO 
##                                               212 
##                                      GARU VILLAGE 
##                                               142 
##                                 GARUBANDHA FOREST 
##                                               396 
##                                   GASHENG VILLAGE 
##                                               243 
##                                      GATE VILLAGE 
##                                               148 
##                                           GECHING 
##                                               211 
##                                      GEKU - KUMKU 
##                                               452 
##                                      GEKU - PERAM 
##                                               502 
##                                         GEKU H.Q. 
##                                               552 
##                                           GELLING 
##                                               237 
##                                  GEMOTALI VILLAGE 
##                                               253 
##                                        GENSI TOWN 
##                                               793 
##                                             GETTE 
##                                               393 
##                                        GIAMUKRIJO 
##                                               120 
##                                              GIBA 
##                                               392 
##                                           GIDDING 
##                                               560 
##                                            GIKUNG 
##                                               169 
##                                             GIMBA 
##                                               397 
##                                         GING-MURI 
##                                               275 
##                                            GINGBA 
##                                               215 
##                                            GINGLO 
##                                               188 
##                                             GISPU 
##                                               360 
##                                         GITE BAGE 
##                                               144 
##                                        GLOTONGLAT 
##                                                42 
##                                             GOBUK 
##                                               427 
##                                         GOGNE DUI 
##                                                77 
##                                     GOGRA VILLAGE 
##                                               413 
##                                GOHPUR TINALI AREA 
##                                               952 
##                                          GOILIANG 
##                                               118 
##                                              GOJU 
##                                               672 
##                                             GOMIN 
##                                                44 
##                                           GOMKANG 
##                                               313 
##                                          GONGKHAR 
##                                               285 
##                                 GORBOW (JAMIYANG) 
##                                                74 
##                                      GORI VILLAGE 
##                                               952 
##                                     GORLUNG (S/W) 
##                                               544 
##                                            GOSANG 
##                                               188 
##                             GREFF CAMP ARE,EZENGO 
##                                               627 
##                                        GSI COLONY 
##                                               310 
##                                             GUCHI 
##                                               274 
##                                           GUMSING 
##                                               177 
##                                             GUMTE 
##                                               160 
##                                          GUMTHUNG 
##                                                33 
##                                         GUMTO - I 
##                                               442 
##                                           GUMTUNG 
##                                               119 
##                                            GUNGTE 
##                                               536 
##          GURUDWARA COLONY UPTO DCS OFFICE COMPLEX 
##                                               640 
##                                            GYAMAR 
##                                               172 
##                                          GYAMDONG 
##                                               232 
##                                           GYASING 
##                                               302 
##                                        H - SECTOR 
##                                               702 
##                                                HA 
##                                               184 
##                                             HABIA 
##                                                81 
##                                             HADAP 
##                                               119 
##                                        HALAIKRONG 
##                                               106 
##                                            HALENG 
##                                                51 
##                                         HAMALIANG 
##                                               132 
##                                          HAMATONG 
##                                                52 
##                                        HAMBAPINDA 
##                                               268 
##                                        HANALTHUNG 
##                                               101 
##                                            HANING 
##                                               142 
##                                            HANKAR 
##                                               249 
##                                             HARAK 
##                                               123 
##                                          HARI - A 
##                                               802 
##                                          HARI - B 
##                                               714 
##                                          HARI - C 
##                                               789 
##                                         HARIPUR-I 
##                                               278 
##                                     HASSE - RUSSA 
##                                               406 
##                                          HATIDUBA 
##                                               162 
##                                        HAWAI H.Q. 
##                                               894 
##                                    HAYULIANG TOWN 
##                                               917 
##                                        HDS COLONY 
##                                               758 
##                                            HEBANG 
##                                               574 
##                                              HEMI 
##                                               174 
##                                         HEMOIBUNG 
##                                               401 
##                                            HERONG 
##                                                79 
##                                      HETLONG VILL 
##                                                93 
##                                            HETMAN 
##                                                89 
##                                              HIBA 
##                                               194 
##                                             HIGIO 
##                                               220 
##                                          HIJA - I 
##                                               849 
##                                         HIJA - II 
##                                               902 
##                                          HILL TOP 
##                                               602 
##                                             HINJU 
##                                               159 
##                            HIPPING KARBAK VILLAGE 
##                                               112 
##                                             HIPPO 
##                                                37 
##                                              HIRI 
##                                               130 
##                                             HIRIK 
##                                               324 
##                                           HISSANG 
##                                               518 
##                                              HIYA 
##                                               729 
##                                    HOLLONGI NISHI 
##                                               690 
##                                              HOMI 
##                                               457 
##                                              HONE 
##                                               104 
##                                          HONG - A 
##                                               855 
##                                          HONG - B 
##                                               964 
##                                          HONG - C 
##                                               549 
##                                          HONG - D 
##                                               527 
##                                            HONKAP 
##                                               294 
##                                           HOONGLA 
##                                               367 
##                                        HORU PUTUK 
##                                               135 
##                                           HOSTLAM 
##                                                93 
##                                              HOTE 
##                                                74 
##                                        HSS COLONY 
##                                               708 
##                                          HUILIANG 
##                                                99 
##                                     HUKAN VILLAGE 
##                                               444 
##                                            HUKANI 
##                                                20 
##                                             HUNLI 
##                                               150 
##                                         HUSSIGAON 
##                                                78 
##                                             IDILI 
##                                                31 
##                                             IDULI 
##                                               469 
##                                   INDUSTRIAL AREA 
##                                               697 
##                                             INJAN 
##                                               817 
##                                              INJU 
##                                                71 
##                                             INNAO 
##                                               652 
##                                      INNAO PATHAR 
##                                               154 
##                                              INSA 
##                                                34 
##                                              IRGO 
##                                               191 
##                                            ITHILI 
##                                                58 
##                               ITI / FOREST COLONY 
##                                               299 
##                                            J.N.C. 
##                                               427 
##                                  JADTHUNG VILLAGE 
##                                                65 
##                                      JAGAN VILLGE 
##                                               466 
##                                            JAIPUR 
##                                               978 
##                                         JAKSITARA 
##                                               443 
##                                         JAMBUPANI 
##                                                32 
##                                      JAMIRI POINT 
##                                               240 
##                                         JANACHING 
##                                               178 
##                                             JANBO 
##                                               204 
##                                            JANGDA 
##                                               279 
##                                              JATE 
##                                                 4 
##                                         JAWA CAMP 
##                                               246 
##                                     JAYANG BAGANG 
##                                               347 
##                                           JAYANTI 
##                                               142 
##                                          JEJUDADA 
##                                               289 
##                                              JEKE 
##                                               289 
##                                              JEKO 
##                                               208 
##                                             JELLY 
##                                               317 
##                                          JENGGING 
##                                               353 
##                                             JERAM 
##                                               459 
##                                      JERIGAON - A 
##                                               360 
##                                           JERLING 
##                                               338 
##                                              JERU 
##                                               247 
##                                               JHA 
##                                               117 
##                                           JIA - I 
##                                               540 
##                                          JIA - II 
##                                               484 
##                                         JIA - III 
##                                               295 
##                                            JIGAON 
##                                               365 
##                                              JIGI 
##                                               543 
##                                          JIMBARAI 
##                                               512 
##                                      JIME VILLAGE 
##                                                90 
##                                            JIRDIN 
##                                               515 
##                                              JITU 
##                                               121 
##                                            JOKHIO 
##                                               165 
##                                       JOLLANG - I 
##                                               785 
##                                             JOLLY 
##                                               408 
##                                JOMLO-BARI VILLAGE 
##                                               264 
##                               JOMLO-MOBUK VILLAGE 
##                                               108 
##                              JOMLO-MONGKU VILLAGE 
##                                               509 
##                                      JOMO VILLAGE 
##                                               643 
##                                             JOMOH 
##                                               359 
##                                          JONA-III 
##                                               976 
##                                           JONA-IV 
##                                               264 
##                                          JONA - I 
##                                               810 
##                                        JONGJIHAVI 
##                                               239 
##                                      JONGLIPATHAR 
##                                                61 
##                                       JONGPHOHATE 
##                                               219 
##                                           JONGRAM 
##                                               120 
##                                             JORAM 
##                                               464 
##                                   JORSING VILLAGE 
##                                               174 
##                                              JORU 
##                                               390 
##                                       JOTTE CHEDA 
##                                               217 
##                                   JUMDANG VILLAGE 
##                                                60 
##                       JUNGMAICHUNG (RANGKATU-III) 
##                                                87 
##                                    JUNGMAISUNG II 
##                                                69 
##                                           JUNGPAM 
##                                               159 
##                                        JYOTINAGAR 
##                                               351 
##                                        JYOTIPUR-I 
##                                               344 
##                                      JYOTSNAPUR-I 
##                                               250 
##                                            KABANG 
##                                                38 
##                                              KABU 
##                                               840 
##                                             KACHA 
##                                                71 
##                                     KADAI VILLAGE 
##                                               126 
##                                          KADASILA 
##                                                74 
##                             KADEYA (BANA VILLAGE) 
##                                               235 
##                                             KAFLA 
##                                               193 
##                                      KAGI VILLAGE 
##                                               132 
##                                      KAIKHEPATHAR 
##                                               464 
##                                    KAIMAI VILLAGE 
##                                               817 
##                                KAIMOI VILLAGE - I 
##                                               461 
##                                              KAJI 
##                                               125 
##                                             KAKKI 
##                                               162 
##                                             KAKOI 
##                                               535 
##                                           KAKUKAO 
##                                               404 
##                                    KALAKTANG TOWN 
##                                               656 
##                                 KALAKTANG VILLAGE 
##                                               172 
##                                      KALEK MIRBUK 
##                                               179 
##                                       KALING - II 
##                                               116 
##                                    KALLEK VILLAGE 
##                                                80 
##                                            KALONG 
##                                               595 
##                                       KAMALANCHEN 
##                                               172 
##                                             KAMBA 
##                                               456 
##                                           KAMBANG 
##                                               112 
##                                     KAMBU VILLAGE 
##                                               478 
##                                   KAMCHAM VILLAGE 
##                                               222 
##                          KAMDAK (EVEREST) VILLAGE 
##                                               196 
##                                        KAMENGBARI 
##                                               152 
##                              KAMHUA-NOKSA VILLAGE 
##                                               497 
##                            KAMHUA NOKNU-I VILLAGE 
##                                               487 
##                           KAMHUA NOKNU-II VILLAGE 
##                                               468 
##                                             KAMJA 
##                                               148 
##                                KAMKI DEGO VILLAGE 
##                                               412 
##                                        KAMKI FARM 
##                                               100 
##                                     KAMKI VILLAGE 
##                                               465 
##                                    KAMKUH - RUSSA 
##                                               164 
##                                     KAMLANG NAGAR 
##                                                90 
##                                            KAMLAT 
##                                                97 
##                                             KAMNU 
##                                               103 
##                                           KAMPONG 
##                                                56 
##                                             KAMRA 
##                                                78 
##                                           KAMRUNG 
##                                               277 
##                                            KAMSAR 
##                                                88 
##                                      KANE VILLAGE 
##                                                27 
##                                           KANGKHO 
##                                                82 
##                                          KANGKONG 
##                                               674 
##                                    KANGKU VILLAGE 
##                                               408 
##                                            KANING 
##                                                78 
##                                              KANO 
##                                                61 
##                                           KANTANG 
##                                                48 
##                                     KANUBARI H.Q. 
##                                               559 
##                                         KAOPATANI 
##                                               804 
##                                      KAPU VILLAGE 
##                                               381 
##                                          KAPUDADA 
##                                               336 
##                                        KARANGONIA 
##                                               145 
##                                          KARARAMU 
##                                               140 
##                              KARBAK BOYOR VILLAGE 
##                                               101 
##                              KARBAK GEIYI VILLAGE 
##                                               287 
##                               KARBAK MOLI VILLAGE 
##                                               154 
##                                     KARDO VILLAGE 
##                                               163 
##                                              KARE 
##                                               162 
##                                             KARHE 
##                                               142 
##                                             KARKO 
##                                               607 
##                                             KARLE 
##                                               450 
##                                              KARO 
##                                               297 
##                                             KAROI 
##                                               380 
##                                  KARSINGSA (EAST) 
##                                               949 
##                                  KARSINGSA (WEST) 
##                                               613 
##                                         KASANGLAT 
##                                                71 
##                                        KATAN H.Q. 
##                                               370 
##                                            KATHAN 
##                                                92 
##                           KATO / NEW KATO VILLAGE 
##                                               381 
##                                          KAYANADI 
##                                               156 
##                                    KAYI ( BOTAK ) 
##                                               197 
##                              KAYI (DUMDE) VILLAGE 
##                                               111 
##                                  KAYI(MEKA - III) 
##                                               282 
##                                       KAYING CAMP 
##                                               392 
##                           KAYING VILLAGE / TUYING 
##                                               542 
##                                              KEBA 
##                                              1129 
##                                            KEBALI 
##                                                94 
##                             KEBANG (RADA) VILLAGE 
##                                               134 
##                             KEBANG (SOLE) VILLAGE 
##                                               136 
##                                    KEBANG VILLAGE 
##                                               170 
##                                              KEBI 
##                                               249 
##                                             KEBIA 
##                                                52 
##                                           KEMBING 
##                                               313 
##                                           KENGKHU 
##                                               228 
##                                     KENON VILLAGE 
##                                               215 
##                                KERANG - I VILLAGE 
##                                               306 
##                               KERANG - II VILLAGE 
##                                               247 
##                                         KESI TALI 
##                                                38 
##                                      KESSE BAGANG 
##                                               194 
##                                          KHACHANG 
##                                               449 
##                             KHAHINALLA (MADHUBAN) 
##                                                25 
##                             KHALEGA / METENGLIANG 
##                                                34 
##                                          KHALIBOK 
##                                               162 
##                                    KHAMDU VILLAGE 
##                                               142 
##                                       KHAMLAIGLAT 
##                                                83 
##                                 KHANU VILLAGE - I 
##                                               470 
##                                KHANU VILLAGE - II 
##                                               453 
##                                          KHARDUNG 
##                                               303 
##                              KHARMANG / KELEKTANG 
##                                               409 
##                                    KHARSANG JUGLI 
##                                               885 
##                                   KHARSANG TINALI 
##                                               972 
##                                     KHARSANG TOWN 
##                                              1649 
##                                          KHARTENG 
##                                               540 
##                                          KHARTOOT 
##                                               516 
##                                           KHARUNG 
##                                               134 
##                                     KHASA VILLAGE 
##                                               857 
##                                            KHASSO 
##                                               268 
##                                            KHAUJI 
##                                               585 
##                                         KHAZALONG 
##                                               181 
##                                             KHEEL 
##                                               386 
##                               KHELA RONYA VILLAGE 
##                                                95 
##                                     KHELA VILLAGE 
##                                               413 
##                                          KHELLONG 
##                                               519 
##                                           KHEMLEE 
##                                               487 
##                                           KHENEWA 
##                                               326 
##                                           KHERANG 
##                                               335 
##                                    KHEREM KACHARI 
##                                               215 
##                                       KHEREM MURA 
##                                               411 
##                                        KHEREMBISA 
##                                               339 
##                                              KHET 
##                                               459 
##                                     KHETI VILLAGE 
##                                               816 
##                                         KHIMIYANG 
##                                               403 
##                                           KHINMEY 
##                                               104 
##                                            KHIRMU 
##                                               373 
##                                        KHOBLETANG 
##                                               149 
##                                           KHODASO 
##                                               235 
##                                    KHOGLA VILLAGE 
##                                               441 
##                                            KHOINA 
##                                               172 
##                              KHORALIANG / PANBARI 
##                                               353 
##                                     KHOUJI PATHAR 
##                                               586 
##                                KHOWATHONG VILLAGE 
##                                               185 
##                                       KHRANGLIANG 
##                                                78 
##                                         KHUCHEP-I 
##                                               182 
##                                        KHUCHEP-II 
##                                               128 
##                                         KHUILIANG 
##                                                92 
##                                       KHUMCHAYKHA 
##                                               163 
##                                             KHUPA 
##                                               334 
##                                             KHUPI 
##                                               270 
##                                          KIBITHOO 
##                                               134 
##                                             KICHO 
##                                               477 
##                                             KILLO 
##                                               252 
##                                      KIMI VILLAGE 
##                                               443 
##                                             KIMIN 
##                                               513 
##                                     KIMIN-II KUDH 
##                                               349 
##                                         KIMIN HQ. 
##                                               465 
##                                     KIYIT VILLAGE 
##                                               929 
##                                             KODAK 
##                                               294 
##                                            KOKILA 
##                                               723 
##                                  KOLAGAON VILLAGE 
##                                               378 
##                                    KOLORIANG TOWN 
##                                               444 
##                                            KOLUNG 
##                                                49 
##                                             KOMBO 
##                                               679 
##                        KOMBO HYDEL /YEGGO VILLAGE 
##                                               180 
##                                       KOMBO MOBUK 
##                                               620 
##                                      KOMBO RAGLAM 
##                                               165 
##                                     KOMKAR RASING 
##                                               345 
##                            KOMSING (KARO) VILLAGE 
##                                               342 
##                                   KOMSING (KUMKU) 
##                                               258 
##                                   KONGKUL VILLAGE 
##                                               123 
##                                    KONGRA/ MATONG 
##                                                72 
##                                            KONGSA 
##                                               293 
##                                     KONNU VILLAGE 
##                                               644 
##                                     KONSA VILLAGE 
##                                               489 
##                                            KOPILA 
##                                               293 
##                                              KOPU 
##                                                99 
##                                            KORANG 
##                                               246 
##                                            KORAPU 
##                                               200 
##                                           KORAYAR 
##                                               301 
##                                            KORENG 
##                                               212 
##                                            KORONU 
##                                               442 
##                                              KOTO 
##                                               152 
##                                             KOYAM 
##                                               309 
##                                         KOYU H.Q. 
##                                                28 
##                                      KOYU VILLAGE 
##                                               359 
##                                          KRELLING 
##                                               121 
##                                          KREMAPAO 
##                                               324 
##                                        KRISHNAPUR 
##                                               476 
##                                            KROMNA 
##                                               177 
##                                            KRONLI 
##                                                11 
##                                           KROSANG 
##                                                49 
##                                            KROWTY 
##                                                34 
##                                           KUGGING 
##                                               140 
##                                      KUGI (POMTE) 
##                                               670 
##                                          KUGITAGO 
##                                               490 
##                                           KULLUNG 
##                                               415 
##                                   KUMARI ADIVASHI 
##                                               734 
##                                    KUMARI KHAMPTI 
##                                               650 
##                                     KUMUNG PATHAR 
##                                               288 
##                                            KUNGBA 
##                                               176 
##                                    KUNTOR VILLAGE 
##                                               243 
##                                 KUNU YAMI VILLAGE 
##                                               207 
##                                          KUPORIJO 
##                                               288 
##                                            KUTUNG 
##                                               296 
##                                            KYAMDO 
##                                               133 
##                                               LAA 
##                                               571 
##                                              LABA 
##                                               217 
##                                    LACHING BAGANG 
##                                               332 
##                                           LACHONG 
##                                                30 
##                                    LACHUNG YANGJE 
##                                               127 
##                                              LADA 
##                                               436 
##                                             LAGAM 
##                                                28 
##                              LAGGI GAMLIN VILLAGE 
##                                               274 
##                                  LAHO VILLAGE - I 
##                                               501 
##                                 LAHO VILLAGE - II 
##                                               328 
##                                             LAIGI 
##                                               154 
##                                           LAIMOYA 
##                                               195 
##                                 LAJU - II VILLAGE 
##                                               574 
##                                         LAJU H.Q. 
##                                               805 
##                                      LAKBAK GONGO 
##                                               270 
##                                           LAKTONG 
##                                               444 
##                                            LALUNG 
##                                               763 
##                                         LAMALIANG 
##                                                34 
##                                            LAMDIK 
##                                                74 
##                                     LAMLO VILLAGE 
##                                               149 
##                                     LAMSA VILLAGE 
##                                               307 
##                                             LAMTA 
##                                                 6 
##                                          LANGCHUK 
##                                                40 
##                                          LANGDENG 
##                                               264 
##                                          LANGTENG 
##                                               463 
##                                            LAPNAN 
##                                               661 
##                                            LAPUNG 
##                                               222 
##                                            LAPUSA 
##                                               100 
##                                      LASSUM-PATTE 
##                                               133 
##                                         LATHAO(A) 
##                                               656 
##                                         LATHAO(B) 
##                                               699 
##                                            LAUTUL 
##                                               202 
##                                             LEBRI 
##                                               122 
##                                             LEDUM 
##                                               584 
##                                              LEEL 
##                                               522 
##                                              LEGA 
##                                                67 
##                                LEKANG GOHAIN GAON 
##                                               567 
##                                            LELUNG 
##                                               110 
##                                        LEMBERDUNG 
##                                               531 
##                                            LEMPIA 
##                                               875 
##                                           LENGBIA 
##                                               233 
##                                    LENGDI - LIANG 
##                                                77 
##                                       LENGFER - I 
##                                               417 
##                                            LENGKA 
##                                               492 
##                                            LENGRO 
##                                               526 
##                                         LEPORIANG 
##                                               363 
##                                   LEPROSY COLONEY 
##                                               641 
##                                    LEPROSY COLONY 
##                                               194 
##                                            LERIAK 
##                                               389 
##                                      LETE VILLAGE 
##                                               100 
##                                              LEYA 
##                                              1049 
##                                          LHALLUNG 
##                                               230 
##                                          LHOUDUNG 
##                                               444 
##                                 LIBU BENE VILLAGE 
##                                               278 
##                                         LICHI - I 
##                                               214 
##                                           LICHINI 
##                                                44 
##                                           LICHLIT 
##                                               244 
##                                     LIDUK VILLAGE 
##                                               113 
##                                      LIGO VILLAGE 
##                                               169 
##                                              LIGU 
##                                               517 
##                                     LIKABALI WEST 
##                                               412 
##                                             LIKOR 
##                                               239 
##                                    LILENG VILLAGE 
##                                               236 
##                                          LILIDONG 
##                                               398 
##                                          LIMEKING 
##                                               245 
##                                           LINGDAM 
##                                               240 
##                                            LINGKA 
##                                               227 
##                                           LINGRAM 
##                                               208 
##                                    LINGRUK RIAMUK 
##                                               233 
##                                            LINIYA 
##                                               351 
##                                             LINKE 
##                                               227 
##                                          LIPHAKPU 
##                                               219 
##                                             LIPIN 
##                                                96 
##                                              LIPO 
##                                                98 
##                               LIPU NAMCHI VILLAGE 
##                                               142 
##                                      LIPU VILLAGE 
##                                               642 
##                                     LIROMOBA CAMP 
##                                               273 
##                                      LIRU VILLAGE 
##                                               688 
##                                              LISH 
##                                               496 
##                                     LISH GOMPACHE 
##                                               443 
##                                   LISSING VILLAGE 
##                                                97 
##                                      LITE VILLAGE 
##                                                71 
##                                  LITEMORI VILLAGE 
##                                               184 
##                                            LOAUNU 
##                                               176 
##                                           LOCHUNG 
##                                               119 
##                                             LOFFA 
##                                               412 
##                                             LOGLU 
##                                               112 
##                                        LOGUM JINI 
##                                               716 
##                                          LOHITPUR 
##                                               245 
##                                          LOILIANG 
##                                               823 
##                                   LOKPENG VILLAGE 
##                                               232 
##                                             LONDA 
##                                               349 
##                                    LONGBO VILLAGE 
##                                               154 
##                                         LONGCHUNG 
##                                               558 
##                                     LONGDING TOWN 
##                                              1954 
##                                           LONGHUA 
##                                               385 
##                               LONGKAI VILLAGE - I 
##                                               559 
##                                           LONGKEY 
##                                               232 
##                                        LONGKHOJAN 
##                                                79 
##                                 LONGKHONG VILLAGE 
##                                                98 
##                                  LONGKHOW VILLAGE 
##                                               958 
##                                   LONGKOM PONTHAI 
##                                               202 
##                                 LONGLIANG VILLAGE 
##                                               450 
##                                          LONGLING 
##                                               244 
##                                          LONGLUNG 
##                                               198 
##                                   LONGMAN VILLAGE 
##                                               208 
##                                       LONGNAKSHIA 
##                                               149 
##                                     LONGO VILLAGE 
##                                               391 
##                                           LONGPHA 
##                                               156 
##                                         LONGPHONG 
##                                               700 
##                                           LONGRAN 
##                                               216 
##                                   LONGSOM VILLAGE 
##                                               713 
##                           LONGSONG - I, II, & III 
##                                                40 
##                                       LONGTE LOTH 
##                                               487 
##                                           LONGTOI 
##                                                59 
##                                            LONYEN 
##                                               171 
##                         LORGING (RALLUNG) VILLAGE 
##                                               338 
##                                            LORRAH 
##                                               220 
##                                              LOTH 
##                                               256 
##                                           LOUDUNG 
##                                               211 
##                              LOWER BALIJAN(NISHI) 
##                                               777 
##                      LOWER BHALUKPONG(NORTH WING) 
##                                               458 
##                      LOWER BHALUKPONG(SOUTH WING) 
##                                               462 
##                             LOWER CHINHAN VILLAGE 
##                                               345 
##                                       LOWER DZONG 
##                                               178 
##                                        LOWER GIDA 
##                                               280 
##                                        LOWER HEYO 
##                                                99 
##                                        LOWER JOTE 
##                                               632 
##                                       LOWER KOLAM 
##                                               275 
##                                       LOWER LEYAK 
##                                               175 
##                                LOWER MIAO (NORTH) 
##                                               520 
##                                     LOWER MILLANG 
##                                               247 
##                             LOWER NYAPIN TOWNSHIP 
##                                               385 
##                                        LOWER SHER 
##                                               423 
##                                LOWER SILATOO MIRI 
##                                               577 
##                                LOWER SINU VILLAGE 
##                                               197 
##                                           LUAKSIM 
##                                               386 
##                                           LUBRANG 
##                                               239 
##                                             LUCHI 
##                                               372 
##                                         LUGUTHANG 
##                                                32 
##                                       LUI VILLAGE 
##                                               624 
##                                            LUKBIA 
##                                               293 
##                                             LUMBA 
##                                               309 
##                                        LUMBAKTANG 
##                                                88 
##                                           LUMDUNG 
##                                               511 
##                                        LUMLA H.Q. 
##                                               619 
##                                             LUMPO 
##                                               667 
##                                           LUNGDUR 
##                                               174 
##                                          LUNGPANG 
##                                               226 
##                                            LUNGSA 
##                                               250 
##                                          LUNGSANG 
##                                               128 
##                                 LUNGSHANG VILLAGE 
##                                               115 
##                                          LUNGTANG 
##                                                45 
##                                            LUNGTE 
##                                               255 
##                                     LUTAK VILLAGE 
##                                               267 
##                                   LUTHONG VILLAGE 
##                                               211 
##                                            LYNGOK 
##                                                72 
##                                            MABIRA 
##                                               183 
##                                           MACHANE 
##                                               182 
##                                           MACHING 
##                                               141 
##                                            MACHUM 
##                                               241 
##                                         MAGANTONG 
##                                               376 
##                                      MAGI VILLAGE 
##                                               601 
##                                              MAGO 
##                                               186 
##                                           MAGOPAM 
##                                                84 
##                                            MAGRIA 
##                                               146 
##                                      MAHADEVPUR-I 
##                                               798 
##                                     MAHADEVPUR-II 
##                                               752 
##                                   MAHADEVPUR - IV 
##                                               427 
##                                   MAHADEVPUR TOWN 
##                                               851 
##                                               MAI 
##                                               301 
##                                    MAIHUA VILLAGE 
##                                               266 
##                                          MAILIANG 
##                                                76 
##                                     MAKAT VILLAGE 
##                                               139 
##                                             MAKBA 
##                                                44 
##                                             MALEK 
##                                               101 
##                                           MALOGAM 
##                                                 2 
##                                          MANABHUM 
##                                               138 
##                                           MANCHAL 
##                                               181 
##                                   MANDALA PHUDUNG 
##                                               625 
##                                              MANE 
##                                               175 
##                                           MANGNAM 
##                                               444 
##                                          MANGNANG 
##                                               231 
##                                            MANKAO 
##                                               394 
##                                           MANKOTA 
##                                               149 
##                                          MANLINYE 
##                                                44 
##                                         MANMAO HQ 
##                                               244 
##                                    MANMAO VILLAGE 
##                                               227 
##                                            MANMOW 
##                                               285 
##                                      MANPENGLIANG 
##                                               517 
##                                            MANTHI 
##                                               120 
##                                        MANYULIANG 
##                                               693 
##                                            MARBOM 
##                                               109 
##                                           MARGING 
##                                               246 
##                                     MARIYANG H.Q. 
##                                               817 
##                                            MARKIA 
##                                               153 
##                                             MARME 
##                                                55 
##                                              MARO 
##                                               439 
##                                           MARONLI 
##                                                45 
##                                         MARZINGLA 
##                                               266 
##                                            MATHOW 
##                                               129 
##                                          MATKRONG 
##                                                16 
##                                            MATOLI 
##                                               107 
##                                         MAWAI - I 
##                                               441 
##                                       MAYU - I(B) 
##                                               449 
##                                      MAYU - II(B) 
##                                               383 
##                                             MAYUM 
##                                                94 
##                           MEBO TOWN & DARNE BAZAR 
##                                               761 
##                                      MEBO VILLAGE 
##                                               956 
##                                        MEBUA CAMP 
##                                               229 
##                                       MECHE MARDE 
##                                               290 
##                                         MEDEMBARI 
##                                               158 
##                                    MEDICAL COLONY 
##                                              1328 
##                    MEDICAL COLONY ,ROING - III(A) 
##                                               547 
##                       MEDICAL LINE,ROING - II (B) 
##                                               425 
##                                         MEDO CAMP 
##                                               644 
##                                              MEER 
##                                               228 
##                                      MEGA VILLAGE 
##                                               137 
##                                          MEKA - I 
##                                               463 
##                                         MEKALIANG 
##                                               345 
##                                         MEMBACHUR 
##                                                96 
##                                             MENGA 
##                                               134 
##                                       MENGI KABAK 
##                                               181 
##                                            MENGIO 
##                                               565 
##                                   MENGKENG KHAMTI 
##                                               385 
##                                      MENGKENGMIRI 
##                                               596 
##                                           MEPSORO 
##                                                61 
##                                       MER VILLAGE 
##                                               406 
##                                   MESSING VILLAGE 
##                                                61 
##                                       METENGLIANG 
##                                               114 
##                                      MIAO SINGPHO 
##                                               974 
##                                             MICHI 
##                                               461 
##                                           MIDLAND 
##                                               436 
##                                         MIDPU - I 
##                                               984 
##                                           MIGGING 
##                                               175 
##                                           MIGLUNG 
##                                               199 
##                                           MIHUNDO 
##                                               141 
##                                            MIKONG 
##                                               442 
##                                             MIMEY 
##                                               170 
##                                           MINTONG 
##                                               761 
##                                             MIRBA 
##                                               131 
##                             MIREM VILLAGE (LOWER) 
##                                               521 
##                             MIREM VILLAGE (UPPER) 
##                                               503 
##                                             MIRKU 
##                                               620 
##                                            MIRSAM 
##                                               614 
##                                    MISSION COLONY 
##                                               970 
##                                            MITAKA 
##                                                30 
##                                              MITE 
##                                               341 
##                                          MITHUMNA 
##                                                79 
##                                  MOBADOKE VILLAGE 
##                                               346 
##                                       MOBANG - II 
##                                               328 
##                                     MODEL VILLAGE 
##                                               984 
##                             MODEL VILLAGE (NAMGO) 
##                                                83 
##                                          MOHIKONG 
##                                                95 
##                                      MOHONG DEORI 
##                                               419 
##                                       MOHONG MURA 
##                                               335 
##                                         MOITRIPUR 
##                                               458 
##                               MOKTOWA - I VILLAGE 
##                                               486 
##                              MOKTOWA - II VILLAGE 
##                                               467 
##                                     MOLOM VILLAGE 
##                                               387 
##                                          MOLORANG 
##                                               404 
##                                            MOMONG 
##                                               601 
##                                              MONA 
##                                               130 
##                                          MONGKHRA 
##                                               163 
##                                            MONGKU 
##                                               472 
##                                          MONIGONG 
##                                               631 
##                                  MOPAKHAT VILLAGE 
##                                               496 
##                                    MOPAYA VILLAGE 
##                                               205 
##                                     MOPIT VILLAGE 
##                                               288 
##                           MOPUNG / PUNGKU VILLAGE 
##                                               256 
##                                      MORI VILLAGE 
##                                               434 
##                                  MORSHING VILLAGE 
##                                               631 
##                                     MOSSANG PUTUK 
##                                                47 
##                                           MOSSING 
##                                               194 
##                                            MOTONG 
##                                                45 
##                                          MOTONGSA 
##                                               125 
##                                    MOTTUM VILLAGE 
##                                               580 
##                      MOTUM - BENTUK / IFCD COLONY 
##                                               484 
##                                 MOWB - II EASTERN 
##                                               726 
##                                 MOWB - II WESTERN 
##                                               894 
##                                            MOYABA 
##                                               239 
##                                            MOYING 
##                                               224 
##                                          MPEN - I 
##                                               130 
##                                           MRAMBOO 
##                                                 6 
##                                       MUDANG TAGE 
##                                               987 
##                                             MUDOI 
##                                               349 
##                                             MUGLI 
##                                               458 
##                                             MUKTO 
##                                               413 
##                                         MUKUTHING 
##                                                75 
##                                        MUNNA CAMP 
##                                               235 
##                                              MURI 
##                                               196 
##                                        MUSHAKSING 
##                                                88 
##                                          NACHIBAN 
##                                               223 
##                                        NACHO H.Q. 
##                                                48 
##                       NAFRA ADMN H.Q. (EAST WING) 
##                                               493 
##                       NAFRA ADMN H.Q. (WEST WING) 
##                                               329 
##                                           NAITONG 
##                                               218 
##                                            NAJANG 
##                                                73 
##                                            NAKANG 
##                                                26 
##                                             NAKHU 
##                                               208 
##                                              NAMA 
##                                                95 
##                                          NAMAZING 
##                                               636 
##                                    NAMCHER BAGANG 
##                                               343 
##                              NAMCHIK FOREST CAMP. 
##                                               403 
##                                           NAMDANG 
##                                                20 
##                                             NAMEY 
##                                               450 
##                    NAMGHAR/SCHOOL LINE CHETA - II 
##                                               681 
##                  NAMGOI VILLAGE - I, II, III & IV 
##                                               294 
##                                          NAMLIANG 
##                                               306 
##                                           NAMORAH 
##                                               142 
##                                             NAMPE 
##                                               328 
##                                       NAMPHAINONG 
##                                               527 
##                                       NAMPONG - I 
##                                               388 
##                                      NAMPONG - II 
##                                               624 
##                                      NAMPONG NALA 
##                                               729 
##                             NAMSAI BLOCK-I (KABA) 
##                                               989 
##                                   NAMSAI BLOCK-II 
##                                               872 
##                                  NAMSAI BLOCK-III 
##                                               998 
##                       NAMSAI BLOCK-V (SOUTH WING) 
##                                               602 
##                        NAMSAI BLOCK-V(NORTH WING) 
##                                               979 
##                                 NAMSAI BLOCK-VI(N 
##                                               258 
##                       NAMSAI BLOCK-VI(SOUTH WING) 
##                                               969 
##                                 NAMSAI BLOCK - IV 
##                                               693 
##                                      NAMSANG H.Q. 
##                                               401 
##                               NAMSANGMUKH VILLAGE 
##                                               409 
##                                            NAMSHU 
##                                               464 
##                                   NAMSING VILLAGE 
##                                               855 
##                                          NAMTHUNG 
##                                                98 
##                               NAMTOK (RICHI LINE) 
##                                               390 
##                                      NANAM KHAMTI 
##                                               687 
##                                    NANAM KHAMYANG 
##                                               456 
##                                           NANGRAM 
##                                               367 
##                                             NAPIT 
##                                               192 
##                                           NARGANG 
##                                               460 
##                                              NARI 
##                                               527 
##                                         NARI CAMP 
##                                               398 
##                                         NARI H.Q. 
##                                               341 
##                               NARINGWA (MORINGWA) 
##                                                48 
##                                              NASI 
##                                               139 
##                                             NATAM 
##                                               315 
##                              NATUN KHETI VILLEAGE 
##                                               278 
##                                              NAVA 
##                                               104 
##                                             NAYAM 
##                                               107 
##                                            NAYANG 
##                                               194 
##                                            NEELAM 
##                                               443 
##                                     NEEPCO COLONY 
##                                               907 
##                                            NEKING 
##                                                95 
##                                        NENCHALAYA 
##                                               701 
##                                            NEOTAN 
##                                               734 
##                                            NEPUWA 
##                                               108 
##                                              NERE 
##                                               342 
##                                            NEREWA 
##                                               144 
##                                    NERIST COMPLEX 
##                                              1412 
##                                      NEW-MOHONG I 
##                                               525 
##                                     NEW-MOHONG II 
##                                               379 
##                                         NEW ABALI 
##                                               303 
##                                         NEW ALONI 
##                                                49 
##                                         NEW ANAYA 
##                                                87 
##                                    NEW BAZAR LINE 
##                                               812 
##                                         NEW BORAK 
##                                                56 
##                               NEW BUNTING VILLAGE 
##                                               131 
##                                     NEW CHANGLANG 
##                                               385 
##                                       NEW DANGLAT 
##                                               414 
##                                NEW DARING VILLAGE 
##                                               242 
##                                          NEW DEKA 
##                                               116 
##                                NEW DOKPEY VILLAGE 
##                                                64 
##                                       NEW ENDOLIN 
##                                                83 
##                                          NEW HAJI 
##                                               225 
##                                          NEW HALI 
##                                               201 
##                                         NEW JUKHI 
##                                                62 
##                                         NEW KASPI 
##                                               163 
##                                NEW KATANG VILLAGE 
##                                               123 
##                                      NEW KHAMLANG 
##                                               282 
##                                     NEW KHIMIYANG 
##                                               683 
##                                NEW KOTHIN VILLAGE 
##                                               339 
##                               NEW KOTHUNG VILLAGE 
##                                               270 
##                              NEW LAINWANG VILLAGE 
##                                               188 
##                               NEW LAPTANG VILLAGE 
##                                               172 
##                                          NEW LIDA 
##                                               260 
##                                        NEW LISSAN 
##                                               223 
##                               NEW LONGTOI VILLAGE 
##                                                60 
##                                         NEW LUMLA 
##                                               555 
##                             NEW PANIDURIA VILLAGE 
##                                                70 
##                              NEW PHINTING VILLAGE 
##                                               138 
##                                       NEW POBLUNG 
##                                                62 
##                                       NEW RANGRAN 
##                                                55 
##                                         NEW REDDI 
##                                               169 
##                                          NEW RIBA 
##                                               271 
##                                          NEW RILO 
##                                               145 
##                                       NEW SALLANG 
##                                               124 
##                                         NEW SEPPA 
##                                               390 
##                                         NEW SEREN 
##                                                51 
##                                       NEW SILATOO 
##                                               593 
##                                  NEW SOHE LAKTONG 
##                                                53 
##                                        NEW SOPUNG 
##                                               169 
##                                NEW SUBANG VILLAGE 
##                                                86 
##                                         NEW TELAM 
##                                               202 
##                                       NEW THAMLOM 
##                                               128 
##                                        NEW YANMAN 
##                                               433 
##                                             NGABA 
##                                               243 
##                                          NGAMDING 
##                                                64 
##                                           NGAMING 
##                                               376 
##                                          NGECHANG 
##                                               134 
##                                    NGENSI VILLAGE 
##                                               104 
##                                 NGINU VILLAGE - I 
##                                               681 
##                                NGINU VILLAGE - II 
##                                               950 
##                                    NGISSA VILLAGE 
##                                               522 
##                                 NGOITHONG VILLAGE 
##                                               147 
##                                          NGOITONG 
##                                               117 
##                                             NGOJU 
##                                               197 
##                                           NGOMDIR 
##                                               378 
##                                             NGOPI 
##                                               170 
##                                    NGOPOK (NORTH) 
##                                               672 
##                                    NGOPOK (SOUTH) 
##                                               600 
##                                          NGORLUNG 
##                                               324 
##                                             NGUKI 
##                                               181 
##                                             NGURI 
##                                               263 
##                                            NIAGIO 
##                                               247 
##                                   NIANU VILLAGE-I 
##                                               871 
##                                            NIAUSA 
##                                               954 
##                                  NICHOBA (NILOBA) 
##                                               126 
##                                            NIGLOK 
##                                               252 
##                                              NIJI 
##                                               307 
##                                             NIKJA 
##                                               322 
##                                             NIKTE 
##                                               469 
##                                            NILANG 
##                                               105 
##                                           NILLING 
##                                               227 
##                                              NILO 
##                                               182 
##                                             NILOK 
##                                                84 
##                                              NIMA 
##                                               237 
##                                             NIMAR 
##                                               141 
##                                             NIMTE 
##                                               674 
##                                           NINGCHO 
##                                               287 
##                                          NINGGING 
##                                               224 
##                                   NINGROO CHARALI 
##                                               882 
##                                            NIOBIA 
##                                               232 
##                                              NIPU 
##                                               176 
##                                          NIRINGHA 
##                                               440 
##                                        NISANGJANG 
##                                               118 
##                                        NITI VIHAR 
##                                               987 
##                                            NIZONG 
##                                                77 
##                                              NOGI 
##                                               121 
##                                     NOGLO VILLAGE 
##                                               381 
##                                     NOGNA VILLAGE 
##                                               261 
##                                NOKFAN FOREST CAMP 
##                                               296 
##                                    NOKFAN VILLAGE 
##                                               199 
##                                     NOKSA VILLAGE 
##                                               396 
##                                     NOMUK VILLAGE 
##                                               311 
##                                          NONGKHON 
##                                               755 
##                                    NONGTAW KHAMTI 
##                                               815 
##                                            NUNGNU 
##                                               221 
##                                            NYAMPU 
##                                               143 
##                                           NYERING 
##                                                45 
##                           NYIGAM VILLAGE PART - I 
##                                               464 
##                          NYIGAM VILLAGE PART - II 
##                                               449 
##                                     NYODU VILLAGE 
##                                               336 
##                                            NYOGIN 
##                                               445 
##                                       NYOKILANGHI 
##                                               117 
##                                            NYORAK 
##                                               354 
##                                       NYUK MADUNG 
##                                               561 
##                                           NYUKONG 
##                                                72 
##         O POINT TINALI NYOKUM LAPANG/6KM NH-52(A) 
##                                               698 
##                  O PT TINALI BAZAR AREA/ADI BOSTI 
##                                               674 
##                                          OLD BULO 
##                                               204 
##                               OLD BUNTING VILLAGE 
##                                               157 
##                             OLD CHANGLANG VILLAGE 
##                                               407 
##                                OLD DARING VILLAGE 
##                                               418 
##                                          OLD DEKA 
##                                               252 
##                               OLD DERENALO (GISI) 
##                                               141 
##                                        OLD DOKPEY 
##                                                46 
##                                          OLD HAJI 
##                                                96 
##                                         OLD JUKHI 
##                                               119 
##                                        OLD KAMLAO 
##                                               241 
##                                OLD KATANG VILLAGE 
##                                               262 
##                                OLD KOTHIN VILLAGE 
##                                                85 
##                               OLD KOTHUNG VILLAGE 
##                                               233 
##                              OLD LAINWANG VILLAGE 
##                                               122 
##                               OLD LAPTANG VILLAGE 
##                                               236 
##                                          OLD LIDA 
##                                                70 
##                                        OLD MARKET 
##                                               492 
##                                        OLD MOHONG 
##                                               995 
##                                           OLD NUK 
##                                               235 
##                                         OLD PANIA 
##                                               554 
##                              OLD PHINTING VILLAGE 
##                                                91 
##                                         OLD PUTUK 
##                                                33 
##                                       OLD RANGRAN 
##                                                89 
##                                         OLD RICHI 
##                                               154 
##                                       OLD SALLANG 
##                                                83 
##      OLD SECRETARIAT / DOKUM (NEAR POLICE STATION 
##                                               990 
##                                         OLD SINGA 
##                                               198 
##                                  OLD TUPI VILLAGE 
##                                               664 
##                                          OLD ZIRO 
##                                              1271 
##                                            OMPULI 
##                                               433 
##                                      OROK VILLAGE 
##                                                58 
##                                OYAN VILLAGE (S/W) 
##                                               716 
##                                            OZAKHO 
##                                               432 
##                                       P- SECTOR(A 
##                                               622 
##                              P - SECTOR EAST SIDE 
##                                               661 
##                              P - SECTOR WEST SIDE 
##                                               571 
##                                         P.I. LINE 
##                                               316 
##                                             PABUA 
##                                               229 
##                                             PACHI 
##                                               129 
##                                     PACHIN COLONY 
##                                               830 
##                                           PADDING 
##                                               207 
##                                      PADI VILLAGE 
##                                               362 
##                                              PADU 
##                                               582 
##                                             PAFFA 
##                                               222 
##                                             PAGBA 
##                                               429 
##                                              PAGI 
##                                               636 
##                                            PAGLAM 
##                                               606 
##                                            PAGLEK 
##                                               891 
##                                              PAGU 
##                                               257 
##                                           PAIGONG 
##                                               624 
##                                          PAILIANG 
##                                               131 
##                                   PAIMORI VILLAGE 
##                                               146 
##                                              PAJA 
##                                                40 
##                                              PAKA 
##                                               412 
##                                             PAKAM 
##                                               531 
##                                             PAKBA 
##                                               274 
##                                             PAKKE 
##                                               301 
##                                     PAKKE-KESSANG 
##                                               427 
##                                            PAKOTI 
##                                               367 
##                                             PAKPU 
##                                               143 
##                                      PAKPU MALING 
##                                               248 
##                                             PAKRO 
##                                               227 
##                                   PAKSING VILLAGE 
##                                               223 
##                                            PAKSOK 
##                                               106 
##                                           PAKTUNG 
##                                               222 
##                                       PALATARIPAM 
##                                               144 
##                                             PALAV 
##                                               162 
##                                      PALE VILLAGE 
##                                               173 
##                                             PALIN 
##                                               213 
##                                            PALIZI 
##                                               507 
##                                           PALLANG 
##                                                78 
##                                           PALLING 
##                                               116 
##                                               PAM 
##                                               258 
##                                          PAMAGHAR 
##                                               376 
##                                      PAME VILLAGE 
##                                               117 
##                                           PAMPOLI 
##                                               199 
##                                               PAN 
##                                               303 
##                                            PANGGO 
##                                               177 
##                                     PANGI VILLAGE 
##                                               136 
##                                            PANGIA 
##                                               203 
##                                       PANGIN TOWN 
##                                               797 
##                                    PANGIN VILLAGE 
##                                               493 
##                                PANGKANG (JORKANG) 
##                                               332 
##                          PANGKANG (KUMKU) VILLAGE 
##                                               210 
##                                           PANGKAO 
##                                               108 
##                                  PANGKENG VILLAGE 
##                                               710 
##                                            PANGMA 
##                                               122 
##                                            PANGRI 
##                                               118 
##                                              PANI 
##                                               184 
##                                             PANIA 
##                                               409 
##                                 PANIDURIA VILLAGE 
##                                               461 
##                                         PANIKHETI 
##                                                 6 
##                                            PANKAR 
##                                                86 
##                                            PANLOM 
##                                               120 
##                               PANSUMTHONG VILLAGE 
##                                               123 
##                                            PANUNG 
##                                               358 
##                                             PANYA 
##                                               280 
##                                              PAPA 
##                                               266 
##                                              PAPI 
##                                               141 
##                                        PAPIKURUNG 
##                                               227 
##                                         PAPU HILL 
##                                              1014 
##                        PAPU NALLAH / PAPU VILLAGE 
##                                               982 
##                                      PAPU VILLAGE 
##                                               663 
##                                         PARA LINE 
##                                               869 
##                                             PARAM 
##                                               112 
##                                            PARBUK 
##                                               411 
##                                        PARENG - I 
##                                               347 
##                                    PARENG VILLAGE 
##                                               424 
##                                              PARO 
##                                               500 
##                                    PARONG (KINNE) 
##                                               194 
##                                    PARONG VILLAGE 
##                                               315 
##                                       PARSING - I 
##                                               668 
##                    PASIGHAT - "G"(FFP/EDN COLONY) 
##                                               618 
##                                      PASIGHAT - A 
##                                               435 
##                                      PASIGHAT - B 
##                                               670 
##                                      PASIGHAT - D 
##                                               472 
##                                      PASIGHAT - E 
##                                               411 
##                                      PASIGHAT - F 
##                                               591 
##                       PASIGHAT BAZAR (NORTH WING) 
##                                               639 
##                       PASIGHAT BAZAR (SOUTH WING) 
##                                               648 
##                                              PATE 
##                                               381 
##                                             PATHA 
##                                                34 
##                                        PATHERGAON 
##                                               669 
##                                            PATIWA 
##                                                69 
##                                              PAYA 
##                                               739 
##                                        PAYUM H.Q. 
##                                               245 
##                                              PECH 
##                                               654 
##                                            PEDUNG 
##                                               565 
##                                              PEEL 
##                                               281 
##                                         PEETAPOOL 
##                                               679 
##                                       PEGA LOMDAK 
##                                               371 
##                                          PEKIMODI 
##                                                67 
##                                         PEL MILLI 
##                                               241 
##                                              PENI 
##                                               264 
##                                      PERI VILLAGE 
##                                               213 
##                                      PESSING CAMP 
##                                               425 
##                                              PEYA 
##                                               253 
##                                            PHADAM 
##                                                67 
##                                      PHANGLONGLAT 
##                                               123 
##                                          PHANGSUM 
##                                                67 
##                                          PHANGTIP 
##                                               139 
##                                           PHANYAK 
##                                               405 
##                                          PHASSANG 
##                                               175 
##                                         PHILOBARI 
##                                               286 
##                                        PHINBERO-I 
##                                               146 
##                                       PHINBERO-II 
##                                                76 
##                                         PHIRIZINE 
##                                               127 
##                                          PHOMGHAR 
##                                               249 
##                                              PHUP 
##                                               486 
##                                             PHUSA 
##                                                81 
##                                              PIDI 
##                                               136 
##                                        PIGIA GIBA 
##                                               494 
##                                         PILLA - I 
##                                               394 
##                                    PILLUNG MALING 
##                                               185 
##                                    PINCHI VILLAGE 
##                                               418 
##                                           PINGING 
##                                               138 
##                                          PIPOKORO 
##                                               132 
##                                         PIPSORANG 
##                                               346 
##                                              PIPU 
##                                               289 
##                                      PIRA VILLAGE 
##                                               236 
##                                      PIRI VILLAGE 
##                                               224 
##                                        PISTANA HQ 
##                                               213 
##                                          PITCHANG 
##                                                74 
##                                            PIYONG 
##                                               791 
##                                       POBDI VILL. 
##                                               551 
##                                           POBLUNG 
##                                               433 
##                                              POBO 
##                                               200 
##                                             POCHU 
##                                               125 
##                                          PODAMARA 
##                                               561 
##                                          PODUMONI 
##                                               979 
##                                     POKTO VILLAGE 
##                                               394 
##                                     POLICE COLONY 
##                                               903 
##                     POLICE COLONY ,ROING - III(B) 
##                                               509 
##                                    POLICE RESERVE 
##                                               539 
##                          POLO COLONY / TPT COLONY 
##                                               779 
##               POLO COLONY /CO-OP,APEX BANK COLONY 
##                                               643 
##                                              POMA 
##                                               638 
##               POMLIANG (LOILIANG BLOCK -I AND II) 
##                                               586 
##                              PONGCHAU VILLAGE - I 
##                                               852 
##                             PONGCHAU VILLAGE - II 
##                                               831 
##                                          PONGGING 
##                                               235 
##                                  PONGKONG VILLAGE 
##                                               186 
##                                            PONGTE 
##                                                66 
##                                           PORDUNG 
##                                               272 
##                                              PORU 
##                                               321 
##                                POTOM DEGI VILLAGE 
##                                               172 
##                              POTOM LARMUK VILLAGE 
##                                                64 
##                                POTOM SALA VILLAGE 
##                                               127 
##                                             POTTE 
##                                               292 
##                                        POTUNG DUI 
##                                               168 
##                                             POUBE 
##                                               232 
##                                     POYOM VILLAGE 
##                                               221 
##                                     PROPER YANGTE 
##                                               245 
##                                         PUAKGUMIN 
##                                               482 
##                                           PUGGING 
##                                               249 
##                                     PUKPU (CHOBA) 
##                                               250 
##                                            PULLOM 
##                                               152 
##                                   PULLONG VILLAGE 
##                                               313 
##                                     PUMAO VILLAGE 
##                                               955 
##                                        PUMTE BAGE 
##                                               129 
##                                             PUNLI 
##                                                75 
##                                      PUSHI NYORAK 
##                                               263 
##                                         PUSHIDOKE 
##                                               318 
##                                             PUTUK 
##                                               212 
##                             PWD COMPLEX CHANGLANG 
##                                               316 
##     PWD DIVISION - IV OFFICE COMPLEX / SENKI PARK 
##                                               706 
##                                            QUIBOM 
##                                                85 
##                                            QUYING 
##                                               384 
##                              R.K. MISSION COMPLEX 
##                                               991 
##                                        RACH TABIO 
##                                               219 
##                                         RACHI - I 
##                                               255 
##                                            RADENG 
##                                               266 
##                                       RAGA HQ - I 
##                                               370 
##                                      RAGA HQ - II 
##                                               243 
##                                  RAGIDOKE VILLAGE 
##                                               234 
##                                              RAGO 
##                                               227 
##                                              RAHA 
##                                               707 
##                                      RAHO VILLAGE 
##                                               178 
##                                            RAHUNG 
##                                               238 
##                                           RAIBALO 
##                                               514 
##                                              RAIK 
##                                               189 
##                                       RAJANAGAR-I 
##                                               664 
##                                              RAJI 
##                                               172 
##                                             RAKER 
##                                               345 
##                                             RAKSO 
##                                               331 
##                                   RALLING VILLAGE 
##                                               167 
##                                         RAMA CAMP 
##                                               359 
##                                        RAMALINGOM 
##                                               186 
##                                             RAMDA 
##                                                89 
##                                           RAMGHAT 
##                                               340 
##                                          RAMNAGAR 
##                                               208 
##                                           RAMSING 
##                                               391 
##                                          RANAGHAT 
##                                               700 
##                                     RANAGHAT CAMP 
##                                                21 
##                                              RANG 
##                                               202 
##                                          RANGHILL 
##                                                55 
##                                           RANGLUA 
##                                               645 
##                                           RANGLUM 
##                                                75 
##                                       RANGRINGKAN 
##                                               249 
##                                      RANGTHANGJOR 
##                                               210 
##                                              RANI 
##                                               445 
##                                        RANI (S/W) 
##                                               454 
##                                           RANKATU 
##                                               355 
##                                  RANLAMRI VILLAGE 
##                                                61 
##                                             RANLI 
##                                                51 
##                                             RAPUM 
##                                               189 
##                                            RAPUNG 
##                                               117 
##                                     RARISH SOLUNG 
##                                                55 
##                              RATAK GAMLIN VILLAGE 
##                                               318 
##                                              RATE 
##                                               164 
##                                              RAWA 
##                                               217 
##                                            RAYANG 
##                                               351 
##                                            RAYING 
##                                               695 
##                                    RAYUK (SOLUNG) 
##                                                42 
##                                              REBE 
##                                               288 
##                                              REBI 
##                                               170 
##                                           REDDING 
##                                               190 
##                                             REDDY 
##                                                74 
##                                      REGI VILLAGE 
##                                               246 
##                                              REGO 
##                                               151 
##                                         RELANGKAN 
##                                                73 
##                                            RELUNG 
##                                               188 
##                                              REMI 
##                                               236 
##                                           RENGCHI 
##                                               413 
##                                          RENGGING 
##                                               244 
##                                     RENGO VILLAGE 
##                                               235 
##                                             RENUK 
##                                               153 
##                                            REPARI 
##                                               226 
##                                          RERU - I 
##                                               777 
##                                         RERU - II 
##                                               522 
##                                        RERU - III 
##                                               529 
##                                        RESTARIANG 
##                                               436 
##                                               RHO 
##                                               304 
##                                             RIAGA 
##                                               404 
##                                            RICHIK 
##                                               661 
##                                 RICHIRITE VILLAGE 
##                                                24 
##                                RIEW VILLAGE (N/W) 
##                                               376 
##                                RIEW VILLAGE (S/W) 
##                                               363 
##                                           RIGA HQ 
##                                               176 
##                          RIGA MOBUK VILLAGE (N/W) 
##                                               406 
##                          RIGA MOBUK VILLAGE (S/W) 
##                                               385 
##                                       RIGA MONGKU 
##                                               324 
##                                        RIGA SIRAM 
##                                               242 
##                                             RIGIA 
##                                               291 
##                                              RIGO 
##                                               452 
##                                    RIGONG VILLAGE 
##                                                71 
##                                             RIGYU 
##                                               517 
##                                           RIKHUNG 
##                                               117 
##                                              RIKO 
##                                               248 
##                                            RIKUNG 
##                                               108 
##                                            RILLOH 
##                                               496 
##                                      RILU VILLAGE 
##                                               286 
##                                              RIMA 
##                                                69 
##                                  RIMA & HORU RIMA 
##                                               113 
##                                              RIME 
##                                               139 
##                                              RINA 
##                                               228 
##                                     RINGI VILLAGE 
##                                               119 
##                                          RINGLING 
##                                               333 
##                                      RISE VILLAGE 
##                                               196 
##                                             RISSI 
##                                               357 
##                                              RITE 
##                                               329 
##                                            RIYANG 
##                                               186 
##                                          ROILIANG 
##                                               128 
##                                             ROING 
##                                               824 
##                                              ROJI 
##                                               229 
##                                              ROJO 
##                                               175 
##                                              ROSE 
##                                               414 
##                                             ROTTE 
##                                               237 
##                                   ROTTUNG VILLAGE 
##                                               226 
##                                       ROW VILLAGE 
##                                                64 
##                                       ROWTA RANGE 
##                                                11 
##                                              RUBA 
##                                               153 
##                                              RUHI 
##                                               943 
##                                             RUKMO 
##                                                59 
##                                       RUKSIN TOWN 
##                                               535 
##                                    RUKSIN VILLAGE 
##                                               438 
##                                   RUMGONG VILLAGE 
##                                               721 
##                                             RUMTE 
##                                               240 
##                                            RUNGBA 
##                                               356 
##                                             RUNNE 
##                                               234 
##                             RUPA TOWN (EAST WING) 
##                                               670 
##                             RUPA TOWN (WEST WING) 
##                                               639 
##                                      RUPA VILLAGE 
##                                               773 
##                                            RURANG 
##                                               157 
##                                             RUSHI 
##                                               199 
##                                     RUSSA VILLAGE 
##                                               317 
##              RWD / SIPU PUYI COLONY / GUMIN NAGAR 
##                                               633 
##                                           SACHIDA 
##                                               108 
##                                           SACHING 
##                                               304 
##                                           SACHUNG 
##                                                74 
##                                            SADDLE 
##                                               133 
##                                  SAGALEE TOWNSHIP 
##                                               640 
##                                             SAGAR 
##                                               137 
##                                      SAGO VILLAGE 
##                                               453 
##                                             SAIMU 
##                                               499 
##                                           SAKIANG 
##                                               443 
##                                           SAKPRET 
##                                               158 
##                                            SAKRIN 
##                                               224 
##                                              SAKU 
##                                                97 
##                                            SAKYUR 
##                                               225 
##                                            SALARI 
##                                               339 
##                                          SAMDRUNG 
##                                                84 
##                                          SAMPHUNG 
##                                               122 
##                                   SAMPONG VILLAGE 
##                                               175 
##                                         SANCHIPAM 
##                                                57 
##                                            SANCHU 
##                                               221 
##                                    SANGBA KORSANG 
##                                               262 
##                                           SANGBIA 
##                                               217 
##                                             SANGO 
##                                               551 
##                                         SANGO - I 
##                                               226 
##                                           SANGRAM 
##                                               422 
##                                  SANGRAM TOWNSHIP 
##                                               371 
##                                        SANGSATHAM 
##                                               106 
##                                            SANGTI 
##                                               602 
##                           SANGTI (BISHUM) PHUDUNG 
##                                               308 
##                                   SANGWAL VILLAGE 
##                                                95 
##                                   SANLIAM VILLAGE 
##                                                97 
##                                              SAPE 
##                                               194 
##                                       SAPPER CAMP 
##                                               188 
##                                       SARCH - GAI 
##                                               277 
##                                SARI LIKAR VILLAGE 
##                                               203 
##                                             SARIO 
##                                               194 
##                                        SARLI TOWN 
##                                               491 
##                                             SARTA 
##                                               132 
##                                             SARTI 
##                                                48 
##                                             SASUM 
##                                               117 
##                                            SATANG 
##                                                57 
##                                     SAW MILL AREA 
##                                               984 
##                                              SAWA 
##                                                78 
##                                              SAZO 
##                                               216 
##                                              SEBA 
##                                               333 
##                                            SEBING 
##                                               156 
##                      SEC.SCHOOL LINE MAYU - II(A) 
##                                               575 
##                                              SEDE 
##                                               317 
##                                         SEEMA - I 
##                                               221 
##                                              SEER 
##                                               209 
##                                          SEKHJARA 
##                                               272 
##                                            SEKONG 
##                                               260 
##                                            SEMNAK 
##                                                36 
##                                       SENGAPATHER 
##                                               338 
##                                             SENGE 
##                                               434 
##                                        SENGRIDOLO 
##                                               287 
##                                         SENGRIKWA 
##                                               233 
##                                          SENGRING 
##                                               106 
##                                        SENKI VIEW 
##                                               604 
##                                        SENUA CAMP 
##                                                34 
##                               SENUA NOKSA VILLAGE 
##                                               154 
##                                   SENUA VILL. - I 
##                                               973 
##                                    SEPENG VILLAGE 
##                                               116 
##                        SEPPA TOWNSHIP - IV COLONY 
##                                               464 
##                           SEPPA TYPE - III COLONY 
##                                               731 
##                                              SERA 
##                                               934 
##                                       SERAM VILL. 
##                                               548 
##                                 SERE TALI VILLAGE 
##                                               119 
##                                             SEREN 
##                                               550 
##                                           SERIANG 
##                                               204 
##                                           SERJONG 
##                                               303 
##                                             SESSA 
##                                               182 
##                               SESSI LIKAR VILLAGE 
##                                               259 
##                                       SEY - GODAK 
##                                               264 
##                                              SEYA 
##                                               301 
##                                            SHAKTI 
##                                               199 
##                                            SHARMA 
##                                               210 
##                                  SHERBANG / YABAB 
##                                               175 
##                                          SHERGAON 
##                                               692 
##                                           SHIRONG 
##                                               118 
##                                            SHYARO 
##                                               220 
##                                              SHYO 
##                                               788 
##                                      SIBE VILLAGE 
##                                              1227 
##                                  SIBERITE VILLAGE 
##                                               229 
##                                         SIBUM - I 
##                                               248 
##                                        SIBUM - II 
##                                               299 
##                                             SIBUT 
##                                               300 
##                                       SIDO - TENE 
##                                               114 
##                                              SIET 
##                                                95 
##                                              SIGA 
##                                               409 
##                                     SIGAR VILLAGE 
##                                               360 
##                                      SIJI VILLAGE 
##                                               250 
##                SIJIR RAKSAP / SOLI RAKSAP VILLAGE 
##                                               111 
##                                      SIKA - BAMIN 
##                                               530 
##                                         SIKA TODE 
##                                               465 
##                                             SIKAO 
##                                               526 
##                                          SIKARIJO 
##                                               479 
##                                             SIKOM 
##                                                86 
##                                         SIL SANGO 
##                                               437 
##                                            SILIPU 
##                                                33 
##                                             SILLA 
##                                               173 
##                                     SILLE VILLAGE 
##                                               720 
##                                             SILLI 
##                                               251 
##                                     SILLI VILLAGE 
##                                               404 
##                                    SILLUK VILLAGE 
##                                               583 
##                                            SIMONG 
##                                               737 
##                                          SIMUGONG 
##                                               120 
##                                            SINDAK 
##                                               107 
##                                      SINE VILLAGE 
##                                               325 
##                                           SINGBIR 
##                                               395 
##                                          SINGGING 
##                                                76 
##                                         SINGIBEEL 
##                                               369 
##                                           SINWANG 
##                                                47 
##                                          SIOLIANG 
##                                                28 
##                                        SIPILIYANG 
##                                                86 
##                              SIPINIPATHER VILLAGE 
##                                               256 
##                                             SIPPI 
##                                               412 
##                                              SIPU 
##                                               625 
##                                       SIPU COLONY 
##                                               785 
##                                            SIRANG 
##                                               174 
##                                              SIRO 
##                                               597 
##                                         SIRU RIJO 
##                                               236 
##                                      SIRU VILLAGE 
##                                               107 
##                                     SIRUM VILLAGE 
##                                               114 
##                                  SIRUTALI VILLAGE 
##                                                97 
##                                    SISSEN VILLAGE 
##                                               130 
##                                    SITANG VILLAGE 
##                                               395 
##                                    SITAPANI MORAN 
##                                               964 
##                                              SITO 
##                                               453 
##                                      SITPANI MIRI 
##                                               420 
##                                        SIYUM H.Q. 
##                                                72 
##                                             SIZER 
##                                               190 
##                                        SOBLALIANG 
##                                                36 
##                                          SOCKTSEN 
##                                               237 
##                                  SODODOKE VILLAGE 
##                                               155 
##                                            SODRIK 
##                                               185 
##                                     SOGUM VILLAGE 
##                                               540 
##                                      SOHA VILLAGE 
##                                               539 
##                                      SOHE LAKTONG 
##                                               124 
##                                       SOI VILLAGE 
##                                               218 
##                                              SOKI 
##                                               304 
##                                         SOLUNGTOO 
##                                               438 
##                                          SOMPOI-I 
##                                               820 
##                                      SONGKHU HAVI 
##                                               111 
##                                             SONGO 
##                                               237 
##                                    SUBANG VILLAGE 
##                                                64 
##                                              SUBU 
##                                               311 
##                                            SUMLAM 
##                                               153 
##                                           SUMSING 
##                                               330 
##                              SUMSIPATHER VILLEAGE 
##                                               105 
##                                           SUNPURA 
##                                               359 
##                                           SUPLANG 
##                                               240 
##                                   SUPSING VILLAGE 
##                                               137 
##                                             SURBI 
##                                               194 
##                                            SURBIN 
##                                                28 
##                                        SWAMI CAMP 
##                                               161 
##                                              TABA 
##                                               405 
##                                          TABASORA 
##                                               484 
##                                             TABIO 
##                                               139 
##                                          TABIRIPO 
##                                               155 
##                                          TABITALL 
##                                               319 
##                                           TABOMNA 
##                                               167 
##                                             TABRI 
##                                               164 
##                                             TADIN 
##                                               595 
##                                          TAFLAGAM 
##                                               162 
##                                          TAFRAGAM 
##                                               744 
##                                        TAFRALIANG 
##                                               132 
##                                           TAGAMPU 
##                                               174 
##                                    TAGANG WARRANG 
##                                               454 
##                                              TAGO 
##                                               203 
##                                            TAGOGI 
##                                                54 
##                                              TAHU 
##                                               328 
##                                               TAI 
##                                               167 
##                                       TAI VILLAGE 
##                                               301 
##                                            TAJANG 
##                                               769 
##                                             TAJGI 
##                                               309 
##                                        TAJILANGPO 
##                                               254 
##                                      TAJO VILLAGE 
##                                               218 
##                                         TAKAMPASA 
##                                               252 
##                                       TAKEMPURING 
##                                               382 
##                                        TAKILALUNG 
##                                               591 
##                                     TAKOM VILLAGE 
##                                               238 
##                                           TAKSANG 
##                                               101 
##                                      TAKSING H.Q. 
##                                               173 
##                                     TAKSO VILLAGE 
##                                               122 
##                                         TALI H.Q. 
##                                               743 
##                                   TALIHA H.Q. (N) 
##                                               156 
##                                   TALIHA H.Q. (S) 
##                                               273 
##                                             TALLO 
##                                               234 
##                                        TALLOMSIMA 
##                                               237 
##                                       TALLONG - I 
##                                               318 
##                                              TALO 
##                                               424 
##                                         TAMIN - I 
##                                               412 
##                                        TAMIN - II 
##                                               369 
##                                            TAMNEY 
##                                               138 
##                                     TANGO VILLAGE 
##                                               161 
##                                   TANGRANG YANGJE 
##                                               147 
##                                             TANIA 
##                                                86 
##                                             TAOSO 
##                                               298 
##                                            TAPANG 
##                                               108 
##                                             TAPAT 
##                                               289 
##                                              TAPI 
##                                               260 
##                                   TAPIYOR VILLAGE 
##                                               160 
##                                      TAPO VILLAGE 
##                                               197 
##                                            TAPOSO 
##                                                60 
##                                              TARA 
##                                                96 
##    TARAJULI VILLAGE / FOREST RANGE OFFICE COMPLEX 
##                                                86 
##                                     TARAK VILLAGE 
##                                               411 
##                                  TARAMORI VILLAGE 
##                                               229 
##                                             TARBA 
##                                               119 
##                                     TAROWA YANGFO 
##                                               240 
##                                           TAROYAR 
##                                               195 
##                                         TASHIGAON 
##                                                91 
##                                          TASIDONI 
##                                               403 
##                                          TASIRING 
##                                                99 
##                                            TASSAR 
##                                               237 
##                                        TASSOMLORA 
##                                               267 
##                                  TATAMORI VILLAGE 
##                                               150 
##                                          TATATARA 
##                                               174 
##                                          TATO H.Q 
##                                               330 
##                                      TATO VILLAGE 
##                                               379 
##                                      TAWANG GOMPA 
##                                               222 
##                                              TAWE 
##                                               213 
##                                              TAYA 
##                                               172 
##                                            TAYENG 
##                                               214 
##                                             TAYOM 
##                                               183 
##                                            TEDUNG 
##                                               280 
##                                         TEEN KILO 
##                                               304 
##                               TEGO GAMLIN VILLAGE 
##                                               231 
##                                            TEKANG 
##                                               370 
##                                     TELAM VILLAGE 
##                                               288 
##                                              TELE 
##                                               125 
##                            TELLULIANG (OLD & NEW) 
##                                               796 
##                                      TENGA MARKET 
##                                               970 
##                                      TENGA VALLEY 
##                                               767 
##                                           TENGMAN 
##                                               185 
##                                            TENGMO 
##                                               139 
##                                          TENGPUNG 
##                                               135 
##                                            TENGRI 
##                                               107 
##                                        TENZINGAON 
##                                                20 
##                           TEZU TOWNSHIP BLOCK - I 
##                                               893 
##                         TEZU TOWNSHIP BLOCK - III 
##                                              1269 
##                          TEZU TOWNSHIP BLOCK - IV 
##                                              1295 
##                           TEZU TOWNSHIP BLOCK - V 
##                                               893 
##                          TEZU TOWNSHIP BLOCK - VI 
##                                              1871 
##                         TEZU TOWNSHIP BLOCK - VII 
##                                              1636 
##                                           TEZUGAM 
##                                                44 
##                                            THALLA 
##                                                21 
##                                         THAMIYANG 
##                                               119 
##                                           THAMLOM 
##                                               141 
##                                         THAMPTONG 
##                                                70 
##                                       THARGELLING 
##                                               140 
##                                          THEMBANG 
##                                               340 
##                                            THESSA 
##                                               196 
##                                           THIKSHI 
##                                                43 
##                                      THINGBU H.Q. 
##                                               152 
##                                    THINSA VILLAGE 
##                                               599 
##                                         THONGLENG 
##                                               368 
##                                   THONGTHUNG HAVI 
##                                                65 
##                                          THRILLAM 
##                                               249 
##                                          THRIZINO 
##                                               819 
##                                 THUNGJONG VILLAGE 
##                                               156 
##                                          THUNGREE 
##                                               285 
##                                      TIGRA MIRBUK 
##                                               785 
##                                             TIKDO 
##                                               550 
##                                   TIKHAK KHAMLANG 
##                                                99 
##                                      TIKHAK TAIPI 
##                                               223 
##                                       TILANGKIONG 
##                                                93 
##                                   TILLA / QUIBANG 
##                                               220 
##                                            TILLAI 
##                                               168 
##                                             TILLI 
##                                               335 
##                                             TIMBA 
##                                               125 
##                                             TINAI 
##                                               120 
##                                             TIPPI 
##                                               607 
##                                TIRBIN TOWN (SIRU) 
##                                               245 
##                                      TIRI VILLAGE 
##                                                94 
##                                        TISSA CAMP 
##                                               288 
##                                            TISSUE 
##                                               284 
##                                            TITRIT 
##                                               231 
##                                              TODE 
##                                               204 
##                                            TONGMA 
##                                               125 
##                                              TOON 
##                                               391 
##                                   TORAJAN VILLAGE 
##                                               312 
##                                              TORU 
##                                               234 
##                                         TOTPU - I 
##                                               252 
##                                         TOWN BILL 
##                                               484 
##                         TRANSPORT / H.S.S. COLONY 
##                                               380 
##                                    TRANSPORT AREA 
##                                               779 
##                                  TRANSPORT COLONY 
##                                               370 
##                                       TSERING PAM 
##                                               106 
##                                            TULUHI 
##                                               111 
##                                    TUMBIN VILLAGE 
##                                               119 
##                                           TUMLANG 
##                                               452 
##                                             TUNGI 
##                                               103 
##                                           TUNGMAR 
##                                               294 
##                                     TURET VILLAGE 
##                                               262 
##                                  TUTING PANIKHETI 
##                                               256 
##                                       TUTING TOWN 
##                                               961 
##                                    TUTNYU VILLAGE 
##                                               364 
##                                         TUWILIANG 
##                                               123 
##                                           TWO HUT 
##                                               651 
##                        TYPE - I COLONY (PART - I) 
##                                               376 
##                       TYPE - I COLONY (PART - II) 
##                                               622 
##                      TYPE - II COLONY & SHANTIPUR 
##                                               718 
##                                          TYPE - V 
##                                               670 
##                                               ULI 
##                                               241 
##                      UPPER BHALUKPONG(NORTH WING) 
##                                               515 
##                      UPPER BHALUKPONG(SOUTH WING) 
##                                               611 
##                             UPPER BORAJAN VILLAGE 
##                                               253 
##                             UPPER COLONY PART - I 
##                                               480 
##                            UPPER COLONY PART - II 
##                                               405 
##                                       UPPER DZONG 
##                                               280 
##                                         UPPER GAI 
##                                               156 
##                                       UPPER HINDA 
##                                               747 
##                                        UPPER JUMI 
##                                               407 
##                               UPPER KOLAM VILLAGE 
##                                               482 
##                                       UPPER LEYAK 
##                                               337 
##                                     UPPER LICHILA 
##                                               365 
##                                    UPPER LIKABALI 
##                                               285 
##                                UPPER MIAO (NORTH) 
##                                               417 
##                                UPPER MIAO (SOUTH) 
##                                               830 
##                                     UPPER MILLANG 
##                                               260 
##                                  UPPER MUDOI DEEP 
##                                                40 
##                             UPPER NYAPIN TOWNSHIP 
##                                               535 
##                                        UPPER ROWA 
##                                               308 
##                                     UPPER SEIJOSA 
##                                               846 
##                                     UPPER SILATOO 
##                                               348 
##                                      UPPER TARASO 
##                                               685 
##                              UPPERCHINHAN VILLAGE 
##                                                74 
##                                         URGELLING 
##                                               572 
##                                               VEO 
##                                               705 
##                                 VETERINARY COLONY 
##                                               453 
##                       VETERINARY LINE MAYU - I(A) 
##                                               469 
##                 VETERINARY OFFICE COMPLEX EASTERN 
##                                               980 
##                     VETTY. OFFICE COMPLEX WESTERN 
##                                               828 
##                    VETTY. OFFICE COPLEX EAST SIDE 
##                                               665 
##                   VETTY. OFFICE COPLEX SOUTH SIDE 
##                                               770 
##                               VIJAYNAGAR (HAZOLO) 
##                                               801 
##                                     VOTNU VILLAGE 
##                                               435 
##                                             WABIA 
##                                               234 
##                                       WADA BAGANG 
##                                               334 
##                                            WAFANG 
##                                                45 
##                                  WAGON PATHAR - I 
##                                               561 
##                                          WAGUN-II 
##                                               413 
##                                     WAGUN PONTHAI 
##                                               460 
##                                              WAII 
##                                               454 
##                                       WAK (RAGYI) 
##                                               279 
##                                          WAKHETNA 
##                                               303 
##                                   WAKKA TOWN H.Q. 
##                                               185 
##                                 WAKKA VILLAGE - I 
##                                               475 
##                                WAKKA VILLAGE - II 
##                                               760 
##                                             WAKKE 
##                                               160 
##                                        WAKRO TOWN 
##                                               925 
##                                            WALONG 
##                                               135 
##                                           WANGHOO 
##                                               261 
##                                             WANLI 
##                                                27 
##                                              WANU 
##                                               818 
##                                           WARJUNG 
##                                               207 
##                                        WARRANGPAM 
##                                                93 
##                                 WASATHONG VILLAGE 
##                                               282 
##                                       WATHIN VILL 
##                                               182 
##                                              WATI 
##                                                72 
##                                            WATLOM 
##                                               186 
##                                             WATTE 
##                                               238 
##                                             WESHI 
##                                               150 
##                                           WESSANG 
##                                               177 
##                                            WINGKO 
##                                               729 
##                                  WINGSENG NONGTAW 
##                                               304 
##                                           WINTONG 
##                                                41 
##                                       WOTTE CHEDA 
##                                               190 
##                                    WOWOI (SUBBAN) 
##                                               145 
##                                              XXXX 
##                                               510 
##                                              YABA 
##                                               317 
##                                      YABHI (D / H 
##                                               294 
##                                           YACHUGI 
##                                               296 
##                                           YACHULI 
##                                               593 
##                                           YAGLUNG 
##                                               332 
##                                           YAGRUNG 
##                                               625 
##                                             YAKHA 
##                                               260 
##                                         YAKI TATO 
##                                               416 
##                                             YAKLI 
##                                               158 
##                                            YAKUNG 
##                                                90 
##                                            YANGFO 
##                                               525 
##                                           YANGSEY 
##                                               295 
##                                            YANGTE 
##                                               579 
##                                           YANKANG 
##                                               200 
##                                            YANMAN 
##                                               381 
##                                             YAPHA 
##                                               254 
##                                             YAPIK 
##                                               150 
##                                             YARBA 
##                                               337 
##                                        YARTEPOUBE 
##                                               226 
##                                            YASONG 
##                                               131 
##                                            YATONG 
##                                               308 
##                                            YATTAP 
##                                               448 
##                                            YAYUNG 
##                                               132 
##                                            YAZALI 
##                                               788 
##                                          YEALIANG 
##                                               559 
##                                     YEGRI VILLAGE 
##                                               256 
##                                    YEKSHI VILLAGE 
##                                               238 
##                                   YEMSING VILLAGE 
##                                               453 
##                                            YEWANG 
##                                               755 
##                                             YIBUK 
##                                               504 
##                                     YIBUK VILLAGE 
##                                               273 
##                                      YIGA VILLAGE 
##                                                99 
##                                         YIGI KAUM 
##                                               640 
##                                    YINGKU VILLAGE 
##                                               231 
##                                YIO (MOLO) VILLAGE 
##                                                77 
##                                       YIO VILLAGE 
##                                               100 
##                                             YOGLU 
##                                               630 
##                                    YOGONG VILLAGE 
##                                               170 
##                                            YOIZAT 
##                                               218 
##               YOJI - YORA / ITBP AREA / K.V. AREA 
##                                               376 
##                                               YOM 
##                                               174 
##                                            YOMCHA 
##                                               329 
##                                             YOMDO 
##                                               265 
##                                    YOMGAM VILLAGE 
##                                               257 
##                                             YORDA 
##                                               400 
##                                             YORDO 
##                                               214 
##                                            YORKUM 
##                                               314 
##                                             YORNI 
##                                               186 
##                                           YORTUNG 
##                                                76 
##                                    YOSING VILLAGE 
##                                               135 
##                                            YOURON 
##                                                33 
##                                              YUBA 
##                                               213 
##                                             YUDIK 
##                                               137 
##                                             YUKER 
##                                               212 
##                                       YULONGRIPAM 
##                                                65 
##                                            YUMLAM 
##                                               513 
##                                          YUTHEMBU 
##                                               669 
##                                         ZAPALIANG 
##                                                82 
##                                              ZARA 
##                                               442 
##                                     ZEDUA VILLAGE 
##                                               587 
##                                     ZEMITHANG H.Q 
##                                               202 
##                                     ZIDO (POKBIR) 
##                                               209 
##                                          ZIMTHUNG 
##                                               269 
##                                        ZINGMURING 
##                                               237 
##                                     ZIRDO VILLAGE 
##                                               294 
##                                              ZONG 
##                                                85 
##                                           ZONGSAM 
##                                               105 
##                               ZOO ROAD, ROING - I 
##                                               535
```
