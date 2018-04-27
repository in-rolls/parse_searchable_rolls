## Meghalaya

Basic descriptive statistics about the data. And sanity checks.


```r
meghalaya <- readr::read_csv("meghalaya.csv")
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
nrow(meghalaya)
```

```
## [1] 1735469
```

Unique Values in Sex:


```r
# Unique values in sex
table(meghalaya$sex)
```

```
## 
## Female   Male 
## 876444 859025
```

Summary of Age:


```r
# Age
summary(meghalaya$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##   19.00   26.00   34.00   37.55   46.00  116.00       1
```

Check if 0 and missing age is from problem in the electoral roll:


```r
meghalaya[which(meghalaya$age == 1), c("id", "filename")]
```

```
## # A tibble: 0 x 2
## # ... with 2 variables: id <chr>, filename <chr>
```

No. of characters in ID:

```r
# Length of ID
table(nchar(meghalaya$id))
```

```
## 
##       9      10      11      16 
##       1 1735284       1       3
```

Number of characters in pin code:


```r
table(nchar(meghalaya$pin_code))
```

```
## 
##       6 
## 1725764
```

Are IDs duplicated?


```r
length(unique(meghalaya$id))
```

```
## [1] 1733904
```

```r
nrow(meghalaya)
```

```
## [1] 1735469
```


```r
# Net electors
sum(with(meghalaya, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 1734874
```

```r
nrow(meghalaya)
```

```
## [1] 1735469
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(meghalaya$elector_name))
```

```
## 
##      4      5      6      7      8      9     10     11     12     13 
##      1     24    123   1090   7599  26591  62204 128771 195950 234148 
##     14     15     16     17     18     19     20     21     22     23 
## 227996 205793 179324 145341 107418  74007  48677  31930  20682  13222 
##     24     25     26     27     28     29     30     31     32     33 
##   8465   5718   3816   2479   1640    982    562    381    212    131 
##     34     35     36     37     38     39     40     41     42     43 
##     75     44     28     18     13      3      4      3      3      1
```

```r
meghalaya[which(nchar(meghalaya$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 0 x 2
## # ... with 2 variables: id <chr>, filename <chr>
```

Does district have a number?

```r
sum(grepl('[0-9]', meghalaya$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(meghalaya$parl_constituency)
```

```
## 
##         1 - NARTIANG (ST)         1 - SHILLONG (ST) 
##                     34752                     86523 
##          10 - JIRANG (ST)         11 - UMSNING (ST) 
##                     34620                     30331 
##           12 - UMROI (ST)    13 - MAWRYNGKNENG (ST) 
##                     24980                     30586 
##          15 - MAWLAI (ST)  17 - NORTH SHILLONG (ST) 
##                     41547                     26352 
##            2 - JOWAI (ST)             2 - TURA (ST) 
##                     33138                     53301 
##         20 - MYLLIEM (ST)     21 - NONGTHYMMAI (ST) 
##                     30887                     33227 
##        22 - NONGKREM (ST)         23 - SOHIONG (ST) 
##                     31078                     27196 
##       24 - MAWPHLANG (ST)       25 - MAWSYNRAM (ST) 
##                     28156                     30178 
##          26 - SHELLA (ST)        27 - PYNURSLA (ST) 
##                     26493                     31685 
##           28 - SOHRA (ST)       29 - MAWKYNREW (ST) 
##                     24092                     29781 
##          3 - RALIANG (ST)         30 - MAIRANG (ST) 
##                     30738                     33410 
##  31 - MAWTHADRAISHAN (ST)       32 - NONGSTOIN (ST) 
##                     33978                     31512 
## 33 - RAMBRAI JYRNGAM (ST)      34 - MAWSHYNRUT (ST) 
##                     30848                     31987 
##         35 - RANIKOR (ST)       36 - MAWKYRWAT (ST) 
##                     28095                     29073 
##       37 - KHARKUTTA (ST)     38 - MENDIPATHAR (ST) 
##                     35714                     24267 
##     39 - RESUBELPARA (ST)         4 - MOWKAIAW (ST) 
##                     25081                     29378 
##      40 - BAJENGDOBA (ST)         41 - SONGSAK (ST) 
##                     27946                     25242 
##        42 - RONGJENG (ST)   43 - WILLIAM NAGAR (ST) 
##                     28364                     31184 
##       44 - RAKSAMGRE (ST)      45 - TIKRIKILLA (ST) 
##                     25767                     29546 
##        48 - SELSELLA (ST)       49 - DADENGGRE (ST) 
##                     29159                     28969 
##   5 - SUTNGA SAIPUNG (ST)      50 - NORTH TURA (ST) 
##                     36423                     28783 
##      51 - SOUTH TURA (ST)      52 - RANGSAKONA (ST) 
##                     29122                     30202 
##          53 - AMPATI (ST)    54 - MAHENDRAGANJ (ST) 
##                     27283                     29867 
##      55 - SALMANPARA (ST)        56 - GAMBEGRE (ST) 
##                     25179                     24536 
##            57 - DALU (ST)    58 - RONGARA SIJU (ST) 
##                     17892                     27882 
##         59 - CHOKPOT (ST)       6 - KHLIEHRIAT (ST) 
##                     25921                     36776 
##        60 - BAGHMARA (ST)          7 - AMLAREM (ST) 
##                     25817                     30542 
##          8 - MAWHATI (ST)          9 - NONGPOH (ST) 
##                     30711                     29372
```

```r
table(meghalaya$ac_name)
```

```
## 
##             1 - NARTIANG (ST)              10 - JIRANG (ST) 
##                         34752                         34620 
##             11 - UMSNING (ST)               12 - UMROI (ST) 
##                         30331                         24980 
##        13 - MAWRYNGKNENG (ST) 14 - PYNTHORUMKHRAH (General) 
##                         30586                         30068 
##              15 - MAWLAI (ST)      17 - NORTH SHILLONG (ST) 
##                         41547                         26352 
##  18 - WEST SHILLONG (General) 19 - SOUTH SHILLONG (General) 
##                         25351                         31104 
##                2 - JOWAI (ST)             20 - MYLLIEM (ST) 
##                         33138                         30887 
##         21 - NONGTHYMMAI (ST)            22 - NONGKREM (ST) 
##                         33227                         31078 
##             23 - SOHIONG (ST)           24 - MAWPHLANG (ST) 
##                         27196                         28156 
##           25 - MAWSYNRAM (ST)              26 - SHELLA (ST) 
##                         30178                         26493 
##            27 - PYNURSLA (ST)               28 - SOHRA (ST) 
##                         31685                         24092 
##           29 - MAWKYNREW (ST)              3 - RALIANG (ST) 
##                         29781                         30738 
##             30 - MAIRANG (ST)      31 - MAWTHADRAISHAN (ST) 
##                         33410                         33978 
##           32 - NONGSTOIN (ST)     33 - RAMBRAI JYRNGAM (ST) 
##                         31512                         30848 
##          34 - MAWSHYNRUT (ST)             35 - RANIKOR (ST) 
##                         31987                         28095 
##           36 - MAWKYRWAT (ST)           37 - KHARKUTTA (ST) 
##                         29073                         35714 
##         38 - MENDIPATHAR (ST)         39 - RESUBELPARA (ST) 
##                         24267                         25081 
##             4 - MOWKAIAW (ST)          40 - BAJENGDOBA (ST) 
##                         29378                         27946 
##             41 - SONGSAK (ST)            42 - RONGJENG (ST) 
##                         25242                         28364 
##       43 - WILLIAM NAGAR (ST)           44 - RAKSAMGRE (ST) 
##                         31184                         25767 
##          45 - TIKRIKILLA (ST)       46 - PHULBARI (General) 
##                         29546                         25211 
##       47 - RAJABALA (General)            48 - SELSELLA (ST) 
##                         28090                         29159 
##           49 - DADENGGRE (ST)       5 - SUTNGA SAIPUNG (ST) 
##                         28969                         36423 
##          50 - NORTH TURA (ST)          51 - SOUTH TURA (ST) 
##                         28783                         29122 
##          52 - RANGSAKONA (ST)              53 - AMPATI (ST) 
##                         30202                         27283 
##        54 - MAHENDRAGANJ (ST)          55 - SALMANPARA (ST) 
##                         29867                         25179 
##            56 - GAMBEGRE (ST)                57 - DALU (ST) 
##                         24536                         17892 
##        58 - RONGARA SIJU (ST)             59 - CHOKPOT (ST) 
##                         27882                         25921 
##           6 - KHLIEHRIAT (ST)            60 - BAGHMARA (ST) 
##                         36776                         25817 
##              7 - AMLAREM (ST)              8 - MAWHATI (ST) 
##                         30542                         30711 
##              9 - NONGPOH (ST) 
##                         29372
```

```r
table(meghalaya$police_station)
```

```
## 
##            ACHOTCHONGGRE       AKAROK SONGGITCHAM                   AMPATI 
##                      545                      999                    30229 
##                  ANE AGA                 ARUAKGRE                 BAGHMARA 
##                      403                      452                    27021 
##                BAJENGDOB               BAJENGDOBA          BAKENANG SONGMA 
##                      686                     2310                      809 
##                  BALMURI                BEKBEKGRE        BOLSONG (B) MOHOL 
##                      406                      802                      882 
##           BOLSONG SONGMA                 CHAKODAM           CHISIM AKANANG 
##                      456                      796                      764 
##                  CHOKPOT                DADENGGRE               DAJONGPARA 
##                    20648                    12855                      826 
##            DALBOT SONGMA                     DALU                    DAWKI 
##                      602                    34547                    13397 
##             DENGGNANGGRE                 DINGREPA             GABIL SONGMA 
##                      729                      403                      999 
##                GASUAPARA                 GOKOLGRE               GOSINGPITA 
##                    13982                      794                      680 
##          GRA SONGGITCHAM                    JOWAI                KAGRAKGRE 
##                      417                   145151                      764 
## KHANAPARA POLICE STATION               KHLIEHRIAT                 KIMDEGRE 
##                    41999                    58076                      473 
##                 KOREPARA                LABAN P.S         LAITUMKHRAH P.S. 
##                      784                    84619                     3830 
##               LINE ADING           LOWER SUALMARI          LUMDIENGJRI P.S 
##                      556                      980                    63764 
##          MADANRITING P.S             MAHENDRAGANJ                  MAIRANG 
##                    81470                    40419                    52860 
##                MAODAMGRE                MAWKYRWAT               MAWLAI P.S 
##                      612                    28452                    41435 
##             MAWNGAP P.S.            MAWSYNRAM P.S               MENDAL (A) 
##                    12984                    20838                      642 
##               MENDAL (B)              MENDIPATHAR              NONGALBIBRA 
##                      550                    83348                     6708 
##   NONGPOH POLICE STATION                NONGSTOIN                  OMORPUR 
##                    65669                   108875                      660 
##                 PHULBARI             PYNURSLA P.S            RAKSAM GENANG 
##                    81950                    40623                      734 
##                  RANIKOR               RARI BAZAR            REM SONGGITAL 
##                    22426                      988                      551 
##              RESUBELPARA                  RONGARA               RONGGOPGRE 
##                     1143                    10850                      827 
##                 RONGJENG               RYNJAH P.S                  SAIPUNG 
##                    28364                    48960                    15123 
##               SALMANPARA              SAMKALAKGRE           SHILLONG SADAR 
##                     3707                      936                    33968 
##               SOHRA P.S.                  SONGSAK               TIKRIKILLA 
##                    43677                    25242                    71427 
##         TORIKKAKONA GARO                     TURA     UMIAM POLICE STATION 
##                      957                   103962                    42060 
##            WAKSO ACHUGRE             WAKSO NENGSA             WILLIAMNAGAR 
##                      385                      763                    31184
```

