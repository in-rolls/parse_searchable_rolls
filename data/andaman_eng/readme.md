## Andaman

Basic descriptive statistics about the data. And sanity checks.


```r
andaman <- readr::read_csv("andaman.csv")
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
nrow(andaman)
```

```
## [1] 215815
```

Unique Values in Sex:


```r
# Unique values in sex
table(andaman$sex)
```

```
## 
## Female   Male 
## 106089 109723
```

Summary of Age:


```r
# Age
summary(andaman$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   18.00   31.00   39.00   42.04   50.00  119.00
```

No. of characters in ID:

```r
# Length of ID
table(nchar(andaman$id))
```

```
## 
##     10     11 
## 215814      1
```

Number of characters in pin code:


```r
table(nchar(andaman$pin_code))
```

```
## 
##      6 
## 175563
```


```r
# Net electors
sum(with(andaman, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 215815
```

```r
nrow(andaman)
```

```
## [1] 215815
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(andaman$elector_name))
```

```
## 
##     1     2     3     4     5     6     7     8     9    10    11    12 
##     1     1   277  2373  6240  9491  9195  9234 14065 20228 27029 31379 
##    13    14    15    16    17    18    19    20    21    22    23    24 
## 27479 20423 13629  8842  5881  4082  2611  1505   834   465   241   136 
##    25    26    27    28    29    30    31    32    34    35    36    37 
##    86    33    17    15     7     6     3     2     2     1     1     1
```

```r
andaman[which(nchar(andaman$elector_name) < 4), "filename"]
```

```
## # A tibble: 279 x 1
##    filename    
##    <chr>       
##  1 PART_354.pdf
##  2 PART_354.pdf
##  3 PART_354.pdf
##  4 PART_354.pdf
##  5 PART_354.pdf
##  6 PART_354.pdf
##  7 PART_354.pdf
##  8 PART_354.pdf
##  9 PART_354.pdf
## 10 PART_354.pdf
## # ... with 269 more rows
```

Basic admin. units:

```r
table(andaman$police_station)
```

```
## < table of extent 0 >
```

```r
table(andaman$mandal)
```

```
## 
##   CAMPBELL BAY       DIGLIPUR     FERRARGUNJ LITTLE ANDAMAN     MAYABUNDER 
##           4212          28911          32348          11894          15839 
##     PORT BLAIR         RANGAT 
##          12259          23162
```

```r
table(andaman$district)
```

```
## 
##             2-BADA ENAKA          2-GANDHI STATUE             2-JETTY AREA 
##                      259                     1109                     1123 
##                 2-JHOOLA            2-MACHI BASTI                2-MALACCA 
##                      503                      759                      328 
##            2-MASALA TAPU                2-MILDERA          2-MODEL VILLAGE 
##                       93                      581                      306 
##                 2-RAMJAW           2-STADIUM AREA                 2-TAEELA 
##                      193                     1062                      926 
##     3-WOMENS HOSTEL AREA                  NICOBAR NORTH AND MIDDLE ANDAMAN 
##                      725                    14049                    65008 
##            SOUTH ANDAMAN 
##                   113910
```

```r
table(andaman$main_town)
```

