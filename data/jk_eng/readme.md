## Jammu and Kashmir

Basic descriptive statistics about the data. And sanity checks.


```r
jk <- readr::read_csv("jk.csv")
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

Number of rows:


```r
nrow(jk)
```

```
## [1] 164713
```

Unique Values in Sex:


```r
# Unique values in sex
table(jk$sex)
```

```
## 
## Female   Male 
##  81365  83348
```

Summary of Age:


```r
# Age
summary(jk$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   18.00   31.00   39.00   42.81   53.00  118.00
```

No. of characters in ID:

```r
# Length of ID
table(nchar(jk$id))
```

```
## 
##      9     10     11 
##      1 164711      1
```

Number of characters in pin code:


```r
table(nchar(jk$pin_code))
```

```
## 
##      6 
## 164002
```


```r
# Net electors
sum(with(jk, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 164713
```

```r
nrow(jk)
```

```
## [1] 164713
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(jk$elector_name))
```

```
## 
##     2     3     4     5     6     7     8     9    10    11    12    13 
##     1    97   511  2089  5514  3174  2371  5856  7930 18879 27049 29700 
##    14    15    16    17    18    19    20    21    22    23    24    25 
## 31959 16237  8372  1924   771   731   589   456   220   147    57    30 
##    26    27    28    29    30    31    32    33    38    40 
##    20     7    13     2     2     1     1     1     1     1
```

```r
jk[which(nchar(jk$elector_name) < 4), "filename"]
```

```
## # A tibble: 98 x 1
##    filename         
##    <chr>            
##  1 EACA049PS0049.pdf
##  2 EACA049PS0030.pdf
##  3 EACA049PS0030.pdf
##  4 EACA049PS0030.pdf
##  5 EACA049PS0030.pdf
##  6 EACA049PS0030.pdf
##  7 EACA048PS0061.pdf
##  8 EACA049PS0104.pdf
##  9 EACA049PS0170.pdf
## 10 EACA049PS0080.pdf
## # ... with 88 more rows
```

Basic admin. units:

```r
table(jk$police_station)
```

```
## 
##         DRASS        KARGIL        KHALSI           LEH         NUBRA 
##          9910         60796         13720         46775         13335 
##         NYOMA PADUM ZANSKAR        SANKOO 
##          8871          8965          1630
```

```r
table(jk$mandal)
```

```
## 
##         DISKIT         KARGIL KHALTSI TEHSIL          KHARU     LEH TEHSIL 
##           1222          46151          13788            251          55327 
##         SANKOO         SUMOOR        TANGTSE        ZANSKAR 
##          26185            188          11925           8965
```

```r
table(jk$district)
```

```
## 
## KARGIL    LEH 
##  81301  82701
```

```r
table(jk$main_town)
```

```
## 
##              ABRAN           ACHAMBUR       ACHINALUNGBA 
##                320                319                 65 
##        ACHINATHANG              AGYAM           AKCHAMAL 
##                395                 26               1281 
##             AKSHOW              ALCHI                ANG 
##                233                607                190 
##            ANGKUNG              ANLEY          ANLEY PHO 
##                 61                324                 82 
##      ANLEY PHUNGUG             APATEE              ARANO 
##                248                783                166 
##        ARANO YAQMA             ATTING    BAGH E KHOMAINI 
##                 96                371                215 
##              BALAM            BARCHEY              BAROO 
##                186                392               1445 
##             BARSOO             BARTOO              BASGO 
##               1245                452                878 
##           BATAMBIS            BHIMBAT              BIAMA 
##                274                834                258 
##        BODHKHARBOO            BOGDANG           BUKSHADO 
##                697                708                100 
##              BURMA                CHA             CHAKOR 
##                 60                219                288 
##          CHAMASTIN             CHANGA           CHANGMAR 
##                278                210                 37 
##            CHANSPA            CHARASA            CHEMDEY 
##               1254                341                294 
##            CHIKTAN             CHILAM           CHILLING 
##                838                273                 55 
##         CHOGLAMSER             CHOKDO           CHOKIYAL 
##                596                 51                617 
##          CHOMOLING           CHOSKORE   CHUCHOT GONGMA A 
##                433               2045                781 
##      CHUCHOT SHAMA     CHUCHOT SHAMMA    CHUCHOT YOKMA A 
##                715                654                910 
##    CHUCHOT YOKMA B          CHULICHAN        CHULISKAMBO 
##                871                520                640 
##         CHULUNGKHA         CHUMATHANG             CHUMUR 
##                103                342                 83 
##            CHUSHUL            DABLENG             DAFANA 
##                755                108                157 
##                DAH             DAMSNA           DARCHIKS 
##                157                467                332 
##            DARKETH             DEMJOK              DIGAR 
##                195                 69                290 
##             DISKIT      DOMKHER BARMA     DOMKHER GONGMA 
##               1136                240                412 
##              DRASS     DRELOUNG LATOO             DURBUK 
##                648                188                460 
##        EZANG SUMDA            FANJILA FARKHA YOKMA MATHO 
##                 14                 73                670 
##            FAROONA          FATULALOK           FOTOKSAR 
##                587                 75                160 
##               GAIK             GARARI            GARKONE 
##                 11                202                761 
##               GERA            GIALING           GINDIYAL 
##                 43                181                396 
##      GOMPA GANGLES              GONBO             GOSHAN 
##                767                 30                885 
##   GOUND MANGALPORE                GYA             HAGNIS 
##               1341                349               1105 
##             HANKAR        HANU GONGMA         HANU YOKMA 
##                105                355                392 
##           HANUPATA          HANUTHANG            HARDASS 
##                 62                123                946 
##    HEMISSHUKPACHEN              HEMYA           HIMILING 
##                379                167                124 
##              HINJU           HINSKOTE              HIPTI 
##                 98                223                 33 
##     HOUSING COLONY   HOUSING COLONY A   HOUSING COLONY D 
##                817                804                578 
##         HUNDAR DOK            HUNDARI             HUNDER 
##                101                239                942 
##              ICHAR               ICHU                IGG 
##                258                 99                 41 
##               IGOO           JASGOUND             KAKSAR 
##                644                278                605 
##              KANJI             KANOOR            KARAMBA 
##                230                734                262 
##        KARCHEYKHAR             KARGEE            KARGIAK 
##                644                393                218 
##             KARGIL            KARGYAM             KARITH 
##               3281                 99                319 
##             KARKIT          KARPOKHAR             KARSHA 
##               1448                 86                652 
##               KAYA              KEREY              KESAR 
##                 77                 85                 72 
##            KHACHAY      KHACHEY THANG          KHAHKATET 
##                383                230                 20 
##            KHALSAR            KHALTSI              KHAMI 
##                117                433                 92 
##             KHANDI            KHARBOO    KHARDONG PHIRKA 
##               1047                656                408 
##   KHARDONG RASERNO            KHARNAK              KHARU 
##                 84                144                148 
##            KHATPOO             KHAWAS              KHEMA 
##                 46                463                 97 
##            KHUMDOK           KHYUNGRU              KOBED 
##                 79                 45                132 
##             KOCHIK             KORZOK              KOTSA 
##                184                233                204 
##              KUBET            KUKSHOW            KUKSTAY 
##                124                439                244 
##            KUNGYAM          KURAMBEIG              KUYUL 
##                208               1024                295 
##            LAGJONG              LAIDO            LALOUNG 
##                138                307                428 
##           LAMAYURU       LAMSO SANDOO      LANGMI RIGING 
##                532                375                266 
##         LANKARCHEY              LARDO     LARGYAB GONGMA 
##               1526                 49                 68 
##      LARGYAB YOGMA              LIKIR             LIKTSE 
##                 41                323                130 
##           LINGSHED             LOCHUM             LUNGBA 
##                462                272                288 
##               MAAN               MAHE             MANGUE 
##                110                 41                342 
##             MARKHA         MARTSELANG            MATAYAN 
##                128                397                321 
##              MATHO              MERAK               MERU 
##                457                191                163 
##             MINJEE               MUDH             MUKLAB 
##               1583                336                 33 
##            MULBEKH          MURADBAGH              MURGI 
##               1059                459                 75 
##            MUSHKOO     NAKLEY LANGKOR            NAMSURU 
##                332                439                554 
##               NANG       NANGMA KUSAR                NEE 
##                310                708                 75 
##                NEY            NEYRAKS             NIDDER 
##                479                104                134 
##              NIMGO              NIMOO            NONGNIT 
##                177                641                 71 
##         NUNAMACHEY              NURLA              NYOMA 
##                159                340                449 
##             ORBISH        PACHA THANG              PADUM 
##                126                157               1013 
##            PANAMIK           PANDRASS           PANIKHAR 
##                254                506                227 
##          PARKACHIK           PARTAPUR          PENCHIMIK 
##                688                464                273 
##               PHEY            PHIRSAY           PHOBRANG 
##                581                 96                424 
##         PHOKPOCHEY               PHOO           PHUKTSEY 
##                 78                441                224 
##             PHYANG     PHYANG CHOUSGO      PHYANG FULUNG 
##                695                691                512 
##             PIPCHA                PIU              POYEN 
##                120                488               1156 
##            PRANTEE            PUSHKUM             RAKURU 
##                364               2028                 39 
##      RALLY EACHING         RAMBIRPURE      RAMILA SKYGAM 
##                 40                611                388 
##            RANGDUM         RANTHAKSHA         RARU MONEY 
##                195                208                245 
##             RIZONG             RONGDO              RONGO 
##                110                 40                272 
##       RONJOK NIMOO             RUKRUK             RUMBAK 
##                390                221                 64 
##           RUMCHHEY           RUMCHUNG              SABOO 
##                236                 32               1076 
##          SAKANDYNG              SAKTI      SALAPI GYAPAK 
##                184                251                485 
##          SALISKOTE      SAMAD ROKCHEN             SAMRAH 
##               1436                278               1010 
##            SANGRAH               SANI             SANJAK 
##                859                400                314 
##             SANKER               SAPI   SARCHEY (KANOOR) 
##               1614                599                206 
##          SASPOCHEY             SASPOL          SATAKCHAY 
##                174                899               1044 
##              SATOO          SHACHUKUL            SHAJING 
##                283                385                902 
##             SHAKAR            SHAKOOR              SHANG 
##               1280                 49                211 
##              SHARA          SHARGANDI           SHARGOLE 
##                250                210                347 
##            SHARNOS             SHELLA             SHENAM 
##                251                 62               1275 
##               SHEY         SHILIKCHEY            SHIMSHA 
##               1450                676                461 
##        SHUN SHADAY             SILMOO       SKALZANGLING 
##                157               1085               2432 
##            SKAMBOO           SKAMPARI            SKAMPUK 
##                442               1773                366 
##              SKARA           SKIDMANG           SKILKHOR 
##               1599                190                581 
##          SKONGSHAT               SKUE           SKUMPATA 
##                301                 60                123 
##             SKUROO             SKYNOS              SOGRA 
##                176               1074                161 
##    SONAM BARMALING             SONODO           SPANGMIK 
##                811                 21                 38 
##             SPITUK             SRIYUL             STAKMO 
##               1235                 35                192 
##             STAKNA             STAKPA               STOK 
##                357                659                796 
##      STONGDAY KUMI              SUMDA       SUMDA CHENMO 
##                609                 73                 71 
##           SUMDA DO              SUMDO             SUMOOR 
##                 28                 22                621 
##              TACHA        TACHAKHASAR              TAGAR 
##                276                187                289 
##            TAISURU             TAKNAK             TAKSHA 
##                399                362                 59 
##            TAKSHAH             TAMBIS            TANGOLE 
##                229               1593                420 
##            TANGTSE            TANGYAR          TAQMACHAK 
##                194                192                352 
##                TAR            TARCHIT              TAROO 
##                 72                272                438 
##     TARUCHEY LIKIR    TASHI GYATSAL A           TEGAZONG 
##                140               1749                364 
##           TEMISGUM              TESTA      THAGAM THUINA 
##                407                273               1630 
##              THANG        THANGDUMBOR             THARUK 
##                371               1857                341 
##            THASGAM          THIKSEY A          THIKSEY B 
##                236                846                832 
##          THROUNGOS      THUKJEY GOMPA             THULUS 
##                265                 27                261 
##        TIA KHALING             TIGGER            TINGDOO 
##                220                485                202 
##             TIRCHI               TIRI            TIRI DO 
##                242                121                 69 
##              TIRTH               TIYA           TONGSTET 
##                192                709                  5 
##           TRESPONE             TRISHA           TRONGIEN 
##               2265                 89                627 
##              TSAGA              TSATI            TSOKSTI 
##                230                139                 23 
##              TUKLA      TUKLA PHULAKS             TUMAIL 
##                122                106                707 
##            TUNGREE         TURTUK YON            TYAKSHI 
##                365               1180                288 
##             UDMARO       UFTIPIPITING              ULLEY 
##                300                619                 37 
##               UMBA               UMLA        UPPER LIKIR 
##                614                102                526 
##         UPPER STOK              UPSHI   URGANLING SPITUK 
##                492                102                339 
##              WAKHA              WANLA              WARIS 
##               1227                275                124 
##    WARLKAS TAMSGAM          YANGTHANG     YOKNOS CHEMDEY 
##                704                116                364 
##             YOLKAN       YOUKMAKHARBO            YOULBOO 
##                 74                372                443 
##          YOULCHUNG         YOURBALTAK             YULJUK 
##                 68               1244                827 
##             ZANGLA     ZANGSTI GOGSUM 
##                670                851
```