```r
table(meghalaya$mandal)
```

```
## < table of extent 0 >
```

```r
table(meghalaya$district)
```

```
## 
##                   BRIDGE                 CEMETERY                  CHOKPOT 
##                     1559                      708                      379 
##                   COLONY                     DUBA          EAST GARO HILLS 
##                      412                      533                    84790 
##       EAST JAINTIA HILLS         EAST KHASI HILLS                    HOUSE 
##                    73199                   468232                     1015 
## KHANAPARA POLICE STATION              LUMMARALONG                   MAWBRI 
##                    40759                      605                      500 
##   NONGPOH POLICE STATION       NONGTHYMMAI KYRDEM    NONGTHYMMAI MAIN ROAD 
##                    63780                      454                      888 
##         NORTH GARO HILLS               OPERA HALL              PAHAMLAPONG 
##                   113008                     1380                      405 
##                  PATARIM                     ROAD        SIDE OF LAWSOHTUN 
##                      757                     1932                      978 
##         SOUTH GARO HILLS    SOUTH WEST GARO HILLS   SOUTH WEST KHASI HILLS 
##                    79241                    82329                    57168 
##          TOMONPO ANGLONG     UMIAM POLICE STATION                UMLANGPUR 
##                      344                    41106                      279 
##            UMPOWIN PDENG       UMSNING PROPER A A             WATCH CORNER 
##                      428                      383                     1089 
##          WEST GARO HILLS       WEST JAINTIA HILLS         WEST KHASI HILLS 
##                   297277                   158136                   161130 
##                     XXXX 
##                      286
```

```r
table(meghalaya$main_town)
```

