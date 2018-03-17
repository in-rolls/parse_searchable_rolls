## Nagaland

Basic descriptive statistics about the data. And sanity checks.


```r
nagaland <- readr::read_csv("nagaland.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_character(),
##   number = col_integer(),
##   age = col_integer(),
##   part_no = col_integer(),
##   year = col_integer(),
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
nrow(nagaland)
```

```
## [1] 1140776
```

Unique Values in Sex:


```r
# Unique values in sex
table(nagaland$sex)
```

```
## 
## Female   Male 
## 565287 575489
```

Summary of Age:


```r
# Age
summary(nagaland$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##   19.00   30.00   38.00   41.58   51.00  328.00       1
```

Check if 0 and missing age is from problem in the electoral roll:


```r
nagaland[which(nagaland$age == 1), c("id", "filename")]
```

```
## # A tibble: 0 x 2
## # ... with 2 variables: id <chr>, filename <chr>
```

No. of characters in ID:

```r
# Length of ID
table(nchar(nagaland$id))
```

```
## 
##       4       5       6       7       8      10      11 
##     274    1118     281      25       3 1109941       2
```

Number of characters in pin code:


```r
table(nchar(nagaland$pin_code))
```

```
## < table of extent 0 >
```

Are IDs duplicated?


```r
length(unique(nagaland$id))
```

```
## [1] 1110518
```

```r
nrow(nagaland)
```

```
## [1] 1140776
```


```r
# Net electors
sum(with(nagaland, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 1140776
```

```r
nrow(nagaland)
```

```
## [1] 1140776
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(nagaland$elector_name))
```

```
## 
##      1      2      3      4      5      6      7      8      9     10 
##      1     10   5503  40801  92214 171263 175192 143053 114617  93155 
##     11     12     13     14     15     16     17     18     19     20 
##  70917  57625  45766  36372  28787  21860  15445  10844   7203   4504 
##     21     22     23     24     25     26     27     28     29     30 
##   2561   1432    728    391    204    137     90     43     21     20 
##     31     32     33     34 
##     11      1      4      1
```

```r
nagaland[which(nchar(nagaland$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 5,514 x 2
##    id         filename        
##    <chr>      <chr>           
##  1 GVZ0562942 AC007PART057.pdf
##  2 FKQ0221614 AC016PART001.pdf
##  3 FKQ0222323 AC016PART001.pdf
##  4 FKQ0222729 AC016PART001.pdf
##  5 FKQ0223164 AC016PART001.pdf
##  6 FKQ0224022 AC016PART001.pdf
##  7 FKQ0224170 AC016PART001.pdf
##  8 FKQ0224337 AC016PART001.pdf
##  9 JPS0334466 AC006PART012.pdf
## 10 HQZ0483370 AC012PART009.pdf
## # ... with 5,504 more rows
```

Does district have a number?

```r
sum(grepl('[0-9]', nagaland$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(nagaland$parl_constituency)
```

```
## 
## 1 , NAGALAND (General)      1 , NAGALAND (ST) 
##                1113317                  27459
```

```r
table(nagaland$ac_name)
```

```
## 
## (General)      (ST) 
##     21881   1118895
```

```r
table(nagaland$police_station)
```

```
## 
##              ABOI          AGHUNATO           AKULUTO            ATOIZU 
##             10924             14589              8631             15301 
##          BHANDARI         CHANGPANG       CHANGTONGYA          CHAZOUBA 
##             17942              2935             16507             26984 
##         CHEN TOWN      DIMAPUR EAST DIMAPUR SUB-URBAN      DIMAPUR WEST 
##              9625             78895             20017             25530 
##          DIPHUPAR         GHATHASHI           KHUZAMA           KIPHIRE 
##             52656              6307             30219             47693 
##          KOBULONG      KOHIMA NORTH      KOHIMA SOUTH          LONGKHIM 
##              9557             43293             37734             30374 
##  LONGLENG & TAMLU       MANGKOLEMBA        MEDZIPHEMA            MELURI 
##             37362             25139             16840             12126 
##    MOKOKCHUNG - 1    MOKOKCHUNG - 2          MON TOWN        NAGINIMORA 
##             27114             36451             31509             13876 
##            NOKLAK       P.S.JALUKIE         P.S.PEREN          PFUTSERO 
##             20506             12514             41836             39908 
##              PHEK    PHOMCHING TOWN         PUGHOBOTO             RALAN 
##             19859             15601              6655              3959 
##             SANIS           SATAKHA          SHAMATOR            SUNGRO 
##             13086             15662             28206              7561 
##          SURUHUTO             TIZIT         TOBU TOWN          TSEMINYU 
##             13993             14370             31614             23952 
##          TUENSANG              TULI             WOKHA         ZUNHEBOTO 
##             34915             18081             50964             19988
```

```r
table(nagaland$mandal)
```

```
## 
##                      .               AGHUNATO              AITEPYONG 
##                   3708                  14589                   4666 
##                AKULUTO               ATHIBUNG                 ATOIZU 
##                   8631                  12170                  15301 
##               BHANDARI              CHANGPANG                  CHARE 
##                  15511                    211                   8280 
##               CHAZOUBA           CHEIPHOBOZOU      CHEN SUB-DIVISION 
##                  27340                  20452                  20406 
##               CHESSORE                CHIZAMI              CHUKITONG 
##                   7558                   7921                   6103 
##            DHANSIRIPAR        DIMAPUR - SADAR                JAKHAMA 
##                  18912                 125813                  30219 
##                JALUKIE        KIPHIRE - SADAR         KOHIMA - SADAR 
##                  11469                  19817                  50626 
##               KUHOBOTO               LONGKHIM               LONGLENG 
##                  14349                  11803                  37362 
##            MANGKOLEMBA             MEDZIPHEMA                 MELURI 
##                  25139                  19884                  12126 
##     MOKOKCHUNG - SADAR                    MON                NIULAND 
##                  71052                  30983                  14980 
##                 NOKLAK                 NOKSEN                  NSONG 
##                  20506                  10291                   3234 
##                  PEREN               PFUTSERO           PHEK - SADAR 
##                  15237                  31987                  19503 
## PHOMCHING SUB-DIVISION              PUGHOBOTO                 PUNGRO 
##                  15601                  12962                  12718 
##                  RALAN                  SANIS                SATAKHA 
##                   4448                  20647                  15662 
##          SECHU (ZUBZA)               SHAMATOR                 SITIMI 
##                   9949                  10256                  15158 
##               SURUHOTO                 TENING              THONOKNYU 
##                  13993                  12240                  12200 
##     TIZIT SUB-DIVISION      TOBU SUB-DIVISION               TSEMINYU 
##                  14370                  31614                  23952 
##       TUENSANG - SADAR                   TULI  WAKCHING SUB-DIVISION 
##                  33107                  32950                  14545 
##          WOKHA - SADAR                WOZHURO              ZUNHEBOTO 
##                  39579                   5282                  19988
```

```r
table(nagaland$district)
```

```
## 
##     COLONY    DIMAPUR    KIPHIRE     KOHIMA   LONGLENG MOKOKCHUNG 
##        770     192859      47693     133861      37662     132849 
##        MON        NAP      PEREN       PHEK  PUGHOBOTO   TUENSANG 
##     127519        675      54350      98877      12962     113335 
##    VILLAGE      WOKHA  ZUNHEBOTO 
##        309      96447      88164
```

```r
table(nagaland$main_town)
```