```
## 
##      ABERDEEN BAZAR    ABERDEEN VILLAGE              ADAJIG 
##                 377                 477                 708 
##          AERIAL BAY            AFRA BAY             ALURONG 
##                 549                 102                 194 
##      ANARKALI BASTI               ARONG           AUSTIN-11 
##                 390                 702                 153 
##          BADA DABLA           BADAKHARI           BAKULTALA 
##                 409                 238                 496 
##          BAMBOOFLAT          BASANTIPUR          BEACH DERA 
##                3427                 633                 178 
##         BEADONA BAD             BENGALI           BHARATPUR 
##                 742                 283                 664 
##         BIG LAPATHY           BIMBLITAN           BINDRABAN 
##                 747                 558                1330 
##              BORANG           BRICHGUNJ         BUNIYADABAD 
##                 111                 789                1685 
##           BURMACHAD          BUTLER BAY          CADDLEGUNJ 
##                 205                 564                 664 
##             CALICUT         CAMPBELLBAY            CHAINPUR 
##                1399                2060                 495 
##             CHAMPIN            CHANGHUA          CHDIYATAPU 
##                 328                  93                 370 
##             CHINGAM          CHOTA INAK           CHOULDARI 
##                  48                 259                1592 
##           CHUKMACHI         Coffee Dera            COLINPUR 
##                 216                 130                 298 
##         CUTBERT BAY             DANAPUR              DARING 
##                 110                 639                 102 
##        DASTARATHPUR           DELANIPUR     DESHABANDHUGRAM 
##                 860                2205                 503 
##              DEVPUR          DHANIKHARI           DHARMAPUR 
##                 774                 496                 355 
##            DIGLIPUR           DOLLYGUNJ        DUGONG CREEK 
##                1063                1839                  54 
##          DUKE NAGAR         DUNDASPOINT            DURGAPUR 
##                1027                 416                 529 
##              E-WALL         E.B.KATCHAL                ENAM 
##                 138                 185                 161 
##          FERRARGUNJ        GANDHI NAGAR        GANESH NAGAR 
##                1286                 686                 527 
##         GARACHARAMA        GOVINDANAGAR          GOVINDAPUR 
##                3984                 688                 879 
##         GOVINDNAGAR           GUPTAPARA               HADDO 
##                1618                 842                4151 
##            HANSPURI        HAREN NALLAH          HARI NAGAR 
##                 273                 117                1016 
##      HARIDAS KATTAI       HARMINDER BAY          HASMATABAD 
##                 284                 834                1063 
##         HERBERTABAD               HITUI           HOPE TOWN 
##                 310                 133                1417 
##          HORREY BAY         HUMFREYGUNJ             HUT BAY 
##                 635                 511                4196 
##      JAGANNATH DERA              JAIPUR        JAPAN TIKREY 
##                 228                 649                 503 
##            JIRKATAG      JOGINDER NAGAR          JUNGLIGHAT 
##                 143                 595                5054 
##         KADAKACHANG           KADAMTALA              KAKANA 
##                 324                1107                 816 
##            KALIGHAT             KALIPUR         KALSI CHOWK 
##                1065                 459                 297 
##             KAMORTA          KANYAPURAM           KARMATANG 
##                 759                 907                1073 
##          KATAI DERA     KAUSHALYA NAGAR             KENYUKA 
##                1059                 882                 781 
##         KERALAPURAM         KHUDIRAMPUR             KIMIOUS 
##                 337                 996                 295 
##              KINMAI        KISHORINAGAR       KRISHNA NAGAR 
##                 406                 883                 599 
##         KRISHNAPURI            KUITASUK         LAKSHMANPUR 
##                 482                 926                 297 
##           LAMBALINE         LAXMI NAGAR            LAXMIPUR 
##                1372                 129                 810 
##         LONG ISLAND             LOROJIG             LUCKNOW 
##                 594                 204                 745 
##            MADHUPUR         MADHYAMGRAM            MAKACHUA 
##                1697                  90                  67 
##             MALACCA           MALAPURAM           MANGLUTAN 
##                1109                 374                1698 
##          MANNARGHAT              MANPUR             MATHURA 
##                 664                 694                 563 
##          MAYABUNDER  MEENAKSHI RAMNAGAR          MILAN GRAM 
##                 876                 209                 599 
##          MILE TILAK            MILLDERA          MINNIE BAY 
##                 504                 581                 605 
##              MINYUK          MITHAKHARI            MOHANPUR 
##                 171                1219                 487 
##           MOHANPURA               MUNAK                 MUS 
##                 418                 193                1123 
##            NABAGRAM          NAMUNAGHAR         NAYA KATTAI 
##                1418                1024                 164 
##            NAYAGAON            NAYAGARH          NAYASHAHAR 
##                2040                 408                 372 
##         NEIL KENDRA        NETAJI NAGAR            NILAMBUR 
##                 444                 797                 937 
##           NIMBUTALA        NISCHINTAPUR            OGRABRAJ 
##                1126                 199                 594 
##         ORAL KATCHA           PAHALGAON           PAHARGAON 
##                 434                1019                 461 
##          PANCHAWATI           PARANGARA           PARNASALA 
##                 401                 648                 735 
##        PASCHIMSAGAR               PERKA         PHOENIX BAY 
##                 723                1560                 522 
##         PHOLONALLAH            PILLOBHA          PILLOPATIA 
##                 182                  23                   7 
##           PILOPANJA           PILPILLOW        PINAKI NAGAR 
##                  72                 285                 848 
##          POKHA DERA           PORT MOUT          PROTHRAPUR 
##                 673                 823                 842 
##         PUDUMADURAI      RABINDRA NAGAR          RADHANAGAR 
##                 343                1914                 608 
##     RAMA KRISHNAPUR     RAMAKRISHNAGRAM            RAMNAGAR 
##                3086                2187                1292 
##              RAMPUR          RANGACHANG              RANGAT 
##                1391                 816                 880 
##          RANGAT BAY             RUTLAND              SABARI 
##                 495                  67                 797 
##         SAGAR DWEEP               SAWAI         SCHOOL LINE 
##                 444                 784                 496 
##          SHAKTIGARH            SHANTANU        SHANTI NAGAR 
##                 503                 755                 308 
##           SHANTIPUR       SHASTRI NAGAR             SHIBPUR 
##                 771                 150                 552 
##          SHIVAPURAM           SHOAL BAY SHOMPEN TRIBAL AREA 
##                 561                 880                  83 
##         SHORE POINT         SHYAM NAGAR           SIPPIGHAT 
##                1973                1433                1236 
##          SITA NAGAR       SMALL LAPATHY         SOUTH POINT 
##                1665                 701                5583 
##         STEWARTGUNJ       STRAIT ISLAND         SUBHAS GRAM 
##                 781                  27                2884 
##          SUNDARGARH       SWADESH NAGAR         SWARAJ GRAM 
##                 835                 918                 643 
##            TALBAGAN             TAMALOO           TAPOIMING 
##                 451                1062                1384 
##              TAPONG              TEETOP          TEYLERABAD 
##                 194                 406                1051 
##               TIRUR             TUGAPUR           TUSHNABAD 
##                 254                1446                1802 
##           URMILAPUR              UTTARA     VIDYASAGARPALLI 
##                 738                 818                 734 
##         VIJAY NAGAR           VIJAYGARH          VIJAYNAGAR 
##                 338                 310                 423 
##         VIKAS NAGAR     VIVEKANANDPURAM             WANDOOR 
##                 127                1013                1241 
##        WIMBERLYGUNJ          WRIGHT MYO 
##                1431                 431
```
