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
## [1] 213999
```

Unique Values in Sex:


```r
# Unique values in sex
table(andaman$sex)
```

```
## 
## Female   Male 
## 105247 108749
```

Summary of Age:


```r
# Age
summary(andaman$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##      18      31      39      42      50     119
```

No. of characters in ID:

```r
# Length of ID
table(nchar(andaman$id))
```

```
## 
##     10     11 
## 213998      1
```

Number of characters in pin code:


```r
table(nchar(andaman$pin_code))
```

```
## 
##      6 
## 173837
```


```r
# Net electors
sum(with(andaman, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 213999
```

```r
nrow(andaman)
```

```
## [1] 213999
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(andaman$elector_name))
```

```
## 
##     1     2     3     4     5     6     7     8     9    10    11    12 
##     1     1   274  2362  6197  9426  9142  9182 13967 20077 26811 31080 
##    13    14    15    16    17    18    19    20    21    22    23    24 
## 27240 20230 13506  8749  5823  4039  2582  1490   816   459   241   134 
##    25    26    27    28    29    30    31    32    34    35    36    37 
##    84    31    17    15     7     6     3     2     2     1     1     1
```

```r
andaman[which(nchar(andaman$elector_name) < 4), "filename"]
```

```
## # A tibble: 276 x 1
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
## # ... with 266 more rows
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
##           4191          28152          31831          11883          15819 
##     PORT BLAIR         RANGAT 
##          12243          23058
```

```r
table(andaman$district)
```

```
## 
##             2-BADA ENAKA          2-GANDHI STATUE             2-JETTY AREA 
##                      259                     1105                     1121 
##                 2-JHOOLA            2-MACHI BASTI                2-MALACCA 
##                      502                      757                      328 
##            2-MASALA TAPU                2-MILDERA          2-MODEL VILLAGE 
##                       93                      580                      288 
##                 2-RAMJAW           2-STADIUM AREA                 2-TAEELA 
##                      193                     1052                      926 
##     3-WOMENS HOSTEL AREA                  NICOBAR NORTH AND MIDDLE ANDAMAN 
##                      714                    13899                    64107 
##            SOUTH ANDAMAN 
##                   113282
```

```r
table(andaman$main_town)
```

```
## 
##      ABERDEEN BAZAR    ABERDEEN VILLAGE              ADAJIG 
##                 375                 476                 706 
##          AERIAL BAY            AFRA BAY             ALURONG 
##                 549                 102                 194 
##      ANARKALI BASTI               ARONG           AUSTIN-11 
##                 390                 702                 153 
##          BADA DABLA           BADAKHARI           BAKULTALA 
##                 262                 238                 495 
##          BAMBOOFLAT          BASANTIPUR          BEACH DERA 
##                3424                 632                 177 
##         BEADONA BAD             BENGALI           BHARATPUR 
##                 742                 274                 657 
##         BIG LAPATHY           BIMBLITAN           BINDRABAN 
##                 731                 558                1325 
##              BORANG           BRICHGUNJ         BUNIYADABAD 
##                  92                 763                1684 
##           BURMACHAD          BUTLER BAY          CADDLEGUNJ 
##                 202                 564                 658 
##             CALICUT         CAMPBELLBAY            CHAINPUR 
##                1399                2060                 494 
##             CHAMPIN            CHANGHUA          CHDIYATAPU 
##                 328                  93                 366 
##             CHINGAM          CHOTA INAK           CHOULDARI 
##                  48                 259                1589 
##           CHUKMACHI         Coffee Dera            COLINPUR 
##                 216                 130                 298 
##         CUTBERT BAY             DANAPUR              DARING 
##                 110                 638                 102 
##        DASTARATHPUR           DELANIPUR     DESHABANDHUGRAM 
##                 857                2199                 497 
##              DEVPUR          DHANIKHARI           DHARMAPUR 
##                 773                 495                 355 
##            DIGLIPUR           DOLLYGUNJ        DUGONG CREEK 
##                1024                1839                  54 
##          DUKE NAGAR         DUNDASPOINT            DURGAPUR 
##                1027                 415                 529 
##              E-WALL         E.B.KATCHAL                ENAM 
##                 138                 185                 161 
##          FERRARGUNJ        GANDHI NAGAR        GANESH NAGAR 
##                 986                 684                 527 
##         GARACHARAMA        GOVINDANAGAR          GOVINDAPUR 
##                3979                 685                 879 
##         GOVINDNAGAR           GUPTAPARA               HADDO 
##                1616                 842                4147 
##            HANSPURI        HAREN NALLAH          HARI NAGAR 
##                 273                 117                1016 
##      HARIDAS KATTAI       HARMINDER BAY          HASMATABAD 
##                 278                 834                1056 
##         HERBERTABAD               HITUI           HOPE TOWN 
##                 310                 128                1413 
##          HORREY BAY         HUMFREYGUNJ             HUT BAY 
##                 379                 509                4189 
##      JAGANNATH DERA              JAIPUR        JAPAN TIKREY 
##                 226                 649                 502 
##            JIRKATAG      JOGINDER NAGAR          JUNGLIGHAT 
##                 143                 577                5041 
##         KADAKACHANG           KADAMTALA              KAKANA 
##                 318                1107                 802 
##            KALIGHAT             KALIPUR         KALSI CHOWK 
##                1039                 459                 281 
##             KAMORTA          KANYAPURAM           KARMATANG 
##                 757                 870                1072 
##          KATAI DERA     KAUSHALYA NAGAR             KENYUKA 
##                1059                 882                 765 
##         KERALAPURAM         KHUDIRAMPUR             KIMIOUS 
##                 336                 993                 293 
##              KINMAI        KISHORINAGAR       KRISHNA NAGAR 
##                 406                 882                 599 
##         KRISHNAPURI            KUITASUK         LAKSHMANPUR 
##                 479                 926                 297 
##           LAMBALINE         LAXMI NAGAR            LAXMIPUR 
##                1369                 128                 805 
##         LONG ISLAND             LOROJIG             LUCKNOW 
##                 594                 203                 737 
##            MADHUPUR         MADHYAMGRAM            MAKACHUA 
##                1693                  78                  67 
##             MALACCA           MALAPURAM           MANGLUTAN 
##                1105                 373                1691 
##          MANNARGHAT              MANPUR             MATHURA 
##                 661                 694                 562 
##          MAYABUNDER  MEENAKSHI RAMNAGAR          MILAN GRAM 
##                 873                 209                 590 
##          MILE TILAK            MILLDERA          MINNIE BAY 
##                 500                 580                 602 
##              MINYUK          MITHAKHARI            MOHANPUR 
##                 171                1215                 480 
##           MOHANPURA               MUNAK                 MUS 
##                 415                 193                1121 
##            NABAGRAM          NAMUNAGHAR         NAYA KATTAI 
##                1402                1015                 164 
##            NAYAGAON            NAYAGARH          NAYASHAHAR 
##                2037                 396                 370 
##         NEIL KENDRA        NETAJI NAGAR            NILAMBUR 
##                 444                 797                 888 
##           NIMBUTALA        NISCHINTAPUR            OGRABRAJ 
##                1124                 188                 585 
##         ORAL KATCHA           PAHALGAON           PAHARGAON 
##                 417                1019                 460 
##          PANCHAWATI           PARANGARA           PARNASALA 
##                 401                 647                 732 
##        PASCHIMSAGAR               PERKA         PHOENIX BAY 
##                 720                1536                 522 
##         PHOLONALLAH            PILLOBHA          PILLOPATIA 
##                 150                  23                   7 
##           PILOPANJA           PILPILLOW        PINAKI NAGAR 
##                  72                 283                 848 
##          POKHA DERA           PORT MOUT          PROTHRAPUR 
##                 673                 823                 829 
##         PUDUMADURAI      RABINDRA NAGAR          RADHANAGAR 
##                 343                1914                 607 
##     RAMA KRISHNAPUR     RAMAKRISHNAGRAM            RAMNAGAR 
##                3083                2185                1291 
##              RAMPUR          RANGACHANG              RANGAT 
##                1389                 814                 880 
##          RANGAT BAY             RUTLAND              SABARI 
##                 491                  67                 797 
##         SAGAR DWEEP               SAWAI         SCHOOL LINE 
##                 417                 779                 494 
##          SHAKTIGARH            SHANTANU        SHANTI NAGAR 
##                 503                 755                 297 
##           SHANTIPUR       SHASTRI NAGAR             SHIBPUR 
##                 771                 149                 552 
##          SHIVAPURAM           SHOAL BAY SHOMPEN TRIBAL AREA 
##                 561                 844                  83 
##         SHORE POINT         SHYAM NAGAR           SIPPIGHAT 
##                1973                1431                1233 
##          SITA NAGAR       SMALL LAPATHY         SOUTH POINT 
##                1607                 691                5571 
##         STEWARTGUNJ       STRAIT ISLAND         SUBHAS GRAM 
##                 767                  27                2831 
##          SUNDARGARH       SWADESH NAGAR         SWARAJ GRAM 
##                 833                 917                 643 
##            TALBAGAN             TAMALOO           TAPOIMING 
##                 446                1052                1380 
##              TAPONG              TEETOP          TEYLERABAD 
##                 194                 388                1049 
##               TIRUR             TUGAPUR           TUSHNABAD 
##                 254                1444                1793 
##           URMILAPUR              UTTARA     VIDYASAGARPALLI 
##                 738                 818                 730 
##         VIJAY NAGAR           VIJAYGARH          VIJAYNAGAR 
##                 338                 310                 423 
##         VIKAS NAGAR     VIVEKANANDPURAM             WANDOOR 
##                 127                1012                1239 
##        WIMBERLYGUNJ          WRIGHT MYO 
##                1397                 424
```
