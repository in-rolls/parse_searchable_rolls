## Mizoram

Basic descriptive statistics about the data. And sanity checks.


```r
mizoram <- readr::read_csv("mizoram.csv")
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
##   pin_code = col_integer(),
##   net_electors_male = col_integer(),
##   net_electors_female = col_integer(),
##   net_electors_total = col_integer()
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
## Warning: 587 parsing failures.
## row # A tibble: 5 x 5 col     row col      expected   actual     file          expected   <int> <chr>    <chr>      <chr>      <chr>         actual 1  3830 house_no an integer DELETED 13 'mizoram.csv' file 2  3897 house_no an integer DELETED 29 'mizoram.csv' row 3  3939 house_no an integer DELETED 41 'mizoram.csv' col 4  3984 house_no an integer DELETED 54 'mizoram.csv' expected 5  4037 house_no an integer DELETED 68 'mizoram.csv'
## ... ................. ... .................................................... ........ .................................................... ...... .................................................... .... .................................................... ... .................................................... ... .................................................... ........ ....................................................
## See problems(...) for more details.
```

Number of rows:


```r
nrow(mizoram)
```

```
## [1] 740508
```

Unique Values in Sex:


```r
# Unique values in sex
table(mizoram$sex)
```

```
## 
## Female   male   Male 
## 378532     83 361893
```

Summary of Age:


```r
# Age
summary(mizoram$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
##    1.00   26.00   34.00   37.63   47.00  673.00       4
```

Check if 0 and missing age is from problem in the electoral roll:


```r
mizoram[which(mizoram$age == 1), c("id", "filename")]
```

```
## # A tibble: 1 x 2
##   id         filename        
##   <chr>      <chr>           
## 1 CRG0092387 AC040PART016.pdf
```

No. of characters in ID:

```r
# Length of ID
table(nchar(mizoram$id))
```

```
## 
##      9     10     11     12     14 
##     19 740325     60      1      1
```

Number of characters in pin code:


```r
table(nchar(mizoram$pin_code))
```

```
## 
##      6 
## 740508
```

Are IDs duplicated?


```r
length(unique(mizoram$id))
```

```
## [1] 738805
```

```r
nrow(mizoram)
```

```
## [1] 740508
```


```r
# Net electors
sum(with(mizoram, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 740508
```

```r
nrow(mizoram)
```

```
## [1] 740508
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(mizoram$elector_name))
```

```
## 
##      3      4      5      6      7      8      9     10     11     12 
##     70   2300   4353   9949  23224  36183  44419  89503 121388  91784 
##     13     14     15     16     17     18     19     20     21     22 
##  79341  63744  40639  34178  29659  23146  17150  10963   6846   4467 
##     23     24     25     26     27     28     29     30     31     32 
##   2742   1653   1027    685    423    255    185    115     52     27 
##     33     34     35     36     39     41     43 
##     16      9      5      5      1      1      1
```

```r
mizoram[which(nchar(mizoram$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 70 x 2
##    id         filename        
##    <chr>      <chr>           
##  1 JDF0050377 AC023PART029.pdf
##  2 MWQ0093005 AC034PART013.pdf
##  3 IMS0029850 AC036PART004.pdf
##  4 HJC0111104 AC001PART013.pdf
##  5 ACH0014472 AC001PART013.pdf
##  6 CRG0163311 AC040PART024.pdf
##  7 DSP0200071 AC037PART063.pdf
##  8 DSP0197293 AC037PART010.pdf
##  9 IMS0035535 AC036PART021.pdf
## 10 CZK0175513 AC040PART002.pdf
## # ... with 60 more rows
```

Does district have a number?

```r
sum(grepl('[0-9]', mizoram$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(mizoram$parl_constituency)
```

```
## 
## 1 - Mizoram (ST) 1 - MIZORAM (ST)     Mizoram (ST)     MIZORAM (ST) 
##           203867           498268              456            37917
```

```r
table(mizoram$ac_name)
```

