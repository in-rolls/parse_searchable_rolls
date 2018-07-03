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
## [1] 1068133
```

Unique Values in Sex:


```r
# Unique values in sex
table(arunachal$sex)
```

```
## 
## Female   Male 
## 538501 529632
```

Summary of Age:


```r
# Age
summary(arunachal$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##     0.0    28.0    35.0    38.8    47.0   120.0      81
```

Check if 0 and missing age is from problem in the electoral roll:


```r
arunachal[which(arunachal$age == 0), c("id", "filename")]
```

```
## # A tibble: 3 x 2
##   id         filename        
##   <chr>      <chr>           
## 1 CJG0052779 AC017PART009.pdf
## 2 CJG0052779 AC017PART009.pdf
## 3 CJG0208835 AC017PART003.pdf
```

No. of characters in ID:

```r
# Length of ID
table(nchar(arunachal$id))
```

```
## 
##      4      5      6     10     16 
##      1      3     10 860724 206556
```

Number of characters in pin code:


```r
table(nchar(arunachal$pin_code))
```

```
## 
##       6 
## 1062373
```

Are IDs duplicated?


```r
length(unique(arunachal$id))
```

```
## [1] 722385
```

```r
nrow(arunachal)
```

```
## [1] 1068133
```

```r
a <- table(arunachal[!is.na(arunachal$id), c("id")])
head(a[rev(order(a))])
```

```
## 
##     EG-193     OBT-78 MFF0175323 MFF0174664 MFF0174656 MFF0174649 
##          4          2          2          2          2          2
```


```r
# Net electors
sum(with(arunachal, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 1062373
```

```r
nrow(arunachal)
```

```
## [1] 1068133
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(arunachal$elector_name))
```

```
## 
##      3      4      5      6      7      8      9     10     11     12 
##    156   2094   3770   4496   6521  29561 105328 181090 205158 176083 
##     13     14     15     16     17     18     19     20     21     22 
## 128296  88297  53481  31442  19049  12280   8133   5225   3481   1907 
##     23     24     25     26     27     28     29     30     31     32 
##   1098    553    299    153     90     34     22     12      9     10 
##     33     49 
##      3      1
```

```r
arunachal[which(nchar(arunachal$elector_name) < 4), "filename"]
```

```
## # A tibble: 156 x 1
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
## # ... with 146 more rows
```

Does district have a number?

```r
sum(grepl('[0-9]', arunachal$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(arunachal$parl_constituency)
```

```
## 
## 1 , ARUNACHAL WEST (General) 2 , ARUNACHAL EAST (General) 
##                       620030                       448103
```

```r
table(arunachal$ac_name)
```

```
## 
##              1 - LUMLA (ST)        10 - SEPPA EAST (ST) 
##                       10753                       14509 
##        11 - SEPPA WEST (ST)     12 - PAKKE KESSANG (ST) 
##                        8774                       10317 
##          13 - ITANAGAR (ST)           14 - DOIMUKH (ST) 
##                       81508                       32508 
##           15 - SAGALEE (ST)           16 - YACHULI (ST) 
##                       19821                       21916 
##       17 - ZIRO HAPOLI (ST)             18 - PALIN (ST) 
##                       30650                       19747 
##            19 - NYAPIN (ST)             2 - TAWANG (ST) 
##                       18273                       11812 
##              20 - TALI (ST)         21 - KOLORIANG (ST) 
##                       15267                       17449 
##             22 - NACHO (ST)            23 - TALIHA (ST) 
##                       16581                       12953 
##          24 - DAPORIJO (ST)              25 - RAGA (ST) 
##                       20722                       22914 
##         26 - DUMPORIJO (ST)          27 - LIROMOBA (ST) 
##                       16293                       17558 
##          28 - LIKABALI (ST)             29 - BASAR (ST) 
##                       18150                       22496 
##              3 - MUKTO (ST)        30 - ALONG WEST (ST) 
##                        9597                       16428 
##        31 - ALONG EAST (ST)           32 - RUMGONG (ST) 
##                       18914                       12951 
##          33 - MECHUKHA (ST)  34 - TUTING YINGKIONG (ST) 
##                       13255                       18077 
##            35 - PANGIN (ST)         36 - NARI-KOYU (ST) 
##                       16176                        9196 
##     37 - PASIGHAT WEST (ST)     38 - PASIGHAT EAST (ST) 
##                       18919                       27500 
##              39 - MEBO (ST)             4 - DIRANG (ST) 
##                       14146                       18739 
##     40 - MARIYANG-GEKU (ST)             41 - ANINI (ST) 
##                       13610                        5462 
##            42 - DAMBUK (ST)             43 - ROING (ST) 
##                       17353                       17144 
##              44 - TEZU (ST)         45 - HAYULIANG (ST) 
##                       20936                       15203 
##          46 - CHOWKHAM (ST)            47 - NAMSAI (ST) 
##                       21625                       29694 
##            48 - LEKANG (ST)          5 - KALAKTANG (ST) 
##                       24447                       12406 
##              50 - MIAO (ST)           51 - NAMPONG (ST) 
##                       24096                       11666 
##   52 - CHANGLANG SOUTH (ST)   53 - CHANGLANG NORTH (ST) 
##                        7315                       11385 
##           54 - NAMSANG (ST)       55 - KHONSA EAST (ST) 
##                       14824                       15602 
##       56 - KHONSA WEST (ST) 57 - BORDURIA BOGAPANI (ST) 
##                       14277                        9570 
##          58 - KANUBARI (ST)    59 - LONGDING PUMAO (ST) 
##                       14060                       14551 
##  6 - THRIZINO-BURAGAON (ST)    60 - PONGCHAO WAKKA (ST) 
##                       17246                       18657 
##            7 - BOMDILA (ST)             8 - BAMENG (ST) 
##                       11327                       13525 
##       9 - CHAYANG TAJO (ST) 
##                       14671
```

```r
table(arunachal$police_station)
```

```
## 
##       Along       Anini      Balemu     Balijan  Banderdewa       Basar 
##       35342        5462         755       11975        4347       15264 
##  Bhalukpong      Boleng     Bomdila    Bordumsa   Changlang Chayangtajo 
##        4807       16176       11327       15143       17899       10281 
##    Chowkham      Dambuk    Daporijo     Deomali      Dirang       Diyun 
##       20287        8327       31635       14250       19217        7039 
##     Doimukh   Dumporijo       Gensi   Hayuliang       Hunli    Itanagar 
##       10911       16293        5759       15203        1642       41669 
##   Jairampur    Jengging   Kalaktang       Kamba    Kanubari      Kaying 
##       11666        3197        6497        9382       11444        5578 
##    Kharsang      Khonsa       Kimin   Kolorinag        Laju    Likabali 
##       11556       31194        6480       52463        8829       11407 
##    Liromoba    Longding       Lumla  Mahadevpur        Mebo    Mechukha 
##        4083       14099       10753       24447       14746       11596 
##        Miao Mukto(Jang)       Nacho  Naharlagun      Namsai        Nari 
##        9902        9597       16581       30367       29694        8405 
##     Nirjuli      Nyapin    Pasighat    Pongchau       Pumao        Raga 
##        7106        9984       29769       18657        3068       12001 
##       Roing      Ruksin     Rumgong        Rupa     Sagalee     Sangram 
##       24528       16614        7373       17115       19821        8289 
##     Seijosa       Seppa     Sunpura      Taliha        Tato      Tawang 
##        4805       46242        2340       12953        1659       11812 
##        Tezu      Tirbin      Tuting  Vijoynagar        XXXX      Yazali 
##       18596        7795        7364        2638        5760       21565 
##   Yingkiong      Yomcha        Ziro 
##       21126        3530       30650
```

```r
table(arunachal$mandal)
```

```
## 
##       Along       Anini       Basar      Boleng     Bomdila    Bordumsa 
##       35342        5462       23059       16176       30544       22182 
##   Changlang Chayangtajo    Chowkham      Dambuk    Daporijo     Deomali 
##       17899       11569       20287        8327       60881       15564 
##   Hayuliang       Hunli   Jairampur        Jang    Kanubari      Khonsa 
##       15203        1642       11666        9597       11444       38709 
##   Koloriang    Likabali    Longding       Lumla  Mahadevpur    Mariyang 
##       52463       17166       35824       10753       24447       13610 
##        Mebo    Mechukha        Miao       Nacho      Namsai        Nari 
##       14746       13255       24096       16581       29694        8405 
##      Nyapin    Pasighat        Raga       Roing      Ruksin     Rumgong 
##       18273       29769       12001       24528       16614       12951 
##        Rupa     Sagalee       Seppa      Tawang        Tezu    Thrizino 
##       24367      132676       49759       11812       20936        4807 
##      Tuting   Yingkiong      Yomcha        Ziro 
##        7364       10713       16995       52215
```

```r
table(arunachal$district)
```

```
## 
##               ANJAW           CHANGLANG       DIBANG VALLEY 
##               14695               77074                5462 
##         EAST KAMENG          EAST SIANG        KURUNG KUMEY 
##               61796               85937               70736 
##               LOHIT            LONGDING LOWER DIBANG VALLEY 
##               20936               47268               34497 
##     LOWER SUBANSIRI              NAMSAI          PAPUM PARE 
##               64567               75766              127767 
##              TAWANG               TIRAP         UPPER SIANG 
##               32162               54273               31027 
##     UPPER SUBANSIRI         WEST KAMENG          WEST SIANG 
##               77166               58626              119396
```

```r
arunachal[which(arunachal$district == "2.YORKODOM"), "filename"]
```

```
## # A tibble: 0 x 1
## # ... with 1 variable: filename <chr>
```

```r
table(arunachal$main_town)
```

```
## 
##                            1300 CHAIN LABOUR CAMP 
##                                                 8 
##                                    14 KM PWD CAMP 
##                                               204 
##                       16TH MILE & TEA GARDEN AREA 
##                                               452 
##                            17TH MILE & MILLS AREA 
##                                               618 
##                            28 KM ROING HUNLI ROAD 
##                                                50 
##                                         28TH MILE 
##                                               788 
##                                          2ND MILE 
##                                              1334 
##                             6 KM ROING HUNLI ROAD 
##                                                54 
##                                          6TH MILE 
##                                               152 
##                                73 KM JORAM(SHUIL) 
##                                               307 
##                                         A-2 BLOCK 
##                                               518 
##                                        A - SECTOR 
##                                              2524 
##                     A - SECTOR / PETROL PUMP AREA 
##                                               991 
##                                            ABANGO 
##                                               266 
##                                      ACHINGMURING 
##                                                78 
##                                  ADANE (EMBRANGO) 
##                                                35 
##                                       ADIPASI - I 
##                                               976 
##                                         AGINKONIA 
##                                               219 
##                                       AIR COMPLEX 
##                                               723 
##                                 AIR FIELD (LOWER) 
##                                               834 
##                                          AKINIRIN 
##                                               242 
##                                             AKOBE 
##                                               116 
##                                          ALC LINE 
##                                              2728 
##                                       ALINYE (LG) 
##                                               242 
##                                           ALOMBRO 
##                                                42 
##                                       ALUBARI (A) 
##                                              1960 
##                                        ALUBARI(B) 
##                                              1940 
##                                              AMBA 
##                                              1800 
##                                             AMBAM 
##                                               638 
##                                              AMJI 
##                                               314 
##                                           AMLIANG 
##                                                85 
##                                        AMSUKPINJA 
##                                               552 
##                                             AMULI 
##                                               172 
##                                   ANELIH TOWNSHIP 
##                                               173 
##                                           ANGGING 
##                                               132 
##                                           ANGOLIN 
##                                                41 
##                                     ANGRIM VALLEY 
##                                               250 
##                                              ANGU 
##                                               957 
##                                             ANINI 
##                                              1910 
##                                          ANKALING 
##                                               486 
##                                             ANPUM 
##                                              1712 
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
##                                               238 
##                                 ARANGO(HORUPAHAR) 
##                                               288 
##                                            ARANLI 
##                                                 6 
##                                             ARIBU 
##                                               148 
##                                            ARONLI 
##                                                26 
##                              ARUNACHAL UNIVERSITY 
##                                               549 
##                                            ARUNLI 
##                                                12 
##                                             ARZOO 
##                                               122 
##                                          ASHOMBRA 
##                                               114 
##                                             ATALI 
##                                                11 
##                                           ATHUNLI 
##                                                54 
##                                          ATTARANG 
##                                               300 
##                                             AUNYE 
##                                                15 
##                                             AWOKA 
##                                                17 
##                                         AYA MARDE 
##                                               380 
##                                         AYA NIRIN 
##                                               134 
##                                           AYAMARA 
##                                               164 
##                                     AYENG VILLAGE 
##                                               875 
##                                          B-SECTOR 
##                                              1992 
##                          B - SECTOR / MARKET AREA 
##                                              1268 
##                                             BABLA 
##                                               884 
##                                     BABUK VILLAGE 
##                                                68 
##                                     BADAK VILLAGE 
##                                               199 
##                                             BAGBI 
##                                               610 
##                                        BAGIASIYUM 
##                                              1026 
##                                      BAGRA (HIGI) 
##                                              1096 
##                                        BAGRA JEYE 
##                                               240 
##                                        BAGRA LIPU 
##                                               568 
##                                       BAGRA TAKPU 
##                                               330 
##                                             BALEK 
##                                              1456 
##                                    BALEMU VILLAGE 
##                                               652 
##                                          BALINONG 
##                                              1320 
##                                            BALISO 
##                                               412 
##                                  BALISORI VILLAGE 
##                                               141 
##                                        BALUPATHAR 
##                                               211 
##                              BAM VILLAGE PART - I 
##                                               557 
##                             BAM VILLAGE PART - II 
##                                               498 
##                                       BAMENG H.Q. 
##                                               524 
##                                             BAMIN 
##                                              1500 
##                                         BANA CAMP 
##                                               175 
##                            BANDERDEWA (EAST SIDE) 
##                                               943 
##                            BANDERDEWA (WEST SIDE) 
##                                              1700 
##                                           BANFERA 
##                                               565 
##                                            BANGGO 
##                                               650 
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
##                                              2289 
##               BARAPANI BAZAR & VETERINARY COMPLEX 
##                                               958 
##                                         BARCHIPAM 
##                                               403 
##                                            BARING 
##                                               412 
##                                       BARIRIJO HQ 
##                                              1248 
##                                            BARITO 
##                                                52 
##                                         BARO MILE 
##                                               294 
##                                    BASAR MCP / SE 
##                                               356 
##                              BASAR TOWN - I (MEN) 
##                                               452 
##                            BASAR TOWN - I (WOMEN) 
##                                               604 
##                                   BASAR TOWN - II 
##                                               938 
##                                         BASORNALO 
##                                              1498 
##                                       BAT VILLAGE 
##                                               632 
##                                             BATOR 
##                                               380 
##                                             BAYOR 
##                                               258 
## BAZAR AREA/ MEDICAL COLONY/ ENQUIRY OFFICE COLONY 
##                                              1848 
##                                        BAZAR LINE 
##                                              1494 
##                                           BEDAGAM 
##                                                84 
##                                 BEGGING (LORGING) 
##                                               168 
##                                   BEGGING VILLAGE 
##                                               216 
##                                              BELO 
##                                               946 
##                                      BELO VILLAGE 
##                                                91 
##                                              BELU 
##                                               508 
##                                              BENE 
##                                              1214 
##                                            BENGDE 
##                                               368 
##                                      BERA VILLAGE 
##                                               666 
##                            BEROM RIME / PIDI RIME 
##                                               105 
##                                            BERUNG 
##                                               864 
##                                        BETCHELING 
##                                               362 
##                                              BEYE 
##                                               488 
##                                            BEYONG 
##                                               269 
##                                        BHEKULIANG 
##                                               319 
##                                      BHISMAKNAGAR 
##                                                96 
##                                          BHOGAMUR 
##                                              1442 
##                                            BICHOM 
##                                              1024 
##                                      BIGI VILLAGE 
##                                                91 
##                                              BIGO 
##                                               381 
##                                        BIJOYPUR-I 
##                                               181 
##                                            BIMPAK 
##                                               182 
##                                              BINE 
##                                               297 
##                                   BINGUNG VILLAGE 
##                                               212 
##                                     BIRI PUNGRUNG 
##                                               736 
##                                              BIRU 
##                                               285 
##                                           BISHING 
##                                                88 
##                                           BIYANLI 
##                                                43 
##                                        BIZARI - A 
##                                               816 
##                                        BIZARI - B 
##                                               850 
##                                          BLEMLENG 
##                                              1058 
##                                             BLONG 
##                                               356 
##                           BN COLONY / FISH MARKET 
##                                              1698 
##                                               BOA 
##                                               210 
##                                     BOA SIMLA - I 
##                                               397 
##                                    BOA SIMLA - II 
##                                               400 
##                                         BOBIA - I 
##                                               379 
##                                     BODAK VILLAGE 
##                                               362 
##                                              BODO 
##                                               694 
##                                  BOGAPANI VILALGE 
##                                               136 
##                                    BOGDO PART - I 
##                                               536 
##                                   BOGDO PART - II 
##                                               858 
##                                             BOGNE 
##                                               220 
##                                     BOGNE VILLAGE 
##                                               782 
##                                      BOGO VILLAGE 
##                                               256 
##                                      BOGU VILLAGE 
##                                               143 
##                                              BOHA 
##                                               492 
##                                 BOJE-KIGI VILLAGE 
##                                               200 
##                                 BOJE LITE VILLAGE 
##                                               185 
##                                 BOJE PARE VILLAGE 
##                                               182 
##                                             BOKAR 
##                                               187 
##                                    BOKFOM VILLAGE 
##                                               155 
##                                      BOLE VILLAGE 
##                                               388 
##                            BOLENG TOWN H.Q. (N/W) 
##                                              1344 
##                                             BOLIK 
##                                               467 
##                                       BOLUNG - II 
##                                              1146 
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
##                                               554 
##                                              BOMI 
##                                               626 
##                                             BOMJA 
##                                               232 
##                                            BOMJIR 
##                                               428 
##                                             BOMNA 
##                                                58 
##                                     BOMTE VILLAGE 
##                                               181 
##                                              BONA 
##                                                42 
##                                          BONGLENG 
##                                               371 
##                                             BONIA 
##                                              1280 
##                                      BOPU VILLAGE 
##                                               329 
##                                         BORAROPUK 
##                                               590 
##                                     BORDUMSA TOWN 
##                                               785 
##                                  BORDUMSA VILLAGE 
##                                               588 
##                                  BORDURIA VILLAGE 
##                                              1301 
##                                   BORGULI VILLAGE 
##                                               707 
##                                          BORISTUM 
##                                               446 
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
##                                               938 
##                                         BRAILIANG 
##                                               183 
##                                          BRALANYI 
##                                                21 
##                                            BRANGO 
##                                                76 
##                                            BRINLI 
##                                               118 
##                                     BROKPALENCHEN 
##                                               236 
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
##                                                60 
##                                        BUMJIPANGA 
##                                               846 
##                                             BUMTE 
##                                               484 
##                                           BUMTENG 
##                                               768 
##                                          BURAGAON 
##                                               403 
##                                      BYALE SULUNG 
##                                               364 
##                                             BYASI 
##                                               258 
##                                        C - SECTOR 
##                                              2817 
##                             C - SECTOR BAZAR AREA 
##                                              1900 
##                                         CF COLONY 
##                                               944 
##                                           CHABANG 
##                                               740 
##                                          CHACHING 
##                                               237 
##                                        CHAGLONGAM 
##                                               193 
##                             CHAILIANG (20TH MILE) 
##                                               251 
##                                            CHAKKA 
##                                               146 
##                                        CHAKMA - I 
##                                               451 
##                                           CHALLAN 
##                                               308 
##                                           CHAMBAB 
##                                                94 
##                                        CHAMELIANG 
##                                               184 
##                                          CHAMPING 
##                                               109 
##           CHAMRO VILLAGE INCLUDES TEA GARDEN AREA 
##                                               150 
##                                           CHANDAR 
##                                               144 
##                 CHANDRA NAGAR BAZAR / POWER HOUSE 
##                                              1800 
##                                          CHANGLAI 
##                                                83 
##                       CHANGLANG AUDITORIUM (WEST) 
##                                               828 
##                   CHANGLANG BSB AUDITORIUM (EAST) 
##                                               535 
##                         CHANGLANG PART - I (EAST) 
##                                               522 
##                         CHANGLANG PART - I (WEST) 
##                                               708 
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
##                                               258 
##                                             CHARU 
##                                               814 
##                                     CHASA VILLAGE 
##                                               807 
##                                  CHATTING VILLAGE 
##                                               623 
##                                          CHATTONG 
##                                               278 
##                                  CHAYANGTAJO H.Q. 
##                                               902 
##                                         CHEBAMARA 
##                                               340 
##                                             CHEGE 
##                                               117 
##                                           CHEGING 
##                                                96 
##                                             CHEKE 
##                                               552 
##                                             CHEKI 
##                                               628 
##                               CHEKORLOMBI VILLAGE 
##                                               504 
##                                            CHELLO 
##                                              1020 
##                                            CHENGO 
##                                               157 
##                                CHENGTHANG VILLAGE 
##                                               206 
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
##                                               206 
##                                          CHILLANG 
##                                               169 
##                                         CHILLIPAM 
##                                               116 
##                                     CHIMI VILLAGE 
##                                               144 
##                                           CHIMIRI 
##                                                56 
##                                     CHIMPU /APP B 
##                                              2213 
##                                            CHINGI 
##                                               175 
##                                         CHINGRING 
##                                               362 
##                                  CHINGRING MURING 
##                                               280 
##                                           CHINGSA 
##                                               209 
##                                   CHINKOI VILLAGE 
##                                               377 
##                                          CHINLANG 
##                                                48 
##                                            CHIPRU 
##                                               162 
##                                           CHIRONG 
##                                                89 
##                                           CHIZANG 
##                                               282 
##                                             CHOBA 
##                                               227 
##                                             CHOLO 
##                                               152 
##                               CHOMUITHONG VILLAGE 
##                                               144 
##                                 CHONGKHOW VILLAGE 
##                                               522 
##                                              CHOP 
##                                               182 
##                                           CHOPEHA 
##                                               816 
##                                            CHOPNU 
##                                              1074 
##                                            CHOPSA 
##                                               218 
##                                             CHOTE 
##                                               221 
##                                        CHOWALIANG 
##                                                77 
##                                          CHOWGONG 
##                                                16 
##                            CHOWKDOK (RANGKATU-II) 
##                                               360 
##                          CHOWKHAM-I (MANPHAKTANG) 
##                                              1118 
##                                     CHOWKHAM - II 
##                                               744 
##                                    CHOWKHAM - III 
##                                              1146 
##                                     CHOWKHAM - IV 
##                                               970 
##                        CHOWKHAM - V(A)(GUNANAGAR) 
##                                              1338 
##                        CHOWKHAM - V(B)(GUNANAGAR) 
##                                              1502 
##                                        CHUAKAMSAR 
##                                                49 
##                                              CHUG 
##                                               882 
##                                            CHULLA 
##                                               247 
##                                            CHULYU 
##                                               307 
##                                          CHUMBANG 
##                                               460 
##                                          CHUMBUNG 
##                                               236 
##                              CHUN (POTIN) VILLAGE 
##                                               133 
##                                           CHURONI 
##                                                23 
##                                       CLUB COLONY 
##                                              1314 
##                                 COFFEE PLANTATION 
##                                               130 
##                  COOPERATIVE LINE ,ROING - II (A) 
##                                               746 
##                                      CRAFT CENTRE 
##                                               501 
##                                        D - SECTOR 
##                                              2632 
##          D - SECTOR / DOORDARSHAN / POSTAL COLONY 
##                                              1566 
##                                 D - SECTOR COLONY 
##                                               497 
##                                      D.N. COLLEGE 
##                                              1872 
##                               D.P.T.E. OYAN (N/W) 
##                                               373 
##                               D.P.T.E. OYAN (S/W) 
##                                               476 
##                               DABA GAMLIN VILLAGE 
##                                               115 
##                                   DADAM I VILLAGE 
##                                              1406 
##                                  DADAM II VILLAGE 
##                                               416 
##                                              DADI 
##                                               106 
##                                  DAFLAGARH FOREST 
##                                               432 
##                                             DAFRI 
##                                               326 
##                                              DAGU 
##                                               898 
##                                               DAI 
##                                               161 
##                                             DAKPE 
##                                               744 
##                                       DALBING - I 
##                                               588 
##                                      DALBING - II 
##                                               324 
##                                      DALI VILLAGE 
##                                               400 
##                                            DAMBUK 
##                                              1164 
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
##                                               576 
##                                          DANGSING 
##                                                64 
##                                              DAPI 
##                                              1380 
##                                            DAPKHU 
##                                               414 
##                                 DAPORIJO EAST - A 
##                                              1488 
##                                 DAPORIJO EAST - B 
##                                              1020 
##                                 DAPORIJO EAST - C 
##                                               733 
##                                 DAPORIJO EAST - D 
##                                               774 
##                                 DAPORIJO WEST - A 
##                                               902 
##                                 DAPORIJO WEST - B 
##                                               644 
##                                 DAPORIJO WEST - C 
##                                               724 
##                                 DAPORIJO WEST - D 
##                                              1410 
##                                        DARAK CAMP 
##                                               546 
##                                             DARBU 
##                                               394 
##                                              DARE 
##                                              1140 
##                                              DARI 
##                                              1126 
##                            DARKA VILLAGE PART - I 
##                                               876 
##                           DARKA VILLAGE PART - II 
##                                               667 
##                                           DARLONG 
##                                               696 
##                                        DARMO - II 
##                                               674 
##                                         DASATHONG 
##                                              1900 
##                                              DASI 
##                                               825 
##                          DCS/ADCS WITH RWD COLONY 
##                                               629 
##                                DEBAN TOURIST CAMP 
##                                                82 
##                                            DEBING 
##                                              1080 
##                                             DEBOM 
##                                               296 
##                                      DECHENGTHANG 
##                                               369 
##                                            DEDOLO 
##                                               804 
##                                              DEDU 
##                                               171 
##                                              DEED 
##                                               403 
##                                        DEED RAKHE 
##                                               698 
##                                             DEGAM 
##                                               326 
##                                              DEGO 
##                                               205 
##                                              DEKE 
##                                               549 
##                                         DELLIPEJI 
##                                               437 
##                                               DEM 
##                                              1144 
##                                          DEMASANG 
##                                                73 
##                                            DENGKA 
##                                               206 
##                                    DENGZI VILLAGE 
##                                               682 
##                                  DENIMISA VILLAGE 
##                                               134 
##                                             DENLO 
##                                               434 
##                                           DEOBEEL 
##                                              1996 
##                                  DEOMALI BLOCK-IV 
##                                              1116 
##                              DEOMALI TOWN BLOCK-I 
##                                              1980 
##                            DEOMALI TOWN BLOCK-III 
##                                               781 
##                           DEOMALI TOWN BLOCK - II 
##                                              1608 
##                             DEOMALI TOWN BLOCK -V 
##                                               575 
##                                              DEPI 
##                                               442 
##                                          DEPIMOLI 
##                                               186 
##                                            DESALI 
##                                               454 
##                                             DETAK 
##                                               163 
##                                         DHARAMPUR 
##                                              1032 
##                                    DHARAMPUR - II 
##                                                95 
##                                            DIBBIN 
##                                               219 
##                                      DIBE VILLAGE 
##                                                34 
##                                           DIBRICK 
##                                               274 
##                                            DIGBAK 
##                                               158 
##                                           DIGGING 
##                                               350 
##                                           DIGNIUM 
##                                               351 
##                                         DIKALMUKH 
##                                               398 
##                                         DIKHIYANG 
##                                                51 
##                                            DIKSHI 
##                                               100 
##                                           DILLING 
##                                                74 
##                                             DIMWE 
##                                               148 
##                                       DINCHANGPAM 
##                                                60 
##                               DINGLIANG (TIDDING) 
##                                                31 
##                                      DIPA VILLAGE 
##                                               802 
##                                             DIPIK 
##                                               158 
##                                        DIPU LAMGU 
##                                               276 
##                                        DIRAK MIRI 
##                                               292 
##                                      DIRAK PATHAR 
##                                               742 
##                          DIRANG H.Q. (EAST WING). 
##                                               895 
##                           DIRANG H.Q. (WEST WING) 
##                                              1934 
##                        DIRANG VILLAGE (EAST WING) 
##                                               489 
##                         DIRANG VILLAGE(WEST WING) 
##                                              1126 
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
##                                                78 
##                                              DODO 
##                                               380 
##                                    DOIDAM VILLAGE 
##                                               636 
##                                           DOIMARA 
##                                               110 
##                                              DOJE 
##                                              1232 
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
##                                               606 
##                                               DON 
##                                               245 
##                                        DONGMARENG 
##                                               788 
##                                  DONGRONG VILLAGE 
##                                               302 
##                                          DONIGAON 
##                                               296 
##                                             DONLI 
##                                               182 
##                DONYI - POLO VIDHYA BHAWAN COMPLEX 
##                                              1376 
##                                            DOPOWA 
##                                                16 
##                                        DORJELLING 
##                                               371 
##                                    DOSING VILLAGE 
##                                               201 
##                                              DOTE 
##                                               520 
##                                             DOYOM 
##                                               157 
##                                            DUCHOK 
##                                               478 
##                                         DUDUNGHAR 
##                                               386 
##                                              DUGI 
##                                               167 
##                                               DUI 
##                                               699 
##                                         DUILINGDI 
##                                               378 
##                                              DUKU 
##                                               133 
##                                              DULA 
##                                               166 
##                                             DULOM 
##                                               415 
##                                      DUMBA MOSANG 
##                                               508 
##                                         DUMPANI-I 
##                                               210 
##                                         DUMPATHAR 
##                                               578 
##                                  DUMPORIJO HQ - I 
##                                              1082 
##                                 DUMPORIJO HQ - II 
##                                               585 
##                                             DUMSI 
##                                               281 
##                                            DUNDRI 
##                                                62 
##                                            DUNGRI 
##                                               119 
##                                            DUNGSE 
##                                               640 
##                                             DUPIT 
##                                               361 
##                                      DUPU VILLAGE 
##                                               125 
##                                         DURALIANG 
##                                               314 
##                                         DURPA - I 
##                                              1432 
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
##                                              1984 
##                       E - SECTOR FOREST PARK AREA 
##                                              1940 
##                                E - SECTOR WESTERN 
##                                              1284 
##                                             EBIYA 
##                                               490 
##                                               EBO 
##                                               298 
##                                           EBRANLI 
##                                                51 
##                         ECHI-SIKU (LOWER) VILLAGE 
##                                                82 
##                                 ECHICHIKU VILLAGE 
##                                               371 
##                                  EDUCATION COLONY 
##                                               966 
##                                              EFFA 
##                                               442 
##                                          EGO CAMP 
##                                               156 
##                                             EIYUM 
##                                               244 
##                                          EKHATAYA 
##                                               634 
##                                    ELEPHANT FLAT. 
##                                               106 
##                                             ELOPE 
##                                                92 
##                                            EMBONG 
##                                               220 
##                                         EMBORIANG 
##                                               193 
##                                             EMCHI 
##                                               958 
##                                           EMPHONG 
##                                               544 
##                                            EMPHUM 
##                                               247 
##                                             EMULI 
##                                                91 
##                                             EMUYI 
##                                               100 
##                                ENGINEERING COLONY 
##                                               756 
##                                           ENGOLIN 
##                                                 7 
##                                            EPANLI 
##                                                80 
##                                             ERBUK 
##                                              1040 
##                                             ERING 
##                                               910 
##                                 ESHIKARTE VILLAGE 
##                                               690 
##                                  ESSIRITE VILLAGE 
##                                               244 
##                                              ESSO 
##                                               119 
##                                             ETABE 
##                                               114 
##                                       ETALIN B.P. 
##                                               404 
##                                            EYANLI 
##                                                64 
##                                               EYI 
##                                               898 
##                                        F - SECTOR 
##                                               538 
##                        F - SECTOR COLONY,ITANAGAR 
##                                              1390 
##                                           FENGCHE 
##                                               510 
##                                             FLAGO 
##                                               251 
##                                     FOREST COLONY 
##                                               786 
##                         FOREST COLONY(G - SECTOR) 
##                                               962 
##                                              FUBA 
##                                              1308 
##                                        G - SECTOR 
##                                              2594 
##                                 G -EXTENSION / SP 
##                                              2025 
##                                       G EXTENSION 
##                                              1938 
##                                               GAA 
##                                               606 
##                                               GAB 
##                                               106 
##                                 GADI MESI VILLAGE 
##                                               225 
##                                     GADUM VILLAGE 
##                                               518 
##                                      GAKO VILLAGE 
##                                               644 
##                                           GALENJA 
##                                               435 
##                                      GALU VILLAGE 
##                                               228 
##                                    GAMENG VILLAGE 
##                                               153 
##                                              GAMI 
##                                               364 
##                                    GAMKAK VILLAGE 
##                                               250 
##                                          GAMLIANG 
##                                               102 
##                              GANDHIGRAM (SIDIKUH) 
##                                               978 
##                               GANGA BLOCK 1 AND 2 
##                                               796 
##                                           GANGNEE 
##                                               396 
##                                             GANTE 
##                                               327 
##                                              GAPO 
##                                               212 
##                                      GARU VILLAGE 
##                                               284 
##                                 GARUBANDHA FOREST 
##                                               792 
##                                   GASHENG VILLAGE 
##                                               243 
##                                      GATE VILLAGE 
##                                               296 
##                                           GECHING 
##                                               422 
##                                      GEKU - KUMKU 
##                                               452 
##                                      GEKU - PERAM 
##                                              1004 
##                                         GEKU H.Q. 
##                                              1104 
##                                           GELLING 
##                                               237 
##                                  GEMOTALI VILLAGE 
##                                               253 
##                                        GENSI TOWN 
##                                              1586 
##                                             GETTE 
##                                               786 
##                                        GIAMUKRIJO 
##                                               240 
##                                              GIBA 
##                                               392 
##                                           GIDDING 
##                                               560 
##                                            GIKUNG 
##                                               338 
##                                             GIMBA 
##                                               794 
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
##                                                84 
##                                             GOBUK 
##                                               854 
##                                         GOGNE DUI 
##                                               154 
##                                     GOGRA VILLAGE 
##                                               413 
##                                GOHPUR TINALI AREA 
##                                              1904 
##                                          GOILIANG 
##                                               236 
##                                              GOJU 
##                                              1344 
##                                             GOMIN 
##                                                44 
##                                           GOMKANG 
##                                               313 
##                                          GONGKHAR 
##                                               570 
##                                 GORBOW (JAMIYANG) 
##                                                74 
##                                      GORI VILLAGE 
##                                              1904 
##                                     GORLUNG (S/W) 
##                                              1088 
##                                            GOSANG 
##                                               188 
##                             GREFF CAMP ARE,EZENGO 
##                                               627 
##                                        GSI COLONY 
##                                               310 
##                                             GUCHI 
##                                               274 
##                                           GUMSING 
##                                               354 
##                                             GUMTE 
##                                               160 
##                                          GUMTHUNG 
##                                                33 
##                                         GUMTO - I 
##                                               442 
##                                           GUMTUNG 
##                                               238 
##                                            GUNGTE 
##                                              1072 
##          GURUDWARA COLONY UPTO DCS OFFICE COMPLEX 
##                                               640 
##                                            GYAMAR 
##                                               344 
##                                          GYAMDONG 
##                                               232 
##                                           GYASING 
##                                               302 
##                                        H - SECTOR 
##                                               702 
##                                                HA 
##                                               368 
##                                             HABIA 
##                                                81 
##                                             HADAP 
##                                               238 
##                                        HALAIKRONG 
##                                               106 
##                                            HALENG 
##                                               102 
##                                         HAMALIANG 
##                                               132 
##                                          HAMATONG 
##                                               104 
##                                        HAMBAPINDA 
##                                               268 
##                                        HANALTHUNG 
##                                               202 
##                                            HANING 
##                                               284 
##                                            HANKAR 
##                                               498 
##                                             HARAK 
##                                               123 
##                                          HARI - A 
##                                              1604 
##                                          HARI - B 
##                                               714 
##                                          HARI - C 
##                                              1578 
##                                         HARIPUR-I 
##                                               556 
##                                     HASSE - RUSSA 
##                                               812 
##                                          HATIDUBA 
##                                               162 
##                                        HAWAI H.Q. 
##                                               894 
##                                    HAYULIANG TOWN 
##                                              1834 
##                                        HDS COLONY 
##                                               758 
##                                            HEBANG 
##                                              1148 
##                                              HEMI 
##                                               174 
##                                         HEMOIBUNG 
##                                               802 
##                                            HERONG 
##                                               158 
##                                      HETLONG VILL 
##                                                93 
##                                            HETMAN 
##                                                89 
##                                              HIBA 
##                                               388 
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
##                                               224 
##                                             HIPPO 
##                                                74 
##                                              HIRI 
##                                               260 
##                                             HIRIK 
##                                               648 
##                                           HISSANG 
##                                               518 
##                                              HIYA 
##                                              1458 
##                                    HOLLONGI NISHI 
##                                              1380 
##                                              HOMI 
##                                               914 
##                                              HONE 
##                                               208 
##                                          HONG - A 
##                                               855 
##                                          HONG - B 
##                                              1928 
##                                          HONG - C 
##                                              1098 
##                                          HONG - D 
##                                               527 
##                                            HONKAP 
##                                               294 
##                                           HOONGLA 
##                                               734 
##                                        HORU PUTUK 
##                                               135 
##                                           HOSTLAM 
##                                               186 
##                                              HOTE 
##                                                74 
##                                        HSS COLONY 
##                                              1416 
##                                          HUILIANG 
##                                                99 
##                                     HUKAN VILLAGE 
##                                               444 
##                                            HUKANI 
##                                                40 
##                                             HUNLI 
##                                               300 
##                                         HUSSIGAON 
##                                                78 
##                                             IDILI 
##                                                62 
##                                             IDULI 
##                                               469 
##                                   INDUSTRIAL AREA 
##                                               697 
##                                             INJAN 
##                                              1634 
##                                              INJU 
##                                               142 
##                                             INNAO 
##                                              1304 
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
##                                               130 
##                                      JAGAN VILLGE 
##                                               932 
##                                            JAIPUR 
##                                              1956 
##                                         JAKSITARA 
##                                               886 
##                                         JAMBUPANI 
##                                                64 
##                                      JAMIRI POINT 
##                                               240 
##                                         JANACHING 
##                                               356 
##                                             JANBO 
##                                               204 
##                                            JANGDA 
##                                               279 
##                                              JATE 
##                                                 8 
##                                         JAWA CAMP 
##                                               492 
##                                     JAYANG BAGANG 
##                                               347 
##                                           JAYANTI 
##                                               142 
##                                          JEJUDADA 
##                                               578 
##                                              JEKE 
##                                               578 
##                                              JEKO 
##                                               416 
##                                             JELLY 
##                                               634 
##                                          JENGGING 
##                                               353 
##                                             JERAM 
##                                               459 
##                                      JERIGAON - A 
##                                               720 
##                                           JERLING 
##                                               338 
##                                              JERU 
##                                               494 
##                                               JHA 
##                                               234 
##                                           JIA - I 
##                                              1080 
##                                          JIA - II 
##                                               968 
##                                         JIA - III 
##                                               590 
##                                            JIGAON 
##                                               365 
##                                              JIGI 
##                                              1086 
##                                          JIMBARAI 
##                                              1024 
##                                      JIME VILLAGE 
##                                                90 
##                                            JIRDIN 
##                                              1030 
##                                              JITU 
##                                               121 
##                                            JOKHIO 
##                                               165 
##                                       JOLLANG - I 
##                                              1570 
##                                             JOLLY 
##                                               816 
##                                JOMLO-BARI VILLAGE 
##                                               528 
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
##                                               528 
##                                          JONA - I 
##                                               810 
##                                        JONGJIHAVI 
##                                               478 
##                                      JONGLIPATHAR 
##                                               122 
##                                       JONGPHOHATE 
##                                               219 
##                                           JONGRAM 
##                                               240 
##                                             JORAM 
##                                               464 
##                                   JORSING VILLAGE 
##                                               348 
##                                              JORU 
##                                               390 
##                                       JOTTE CHEDA 
##                                               217 
##                                   JUMDANG VILLAGE 
##                                                60 
##                       JUNGMAICHUNG (RANGKATU-III) 
##                                               174 
##                                    JUNGMAISUNG II 
##                                               138 
##                                           JUNGPAM 
##                                               159 
##                                        JYOTINAGAR 
##                                               702 
##                                        JYOTIPUR-I 
##                                               344 
##                                      JYOTSNAPUR-I 
##                                               250 
##                                            KABANG 
##                                                38 
##                                              KABU 
##                                              1680 
##                                             KACHA 
##                                               142 
##                                     KADAI VILLAGE 
##                                               252 
##                                          KADASILA 
##                                                74 
##                             KADEYA (BANA VILLAGE) 
##                                               470 
##                                             KAFLA 
##                                               193 
##                                      KAGI VILLAGE 
##                                               132 
##                                      KAIKHEPATHAR 
##                                               464 
##                                    KAIMAI VILLAGE 
##                                              1634 
##                                KAIMOI VILLAGE - I 
##                                               461 
##                                              KAJI 
##                                               250 
##                                             KAKKI 
##                                               162 
##                                             KAKOI 
##                                               535 
##                                           KAKUKAO 
##                                               808 
##                                    KALAKTANG TOWN 
##                                              1312 
##                                 KALAKTANG VILLAGE 
##                                               344 
##                                      KALEK MIRBUK 
##                                               358 
##                                       KALING - II 
##                                               116 
##                                    KALLEK VILLAGE 
##                                                80 
##                                            KALONG 
##                                              1190 
##                                       KAMALANCHEN 
##                                               172 
##                                             KAMBA 
##                                               456 
##                                           KAMBANG 
##                                               224 
##                                     KAMBU VILLAGE 
##                                               478 
##                                   KAMCHAM VILLAGE 
##                                               444 
##                          KAMDAK (EVEREST) VILLAGE 
##                                               196 
##                                        KAMENGBARI 
##                                               152 
##                              KAMHUA-NOKSA VILLAGE 
##                                               497 
##                            KAMHUA NOKNU-I VILLAGE 
##                                               974 
##                           KAMHUA NOKNU-II VILLAGE 
##                                               468 
##                                             KAMJA 
##                                               296 
##                                KAMKI DEGO VILLAGE 
##                                               824 
##                                        KAMKI FARM 
##                                               100 
##                                     KAMKI VILLAGE 
##                                               465 
##                                    KAMKUH - RUSSA 
##                                               164 
##                                     KAMLANG NAGAR 
##                                                90 
##                                            KAMLAT 
##                                               194 
##                                             KAMNU 
##                                               103 
##                                           KAMPONG 
##                                                56 
##                                             KAMRA 
##                                               156 
##                                           KAMRUNG 
##                                               554 
##                                            KAMSAR 
##                                               176 
##                                      KANE VILLAGE 
##                                                27 
##                                           KANGKHO 
##                                               164 
##                                          KANGKONG 
##                                               674 
##                                    KANGKU VILLAGE 
##                                               816 
##                                            KANING 
##                                               156 
##                                              KANO 
##                                               122 
##                                           KANTANG 
##                                                96 
##                                     KANUBARI H.Q. 
##                                               559 
##                                         KAOPATANI 
##                                              1608 
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
##                                               574 
##                               KARBAK MOLI VILLAGE 
##                                               308 
##                                     KARDO VILLAGE 
##                                               163 
##                                              KARE 
##                                               324 
##                                             KARHE 
##                                               142 
##                                             KARKO 
##                                              1214 
##                                             KARLE 
##                                               450 
##                                              KARO 
##                                               594 
##                                             KAROI 
##                                               380 
##                                  KARSINGSA (EAST) 
##                                               949 
##                                  KARSINGSA (WEST) 
##                                               613 
##                                         KASANGLAT 
##                                                71 
##                                        KATAN H.Q. 
##                                               740 
##                                            KATHAN 
##                                               184 
##                           KATO / NEW KATO VILLAGE 
##                                               762 
##                                          KAYANADI 
##                                               156 
##                                    KAYI ( BOTAK ) 
##                                               394 
##                              KAYI (DUMDE) VILLAGE 
##                                               111 
##                                  KAYI(MEKA - III) 
##                                               564 
##                                       KAYING CAMP 
##                                               392 
##                           KAYING VILLAGE / TUYING 
##                                               542 
##                                              KEBA 
##                                              1582 
##                                            KEBALI 
##                                                94 
##                             KEBANG (RADA) VILLAGE 
##                                               134 
##                             KEBANG (SOLE) VILLAGE 
##                                               272 
##                                    KEBANG VILLAGE 
##                                               170 
##                                              KEBI 
##                                               498 
##                                             KEBIA 
##                                               104 
##                                           KEMBING 
##                                               313 
##                                           KENGKHU 
##                                               456 
##                                     KENON VILLAGE 
##                                               215 
##                                KERANG - I VILLAGE 
##                                               306 
##                               KERANG - II VILLAGE 
##                                               247 
##                                         KESI TALI 
##                                                76 
##                                      KESSE BAGANG 
##                                               194 
##                                          KHACHANG 
##                                               449 
##                             KHAHINALLA (MADHUBAN) 
##                                                50 
##                             KHALEGA / METENGLIANG 
##                                                34 
##                                          KHALIBOK 
##                                               324 
##                                    KHAMDU VILLAGE 
##                                               284 
##                                       KHAMLAIGLAT 
##                                                83 
##                                 KHANU VILLAGE - I 
##                                               940 
##                                KHANU VILLAGE - II 
##                                               453 
##                                          KHARDUNG 
##                                               303 
##                              KHARMANG / KELEKTANG 
##                                               409 
##                                    KHARSANG JUGLI 
##                                               885 
##                                   KHARSANG TINALI 
##                                              1944 
##                                     KHARSANG TOWN 
##                                              2462 
##                                          KHARTENG 
##                                               540 
##                                          KHARTOOT 
##                                               516 
##                                           KHARUNG 
##                                               134 
##                                     KHASA VILLAGE 
##                                               857 
##                                            KHASSO 
##                                               536 
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
##                                               527 
##                                           KHEMLEE 
##                                               487 
##                                           KHENEWA 
##                                               652 
##                                           KHERANG 
##                                               670 
##                                    KHEREM KACHARI 
##                                               430 
##                                       KHEREM MURA 
##                                               411 
##                                        KHEREMBISA 
##                                               678 
##                                              KHET 
##                                               459 
##                                     KHETI VILLAGE 
##                                               816 
##                                         KHIMIYANG 
##                                               806 
##                                           KHINMEY 
##                                               104 
##                                            KHIRMU 
##                                               746 
##                                        KHOBLETANG 
##                                               298 
##                                           KHODASO 
##                                               470 
##                                    KHOGLA VILLAGE 
##                                               441 
##                                            KHOINA 
##                                               172 
##                              KHORALIANG / PANBARI 
##                                               706 
##                                     KHOUJI PATHAR 
##                                               586 
##                                KHOWATHONG VILLAGE 
##                                               370 
##                                       KHRANGLIANG 
##                                               156 
##                                         KHUCHEP-I 
##                                               182 
##                                        KHUCHEP-II 
##                                               128 
##                                         KHUILIANG 
##                                               184 
##                                       KHUMCHAYKHA 
##                                               326 
##                                             KHUPA 
##                                               334 
##                                             KHUPI 
##                                               540 
##                                          KIBITHOO 
##                                               268 
##                                             KICHO 
##                                               954 
##                                             KILLO 
##                                               504 
##                                      KIMI VILLAGE 
##                                               443 
##                                             KIMIN 
##                                               513 
##                                     KIMIN-II KUDH 
##                                               349 
##                                         KIMIN HQ. 
##                                               930 
##                                     KIYIT VILLAGE 
##                                              1858 
##                                             KODAK 
##                                               294 
##                                            KOKILA 
##                                              1446 
##                                  KOLAGAON VILLAGE 
##                                               756 
##                                    KOLORIANG TOWN 
##                                               444 
##                                            KOLUNG 
##                                                98 
##                                             KOMBO 
##                                               679 
##                        KOMBO HYDEL /YEGGO VILLAGE 
##                                               180 
##                                       KOMBO MOBUK 
##                                              1240 
##                                      KOMBO RAGLAM 
##                                               165 
##                                     KOMKAR RASING 
##                                               690 
##                            KOMSING (KARO) VILLAGE 
##                                               342 
##                                   KOMSING (KUMKU) 
##                                               258 
##                                   KONGKUL VILLAGE 
##                                               246 
##                                    KONGRA/ MATONG 
##                                                72 
##                                            KONGSA 
##                                               293 
##                                     KONNU VILLAGE 
##                                              1288 
##                                     KONSA VILLAGE 
##                                               489 
##                                            KOPILA 
##                                               586 
##                                              KOPU 
##                                                99 
##                                            KORANG 
##                                               492 
##                                            KORAPU 
##                                               400 
##                                           KORAYAR 
##                                               301 
##                                            KORENG 
##                                               424 
##                                            KORONU 
##                                               442 
##                                              KOTO 
##                                               304 
##                                             KOYAM 
##                                               618 
##                                         KOYU H.Q. 
##                                                56 
##                                      KOYU VILLAGE 
##                                               718 
##                                          KRELLING 
##                                               121 
##                                          KREMAPAO 
##                                               648 
##                                        KRISHNAPUR 
##                                               476 
##                                            KROMNA 
##                                               354 
##                                            KRONLI 
##                                                11 
##                                           KROSANG 
##                                                98 
##                                            KROWTY 
##                                                68 
##                                           KUGGING 
##                                               280 
##                                      KUGI (POMTE) 
##                                              1340 
##                                          KUGITAGO 
##                                               980 
##                                           KULLUNG 
##                                               415 
##                                   KUMARI ADIVASHI 
##                                              1468 
##                                    KUMARI KHAMPTI 
##                                               650 
##                                     KUMUNG PATHAR 
##                                               288 
##                                            KUNGBA 
##                                               176 
##                                    KUNTOR VILLAGE 
##                                               486 
##                                 KUNU YAMI VILLAGE 
##                                               414 
##                                          KUPORIJO 
##                                               288 
##                                            KUTUNG 
##                                               296 
##                                            KYAMDO 
##                                               133 
##                                               LAA 
##                                              1025 
##                                              LABA 
##                                               434 
##                                    LACHING BAGANG 
##                                               332 
##                                           LACHONG 
##                                                60 
##                                    LACHUNG YANGJE 
##                                               127 
##                                              LADA 
##                                               872 
##                                             LAGAM 
##                                                28 
##                              LAGGI GAMLIN VILLAGE 
##                                               274 
##                                  LAHO VILLAGE - I 
##                                               501 
##                                 LAHO VILLAGE - II 
##                                               656 
##                                             LAIGI 
##                                               308 
##                                           LAIMOYA 
##                                               390 
##                                 LAJU - II VILLAGE 
##                                              1148 
##                                         LAJU H.Q. 
##                                               805 
##                                      LAKBAK GONGO 
##                                               270 
##                                           LAKTONG 
##                                               444 
##                                            LALUNG 
##                                              1526 
##                                         LAMALIANG 
##                                                68 
##                                            LAMDIK 
##                                                74 
##                                     LAMLO VILLAGE 
##                                               298 
##                                     LAMSA VILLAGE 
##                                               307 
##                                             LAMTA 
##                                                12 
##                                          LANGCHUK 
##                                                80 
##                                          LANGDENG 
##                                               264 
##                                          LANGTENG 
##                                               926 
##                                            LAPNAN 
##                                               661 
##                                            LAPUNG 
##                                               444 
##                                            LAPUSA 
##                                               100 
##                                      LASSUM-PATTE 
##                                               133 
##                                         LATHAO(A) 
##                                              1312 
##                                         LATHAO(B) 
##                                              1398 
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
##                                              1134 
##                                            LELUNG 
##                                               110 
##                                        LEMBERDUNG 
##                                              1062 
##                                            LEMPIA 
##                                              1750 
##                                           LENGBIA 
##                                               233 
##                                    LENGDI - LIANG 
##                                                77 
##                                       LENGFER - I 
##                                               834 
##                                            LENGKA 
##                                               492 
##                                            LENGRO 
##                                               526 
##                                         LEPORIANG 
##                                               726 
##                                   LEPROSY COLONEY 
##                                              1282 
##                                    LEPROSY COLONY 
##                                               194 
##                                            LERIAK 
##                                               389 
##                                      LETE VILLAGE 
##                                               100 
##                                              LEYA 
##                                              1049 
##                                          LHALLUNG 
##                                               460 
##                                          LHOUDUNG 
##                                               444 
##                                 LIBU BENE VILLAGE 
##                                               556 
##                                         LICHI - I 
##                                               214 
##                                           LICHINI 
##                                                44 
##                                           LICHLIT 
##                                               488 
##                                     LIDUK VILLAGE 
##                                               113 
##                                      LIGO VILLAGE 
##                                               169 
##                                              LIGU 
##                                              1034 
##                                     LIKABALI WEST 
##                                               824 
##                                             LIKOR 
##                                               478 
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
##                                               466 
##                                            LINIYA 
##                                               351 
##                                             LINKE 
##                                               454 
##                                          LIPHAKPU 
##                                               219 
##                                             LIPIN 
##                                                96 
##                                              LIPO 
##                                                98 
##                               LIPU NAMCHI VILLAGE 
##                                               142 
##                                      LIPU VILLAGE 
##                                              1284 
##                                     LIROMOBA CAMP 
##                                               273 
##                                      LIRU VILLAGE 
##                                              1376 
##                                              LISH 
##                                               496 
##                                     LISH GOMPACHE 
##                                               443 
##                                   LISSING VILLAGE 
##                                                97 
##                                      LITE VILLAGE 
##                                                71 
##                                  LITEMORI VILLAGE 
##                                               368 
##                                            LOAUNU 
##                                               176 
##                                           LOCHUNG 
##                                               119 
##                                             LOFFA 
##                                               824 
##                                             LOGLU 
##                                               112 
##                                        LOGUM JINI 
##                                              1432 
##                                          LOHITPUR 
##                                               245 
##                                          LOILIANG 
##                                               823 
##                                   LOKPENG VILLAGE 
##                                               232 
##                                             LONDA 
##                                               698 
##                                    LONGBO VILLAGE 
##                                               308 
##                                         LONGCHUNG 
##                                              1116 
##                                     LONGDING TOWN 
##                                              2920 
##                                           LONGHUA 
##                                               385 
##                               LONGKAI VILLAGE - I 
##                                               559 
##                                           LONGKEY 
##                                               464 
##                                        LONGKHOJAN 
##                                               158 
##                                 LONGKHONG VILLAGE 
##                                               196 
##                                  LONGKHOW VILLAGE 
##                                               958 
##                                   LONGKOM PONTHAI 
##                                               404 
##                                 LONGLIANG VILLAGE 
##                                               900 
##                                          LONGLING 
##                                               488 
##                                          LONGLUNG 
##                                               396 
##                                   LONGMAN VILLAGE 
##                                               416 
##                                       LONGNAKSHIA 
##                                               298 
##                                     LONGO VILLAGE 
##                                               782 
##                                           LONGPHA 
##                                               156 
##                                         LONGPHONG 
##                                              1400 
##                                           LONGRAN 
##                                               432 
##                                   LONGSOM VILLAGE 
##                                               713 
##                           LONGSONG - I, II, & III 
##                                                40 
##                                       LONGTE LOTH 
##                                               974 
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
##                                               924 
##                             LOWER CHINHAN VILLAGE 
##                                               690 
##                                       LOWER DZONG 
##                                               178 
##                                        LOWER GIDA 
##                                               280 
##                                        LOWER HEYO 
##                                                99 
##                                        LOWER JOTE 
##                                              1264 
##                                       LOWER KOLAM 
##                                               275 
##                                       LOWER LEYAK 
##                                               175 
##                                LOWER MIAO (NORTH) 
##                                              1040 
##                                     LOWER MILLANG 
##                                               247 
##                             LOWER NYAPIN TOWNSHIP 
##                                               385 
##                                        LOWER SHER 
##                                               423 
##                                LOWER SILATOO MIRI 
##                                              1154 
##                                LOWER SINU VILLAGE 
##                                               394 
##                                           LUAKSIM 
##                                               386 
##                                           LUBRANG 
##                                               239 
##                                             LUCHI 
##                                               372 
##                                         LUGUTHANG 
##                                                64 
##                                       LUI VILLAGE 
##                                              1248 
##                                            LUKBIA 
##                                               586 
##                                             LUMBA 
##                                               618 
##                                        LUMBAKTANG 
##                                                88 
##                                           LUMDUNG 
##                                              1022 
##                                        LUMLA H.Q. 
##                                               619 
##                                             LUMPO 
##                                               667 
##                                           LUNGDUR 
##                                               348 
##                                          LUNGPANG 
##                                               452 
##                                            LUNGSA 
##                                               250 
##                                          LUNGSANG 
##                                               128 
##                                 LUNGSHANG VILLAGE 
##                                               230 
##                                          LUNGTANG 
##                                                45 
##                                            LUNGTE 
##                                               510 
##                                     LUTAK VILLAGE 
##                                               534 
##                                   LUTHONG VILLAGE 
##                                               211 
##                                            LYNGOK 
##                                               144 
##                                            MABIRA 
##                                               183 
##                                           MACHANE 
##                                               364 
##                                           MACHING 
##                                               141 
##                                            MACHUM 
##                                               241 
##                                         MAGANTONG 
##                                               376 
##                                      MAGI VILLAGE 
##                                              1202 
##                                              MAGO 
##                                               372 
##                                           MAGOPAM 
##                                                84 
##                                            MAGRIA 
##                                               146 
##                                      MAHADEVPUR-I 
##                                              1596 
##                                     MAHADEVPUR-II 
##                                               752 
##                                   MAHADEVPUR - IV 
##                                               427 
##                                   MAHADEVPUR TOWN 
##                                               851 
##                                               MAI 
##                                               602 
##                                    MAIHUA VILLAGE 
##                                               532 
##                                          MAILIANG 
##                                               152 
##                                     MAKAT VILLAGE 
##                                               139 
##                                             MAKBA 
##                                                88 
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
##                                               462 
##                                            MANKAO 
##                                               394 
##                                           MANKOTA 
##                                               298 
##                                          MANLINYE 
##                                                44 
##                                         MANMAO HQ 
##                                               244 
##                                    MANMAO VILLAGE 
##                                               454 
##                                            MANMOW 
##                                               570 
##                                      MANPENGLIANG 
##                                               517 
##                                            MANTHI 
##                                               240 
##                                        MANYULIANG 
##                                              1386 
##                                            MARBOM 
##                                               109 
##                                           MARGING 
##                                               246 
##                                     MARIYANG H.Q. 
##                                               817 
##                                            MARKIA 
##                                               153 
##                                             MARME 
##                                               110 
##                                              MARO 
##                                               439 
##                                           MARONLI 
##                                                45 
##                                         MARZINGLA 
##                                               532 
##                                            MATHOW 
##                                               129 
##                                          MATKRONG 
##                                                32 
##                                            MATOLI 
##                                               214 
##                                         MAWAI - I 
##                                               441 
##                                       MAYU - I(B) 
##                                               898 
##                                      MAYU - II(B) 
##                                               766 
##                                             MAYUM 
##                                                94 
##                           MEBO TOWN & DARNE BAZAR 
##                                               761 
##                                      MEBO VILLAGE 
##                                              1912 
##                                        MEBUA CAMP 
##                                               229 
##                                       MECHE MARDE 
##                                               290 
##                                         MEDEMBARI 
##                                               316 
##                                    MEDICAL COLONY 
##                                              2188 
##                    MEDICAL COLONY ,ROING - III(A) 
##                                              1094 
##                       MEDICAL LINE,ROING - II (B) 
##                                               850 
##                                         MEDO CAMP 
##                                              1288 
##                                              MEER 
##                                               228 
##                                      MEGA VILLAGE 
##                                               274 
##                                          MEKA - I 
##                                               926 
##                                         MEKALIANG 
##                                               690 
##                                         MEMBACHUR 
##                                               192 
##                                             MENGA 
##                                               134 
##                                       MENGI KABAK 
##                                               181 
##                                            MENGIO 
##                                              1130 
##                                   MENGKENG KHAMTI 
##                                               770 
##                                      MENGKENGMIRI 
##                                              1192 
##                                           MEPSORO 
##                                               122 
##                                       MER VILLAGE 
##                                               812 
##                                   MESSING VILLAGE 
##                                                61 
##                                       METENGLIANG 
##                                               114 
##                                      MIAO SINGPHO 
##                                               974 
##                                             MICHI 
##                                               922 
##                                           MIDLAND 
##                                               872 
##                                         MIDPU - I 
##                                               984 
##                                           MIGGING 
##                                               350 
##                                           MIGLUNG 
##                                               199 
##                                           MIHUNDO 
##                                               282 
##                                            MIKONG 
##                                               884 
##                                             MIMEY 
##                                               340 
##                                           MINTONG 
##                                              1522 
##                                             MIRBA 
##                                               131 
##                             MIREM VILLAGE (LOWER) 
##                                              1042 
##                             MIREM VILLAGE (UPPER) 
##                                              1006 
##                                             MIRKU 
##                                              1240 
##                                            MIRSAM 
##                                               614 
##                                    MISSION COLONY 
##                                              1940 
##                                            MITAKA 
##                                                60 
##                                              MITE 
##                                               682 
##                                          MITHUMNA 
##                                               158 
##                                  MOBADOKE VILLAGE 
##                                               692 
##                                       MOBANG - II 
##                                               328 
##                                     MODEL VILLAGE 
##                                               984 
##                             MODEL VILLAGE (NAMGO) 
##                                               166 
##                                          MOHIKONG 
##                                                95 
##                                      MOHONG DEORI 
##                                               838 
##                                       MOHONG MURA 
##                                               670 
##                                         MOITRIPUR 
##                                               458 
##                               MOKTOWA - I VILLAGE 
##                                               486 
##                              MOKTOWA - II VILLAGE 
##                                               934 
##                                     MOLOM VILLAGE 
##                                               387 
##                                          MOLORANG 
##                                               404 
##                                            MOMONG 
##                                              1202 
##                                              MONA 
##                                               260 
##                                          MONGKHRA 
##                                               163 
##                                            MONGKU 
##                                               944 
##                                          MONIGONG 
##                                              1262 
##                                  MOPAKHAT VILLAGE 
##                                               992 
##                                    MOPAYA VILLAGE 
##                                               410 
##                                     MOPIT VILLAGE 
##                                               288 
##                           MOPUNG / PUNGKU VILLAGE 
##                                               512 
##                                      MORI VILLAGE 
##                                               434 
##                                  MORSHING VILLAGE 
##                                              1262 
##                                     MOSSANG PUTUK 
##                                                47 
##                                           MOSSING 
##                                               388 
##                                            MOTONG 
##                                                45 
##                                          MOTONGSA 
##                                               125 
##                                    MOTTUM VILLAGE 
##                                              1160 
##                      MOTUM - BENTUK / IFCD COLONY 
##                                               968 
##                                 MOWB - II EASTERN 
##                                              1452 
##                                 MOWB - II WESTERN 
##                                               894 
##                                            MOYABA 
##                                               478 
##                                            MOYING 
##                                               224 
##                                          MPEN - I 
##                                               260 
##                                           MRAMBOO 
##                                                 6 
##                                       MUDANG TAGE 
##                                              1974 
##                                             MUDOI 
##                                               698 
##                                             MUGLI 
##                                               916 
##                                             MUKTO 
##                                               826 
##                                         MUKUTHING 
##                                               150 
##                                        MUNNA CAMP 
##                                               235 
##                                              MURI 
##                                               196 
##                                        MUSHAKSING 
##                                                88 
##                                          NACHIBAN 
##                                               223 
##                                        NACHO H.Q. 
##                                                96 
##                       NAFRA ADMN H.Q. (EAST WING) 
##                                               493 
##                       NAFRA ADMN H.Q. (WEST WING) 
##                                               329 
##                                           NAITONG 
##                                               436 
##                                            NAJANG 
##                                                73 
##                                            NAKANG 
##                                                26 
##                                             NAKHU 
##                                               208 
##                                              NAMA 
##                                               190 
##                                          NAMAZING 
##                                              1272 
##                                    NAMCHER BAGANG 
##                                               686 
##                              NAMCHIK FOREST CAMP. 
##                                               806 
##                                           NAMDANG 
##                                                40 
##                                             NAMEY 
##                                               450 
##                    NAMGHAR/SCHOOL LINE CHETA - II 
##                                               681 
##                  NAMGOI VILLAGE - I, II, III & IV 
##                                               588 
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
##                                              1248 
##                                      NAMPONG NALA 
##                                               729 
##                             NAMSAI BLOCK-I (KABA) 
##                                               989 
##                                   NAMSAI BLOCK-II 
##                                               872 
##                                  NAMSAI BLOCK-III 
##                                               998 
##                       NAMSAI BLOCK-V (SOUTH WING) 
##                                              1204 
##                        NAMSAI BLOCK-V(NORTH WING) 
##                                               979 
##                                 NAMSAI BLOCK-VI(N 
##                                               516 
##                       NAMSAI BLOCK-VI(SOUTH WING) 
##                                               969 
##                                 NAMSAI BLOCK - IV 
##                                               693 
##                                      NAMSANG H.Q. 
##                                               401 
##                               NAMSANGMUKH VILLAGE 
##                                               818 
##                                            NAMSHU 
##                                               928 
##                                   NAMSING VILLAGE 
##                                              1710 
##                                          NAMTHUNG 
##                                               196 
##                               NAMTOK (RICHI LINE) 
##                                               780 
##                                      NANAM KHAMTI 
##                                               687 
##                                    NANAM KHAMYANG 
##                                               912 
##                                           NANGRAM 
##                                               734 
##                                             NAPIT 
##                                               384 
##                                           NARGANG 
##                                               920 
##                                              NARI 
##                                               527 
##                                         NARI CAMP 
##                                               796 
##                                         NARI H.Q. 
##                                               682 
##                               NARINGWA (MORINGWA) 
##                                                96 
##                                              NASI 
##                                               139 
##                                             NATAM 
##                                               315 
##                              NATUN KHETI VILLEAGE 
##                                               556 
##                                              NAVA 
##                                               208 
##                                             NAYAM 
##                                               107 
##                                            NAYANG 
##                                               194 
##                                            NEELAM 
##                                               443 
##                                     NEEPCO COLONY 
##                                              1449 
##                                            NEKING 
##                                               190 
##                                        NENCHALAYA 
##                                               701 
##                                            NEOTAN 
##                                               734 
##                                            NEPUWA 
##                                               216 
##                                              NERE 
##                                               342 
##                                            NEREWA 
##                                               288 
##                                    NERIST COMPLEX 
##                                              2132 
##                                      NEW-MOHONG I 
##                                              1050 
##                                     NEW-MOHONG II 
##                                               379 
##                                         NEW ABALI 
##                                               303 
##                                         NEW ALONI 
##                                                98 
##                                         NEW ANAYA 
##                                                87 
##                                    NEW BAZAR LINE 
##                                               812 
##                                         NEW BORAK 
##                                               112 
##                               NEW BUNTING VILLAGE 
##                                               131 
##                                     NEW CHANGLANG 
##                                               385 
##                                       NEW DANGLAT 
##                                               414 
##                                NEW DARING VILLAGE 
##                                               484 
##                                          NEW DEKA 
##                                               232 
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
##                                              1366 
##                                NEW KOTHIN VILLAGE 
##                                               678 
##                               NEW KOTHUNG VILLAGE 
##                                               270 
##                              NEW LAINWANG VILLAGE 
##                                               376 
##                               NEW LAPTANG VILLAGE 
##                                               172 
##                                          NEW LIDA 
##                                               520 
##                                        NEW LISSAN 
##                                               446 
##                               NEW LONGTOI VILLAGE 
##                                                60 
##                                         NEW LUMLA 
##                                              1110 
##                             NEW PANIDURIA VILLAGE 
##                                                70 
##                              NEW PHINTING VILLAGE 
##                                               138 
##                                       NEW POBLUNG 
##                                               124 
##                                       NEW RANGRAN 
##                                               110 
##                                         NEW REDDI 
##                                               338 
##                                          NEW RIBA 
##                                               271 
##                                          NEW RILO 
##                                               290 
##                                       NEW SALLANG 
##                                               124 
##                                         NEW SEPPA 
##                                               390 
##                                         NEW SEREN 
##                                               102 
##                                       NEW SILATOO 
##                                              1186 
##                                  NEW SOHE LAKTONG 
##                                                53 
##                                        NEW SOPUNG 
##                                               169 
##                                NEW SUBANG VILLAGE 
##                                               172 
##                                         NEW TELAM 
##                                               202 
##                                       NEW THAMLOM 
##                                               256 
##                                        NEW YANMAN 
##                                               866 
##                                             NGABA 
##                                               243 
##                                          NGAMDING 
##                                               128 
##                                           NGAMING 
##                                               376 
##                                          NGECHANG 
##                                               134 
##                                    NGENSI VILLAGE 
##                                               208 
##                                 NGINU VILLAGE - I 
##                                               681 
##                                NGINU VILLAGE - II 
##                                              1900 
##                                    NGISSA VILLAGE 
##                                              1044 
##                                 NGOITHONG VILLAGE 
##                                               294 
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
##                                               494 
##                                   NIANU VILLAGE-I 
##                                              1742 
##                                            NIAUSA 
##                                               954 
##                                  NICHOBA (NILOBA) 
##                                               252 
##                                            NIGLOK 
##                                               252 
##                                              NIJI 
##                                               307 
##                                             NIKJA 
##                                               644 
##                                             NIKTE 
##                                               469 
##                                            NILANG 
##                                               105 
##                                           NILLING 
##                                               227 
##                                              NILO 
##                                               364 
##                                             NILOK 
##                                                84 
##                                              NIMA 
##                                               237 
##                                             NIMAR 
##                                               282 
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
##                                               762 
##                                     NOGNA VILLAGE 
##                                               522 
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
##                                               442 
##                                            NYAMPU 
##                                               143 
##                                           NYERING 
##                                                45 
##                           NYIGAM VILLAGE PART - I 
##                                               928 
##                          NYIGAM VILLAGE PART - II 
##                                               898 
##                                     NYODU VILLAGE 
##                                               336 
##                                            NYOGIN 
##                                               890 
##                                       NYOKILANGHI 
##                                               117 
##                                            NYORAK 
##                                               354 
##                                       NYUK MADUNG 
##                                              1122 
##                                           NYUKONG 
##                                                72 
##         O POINT TINALI NYOKUM LAPANG/6KM NH-52(A) 
##                                              1396 
##                  O PT TINALI BAZAR AREA/ADI BOSTI 
##                                               674 
##                                          OLD BULO 
##                                               408 
##                               OLD BUNTING VILLAGE 
##                                               157 
##                             OLD CHANGLANG VILLAGE 
##                                               407 
##                                OLD DARING VILLAGE 
##                                               418 
##                                          OLD DEKA 
##                                               504 
##                               OLD DERENALO (GISI) 
##                                               141 
##                                        OLD DOKPEY 
##                                                92 
##                                          OLD HAJI 
##                                               192 
##                                         OLD JUKHI 
##                                               119 
##                                        OLD KAMLAO 
##                                               241 
##                                OLD KATANG VILLAGE 
##                                               524 
##                                OLD KOTHIN VILLAGE 
##                                               170 
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
##                                              1990 
##                                           OLD NUK 
##                                               470 
##                                         OLD PANIA 
##                                               554 
##                              OLD PHINTING VILLAGE 
##                                                91 
##                                         OLD PUTUK 
##                                                66 
##                                       OLD RANGRAN 
##                                               178 
##                                         OLD RICHI 
##                                               154 
##                                       OLD SALLANG 
##                                               166 
##      OLD SECRETARIAT / DOKUM (NEAR POLICE STATION 
##                                              1980 
##                                         OLD SINGA 
##                                               396 
##                                  OLD TUPI VILLAGE 
##                                              1328 
##                                          OLD ZIRO 
##                                              2042 
##                                            OMPULI 
##                                               866 
##                                      OROK VILLAGE 
##                                               116 
##                                OYAN VILLAGE (S/W) 
##                                              1432 
##                                            OZAKHO 
##                                               432 
##                                       P- SECTOR(A 
##                                              1244 
##                              P - SECTOR EAST SIDE 
##                                               661 
##                              P - SECTOR WEST SIDE 
##                                              1142 
##                                         P.I. LINE 
##                                               632 
##                                             PABUA 
##                                               229 
##                                             PACHI 
##                                               258 
##                                     PACHIN COLONY 
##                                               830 
##                                           PADDING 
##                                               414 
##                                      PADI VILLAGE 
##                                               362 
##                                              PADU 
##                                               582 
##                                             PAFFA 
##                                               222 
##                                             PAGBA 
##                                               858 
##                                              PAGI 
##                                              1272 
##                                            PAGLAM 
##                                               606 
##                                            PAGLEK 
##                                              1782 
##                                              PAGU 
##                                               257 
##                                           PAIGONG 
##                                              1248 
##                                          PAILIANG 
##                                               131 
##                                   PAIMORI VILLAGE 
##                                               146 
##                                              PAJA 
##                                                40 
##                                              PAKA 
##                                               824 
##                                             PAKAM 
##                                               531 
##                                             PAKBA 
##                                               274 
##                                             PAKKE 
##                                               301 
##                                     PAKKE-KESSANG 
##                                               854 
##                                            PAKOTI 
##                                               734 
##                                             PAKPU 
##                                               286 
##                                      PAKPU MALING 
##                                               248 
##                                             PAKRO 
##                                               227 
##                                   PAKSING VILLAGE 
##                                               223 
##                                            PAKSOK 
##                                               106 
##                                           PAKTUNG 
##                                               444 
##                                       PALATARIPAM 
##                                               144 
##                                             PALAV 
##                                               324 
##                                      PALE VILLAGE 
##                                               173 
##                                             PALIN 
##                                               426 
##                                            PALIZI 
##                                               507 
##                                           PALLANG 
##                                                78 
##                                           PALLING 
##                                               116 
##                                               PAM 
##                                               258 
##                                          PAMAGHAR 
##                                               752 
##                                      PAME VILLAGE 
##                                               234 
##                                           PAMPOLI 
##                                               199 
##                                               PAN 
##                                               606 
##                                            PANGGO 
##                                               354 
##                                     PANGI VILLAGE 
##                                               272 
##                                            PANGIA 
##                                               406 
##                                       PANGIN TOWN 
##                                               797 
##                                    PANGIN VILLAGE 
##                                               493 
##                                PANGKANG (JORKANG) 
##                                               332 
##                          PANGKANG (KUMKU) VILLAGE 
##                                               420 
##                                           PANGKAO 
##                                               216 
##                                  PANGKENG VILLAGE 
##                                               710 
##                                            PANGMA 
##                                               244 
##                                            PANGRI 
##                                               236 
##                                              PANI 
##                                               368 
##                                             PANIA 
##                                               409 
##                                 PANIDURIA VILLAGE 
##                                               461 
##                                         PANIKHETI 
##                                                12 
##                                            PANKAR 
##                                               172 
##                                            PANLOM 
##                                               240 
##                               PANSUMTHONG VILLAGE 
##                                               246 
##                                            PANUNG 
##                                               358 
##                                             PANYA 
##                                               560 
##                                              PAPA 
##                                               266 
##                                              PAPI 
##                                               282 
##                                        PAPIKURUNG 
##                                               454 
##                                         PAPU HILL 
##                                              1014 
##                        PAPU NALLAH / PAPU VILLAGE 
##                                              1964 
##                                      PAPU VILLAGE 
##                                               663 
##                                         PARA LINE 
##                                               869 
##                                             PARAM 
##                                               224 
##                                            PARBUK 
##                                               822 
##                                        PARENG - I 
##                                               694 
##                                    PARENG VILLAGE 
##                                               848 
##                                              PARO 
##                                              1000 
##                                    PARONG (KINNE) 
##                                               388 
##                                    PARONG VILLAGE 
##                                               630 
##                                       PARSING - I 
##                                              1336 
##                    PASIGHAT - "G"(FFP/EDN COLONY) 
##                                               618 
##                                      PASIGHAT - A 
##                                               435 
##                                      PASIGHAT - B 
##                                              1340 
##                                      PASIGHAT - D 
##                                               944 
##                                      PASIGHAT - E 
##                                               822 
##                                      PASIGHAT - F 
##                                              1182 
##                       PASIGHAT BAZAR (NORTH WING) 
##                                               639 
##                       PASIGHAT BAZAR (SOUTH WING) 
##                                               648 
##                                              PATE 
##                                               762 
##                                             PATHA 
##                                                68 
##                                        PATHERGAON 
##                                               669 
##                                            PATIWA 
##                                                69 
##                                              PAYA 
##                                               958 
##                                        PAYUM H.Q. 
##                                               490 
##                                              PECH 
##                                              1308 
##                                            PEDUNG 
##                                               565 
##                                              PEEL 
##                                               281 
##                                         PEETAPOOL 
##                                              1358 
##                                       PEGA LOMDAK 
##                                               371 
##                                          PEKIMODI 
##                                               134 
##                                         PEL MILLI 
##                                               482 
##                                              PENI 
##                                               528 
##                                      PERI VILLAGE 
##                                               213 
##                                      PESSING CAMP 
##                                               425 
##                                              PEYA 
##                                               253 
##                                            PHADAM 
##                                               134 
##                                      PHANGLONGLAT 
##                                               123 
##                                          PHANGSUM 
##                                               134 
##                                          PHANGTIP 
##                                               278 
##                                           PHANYAK 
##                                               810 
##                                          PHASSANG 
##                                               175 
##                                         PHILOBARI 
##                                               286 
##                                        PHINBERO-I 
##                                               292 
##                                       PHINBERO-II 
##                                                76 
##                                         PHIRIZINE 
##                                               254 
##                                          PHOMGHAR 
##                                               249 
##                                              PHUP 
##                                               486 
##                                             PHUSA 
##                                                81 
##                                              PIDI 
##                                               272 
##                                        PIGIA GIBA 
##                                               988 
##                                         PILLA - I 
##                                               788 
##                                    PILLUNG MALING 
##                                               370 
##                                    PINCHI VILLAGE 
##                                               418 
##                                           PINGING 
##                                               138 
##                                          PIPOKORO 
##                                               264 
##                                         PIPSORANG 
##                                               346 
##                                              PIPU 
##                                               289 
##                                      PIRA VILLAGE 
##                                               472 
##                                      PIRI VILLAGE 
##                                               224 
##                                        PISTANA HQ 
##                                               213 
##                                          PITCHANG 
##                                               148 
##                                            PIYONG 
##                                              1582 
##                                       POBDI VILL. 
##                                              1102 
##                                           POBLUNG 
##                                               433 
##                                              POBO 
##                                               200 
##                                             POCHU 
##                                               250 
##                                          PODAMARA 
##                                               561 
##                                          PODUMONI 
##                                               979 
##                                     POKTO VILLAGE 
##                                               788 
##                                     POLICE COLONY 
##                                               903 
##                     POLICE COLONY ,ROING - III(B) 
##                                               509 
##                                    POLICE RESERVE 
##                                              1078 
##                          POLO COLONY / TPT COLONY 
##                                              1558 
##               POLO COLONY /CO-OP,APEX BANK COLONY 
##                                              1286 
##                                              POMA 
##                                              1276 
##               POMLIANG (LOILIANG BLOCK -I AND II) 
##                                              1172 
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
##                                               584 
##                                        POTUNG DUI 
##                                               168 
##                                             POUBE 
##                                               464 
##                                     POYOM VILLAGE 
##                                               221 
##                                     PROPER YANGTE 
##                                               245 
##                                         PUAKGUMIN 
##                                               964 
##                                           PUGGING 
##                                               249 
##                                     PUKPU (CHOBA) 
##                                               500 
##                                            PULLOM 
##                                               152 
##                                   PULLONG VILLAGE 
##                                               626 
##                                     PUMAO VILLAGE 
##                                               955 
##                                        PUMTE BAGE 
##                                               129 
##                                             PUNLI 
##                                               146 
##                                      PUSHI NYORAK 
##                                               263 
##                                         PUSHIDOKE 
##                                               318 
##                                             PUTUK 
##                                               424 
##                             PWD COMPLEX CHANGLANG 
##                                               316 
##     PWD DIVISION - IV OFFICE COMPLEX / SENKI PARK 
##                                              1412 
##                                            QUIBOM 
##                                                85 
##                                            QUYING 
##                                               384 
##                              R.K. MISSION COMPLEX 
##                                               991 
##                                        RACH TABIO 
##                                               438 
##                                         RACHI - I 
##                                               255 
##                                            RADENG 
##                                               532 
##                                       RAGA HQ - I 
##                                               740 
##                                      RAGA HQ - II 
##                                               486 
##                                  RAGIDOKE VILLAGE 
##                                               468 
##                                              RAGO 
##                                               454 
##                                              RAHA 
##                                               707 
##                                      RAHO VILLAGE 
##                                               356 
##                                            RAHUNG 
##                                               238 
##                                           RAIBALO 
##                                              1028 
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
##                                               334 
##                                         RAMA CAMP 
##                                               359 
##                                        RAMALINGOM 
##                                               186 
##                                             RAMDA 
##                                                89 
##                                           RAMGHAT 
##                                               680 
##                                          RAMNAGAR 
##                                               208 
##                                           RAMSING 
##                                               782 
##                                          RANAGHAT 
##                                              1400 
##                                     RANAGHAT CAMP 
##                                                21 
##                                              RANG 
##                                               202 
##                                          RANGHILL 
##                                                55 
##                                           RANGLUA 
##                                              1290 
##                                           RANGLUM 
##                                               150 
##                                       RANGRINGKAN 
##                                               498 
##                                      RANGTHANGJOR 
##                                               210 
##                                              RANI 
##                                               890 
##                                        RANI (S/W) 
##                                               454 
##                                           RANKATU 
##                                               355 
##                                  RANLAMRI VILLAGE 
##                                                61 
##                                             RANLI 
##                                                51 
##                                             RAPUM 
##                                               378 
##                                            RAPUNG 
##                                               117 
##                                     RARISH SOLUNG 
##                                               110 
##                              RATAK GAMLIN VILLAGE 
##                                               318 
##                                              RATE 
##                                               328 
##                                              RAWA 
##                                               217 
##                                            RAYANG 
##                                               702 
##                                            RAYING 
##                                               695 
##                                    RAYUK (SOLUNG) 
##                                                42 
##                                              REBE 
##                                               576 
##                                              REBI 
##                                               170 
##                                           REDDING 
##                                               190 
##                                             REDDY 
##                                               148 
##                                      REGI VILLAGE 
##                                               492 
##                                              REGO 
##                                               151 
##                                         RELANGKAN 
##                                                73 
##                                            RELUNG 
##                                               188 
##                                              REMI 
##                                               236 
##                                           RENGCHI 
##                                               826 
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
##                                              1058 
##                                        RESTARIANG 
##                                               436 
##                                               RHO 
##                                               304 
##                                             RIAGA 
##                                               808 
##                                            RICHIK 
##                                              1322 
##                                 RICHIRITE VILLAGE 
##                                                24 
##                                RIEW VILLAGE (N/W) 
##                                               752 
##                                RIEW VILLAGE (S/W) 
##                                               363 
##                                           RIGA HQ 
##                                               176 
##                          RIGA MOBUK VILLAGE (N/W) 
##                                               406 
##                          RIGA MOBUK VILLAGE (S/W) 
##                                               770 
##                                       RIGA MONGKU 
##                                               648 
##                                        RIGA SIRAM 
##                                               484 
##                                             RIGIA 
##                                               582 
##                                              RIGO 
##                                               904 
##                                    RIGONG VILLAGE 
##                                                71 
##                                             RIGYU 
##                                              1034 
##                                           RIKHUNG 
##                                               117 
##                                              RIKO 
##                                               248 
##                                            RIKUNG 
##                                               108 
##                                            RILLOH 
##                                               992 
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
##                                               392 
##                                             RISSI 
##                                               714 
##                                              RITE 
##                                               658 
##                                            RIYANG 
##                                               372 
##                                          ROILIANG 
##                                               128 
##                                             ROING 
##                                               824 
##                                              ROJI 
##                                               229 
##                                              ROJO 
##                                               175 
##                                              ROSE 
##                                               828 
##                                             ROTTE 
##                                               237 
##                                   ROTTUNG VILLAGE 
##                                               226 
##                                       ROW VILLAGE 
##                                                64 
##                                       ROWTA RANGE 
##                                                22 
##                                              RUBA 
##                                               306 
##                                              RUHI 
##                                              1886 
##                                             RUKMO 
##                                               118 
##                                       RUKSIN TOWN 
##                                              1070 
##                                    RUKSIN VILLAGE 
##                                               876 
##                                   RUMGONG VILLAGE 
##                                              1442 
##                                             RUMTE 
##                                               480 
##                                            RUNGBA 
##                                               712 
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
##                                              1266 
##                                           SACHIDA 
##                                               108 
##                                           SACHING 
##                                               304 
##                                           SACHUNG 
##                                               148 
##                                            SADDLE 
##                                               266 
##                                  SAGALEE TOWNSHIP 
##                                              1280 
##                                             SAGAR 
##                                               137 
##                                      SAGO VILLAGE 
##                                               453 
##                                             SAIMU 
##                                               998 
##                                           SAKIANG 
##                                               443 
##                                           SAKPRET 
##                                               158 
##                                            SAKRIN 
##                                               224 
##                                              SAKU 
##                                               194 
##                                            SAKYUR 
##                                               225 
##                                            SALARI 
##                                               339 
##                                          SAMDRUNG 
##                                               168 
##                                          SAMPHUNG 
##                                               244 
##                                   SAMPONG VILLAGE 
##                                               350 
##                                         SANCHIPAM 
##                                                57 
##                                            SANCHU 
##                                               221 
##                                    SANGBA KORSANG 
##                                               524 
##                                           SANGBIA 
##                                               217 
##                                             SANGO 
##                                              1102 
##                                         SANGO - I 
##                                               226 
##                                           SANGRAM 
##                                               422 
##                                  SANGRAM TOWNSHIP 
##                                               742 
##                                        SANGSATHAM 
##                                               212 
##                                            SANGTI 
##                                               602 
##                           SANGTI (BISHUM) PHUDUNG 
##                                               616 
##                                   SANGWAL VILLAGE 
##                                                95 
##                                   SANLIAM VILLAGE 
##                                               194 
##                                              SAPE 
##                                               194 
##                                       SAPPER CAMP 
##                                               376 
##                                       SARCH - GAI 
##                                               277 
##                                SARI LIKAR VILLAGE 
##                                               203 
##                                             SARIO 
##                                               194 
##                                        SARLI TOWN 
##                                               491 
##                                             SARTA 
##                                               264 
##                                             SARTI 
##                                                48 
##                                             SASUM 
##                                               117 
##                                            SATANG 
##                                               114 
##                                     SAW MILL AREA 
##                                               984 
##                                              SAWA 
##                                               156 
##                                              SAZO 
##                                               432 
##                                              SEBA 
##                                               333 
##                                            SEBING 
##                                               156 
##                      SEC.SCHOOL LINE MAYU - II(A) 
##                                              1150 
##                                              SEDE 
##                                               634 
##                                         SEEMA - I 
##                                               221 
##                                              SEER 
##                                               209 
##                                          SEKHJARA 
##                                               272 
##                                            SEKONG 
##                                               520 
##                                            SEMNAK 
##                                                72 
##                                       SENGAPATHER 
##                                               676 
##                                             SENGE 
##                                               434 
##                                        SENGRIDOLO 
##                                               287 
##                                         SENGRIKWA 
##                                               233 
##                                          SENGRING 
##                                               106 
##                                        SENKI VIEW 
##                                              1208 
##                                        SENUA CAMP 
##                                                68 
##                               SENUA NOKSA VILLAGE 
##                                               154 
##                                   SENUA VILL. - I 
##                                               973 
##                                    SEPENG VILLAGE 
##                                               116 
##                        SEPPA TOWNSHIP - IV COLONY 
##                                               928 
##                           SEPPA TYPE - III COLONY 
##                                               731 
##                                              SERA 
##                                              1602 
##                                       SERAM VILL. 
##                                               548 
##                                 SERE TALI VILLAGE 
##                                               238 
##                                             SEREN 
##                                              1100 
##                                           SERIANG 
##                                               408 
##                                           SERJONG 
##                                               606 
##                                             SESSA 
##                                               182 
##                               SESSI LIKAR VILLAGE 
##                                               259 
##                                       SEY - GODAK 
##                                               264 
##                                              SEYA 
##                                               602 
##                                            SHAKTI 
##                                               398 
##                                            SHARMA 
##                                               210 
##                                  SHERBANG / YABAB 
##                                               350 
##                                          SHERGAON 
##                                               692 
##                                           SHIRONG 
##                                               236 
##                                            SHYARO 
##                                               440 
##                                              SHYO 
##                                               788 
##                                      SIBE VILLAGE 
##                                              2364 
##                                  SIBERITE VILLAGE 
##                                               458 
##                                         SIBUM - I 
##                                               496 
##                                        SIBUM - II 
##                                               299 
##                                             SIBUT 
##                                               600 
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
##                                               222 
##                                      SIKA - BAMIN 
##                                              1060 
##                                         SIKA TODE 
##                                               465 
##                                             SIKAO 
##                                               526 
##                                          SIKARIJO 
##                                               479 
##                                             SIKOM 
##                                                86 
##                                         SIL SANGO 
##                                               874 
##                                            SILIPU 
##                                                33 
##                                             SILLA 
##                                               173 
##                                     SILLE VILLAGE 
##                                              1440 
##                                             SILLI 
##                                               251 
##                                     SILLI VILLAGE 
##                                               808 
##                                    SILLUK VILLAGE 
##                                               583 
##                                            SIMONG 
##                                               737 
##                                          SIMUGONG 
##                                               240 
##                                            SINDAK 
##                                               107 
##                                      SINE VILLAGE 
##                                               325 
##                                           SINGBIR 
##                                               790 
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
##                                               693 
##                                       SIPU COLONY 
##                                              1570 
##                                            SIRANG 
##                                               174 
##                                              SIRO 
##                                              1194 
##                                         SIRU RIJO 
##                                               236 
##                                      SIRU VILLAGE 
##                                               214 
##                                     SIRUM VILLAGE 
##                                               228 
##                                  SIRUTALI VILLAGE 
##                                               194 
##                                    SISSEN VILLAGE 
##                                               260 
##                                    SITANG VILLAGE 
##                                               395 
##                                    SITAPANI MORAN 
##                                              1928 
##                                              SITO 
##                                               453 
##                                      SITPANI MIRI 
##                                               840 
##                                        SIYUM H.Q. 
##                                                72 
##                                             SIZER 
##                                               380 
##                                        SOBLALIANG 
##                                                36 
##                                          SOCKTSEN 
##                                               237 
##                                  SODODOKE VILLAGE 
##                                               155 
##                                            SODRIK 
##                                               370 
##                                     SOGUM VILLAGE 
##                                              1080 
##                                      SOHA VILLAGE 
##                                              1078 
##                                      SOHE LAKTONG 
##                                               248 
##                                       SOI VILLAGE 
##                                               218 
##                                              SOKI 
##                                               304 
##                                         SOLUNGTOO 
##                                               438 
##                                          SOMPOI-I 
##                                              1640 
##                                      SONGKHU HAVI 
##                                               222 
##                                             SONGO 
##                                               237 
##                                    SUBANG VILLAGE 
##                                               128 
##                                              SUBU 
##                                               622 
##                                            SUMLAM 
##                                               194 
##                                           SUMSING 
##                                               660 
##                              SUMSIPATHER VILLEAGE 
##                                               210 
##                                           SUNPURA 
##                                               718 
##                                           SUPLANG 
##                                               480 
##                                   SUPSING VILLAGE 
##                                               274 
##                                             SURBI 
##                                               194 
##                                            SURBIN 
##                                                28 
##                                        SWAMI CAMP 
##                                               322 
##                                              TABA 
##                                               810 
##                                          TABASORA 
##                                               484 
##                                             TABIO 
##                                               139 
##                                          TABIRIPO 
##                                               155 
##                                          TABITALL 
##                                               638 
##                                           TABOMNA 
##                                               167 
##                                             TABRI 
##                                               164 
##                                             TADIN 
##                                              1190 
##                                          TAFLAGAM 
##                                               324 
##                                          TAFRAGAM 
##                                               744 
##                                        TAFRALIANG 
##                                               264 
##                                           TAGAMPU 
##                                               174 
##                                    TAGANG WARRANG 
##                                               908 
##                                              TAGO 
##                                               203 
##                                            TAGOGI 
##                                               108 
##                                              TAHU 
##                                               656 
##                                               TAI 
##                                               334 
##                                       TAI VILLAGE 
##                                               301 
##                                            TAJANG 
##                                              1538 
##                                             TAJGI 
##                                               618 
##                                        TAJILANGPO 
##                                               254 
##                                      TAJO VILLAGE 
##                                               436 
##                                         TAKAMPASA 
##                                               252 
##                                       TAKEMPURING 
##                                               764 
##                                        TAKILALUNG 
##                                               591 
##                                     TAKOM VILLAGE 
##                                               238 
##                                           TAKSANG 
##                                               101 
##                                      TAKSING H.Q. 
##                                               173 
##                                     TAKSO VILLAGE 
##                                               244 
##                                         TALI H.Q. 
##                                              1486 
##                                   TALIHA H.Q. (N) 
##                                               312 
##                                   TALIHA H.Q. (S) 
##                                               273 
##                                             TALLO 
##                                               468 
##                                        TALLOMSIMA 
##                                               237 
##                                       TALLONG - I 
##                                               636 
##                                              TALO 
##                                               424 
##                                         TAMIN - I 
##                                               412 
##                                        TAMIN - II 
##                                               369 
##                                            TAMNEY 
##                                               276 
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
##                                               578 
##                                              TAPI 
##                                               260 
##                                   TAPIYOR VILLAGE 
##                                               320 
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
##                                               458 
##                                             TARBA 
##                                               119 
##                                     TAROWA YANGFO 
##                                               480 
##                                           TAROYAR 
##                                               195 
##                                         TASHIGAON 
##                                               182 
##                                          TASIDONI 
##                                               806 
##                                          TASIRING 
##                                                99 
##                                            TASSAR 
##                                               474 
##                                        TASSOMLORA 
##                                               267 
##                                  TATAMORI VILLAGE 
##                                               300 
##                                          TATATARA 
##                                               174 
##                                          TATO H.Q 
##                                               330 
##                                      TATO VILLAGE 
##                                               379 
##                                      TAWANG GOMPA 
##                                               444 
##                                              TAWE 
##                                               426 
##                                              TAYA 
##                                               344 
##                                            TAYENG 
##                                               428 
##                                             TAYOM 
##                                               183 
##                                            TEDUNG 
##                                               280 
##                                         TEEN KILO 
##                                               608 
##                               TEGO GAMLIN VILLAGE 
##                                               462 
##                                            TEKANG 
##                                               740 
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
##                                               214 
##                                        TENZINGAON 
##                                                40 
##                           TEZU TOWNSHIP BLOCK - I 
##                                               893 
##                         TEZU TOWNSHIP BLOCK - III 
##                                              1269 
##                          TEZU TOWNSHIP BLOCK - IV 
##                                              2590 
##                           TEZU TOWNSHIP BLOCK - V 
##                                               893 
##                          TEZU TOWNSHIP BLOCK - VI 
##                                              1871 
##                         TEZU TOWNSHIP BLOCK - VII 
##                                              1636 
##                                           TEZUGAM 
##                                                44 
##                                            THALLA 
##                                                42 
##                                         THAMIYANG 
##                                               238 
##                                           THAMLOM 
##                                               141 
##                                         THAMPTONG 
##                                               140 
##                                       THARGELLING 
##                                               140 
##                                          THEMBANG 
##                                               340 
##                                            THESSA 
##                                               196 
##                                           THIKSHI 
##                                                43 
##                                      THINGBU H.Q. 
##                                               304 
##                                    THINSA VILLAGE 
##                                              1198 
##                                         THONGLENG 
##                                               736 
##                                   THONGTHUNG HAVI 
##                                               130 
##                                          THRILLAM 
##                                               249 
##                                          THRIZINO 
##                                               819 
##                                 THUNGJONG VILLAGE 
##                                               312 
##                                          THUNGREE 
##                                               570 
##                                      TIGRA MIRBUK 
##                                               785 
##                                             TIKDO 
##                                              1100 
##                                   TIKHAK KHAMLANG 
##                                               198 
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
##                                               250 
##                                             TINAI 
##                                               240 
##                                             TIPPI 
##                                               607 
##                                TIRBIN TOWN (SIRU) 
##                                               245 
##                                      TIRI VILLAGE 
##                                                94 
##                                        TISSA CAMP 
##                                               576 
##                                            TISSUE 
##                                               284 
##                                            TITRIT 
##                                               231 
##                                              TODE 
##                                               408 
##                                            TONGMA 
##                                               125 
##                                              TOON 
##                                               391 
##                                   TORAJAN VILLAGE 
##                                               624 
##                                              TORU 
##                                               468 
##                                         TOTPU - I 
##                                               504 
##                                         TOWN BILL 
##                                               968 
##                         TRANSPORT / H.S.S. COLONY 
##                                               760 
##                                    TRANSPORT AREA 
##                                               779 
##                                  TRANSPORT COLONY 
##                                               370 
##                                       TSERING PAM 
##                                               212 
##                                            TULUHI 
##                                               222 
##                                    TUMBIN VILLAGE 
##                                               238 
##                                           TUMLANG 
##                                               904 
##                                             TUNGI 
##                                               103 
##                                           TUNGMAR 
##                                               588 
##                                     TURET VILLAGE 
##                                               524 
##                                  TUTING PANIKHETI 
##                                               512 
##                                       TUTING TOWN 
##                                              1922 
##                                    TUTNYU VILLAGE 
##                                               728 
##                                         TUWILIANG 
##                                               123 
##                                           TWO HUT 
##                                               651 
##                        TYPE - I COLONY (PART - I) 
##                                               376 
##                       TYPE - I COLONY (PART - II) 
##                                              1244 
##                      TYPE - II COLONY & SHANTIPUR 
##                                               718 
##                                          TYPE - V 
##                                              1340 
##                                               ULI 
##                                               241 
##                      UPPER BHALUKPONG(NORTH WING) 
##                                              1030 
##                      UPPER BHALUKPONG(SOUTH WING) 
##                                              1222 
##                             UPPER BORAJAN VILLAGE 
##                                               506 
##                             UPPER COLONY PART - I 
##                                               480 
##                            UPPER COLONY PART - II 
##                                               810 
##                                       UPPER DZONG 
##                                               280 
##                                         UPPER GAI 
##                                               312 
##                                       UPPER HINDA 
##                                               747 
##                                        UPPER JUMI 
##                                               814 
##                               UPPER KOLAM VILLAGE 
##                                               964 
##                                       UPPER LEYAK 
##                                               337 
##                                     UPPER LICHILA 
##                                               365 
##                                    UPPER LIKABALI 
##                                               570 
##                                UPPER MIAO (NORTH) 
##                                               417 
##                                UPPER MIAO (SOUTH) 
##                                              1660 
##                                     UPPER MILLANG 
##                                               260 
##                                  UPPER MUDOI DEEP 
##                                                80 
##                             UPPER NYAPIN TOWNSHIP 
##                                              1070 
##                                        UPPER ROWA 
##                                               616 
##                                     UPPER SEIJOSA 
##                                               846 
##                                     UPPER SILATOO 
##                                               348 
##                                      UPPER TARASO 
##                                               685 
##                              UPPERCHINHAN VILLAGE 
##                                               148 
##                                         URGELLING 
##                                               572 
##                                               VEO 
##                                              1102 
##                                 VETERINARY COLONY 
##                                               453 
##                       VETERINARY LINE MAYU - I(A) 
##                                               938 
##                 VETERINARY OFFICE COMPLEX EASTERN 
##                                              1960 
##                     VETTY. OFFICE COMPLEX WESTERN 
##                                               828 
##                    VETTY. OFFICE COPLEX EAST SIDE 
##                                              1330 
##                   VETTY. OFFICE COPLEX SOUTH SIDE 
##                                               770 
##                               VIJAYNAGAR (HAZOLO) 
##                                               801 
##                                     VOTNU VILLAGE 
##                                               870 
##                                             WABIA 
##                                               468 
##                                       WADA BAGANG 
##                                               334 
##                                            WAFANG 
##                                                45 
##                                  WAGON PATHAR - I 
##                                              1122 
##                                          WAGUN-II 
##                                               413 
##                                     WAGUN PONTHAI 
##                                               920 
##                                              WAII 
##                                               908 
##                                       WAK (RAGYI) 
##                                               279 
##                                          WAKHETNA 
##                                               606 
##                                   WAKKA TOWN H.Q. 
##                                               370 
##                                 WAKKA VILLAGE - I 
##                                               950 
##                                WAKKA VILLAGE - II 
##                                               760 
##                                             WAKKE 
##                                               160 
##                                        WAKRO TOWN 
##                                              1850 
##                                            WALONG 
##                                               270 
##                                           WANGHOO 
##                                               522 
##                                             WANLI 
##                                                27 
##                                              WANU 
##                                               818 
##                                           WARJUNG 
##                                               207 
##                                        WARRANGPAM 
##                                                93 
##                                 WASATHONG VILLAGE 
##                                               564 
##                                       WATHIN VILL 
##                                               364 
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
##                                               380 
##                                    WOWOI (SUBBAN) 
##                                               290 
##                                              XXXX 
##                                               510 
##                                              YABA 
##                                               598 
##                                      YABHI (D / H 
##                                               588 
##                                           YACHUGI 
##                                               592 
##                                           YACHULI 
##                                               593 
##                                           YAGLUNG 
##                                               664 
##                                           YAGRUNG 
##                                               625 
##                                             YAKHA 
##                                               520 
##                                         YAKI TATO 
##                                               832 
##                                             YAKLI 
##                                               158 
##                                            YAKUNG 
##                                                90 
##                                            YANGFO 
##                                              1050 
##                                           YANGSEY 
##                                               295 
##                                            YANGTE 
##                                              1158 
##                                           YANKANG 
##                                               200 
##                                            YANMAN 
##                                               381 
##                                             YAPHA 
##                                               254 
##                                             YAPIK 
##                                               300 
##                                             YARBA 
##                                               337 
##                                        YARTEPOUBE 
##                                               226 
##                                            YASONG 
##                                               131 
##                                            YATONG 
##                                               616 
##                                            YATTAP 
##                                               896 
##                                            YAYUNG 
##                                               264 
##                                            YAZALI 
##                                              1576 
##                                          YEALIANG 
##                                               559 
##                                     YEGRI VILLAGE 
##                                               512 
##                                    YEKSHI VILLAGE 
##                                               238 
##                                   YEMSING VILLAGE 
##                                               453 
##                                            YEWANG 
##                                              1510 
##                                             YIBUK 
##                                               504 
##                                     YIBUK VILLAGE 
##                                               273 
##                                      YIGA VILLAGE 
##                                               198 
##                                         YIGI KAUM 
##                                               640 
##                                    YINGKU VILLAGE 
##                                               462 
##                                YIO (MOLO) VILLAGE 
##                                                77 
##                                       YIO VILLAGE 
##                                               100 
##                                             YOGLU 
##                                               630 
##                                    YOGONG VILLAGE 
##                                               340 
##                                            YOIZAT 
##                                               436 
##               YOJI - YORA / ITBP AREA / K.V. AREA 
##                                               752 
##                                               YOM 
##                                               348 
##                                            YOMCHA 
##                                               658 
##                                             YOMDO 
##                                               530 
##                                    YOMGAM VILLAGE 
##                                               514 
##                                             YORDA 
##                                               800 
##                                             YORDO 
##                                               428 
##                                            YORKUM 
##                                               314 
##                                             YORNI 
##                                               372 
##                                           YORTUNG 
##                                               152 
##                                    YOSING VILLAGE 
##                                               135 
##                                            YOURON 
##                                                33 
##                                              YUBA 
##                                               426 
##                                             YUDIK 
##                                               137 
##                                             YUKER 
##                                               212 
##                                       YULONGRIPAM 
##                                               130 
##                                            YUMLAM 
##                                               513 
##                                          YUTHEMBU 
##                                               669 
##                                         ZAPALIANG 
##                                                82 
##                                              ZARA 
##                                               884 
##                                     ZEDUA VILLAGE 
##                                              1174 
##                                     ZEMITHANG H.Q 
##                                               202 
##                                     ZIDO (POKBIR) 
##                                               418 
##                                          ZIMTHUNG 
##                                               269 
##                                        ZINGMURING 
##                                               237 
##                                     ZIRDO VILLAGE 
##                                               588 
##                                              ZONG 
##                                                85 
##                                           ZONGSAM 
##                                               105 
##                               ZOO ROAD, ROING - I 
##                                              1070
```