```
## 
##                            0504000000000033R 
##                                          561 
##                       7th MILE MODEL VILLAGE 
##                                          309 
##                             7TH MILE VILLAGE 
##                                          308 
##                        A.G. COLONY (UPPER-I) 
##                                          888 
##                        A.G.COLONY (UPPER-II) 
##                                          684 
##                          A.G.COLONY(LOWER-I) 
##                                          964 
##                         A.G.COLONY(LOWER-II) 
##                                          850 
##                                  A/SAGHEMI N 
##                                          517 
##                                  A/SAGHEMI S 
##                                          857 
##                                     ABOI HQ. 
##                                         2069 
##                                ACHIKUCHU (A) 
##                                          566 
##                                     AGHULIMI 
##                                          346 
##                                     AGHUNATO 
##                                          770 
##                                 AGHUNATO PWD 
##                                          558 
##                                AGHUNATO TOWN 
##                                          527 
##                                   AGHUYILIMI 
##                                          232 
##                                     AGHUYITO 
##                                          152 
##                                    AGRI FARM 
##                                          590 
##                        AGRI WARD-5, LONGLENG 
##                                          380 
##                    AGRI/ ELECTRICAL COLONIES 
##                                          861 
##                         AGRI/ELECTRICAL - II 
##                                          588 
##                                    AHTHIBUNG 
##                                          998 
##                                  AIRFIELD AO 
##                                          909 
##                                    AITEPYONG 
##                                          210 
##                                       AIZUTO 
##                                          209 
##                              AJIQAMI VILLAGE 
##                                          227 
##                                      AKHAKHU 
##                                          593 
##                              AKHEGOW VILLAGE 
##                                          649 
##                                AKHEN VILLAGE 
##                                           66 
##                                       AKHOIA 
##                                          782 
##                                      AKUBA A 
##                                          306 
##                                      AKUBA B 
##                                          101 
##                                    AKUHAIQUA 
##                                          199 
##                                     AKUHAITO 
##                                          336 
##                                     AKUK NEW 
##                                          185 
##                                 AKUK OLD-III 
##                                          685 
##                               AKUK OLD - III 
##                                          868 
##                                 AKUK OLD – I 
##                                          725 
##                                AKUK OLD – II 
##                                          821 
##                                 AKULUTO TOWN 
##                                         1885 
##                                       AKUMEN 
##                                          285 
##                                      ALAHUTO 
##                                         2792 
##                                     ALAPHUMI 
##                                          535 
##                                      ALAYONG 
##                                          304 
##               ALEMPANG WARD I (C-II) N/ WING 
##                                          998 
##              ALEMPANG WARD II (C-II) S/ WING 
##                                          718 
##                                        ALIBA 
##                                          769 
##                                    ALICHEN I 
##                                          820 
##                                   ALICHEN II 
##                                          729 
##                                  ALICHEN III 
##                                          856 
##                                   ALICHEN IV 
##                                          672 
##                                      ALIKHUM 
##                                          145 
##                                     ALISOPUR 
##                                         1588 
##                              ALISOPUR N - II 
##                                          591 
##                                    ALONGCHEN 
##                                          264 
##                                    ALONGKIMA 
##                                          238 
##                                ALONGMEN WARD 
##                                          662 
##                                    ALONGTAKI 
##                                          167 
##             ALUMINIUM FACTORY, NAGALAND GATE 
##                                          487 
##                             AMAHATOR VILLAGE 
##                                          825 
##                                      AMALUMA 
##                                          558 
##                                       AMBOTO 
##                                          202 
##                                     AMIPHOTO 
##                                          999 
##                               AMOSEN VILLAGE 
##                                          288 
##                                        ANAKI 
##                                          539 
##                                      ANAKI C 
##                                          271 
##                                 ANAKI YIMSEN 
##                                          339 
##                            ANATONGER VILLAGE 
##                                          818 
##                          ANATONGER VILLAGE A 
##                                          495 
##                                     ANGANGBA 
##                                          678 
##                                   ANGANGBA B 
##                                          786 
##                          ANGJANGYANG VILLAGE 
##                                          364 
##                           ANGPHANG VILLAGE A 
##                                          924 
##                           ANGPHANG VILLAGE B 
##                                          855 
##                           ANGPHANG VILLAGE C 
##                                          922 
##                           ANGPHANG VILLAGE D 
##                                          884 
##                           ANGPHANG VILLAGE E 
##                                          959 
##                                     ANYAKSHU 
##                                          286 
##                                    AO-SETTSU 
##                                          336 
##                       AO / LOTHA CHURCH AREA 
##                                          461 
##                                     AO NOKPU 
##                                          240 
##                                      AOCHING 
##                                          424 
##                            AOKUM & TSUTAPELA 
##                                          114 
##                                      AOLIJEN 
##                                          557 
##                          AONGZA WARD N/ WING 
##                                          995 
##                                AONOKPUYIMSEN 
##                                          120 
##                                AOPAO VILLAGE 
##                                          639 
##                                      AOPENZU 
##                                          318 
##                                     AOSENDEN 
##                                          127 
##                                    AOSUNGKUM 
##                                          103 
##                             AOYIMKUM VILLAGE 
##                                          915 
##                         APAO CHANGLE VILLAGE 
##                                          123 
##                                       APOIJI 
##                                          123 
##                                     AREE NEW 
##                                          271 
##                                     AREE OLD 
##                                          603 
##                        ARKONG WARD E N/ WING 
##                                          920 
##                        ARKONG WARD E S/ WING 
##                                          600 
##                                  ARTANG WARD 
##                                          703 
##                                ARTANG WARD I 
##                                          777 
##                                      ASANGMA 
##                                          872 
##                                        ASHAA 
##                                           99 
##                                     ASUKHOMI 
##                                          679 
##                                   ASUKHOMI-B 
##                                          268 
##                             ASUKHUTO VILLAGE 
##                                          127 
##                                      ASUKIQA 
##                                           74 
##                                   ASUTO TOWN 
##                                          374 
##                               ATHIBUNG (S/W) 
##                                          895 
##                                    ATHUPHUMI 
##                                          165 
##                                       ATOIZU 
##                                          799 
##                              AVANKHU VILLAGE 
##                                           80 
##                                      AWOHUMI 
##                                          239 
##                                 AWOTSAKILIMI 
##                                          617 
##                                     AZAILONG 
##                                          794 
##                                AZETO VILLAGE 
##                                           86 
##                                      AZUHOTO 
##                                           76 
##                                  B-NAMSANG C 
##                                          237 
##                                  B/NAMSANG A 
##                                          302 
##               B/NAMSANG A KONGSHONG COMPOUND 
##                                          421 
##                                  B/NAMSANG B 
##                                          746 
##                                         BADE 
##                                          600 
##                                   BAGHTY – A 
##                                          613 
##                                   BAGHTY – B 
##                                          921 
##                                BAGHTY HQ - I 
##                                          648 
##                                       BAIMHO 
##                                          453 
##                         BAMAN PUKHURI I & II 
##                                          861 
##                                  BAMSIAKILWA 
##                                          170 
##                                  BANK COLONY 
##                                          752 
##                         BAYAVU HILL /SEPFUZU 
##                                          591 
##                            BAYAVU HILL LOWER 
##                                          686 
##                       BAYAVU HILL LOWER - II 
##                                          544 
##                           BAYAVU HILL MIDDLE 
##                                          679 
##                               BAZAR SECTOR A 
##                                          692 
##                               BAZAR SECTOR B 
##                                          627 
##                               BAZAR SECTOR C 
##                                          719 
##                               BAZAR SECTOR D 
##                                          714 
##                                 BEISUMPUIKAM 
##                                          991 
##                                 BEISUMPUILOA 
##                                           75 
##                                       BENREU 
##                                          520 
##                            BHANDARI TOWN – I 
##                                          803 
##                           BHANDARI TOWN – II 
##                                          768 
##                             BHANDARI VILLAGE 
##                                          293 
##                             BHANDHARI HQ III 
##                                          746 
##                              BHANDHARI HQ IV 
##                                          827 
##                                    BHUMNYU A 
##                                          255 
##                      BHUMNYU B MEISHA MORUNG 
##                                          393 
##                                    BHUMNYU C 
##                                          220 
##                                      BHUMPAK 
##                                          262 
##                       BILONGKYU VILLAGE (UR) 
##                                          146 
##                                 BONGKOLONG I 
##                                          634 
##                                     BOTANBOU 
##                                           92 
##                                        BOTSA 
##                                          653 
##                                BUMEI VILLAGE 
##                                          342 
##                                     BUNGSANG 
##                                          607 
##                            C.GOCHING VILLAGE 
##                                          625 
##                                       CHAKPA 
##                                          999 
##                                        CHAMI 
##                                           95 
##                              CHANDALASHUNG B 
##                                          159 
##                            CHANDALASHUNG NEW 
##                                          399 
##                            CHANDALASHUNG OLD 
##                                          139 
##                            CHANDMARI (LOWER) 
##                                          952 
##                           CHANDMARI (MIDDLE) 
##                                          607 
##                          CHANDMARI (UPPER-I) 
##                                          655 
##                         CHANDMARI (UPPER-II) 
##                                          689 
##                        CHANDMARI (UPPER-III) 
##                                          756 
##                           CHANGCHORE VILLAGE 
##                                          753 
##                                    CHANGDANG 
##                                          359 
##                                    CHANGKI I 
##                                          703 
##                                   CHANGKI II 
##                                          583 
##                                  CHANGKI III 
##                                          506 
##                               CHANGLANGSHU A 
##                                         2552 
##                               CHANGLANGSHU B 
##                                          294 
##                CHANGLANGSHU CHANGSHA VILLAGE 
##                                          200 
##                              CHANGLU VILLAGE 
##                                          244 
##                             CHANGNYU VILLAGE 
##                                          567 
##                                    CHANGPANG 
##                                          449 
##                           CHANGPANG ADM. HQ. 
##                                          211 
##                                  CHANGSU NEW 
##                                          821 
##                                CHANGSU OLD I 
##                                         1225 
##                               CHANGSU OLD II 
##                                          877 
##                      CHANGTONGYA STATION - V 
##                                          713 
##                     CHANGTONGYA STATION - VI 
##                                          827 
##                             CHANGTONGYA TOWN 
##                                         3638 
##                          CHANGTONGYA YIMCHEN 
##                                          465 
##                    CHANGTONGYA YIMCHEN - III 
##                                          435 
##        CHANGTONGYA YIMCHEN LONGZUNG MEPU (I) 
##                                          647 
##                                       CHANKA 
##                                           73 
##                              CHAOCHACHINGNYU 
##                                          537 
##                              CHAOHA CHINGLEN 
##                                          136 
##                               CHAOHACHINGNYU 
##                                          526 
##                                 CHARE HQ.NEW 
##                                          992 
##                                 CHARE HQ.OLD 
##                                          455 
##                                 CHARE VILL A 
##                                          922 
##                                 CHARE VILL B 
##                                          713 
##                                      CHASSIR 
##                                          383 
##                        CHAZOUBA TOWN A/ WING 
##                                          508 
##                        CHAZOUBA TOWN B/ WING 
##                                          901 
##                         CHAZOUBA TOWN C-WING 
##                                          465 
##                     CHAZOUBA VILLAGE A/ WING 
##                                          593 
##                     CHAZOUBA VILLAGE B/ WING 
##                                          624 
##                      CHAZOUBA VILLAGE C-WING 
##                                          557 
##                                      CHEDEMA 
##                                          988 
##                        CHEDEMA MODEL VILLAGE 
##                                          204 
##                                    CHEKIYE A 
##                                         1070 
##                                    CHEKIYE B 
##                                          653 
##                                     CHEN HQ. 
##                                          510 
##                              CHENDANG SADDLE 
##                                          411 
##                             CHENDANG VILLAGE 
##                                          519 
##                           CHENLOISHO VILLAGE 
##                                         2246 
##                             CHENMOHO VILLAGE 
##                                         2170 
##                                   CHENWETNYU 
##                                         1019 
##                            CHEPOKETA VILLAGE 
##                                          601 
##                         CHESEZU NASA VILLAGE 
##                                          229 
##                          CHESEZU VILLAGE A/W 
##                                          624 
##                      CHESEZU VILLAGE B/ WING 
##                                          700 
##                       CHESEZU VILLAGE C-WING 
##                                          591 
##                       CHESEZU VILLAGE D-WING 
##                                          608 
##                                 CHESSORE HQ. 
##                                          502 
##                         CHESSORE VILLAGE (A) 
##                                          697 
##                         CHESSORE VILLAGE (B) 
##                                          574 
##                           CHESSORE VILLAGE C 
##                                          884 
##                                CHETHEBA TOWN 
##                                          932 
##                               CHIECHAMA BASA 
##                                          999 
##                               CHIECHAMA BAWE 
##                                          727 
##                             CHIECHAMA PHELUO 
##                                          553 
##                           CHIECHAMA PHESAZOU 
##                                          664 
##                                 CHIEPHOBOZOU 
##                                          944 
##                                  CHIKIPONGER 
##                                          230 
##                                     CHILLISO 
##                                          385 
##                                  CHIMONGER D 
##                                          602 
##                                  CHIMONGER E 
##                                          170 
##                          CHIMONGER VILLAGE A 
##                                          752 
##                          CHIMONGER VILLAGE B 
##                                          994 
##                          CHIMONGER VILLAGE C 
##                                          735 
##                          CHINGAI WARD MON HQ 
##                                          953 
##                     CHINGKANG SAKSHI VILLAGE 
##                                          187 
##                             CHINGKAO CHINGHA 
##                                          522 
##                            CHINGKAO CHINGNYU 
##                                         1263 
##                       CHINGKAO NYAHO VILLAGE 
##                                          120 
##                            CHINGLANG VILLAGE 
##                                         1120 
##                            CHINGLONG VILLAGE 
##                                          966 
##                                     CHINGMEI 
##                                         1347 
##                                   CHINGMELEN 
##                                          651 
##                                 CHINGMELEN B 
##                                          647 
##                                     CHINGONG 
##                                          236 
##                            CHINGPHOI VILLAGE 
##                                          464 
##                            CHINGTANG VILLAGE 
##                                          669 
##                                       CHIPUR 
##                                          891 
##                                   CHISHILIMI 
##                                          579 
##                                   CHISHOLIMI 
##                                          375 
##                             CHIZAMI NEW TOWN 
##                                          536 
##                                 CHIZAMI TOWN 
##                                          503 
##                       CHIZAMI VILLAGE A/WING 
##                                          416 
##                       CHIZAMI VILLAGE B/WING 
##                                          673 
##                       CHIZAMI VILLAGE C-WING 
##                                          317 
##                           CHOKLANGAN VILLAGE 
##                                          998 
##                              CHOKNYU VILLAGE 
##                                          653 
##                              CHOSABA VILLAGE 
##                                          120 
##                             CHOTOBOSTI LOWER 
##                                         1350 
##                             CHOTOBOSTI UPPER 
##                                          310 
##                       CHOZUBA VILLAGE C/WING 
##                                          684 
##                                  CHUBAYIMKUM 
##                                          130 
##                              CHUCHU COMPOUND 
##                                          835 
##                            CHUCHU COMPOUND I 
##                                          803 
##                                CHUCHUYIMLANG 
##                                         3972 
##                CHUCHUYIMLANG-VLENDIKONG MEPU 
##                                          667 
##                            CHUCHUYIMPANG-III 
##                                          805 
##            CHUCHUYIMPANG I CHANGCHANG LENDEN 
##                                          790 
##                     CHUCHUYIMPANG II N/ WING 
##                                          776 
##                                        CHUDI 
##                                          781 
##                                 CHUI VILLAGE 
##                                         1056 
##                                    CHUKITONG 
##                                         1111 
##                       CHUMUKEDIMA BL-III S/W 
##                                          450 
##                          CHUMUKEDIMA VILLAGE 
##                                        11469 
##                           CHUNGLIYIMSEN VILL 
##                                          254 
##                               CHUNGLIYIMTI A 
##                                          193 
##                               CHUNGLIYIMTI B 
##                                          314 
##                                 CHUNGTIA-III 
##                                          813 
##                                   CHUNGTIA I 
##                                          751 
##                                  CHUNGTIA II 
##                                          720 
##                               CHUNGTIAYIMSEN 
##                                          999 
##                                     CHUNGTOR 
##                                         1352 
##                                     CHUNLIKA 
##                                          695 
##                          CHURCH ROAD RAJBARI 
##                                          186 
##                             CIDEVONG VILLAGE 
##                                          113 
##                           CIRCUIT HOUSE AREA 
##                                          933 
##                   CIRCULAR ROAD BISHOP HOUSE 
##                                          248 
##                          D.BLOCK - I (UPPER) 
##                                          294 
##                        D.BLOCK - II (MIDDLE) 
##                                          457 
##                              D.BLOCK (LOWER) 
##                                          597 
##                                 D.C. HIL S/W 
##                                         1381 
##                                D.C. HILL N/W 
##                                          941 
##                                       D.KHEL 
##                                         1695 
##                                    DAKLANE-1 
##                                          390 
##                                   DAKLANE-II 
##                                          406 
##                           DAKLANE SECTOR-III 
##                                          352 
##                                  DAN VILLAGE 
##                                          130 
##                               DANIEL VILLAGE 
##                                          212 
##                                    DAROGAJAN 
##                                          759 
##                              DELIEZHU COLONY 
##                                          996 
##                                    DEUKWARAM 
##                                          208 
##                             DHANSIRIPAR TOWN 
##                                          750 
##                          DHANSIRIPAR VILLAGE 
##                                          646 
##                            DHEP (NORTH BANK) 
##                                          406 
##                                       DIBUIA 
##                                          612 
##                                     DIEZEPHE 
##                                          431 
##                                       DIHOMA 
##                                          844 
##                              DILONG WARD I D 
##                                          807 
##                             DILONG WARD II D 
##                                          816 
##                                   DIPHUPAR A 
##                                          885 
##                              DIPHUPAR B KHEL 
##                                          812 
##                           DIPHUPAR B VILLAGE 
##                                         1713 
##                       DIPHUPAR B VILLAGE E/W 
##                                          756 
##                       DIPHUPAR B VILLAGE W/W 
##                                          717 
##                          DIPHUPAR C & D KHEL 
##                                          577 
##                       DIPHUPAR C, D & H KHEL 
##                                          932 
##                              DIPHUPAR E KHEL 
##                                          486 
##                              DIPHUPAR G KHEL 
##                                          642 
##                                    DISAGAPHU 
##                                          214 
##     DISTRICT EXECUTIVE FORCE COLONY (CHUCHU) 
##                                          324 
##                                     DOBAGAON 
##                                          482 
##                                 DOROGAPATHAR 
##                                         1112 
##                      DOYANG DHEP, SOUTH BANK 
##                                          546 
##                                      DOYAPUR 
##                                         1061 
##                           DUNCAN BASTI B S/W 
##                                          497 
##                                 DUNCAN BOSTI 
##                                          376 
##                               DUNCAN BOSTI B 
##                                          252 
##                               DUNCAN VILLAGE 
##                                          446 
##                             DUNCAN VILLAGE A 
##                                          315 
##                            DUNGKHAO COMPOUND 
##                                          236 
##                                       DUNGKI 
##                                          376 
##                                 DUNGKI (S/W) 
##                                          481 
##                                       DZUDZA 
##                                           50 
##                                    DZULAKEMA 
##                                          119 
##                     DZULHAMI VILLAGE A/ WING 
##                                          804 
##                     DZULHAMI VILLAGE B/ WING 
##                                          521 
##                      DZULHAMI VILLAGE C-WING 
##                                          461 
##                                       EHUNNA 
##                                          589 
##                                     EKHYOYAN 
##                                          334 
##                                 EKRANIPATHAR 
##                                          558 
##                  ELECTRICAL COLONY LONGWIRAM 
##                                         1185 
##                               ELUMYO VILLAGE 
##                                         1004 
##                                      EMULOMI 
##                                          352 
##                                       ENGLAN 
##                                          319 
##                    ENHULUMI VILLAGE (YOSUBA) 
##                                          637 
##                                    ERALIBILL 
##                                          916 
##                     EROS LINE, GOLAGHAT ROAD 
##                                          264 
##                               EYEANG VILLAGE 
##                                          323 
##                                FAKIM VILLAGE 
##                                          232 
##                                FOREST COLONY 
##                                          445 
##                FOREST PLANTATION SIGNAL SEMA 
##                                          568 
##                                        GAILI 
##                                          804 
##                                  GAILI NAMDI 
##                                          130 
##                                 GANESH NAGAR 
##                                          439 
##                                    GARIPHEMA 
##                                          777 
##                               GARIPHEMA BASA 
##                                           78 
##                                    GAURILANE 
##                                          346 
##                                    GHATHASHI 
##                                          527 
##                                     GHOKHUVI 
##                                          591 
##                                      GHOKIMI 
##                                          481 
##                                 GHOKIMI - II 
##                                          370 
##                                     GHOKISHE 
##                                          219 
##                                      GHOKUTO 
##                                          230 
##                              GHOTOVI VILLAGE 
##                                          230 
##                                     GHUKHUYI 
##                                          191 
##                                      GHUKITO 
##                                          643 
##                                     GHUVISHE 
##                                          268 
##                        GOVT. HIGHER S.SCHOOL 
##                                         1009 
##                                       GOWOTO 
##                                          194 
##                               GOZOTO VILLAGE 
##                                          191 
##                                     GUKHANYU 
##                                          156 
##                                          HAK 
##                                          356 
##                             HAKAMUTI VILLAGE 
##                                           96 
##                                     HAKCHANG 
##                                          613 
##                                   HAKCHANG B 
##                                          551 
##                                     HAKHIZHE 
##                                          395 
##                          HAMLIKONG ORANGKONG 
##                                          260 
##                          HANINGKUNGLWA (S/W) 
##                                          468 
##                                HANKU VILLAGE 
##                                          419 
##                                     HAZADISA 
##                                          259 
##                               HAZI PARK AREA 
##                                          138 
##                                     HEBOLIMI 
##                                          573 
##                                   HEIRANGLWA 
##                                          322 
##                                     HEKHESHE 
##                                          232 
##                               HEKIYE VILLAGE 
##                                           88 
##                                     HELIPONG 
##                                          215 
##                                   HELIPONG B 
##                                          118 
##                                     HENBENJI 
##                                          158 
##                                HENINGKUNGLWA 
##                                          561 
##                                       HENIVI 
##                                          321 
##                             HEUNAMBE VILLAGE 
##                                           67 
##                            HIGH SCHOOL SEC A 
##                                          960 
##                            HIGH SCHOOL SEC B 
##                                         1562 
##                HIGH SCHOOL SECTOR - B E/W-II 
##                                          713 
##                                       HOISHE 
##                                          217 
##                                        HOITO 
##                                          324 
##                                     HOKHEZHE 
##                                           58 
##                                       HOKIYE 
##                                          231 
##                                     HOLONGBA 
##                                          572 
##                      HOLY CROSS, CHURCH ROAD 
##                                          128 
##                         HONGKONG MARKET AREA 
##                                          165 
##                              HONGNYU VILLAGE 
##                                          180 
##                                     HONGPHOI 
##                                          993 
##                               HONITO VILLAGE 
##                                          460 
##                             HORONGER VILLAGE 
##                                          887 
##                                    HOSHEPU B 
##                                          871 
##                              HOSPITAL COLONY 
##                                          622 
##                             HOTAHOTI VILLAGE 
##                                           88 
##                                      HOVISHE 
##                                          412 
##                              HOVUKHU VILLAGE 
##                                          561 
##                                      HOZUKHE 
##                                          476 
##                                        HUKER 
##                                          453 
##                                      HUKER B 
##                                          484 
##                                    HUKPANG A 
##                                          502 
##                                    HUKPANG B 
##                                          434 
##                                    HUKPANG C 
##                                          532 
##                               HUMTSO VILLAGE 
##                                         1116 
##                               HUTAMI VILLAGE 
##                                          354 
##                                HUTSU VILLAGE 
##                                          577 
##                                     IGHANUMI 
##                                          380 
##                                IGHANUMI - II 
##                                          415 
##                                     IGHAVITO 
##                                          100 
##                                  IKIESINGRAM 
##                                          245 
##                                       IKISHE 
##                                          529 
##                                        IKIYE 
##                                          209 
##                                        IMPUR 
##                                          104 
##                                       INBUNG 
##                                          441 
##                                      INDISEN 
##                                          946 
##            INDUSTRIAL VILLAGE RAZHUPHE-I E/W 
##                                          965 
##           INDUSTRIAL VILLAGE RAZHUPHE-II N/W 
##                                          805 
##                              INSIKUR VILLAGE 
##                                          460 
##                                     IPHONUMI 
##                                          334 
##                              IPONGER VILLAGE 
##                                          273 
##                                      IPUNGER 
##                                          310 
##                                        ITOVI 
##                                          199 
##                               IZHETO VILLAGE 
##                                          129 
##                               JABOKA VILLAGE 
##                                          711 
##                           JAHJON WARD MON HQ 
##                                          762 
##                                  JAIL COLONY 
##                                          667 
##                             JAIN SCHOOL AREA 
##                                          290 
##                                JAKHAMA LOWER 
##                                         1274 
##                               JAKHAMA MIDDLE 
##                                          943 
##                                 JAKHAMA TOWN 
##                                          921 
##                                JAKHAMA UPPER 
##                                          925 
##                           JAKPHANG VILLAGE A 
##                                          620 
##                           JAKPHANG VILLAGE B 
##                                         1436 
##                                    JALUKIE B 
##                                         3995 
##                              JALUKIE B (S/W) 
##                                          561 
##                      JALUKIE SANGTAM VILLAGE 
##                                          115 
##                JALUKIE TOWN-B SECTOR-I (W/W) 
##                                          585 
##               JALUKIE TOWN-B SECTOR-II (S/W) 
##                                          510 
##                                JALUKIEJANGDI 
##                                          537 
##                                   JALUKIEKAM 
##                                          321 
##                            JALUKIELO VILLAGE 
##                                          100 
##                           JALUKIERAM VILLAGE 
##                                          147 
##                                         JAPU 
##                                          369 
##                                JENTI VILLAGE 
##                                           77 
##                                   JHARNAPANI 
##                                          623 
##                              JOTSOMA (LOWER) 
##                                          999 
##                              JOTSOMA (UPPER) 
##                                          999 
##                            K. XEKIYE VILLAGE 
##                                          185 
##                            K.HOLLOHON COLONY 
##                                          728 
##                                   K.LONGSORE 
##                                          195 
##                                    K.STATION 
##                                          690 
##                                  KACHARIGAON 
##                                          814 
##                         KALIBARI JAIN TEMPLE 
##                                          154 
##                                KALIBARI ROAD 
##                                          371 
##                                 KAMI VILLAGE 
##                                          878 
##                          KANCHANGSHU VILLAGE 
##                                          779 
##                                  KANDINU-III 
##                                          628 
##                                  KANDINU - I 
##                                          604 
##                                 KANDINU - II 
##                                          636 
##                                  KANGCHING A 
##                                          415 
##                                  KANGCHING B 
##                                          330 
##                                  KANGCHING C 
##                                          138 
##                             KANGJANG VILLAGE 
##                                          290 
##                KANGTSUNG- TULUBA - I N/ WING 
##                                          445 
##                 KANGTSUNG TULUBA - I S/ WING 
##                                          619 
##         KANGTSUNG TULUBA - II B - KHEL BLOCK 
##                                          546 
##                          KANGTSUNG TULUBA IV 
##                                          402 
##                      KANGTSUNGYIMSEN VILLAGE 
##                                          256 
##                                     KASHANYU 
##                                          457 
##                           KASIRAM RANGAPAHAR 
##                                          888 
##                                      KATHARA 
##                                          264 
##                                       KAWOTO 
##                                          408 
##                                    KEJANGLWA 
##                                          424 
##                                        KEJOK 
##                                          414 
##                                KELETZAI WARD 
##                                          714 
##                                    KELINGMEN 
##                                          336 
##                                      KELTOMI 
##                                          376 
##                                      KENDUNG 
##                                           67 
##                                      KENGNYU 
##                                          547 
##                                      KENJONG 
##                                          373 
##                                     KENUOZOU 
##                                          809 
##                                       KEPHOR 
##                                          189 
##                               KESHAI VILLAGE 
##                                          129 
##                             KEVICHUSA COLONY 
##                                          258 
##                               KEVIJAU COLONY 
##                                         2072 
##            KEVIJAU COLONY, SIGNAL RANGAPAHAR 
##                                          759 
##                                      KEYAKIE 
##                                          256 
##                KEZIEKIE/ VETERINARY COLONIES 
##                                          419 
##                                    KEZO TOWN 
##                                          523 
##                         KEZO TOWN/ KEZO BASA 
##                                          229 
##                                       KEZOMA 
##                                          999 
##                                     KHAIBUNG 
##                                          332 
##                                   KHAKUTHATO 
##                                          158 
##                                      KHANIMO 
##                                          114 
##                                     KHAR-III 
##                                          811 
##                  KHARI I TONGPANG REJU BLOCK 
##                                          893 
##                         KHARI II IMRONG MEPU 
##                                          847 
##                                       KHEHOI 
##                                          708 
##                                     KHEHOKHU 
##                                          447 
##                              KHEKIHO VILLAGE 
##                                          974 
##                                      KHEKIYI 
##                                          510 
##                        KHELHOSHE POLYTECHNIC 
##                                          726 
##                                       KHELMA 
##                                          308 
##                                     KHENSA I 
##                                          472 
##                                    KHENSA II 
##                                          701 
##                                   KHENSA III 
##                                          659 
##                                       KHENYU 
##                                          278 
##                                    KHERMAHAL 
##                                          208 
##              KHERMAHAL CHAKHESANG COLONY E/W 
##                                          220 
##              KHERMAHAL CHAKHESANG COLONY N/W 
##                                          555 
##                                     KHESHITO 
##                                          105 
##                              KHESOMI VILLAGE 
##                                          182 
##                                       KHETOI 
##                                          771 
##                                      KHEWOTO 
##                                          365 
##                   KHEZHAKENO VILLAGE A/ WING 
##                                          735 
##                   KHEZHAKENO VILLAGE B/ WING 
##                                          491 
##                    KHEZHAKENO VILLAGE C/WING 
##                                          439 
##                    KHEZHAKENO VILLAGE D/WING 
##                                          967 
##                              KHOI DIPHUPAR A 
##                                          923 
##                                    KHOLEBOTO 
##                                          184 
##                                KHONG VILLAGE 
##                                           85 
##                            KHONGJIRE VILLAGE 
##                                          248 
##                              KHONGKA VILLAGE 
##                                          179 
##                              KHONGSA VILLAGE 
##                                          279 
##                              KHONOMA (LOWER) 
##                                          863 
##                              KHONOMA (UPPER) 
##                                          852 
##                                    KHOPANALA 
##                                          695 
##                            KHRIEHULIE COLONY 
##                                         1171 
##                           KHRIEZEPHE VILLAGE 
##                                          264 
##                                    KHRIMTOMI 
##                                          702 
##                               KHUDEI VILLAGE 
##                                          429 
##                                     KHUGHOVI 
##                                          463 
##                                   KHUGHUTOMI 
##                                          245 
##                                     KHUKISHE 
##                                          867 
##                                      KHUKIYE 
##                                          423 
##                          KHULAZU BASA B/WING 
##                                          551 
##                  KHULAZU BASA VILLAGE A/WING 
##                                          562 
##                  KHULAZU BAWE VILLAGE A/WING 
##                                          643 
##                  KHULAZU BAWE VILLAGE B/WING 
##                                          194 
##                                     KHULHOPU 
##                                          478 
##                                   KHUMCHOYAN 
##                                           83 
##                             KHUMIASU VILLAGE 
##                                          233 
##                                   KHUMISHU A 
##                                          328 
##                             KHUTSAMI VILLAGE 
##                                          385 
##                          KHUTSOKHUNO VILLAGE 
##                                          278 
##                                      KHUVUXU 
##                                          244 
##                                    KHUWABOTO 
##                                          945 
##                             KHUZAMA (MIDDLE) 
##                                          549 
##                              KHUZAMA (UPPER) 
##                                          733 
##                              KHUZAMI VILLAGE 
##                                          513 
##                              KHUZUMA (LOWER) 
##                                          804 
##                                    KICHILIMI 
##                                          606 
##                                     KICHUTIP 
##                                          933 
##                                       KIDIMA 
##                                          679 
##                               KIDIMA (LOWER) 
##                                          633 
##                               KIDIMA (UPPER) 
##                                          594 
##                                       KIDING 
##                                          283 
##          KIGWEMA (UPPER-I, UPPER-II & LOWER) 
##                                          300 
##                                KIGWEMA LOWER 
##                                          591 
##                                KIGWEMA UPPER 
##                                         1823 
##                                  KIJUMETOUMA 
##                                          390 
##                             KIJUMETOUMA BASA 
##                                           94 
##                              KIKHEVI VILLAGE 
##                                          108 
##                    KIKRUMA VILLAGE N/ WING-1 
##                                          657 
##                   KIKRUMA VILLAGE N/ WING-II 
##                                          440 
##                      KIKRUMA VILLAGE N/W-III 
##                                          616 
##                       KIKRUMA VILLAGE N/W-IV 
##                                          436 
##                    KIKRUMA VILLAGE S/ WING-1 
##                                          824 
##                   KIKRUMA VILLAGE S/ WING-II 
##                                          567 
##                       KIKRUMA VILLAGE S/W-IV 
##                                          549 
##                 KIKRUMA VILLAGE S/WING - III 
##                                          792 
##                                     KILO OLD 
##                                          295 
##                                       KILOMI 
##                                          587 
##                              KINGPAO VILLAGE 
##                                           80 
##                                     KINUNGER 
##                                          249 
##                                 KIOR VILLAGE 
##                                          308 
##                                    KIPEUJANG 
##                                          486 
##                                 KIPHIRE TOWN 
##                                         7657 
##                         KIPHIRE TOWN SOUTH C 
##                                          512 
##                              KIPHIRE VILLAGE 
##                                          999 
##                                        KIRHA 
##                                          367 
##                          KIRUPHEMA BAWE/BASA 
##                                          315 
##                             KISETONG VILLAGE 
##                                         1565 
##                                     KITAHUMI 
##                                          100 
##                                       KITAMI 
##                                          605 
##                    KITHOZWU (K.KHEL VISWEMA) 
##                                          538 
##                                       KIUSAM 
##                                          302 
##                                   KIUTSUKIUR 
##                                          489 
##                                       KIYATO 
##                                          655 
##                               KIYAVI VILLAGE 
##                                          249 
##                                       KIYAZU 
##                                         5270 
##                               KIYAZU A (S/W) 
##                                          634 
##                               KIYAZU B (N/W) 
##                                          971 
##                                      KIYEKHU 
##                                          463 
##                                      KIYETHA 
##                                          171 
##                              KIYEZHE VILLAGE 
##                                          101 
##                               KIZARI VILLAGE 
##                                          324 
##                                     KOBULONG 
##                                          341 
##                                      KOIBOTO 
##                                          196 
##                                         KOIO 
##                                          999 
##                               KONGAN VILLAGE 
##                                          878 
##                                   KONGRUKONG 
##                                          369 
##                                        KONYA 
##                                          659 
##                                 KORO VILLAGE 
##                                          186 
##                               KOTISU VILLAGE 
##                                          345 
##                                        KUBZA 
##                                          616 
##                                       KUHOXU 
##                                         1303 
##                                     KUHUBOTO 
##                                         1820 
##                                       KUHUPE 
##                                           55 
##                             KUKHEGOW VILLAGE 
##                                          221 
##                                   KUKIDOLONG 
##                                          464 
##                               KUMLONG WARD-I 
##                                          760 
##                              KUMLONG WARD-II 
##                                          985 
##                                      KUMPONG 
##                                          129 
##                                   KUSHIABILL 
##                                         1263 
##                               KUSONG VILLAGE 
##                                          321 
##                             KUTHUR VILLAGE A 
##                                          812 
##                             KUTHUR VILLAGE B 
##                                          598 
## KUTSAPO VILLAGE A/WING (NASA & RUSOZU KHEL ) 
##                                          703 
##                       KUTSAPO VILLAGE B/WING 
##                                          698 
##                               KUZATU VILLAGE 
##                                           88 
##                                     L.HOTOVI 
##                                          163 
##                               L.KHEL (LOWER) 
##                                         1658 
##                               L.KHEL (UPPER) 
##                                         1179 
##                                L.R.C. COLONY 
##                                         1084 
##                                   L.YANTHUNG 
##                                           88 
##                                    LADEIGARH 
##                                          334 
##                                    LAGHILATO 
##                                          761 
##                                      LAKHUNI 
##                                          409 
##                           LAKHUTI - I (EAST) 
##                                          851 
##                                 LAKHUTI - II 
##                                         1072 
##                                LAKHUTI - III 
##                                          805 
##                                 LAKHUTI - IV 
##                                          738 
##                                  LAKHUTI - V 
##                                         1060 
##                                LAKHUTI - VII 
##                                          762 
##                                       LALONG 
##                                          672 
##                                 LALONG (S/W) 
##                                          388 
##                                        LAMHI 
##                                          408 
##                      LAMPONGSHEANGHA VILLAGE 
##                                          535 
##                                LANGA VILLAGE 
##                                           46 
##                            LANGKOKER VILLAGE 
##                                          337 
##                            LANGMEANG VILLAGE 
##                                          809 
##                                      LANGNOK 
##                                          579 
##                           LANGZANGER VILLAGE 
##                                          337 
##                               LANYE JUNCTION 
##                                          184 
##                                       LAOKHU 
##                                          388 
##                                 LAPA LAMPONG 
##                                         1248 
##                                 LAPA VILLAGE 
##                                          653 
##                               LARURI VILLAGE 
##                                          227 
##                                     LASIKIUR 
##                                          141 
##                                LASUMI A/WING 
##                                          391 
##                                LASUMI B/WING 
##                                          437 
##                                 LAZA KHULUQA 
##                                          320 
##                                       LAZAMI 
##                                          633 
##                               LAZAMI (IYINU) 
##                                          515 
##                               LAZAMI (IZUQA) 
##                                          253 
##                          LAZAMI (IZUQA) - II 
##                                          381 
##                              LEANGHA VILLAGE 
##                                          953 
##                                  LEANGKONGER 
##                                          514 
##                                     LEANGNYU 
##                                          412 
##                             LEKHROMI VILLAGE 
##                                          818 
##                                      LENGNYU 
##                                          859 
##                            LENGRIJAN VILLAGE 
##                                         2238 
##                              LEPHORI VILLAGE 
##                                          739 
##                                 LERIE CHAZOU 
##                                          797 
##                                 LERIE COLONY 
##                                          913 
##                            LERIE COLONY - II 
##                                          837 
##                      LESHEMI VILLAGE A/ WING 
##                                          688 
##                      LESHEMI VILLAGE B/ WING 
##                                          716 
##                               LETSAM VILLAGE 
##                                           69 
##                              LHOMITHI COLONY 
##                                         1380 
##                  LHOMITHI COLONY (DHOBINALA) 
##                                         1185 
##                             LHOTHAVI VILLAGE 
##                                          498 
##                                    LIBEMPHAI 
##                                           99 
##                                     LICHUYAN 
##                                           35 
##                           LIHTSAOUNG VILLAGE 
##                                          102 
##                            LIJABA LIJEN WARD 
##                                          622 
##                                        LILEN 
##                                          562 
##                             LIMA SCHOOL AREA 
##                                          989 
##                                    LIMTHSAMI 
##                                          539 
##                              LINGTAK VILLAGE 
##                                          466 
##                               LIO – LONGCHUM 
##                                          204 
##                              LIO – LONGIDANG 
##                                          475 
##                              LIO – WOKHA NEW 
##                                           84 
##                              LIO – WOKHA OLD 
##                                          199 
##                                    LIPHANYAN 
##                                          586 
##                             LIPHIYAN VILLAGE 
##                                          279 
##                                       LIRISE 
##                                          655 
##                                 LIRMEN A OLD 
##                                          530 
##                        LIROYIM MODEL VILLAGE 
##                                          139 
##                                     LISHAYAN 
##                                           57 
##                                      LISHUYO 
##                                           74 
##                                        LITEM 
##                                          533 
##                                     LITHSAMI 
##                                          456 
##                                      LITSAMI 
##                                          865 
##                                    LITTA NEW 
##                                          347 
##                                    LITTA OLD 
##                                          500 
##                           LIZO MODEL VILLAGE 
##                                          106 
##                                LIZU AVIQUATO 
##                                          247 
##                                 LIZU NAGHUTO 
##                                          383 
##                                     LIZU NEW 
##                                          256 
##                                  LIZU PHUYEU 
##                                          288 
##                                     LIZUTOMI 
##                                          534 
##                                      LOAKHUN 
##                                          548 
##                                      LOCHOMI 
##                                          386 
##                                       LOGONG 
##                                          310 
##                                   LOGWESUNYU 
##                                          234 
##                                     LOKOBOMI 
##                                          403 
##                                     LONGAYIM 
##                                          159 
##                                     LONGCHEM 
##                                          501 
##                                 LONGCHENKONG 
##                                          121 
##                               LONGCHING TOWN 
##                                          248 
##                            LONGCHING VILLAGE 
##                                         2568 
##                       LONGHAPANG, MERANGKONG 
##                                          606 
##                                     LONGJANG 
##                                          587 
##                                 LONGJANG - I 
##                                          805 
##                               LONGJANG - III 
##                                          664 
##                                LONGJANG - IV 
##                                          637 
##                                   LONGJANG V 
##                                          372 
##                                      LONGKEI 
##                                          996 
##                                  LONGKHIM HQ 
##                                         1479 
##                          LONGKHIMONG VILLAGE 
##                                          230 
##                                   LONGKHIPET 
##                                          396 
##                                   LONGKHUM I 
##                                          446 
##                                  LONGKHUM II 
##                                          518 
##                                 LONGKHUM III 
##                                          587 
##                                  LONGKHUM IV 
##                                          414 
##                                   LONGKHUM V 
##                                          568 
##                                     LONGKONG 
##                                          915 
##                                       LONGLA 
##                                          647 
##                                      LONGLEM 
##                                          214 
##                               LONGLENG HQ. A 
##                                          688 
##                               LONGLENG HQ. B 
##                                         1103 
##                               LONGLENG HQ. C 
##                                          836 
##                                LONGLENG TOWN 
##                                          291 
##            LONGLI LENDEN WARD & PIGGERY FARM 
##                                          623 
##                               LONGMATRA TOWN 
##                                          522 
##                            LONGMATRA VILLAGE 
##                                          402 
##                  LONGMISA -I RESONGKONG MEPU 
##                                          727 
##                     LONGMISA II YIMLANG MEPU 
##                                          722 
##                   LONGMISA III JANGJANG MEPU 
##                                          809 
##                                  LONGMISA IV 
##                                          777 
##                                      LONGNAK 
##                                          701 
##                                       LONGPA 
##                                          413 
##                                 LONGPAYIMSEN 
##                                          999 
##                              LONGPHO VILLAGE 
##                                          607 
##                                LONGPONG WARD 
##                                          687 
##                                       LONGRA 
##                                          875 
##                                   LONGSA - I 
##                                          736 
##                                   LONGSA -II 
##                                         1193 
##                                     LONGSA I 
##                                          799 
##                                    LONGSA II 
##                                          690 
##                                   LONGSA III 
##                                          566 
##                                    LONGSA IV 
##                                          685 
##                                     LONGSA V 
##                                          728 
##                                  LONGSACHUNG 
##                                         1109 
##                                  LONGSEMDANG 
##                                          300 
##                                 LONGSHEN HQ. 
##                                          333 
##                                    LONGSTUNG 
##                                          895 
##                                     LONGTANG 
##                                          587 
##                                      LONGTHO 
##                                          228 
##                          LONGTHONGER VILLAGE 
##                                          234 
##                             LONGTING VILLAGE 
##                                          402 
##                                    LONGTOKUR 
##                                          352 
##                                   LONGTSSIRI 
##                                          185 
##                                  LONGTSUKTEP 
##                                          322 
##                                  LONGTSUNGER 
##                                          464 
##                               LONGWA VILLAGE 
##                                         3127 
##                          LONGWA WASA VILLAGE 
##                                          362 
##                             LONGZANG VILLAGE 
##                                         1357 
##                            LOPFUKONG VILLAGE 
##                                          157 
##                       LOSAMI VILLAGE A/ WING 
##                                          750 
##                       LOSAMI VILLAGE B/ WING 
##                                          744 
##                        LOSAMI VILLAGE C/WING 
##                                           65 
##                   LOTHA COLONY, KYONG COLONY 
##                                          998 
##                                     LOTISAMI 
##                                          297 
##                                 LOTISAMI NEW 
##                                          148 
##                                       LOTOVI 
##                                          926 
##                                        LOTSU 
##                                          905 
##                          LOWER KHOMI VILLAGE 
##                                          104 
##                           LOWER TIRU VILLAGE 
##                                          241 
##                               LOYUNG VILLAGE 
##                                          815 
##                    LOZAPHUHU VILLAGE A/ WING 
##                                          643 
##                    LOZAPHUHU VILLAGE B/ WING 
##                                          692 
##                                       LUKHAI 
##                                          352 
##                              LUKHAMI VILLAGE 
##                                          181 
##                                    LUKHUYIMI 
##                                          385 
##                                      LUKIKHE 
##                                          488 
##                           LUKONGMENDANG WARD 
##                                          510 
##                               LUTHUR VILLAGE 
##                                          396 
##                                     LUTSHUMI 
##                                          661 
##                                  LUVISHE (A) 
##                                           87 
##                                  LUVISHE (B) 
##                                          270 
##                                       MAKSHA 
##                                          467 
##                              MANGKOLEMBA-III 
##                                          998 
##                                MANGKOLEMBA I 
##                                          999 
##                               MANGKOLEMBA II 
##                                          568 
##                                   MANGLUMUKH 
##                                          175 
##                                 MANGMETONG I 
##                                          784 
##                         MANGMETONG II S/WING 
##                                          577 
##                        MANGMETONG III N/WING 
##                                          573 
##                                MANGMETONG IV 
##                                          693 
##                                 MANGMETONG V 
##                                          494 
##                                     MAPULUMI 
##                                          517 
##                         MAREPKONG PHE COLONY 
##                                          645 
##                                       MAROMI 
##                                          455 
##                             MATIKHRU VILLAGE 
##                                          385 
##                                      MBAULWA 
##                                          686 
##                                  MBAUPUNGCHI 
##                                          240 
##                                   MBAUPUNGWA 
##                                          464 
##                                  MECHANGBUNG 
##                                          291 
##                                     MEDEMYIM 
##                                          218 
##                       MEDICAL WARD, LONGLENG 
##                                          675 
##                                   MEDZIPHEMA 
##                                         5482 
##                        MEDZIPHEMA BLOCK -III 
##                                          775 
##                         MEDZIPHEMA BLOCK -IV 
##                                          604 
##                                     MEKIRANG 
##                                           71 
##                                  MEKOKLA-III 
##                                          539 
##                                  MEKOKLA – I 
##                                          624 
##                                 MEKOKLA – II 
##                                          999 
##                                       MEKULI 
##                                          194 
##                                     MELAHUMI 
##                                          327 
##                                  MELANGCHURI 
##                                          506 
##                          MELURI TOWN A/ WING 
##                                          409 
##                          MELURI TOWN B/ WING 
##                                          753 
##                          MELURI TOWN C/ WING 
##                                          848 
##                           MELURI TOWN D-WING 
##                                          490 
##           MELURI VILL. CHRISTIAN KHEL B/WING 
##                                          574 
##            MELURI VILL.CHRISTAIN KHEL A/WING 
##                                          573 
##               MELURI VILL.NON CHRISTAIN KHEL 
##                                          242 
##                                MENDENTI WARD 
##                                          632 
##                                    MENGUJUMA 
##                                          360 
##                          MERANGKONG COMPOUND 
##                                          630 
##                                MERAPANI TOWN 
##                                          810 
##                                       MEREMA 
##                                          999 
##                                      MERIYAN 
##                                          233 
##                                   MESHANGPEN 
##                                          288 
##                      MESOLUMI VILLAGE B/WING 
##                                          675 
##                      MESULUMI VILLAGE A/WING 
##                                          613 
##                                 METHA COLONY 
##                                          421 
##                                    METILIJEN 
##                                          106 
##                                     METONGER 
##                                          542 
##                              METSALE VILLAGE 
##                                          447 
##                                     MEYILONG 
##                                          101 
##                                    MEZO BASA 
##                                          158 
##                                       MEZOMA 
##                                          669 
##                                  MEZOMA - II 
##                                          538 
##                                      MHAIKAM 
##                                          465 
##                                   MHAINAMTSI 
##                                          641 
##                             MHAINAMTSI (S/W) 
##                                          526 
##                                     MID-LAND 
##                                          730 
##                         MIDDLE KHOMI VILLAGE 
##                                          783 
##                                 MIDDLE PWD-I 
##                                          413 
##                                MIDDLE PWD-II 
##                                          429 
##                              MIDLAND (LOWER) 
##                                          810 
##                             MIDLAND (MIDDLE) 
##                                          536 
##                              MIDLAND (UPPER) 
##                                          474 
##                          MIENCHANGLE VILLAGE 
##                                          157 
##                                         MIMA 
##                                         1628 
##                                 MIMI VILLAGE 
##                                          442 
##                                MISHILIMI (P) 
##                                          255 
##                                MISHILIMI (Y) 
##                                          522 
##                             MISHILIMI P - II 
##                                          369 
##                             MISSION COMPOUND 
##                                          246 
##                                    MITELEPHE 
##                                          141 
##                                    MOALENDEN 
##                                          116 
##                                        MOAVA 
##                                          814 
##                                     MOAYIMTI 
##                                          686 
##                                MODEL VILLAGE 
##                                          746 
##                       MOHUNG CHANGAI VILLAGE 
##                                          145 
##                               MOHUNG VILLAGE 
##                                          474 
##                                       MOILAN 
##                                          619 
##                                MOKIE VILLAGE 
##                                           82 
##                       MOKOCHUNG VILLAGE - IV 
##                                          813 
##                                   MOKOKCHUNG 
##                                         1026 
##                         MOKOKCHUNG VILLAGE-I 
##                                          828 
##                        MOKOKCHUNG VILLAGE-II 
##                                          700 
##                       MOKOKCHUNG VILLAGE-III 
##                                          917 
##                               MOLLEN VILLAGE 
##                                          236 
##                               MOLUNGKIMONG-I 
##                                          855 
##                              MOLUNGKIMONG-II 
##                                          843 
##                 MOLUNGYIMSEN-I RANGPANG MEPU 
##                                          653 
##                  MOLUNGYIMSEN-II LODONG MEPU 
##                                          539 
##                                       MOLVOM 
##                                          545 
##                                       MOLVUM 
##                                          285 
##                                     MOMCHING 
##                                          322 
##                                  MON VILLAGE 
##                                          967 
##                                     MONGCHEN 
##                                          369 
##                            MONGKHONG BHUMNYU 
##                                          313 
##                                     MONGPHIO 
##                                          115 
##                             MONGSENBHAI WARD 
##                                         1386 
##                     MONGSENTENEM, MERANGKONG 
##                                          369 
##                        MONGSENYIMTI COMPOUND 
##                                          529 
##                   MONGSENYIMTI I IMRONG TEMA 
##                                          596 
##                   MONGSENYIMTI II LONGSABANG 
##                                          549 
##             MONGSENYIMTI III SHITILONG BLOCK 
##                                          817 
##                                   MONGTIKANG 
##                                          507 
##                          MONGTSUVONG VILLAGE 
##                                          135 
##                                  MONYAKSHU A 
##                                         1237 
##                                  MONYAKSHU B 
##                                          998 
##                                  MONYAKSHU C 
##                                         1290 
##                               MONYAKSHU TOWN 
##                                          327 
##                                  MOPUNG TOWN 
##                                          275 
##                             MOPUNGCHUKET - I 
##                                          541 
##                            MOPUNGCHUKET - II 
##                                          408 
##                           MOPUNGCHUKET - III 
##                                          542 
##                            MOPUNGCHUKET - IV 
##                                          676 
##                                     MORAKCHO 
##                                          444 
##                                 MOYA VILLAGE 
##                                          464 
##                                  MPAI NAMCHI 
##                                          410 
##             mPFUTSERO TOWN,MENYITSUDA COLONY 
##                                          500 
##                                     MUKALIMI 
##                                          363 
##                                       MUNGYA 
##                                          725 
##                                       MURISE 
##                                          365 
##                                  MUTINGKHONG 
##                                           60 
##                                 N – LONGCHUM 
##                                          251 
##                             N.A.P SECTOR - A 
##                                          837 
##                             N.A.P SECTOR - B 
##                                          495 
##                                  N.LONGIDANG 
##                                          786 
##                              N.LONGIDANG - I 
##                                          900 
##                                      NACHAMA 
##                                          408 
##                       NAGA BAZAR - I (UPPER) 
##                                          731 
##                      NAGA BAZAR - II (LOWER) 
##                                          826 
##                                    NAGA GAON 
##                                          995 
##                                  NAGA UNITED 
##                                          957 
##                           NAGALAND SEED FARM 
##                                           34 
##                          NAGALAND UNIVERSITY 
##                                          168 
##                                     NAGARJAN 
##                                          946 
##                                   NAGARJAN C 
##                                          355 
##                               NAGARJAN C W/W 
##                                         1168 
##                       NAGARJAN HOSPITAL AREA 
##                                          927 
##                                  NAGHUTO NEW 
##                                          310 
##                                  NAGHUTO OLD 
##                                          871 
##                                NAGINIMORA HQ 
##                                         3516 
##                               NAGINIMORA HQ. 
##                                          106 
##                                    NAHARBARI 
##                                         2116 
##                                      NAKSHOU 
##                                          387 
##                                      NALTOKA 
##                                         1542 
##                            NAMCHING COMPOUND 
##                                           90 
##                           NAMHACHING VILLAGE 
##                                          108 
##                                      NANGTAN 
##                                          398 
##                                    NATHA NEW 
##                                          318 
##                                    NATHA OLD 
##                                          399 
##                              NATSAMI VILLAGE 
##                                          348 
##                                      NATSUMI 
##                                          452 
##                                 NATSUMI - II 
##                                          375 
##                                  NCHANGRAM-I 
##                                          951 
##                                 NCHANGRAM-II 
##                                          733 
##                                     NDUNGLWA 
##                                          351 
##                         NEISETUO / LAKE VIEW 
##                                         1110 
##                              NEITONG VILLAGE 
##                                          271 
##                                 NEPALI BOSTI 
##                                          585 
##                          NERHE MODEL VILLAGE 
##                                          373 
##                                NERHEMA LOWER 
##                                          500 
##                               NERHEMA MIDDLE 
##                                          309 
##                                NERHEMA UPPER 
##                                          407 
##                                NETAJI COLONY 
##                                         1554 
##                               NETNYU VILLAGE 
##                                          223 
##                          NEW AKHEGOW VILLAGE 
##                                          187 
##                                NEW BEISUMPUI 
##                                          422 
##                                  NEW CHALKOT 
##                                          283 
##                  NEW COLONY (R.KHEL VISWEMA) 
##                                          620 
##                               NEW COLONY N/W 
##                                          606 
##                               NEW COLONY S/W 
##                                          486 
##                                  NEW JALUKIE 
##                                          890 
##                            NEW JALUKIE (S/W) 
##                                          733 
##                        NEW LONGMATRA VILLAGE 
##                                           89 
##                                  NEW MANGAKI 
##                                          158 
##                          NEW MARKET- I & III 
##                                          704 
##                               NEW MARKET- II 
##                                          341 
##                       NEW MARKET (DHOBINALA) 
##                                          127 
##                NEW MARKET (LATIKA HALL AREA) 
##                                          328 
##                      NEW MARKET (MIYA PATTY) 
##                                          331 
##                            NEW MINISTER HILL 
##                                          741 
##                      NEW MINISTERS HILL - II 
##                                          775 
##                           NEW MONGER VILLAGE 
##                                          427 
##                                  NEW NGWALWA 
##                                          554 
##                            NEW NGWALWA (S/W) 
##                                          474 
##                                     NEW NKIO 
##                                          253 
##                             NEW PHOR VILLAGE 
##                                          326 
##                         NEW RISETHSI VILLAGE 
##                                          322 
##                         NEW RUZHAZHO VILLAGE 
##                                           73 
##                                  NEW SANGLAO 
##                                          126 
##                               NEW SANGSOMONG 
##                                          253 
##                       NEW SEWAK VIOLA COLONY 
##                                          947 
##                                    NEW SOGET 
##                                          123 
##                                NEW TEROGONYU 
##                                          884 
##                                  NEW THEWATI 
##                                          164 
##                                NEW TSADANGER 
##                                          211 
##                                   NEW VONGTI 
##                                           92 
##                                   NEW YAMHON 
##                                          201 
##                                      NEWLAND 
##                                          122 
##                                         NGAM 
##                                          344 
##                           NGANGCHING VILLAGE 
##                                          825 
##                                    NGANGPONG 
##                                          372 
##                            NGANGTING VILLAGE 
##                                          376 
##                               NGETCHUNGCHING 
##                                           85 
##                                   NGONGCHUNG 
##                                          177 
##                              NGOROMI VILLAGE 
##                                          247 
##                                 NGOULONG NEW 
##                                          257 
##                                 NGOULONG OLD 
##                                          274 
##                                    NGOZUBOMI 
##                                          257 
##                                     NGVUPHEN 
##                                          289 
##                                 NGWALWA TOWN 
##                                          224 
##                                       NIAN A 
##                                          562 
##                                       NIAN B 
##                                          333 
##                        NIAN B CHINGLA MORUNG 
##                                          526 
##                                       NIAN C 
##                                          393 
##                                      NIHOKHU 
##                                          701 
##                                  NIHOSHE (S) 
##                                          333 
##                                       NIHOTO 
##                                          766 
##                                     NIKHEKHU 
##                                          835 
##                               NIKIYE VILLAGE 
##                                          120 
##                                       NIKUTO 
##                                          209 
##                                       NIROYO 
##                                          955 
##                                NITOI VILLAGE 
##                                          437 
##                                   NIULAND-II 
##                                          545 
##                                      NKIALWA 
##                                          688 
##                                     NKIO (B) 
##                                          192 
##                                     NKIO OLD 
##                                          876 
##                                     NKWAKREU 
##                                          315 
##                              NOKHU VILLAGE A 
##                                          895 
##                              NOKHU VILLAGE B 
##                                          871 
##                                    NOKLAK HQ 
##                                         2910 
##                           NOKLAK VILLAGE (A) 
##                                          861 
##                           NOKLAK VILLAGE (B) 
##                                          408 
##                             NOKLAK VILLAGE C 
##                                          858 
##                   NOKLANGKONG WARD, LONGLENG 
##                                          182 
##                                      NOKPU I 
##                                          448 
##                                     NOKPU II 
##                                          608 
##                                  NOKSEN HQ B 
##                                          481 
##                                   NOKSEN HQ. 
##                                          557 
##                               NOKSEN VILLAGE 
##                                         1434 
##                                       NOKYAN 
##                                         1628 
##                              NOKZANG VILLAGE 
##                                          682 
##                                  NORTH POINT 
##                                          954 
##                                      NSENLWA 
##                                          189 
##                                   NSONG TOWN 
##                                          384 
##                                NSONG VILLAGE 
##                                          486 
##                                   NST COLONY 
##                                          565 
##                                   NST SECTOR 
##                                          999 
##                                       NSUNYU 
##                                          661 
##                               NSUNYU VILLAGE 
##                                          727 
##                                  NTU VILLAGE 
##                                          666 
##                            NUKSOSANG VILLAGE 
##                                          170 
##                                     NUNGYING 
##                                          688 
##                               NUNUMI VILLAGE 
##                                          611 
##                      NUTON BOSTI I.V. COLONY 
##                                         1075 
##                                NUTSU VILLAGE 
##                                           95 
##                         NYAMO / GHOSITO AREA 
##                                          973 
##                               NYANYU VILLAGE 
##                                          852 
##                                NYASA VILLAGE 
##                                          939 
##                                      NYINYEM 
##                                          388 
##                                         NZAU 
##                                          621 
##                                  NZAU NAMSAN 
##                                          437 
##                                       NZAUNA 
##                                          703 
##                              OFFICERS COLONY 
##                                          891 
##                           OFFICERS COLONY-II 
##                                          800 
##                                OFFICERS HILL 
##                                          848 
##                          OFFICERS HILL LOWER 
##                                          629 
##                                 OKHE VILLAGE 
##                                           86 
##                                      OKHEYAN 
##                                          166 
##                                       OKOTSO 
##                                          567 
##                                    OKOTSO II 
##                                          435 
##                                   OKOTSO III 
##                                          397 
##                                OLD BEISUMPUI 
##                                          276 
##                                  OLD CHALKOT 
##                                          204 
##                           OLD HOSPITAL SEC A 
##                                         1738 
##                           OLD HOSPITAL SEC B 
##                                         1859 
##                           OLD JABOKA VILLAGE 
##                                          121 
##                            OLD JALUKIE LOWER 
##                                          211 
##                            OLD JALUKIE UPPER 
##                                          119 
##                  OLD JALUKIE UPPER (BLOCK A) 
##                                          156 
##                                  OLD MANGAKI 
##                                          557 
##                              OLD MARKET AREA 
##                                          360 
##                            OLD MINISTER HILL 
##                                          507 
##                      OLD MINISTERS HILL - II 
##                                          808 
##                           OLD MONGER VILLAGE 
##                                          685 
##                                     OLD MPAI 
##                                          205 
##                         OLD RISETHSI VILLAGE 
##                                          270 
##                                    OLD SOGET 
##                                          255 
##                                  OLD THEWATI 
##                                           71 
##                                OLD TSADANGER 
##                                          948 
##                                   OLD VONGTI 
##                                           96 
##                                   OLD YAMHON 
##                                          399 
##                               ORANGKONG VILL 
##                                         1586 
##                     ORIENTAL COLONY SUB-JAIL 
##                                          751 
##                                OTING VILLAGE 
##                                          911 
##                               OUSHOK VILLAGE 
##                                          386 
##                                  OVER BRIDGE 
##                                          542 
##                                       P.KHEL 
##                                         1509 
##                         P.P.C WARD, LONGLENG 
##                                          559 
##                           P.R HILL (LOWER-I) 
##                                          863 
##                          P.R HILL (LOWER-II) 
##                                          814 
##                             P.R HILL (UPPER) 
##                                          408 
##                                P.W.D. COLONY 
##                                         1428 
##                              P.W.D.(UPPER-I) 
##                                          894 
##                                PADAM POKHURI 
##                                         1209 
##                            PADAM PUKHURI-III 
##                                          942 
##                 PAGLAPAHAR (NEW CHUMUKEDIMA) 
##                                          270 
##                                 PAIRA COLONY 
##                                          910 
##                                         PANG 
##                                          618 
##                            PANGSANG COMPOUND 
##                                          176 
##                                  PANGSHA NEW 
##                                          533 
##                                PANGSHA NEW B 
##                                          485 
##                                  PANGSHA OLD 
##                                          626 
##                            PANGTI - I (EAST) 
##                                          568 
##                                  PANGTI - II 
##                                          620 
##                                 PANGTI - III 
##                                          408 
##                                  PANGTI - IV 
##                                          323 
##                                  PANGTI - IX 
##                                          561 
##                                   PANGTI - V 
##                                          671 
##                                  PANGTI - VI 
##                                          299 
##                                 PANGTI - VII 
##                                          606 
##                                PANGTI - VIII 
##                                          510 
##                                     PANGTONG 
##                                          264 
##                                PAPONG COLONY 
##                                          506 
##                                 PARA MEDICAL 
##                                         1793 
##                        PATHSO NOKENG VILLAGE 
##                                         1828 
##                       PATHSO VILLAGE(W/WING) 
##                                         1158 
##                                PATIZUNG WARD 
##                                          576 
##                                         PEDI 
##                                           42 
##                                      PEDUCHA 
##                                          548 
##                                     PELETKIE 
##                                          267 
##                                      PELHANG 
##                                          663 
##                                       PENKIM 
##                                          314 
##                            PENLI WARD (B-II) 
##                                          987 
##                                   PERACIEZIE 
##                                          873 
##                                  PEREN NAMDI 
##                                          109 
##                                    PEREN NEW 
##                                         1831 
##                                    PEREN OLD 
##                                          503 
##                    PEREN TOWN-A SECTOR (W/W) 
##                                          299 
##                    PEREN TOWN-B SECTOR (S/W) 
##                                           62 
##                                        PESHU 
##                                          919 
##                                      PESHU B 
##                                          779 
##                                     PESSAO A 
##                                         1254 
##                                     PESSAO B 
##                                          612 
##                                 PEZIELIETSIE 
##                                          530 
##                                     PFUCHAMA 
##                                          671 
##                                PFUTSERO TOWN 
##                                         3995 
##                       PFUTSERO TOWN C-WING-I 
##                                          437 
##                       PFUTSEROMI VILL A WING 
##                                          619 
##                       PFUTSEROMI VILL B WING 
##                                          492 
##                    PFUTSEROMI VILLAGE C-WING 
##                                          629 
##                    PFUTSEROMI VILLAGE D-WING 
##                                          490 
##                                      PHAIJOL 
##                                          380 
##                                   PHAIKHOLUM 
##                                           51 
##                                   PHAIPIJANG 
##                                         1051 
##                                     PHANJANG 
##                                          205 
##                                         PHEK 
##                                          543 
##                            PHEK BASA VILLAGE 
##                                          270 
##                                    PHEK TOWN 
##                                         6029 
##                             PHEK TOWN H/WING 
##                                          505 
##                             PHEK TOWN I/WING 
##                                          735 
##                             PHEK TOWN J/WING 
##                                          696 
##                         PHEK VILLAGE A/ WING 
##                                          574 
##                             PHEK VILLAGE C/W 
##                                          438 
##                          PHEK VILLAGE D-WING 
##                                          435 
##                            PHEKERKREIMA BASA 
##                                           87 
##                             PHEKRKRIEMA BAWE 
##                                          240 
##                            PHELONGER VILLAGE 
##                                          631 
##                          PHELONGER VILLAGE A 
##                                          308 
##                                   PHENSHUNYU 
##                                         1156 
##                                   PHENWHENYU 
##                                          539 
##                                    PHERIMA A 
##                                          566 
##                              PHESAMA (LOWER) 
##                                          937 
##                              PHESAMA (UPPER) 
##                                          807 
##                                       PHEZHA 
##                                          249 
##                                      PHILIMI 
##                                          600 
##                                  PHIRE-AHIRE 
##                                          935 
##                                    PHIRO - I 
##                                          659 
##                                   PHIRO - II 
##                                          505 
##                                  PHIRO - III 
##                                          392 
##                                   PHIRO - IV 
##                                          443 
##                              PHISAMI VILLAGE 
##                                          956 
##                              PHOKHUNGRI TOWN 
##                                          132 
##                           PHOKHUNGRI VILLAGE 
##                                          390 
##                                     PHOKPHUR 
##                                          894 
##                             PHOKTONG VILLAGE 
##                                          597 
##                          PHOLAMI NEW VILLAGE 
##                                          537 
##                              PHOLAMI VILLAGE 
##                                          623 
##                                PHOMCHING.HQ. 
##                                          960 
##                                 PHOR VILLAGE 
##                                          453 
##                             PHUGWIMI VILLAGE 
##                                          948 
##                                 PHULESHETOMI 
##                                          304 
##                   PHUSACHODU VILLAGE A/ WING 
##                                          866 
##                   PHUSACHODU VILLAGE B/ WING 
##                                          766 
##                   PHUSACHODU VILLAGE C/ WING 
##                                          749 
##                    PHUSACHODU VILLAGE D/WING 
##                                          813 
##                    PHUSACHODU VILLAGE F-WING 
##                                          703 
##                    PHUSACHODU WILLAGE E-WING 
##                                          789 
##                                     PHUSHUMI 
##                                          538 
##                           PHUVKIU VILLAGE- A 
##                                          986 
##                            PHUVKIU VILLAGE B 
##                                          611 
##                                    PHUYE NEW 
##                                          336 
##                                    PHUYE OLD 
##                                          364 
##                              PHUYOBA VILLAGE 
##                                          124 
##                                        PIMLA 
##                                          936 
##                         PIPHEMA BAZAAR (N/W) 
##                                          309 
##                         PIPHEMA BAZAAR (S/W) 
##                                          224 
##                                  PIPHEMA NEW 
##                                          137 
##                      PIPHEMA OLD/PIPHEMA NEW 
##                                          262 
##                                     PISHIKHU 
##                                          300 
##                                   POILWA NEW 
##                                          456 
##                                   POILWA OLD 
##                                          664 
##                             POILWA OLD (S/W) 
##                                          601 
##                                POLICE COLONY 
##                                          752 
##                               POLICE PROJECT 
##                                          581 
##                    POLICE PROJECT LOWER - II 
##                                          771 
##                                    PONGCHING 
##                                         1218 
##                      PONGENTENEM, MERANGKONG 
##                                          704 
##                                    PONGITONG 
##                                         1259 
##                             PONGKONG VILLAGE 
##                                          835 
##                                      PONGO A 
##                                         1233 
##                                      PONGO B 
##                                          811 
##                                      PONGO C 
##                                          287 
##                           PORTER LANE(LOWER) 
##                                          735 
##                           PORTER LANE(UPPER) 
##                                          980 
##                       PORUBA VILLAGE A/ WING 
##                                          671 
##                       PORUBA VILLAGE B/ WING 
##                                          746 
##                        PORUBA VILLAGE C/WING 
##                                          676 
##                       POST OFFICE SECTOR - A 
##                                          803 
##                       POST OFFICE SECTOR - B 
##                                          665 
##                 PRANAB VIDYAPITH SCHOOL AREA 
##                                          457 
##                                 PROJECT EAST 
##                                          736 
##                                 PROJECT WEST 
##                                          712 
## PUBLIC COLLEGE (Co.oP.BANK AREA POWER HOUSE) 
##                                          659 
##   PUBLIC COLLEGE CO-OP.BANK AREA POWER HOUSE 
##                                          553 
##           PUBLIC COMMERCE COLLEGE (RLY.LINE) 
##                                          725 
##                                PUDAM PUKHURI 
##                                         1253 
##                                    PUGHOBOTO 
##                                         1023 
##                                   PUILWA NEW 
##                                          206 
##                                   PUILWA OLD 
##                                           85 
##                                PUKHA VILLAGE 
##                                          605 
##                                     PUNEBOQA 
##                                          111 
##                                      PUNGLWA 
##                                          731 
##                              PUNGREN VILLAGE 
##                                          225 
##                              PUNGRO TOWN - A 
##                                          829 
##                              PUNGRO TOWN - B 
##                                          996 
##                                PUNGRO TOWN A 
##                                          999 
##                               PUNGRO VILLAGE 
##                                          639 
##                               PURANA BAZAR-B 
##                                          769 
##                 PURANA BAZAR (PADAM PUKHURI) 
##                                         2101 
##            PURANA BAZAR (PRAGADY SAMAJ HALL) 
##                                          927 
##                    PURANA BAZAR (RIVER SIDE) 
##                                         1113 
##                 PURANA BAZAR (RIVERSIDE) S/W 
##                                         1183 
##                               PURRUR VILLAGE 
##                                          536 
##                               PWD LOWER - II 
##                                          389 
##                                 PWD LOWER -I 
##                                          675 
##                                      PYANGSA 
##                                          434 
##                                       PYOCHU 
##                                          186 
##                                    RALAN NEW 
##                                          338 
##                                    RALAN OLD 
##                                          361 
##                        RAM JANKI SCHOOL AREA 
##                                          451 
##                           RANGAPAHAR VILLAGE 
##                                          380 
##                                   RAZEBA HQ. 
##                                          519 
##                                     RAZHAPHE 
##                                          488 
##                               REGURI VILLAGE 
##                                          324 
##                                   RENGMAPANI 
##                                          255 
##                             RESIDENCY COLONY 
##                                          616 
##                RIEHUOPE KHEL, MELURI VILLAGE 
##                                          259 
##                               RIHUBA VILLAGE 
##                                          389 
##                                RILAN VILLAGE 
##                                          245 
##                                  RIPHYIM NEW 
##                                          857 
##                              RIPHYIM OLD - I 
##                                         1216 
##                             RIPHYIM OLD - II 
##                                          893 
##                             RIVERBELT COLONY 
##                                          816 
##                                  RLY. COLONY 
##                                          816 
##                        RLY. H.E. SCHOOL AREA 
##                                          327 
##                               RONGMAI COLONY 
##                                          310 
##                                         RONI 
##                                          192 
##                                        RONSU 
##                                          105 
##                                ROTTO NEW - I 
##                                          750 
##                                 ROTTO NEW II 
##                                          747 
##                                    ROTTO OLD 
##                                          744 
##                                 ROTTO OLD II 
##                                          743 
##                                       RUCHAN 
##                                          219 
##                                   RUMENSINYU 
##                                          371 
##                         RUNGUZU NASA VILLAGE 
##                                          266 
##                         RUNGUZU NAWE VILLAGE 
##                                          798 
##                            RURUR VILLAGE (A) 
##                                          284 
##                            RURUR VILLAGE (B) 
##                                          221 
##                                       RUSOMA 
##                                          809 
##                                  RUSOMA BASA 
##                                          808 
##                                    RUZAPHEMA 
##                                         1179 
##                              RUZAZHO VILLAGE 
##                                          549 
##                       RUZAZHO VILLAGE B/WING 
##                                          393 
##                     RUZAZHOMI VILLAGE A/WING 
##                                          600 
##                                     S WOKHAN 
##                                           63 
##                                     S. HETOI 
##                                          158 
##                            S/TANGTAN VILLAGE 
##                                         1009 
##                                     SABANGYA 
##                                          843 
##                             SACHUBA (KIDIMA) 
##                                          680 
##                                      SAIJANG 
##                                          562 
##                                      SAILHEM 
##                                          179 
##                              SAKCHI COMPOUND 
##                                          242 
##                                    SAKHABAMA 
##                                          602 
##                                 SAKRABA TOWN 
##                                          479 
##                              SAKRABA VILLAGE 
##                                          639 
##                               SAKSHI VILLAGE 
##                                          520 
##                             SALANGTEM WARD-I 
##                                          624 
##                            SALANGTEM WARD-II 
##                                          803 
##                                   SALULEMANG 
##                                          607 
##                            SALUMI VILLAGE- A 
##                                          513 
##                            SALUMI VILLAGE- B 
##                                          572 
##                                     SAMAGURI 
##                                          430 
##                           SAMJIURAM SECTOR A 
##                                          797 
##                     SAMJIURAM SECTOR B (S/W) 
##                                          513 
##                     SAMJIURAM SECTOR C (S/W) 
##                                          195 
##                              SAMPHUR VILLAGE 
##                                          791 
##                           SAMZIURAM SECTOR B 
##                                          719 
##                           SAMZIURAM SECTOR C 
##                                          812 
##                            SANGCHEN COMPOUND 
##                                          131 
##                                    SANGKUMTI 
##                                          963 
##                               SANGLAO (EAST) 
##                                          792 
##                               SANGLAO (WEST) 
##                                          698 
##                                   SANGPHUR C 
##                                          431 
##                                   SANGPHUR D 
##                                          378 
##                         SANGPHUR VILLAGE (A) 
##                                          537 
##                         SANGPHUR VILLAGE (B) 
##                                          407 
##                               SANGSA VILLAGE 
##                                          654 
##                                  SANGSANGNYU 
##                                          378 
##                                   SANGSOMOMG 
##                                          842 
##                                      SANGTAK 
##                                          943 
##                         SANGTAMTILLA VILLAGE 
##                                          808 
##                           SANGTEMLA WARD I A 
##                                          701 
##                          SANGTEMLA WARD II A 
##                                          709 
##                            SANGTSOZE VILLAGE 
##                                          162 
##                                  SANGTSUNGER 
##                                           53 
##                                   SANIS TOWN 
##                                          549 
##                                SANIS VILLAGE 
##                                          850 
##                                    SANKITONG 
##                                          470 
##                               SANKITONG - II 
##                                          430 
##                          SANTHAM WARD MON HQ 
##                                          813 
##                                      SAOSHOU 
##                                          313 
##                                     SAPOTIMI 
##                                          427 
##                                      SAPTIQA 
##                                          153 
##                                    SARINGYIM 
##                                          436 
##                                      SASTAMI 
##                                          309 
##                                  SATAKHA OLD 
##                                          258 
##                           SATAKHA TOWN NEW B 
##                                         1195 
##                           SATAKHA TOWN OLD A 
##                                         1520 
##                              SATAKHA VILLAGE 
##                                          407 
##                                       SATAMI 
##                                          993 
##                         SATHAZU NASA VILLAGE 
##                                          329 
##                         SATHAZU NAWE VILLAGE 
##                                          925 
##                              SATHERI VILLAGE 
##                                           91 
##                                   SATOI TOWN 
##                                          271 
##                                SATOI VILLAGE 
##                                          315 
##                                     SATSUKBA 
##                                          163 
##                                       SATTSU 
##                                          115 
##                               SATUZA VILLAGE 
##                                          257 
##                              SCIENCE COLLEGE 
##                                          970 
##                       SCIENCE COLLEGE PHEZHU 
##                                          672 
##                                      SECHUMA 
##                                          329 
##                                 SEITHEKEMA C 
##                                          996 
##                               SEITHEKEMA NEW 
##                                         1093 
##                               SEITHEKEMA OLD 
##                                          659 
##                                 SEIYHA PHESA 
##                                           85 
##                                     SEIYHAMA 
##                                          605 
##                         SEKREZU HEAD QUARTER 
##                                          258 
##                                       SELUKU 
##                                          508 
##                                      SELUPHE 
##                                          661 
##                                     SEMATILA 
##                                          871 
##                                     SENDENYU 
##                                         1027 
##                               SENJUM VILLAGE 
##                                          552 
##                                     SEPFUZOU 
##                                          601 
##                                     SERIKA A 
##                                          210 
##                                       SEWANU 
##                                          378 
##                               SEYOCHUNG TOWN 
##                                          593 
##                          SEYOCHUNG VILLAGE B 
##                                         1349 
##                                   SHAHAPHUMI 
##                                          192 
##                                    SHAKI - I 
##                                          598 
##                                    SHAKI -II 
##                                          637 
##                                   SHAKI -III 
##                                          514 
##                              SHAMATOR HQ - C 
##                                          807 
##                              SHAMATOR HQ - D 
##                                          519 
##                            SHAMATORE HQ. (A) 
##                                          923 
##                            SHAMATORE HQ. (B) 
##                                          505 
##                            SHAMATORE VILLAGE 
##                                          985 
##                            SHAMKANG WARD LLG 
##                                          430 
##                                 SHAMNYU WARD 
##                                         1787 
##                               SHAMSHANGCHING 
##                                          205 
##                             SHANGNYU VILLAGE 
##                                          904 
##                        SHAULI WARD, LONGLENG 
##                                          379 
##                     SHE-KIDA (KIDIMA MIDDLE) 
##                                          633 
##                    SHEANGHA CHINGNYU VILLAGE 
##                                         3042 
##                       SHEANGHA MOKOK VILLAGE 
##                                          999 
##                     SHEANGHA TANGTAN VILLAGE 
##                                          968 
##                       SHEANGHA WAMSA VILLAGE 
##                                         1682 
##                               SHEMNYUNGCHING 
##                                          329 
##                                    SHENA NEW 
##                                          654 
##                                    SHENA OLD 
##                                         1761 
##                                    SHESULIMI 
##                                          459 
##                                     SHEVISHE 
##                                          560 
##                                      SHEYIPU 
##                                          540 
##                             SHICHIMI VILLAGE 
##                                          165 
##                                      SHIKAVI 
##                                          295 
##                                      SHIKUTO 
##                                          164 
##                             SHINGNYU VILLAGE 
##                                          171 
##                                    SHIPONGER 
##                                          973 
##                             SHISHIMI VILLAGE 
##                                          165 
##                               SHITAP VILLAGE 
##                                          342 
##                              SHITOVI VILLAGE 
##                                          344 
##                                     SHITSUMI 
##                                          501 
##                              SHIYONG VILLAGE 
##                                          974 
##                                       SHOIPU 
##                                          686 
##                                       SHOIXE 
##                                          576 
##                                     SHOKHUVI 
##                                          782 
##                             SHOTHUMI VILLAGE 
##                                          516 
##                                      SHOTOMI 
##                                          325 
##                                      SHOWUBA 
##                                          395 
##                                  SHOWUBA NEW 
##                                          495 
##                                  SHOWUBA OLD 
##                                         1412 
##                                  SHOZUKHU IV 
##                                          950 
##                             SHURHOBA VILLAGE 
##                                           71 
##                        SIGNAL ANGAMI VILLAGE 
##                                         2027 
##                           SIKIUR VILLAGE (A) 
##                                          350 
##                           SIKIUR VILLAGE (B) 
##                                          463 
##                              SINGREP VILLAGE 
##                                          999 
##                                    SINGRIJAN 
##                                         1355 
##                             SINJOL (A) LOWER 
##                                           68 
##                             SINJOL (B) UPPER 
##                                          141 
##                                   SIPONGSANG 
##                                          348 
##                                 SIRHI ANGAMI 
##                                          194 
##                                      SIRHIMA 
##                                          565 
##                                      SISHUNU 
##                                          610 
##                  SITIKOLAK & AITELENDEN WARD 
##                                          916 
##                                  SITIMI TOWN 
##                                          756 
##                               SITIMI VILLAGE 
##                                          670 
##                                     SOCUNOMA 
##                                          408 
##                            SODZULHOU VILLAGE 
##                                          706 
##                               SOHOMI VILLAGE 
##                                          395 
##                            SOKRIBA (KHUZAMA) 
##                                          633 
##                                      SONGLHU 
##                                          406 
##                                       SONGOU 
##                                           52 
##                                       SOSHAN 
##                                          455 
##                                    SOTOKUR A 
##                                          555 
##                                    SOTOKUR B 
##                                          753 
##                                    SOTOKUR D 
##                                          509 
##                                     SOTOKURC 
##                                          409 
##                              SOUTH POINT N/W 
##                                          987 
##                              SOUTH POINT S/W 
##                                         1197 
##                                     SOVIMA A 
##                                         1157 
##                                     SOVIMA D 
##                                          731 
##                         SOWA CHANGLE VILLAGE 
##                                          147 
##                                 SOWA VILLAGE 
##                                          569 
##                   St. JOHN SECTOR - A N/W-II 
##                                          529 
##                         St. JOHN SECTOR B-II 
##                                          460 
##                          ST.JOHN SCHOOL AREA 
##                                          620 
##                         ST.JOHN SCHOOL SEC A 
##                                         1019 
##                         ST.JOHN SCHOOL SEC B 
##                                          646 
##                          St.JOHN SECTOR B-II 
##                                          793 
##                                        SUHOI 
##                                         2797 
##                                      SUKHALU 
##                                          410 
##                                      SUKHAYI 
##                                          385 
##                                       SUKOMI 
##                                          397 
##                                 SUMI VILLAGE 
##                                          337 
##                                       SUMITO 
##                                           76 
##                                      SUNGKHA 
##                                          181 
##                               SUNGKOMEN WARD 
##                                          999 
##                                      SUNGLUP 
##                                          619 
##                                SUNGRATSU - I 
##                                          748 
##                               SUNGRATSU - II 
##                                          769 
##                              SUNGRATSU - III 
##                                          760 
##                                       SUNGRO 
##                                          623 
##                                    SUPHANYAN 
##                                          101 
##              SUPPLY CLY. LAPALOMA CINE. HALL 
##                                          533 
##           SUPPLY COLONY LAPALOMA CINEMA HALL 
##                                          609 
##                      SUPPLY COLONY, W/POLICE 
##                                          261 
##                                SURUHOTO TOWN 
##                                          621 
##                                SURUHUTO TOWN 
##                                          427 
##                         SURUHUTO TOWN A-KHEL 
##                                          532 
##                                   SURUMI (N) 
##                                          768 
##                                   SURUMI (S) 
##                                         1216 
##                                       SUTEMI 
##                                          440 
##                    SUTHOTSU VILLAGE (NAHATO) 
##                                          204 
##                                SUTSU VILLAGE 
##                                          284 
##                               T.KHEL (LOWER) 
##                                          727 
##                               T.KHEL (UPPER) 
##                                          641 
##                                   T/CHINGKHO 
##                                          815 
##                                   T/CHINGNYU 
##                                          861 
##                                       TAKNYU 
##                                          210 
##                              TAMKONG VILLAGE 
##                                         1397 
##                                 TAMLU HQ -II 
##                                           77 
##                                  TAMLU HQ. A 
##                                          566 
##                                  TAMLU HQ. B 
##                                          492 
##                              TAMLU VILLAGE B 
##                                          393 
##                         TAMLU VILLAGE K/KHEL 
##                                          537 
##                     TAMLU VILLAGE P/KHEL - I 
##                                          618 
##                    TAMLU VILLAGE P/KHEL - II 
##                                          443 
##                                       TANGHA 
##                                          380 
##                                     TANGHA C 
##                                          323 
##                                      TANGNYU 
##                                         1898 
##                                TANGYO MORUNG 
##                                          425 
##                           TANLAO WARD MON HQ 
##                                         1152 
##                               TANNAI VILLAGE 
##                                          828 
##                                     TAZUHUMI 
##                                          187 
##                                  TCHUCHANPEN 
##                                           74 
##                                TECHAHAN WARD 
##                                          667 
##                              TEHEPHU VILLAGE 
##                                          295 
##                                     TEICHUMA 
##                                          400 
##                               TEKANG VILLAGE 
##                                          163 
##                             TEKIVONG VILLAGE 
##                                          133 
##                                TEKUK VILLAGE 
##                                           96 
##                                TEKUN VILLAGE 
##                                           62 
##                                 TELA VILLAGE 
##                                          204 
##                             TENING CHRISTIAN 
##                                          598 
##                       TENING CHRISTIAN (S/W) 
##                                          419 
##                                  TENING TOWN 
##                                          716 
##                            TENING TOWN (S/W) 
##                                          495 
##                               TENING VILLAGE 
##                                          128 
##                             TENYIPHE VILLAGE 
##                                         2418 
##                                        TEPUN 
##                                          472 
##                         TERHUTSESEMI VILLAGE 
##                                          636 
##                                    TEROGONYU 
##                                          825 
##                                    TESEN NEW 
##                                          825 
##                                    TESEN OLD 
##                                          667 
##                              TESEN OLD (S/W) 
##                                          447 
##                          TESOPHENYU (MIDDLE) 
##                                          858 
##                           TESOPHENYU (UPPER) 
##                                         2189 
##                        TESOPHENYU LOWER - II 
##                                          716 
##                              TETHEYO VILLLGE 
##                                          431 
##                              TETHEZU VILLAGE 
##                                          261 
##                              TEZATSE VILLAGE 
##                                          189 
##                           THAHEKHU VILLAGE A 
##                                         1199 
##                           THAHEKHU VILLAGE B 
##                                         1611 
##                                      THAKIYE 
##                                          376 
##                          THAMNAN WARD MON HQ 
##                                          653 
##                             THANAMIR VILLAGE 
##                                          383 
##                            THANGTHUR VILLAGE 
##                                          963 
##                              THAZUVI VILLAGE 
##                                          156 
##                   THECHULUMI VILLAGE A/ WING 
##                                          489 
##                   THECHULUMI VILLAGE B/ WING 
##                                          762 
##                    THECHULUMI VILLAGE C-WING 
##                                          511 
##                                 THEKRUJUNAMA 
##                                          235 
##                     THENYIZU VILLAGE A/ WING 
##                                          557 
##                     THENYIZU VILLAGE B/ WING 
##                                          805 
##                      THENYIZU VILLAGE C-WING 
##                                          499 
##                    THEVOPISU VILLAGE A\\WING 
##                                          449 
##                    THEVOPISU VILLAGE B\\WING 
##                                          491 
##                     THEVOPISU VILLAGE C-WING 
##                                          454 
##                     THEVOPISU VILLAGE D-WING 
##                                          490 
##                                      THILIXU 
##                                         1142 
##                    THIPUZUMI VILLAGE A/ WING 
##                                          655 
##                    THIPUZUMI VILLAGE B/ WING 
##                                          606 
##                     THIPUZUMI VILLAGE C-WING 
##                                          504 
##                     THIPUZUMI VILLAGE D-WING 
##                                          452 
##                              THIZAMA 4th NAP 
##                                          675 
##                              THIZAMA VILLAGE 
##                                          414 
##                                    THOKIHIMI 
##                                          425 
##                                   THONGSONYU 
##                                          239 
##                                   THONGSUNYU 
##                                          216 
##                                 THONOKNYU HQ 
##                                          810 
##                            THONOKNYU VILLAGE 
##                                          534 
##                                     THSURUHU 
##                                          173 
##                               THULUN VILLAGE 
##                                          104 
##                                  TICHIBAMI B 
##                                          532 
##                                    TICHIPAMI 
##                                          541 
##                                   TINGALIBAM 
##                                          249 
##                            TIZIT HEADQUARTER 
##                                         1661 
##                                TIZIT VILLAGE 
##                                         3093 
##                                     TOBU HQ. 
##                                         1800 
##                          TOBU VILLAGE B KHEL 
##                                          584 
##                   TOBU VILLAGE CHANGKHU KHEL 
##                                          466 
##                                      TOKCHUR 
##                                          235 
##                                       TOKIYE 
##                                          311 
##                                      TOKIZHE 
##                                          116 
##                                      TOKUGHA 
##                                          662 
##                                       TOLUVI 
##                                          967 
##                          TOMPANG WARD MON HQ 
##                                          674 
##                          TONGDENTSUYONG WARD 
##                                          993 
##                                 TONGLONGSORE 
##                                           52 
##                              TOSHEZU VILLAGE 
##                                          253 
##                                      TOSHIHO 
##                                          306 
##                        TOTOK CHINGHA VILLAGE 
##                                          762 
##                       TOTOK CHINGLEN VILLAGE 
##                                          297 
##                        TOTOKCHINGNYU VILLAGE 
##                                          517 
##                                TOTSU VILLAGE 
##                                          313 
##                                   TOULAZOUMA 
##                                         1280 
##                                TOUPHE-PHEZOU 
##                                           62 
##                              TOUPHE BAWE - B 
##                                          437 
##                                TOWN SECTOR A 
##                                          504 
##                                      TRONGER 
##                                          905 
##                                     TSAPHIMI 
##                                          333 
##                                       TSAWAO 
##                                          589 
##                       TSEIPAMA MODEL VILLAGE 
##                                          139 
##                            TSEMINYU NEW TOWN 
##                                         1759 
##                       TSEMINYU NEW TOWN -III 
##                                          676 
##                            TSEMINYU OLD TOWN 
##                                          663 
##                             TSEMINYU VILLAGE 
##                                          744 
##                        TSEMINYU VILLAGE - II 
##                                          832 
##                                  TSETHRONGSE 
##                                          605 
##                                  TSIEMEKHUMA 
##                                          235 
##                             TSIEMEKHUMA BAWE 
##                                          209 
##                                     TSIEPAMA 
##                                          513 
##                                TSIESEMA BASA 
##                                          307 
##                                TSIESEMA BAWE 
##                                          556 
##                                   TSONGPHONG 
##                                          163 
##                                       TSONSA 
##                                          218 
##                                        TSOPO 
##                                          384 
##                                    TSORI NEW 
##                                          347 
##                                    TSORI OLD 
##                                          367 
##                                     TSOSINYU 
##                                          319 
##                                      TSUKOMI 
##                                          168 
##                              TSUNGAR VILLAGE 
##                                          575 
##                                 TSUNGIKI - I 
##                                          697 
##                                TSUNGIKI - II 
##                                          999 
##                               TSUNGIKI - III 
##                                          376 
##                            TSUNGTANG VILLAGE 
##                                          163 
##                                 TSUNGTSUTONG 
##                                          537 
##                                      TSUNGZA 
##                                          172 
##                   TSUPFUMI (CHOBAMA) VILLAGE 
##                                          643 
##                                    TSUREMMEN 
##                                          420 
##                            TSUREVONG VILLAGE 
##                                           61 
##                                    TSUSAPANG 
##                                          596 
##                               TSUTHU VILLAGE 
##                                          118 
##                                      TSUTOHO 
##                                          339 
##                               TSUUMA VILLAGE 
##                                          302 
##                           TUENSANG VILLAGE A 
##                                         1294 
##                           TUENSANG VILLAGE B 
##                                          874 
##                           TUENSANG VILLAGE C 
##                                         1329 
##                           TUENSANG VILLAGE D 
##                                          644 
##                           TUENSANG VILLAGE E 
##                                          337 
##                               TUIMEI VILLAGE 
##                                          419 
##                                     TUKULIQA 
##                                          108 
##                                   TUKUNASAMI 
##                                          304 
##                                TULIKONG WARD 
##                                          539 
##                                TULIYONG WARD 
##                                          827 
##                                TUOPHEMA BASA 
##                                          845 
##                                TUOPHEMA BAWE 
##                                          625 
##                                    TZUDIKONG 
##                                         2159 
##                                 UKHA VILLAGE 
##                                          639 
##                               UKHA VILLAGE A 
##                                          646 
##                            UNGER - I N/ WING 
##                                          474 
##                            UNGER - I S/ WING 
##                                          500 
##                                     UNGMA-VI 
##                                          899 
##                     UNGMA I AONGLENDEN BLOCK 
##                                          918 
##                     UNGMA II MEKUMPONG BLOCK 
##                                          953 
##                            UNGMA III N/ WING 
##                                          683 
##                             UNGMA IV S/ WING 
##                                          679 
##                     UNGMA V YIMSENKONG BLOCK 
##                                          923 
##                           UNITED NORTH BLOCK 
##                                          889 
##                         UNITED NORTH BLOCK I 
##                                          521 
##                            UNITY VILLAGE E/W 
##                                          605 
##                            UNITY VILLAGE N/W 
##                                          820 
##                            UNITY VILLAGE S/W 
##                                          893 
##                            UPPER AGRI COLONY 
##                                          812 
##                          UPPER KHOMI VILLAGE 
##                                          486 
##                                UPPER NAMTHAI 
##                                          210 
##                           UPPER TIRU VILLAGE 
##                                          540 
##                                 URRA VILLAGE 
##                                          556 
##                                      USUTOMI 
##                                          999 
##                                    V.K. TOWN 
##                                          825 
##                                   VANKHOSUNG 
##                                          293 
##                                       VEDAMI 
##                                          203 
##                                   VEKUHO NEW 
##                                          339 
##                                   VEKUHO OLD 
##                                          552 
##                            VETERINARY COLONY 
##                                          582 
##                 VETUBA COLONY,YORUBA VILLAGE 
##                                          172 
##                               VIDIMA VILLAGE 
##                                          472 
##                                      VIHOKHU 
##                                          806 
##                           VIKHOZOU (KIGWEMA) 
##                                          624 
##                                      VIPHOMA 
##                                          347 
##                              VISABA (KIDIMA) 
##                                          728 
##                                      VISHEPU 
##                                          461 
##                             VISWEMA (K.KHEL) 
##                                         1963 
##                             VISWEMA (P.KHEL) 
##                                          844 
##                             VISWEMA (R.KHEL) 
##                                         1783 
##                             VISWEMA (Z.KHEL) 
##                                         2207 
##                                      VIYILHO 
##                                          391 
##                                       VIYITI 
##                                          180 
##                                       VIYIXE 
##                                          387 
##                                   VONGKITHEM 
##                                          233 
##                          VONGTSUVONG VILLAGE 
##                                          128 
##                               VONGVA VILLAGE 
##                                           99 
##                            WAGIM WARD MON HQ 
##                                          535 
##                             WAKCHING CHINGLA 
##                                          302 
##                                 WAKCHING HQ. 
##                                         1124 
##                             WAKCHING VILLAGE 
##                                         2344 
##                               WALFORD COLONY 
##                                          741 
##                           WALFORD COLONY E/W 
##                                         1012 
##                             WALO WARD MON HQ 
##                                         1216 
##                                      WAMEKEN 
##                                          379 
##                             WANCHING VILLAGE 
##                                         2261 
##                               WANGLA VILLAGE 
##                                          632 
##                      WANGSHU CHANGLU VILLAGE 
##                                          399 
##                              WANGSHU VILLAGE 
##                                         1373 
##                               WANGTI VILLAGE 
##                                         1122 
##                                       WANSOI 
##                                          415 
##                                       WAOSHU 
##                                          360 
##                                       WAPHUR 
##                                          556 
##                                     WAROMONG 
##                                         1255 
##                                 WAROMONG-III 
##                                          504 
##                            WAROMONG COMPOUND 
##                                          173 
##                              WASHELO VILLAGE 
##                                          100 
##                                      WATIYIM 
##                                          259 
##      WEST YARD (ARMY CAMP) CHOTESWARI COLONY 
##                                          770 
##                      WEST YARD (TOWARDS RLY) 
##                                          331 
##                     WEST YARD RLY. LINE AREA 
##                                          536 
##                              WETTING VILLAGE 
##                                          305 
##                        WEZHIO VILLAGE A/WING 
##                                          529 
##                        WEZHIO VILLAGE B/WING 
##                                          230 
##                                       WOCHAN 
##                                          159 
##                                   WOKHA TOWN 
##                                        14813 
##                            WOKHA VILLAGE - I 
##                                          947 
##                           WOKHA VILLAGE - II 
##                                          604 
##                          WOKHA VILLAGE - III 
##                                          629 
##                           WOKHA VILLAGE - IV 
##                                          495 
##                             WOKHA VILLAGE -V 
##                                          671 
##                                      WONGTHU 
##                                           69 
##                                       WOROKU 
##                                          260 
##                                 WOZHUYAN OLD 
##                                          165 
##                                          WUI 
##                                          550 
##                                 WUZU VILLAGE 
##                                          173 
##                                   XAMUNUBOTO 
##                                          638 
##                                        XUIVI 
##                                          541 
##                                   XUIVI - II 
##                                          398 
##                                      XUKHEPU 
##                                          303 
##                                XUVIHE COLONY 
##                                         1080 
##                              XUVISHE VILLAGE 
##                                           98 
##                                      Y.ANNER 
##                                          616 
##                               Y.ZHIMO COLONY 
##                                          526 
##                                     YACHEM A 
##                                          854 
##                  YACHEM A NUKSOSANG COMPOUND 
##                                          324 
##                                     YACHEM B 
##                                          584 
##                                     YACHEM C 
##                                          567 
##                                       YAJANG 
##                                          829 
##                                   YAJANG (A) 
##                                          489 
##                                   YAJANG C-I 
##                                          559 
##                                       YAKHUR 
##                                          730 
##                               YAKSHU VILLAGE 
##                                         1914 
##                                         YALI 
##                                          794 
##                                    YANGCHING 
##                                          398 
##                                  YANGCHING B 
##                                          279 
##                              YANGKANG SAKSHI 
##                                           63 
##                                       YANGPI 
##                                          939 
##                                   YANGPI - B 
##                                          906 
##                            YANGSEKYU VILLAGE 
##                                          139 
##                         YANGZITONG VILLAGE A 
##                                          992 
##                         YANGZITONG VILLAGE B 
##                                          538 
##                                      YANKELI 
##                                          235 
##                                       YANLUM 
##                                          115 
##                                       YANNYU 
##                                          551 
##                               YANPAN VILLAGE 
##                                          212 
##                                       YANPHA 
##                                          432 
##                                     YANTHAMO 
##                                          640 
##                                  YANTHAMO II 
##                                          363 
##                                YAONG VILLAGE 
##                                          395 
##                   YAONG VILLAGE LENYE MORUNG 
##                                          542 
##                                  YAONGYIMSEN 
##                                         1410 
##                            YAONGYIMSEN - III 
##                                          619 
##                         YAONGYIMSEN COMPOUND 
##                                          555 
##                               YAONGYIMTI NEW 
##                                          353 
##                               YAONGYIMTI OLD 
##                                          652 
##                              YAPHANG VILLAGE 
##                                           99 
##                                       YEHEMI 
##                                         1179 
##                                  YEI VILLAGE 
##                                          609 
##                                      YEMISHE 
##                                          414 
##                              YESHITO/YEVISHE 
##                                          129 
##                                    YESHOLUTO 
##                                          451 
##                                 YESI VILLAGE 
##                                           68 
##                                       YEVETO 
##                                          201 
##                                       YEZAMI 
##                                          507 
##                                    YEZASHIMI 
##                                          411 
##                                      YIKHANU 
##                                          255 
##                                   YIKHUM - I 
##                                          907 
##                                  YIKHUM - II 
##                                          731 
##                                 YIKHUM - III 
##                                          574 
##                                     YIMCHALU 
##                                           60 
##                                YIMCHENKIMONG 
##                                          999 
##                                       YIMKHA 
##                                          578 
##                                      YIMPANG 
##                                         1203 
##                                    YIMPARASA 
##                                          248 
##                                       YIMRUP 
##                                          603 
##                                        YIMYU 
##                                         1411 
##                                        YIMZA 
##                                           90 
##                            YINGPHIRE VILLAGE 
##                                          703 
##                     YINGSUNGNTSOMO (AGATITO) 
##                                          194 
##                           YISEMYONG COMPOUND 
##                                          657 
##                            YISISOTHA VILLAGE 
##                                          118 
##                                        YOKAO 
##                                          741 
##                                    YONCHUCHO 
##                                          438 
##                                       YONGAM 
##                                          719 
##                                     YONGAM A 
##                                          278 
##                             YONGHONG VILLAGE 
##                                          914 
##                             YONGKHAO VILLAGE 
##                                         1068 
##                              YONGLOK VILLAGE 
##                                          112 
##                                    YONGNYA A 
##                                          295 
##                    YONGNYA A PHAMJONG MORUNG 
##                                          338 
##                                    YONGNYA B 
##                                          538 
##                             YONGNYA COMPOUND 
##                                          392 
##                                   YONGNYAH E 
##                                          343 
##                             YONGNYAH VILLAGE 
##                                          323 
##                                  YONGPHANG A 
##                                          311 
##                                  YONGPHANG B 
##                                          449 
##                                  YONGPHANG C 
##                                          102 
##                                   YONGSHEI A 
##                                          674 
##                                   YONGSHEI B 
##                                          526 
##                       YORUBA VILLAGE A/ WING 
##                                          670 
##                       YORUBA VILLAGE B/ WING 
##                                          386 
##                        YORUBA VILLAGE C-WING 
##                                          623 
##                        YORUBA VILLAGE D-WING 
##                                          473 
##                                    YUKUMSANG 
##                                           96 
##                                       YUNGJA 
##                                          172 
##                             YUNGPHANG SECTOR 
##                                          254 
##                                        YUNYU 
##                                          528 
##                               YUTING VILLAGE 
##                                          938 
##                                        ZAKHO 
##                                          301 
##                            ZAKIESATUO COLONY 
##                                          544 
##                                  ZAKLUM WARD 
##                                          991 
##                                     ZANGKHAM 
##                                         1146 
##                      ZANGKHAM TINGSA VILLAGE 
##                                          138 
##                                         ZANI 
##                                          358 
##                              ZAONGER VILLAGE 
##                                          668 
##                        ZAPAMI VILLAGE A/WING 
##                                          435 
##                        ZAPAMI VILLAGE B/WING 
##                                          445 
##                                      ZAPHUMI 
##                                          106 
##                             ZAVACHHI VILLAGE 
##                                          287 
##                                ZELIANGRONG A 
##                                          932 
##                                ZELIANGRONG B 
##                                          752 
##                               ZELUME VILLAGE 
##                                          721 
##                                     ZEPHENYU 
##                                          662 
##                                   ZHADI BASA 
##                                          820 
##                                   ZHADI BAWE 
##                                          754 
##                                  ZHADI KIMHO 
##                                          811 
##                                ZHADIMA UPPER 
##                                          486 
##             ZHAVAME (ZHAMAI) VILLAGE A/ WING 
##                                          413 
##                       ZHAVAME VILLAGE C/WING 
##                                          605 
##                       ZHAVAMI VILLAGE D-WING 
##                                          509 
##                                      ZHEKIYE 
##                                          346 
##                                      ZHEKUTO 
##                                          159 
##                                     ZHEVISHE 
##                                          247 
##                                     ZHEYISHE 
##                                          210 
##                                  ZIENUOBADZE 
##                                          742 
##                                       ZIEZOU 
##                                          214 
##                                ZIPHU VILLAGE 
##                                          230 
##                                      ZISUNYU 
##                                          998 
##                                ZUBZA (SECHU) 
##                                          611 
##                             ZUBZA/SECHU - II 
##                                          662 
##                                     ZUIKHU A 
##                                          607 
##                                      ZUKETSA 
##                                          450 
##                                     ZUKHESHE 
##                                          161 
##                              ZUMKIUR VILLAGE 
##                                          380 
##                                       ZUNGTI 
##                                          404 
##                                        ZUTOI 
##                                          846 
##                                       ZUTOVI 
##                                          482 
##                               ZUTOVI VILLAGE 
##                                          414
```