```
## 
##             1 - HACHHEK (ST)     10 - AIZAWL NORTH I (ST) 
##                        22847                        18378 
##    11 - AIZAWL NORTH II (ST)   12 - AIZAWL NORTH III (ST) 
##                        16907                        18141 
## 13 - AIZAWL EAST I (General)     14 - AIZAWL EAST II (ST) 
##                        17509                        13881 
##      15 - AIZAWL WEST I (ST)     16 - AIZAWL WEST II (ST) 
##                        22920                        17121 
##    17 - AIZAWL WEST III (ST)     18 - AIZAWL SOUTH I (ST) 
##                        15459                        14063 
##    19 - AIZAWL SOUTH II (ST)               2 - DAMPA (ST) 
##                        23131                        16134 
##   20 - AIZAWL SOUTH III (ST)           21 - LENGTENG (ST) 
##                        19065                        16799 
##           22 - TUICHANG (ST)     23 - CHAMPHAI NORTH (ST) 
##                        15877                        18211 
##     24 - CHAMPHAI SOUTH (ST)        25 - EAST TUIPUI (ST) 
##                        17156                        14427 
##           26 - SERCHHIP (ST)             27 - TUIKUM (ST) 
##                        17217                        15127 
##         28 - HRANGTURZO (ST)       29 - SOUTH TUIPUI (ST) 
##                        15279                        14284 
##               3 - MAMIT (ST)      30 - LUNGLEI NORTH (ST) 
##                        20476                        15689 
##       31 - LUNGLEI EAST (ST)       32 - LUNGLEI WEST (ST) 
##                        14279                        13842 
##      33 - LUNGLEI SOUTH (ST)            34 - THORANG (ST) 
##                        16197                        12792 
##        35 - WEST TUIPUI (ST)          36 - TUICHAWNG (ST) 
##                        13660                        26521 
##     37 - LAWNGTLAI WEST (ST)     38 - LAWNGTLAI EAST (ST) 
##                        25308                        22877 
##              39 - SAIHA (ST)             4 - TUIRIAL (ST) 
##                        18597                        16479 
##              40 - PALAK (ST)             5 - KOLASIB (ST) 
##                        17503                        20936 
##              6 - SERLUI (ST)             7 - TUIVAWL (ST) 
##                        18086                        15855 
##            8 - CHALFILH (ST)                9 - TAWI (ST) 
##                        18037                        15068 
##      AIZAWL EAST I (General)          AIZAWL EAST II (ST) 
##                         4444                         3398 
##          AIZAWL NORTH I (ST)         AIZAWL NORTH II (ST) 
##                         3746                         5083 
##          AIZAWL SOUTH I (ST)           AIZAWL WEST I (ST) 
##                         6875                          527 
##          AIZAWL WEST II (ST)         AIZAWL WEST III (ST) 
##                         2639                         5190 
##                   DAMPA (ST)                   SAIHA (ST) 
##                         1404                         1837 
##               TUICHAWNG (ST)             WEST TUIPUI (ST) 
##                         2774                          456
```

```r
table(mizoram$police_station)
```

```
## 
##        AIZAWL       Bairabi       BAIRABI     Bawngkawn     BAWNGKAWN 
##        115200          4108           371          4369         74973 
##   BORAPANSURY      BUNGHMUN      CHAMPHAI      CHAWNGTE       DARLAWN 
##          5627          4350         49794          9015         15799 
##     HNAHTHIAL       KANHMUN       Kawnpui      KAWRTHAH      Khawzawl 
##         14353          8907         12273         13446          1670 
##      KHAWZAWL       Kolasib      KULIKAWN     LAWNGTLAI       LUNGLEI 
##         19910         21622         34610         35004         54169 
##       LUNGSEN         MAMIT       MARPARA N. Vanlaiphai         NGOPA 
##          7974          9107          7663          8330         12766 
##         SAIHA       SAIRANG       SAITUAL     SAKAWRDAI        SANGAU 
##         25952          8536         18290          6869         12796 
##      Serchhip       SIALSUK      Thenzawl      THINGSAI       TLABUNG 
##         29302          5738          5883          4190         16163 
##       TUIPANG     Vairengte     VAIVAKAWN    VASEITLANG    W.PHAILENG 
##         11985         15567          2366         15038         16423
```

```r
table(mizoram$mandal)
```

