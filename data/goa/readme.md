## Goa

Basic descriptive statistics about the data. And sanity checks.


```r
goa <- readr::read_csv("goa.csv")
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
##   net_electors_total = col_integer()
## )
```

```
## See spec(...) for full column specifications.
```

Number of rows:


```r
nrow(goa)
```

```
## [1] 1077909
```

Unique Values in Sex:


```r
# Unique values in sex
table(goa$sex)
```

```
## 
## Female   Male 
## 547456 530453
```

Summary of Age:


```r
# Age
summary(goa$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   18.00   33.00   43.00   45.07   56.00  116.00
```

No. of characters in ID:

```r
# Length of ID
table(nchar(goa$id))
```

```
## 
##      9     10     11     12     13     15     16     17 
##     10 923728      1      1      1      1 153789      3
```

Number of characters in pin code:


```r
table(nchar(goa$pin_code))
```

```
## 
##       6 
## 1077909
```


```r
# Net electors
sum(with(goa, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 1077909
```

```r
nrow(goa)
```

```
## [1] 1077909
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
goa[which(nchar(goa$elector_name) == 4), "id"]
```

```
## # A tibble: 1 x 1
##   id        
##   <chr>     
## 1 JMQ2235729
```

```r
goa[which(nchar(goa$elector_name) == 50), "filename"]
```

```
## # A tibble: 1 x 1
##   filename        
##   <chr>           
## 1 AC032_Part02.pdf
```

Basic admin. units:

```r
table(goa$police_station)
```

```
## 
##       Agassaim         Anjuna       Bicholim      Calangute       Canacona 
##          20861           7352          74365          41788          36939 
##         Collem          Colva       Cuncolim      Curchorem Maina Curtorim 
##           9797          35365          47825          30782          43026 
##         Mapusa         Margao        Old-Goa         Panaji         Pernem 
##         107952          76049          59710          47917          62744 
##          Ponda   Ponda(North)       Porvorim         Quepem        Sanguem 
##         116485          10635          28978          36239          16923 
##         Valpoi          Vasco          Verna 
##          49007          79335          37835
```

```r
table(goa$mandal)
```

```
## 
##      Bardez    Bicholim    Canacona Dharbandora    Mormugao      Pernem 
##      186070       74365       36939       19482      109804       62744 
##       Ponda      Quepem     Salcete     Sanguem     Sattari     Tiswadi 
##      122303       61782      196939       29986       49007      128488
```

```r
table(goa$district)
```

```
## 
## North Goa South Goa 
##    511309    566600
```

```r
table(goa$main_town)
```