```
## 
##                       18TH MILE                      20TH. MILE 
##                             440                             832 
##    3RD HALF MILE UPPER SHILLONG         4TH MILE UPPER SHILLONG 
##                             906                             901 
##         5TH MILE UPPER SHILLONG             6TH MILE GOVT. FARM 
##                            1079                             296 
##                           ABIMA                     AGILLANGGRE 
##                             799                             999 
##                       AGRONGGRE                        AGURAGRE 
##                             364                             485 
##                      AIGRE APAL                       ALLEKPARA 
##                             831                             813 
##                 ALOKPANG BULAWE                  AMINDA SIMSANG 
##                             287                             654 
##                    AMJAJER ROKO                        AMJALONG 
##                              89                             296 
##                           AMJOK                          AMJONG 
##                             563                             388 
##                 AMKHLOO PAMTBUH                           AMKOI 
##                             507                             380 
##                         AMLANAI                         AMLAREM 
##                             315                             782 
##                    AMLARI MODEL                      AMLYMPIANG 
##                             324                             103 
##                        AMMUTONG                        AMONGGRE 
##                             558                             751 
##                       AMPANGGRE                          AMPATI 
##                            1735                             999 
##                          AMPHER                        AMPHRENG 
##                             935                             343 
##                           AMSKU                      AMSOHRHONG 
##                             163                             159 
##                         AMTAPOH             ANANGPARA CHRISTIAN 
##                             252                             869 
##                  ANCHENGGRE - B                    ANGALLANGGRE 
##                             214                             447 
##                ANGKE RONGDIKGRE                          ANOGRE 
##                             386                             577 
##                         APALGRE                      ASANANGGRE 
##                             354                             438 
##                          ASIGRE                  ASIL SONGGITAL 
##                             530                             420 
##                         ASIMGRE                       ASKIKANDI 
##                             721                            1627 
##                          ASUGRE                  ATABENGAGITTIM 
##                             711                             295 
##                         BABADAM                      BABELAPARA 
##                             363                            1061 
##                        BABILGRE                    BABUPARA - I 
##                             447                             773 
##               BADRI WATREGITTIM                        BADUPARA 
##                             999                             491 
##                        BAGHMARA                         BAGUGRE 
##                            6895                             395 
##                       BAINAPARA                       BAKATAGRE 
##                            1165                             609 
##                        BAKDAGRE                        BAKLAGRE 
##                             651                             601 
##                   BALACHANDA -I                     BALADINGGRE 
##                             839                             296 
##                       BALAMAGRE                        BALAPARA 
##                             542                            1206 
##                         BALAT-A                    BALJEK ADUMA 
##                             669                             518 
##           BALJEKGRE SONGGITCHAM                 BALKAL JALAIGRE 
##                             501                             636 
##                       BALSATGRE                        BALUGHAT 
##                             700                             999 
##                        BALUPARA                       BALWATGRE 
##                             661                             775 
##                  BAMIL NONGRURA                        BAMKAMAR 
##                            1609                             702 
##                        BAMONGRE                      BAMUNDANGA 
##                             689                             678 
##                        BANAJURI                        BANBUDAI 
##                             451                             360 
##                      BANDARKONA                      BANGALKATA 
##                             999                            1813 
##             BANGONG BINGBANGGRE                     BANGRANGGRE 
##                             497                             541 
##                     BANGSI APAL                    BANGSI DOGRU 
##                             941                             734 
##                       BANGSIDUA                       BANSAMGRE 
##                             893                             572 
##                      BANSINGGRE                        BARATO A 
##                             112                            1098 
##                        BARATO B                     BARENGAPARA 
##                            1080                             726 
##                BARIDUA 9TH MILE                        BARIKGRE 
##                             600                             497 
##               BARINGGRE BOLKRET                        BATABARI 
##                             475                             857 
##                           BATAW                         BAWEGRE 
##                            1004                             430 
##                     BAWEGRE (A)                        BELAHARI 
##                             232                             300 
##                         BELBARI                         BELGURI 
##                            1642                             494 
##                       BENABAZAR          BERNONGSAI (NONGSPUNG) 
##                             307                             296 
##                        BERUBARI                        BERUPARA 
##                             520                             511 
##                        BETASING                         BETGORA 
##                            1746                             330 
##                    BHAITBARI-II                       BHAJAMARA 
##                            1707                             785 
##                      BHANGARPAR                     BHARALIGAON 
##                            1098                             521 
##                      BHATUAGAON                      BHAWANIPUR 
##                             615                             222 
##                      BHOIRAKUPI       BHOIRYMBONG (LUMSOHPIENG) 
##                             505                             695 
##                     BHOLARBHITA                        BIBRAGRE 
##                            2310                             709 
##              BIJASIK MATWA APAL                BIJASIK TIMBOGRE 
##                             528                             399 
##                     BIKONGGRE-I                         BILKONA 
##                             971                             840 
##                         BILLGRE                       BLEISHIAH 
##                             279                             116 
##                     BOIRAGIPARA                        BOLABETA 
##                            1251                             764 
##                       BOLBOKGRE              BOLCHIMDA SONGMONG 
##                            1045                             730 
##                       BOLCHUGRE                 BOLCHUKATONGGRE 
##                            1073                             398 
##                       BOLDAKGRE                   BOLDAKGRE (B) 
##                             323                             308 
##                       BOLDAMGRE                      BOLKINGGRE 
##                            2035                            1008 
##                      BOLLONGGRE                  BOLLONGGRE (A) 
##                             273                             868 
##                BOLMORAM AGALGRE              BOLMORAM DOCHOKGRE 
##                             380                             408 
##        BOLONGGRE SONGSAK AGITOK                         BOLPUMA 
##                             663                             696 
##                       BOLSALGRE                   BONDUKMALI(B) 
##                             893                             798 
##                   BONE CHISOGRE                         BONEGRE 
##                             281                             534 
##                        BORBHUIN                 BORGANG MARNGAR 
##                             513                             660 
##                         BORGHAT                    BORODOLDONGA 
##                             450                             404 
##                       BORUAPARA                        BOWABARI 
##                             480                             426 
##                        BURIPARA                       BURIRJHAR 
##                             818                            1289 
##                       BYNDIHATI                        BYRNIHAT 
##                            1464                             508 
##                           BYRWA                          BYRWAI 
##                             603                             911 
##                  CENTRE VILLAGE                      CHACHATGRE 
##                             412                             646 
##                        CHAIPANI                       CHAM-CHAM 
##                            1107                             792 
##                       CHAMAGURI                       CHAMBAGRE 
##                            1548                             668 
##                CHAMBIL TOLEJANG                       CHANDIGRE 
##                             568                            1193 
##                      CHANDOBHUI                   CHAPAHATI (1) 
##                             835                             788 
##                   CHAPAHATI (2)                    CHARBATAPARA 
##                             570                            1571 
##                  CHARKASARIPARA                       CHASINGRE 
##                             396                             926 
##                       CHEKWEBRA                       CHELIPARA 
##                             438                             100 
##                      CHENGBAGRE                      CHENGGALMA 
##                             764                             923 
##                     CHENGGAPARA               CHENGGNI SONGMONG 
##                             770                             273 
##                       CHENGKALI                    CHENGKOMPARA 
##                             697                             720 
##                        CHEPAGRE                CHERAN SONGGITAL 
##                             628                             471 
##              CHERAN SONGGITCHAM                CHERAN SONGMAGRE 
##                             234                             542 
##                    CHERRAPUNJEE                     CHIBOK APAL 
##                            7393                             307 
##          CHIBONGGRE SONGGITCHAM                  CHIBRA AGALGRE 
##                            1005                            1502 
##                 CHIDARET SONGMA                       CHIDEKGRE 
##                             503                             743 
##                 CHIDIMIT NAMESA                      CHIEHRUPHI 
##                             558                             570 
##                  CHIGANCHINGGRE                   CHIGITCHAKGRE 
##                             372                            1638 
##               CHIKAL DAWAGITTIM                    CHIKAL PEKRO 
##                             184                             461 
##                   CHIKAL SONGMA                     CHIKASINGRE 
##                             253                             688 
##                 CHIMAGRE GRADEK                        CHIMITAP 
##                             349                             323 
##                     CHINABATGRE                     CHIRINGPARA 
##                             351                             399 
##                      CHIRRAKATA                       CHISAKGRE 
##                             786                             455 
##                     CHISIM APAL                       CHISIMARI 
##                             999                             799 
##                       CHISREGRE                     CHITIL APAL 
##                            1484                             422 
##                   CHITUK DADRAM                        CHOKAGRE 
##                             970                             473 
##                      CHOKCHOKIA                      CHOKPOTGRE 
##                             715                             999 
##            CHONDONPARA (SONGMA)                     CHONGNAPARA 
##                             798                             642 
##                       CHOPAPARA               CHOTTO BOLLANGGRE 
##                             127                             650 
##                    CHURABUDIGRE                        DABAKGRE 
##                             887                             402 
##             DABANG BOLSALDAMGRE                     DABIT BIBRA 
##                             636                             725 
##                     DABITGITTIM                       DADENGGRE 
##                             850                            1534 
##                       DADONGGRE                      DAGAL APAL 
##                             215                             592 
##                   DAGAL ARINGGA                 DAGAL BOLMEDANG 
##                             348                             320 
##                 DAGAL SONGITTAL                        DAISTONG 
##                             592                             546 
##                      DAJAKKAGRE                  DAJI TEKSRAGRE 
##                             360                             727 
##                     DAJONG GATE                  DALBOT MATRANG 
##                             401                             291 
##                    DALCHENGKONA                        DALDAGRE 
##                             492                             535 
##                           DALIA                      DALLANGGRE 
##                             577                             305 
##                   DALLENGGITTIM                        DALUAGRE 
##                             287                             483 
##                        DALUGAON                        DALUPARA 
##                            1114                             651 
##                      DAMAL ASIM                          DAMASH 
##                             745                            1998 
##                DAMBO BIMAGITTIM                 DAMBO RESERVE-I 
##                             845                             672 
##                    DAMBO WATESA                      DAMBUK AGA 
##                             592                             784 
##                     DAMBUK APAL                    DAMDILLOKGRE 
##                             202                             893 
##                    DAMIT DANGRA                      DANAKGRE A 
##                             454                             992 
##               DANAL BOLGIPOKGRE               DANAL SONGGITCHAM 
##                             357                             136 
##                       DANANGGRE                        DANDAKOL 
##                             757                             460 
##                          DANGAR               DANGKONG DOKATONG 
##                             920                             454 
##                          DAPGRE                DAPORBHITA RABHA 
##                            1034                             910 
##              DAPSI NENGRUGITTIM                  DARAK AKONGGRE 
##                             299                             609 
##                        DARAKONA                   DARANG BOLDAK 
##                             545                             493 
##               DARANG PATALGITIM                     DARECHIKGRE 
##                             999                             546 
##                      DAREN AGAL                      DARIBOKGRE 
##                             868                             149 
##                     DARING APAL                   DARIT NILWASA 
##                             186                             386 
##                      DARONG ADU                       DARRANG A 
##                             547                             572 
##                       DARRANG B                         DARUGRE 
##                             596                             850 
##          DARUSAK (DARUGRE ALDA)                    DASING BIBRA 
##                            2174                             429 
##                         DASPARA                  DAWA GITINGGRE 
##                            1518                             725 
##                           DAWKI                        DEBRAGRE 
##                            1260                             680 
##                     DEFULIAPARA                      DEGRANGGRE 
##                             683                             505 
##                     DEINSHYNRUM                       DEMTHRING 
##                             382                            2198 
##                     DEMTHRING A                     DEMTHRING B 
##                             463                             514 
##                      DENAJIKGRE                       DENDAMGRE 
##                             319                             556 
##                     DENGNAKPARA                         DEOSALI 
##                            1097                             617 
##                     DERINGGAGRE                       DEWANKATA 
##                             602                             294 
##               DEWLIEH MAWRISNAI                          DEWSAW 
##                             569                             415 
##                     DHAPANGPARA                     DHOLAI GOAN 
##                             935                             755 
##                    DHOLAI MALAI                       DHOPAKURA 
##                             507                             714 
##                   DIENGKYNTHONG                      DIENGLIENG 
##                            1100                             474 
##                      DIENGPASOH           DIENGSOHMAUD MAWBSEIN 
##                            1187                             505 
##                      DIGRANGGRE                       DIJINGGRE 
##                             433                             491 
##                DILMA KERAGALRAM    DILMA SONGGITCHAM (CHIADING) 
##                             773                             326 
##                        DILSIGRE                  DIMBIL BONEGRE 
##                             835                             258 
##                       DIMILIGRE                           DIMIT 
##                             593                             216 
##                     DINAMINGGRE                      DINANGPARA 
##                             324                             790 
##                      DINGAMPARA                      DINGANPARA 
##                             931                             730 
##                        DINGJOAR                         DIPOGRE 
##                             669                             492 
##                            DIRA                          DISONG 
##                             637                             851 
##                           DIWON                     DKHIAH EAST 
##                             833                            1293 
##                     DKHIAH WEST                       DOABOKGRE 
##                             655                             515 
##                       DOBA APAL            DOBAKOL NENGJAGITTIM 
##                             817                             740 
##                         DOBOGRE                  DOBOK JAKOLGRE 
##                             433                             507 
##                 DOBU CHITIMBING         DOBU RONGMU SONGGITCHAM 
##                             181                             345 
##                   DOBU SONGMONG                       DODANGGRE 
##                            1353                             247 
##                   DOGRINGGITTIM                      DOKAMCHENG 
##                             202                             999 
##                        DOLDEGRE                      DOLLONGGRE 
##                             454                            1012 
##                     DOLSI NOKAT                       DOMAGITOK 
##                             816                             240 
##                       DOME ANTI                      DOMMAWLEIN 
##                            1281                             217 
##                        DOMSKONG                         DOMTRAW 
##                             319                             114 
##                        DONASKUL                   DONGKIINGDING 
##                             693                             577 
##                     DOPANANGGRE                     DOPATCHIGRE 
##                             324                             919 
##                          DOPGRE                         DOPOGRE 
##                             808                             689 
##                        DORAKGRE                     DORAMBOKGRE 
##                             162                             848 
##                     DORENGKIGRE                       DOROMCHAS 
##                             428                             353 
##                         DUBAGRE                      DUFARIGAON 
##                             373                             999 
##                        DUGALGRE                         DUM DUM 
##                             781                            1360 
##                       DUMNIGAON                    DURA ASIMGRE 
##                             544                             651 
##             DURABANDA AGITOKGRE                   DURAKANTRAGRE 
##                             417                             155 
##                        EDENBARI                         EGOPARA 
##                             606                             515 
##                  EMAN DURABANDA                 EMAN GATABILGRE 
##                             623                             311 
##                   EMAN SONGMONG                       ERA ANING 
##                             591                             498 
##                      FERSAKANDI                  GABIL DANINGKA 
##                            1631                             731 
##                     GABIL KOKSI                       GALWANGSA 
##                             499                             608 
##                      GAMBARIGRE                        GAMBEGRE 
##                             309                             832 
##                      GAMBIL AGA                 GANCHIKALAK (A) 
##                             654                             973 
##                      GANDHIMARI                      GANDHIPARA 
##                             515                             840 
##            GANDOPARA (BALALGRE)                       GANGBANGA 
##                             817                             571 
##                      GANOL APAL                         GAOBARI 
##                             524                             644 
##                  GARA BOKMANGRE                   GARE SONGMONG 
##                             639                             813 
##                       GAROBADHA                        GARODUBI 
##                            1852                            1931 
##                       GASUAPARA                      GASURAGAON 
##                            1487                             722 
##                       GIMBILGRE                         GIMEGRE 
##                             287                             997 
##                     GINDAPASARI                       GINDOPARA 
##                             593                             538 
##             GITTINGGRE SONGMONG                        GOALGAON 
##                             703                             589 
##                        GODALGRE                         GOKAGRE 
##                             782                             689 
##                       GOLADIGLI                  GOLADIGLI - II 
##                             561                             423 
##                       GOLDATGRE          GOLFLINK KHLIEH SHNONG 
##                             801                            2588 
##           GOLFLINK PDENG SHNONG                      GOMAIJHORA 
##                            2522                             955 
##                   GONCHUDAREGRE                        GONDAGRE 
##                             746                             708 
##                      GONDENGGRE                     GONGGANGGRE 
##                             437                             887 
##                    GONGGLANGGRE                      GONGGNAGRE 
##                             971                             239 
##                        GONGRANG                       GOPALTHAN 
##                             386                             390 
##                   GOPINATHKILLA                       GOPRAMGRE 
##                             791                             579 
##                        GORAMARA                      GRENGGANDI 
##                             941                             703 
##                   GURPANI BIBRA                        HALCHATI 
##                             887                             480 
##                       HALDIBARI                    HALLIDAYGANJ 
##                            1228                            1075 
##                     HALWA ATONG                       HARIBANGA 
##                             587                            1162 
##                        HARIGAON                  HARINKATA GARO 
##                             416                             991 
##                         HARIPUR                     HARLI BAGAN 
##                             590                             859 
##              HASLONG RENGGITTIM                      HAT MAWDON 
##                             630                             761 
##                     HAT THYMMAI                        HATHISIL 
##                             112                             794 
##                  HATIBASA RABHA                        HATUGAON 
##                             537                            1192 
##                HAWAIBHOI (AMSE)                        HINGARIA 
##                             268                             511 
##                       HULLUKONA                           HUROI 
##                            1129                             764 
##                          IALONG               IALONG LUTI TUBER 
##                            1210                             756 
##                         IAMKHON                         IAPMALA 
##                             273                             563 
##                        ICHAMATI                      IEWMAWIONG 
##                            1335                             637 
##                      IEWMAWLONG              IMSILTOK BARINGGRE 
##                             476                             734 
##                          INGSAW                       IONGKALUH 
##                             496                            1325 
##                        IONGLWIT                         IONGNOH 
##                            1514                             682 
##                       IONGSNIEJ                          IOOKSI 
##                             419                            1297 
##                       ITSOHPAIR               IURIMKHLIEHSHNONG 
##                             263                             294 
##                           JABAR                           JADAP 
##                             792                             397 
##                            JAIR                    JAISRUGITTIM 
##                             266                             369 
##                         JAKHONG                          JAKREM 
##                             386                            1814 
##                  JALAPHET SUMER                 JALAPHET SUTNGA 
##                            1156                            1528 
##                        JALUAGRE                        JALWAGRE 
##                             731                             310 
##                         JALYIAH                       JALYNTENG 
##                            1354                            1001 
##                        JAMADWAR                    JAMBALGITTIM 
##                             574                             554 
##                      JANGRAPARA                          JARAIN 
##                             394                             871 
##                      JARANGKONA                      JARANGPARA 
##                             598                             253 
##                       JARIMPARA                          JAROIT 
##                             637                             422 
##                JAROIT POMKANIEW                  JATAH LAKADONG 
##                             734                             528 
##                  JATAH NONGLYER                       JATRAKONA 
##                             354                             807 
##                     JELBONGPARA                       JENDRAGRE 
##                             586                             390 
##                    JENGRINGPARA                        JERMANAI 
##                             655                             177 
##                        JETRAGRE                      JIJIKAPARA 
##                             584                             558 
##                      JOIRANGGRE               JONGBO CHIRINGGRE 
##                             683                             552 
##                      JONGDONGRE                      JONGKIPARA 
##                             418                             777 
##                        JONGKSHA                       JONGMEGRE 
##                            1939                             156 
##                       JONGUSHEN                          JORBIL 
##                             592                             899 
##              JOSIPARA CHRISTIAN                           JOWAI 
##                             621                           17057 
##                          JOYFER                       JUGIRJHAR 
##                             874                            1568 
##                          JYNTAH                          JYNTRU 
##                             461                             527 
##                         JYRMANG       KADAMSHALI(TIKRIKILL A C) 
##                             399                             656 
##                    KAIMBATAPARA                       KALAICHAR 
##                            1986                             999 
##          KALAIGAON MARAHALIPARA              KALAIGAON TILAPARA 
##                             633                             682 
##                 KALAK SONGGITAL                      KALAPANGTI 
##                             252                             174 
##                    KALCHENGPARA                        KALEGAON 
##                             864                             572 
##                   KAMA MRONGGRE                         KAMSING 
##                             592                              26 
##                           KANAI                      KANTOLGURI 
##                             474                             837 
##                      KAPASIPARA                     KARAWENGGRE 
##                             673                             379 
##                     KARIJORAGRE                       KARONGGRE 
##                             381                             682 
##                KARUKOL ADINGGRE                      KASARIPARA 
##                             520                            1132 
##                          KASHRA                         KASKONA 
##                             691                            1481 
##             KATCHUGRE (KOIKURI)                      KATHALBARI 
##                             507                            1197 
##                      KATULIGAON                        KAZIPARA 
##                             775                             537 
##                    KBET NONGBRI                        KDOHHATI 
##                             420                             801 
##                          KENBAH                      KENDRAKONA 
##                             373                             444 
##                   KENE SONGMONG                         KENIONG 
##                             545                             597 
##                         KHADDUM                         KHAHNAR 
##                             422                             584 
##                      KHALPARA-I               KHANAPARA HIGHWAY 
##                             553                             584 
##             KHANAPARA HILL DUBA                        KHANDULI 
##                             533                            1497 
##                        KHAPMARA                         KHAPMAW 
##                             194                             334 
##                        KHARABRI                         KHARANG 
##                             726                            1165 
##                       KHARANGOI                       KHARIGAON 
##                             651                             800 
##                       KHARKHANA                       KHASIADOP 
##                             181                             455 
##                        KHASIGRE           KHATARMER (12TH MILE) 
##                             770                            1233 
##                KHERAPARA SONGMA                         KHILBOI 
##                            1104                             841 
##                 KHLIEH LYNGKHOI                   KHLIEH UMSTEM 
##                            1183                             894 
##                   KHLIEH UMTREW                   KHLIEHRANGNAH 
##                             578                            1391 
##                 KHLIEHRIAT EAST                 KHLIEHRIAT WEST 
##                            1278                            1674 
##                    KHLIEHTYRSHI                     KHLOOKYNRIN 
##                             553                             509 
##                      KHONGLAH A                       KHONGPARA 
##                             816                             806 
##                      KHONSHNONG                          KHRANG 
##                             702                             400 
##                       KHUAINGOI                       KHUJIKURA 
##                             181                             690 
##            KHWAD (INC. SILTHAM)                          KHWENG 
##                             218                             340 
##                       KHYNDEWSO                       KILLAPARA 
##                            1356                            1368 
##                            KLEW                      KMAWAN RUM 
##                             678                             563 
##                      KODALDHOWA                       KOINABHUI 
##                             646                             741 
##                       KOINADUBI                    KOKNAL IMONG 
##                             484                             405 
##                   KOKSI NENGSAT                        KOLAPARA 
##                             489                             457 
##                       KOLTAPARA                       KONARCHAR 
##                             702                            1093 
##                   KONGKINANGGRE                       KONGTHONG 
##                             374                             430 
##                     KONGTOKPARA                        KONGWANG 
##                            1212                             376 
##                        KORHADEM                KORSTEP NONGTLUH 
##                             589                             279 
##                       KOSI GATE                           KRANG 
##                             880                            1182 
##                           KREIT                           KRUIN 
##                            1261                             571 
##                     KSEHKOHMOIT                      KSEHMAWNAI 
##                             618                             444 
##                    KSEHPYNGDENG                    KSEHRYNSHANG 
##                             698                             708 
##                      KUDENG RIM                  KUDENG THYMMAI 
##                             257                             246 
##                        KUKURMUA                         KULIANG 
##                             808                             691 
##                        KULIGAON                        KULUPARA 
##                             721                             814 
##                       KUMLIGAON                       KUNONGRIM 
##                             858                             112 
##                             KUT                           KYIEM 
##                             861                            1141 
##                         KYNDONG       KYNDONGTUBER LUMKHANGDONG 
##                             802                             782 
##                  KYNDONGTUBER N                  KYNDONGTUBER S 
##                             766                            1186 
##                   KYNJOIN UMRAN                       KYNMYNSAW 
##                             577                             613 
##                         KYNRANG                          KYNROH 
##                             340                            1000 
##                          KYNRUD                          KYNSEW 
##                             798                             493 
##                          KYNSHI                   KYNSHI BANGLA 
##                             574                             637 
##              KYNSHI MAWPHAN AIN                   KYNSHI MAWRIA 
##                             430                             690 
##                          KYRDEM                KYRDEMKULAI 5 KM 
##                             704                             804 
##                          KYRDOH                         KYRPHEI 
##                             685                             546 
##                       LABANSARO                     LAD MAWRENG 
##                             670                             695 
##                      LAD MUKHLA                      LAD RYMBAI 
##                             897                            1111 
##                    LADMAWPHLANG                         LADMIRI 
##                             408                             498 
##                LAIPHEWDIENGNGAN                       LAITARTED 
##                             505                             552 
##                    LAITDIENGSAI                         LAITDUH 
##                             446                             115 
##                         LAITIAM                         LAITJEM 
##                             414                             806 
##                         LAITKOR                        LAITKSEH 
##                            4491                             622 
##                      LAITKYNSEW                     LAITKYRHONG 
##                             892                            1206 
##                         LAITLUM                      LAITLYNDOP 
##                             401                             407 
##                     LAITLYNGKOT                      LAITLYTING 
##                            2758                             754 
##                      LAITMAWPEN                    LAITMAWSIANG 
##                             536                            1331 
##                     LAITMYNSANG                     LAITNAMLANG 
##                             176                             388 
##                        LAITNONG                    LAITNONGKSEH 
##                             525                             919 
##                     LAITNONGRIM                      LAITRYNGEW 
##                             909                            1979 
##                       LAITSOHUM                        LAITTYRA 
##                             311                             504 
##                        LAKADONG                LAKADONG (UMMAT) 
##                             304                             311 
##               LAKADONG UMLATDOH                        LAKASEIN 
##                             339                             345 
##                         LALPANI                        LALUMPAM 
##                             970                             393 
##                            LAMA                        LAMALONG 
##                             204                             388 
##                    LAMIN SHNONG                         LAMLYER 
##                            1157                             483 
##                      LAMYRSIANG                       LANGKAWET 
##                             502                             125 
##              LANGKYRDING MIHNGI                          LANGPA 
##                            1150                             235 
##                         LANGTOR                        LAPALANG 
##                             646                            1150 
##                        LAPANGAP                          LARKET 
##                            1030                             430 
##                         LASKEIN                   LASKERPARA(A) 
##                            1080                             689 
##                        LATRIGRE                        LATYMPHU 
##                             585                            1075 
##                         LATYRKE                          LAWBAH 
##                             710                             923 
##                       LAWBYRTUN                        LAWBYRWA 
##                             840                             373 
##                      LAWJYNRIEW                       LAWKYNTER 
##                            1930                             319 
##                          LAWMEI                        LAWSHLEM 
##                            1290                             299 
##                         LAWSIEJ                       LAWSOHTUN 
##                             653                            5128 
##                          LEIJRI                           LELAD 
##                             588                             458 
##                  LEPROCY COLONY                        LIARBANG 
##                             183                             542 
##                        LIARKHLA                    LOWER BALIAN 
##                             496                             645 
##              LOWER CHIGIJANGGRE                 LOWER CHISIKGRE 
##                             435                             873 
##                 LOWER DAMACHIGA                  LOWER DAMALGRE 
##                             548                             729 
##                   LOWER DOSOGRE               LOWER KARCHENGDAP 
##                             455                             913 
##                       LUKAICHAR            LUM MISSION MAWBSEIN 
##                             512                             627 
##                     LUM SHYRMIT                        LUMBASUK 
##                             716                             863 
##                     LUMDAITKHLA                         LUMDING 
##                            1096                             507 
##                      LUMIAWBLOT                         LUMKSEH 
##                             931                             526 
##                          LUMKYA             LUMLYNGKUT LUMSTONG 
##                             311                             678 
##                       LUMMAWBAH               LUMMAWSIANG UMDUM 
##                            2424                             601 
##                        LUMNIWAR                      LUMNONGRIM 
##                             618                            1445 
##                       LUMPUTHOI                     LUMPYNGNGAD 
##                             406                            1064 
##                        LUMROMAN                        LUMSHKEN 
##                             842                             720 
##                      LUMSHNGAIN                       LUMSHNONG 
##                            1015                            1079 
##                       LUMSHYIAP                     LUMSOHKHLUR 
##                            2779                             960 
##                       LUMWAHNAI                            LURA 
##                             577                             363 
##                        LUTUBARI                        LYMPHUID 
##                             550                             265 
##                LYMPUNG SHYRNGAN                          LYNDEM 
##                             460                             332 
##                    LYNDET KHLAW                     LYNGDOHMASI 
##                             661                             362 
##                  LYNGKHAT KHURI                       LYNGKHUNG 
##                              78                             847 
##               LYNGKYRDEM IEWDUH                        LYNSHING 
##                             801                             873 
##                   LYTING LARBRI                  LYTING LYNGDOH 
##                             113                             279 
##                     MADAN BITAW                MADAN IING SYIEM 
##                             956                             979 
##        MADAN LYNGDOH NONGKYNRIH               MADAN NONGLAKHIAT 
##                             982                             542 
##                  MADAN SHADSNGI                    MADANBYNTHER 
##                             734                            1382 
##                     MADANKYNSAW                     MADANMAROID 
##                            1203                             538 
##                      MADANRTING                           MADUR 
##                            8023                             852 
##                       MAGALPARA                        MAGUPARA 
##                             495                             517 
##                MAHADEO SONGMONG              MAHENDRAGANJ BAZAR 
##                            1214                            1845 
##                MAHISHBATHANPARA                        MAIKHULI 
##                             772                            1149 
##                      MAIRANGBAH                  MAIRANGMISSION 
##                             668                            1872 
##                      MAIRUNGHEH                       MAITDIENG 
##                             559                             888 
##                      MAJHERCHAR                        MAJIPARA 
##                             571                             548 
##                       MAKALPARA                          MAKDOH 
##                             248                             188 
##                         MAKHALI                      MALCHAPARA 
##                             544                             467 
##                          MALMUA                           MANAD 
##                             529                             928 
##                           MANAI                        MANDAGRE 
##                             542                             724 
##                       MANDALGRE               MANDANG REDINGGRE 
##                             329                             609 
##                     MANGCHIMGRE                      MANGGAKGRE 
##                             563                             803 
##                      MANGGAPARA               MANGKENG SONGMONG 
##                             339                            1165 
##                       MANGRUGRE                 MANGSANG MOKURA 
##                             230                            1217 
##                       MANKINGRE                MARAK DILWANGGRE 
##                             215                             569 
##                        MARAPARA                      MARBANIANG 
##                             600                             739 
##                 MARBISU MAWSMAI             MARBISU PDENGSHNONG 
##                            1694                            1094 
##                          MARIEM                         MARKASA 
##                             604                             926 
##                         MARMAIN                           MAROK 
##                             735                             720 
##                          MARPNA                      MARSHILONG 
##                             750                             876 
##                      MASANGPANI                          MASSAR 
##                             442                             403 
##           MASSAR (INC. DYMMIEW)                       MATALAGRE 
##                             286                             619 
##                    MATRAMCHIGRE                      MAULAKANDI 
##                             852                            1774 
##                          MAW-AH                          MAWBEH 
##                             103                            1120 
##                          MAWBER                        MAWBLANG 
##                            1186                             548 
##                         MAWBLEI                          MAWBRI 
##                             839                             500 
##                         MAWDANG                  MAWDIANG-DIANG 
##                             771                             563 
##                      MAWDIANGUM                          MAWDON 
##                             575                             203 
##                       MAWEITNAR                    MAWHATIPDENG 
##                             279                             921 
##                      MAWIAPBANG                         MAWIONG 
##                             231                            1495 
##                     MAWIONG RIM                    MAWIONG SUNG 
##                             787                             154 
##                MAWIONG UMJAPUNG                          MAWJAI 
##                            3444                             238 
##                       MAWJARAIN                        MAWJATAP 
##                             160                             457 
##                        MAWKAJEM                       MAWKAMOIT 
##                             312                             946 
##                       MAWKAPHAN              MAWKARAH NONGKDAIT 
##                             249                             764 
##              MAWKARAH NONGWAHRE                      MAWKASIANG 
##                             778                             623 
##                         MAWKDOK                         MAWKDUK 
##                            1065                             519 
##                          MAWKER                         MAWKHAN 
##                             409                            1144 
##                        MAWKHANU                         MAWKHAP 
##                             182                             983 
##                         MAWKHAR                         MAWKHLI 
##                             953                             371 
##                    MAWKHMAHRANG                     MAWKHYRWANG 
##                             382                             223 
##                        MAWKLIAW                         MAWKLOT 
##                             495                            1171 
##                          MAWKMA                        MAWKNENG 
##                             576                             995 
##                       MAWKOHMIT                      MAWKOHNGEI 
##                             613                             448 
##                      MAWKOHPHET                         MAWKRIA 
##                             386                             468 
##                        MAWKRIAH                       MAWKYLLEI 
##                            1413                             741 
##                      MAWKYNRANG                       MAWKYNREW 
##                             483                             613 
##                      MAWKYNRING              MAWKYNWAN LYNGKHOM 
##                             293                             198 
##                      MAWKYRDANG                       MAWKYRDEP 
##                             310                             549 
##                       MAWKYRWAT               MAWLAI IEWRYNGHEP 
##                            1193                            1690 
##            MAWLAI KYNTON MASSAR               MAWLAI MAWDATBAKI 
##                            2512                            4434 
##                   MAWLAI MAWROH                 MAWLAI MOTSYIAR 
##                            2739                            1421 
##                 MAWLAI NONGKWAR                  MAWLAI NONGLUM 
##                            4470                            2851 
##                MAWLAI NONGPDENG                 MAWLAI PHUDMURI 
##                            2316                            2806 
##             MAWLAI SYLLAIKARIAH                  MAWLAI UMJAIUR 
##                            1269                            1963 
##                 MAWLAI UMTHLONG                      MAWLAINGUT 
##                            1379                             411 
##                  MAWLAISYIEM(M)                      MAWLAITENG 
##                             595                             641 
##                         MAWLALI                          MAWLAM 
##                             509                             667 
##                         MAWLANG                      MAWLANGREN 
##                             315                             667 
##                      MAWLANGWIR                       MAWLASNAI 
##                            1414                            1821 
##                          MAWLAT                       MAWLATANG 
##                             549                             260 
##                         MAWLEIN                 MAWLEIN MAWKHAN 
##                             507                            1002 
##                         MAWLIEH                  MAWLIEHLAITDOM 
##                             275                             675 
##                         MAWLONG                      MAWLONGBAH 
##                            3704                             167 
##                      MAWLONGROH               MAWLUM MAWJAHKSEW 
##                             388                             459 
##                 MAWLUMKOHKHRANG                         MAWLWAI 
##                             249                             150 
##                       MAWLYNDEP                       MAWLYNDUN 
##                             490                             467 
##                       MAWLYNGAD                    MAWLYNGKHUNG 
##                            1062                             648 
##       MAWLYNGOT INC. IEWRYNGHEP                      MAWLYNNONG 
##                             500                             271 
##                       MAWLYNREI                    MAWLYNTRIANG 
##                            2238                             844 
##                        MAWMARAM                       MAWMERANG 
##                             867                             236 
##               MAWMITBAH-DOMRUAH                         MAWMLUH 
##                             366                             876 
##                       MAWMUTHOH                          MAWNAI 
##                            1081                            1120 
##                         MAWNGAP                   MAWNGAP DUKAN 
##                             124                             512 
##                 MAWNGAP MAWSMAI                     MAWNGAP RIM 
##                            1416                             979 
##                     MAWNIANGLAH                    MAWNOHSYNRUM 
##                             916                             157 
##                          MAWPAT                        MAWPDANG 
##                            3821                            1055 
##                          MAWPEN                     MAWPHANNIEW 
##                             948                            1370 
##                       MAWPHLANG                        MAWPHREW 
##                            2059                             245 
##                         MAWPHRU                          MAWPHU 
##                             474                             632 
##                  MAWPON MYRKHEW                     MAWPONGHONG 
##                              82                             637 
##                         MAWPRAN                          MAWPUD 
##                             799                             846 
##                          MAWPUN                   MAWPUN KSHAID 
##                            4069                             333 
##                      MAWPUNNENG                       MAWPYLLUN 
##                             717                             682 
##                      MAWPYNTHIH                     MAWPYRSHONG 
##                            1472                            1167 
##                          MAWRAH                         MAWRANG 
##                             564                             184 
##                     MAWRANGLANG                          MAWRAP 
##                             871                             202 
##                        MAWRAPAD                        MAWRASAI 
##                             808                             252 
##                         MAWRENG                           MAWRI 
##                             913                             836 
##                        MAWRIANG                  MAWRIANGTYNNAI 
##                             534                             252 
##                        MAWRIPIH                          MAWROH 
##                             290                            1354 
##                         MAWRONG                     MAWRYNGKANG 
##                             978                             518 
##                    MAWRYNGKNENG                       MAWSADANG 
##                            3926                             634 
##                        MAWSAHEW                         MAWSAIN 
##                             468                             132 
##                          MAWSAW                          MAWSEP 
##                             767                             501 
##                       MAWSHBUIT                         MAWSHUN 
##                            1725                             844 
##                         MAWSHUT                    MAWSIATKHNAM 
##                             718                             710 
##                         MAWSING                          MAWSIR 
##                             457                             337 
##                         MAWSIUM                     MAWSKEITHEM 
##                             278                             369 
##                         MAWSMAI                          MAWSNA 
##                            1171                             512 
##                        MAWSPONG                       MAWSYNNAM 
##                              60                             704 
##              MAWSYNRAM DONGNENG               MAWSYNRAM DONGRUM 
##                            1170                            1077 
##                       MAWSYNTAI                         MAWTARI 
##                             460                             543 
##                        MAWTAWAR                       MAWTEIBAH 
##                            1026                             298 
##                          MAWTEN                       MAWTEPIEW 
##                            1371                             581 
##            MAWTHANG SOHKHYLLUNG                     MAWTHAWPDAH 
##                             733                             637 
##                         MAWTHEI                        MAWTHLEN 
##                             388                             170 
##                        MAWTHONG                       MAWTIKHAR 
##                             620                             368 
##                         MAWTNEN                        MAWTNENG 
##                             340                            1052 
##                         MAWTNUM                       MEBITPARA 
##                             466                             603 
##                       MEDU APAL                         MEGAGRE 
##                             968                             452 
##                        MEGAPGRE                  MEGUA SONGMONG 
##                             929                             424 
##            MEJOLGRE CHEKJONGBRA                     MEKA ADUGRE 
##                             309                             309 
##                       MEKMAKGRE                    MERENGGIPARA 
##                             609                             583 
##                     MERINGAPARA             MESEB & MCCL COLONY 
##                             411                             257 
##                         MIAPARA                       MIBONPARA 
##                             905                             726 
##                       MIHMYNTDU      MIHMYNTDU LUMPYRTUH SALINI 
##                            3095                             412 
##                       MINDIKGRE                       MISIMAGRE 
##                             862                             416 
##                  MITAP SONGMONG                         MOAMARI 
##                             689                             613 
##                       MODOKPARA                          MOILAM 
##                            1025                             648 
##                   MON BANGAMGRE                        MONABARI 
##                             547                             987 
##                      MONDOLPARA                       MOOBAKHON 
##                             961                             882 
##                          MOODOP                       MOODYMMAI 
##                            1120                            1791 
##                       MOOIAMBEI                       MOOKYMPAD 
##                             586                             534 
##                       MOOKYNDUR                      MOOKYNIANG 
##                             674                            1239 
##                      MOOLAMANOH                   MOOLAMYLLIANG 
##                             914                             459 
##                         MOOLANG                       MOOLASNGI 
##                             524                             482 
##                         MOOPALA                 MOOPYLLAITSYIAR 
##                             516                             640 
##                          MOORAB                       MOORATHUD 
##                             425                             684 
##                       MOOSAKHIA                        MOOSHROT 
##                             248                            1011 
##                        MORASUTI                         MORKONA 
##                            1258                             871 
##               MORONGGA NENGKRAM             MORONGGA RONGA AGAL 
##                             463                             646 
##                       MOTINAGAR                        MOULLIAN 
##                            1041                             675 
##                         MOULSEI                      MOWKAIAW A 
##                             941                            1109 
##                      MOWKAIAW B                   MOWTYRSHIAH A 
##                            1356                             989 
##                   MOWTYRSHIAH B                     MUKHAIALONG 
##                            1073                            1109 
##                          MUKHAP                          MUKHLA 
##                            1653                            1278 
##                           MUKOH                          MUKROH 
##                             511                            1238 
##                        MUKTAPUR                    MULAIT SUMER 
##                             654                             737 
##                        MULIEH R                           MULUM 
##                             731                             406 
##                           MUNAI                        MUPHLANG 
##                             625                             341 
##                        MUPLIANG                          MUPYUT 
##                             823                             931 
##                      MURCHAPANI            MUSIANG LAMARE (OLD) 
##                             884                             836 
##                        MUSNIANG                        MUSTEM A 
##                            1211                             582 
##                        MUSTEM B                          MUSTOH 
##                             605                             405 
##                     MUTHLONGRIM                          MUTONG 
##                             358                             749 
##                          MYLLAT                MYNGSNGAT RAKHWI 
##                             523                             677 
##                          MYNKBU                         MYNKREM 
##                             494                            1007 
##                         MYNKSAN                   MYNNAR JIRANG 
##                             401                             599 
##                   MYNRI UMSNING                        MYNRIANG 
##                             447                             286 
##                        MYNRIENG                         MYNSAIN 
##                             159                             348 
##                         MYNSANG                          MYNSKA 
##                             523                            1250 
##                        MYNSNGAT                   MYNSO LUMMARI 
##                            1095                            1089 
##                 MYNSO LUMPHLONG                         MYNTHLU 
##                             913                             731 
##                        MYNTKUNG                       MYNTRIANG 
##                             477                             344 
##                  MYRDON MAWTARI                  MYRDON NONGBAH 
##                             833                             571 
##                          MYRIAW                          MYRJAI 
##                            1036                             349 
##                       NADONGKOL                       NAGORGAON 
##                             232                             921 
##                        NAGRABIL                       NAGRAJORA 
##                             540                             931 
##                       NAGUAPARA                    NAJOKGRE - A 
##                             681                             322 
##                       NAMABILLA                         NAMDONG 
##                             941                            1161 
##                       NAMDONG A                      NANDIRCHAR 
##                             562                            1182 
##                         NANGAPA                      NAPAK APAL 
##                             853                             390 
##                 NAPAK BOLCHUGRE                        NAPAKGRE 
##                             432                             679 
##                         NARAGRE                         NARIGRE 
##                             428                              76 
##        NARINGGRE MARCHONGGITTIM                       NARONGGRE 
##                            1187                             333 
##                       NARONGKOL                          NARTAP 
##                             737                             677 
##                      NARTIANG A                      NARTIANG B 
##                             885                             698 
##                          NARWAN                 NARWAN LUMPYRDI 
##                             942                             483 
##                     NARWAN NEIN                    NAWERAM ASIM 
##                             443                             183 
##                        NAYAGAON                        NAYAPARA 
##                            1737                             884 
##                          NEKORA                NENGJA BOLCHUGRE 
##                             887                             512 
##                     NENGKALPARA                NENGKONG MANDANG 
##                             701                             256 
##               NENGKONG SONGMONG                     NENGKRA AWE 
##                             945                            1093 
##                     NENGSA APAL                      NENGSAMGRE 
##                             456                             612 
##                         NENGSRA                NENGSRANG ADUGRE 
##                             519                              91 
##                         NERBONG                      NEW AMKREM 
##                             694                             163 
##                   NEW BHAITBARI                     NEW BONBERA 
##                            1626                             235 
##             NEW MAJAI BHOLAGANJ                   NEW NONGTNGER 
##                            1522                             260 
##                   NEW PUTHIMARI                    NEW RUKALGRE 
##                             473                             404 
##                      NGUNDILANG                         NGUNRAW 
##                             131                            1087 
##                   NIANGBARITHEM                       NIDHANPUR 
##                             493                            1818 
##                        NILWAGRE                       NIMAIKATA 
##                             810                             815 
##                         NIRIANG                       NOGORPARA 
##                             615                             809 
##                          NOHRON                          NOHWET 
##                             533                            1568 
##                        NOKATGRE                          NOKCHI 
##                             942                             390 
##                        NOLIKATA                     NONGALBIBRA 
##                             377                            1797 
##                         NONGBAH              NONGBAH IAWMUSIANG 
##                            1369                             940 
##            NONGBAH KYNDONGSYIEM              NONGBAH MARSHILONG 
##                             875                             296 
##                  NONGBAH MAWDEM                NONGBAH MAWSHUIT 
##                             409                             390 
##                  NONGBAH MULANG               NONGBAH RANGBLANG 
##                            1283                             238 
##                   NONGBAHJYNRIN                   NONGBAREH RIM 
##                              62                             897 
##                         NONGBET                     NONGBIR LUM 
##                             830                             242 
##                        NONGBLAI                NONGBREI-NONGDOM 
##                             159                             675 
##                        NONGBSAP                       NONGCHRAM 
##                             768                            1698 
##                        NONGDIAT                   NONGDIENGNGAN 
##                             614                             432 
##                         NONGDOM                  NONGDOM MAWRIA 
##                            1394                            1020 
##                    NONGEITNIANG                        NONGHALI 
##                             250                             661 
##                       NONGHULEW                        NONGJNGI 
##                             329                            1189 
##                         NONGJRI        NONGJRI (INC. WAHSKONG & 
##                             479                             204 
##                 NONGJRI NONGBAH                       NONGJRONG 
##                            1793                             883 
##                       NONGKASEN                       NONGKDAIT 
##                             913                             858 
##                      NONGKENBAH                       NONGKHLAW 
##                             326                            1033 
##                     NONGKHLIENG                       NONGKHRAH 
##                             299                             617 
##                       NONGKHROH                     NONGKHYRIEM 
##                            1001                            1628 
##                      NONGKOHLEW                     NONGKONGKIL 
##                             311                             414 
##                        NONGKREM                        NONGKSEH 
##                            4023                            4263 
##                       NONGKTIEH                        NONGKWAI 
##                             778                             549 
##                         NONGKYA                      NONGKYNRIH 
##                             567                             745 
##                       NONGLADEW                        NONGLAIT 
##                             687                             824 
##                        NONGLANG                       NONGLATEM 
##                            1099                             827 
##                         NONGLUM                    NONGLYNGKIEN 
##                             501                             115 
##                       NONGLYPUT                       NONGMAHIR 
##                             677                             419 
##                      NONGMALANG                     NONGMYNSONG 
##                             108                            8459 
##                         NONGNAM                 NONGNUB UMPOWIN 
##                             275                             626 
##                      NONGPATHAW                        NONGPIUR 
##                             659                             829 
##                         NONGPOH                      NONGPRIANG 
##                            2341                             169 
##          NONGPYRDI (INC. KLANG)                         NONGRAH 
##                             189                            7480 
##                        NONGRIAT                      NONGRILONG 
##                             125                             155 
##               NONGRIM (WARDING)                   NONGRIM HILLS 
##                             240                            2620 
##                  NONGRIM JIRANG               NONGRIM NONGLADEW 
##                             447                             437 
##                NONGRIMBAMBTHONG                        NONGRMAI 
##                             440                             522 
##                     NONGRYNGKOH                    NONGRYNNIANG 
##                            1176                             291 
##                       NONGSANGU                        NONGSDER 
##                             499                            2189 
##                   NONGSHILLIANG                    NONGSHILLONG 
##                            1654                             676 
##                       NONGSHKEN                      NONGSHLUID 
##                            1253                             337 
##                NONGSHYIAPJARAIN                       NONGSNING 
##                             117                             734 
##                       NONGSOHMA                       NONGSPUNG 
##                             909                            1647 
##                     NONGSPUNG A                       NONGSTENG 
##                             461                             328 
##                       NONGSTOIN                     NONGSYNRIEH 
##                           15810                             679 
##                    NONGTALANG A        NONGTALANG AMSOHMEHELENG 
##                             651                             149 
##                    NONGTALANG B                    NONGTALANG C 
##                             400                             820 
##                    NONGTALANG D                      NONGTHLIEW 
##                             620                            1254 
##                     NONGTHYLLEP                     NONGTHYMMAI 
##                             868                            8757 
##           NONGTHYMMAI 15TH MILE              NONGTHYMMAI KYRDEM 
##                             598                             454 
##                        NONGTRAI                        NONGTRAW 
##                             714                             604 
##                      NONGTYNGUR                     NONGTYNNIAW 
##                             970                             392 
##                      NONGTYRLAW                          NONGUM 
##                             296                             596 
##                      NONGUMLONG                       NONGUMMER 
##                             912                             304 
##                          NONGUR                         NONGWAH 
##                             635                             519 
##                 NONGWAH MAWLEIN                 NONGWAH MAWPNAR 
##                             441                             211 
##                         NONGWAR                 NOONMATI GOFRAI 
##                             679                             986 
##                        ODALGURI                       OKCHOKGRE 
##                            1103                             331 
##            OKKAPARA SONGGITCHAM                 OKKAPARA SONGMA 
##                             361                             395 
##                        PADU BAH                 PAGLAPARA NOKAT 
##                            1342                             545 
##                           PAHAM                    PAHAM SOHBAR 
##                            1233                              41 
##                  PAHAM TILAPARA                PAHAM UMSYLLIANG 
##                             656                             290 
##                   PAHAMBIR THEM                 PAHAMDIENGSYIAR 
##                             517                             357 
##                        PAHAMJRI                      PAHAMKHROH 
##                             512                             250 
##                     PAHAMLAPONG                     PAHAMRINIAI 
##                             405                             389 
##                  PAHAMRIOH THEM                      PAHAMSYIEM 
##                            1126                            1155 
##                     PAHAMUMSHRU                        PAKREGRE 
##                             649                             853 
##                            PALA                        PAMLABAN 
##                             677                             302 
##                        PAMLATAR                        PAMMANIK 
##                             268                            1209 
##                PAMRA KMAISHNONG                    PAMRAPAITHLU 
##                             748                             573 
##                       PAMRINIAI                    PANCHERING-A 
##                             218                             647 
##                  PANDA CHIKASIN                PANITOLA DAMSITE 
##                             320                             201 
##                         PARIONG                        PASADWAR 
##                            1045                             486 
##                          PASHUM                          PASYIH 
##                             137                            1321 
##                        PATAGHAT                      PATHARKATA 
##                             738                             998 
##                     PATHARKHMAH                    PATHARLYNDAN 
##                            1899                             494 
##                        PATIJORA                        PATRANGA 
##                             464                             558 
##                        PAULPARA                       PAWPHLANG 
##                             847                             530 
##                      PDEINIADAW                     PDENGKARONG 
##                             513                             254 
##                       PDENGKSEH                    PDENGNONGRIM 
##                             101                             243 
##                     PDENGSHAKAP              PEDALDOBA-I (GARO) 
##                             987                            1150 
##                        PHANBHUR                  PHLANG MAWPRAH 
##                             466                             409 
##                    PHLANGDILOIN             PHLANGKYNSHI MIHNGI 
##                             680                             466 
##                 PHLANGMAWSYRPAT                    PHLANGTYNGUR 
##                             256                             416 
##                   PHLANGWANBROI                   PHLONGINGKHAW 
##                            1178                             532 
##                       PHOTAMATI                        PHOTJAUD 
##                             546                             762 
##              PHOTJAUD-RANGTHONG                        PHOTKROH 
##                             361                             432 
##                        PHULBARI                      PILANGKATA 
##                            3749                             959 
##                      PILANGKU B                        PINGWAIT 
##                             270                             638 
##                          PLASHA                         POHKSEH 
##                             620                             502 
##                       POKIRKONA        POLICE QUARTER (MAWIONG) 
##                             464                             830 
##                      POLO HILLS                        POMBLANG 
##                            1022                             236 
##                       POMLAHIER                       POMLAKRAI 
##                             571                            2996 
##                          POMLUM                         POMMURA 
##                            1484                             385 
##                      POMSANNGUT                       POMSHUTIA 
##                             808                             558 
##                      PONCHAPARA                        PONGKUNG 
##                             453                             842 
##                        PONGTUNG                    POSSENGGAGRE 
##                             498                             535 
##                          PRIANG                     PUNGSANIANG 
##                             438                             341 
##                      PURAKHASIA                 PURDUA KHARPATI 
##                             618                             257 
##                         PURIANG                     PUSKANIPARA 
##                            1089                             924 
##                          PYLLUN                     PYNDENDIWAH 
##                             637                             194 
##                   PYNDENGDOMBAH                  PYNDENGNONGBRI 
##                             714                             702 
##                   PYNDENGSOHSAW         PYNDENGUMIONG DONG GATE 
##                             949                             986 
## PYNDENGUMIONG DONG LANGSTIEHRIM       PYNDENGUMIONG DONG LUMIEW 
##                            1332                             951 
##  PYNDENGUMIONG DONG LUMMARALONG      PYNDENGUMIONG DONG MAWSAWA 
##                             605                             744 
##                 PYNDENGUMJARAIN                      PYNDENKSEH 
##                             245                             290 
##                   PYNDENSAKWANG                     PYNDENUMSAW 
##                             347                             606 
##                       PYNGKER A                       PYNGKER B 
##                             197                             157 
##                          PYNKYA                          PYNTER 
##                             240                             833 
##                         PYNTHOR                      PYNTHORBAH 
##                             541                            5268 
##                 PYNTHORLANGTEIN                        PYNURSLA 
##                             403                            2605 
##                           PYRDA                          PYRNAI 
##                            1020                             706 
##                       PYRTAKUNA                         QUININE 
##                             382                             377 
##                         RAITONG                       RAJA APAL 
##                             717                             674 
##                        RAJABALA                         RAJAI-A 
##                             999                             333 
##                         RAKABAH                       RAKSAMGRE 
##                             533                             803 
##                       RALIANG A                       RALIANG B 
##                             535                             825 
##          RALIANG DONG LUMSEHKOT                      RAMCHENGGA 
##                             486                             861 
##                      RAMJONGGRE        RAMKHENG (INC. IAPSMIAW) 
##                             619                             330 
##                         RAMSIEJ                       RANGASORA 
##                             492                             277 
##                     RANGBIH-BIH              RANGBLANG POMBRIEW 
##                             481                             972 
##            RANGBLANG SOHSYNIANG                      RANGDIKHEW 
##                             826                             598 
##                      RANGJADONG                RANGMAI SONGMONG 
##                             383                             219 
##                      RANGMALGRE                         RANGMAW 
##                             398                            1321 
##                      RANGPHLANG                       RANGSAGRE 
##                             309                             582 
##                      RANGSAKONA                       RANGSHKEN 
##                            1564                            1051 
##                       RANGTHONG                   RANGTHYLLIANG 
##                             776                             554 
##                     RANI JIRANG                        RANIBARI 
##                             437                            1209 
##                         RANIKOR                         RAPLENG 
##                             800                             486 
##                          RASONG                      RATACHERRA 
##                             347                            1165 
##                       RENCHAGRE                  RENE BADIMAGRE 
##                             479                             529 
##                       RENGMAGRE                     RENGRAMPARA 
##                             504                             427 
##                     RENGSINPARA                      RENGSIPARA 
##                             924                             541 
##                        RERAPARA                     RESUBELPARA 
##                             517                           13448 
##                  REWAK SONGMONG                       RIANGMANG 
##                             806                             900 
##                          RIKHEN                          RILONG 
##                             361                             257 
##                 RIMRANG BONEGRE                     RIMRANGPARA 
##                             378                             692 
##                      RIMTONGGRE                       RINGGIGRE 
##                             674                            1001 
##                       RINGREGRE                           RNGAT 
##                             151                             743 
##          RNGIBAH (INC. MAWSHAR)                        RNGIKSEH 
##                             366                             330 
##                      ROCHONPARA                     ROHONPARA-I 
##                             593                             781 
##                  ROMBA ADINGGRE                        ROMBAGRE 
##                             417                             323 
##                          ROMGRE                      ROMPA ASIM 
##                             746                             296 
##                       RONDUPARA                       RONGALGRE 
##                             736                             539 
##       RONGAP MIKILSIMGRE (KERA)                RONGAP SONGGITAL 
##                             413                             337 
##                 RONGARA DOBAKOL               RONGARA RONGTOTMA 
##                             645                             698 
##                      RONGBAKGRE                     RONGBENGGRE 
##                             527                             267 
##             RONGBING BOLDAK (A)                RONGBOK KOSAKGRE 
##                             798                             229 
##                      RONGBOKGRE                  RONGCHADENGGRE 
##                             336                            1155 
##                  RONGCHANDALGRE                     RONGCHEKGRE 
##                             559                             561 
##              RONGCHENG SONGMONG                    RONGCHONGGRE 
##                             120                             583 
##                      RONGCHUGRE                      RONGDIKGRE 
##                             334                             352 
##          RONGJENG AWANGGAGITTIM             RONGJENG BLOCK CAMP 
##                             929                            2389 
##                RONGJENG RESERVE                      RONGKAIGRE 
##                            1215                             301 
##                    RONGKAMINCHI               RONGKON SONGGITAL 
##                             507                            1331 
##                     RONGKONGGRE                 RONGMA PAROMGRE 
##                             701                             287 
##                RONGMA REKMANGRE                       RONGMASEK 
##                             167                             600 
##                  RONGMATCHOKGRE                       RONGMEGRE 
##                             309                             313 
##             RONGMIL GABIL AKAWE                       RONGONGRE 
##                            1831                             432 
##                      RONGPAKGRE                      RONGPETCHI 
##                             419                             733 
##                      RONGRAKGRE                         RONGRAM 
##                             437                            1455 
##                      RONGRAMGRE                  RONGRENG NOKAT 
##                            1170                             264 
##                     RONGRENGPAL               RONGRIBO WATREGRE 
##                             466                             468 
##              RONGRIKIM KILAMPOK                RONGRONG ANTIDAM 
##                             999                             332 
##            RONGRONG BOLSONGCHOK              RONGRONG DAMEBIBRA 
##                             445                             636 
##                     RONGRU ASIM                       RONGSAHEP 
##                             356                             524 
##                         RONGSAI                      RONGSAKGRE 
##                             766                             642 
##                 RONGSANG ABAGRE                RONGSEP ADINGGRE 
##                             701                             635 
##                 RONGSEP KAMAGRE                      RONGSEPGRE 
##                             509                             765 
##                     RONGSU AGAL             RONGSU RONGRIGITTIM 
##                             429                             205 
##                       RONGSUGRE                       RONI ASIM 
##                             468                            1448 
##                          RTIANG                        RTIANG S 
##                             497                             800 
##                    RUGA DONIGRE                   RUGA SONGMONG 
##                             452                             590 
##                         RUMNONG                RYMBAI IAWPYNSIN 
##                             209                            1054 
##           RYMBAI MADAN PYNRIANG                  RYMBAI POHSKUR 
##                             363                             503 
##           RYMBAI SHKEN SHYNRIAH        RYMBAI SYNRANG SHAHKHAIN 
##                             997                             625 
##                RYMBAI WAHSHNONG                    RYNGKU BAZAR 
##                             606                             594 
##                          RYNGUD                          RYNJAH 
##                             570                            5254 
##                           RYNLI                            SABA 
##                             491                             462 
##                    SABAHMUSWANG                       SABANGGRE 
##                            1186                             783 
##                           SADEW                       SADOLPARA 
##                            1053                             896 
##                     SAHSNIANG A                     SAHSNIANG B 
##                            1370                             915 
##                         SAIBUAL                   SAIDEN PROPER 
##                             398                             899 
##                        SAIKARAP                         SAIPUNG 
##                             496                            1222 
##                        SAITSAMA                    SAITSHYLLIAH 
##                            1132                             798 
##                  SAKA BOLDAKGRE                  SAKA BOLDAMGRE 
##                             476                             702 
##                         SAKHAIN                SAKHAIN MOOLIMEN 
##                             432                             478 
##                          SAKMAL                         SAKWANG 
##                             601                             789 
##                     SALBARIPARA                      SALBILLA-I 
##                             693                             788 
##                      SALMANPARA               SAMANDA CHINEMGRE 
##                             791                             724 
##                SAMANDA MEGAPGRE                        SAMANONG 
##                             821                             130 
##                          SAMASI                         SAMATAN 
##                             317                             485 
##                      SAMATIGAON              SAMIN INDIKKIM (B) 
##                             752                             605 
##                 SAMIN RONGALGRE                        SAMINGRE 
##                             466                             441 
##                       SAMPALGRE                          SANARO 
##                            1239                             800 
##                     SANCHONGGRE                        SANDAGRE 
##                             577                             474 
##                      SANDAGRE-A                  SANDONG SONGMA 
##                             292                             293 
##                     SANGKARIGRE                      SANGKNIGRE 
##                             778                            1110 
##                     SANJENGPARA                         SANKHAD 
##                             448                             250 
##                        SANTIPUR                       SAPALGURI 
##                             300                             356 
##                SAPHAI POHRTIANG                       SARIKUSHI 
##                            1637                             693 
##                           SARIN                        SATHEGRE 
##                             344                             446 
##                        SATPATOR                            SDER 
##                             486                             372 
##                       SELBALGRE             SELSELLA AGIPENGGRE 
##                             965                             685 
##               SELSELLA DAMALGRE                SELSELLA PROJECT 
##                             513                             904 
##                       SENTAPARA                      SESENGPARA 
##                            1388                             851 
##               SHAID SHAID-UMOID                      SHAKOIKUNA 
##                             446                             366 
##                     SHANGBANGLA          SHANGPUNG KHLIEHMUCHUT 
##                             391                             669 
##               SHANGPUNG MISSION             SHANGPUNG MOOLIBANG 
##                            1220                             431 
##             SHANGPUNG POHSHNONG           SHANGPUNG POHSHNONG C 
##                            1361                             401 
##                      SHIDAKANDI                 SHILIANG DONGKI 
##                             661                            1124 
##                 SHILIANG JASHAR                 SHILIANGMYNTANG 
##                             430                             512 
##               SHILLIANG UMSHONG                        SHILLONG 
##                             386                           82807 
##                     SHKENPYRSIT                     SHKENTALANG 
##                             529                             477 
##                    SHNGIMAWLEIN                    SHNONGKALONG 
##                             663                             389 
##                      SHNONGPDEI                     SHNONGPDENG 
##                             291                             560 
##                       SHNONGRIM                    SHNONGTHYMME 
##                             682                             494 
##                      SHYAMNAGAR                    SHYNTORBULIA 
##                            1394                             129 
##                        SHYRMANG                       SIATBAKON 
##                             427                             538 
##                SIBBARI GOSEGAON                   SIJU DURAMONG 
##                             756                            1469 
##         SIJU DURAMONG SONGGITAL                  SILCHANGGITTIM 
##                             606                             648 
##                         SILKATA                   SILKI BETAGRE 
##                             811                             885 
##           SILKI CHRISTIANGITTIM                     SIMBUKOLGRE 
##                             787                             704 
##                  SIMSENG BONGGA                   SIMSENG NAKOL 
##                             289                             329 
##                  SIMSENG RONGAL                SINAI MAWSHYNRUT 
##                             266                             257 
##                       SINDILGRE                      SISSOBIBRA 
##                             447                             663 
##                          SKAGRE                            SMIT 
##                             479                            3143 
##                    SNAL DAJRENG                         SNALGRE 
##                             907                             577 
##                        SOBOKGRE                     SOENANG AGA 
##                             325                             219 
##                    SOENANG GARO                          SOHBAR 
##                             722                            1059 
##                         SOHIONG                SOHKHA MISSION A 
##                            1602                             454 
##                SOHKHA MISSION B            SOHKHA MODEL MATHMAT 
##                             498                             251 
##                        SOHKHMIE                        SOHKHWAI 
##                             202                             721 
##                      SOHKHYLLAM                      SOHKYMPHOR 
##                             320                            1965 
##                       SOHKYNDUH               SOHKYRBAM NONGRIM 
##                             469                             484 
##                          SOHLAB                         SOHLIYA 
##                             714                             298 
##                         SOHLWAI                      SOHMYNTING 
##                             452                            1299 
##              SOHMYNTING DONGWAH                         SOHPHOH 
##                             664                            1441 
##                           SOHPI                         SOHPIAN 
##                             288                             965 
##                        SOHRARIM                     SOHRIEWBLEI 
##                             700                             248 
##                     SOHRYNGKHAM                     SOHTYNGKHUR 
##                            3916                             501 
##                 SOKADAM BANGGNA                         SONABIL 
##                             265                             680 
##                         SONAGRE                        SONAMITE 
##                             749                             818 
##                        SONATOLA                  SONGGITCHAMGRE 
##                             700                             486 
##                     SONGJELPARA                    SONGMA ADING 
##                             487                             237 
##                       SONGMEGAP                 SONGSAK AGALGRE 
##                             800                             492 
##                         SONIDAN                         SORAGRE 
##                             773                             367 
##                   SUCHEN THYMME                          SUKTIA 
##                             444                             497 
##                         SULGURI                           SUMER 
##                            1089                             675 
##                       SUNAPYRDI                SUTNGA POHSHNONG 
##                             660                             609 
##      SUTNGA POHSKUL IEW KHYLLAW          SUTNGA POHSKUL MISSION 
##                             699                             608 
##                  SUTNGA WAILONG                     SWER LUMBAH 
##                             502                             841 
##                         SYADHEH               SYNDAI KMAISHNONG 
##                             857                             799 
##                          SYNGKU                        SYNIASYA 
##                             633                             326 
##                  SYNNEI NONGRIM                         SYNTUNG 
##                             277                             572 
##                       TAKIMAGRE                         TAKTAKI 
##                             536                             706 
##                     TAKURANBARI                 TAKURVILLA GARO 
##                             657                             520 
##                      TALLANGGRE                            TAMU 
##                             216                            1218 
##                   TANGABARIPARA                         TANGLEI 
##                             612                             225 
##                        TANGMANG                      TAPRA ALDA 
##                             905                             542 
##                        TARAPARA                           TASKU 
##                             972                             577 
##                   TEBIL BONEGRE                      TEBRONGGRE 
##                             941                             458 
##               TEBRONGGRE SONGMA                      TEKMANPARA 
##                             461                             237 
##                         TELSORA                        TENAKGRE 
##                             333                             184 
##                          TENGRI                       TEWALIGRE 
##                             298                             698 
##                            THAD                          THADAN 
##                             705                             664 
##                       THADBAMON                  THADMUTHLONG A 
##                             673                            1293 
##                  THADMUTHLONG C            THADMUTHLONG PHRAMER 
##                             539                             665 
##                       THADMYNRI                     THADNONGIAW 
##                             892                             572 
##            THADRANG MADANLANGBA                       THADSNING 
##                             881                             591 
##                    THAINTHYNROH                       THANGBNAI 
##                            1503                             376 
##                     THANGBULI A                     THANGBULI B 
##                             525                             482 
##                        THANGMAW                        THANGRAI 
##                             587                             242 
##                       THANGRAIN                     THANGSHALAI 
##                            1462                             328 
##                      THANGSNING                     THANGTHRING 
##                            1345                             536 
##                  THAPA AGITCHAK                    THAPA DANGRE 
##                             843                             695 
##                  THAPA DARENCHI                   THAPA SEPIKOL 
##                             650                             557 
##                       THIBAPARA              THIEDDIENG NONGBAH 
##                             956                             364 
##                          THURUK                         THYLLAW 
##                             706                             474 
##                        THYNROIT                         TIEHBAH 
##                            1933                             351 
##                     TIEHNONGBAH                        TIEHWIEH 
##                             919                             283 
##                      TIKRIKILLA                        TILAGOAN 
##                            1593                             166 
##                        TLANGPUI                      TLONGPLENG 
##                             318                             700 
##                            TLUH                            TMAR 
##                             893                            1703 
##                       TOCHAPARA                         TOLEGRE 
##                             255                             575 
##                 TOMONPO ANGLONG                      TONGBOLGRE 
##                             344                             425 
##               TONGSENG (NARPUH)               TONGSENG (SUTNGA) 
##                             799                             782 
##              TRANGBLANG MISSION                TUBER KMAISHNONG 
##                             546                            1190 
##                TUBER SHOHSHRIEH                         TUM TUM 
##                             677                            1164 
##                     TUNGRURCHAR                            TURA 
##                            1569                           45288 
##                    TWAH-U-SDIAH                        TYNGNGER 
##                             257                             801 
##                        TYNRIANG                         TYNRING 
##                             202                            1519 
##                           TYRNA                          TYRSAD 
##                             857                            1160 
##                        TYRSHANG                           TYRSO 
##                             870                             828 
##                        UJENGGRE                           UMBIR 
##                             886                             627 
##                          UMBLAI                     UMDAP RANGI 
##                             172                             232 
##                       UMDEINLIN                      UMDEN ARKA 
##                             530                             664 
##                   UMDEN MISSION                  UMDEN NONGTLUH 
##                             345                             901 
##                      UMDIENGPOH                         UMDIHAR 
##                             305                             757 
##                         UMDIKER                    UMDOHBYRTHIH 
##                            1245                             640 
##               UMDOHKHA NONGTLUH                        UMDOHLUN 
##                             598                             527 
##                          UMDUBA                           UMEIT 
##                             585                             375 
##                UMEIT MAWLYNGBNA                           UMIAM 
##                             943                             940 
##             UMIAM PROJECT SUMER                        UMIARONG 
##                             517                             380 
##                          UMIONG                        UMJAKOIT 
##                             240                             752 
##                      UMJALISIAW                        UMJARAIN 
##                             600                             586 
##                        UMJARASI                          UMJARI 
##                             593                             477 
##                         UMKADUH                           UMKEI 
##                             795                             535 
##                           UMKET                        UMKHABAW 
##                             569                             756 
##                         UMKIANG                          UMKLAI 
##                            1957                             402 
##                           UMKON                           UMKRA 
##                             807                             378 
##                          UMKREM                         UMKTIEH 
##                            1171                             594 
##                       UMKYNSIER                       UMKYRPONG 
##                             738                             520 
##                        UMLADANG                       UMLADKHUR 
##                             885                             674 
##                       UMLAITENG                        UMLAKHAR 
##                             456                             425 
##                       UMLANGPUR                      UMLANGSHOR 
##                             279                             853 
##                         UMLAPER                          UMLING 
##                             576                             941 
##                 UMLING LAMBRANG                        UMLYNGKA 
##                             263                            4319 
##                     UMLYNGKDAIT                           UMMAR 
##                             767                             331 
##                           UMMIR                      UMMULONG A 
##                             124                             553 
##                      UMMULONG B              UMMULONG LUMKYNSAW 
##                            1364                             621 
##                          UMNIUH                        UMPATHAW 
##                             302                             331 
##                          UMPDEM                        UMPHIENG 
##                             558                             170 
##                         UMPHREW                         UMPHRUP 
##                             231                            1251 
##                       UMPHYRNAI                         UMPLING 
##                            1915                            4301 
##                   UMPOWIN PDENG                          UMPUNG 
##                             428                             652 
##                        UMRALENG                        UMRALING 
##                             477                             267 
##                     UMRAN DAIRY               UMRAN NIANGBYRNAI 
##                            1020                             619 
##                  UMRANG NONGBAH                           UMRIT 
##                             618                             538 
##                        UMRYNJAH           UMSAITSNING NONGPDENG 
##                             490                             540 
##                 UMSAKHLAWMYRIAW                        UMSALAIT 
##                             431                             688 
##                        UMSALANG                        UMSAMLEM 
##                             173                             610 
##                         UMSATAI                           UMSAW 
##                             616                            1644 
##                     UMSAW (WAR)                  UMSAW MAWTAWAR 
##                             529                             395 
##                   UMSAW NONGBRI                        UMSAWLUM 
##                             707                            1146 
##                       UMSAWRANG                      UMSAWRIANG 
##                            1059                             380 
##                           UMSEN                        UMSHAKEN 
##                             550                             571 
##                         UMSHIAW               UMSHING MAWKYNROH 
##                             780                            1860 
##                     UMSHOHPHRIA                  UMSIANG MAIONG 
##                             348                             646 
##                         UMSNING                 UMSNING PATARIM 
##                             377                             757 
##                UMSNING PROPER A               UMSNING UMSOHLANG 
##                             793                             441 
##                        UMSOHBAR                       UMSOHLAIT 
##                             394                             813 
##                         UMSOHMA                      UMSOHMATAN 
##                             151                             368 
##                      UMSOHPANAN                          UMSONG 
##                             510                             713 
##                         UMSYIEM                            UMTA 
##                             536                             260 
##                      UMTANGLING                UMTASOR MAWDKHAR 
##                             299                             799 
##                          UMTHLI                        UMTHLONG 
##                             710                            1338 
##                          UMTHLU                         UMTNGAM 
##                             408                             651 
##                          UMTONG                          UMTRAI 
##                             344                             541 
##                          UMTREW                          UMTUNG 
##                             528                             594 
##                        UMTYNGAR                      UMTYRKHANG 
##                             449                             365 
##                        UMTYRNGA                       UMTYRNIUT 
##                            1388                             471 
##                           UMWAI                          UMWANG 
##                             474                             344 
##              UPPER CHIGIJANGGRE                  UPPER DAMALGRE 
##                             622                             999 
##                  UPPER DARENGRE                   UPPER HARIPUR 
##                             948                             535 
##                   UPPER KHAMARI                UPPER KONGRAPARA 
##                            1592                            1260 
##                 UPPER MANIKGANJ                 UPPER NOGOLPARA 
##                             944                             808 
##              UPPER NONGBAK APAL                  UPPER REMBIGRE 
##                            1114                             702 
##                UPPER RONGDOTCHI                  UPPER RONGJENG 
##                             265                             720 
##                  UPPER SASATGRE                     UPPER UMSIH 
##                             607                             748 
##               UPPER WATREGRE(B)                        URINGGRE 
##                             638                             680 
##                URKSEW-WAHPATHAW                    URMASI-U-JOH 
##                             828                             631 
##                      WADAGOKGRE                     WADRO WATRE 
##                             777                             419 
##                 WAGE CHIRINGGRE                    WAGEGITOKGRE 
##                             648                             658 
##                        WAGOPGRE                       WAH-U-TIM 
##                             907                             130 
##               WAHIAJER (NARPUH)                      WAHIAJER A 
##                             719                             463 
##                      WAHIAJER B                      WAHIAJER C 
##                             450                             580 
##                      WAHIAJER D           WAHIAJER LUMBHAHDAKHA 
##                             520                             994 
##                     WAHIAJER RC                        WAHJAREM 
##                             883                             121 
##                         WAHKAJI                       WAHKALIAR 
##                             409                             266 
##                        WAHKDAIT                         WAHKHEN 
##                             544                             876 
##                      WAHLAKHIAT              WAHLANG INC.JARAIN 
##                             616                             569 
##                      WAHLYNGDOH                     WAHLYNGKHAT 
##                             293                             796 
##                       WAHMAWPAD                           WAHRA 
##                             922                             217 
##                        WAHRAHAW                      WAHRAMKHAR 
##                             590                             110 
##                          WAHRIT                         WAHSIEJ 
##                             365                             530 
##                        WAHSOHRA               WAHSYNON(NONGDOM) 
##                             438                             520 
##                       WAHUMLEIN                       WAJATAGRE 
##                             305                             698 
##                      WAKANTAGRE                  WAKRINGTONGGRE 
##                             477                             450 
##                   WANKOLA DAKOP           WANKOLAGRE(KALAJAR I) 
##                             906                             493 
##                   WAPUNG SHNONG                     WAPUNG SKUR 
##                            1288                            1671 
##                         WAR-WAR                    WARAM SONGMA 
##                             285                             511 
##                      WARIBOKGRE                       WARIMAGRE 
##                             413                             884 
##                       WARMAWSAW                        WATREGRE 
##                             955                             608 
##                    WATREGRE (A)                      WEILYNGKUT 
##                             682                             787 
##                      WEIMYNSIER                  WEST RANGASORA 
##                             271                             759 
##                    WILLIAMNAGAR                          ZIKZAK 
##                           16302                            1709
```