```
## 
##         AIBAWK   BILKHAWTHLIR       BUNGHMUN      BUNGTLANG       CHAMPHAI 
##          13252          37218          10408          11237          29827 
##       CHAWNGTE        DARLAWN     E. Lungdar      HNAHTHIAL       KHAWBUNG 
##          29295          19088          10488          18781          14427 
##       Khawzawl       KHAWZAWL      LAWNGTLAI        LUNGLEI        LUNGSEN 
##           1670          24670          24152          50989          21021 
##          NGOPA        PHULLEN          REIEK          SAIHA         SANGAU 
##          13546          10118          11805          23645          12796 
##       Serchhip      THINGDAWL Thingsulthliah THINGSULTHLIAH      TLANGNUAM 
##          33027          18283           2438          19754         215225 
##        TUIPANG     W.PHAILENG       ZAWLNUAM 
##          14292          18246          30810
```

```r
table(mizoram$district)
```

```
## 
##    AIZAWL  CHAMPHAI   KOLASIB LAWNGTLAI     MAMIT     SAIHA 
##    273013     80129     53701     74970     55917     32353
```

```r
table(mizoram$main_town)
```

```
## 
##                ADUBANGASORA                      Ahmypi 
##                         189                         103 
##                      AIBAWK                    AIDUZAWL 
##                        1052                         196 
##                     AILAWNG                       AINAK 
##                         473                         416 
##                      Aithur                      AIZAWL 
##                         106                      203909 
##                 AJASORA - I                  ANDERMANIK 
##                        1036                         593 
##                    AOC VENG                   ARCHHUANG 
##                         821                         420 
##                        ARRO                     BAIRABI 
##                         107                        2791 
##                   BAJEISORA             BAJIRUNGPA VENG 
##                         915                         593 
##                    Baktawng                  Bandiasora 
##                        2239                         400 
##                 BANDUKBANGA                   Bawktlang 
##                         601                         214 
##                      BAWLTE                   BAWNGTHAH 
##                         203                         278 
##                     BELKHAI           Belpei (Matisora) 
##                         273                         522 
##                     Belthei                       Biate 
##                         259                        1670 
##                BILKHAWTHLIR                    BILOSORA 
##                        3239                         233 
##                    BOLISORA                 BORAGUISURY 
##                         454                         320 
##               BORAKABAKHALI             BORAPANSURY - I 
##                         357                        1075 
##            BORAPANSURY - II                    BORKOLOK 
##                         998                         432 
##                     BUALPUI           BUALPUI- I (EAST) 
##                         755                        1031 
##          BUALPUI - I (WEST)                   Bualpui H 
##                         815                         552 
##                   Bualpui V                       BUANG 
##                         339                         268 
##                    Buangpui                     Buarpui 
##                         267                         952 
##                      BUHBAN                BUHCHANGPHAI 
##                         442                         588 
##                 Buhkangkawn                      BUILUM 
##                          71                         274 
##                     Buknuam                      BUKPUI 
##                         158                         772 
##                   BUKVANNEI                  BULFEKZAWL 
##                         497                         223 
##                    Bunghmun                    BUNGHMUN 
##                         673                         870 
##                   BUNGTHUAM                   Bungtlang 
##                         593                        1401 
##             BUNGTLANG SOUTH                    BUNGZUNG 
##                        1507                         704 
##                      Bymari                      C.T.I. 
##                         244                         448 
##                    CHAKHANG                  CHAKHEITLA 
##                         768                         192 
##                    CHALRANG               CHAMDUR P - I 
##                         495                         330 
##            CHAMDURTLANG - I           CHAMDURTLANG - II 
##                         335                          68 
##                    CHAMPHAI                    CHAMRING 
##                       22371                         204 
##              CHANDMARY - II                    Changpui 
##                         615                         294 
##                   CHANGZAWL                      CHAPUI 
##                         347                         576 
##                 CHAPUI - II                CHARLUITLANG 
##                         158                         101 
##                   CHAWILUNG                 Chawilung S 
##                         336                         213 
##                  Chawngte L                  CHAWNGTE P 
##                         673                         914 
##                 CHAWNGTELUI                  CHAWNGTLAI 
##                         225                        1180 
##                 CHAWNGTUI E                 Chawngtui S 
##                         151                         361 
##                     CHAWNHU               CHAWNTLANGPUI 
##                         415                         236 
##                     Chekawn    Chengkawllui (Samuksuri) 
##                         192                         456 
##                    Chengpui                    Cherhlun 
##                          78                        1627 
##                     CHEURAL               CHHANCHHUAHNA 
##                         823                          95 
##                   CHHAWRTUI                    CHHEIHLU 
##                         696                         293 
##                 Chhingchhip                   Chhipphir 
##                        2591                         965 
##           CHHOTAGUISURY - I               CHHOTAPANSURY 
##                         658                         597 
##              CHHUARLUNG- II              CHHUARLUNG - I 
##                         174                         600 
##                   Chhumkhum                    CHIAHPUI 
##                         109                         608 
##                  CHIKHURLUI                      CHILUI 
##                         212                         457 
##                     Chithar                     CHUHVEL 
##                         175                         677 
##                  CHUNGTLANG                COLLEGE VENG 
##                         306                        1377 
##                COUNCIL VENG                       DAIDO 
##                        1330                         393 
##                      DAMLUI                DAMPARENGPUI 
##                         367                        1551 
##                      Dampui                      DAMPUI 
##                          28                         555 
##                      DARLAK                     DARLAWN 
##                         869                        2965 
##                    Darlawng                     DARLUNG 
##                         394                         666 
##                 DARNAMTLANG                  Darngawn W 
##                         180                         298 
##                       Darzo                        Dawn 
##                         993                         229 
##                     Dengsur                    Devasora 
##                         283                         386 
##              DEVASORA NORTH                     DILKAWN 
##                         626                         537 
##                     DILKHAN              DILTLANG SOUTH 
##                         175                         828 
##                     DILZAWL                   Duduksora 
##                         164                         279 
##                       DULTE                 DUMZAUTLANG 
##                         627                         133 
##                   DUNGTLANG                  E. Lungdar 
##                         565                        2171 
##                 E. PHAILENG                     FALKAWN 
##                         874                         937 
##                  FANGFARLUI                   FARKAWN I 
##                         187                         867 
##                  FARKAWN II                     FULTULI 
##                         891                         374 
##                     FUTSURY               GERAGULUKSORA 
##                         423                         226 
##                    GERASURY              GULSINGBAPSORA 
##                         343                         211 
##                  Haulawng I                    Hauruang 
##                        1637                         810 
##                  HLIAPPUI I                 HLIAPPUI II 
##                         545                         601 
##                      Hlumte                    HMAWNGBU 
##                         112                         529 
##              HMAWNGBUCHHUAH                  Hmawngkawn 
##                         310                         116 
##                    HMUIFANG                   HMUNCHENG 
##                         203                         171 
##                     HMUNLAI                   HMUNNGHAK 
##                         328                         243 
##                    HMUNNUAM                     HMUNPUI 
##                         317                         740 
##                     Hmuntha                    Hmunthar 
##                         493                          85 
##                   Hmuntlang                    Hmunzawl 
##                          89                         305 
##                   HNAHLAN I                  HNAHLAN II 
##                         994                         879 
##                   Hnahthial                      HNAHVA 
##                        5319                         550 
##                     HORTOKI                  HRIANGHMUN 
##                        1902                         425 
##                 Hriangtlang                     HRIPHAW 
##                         380                         803 
##                   HRUAIKAWN                 HRUAITLUANG 
##                         227                         267 
##                     HRUIDUK                  HRUITEZAWL 
##                         473                         327 
##                 HUALNGOHMUN                      Hualtu 
##                         581                         667 
##               JARULDUBASORA                   JARULSURY 
##                         528                         523 
##                   JOGNASURY                    K.SARALI 
##                         613                         440 
##                      Kaisih                  KAKICHHUAH 
##                         326                         163 
##                    Kalapani             KAMALANAGAR - I 
##                         474                        1298 
##            KAMALANAGAR - II           KAMALANAGAR - III 
##                        1511                        1263 
##            KAMALANAGAR - IV                     KAMTULI 
##                         673                         331 
##                   KANANTHAR                    KANGHMUN 
##                         347                         764 
##                  Kanghmun S                     KANHMUN 
##                         368                        1084 
##                      KARLUI         Kawizau (Diblibagh) 
##                         568                        1048 
##                     KAWLBEM               KAWLCHAW EAST 
##                         877                         592 
##               KAWLCHAW WEST                    Kawlhawk 
##                         373                          95 
##                  KAWLKULH I                 KAWLKULH II 
##                         607                         717 
##                KAWLKULH III                    KAWNMAWI 
##                         805                         635 
##                     KAWNPUI                   Kawnpui W 
##                        4890                          91 
##              KAWRTETHAWVENG                    KAWRTHAH 
##                        1449                        1965 
##                KAWRTHINDENG                      Keitum 
##                         394                        1340 
##                     KELKANG                      KELSIH 
##                         674                         513 
##                      KEPRAN                     KHAIKHY 
##                         584                          93 
##                    KHAMRANG                    KHANKAWN 
##                         312                         406 
##                     KHANPUI                   KHANTLANG 
##                        1070                         293 
##                     Khawbel                  KHAWBUNG I 
##                         383                         713 
##                 KHAWBUNG II                     KHAWHAI 
##                         732                        1755 
##                    KHAWHNAI                     Khawhri 
##                         310                         244 
##                    KHAWKAWN                 Khawlailung 
##                         628                        1576 
##                   Khawlek S                    KHAWLIAN 
##                          91                        1345 
##                    Khawmawi                    KHAWPUAR 
##                         588                         327 
##                  KHAWRIHNIM                 KHAWRUHLIAN 
##                         621                        1574 
##                    KHAWZAWL                  Khojoysuri 
##                        7423                         524 
##                      Khopai                     KHUALEN 
##                         410                         150 
##                  KHUANGLENG                  KHUANGPHAH 
##                        1071                         399 
##                 KHUANGTHING                    Khumtung 
##                         906                         819 
##                    KOLALIAN                     KOLASIB 
##                         543                       16828 
##                 KUKURDULEYA               KURBALOVASORA 
##                         449                         540 
##                      LAILAK                   Laisawral 
##                         346                         347 
##                    LAITLANG                        Laki 
##                         124                         708 
##                      LALLEN                Lalmona Veng 
##                         609                         123 
##                    Lalnutui                    LAMCHHIP 
##                         119                         553 
##                     LAMHERH                     Lamthai 
##                         369                         846 
##                     LAMZAWL                    Lawngban 
##                         255                         374 
##               LAWNGTLAI - I      LAWNGTLAI - II (BAZAR) 
##                        1929                        1665 
##             LAWNGTLAI - III LAWNGTLAI - IV ( CHANDMARY) 
##                        2158                        2384 
##                    LEISENZO                       Leite 
##                         575                         553 
##                     LEITHUM                     LENCHIM 
##                         395                         225 
##                        Leng                     LENGPUI 
##                         536                        2201 
##                      LENGTE                   Lianbuang 
##                         352                         153 
##                  LIANDOPHAI                     LIANPUI 
##                         629                         414 
##                      Liapha                       LOHRY 
##                         154                         169 
##                   LOKKISURY                      Lomasu 
##                         271                         174 
##                 LONGPUIGHAT                   LUANGPAWN 
##                        1189                         341 
##          Luihausa (Malsuri)                     LUIMAWI 
##                         479                         323 
##                     LUNGBUN                    Lungchem 
##                         620                         265 
##                  Lungchhuan                     LUNGDAI 
##                         466                        1402 
##                   Lungdai S                     Lungdar 
##                         156                         165 
##                   LUNGHAUKA                   Lungkawlh 
##                         319                         521 
##                     Lunglei                    LUNGLENG 
##                       35689                         613 
##                  Lungleng S                    Lungmawi 
##                         104                         181 
##                    LUNGMUAT                    LUNGPHER 
##                         435                        1066 
##                     Lungpho                    LUNGPHUN 
##                         592                         429 
##                LUNGPHUNLIAN                Lungpuitlang 
##                         221                         130 
##                     Lungpuk                  Lungrang S 
##                         585                         810 
##                     LUNGSEI                     Lungsen 
##                         182                        1640 
##                     LUNGSUM                     LUNGTAN 
##                         333                         416 
##                LUNGTIAN - I               LUNGTIAN - II 
##                         764                         327 
##                 LUNGZARHTUM                  M. KAWNPUI 
##                         689                         639 
##                       MAILA                       MAITE 
##                         167                         594 
##                       MAMIT                      MAMPUI 
##                        4916                         706 
##                       Mamte           MANIABAPSORA - II 
##                         353                         584 
##                   MARPARA N                   Marpara S 
##                         994                        1311 
##              MAUBAWK L & CH                    MAUBUANG 
##                         636                         475 
##                     MAUCHAR                      Mausen 
##                         624                         148 
##                    Mautlang                    MAUTLANG 
##                         123                         214 
##                      Mauzam                      MAWHRE 
##                         210                         424 
##                      MEIDUM                      MELBUK 
##                         481                         337 
##                     MELRIAT                       Miepu 
##                         813                         172 
##                   MIMBUNG I                  MIMBUNG II 
##                         644                         784 
##                 MONDIRASORA                     MONTOLA 
##                         379                         398 
##                    MUALBU L                   Mualcheng 
##                         249                         934 
##                 Mualcheng S                    MUALKAWI 
##                         572                         458 
##                   MUALKHANG                 Muallianpui 
##                         252                         707 
##                 MUALLUNGTHU                   MUALPHENG 
##                         875                         552 
##                   MUALTHUAM                 Mualthuam N 
##                         532                        1006 
##                 Mualthuam S                     MUALVUM 
##                         323                         717 
##                      MURLEN                       MUTHI 
##                         291                         596 
##              N. KHAWDUNGSEI                  N. KHAWLEK 
##                         142                         552 
##                 N. LUNGLENG                 N. LUNGPHER 
##                         536                         594 
##                  N. SERZAWL               N. Vanlaiphai 
##                         451                        2454 
##                  N.CHAWNPUI                N.CHHIMLUANG 
##                         251                         243 
##                  N.DILTLANG              N.E. TLANGNUAM 
##                         196                         400 
##           N.E.KHAWDUNGSEI I          N.E.KHAWDUNGSEI II 
##                         705                         706 
##                    N.HLIMEN                  N.KHAWBUNG 
##                         767                         584 
##                 N.THINGLIAN                         N/A 
##                         200                         306 
##                 NAGDARASORA                     NALZAWL 
##                         210                         825 
##                      NAUSEL                    NEIHDAWN 
##                         229                         421 
##                     Neihloh                NEW CHALRANG 
##                         207                         432 
##                New Chhippui                    NEW EDEN 
##                          85                         273 
##               NEW HRUAIKAWN           NEW JOGNASURY - I 
##                          89                         720 
##          NEW JOGNASURY - II                 New Khawlek 
##                         249                          93 
##              New Khojoysuri                  NEW LATAWH 
##                         578                         432 
##              New Ngharchhip                  New Sachan 
##                         257                         322 
##                 NEW SERKAWR                  NEW VERVEK 
##                         102                         556 
##              NEW W.PHAILENG                    NGAIZAWL 
##                        1404                         448 
##                 NGENGPUIKAI               NGENGPUITLANG 
##                         448                         431 
##                   Ngentiang                  NGHALCHAWM 
##                         387                         299 
##                  NGHALIMLUI                  Ngharchhip 
##                         605                         172 
##                     NGOPA I                    NGOPA II 
##                         958                         876 
##                   NGOPA III                NGUNLINGKHUA 
##                         935                         179 
##                        NGUR                  NIAWHTLANG 
##                         947                        1211 
##                     NISAPUI                     Nunsuri 
##                         625                         993 
##               Old Bajeisora                     PAITHAR 
##                          82                         516 
##                     PALSANG                    PAMCHUNG 
##                         276                         183 
##                 PANDAWNGLUI                 PANGBALKAWN 
##                         290                         497 
##                    PANGKHUA                  Pangzawl I 
##                         928                        1831 
##                   PARVA - I                  PARVA - II 
##                         986                         295 
##                 PARVA - III                    PARVATUI 
##                         272                         250 
##                    PAWLRANG                     PEHLAWN 
##                         674                         537 
##                  Phaileng S                    PHAINUAM 
##                         188                         789 
##             Phairuangchhuah                Phairuangkai 
##                         398                         718 
##                     PHAISEN                     PHAIZAU 
##                         524                         242 
##                   PHALHRANG                  PHUAIBUANG 
##                         257                        1676 
##                 PHULDUNGSEI                     PHULLEN 
##                        1111                        1397 
##                    Phulmawi                     PHULPUI 
##                         189                         770 
##                       Phura                       Piler 
##                         772                         277 
##                    Puankhai                       PUILO 
##                         478                         296 
##                     PUKZING            PUKZING VENGTHAR 
##                         327                         214 
##                 Putlungasih                   R. VANHNE 
##                         869                         218 
##                      RABUNG                 RAJIV NAGAR 
##                        1051                        1922 
##                   RAJMANDAL                    Ralvawng 
##                         272                         284 
##                   Ramlaitui                      Rangte 
##                         385                         540 
##                        RATU                     RAWLBUK 
##                        1686                         357 
##                   RAWMIBAWK                      Rawpui 
##                         389                         575 
##                 RAWPUICHHIP                       REIEK 
##                         313                        1211 
##                   RENGASHYA                     RENGDIL 
##                         516                        1367 
##                  RENGTEKAWN                   RIANGTLEI 
##                         986                         287 
##                    RIASIKAH                       Rolui 
##                          95                         188 
##                   Rotlang E                   Rotlang W 
##                         460                         325 
##                   Rualalung                     RULKUAL 
##                         287                         338 
##                      Rullam                  RULPUIHLIM 
##                         341                         291 
##                     Runtung               S. Vanlaiphai 
##                         106                        1356 
##                S.CHHIMLUANG                    S.SABUAL 
##                         339                         396 
##                 SABUALTLANG                      Sachan 
##                         236                         231 
##                     SAIBAWH                     SAICHAL 
##                         530                         671 
##                       SAIHA                    SAIHAKAI 
##                       16506                         197 
##                  SAIHAPUI K                  SAIHAPUI V 
##                         562                         177 
##                      SAIKAH                SAIKHAWTHLIR 
##                         355                         635 
##                 SAIKHUMPHAI                      SAILAM 
##                         112                         616 
##                      Sailen                    Sailulak 
##                          70                         619 
##                    SAILUTAR                     SAIPHAI 
##                         356                        1213 
##                      SAIPUM                     SAIRANG 
##                        1519                        3349 
##                      Sairep                     SAITHAH 
##                         162                         927 
##                     SAITLAW                     SAITUAL 
##                         244                        8034 
##                SAIZAWH EAST                SAIZAWH WEST 
##                         175                         341 
##                   SAKAWRDAI                SAKEILUI - I 
##                        1738                         150 
##               SAKEILUI - II                   SAMLUKHAI 
##                         273                         953 
##                    SAMTHANG                    SAMTLANG 
##                         696                         633 
##                  SANGAU - I                 SANGAU - II 
##                         874                         457 
##                SANGAU - III                      SATEEK 
##                        1447                         700 
##                     SAWLENG                       SAZEP 
##                        1104                         385 
##                      Sekhum                   SEKULHKAI 
##                         231                          93 
##                       SELAM                      SELING 
##                         597                        1661 
##                 SENTETFIANG                    SENTLANG 
##                         153                         277 
##                    Serchhip                     SERHMUN 
##                       14184                         623 
##                     SERKAWR                     SERKHAN 
##                         824                         516 
##                      SERLUI                       Serte 
##                         388                         294 
##                 Sertlangpui                      Sesawm 
##                         332                         267 
##                     SESAWNG                       SESIH 
##                        2146                         778 
##                SIACHANGKAWN                     Sialhau 
##                         645                         336 
##                  SIALHAWK I                 SIALHAWK II 
##                         776                         796 
##                     Sialsir                     SIALSUK 
##                         223                        1510 
##                       SIASI                       SIATA 
##                         202                         643 
##                     SIATLAI                       SIHFA 
##                         242                         765 
##                     SIHPHIR            SIHPHIR VENGHLUN 
##                        2945                        1988 
##                   SIHTHIANG                 SIHTLANGPUI 
##                         947                         339 
##                      Silkur                    Silosora 
##                         417                         515 
##                    SILOSORA                     SILSURI 
##                         145                        1459 
##                     SILSURY                   SIMEISURY 
##                         482                         176 
##                      Sotapa                SUANGPUILAWN 
##                         110                        1339 
##                   SUARHLIAP                    Sumasumi 
##                         371                         140 
##                    SUMSILUI                     SUMSUIH 
##                         781                         590 
##                 SUNHLUCHHIP                       Supha 
##                         334                          62 
##                   T. DUMZAU                     TACHHIP 
##                         184                         798 
##                  TAITAWKAWN                      Tarpho 
##                          51                         221 
##                   Tawipui N                Tawipui N-II 
##                         425                         567 
##                   Tawipui S                      TAWIZO 
##                         953                         255 
##                    TEIKHANG                   Terabonia 
##                        1042                         167 
##                    THAIDAWR                    Thaizawl 
##                         662                         530 
##                   THALTLANG                THANGLAILUNG 
##                         373                         544 
##                     Thangte                Thanzamasora 
##                         178                         222 
##                     Thehlep                      THEIRI 
##                          41                         453 
##                      THEIVA                     THEKPUI 
##                         457                         188 
##                      THEKTE                    Thenhlum 
##                         286                         724 
##                   Thentlang                    Thenzawl 
##                         455                        5409 
##                       THIAK                   Thiltlang 
##                         591                         840 
##                   THINGDAWL                    Thingfal 
##                        2275                        1068 
##                   THINGHLUN                    THINGKAH 
##                         484                         847 
##                   Thinglian                    Thingsai 
##                         265                        1529 
##                    THINGSAT              THINGSULTHLIAH 
##                         148                        2678 
##                  THINGTHELH                   Thlengang 
##                         321                         114 
##                    Thualthu                    Thuampui 
##                         378                         303 
##              TIALDAWNGILUNG                    TINGHMUN 
##                         252                         602 
##                  Tiperaghat                     Tlabung 
##                         915                        3373 
##                  TLANGKHANG                   TLANGNUAM 
##                         168                         940 
##                    TLANGPUI                    Tlungvel 
##                         553                        1855 
##                  Tongkolong                    TUAHZAWL 
##                         356                         320 
##                    TUALBUNG                   TUALCHENG 
##                         558                         499 
##                     TUALPUI                      TUALTE 
##                         401                         804 
##                   Tuichawng              TUICHAWNGTLANG 
##                        1401                         370 
##                      TUIDAM               Tuidangchhuah 
##                        1210                         231 
##                TUIDANGTLANG                     Tuikawi 
##                         190                         378 
##                  TUIKHURHLU                  TUIKHURLUI 
##                         129                         269 
##                     TUIPANG               TUIPANG BAZAR 
##                        1882                         503 
##                      TUIPUI                    Tuipui D 
##                         320                         606 
##                  TUIPUIBARI            Tuirial Airfield 
##                        1767                         427 
##                      TUIRUM                Tuisenchhuah 
##                         480                         499 
##                 TUISENTLANG                      TUISIH 
##                         331                         711 
##                   TUISUMPUI                 TUITHUMHNAR 
##                         385                         321 
##                  TUMPANGLUI               UDALTHANA - I 
##                         489                         588 
##              UDALTHANA - II                    UGALSURY 
##                         645                         433 
##             UGUDASURY NORTH             UGUDASURY SOUTH 
##                         185                         856 
##                    Ukdasuri                     ULUSURY 
##                         204                         275 
##                  Undermanik             UPPER SAKAWRDAI 
##                         240                          82 
##                       Vahai                VAIKHAWTLANG 
##                         497                         590 
##                   VAIRENGTE                      Vaisam 
##                        5936                         203 
##                      VAITIN                    VANBAWNG 
##                         778                         891 
##                 VANCHENGPUI                  Vanchengte 
##                         485                          84 
##                   VANGCHHIA                   VANGTLANG 
##                         494                         382 
##                      Vanhne                      VANKAL 
##                         510                         234 
##                      VANZAU                       VAPAR 
##                         502                         541 
##                    VAPHAI I                   VAPHAI II 
##                         655                         648 
##                      VARTEK                   VARTEKKAI 
##                         159                         198 
##                    VASEIKAI              VASEITLANG - I 
##                         445                         692 
##                  VATHUAMPUI                     VAWMBUK 
##                         814                        1018 
##                  VAWNGAWNZO                      VERVEK 
##                         380                         180 
##                   W.LUNGDAR                  W.PHAILENG 
##                         517                        1487 
##                   W.SERZAWL              West Bungtlang 
##                         281                         167 
##                WEST PHULPUI                     ZAMUANG 
##                         425                        1108 
##                     ZANLAWN                    ZAWLNUAM 
##                         708                        2841 
##                     Zawlpui                     ZAWLPUI 
##                         753                         338 
##                     ZAWLSEI                     ZAWNGIN 
##                         363                         429 
##                   ZAWNGLING              ZAWNGLING - II 
##                         492                         661 
##                  ZAWNGTETUI                      Zehtet 
##                         123                         257 
##                  ZERO POINT                 ZOCHACHHUAH 
##                         467                         171 
##                       ZODIN                      Zohmun 
##                         641                         187 
##                      ZOHMUN                  ZOKHAWTHAR 
##                         939                        1232 
##                ZOKHAWTHIANG                 ZOMUANTLANG 
##                         144                         494 
##                       ZOPUI                      Zote S 
##                          45                         541 
##                  Zotuitlang 
##                         382
```