```
## 
##            Adcolna              Adnem              Advoi 
##               1158               1100                537 
##          Adwalpale            Agacaim           Agarvado 
##               1219               4236               1707 
##             Agonda             Aldona             Alorna 
##               3255               6825               1447 
##           Ambaulim            Ambedem            Ambelim 
##               2014                660               2230 
##              Amone             Anjuna              Aquem 
##               2414               7352               4968 
##            Arambol            Arossim             Arpora 
##               4592                882               2310 
##            Assagao            Assolda            Assolna 
##               3562               2347               3041 
##           Assonora             Avedem            Azossim 
##               4089               1732               3424 
##          Baiguinim               Bali           Bambolim 
##               3894               2236               1249 
##            Bandora             Barcem            Bastora 
##               8348               3308               3138 
##               Bati              Batim           Benaulim 
##               1692               1332               9699 
##         Betelbatim             Betora             Betqui 
##               2979               3461               1435 
##              Betul           Bicholim           Birondem 
##               1078              12288               1328 
##               Boma              Borim            Buimpal 
##               1939               6767                944 
##          Calangute            Calapor             Calata 
##              10432              10419               1423 
##              Calem           Camurlim           Canacona 
##               3264               2590              13021 
##              Canca           Candepar            Candola 
##               2401               3028               3753 
##           Candolim          Cansaulim              Capao 
##               7273               2690                142 
##         Carambolim           Caranzol            Carapur 
##               4186                672               3732 
##            Carmona        Casarvarnem             Casnem 
##               3015                999                659 
##         Cavelossim            Cavorem            Cavorim 
##               1664                970               2124 
##            Chandel            Chandor           Chicalim 
##                866               3409               3272 
##           Chicolna            Chimbel         Chinchinim 
##               1677              10493               5947 
##             Chorao         Choraundem              Codal 
##               4946                583                935 
##             Codiem            Codiqui               Cola 
##                661                761               4393 
##             Collem            Colomba              Colva 
##               4453               1394               2749 
##            Colvale          Compordem             Cordem 
##               4672                926               1125 
##             Corgao           Corjuvem             Corlim 
##               5367               1134               4711 
##           Cortalim            Cotarli            Cotigao 
##               5407               1110               2050 
##            Cotombi             Cudcem             Cudnem 
##                895                823               2555 
##             Cuelim             Cujira         Cumbharjua 
##               1342                759               3863 
##           Cuncolim            Cundaim              Curca 
##              12285               3154               3757 
##          Curchirem   Curchorem Cacora             Curpem 
##               1220              17067                644 
##              Curti            Dabolim            Damocem 
##              11810               3659                457 
##              Davem           Davorlim            Deussua 
##                517              11687                967 
##        Dharbandora          Dhargalim          Dicarpali 
##               4817               4658               2126 
##           Dongurli           Dramapur            Durbhat 
##               1092               1918               2891 
##            Fatorpa             Gangem         Gaodongrem 
##               1474                378               3892 
##          Gaundalim          Goa Velha            Golauli 
##                239               3452                487 
##             Goltim            Govanem          Guirdolim 
##               1338                451               1580 
##             Guirim             Guleli           Hankhane 
##               4214                660                616 
##           Hassapur           Ibrampur           Issorcim 
##                809               1145                672 
##      Ivrem-Buzruco                Jua   Karambolim Brama 
##                734               3539               1120 
##     Kirlapal Dabal        Latambarcem       Loliem-Polem 
##               4868               5195               4593 
##           Loutulim           Macasana               Maem 
##               4693               1839               7332 
##            Majorda              Malar            Mandrem 
##               2503               1396               7128 
##             Mangal             Mapusa            Marcaim 
##                810              32852               5076 
##        Margao Town   Maulinguem North              Mauxi 
##              57788               1124               1473 
##           Melaulim           Mencurem              Moira 
##               1231               1467               3646 
##          Molcarnem             Mollem               Mopa 
##               1832               1986                898 
##             Morjim             Morlim           Mormugao 
##               5864               2674              34325 
##   Morombi-O-Grande  Morombi-O-Pequeno           Morpirla 
##               1426               2107               2196 
##             Muguli              Mulem             Mulgao 
##                403               1992               2944 
##              Murda          Nachinola             Nadora 
##               3056               2217               1170 
##              Nagoa           Naquerim              Narao 
##               3501                725                450 
##              Naroa            Navelim              Nerul 
##               1424              11052               3638 
##            Netorli     Neura-O-Grande    Neura-O-Pequeno 
##                895                507               1060 
##           Nirancal             Nundem              Nuvem 
##               2336                841               7228 
##                Ona               Onda              Orgao 
##               1428               3799               3311 
##              Orlim               Oxel             Ozarim 
##               1578               2445               1555 
##               Padi               Pale             Paliem 
##                679               4427               3561 
##             Panaji         Panchavadi            Panelim 
##              33664               3713                787 
##             Parcem             Paroda              Parra 
##               3747                811               3485 
##    Penha-De-Franca             Pernem            Pilerne 
##              10487               3838               4577 
##            Piligao              Pirla              Pirna 
##               2239                592               2192 
##          Pissurlem            Podocem         Poinguinim 
##               1793                751               5735 
##           Pomburpa              Ponda             Poriem 
##               3417              15761               3148 
##         Poroscodem            Porteem              Priol 
##               1397               1963               6392 
##             Punola              Quela          Quelossim 
##                523               5057               2124 
##             Quepem             Querim             Quitol 
##              11609               8251                524 
##             Ravona         Reis-Magos           Renovadi 
##               1006               5895                717 
##             Revora             Rivona             Saleli 
##               2226               2822                765 
##              Salem            Saligao  Salvador-Do-Mundo 
##               2873               4733               4867 
##           Sancoale           Sancorda           Sangolda 
##               3975               3358               2893 
##            Sanguem          Sanquelim          Sanvordem 
##               5210               9710               6671 
## Sao Jacinto Island  Sao Jose De Areal           Sarvorna 
##                885               6522               2253 
##            Sarzora        Savoi-Vernm           Seraulim 
##               1989                758               2944 
##         Sernabatim            Shiroda             Siolim 
##               1162              11950               9862 
##            Sircaim             Sirgao            Siridao 
##               2300               1423               1844 
##             Sirlim           Sirsodem            Socorro 
##                757                568               9047 
##    Sonus-Vonvoliem              Surla           Talaulim 
##                624               4786               5344 
##           Taleigao            Talvoda           Tamboxem 
##              14253               1387                537 
##              Tiloi            Tiracol              Tivim 
##                458                192               7357 
##             Tivrem             Torxem               Tuem 
##               1330               2143               2360 
##           Ucassaim              Uguem            Undorna 
##               1304               3268                434 
##              Usgao              Ustem             Utorda 
##              10257                456               1818 
##             Valpoi            Vanelim             Vantem 
##               6327               1512               1159 
##              Varca           Varkhand      Vasco-Da-Gama 
##               4137               1961              35517 
##            Velguem              Velim            Velinga 
##               3223               5681               1384 
##             Velsao              Verla             Verlem 
##               2422               2560                521 
##              Verna         Vichundrem            Viliena 
##               4994                611                777 
##            Virnora             Volvai             Xeldem 
##               2355               1466               5782 
##            Xelvona             Zormen         Zuarinagar 
##                795                879              10955
```
