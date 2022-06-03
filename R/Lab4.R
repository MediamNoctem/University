# Exercise 2
library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_m.xls')
olymp_winter_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_f.xls')
olymp_winter_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_f
odbcClose(channel)

library(viridis)
layout(matrix(c(1,2,3,4),2,2, byrow = TRUE))

barplot(olymp_winter_m,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди мужчин, Финляндия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("top", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))

barplot(olymp_winter_f,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди женщин, Финляндия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("right", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))


pie(olymp_winter_m[1,], 
    names(olymp_winter_m[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди мужчин, Финляндия")

pie(olymp_winter_f[1,], 
    names(olymp_winter_f[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди женщин, Финляндия")

layout(matrix(c(1,2),2,2,byrow = TRUE))
years <- names(olymp_winter_m[1,]);years
num_prizes <- apply(olymp_winter_m[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди мужчин, Финляндия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes)     

years <- names(olymp_winter_f[1,]);years
num_prizes <- apply(olymp_winter_f[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди женщин, Финляндия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes) 

# Exercise 3
library(RODBC)
layout(matrix(c(1,2),2,2,byrow = TRUE))

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Canada.xls')
olymp_winter_Canada <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Canada
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_China.xls')
olymp_winter_China <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_China
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Germany.xls')
olymp_winter_Germany <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Germany
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Netherland.xls')
olymp_winter_Netherland <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Netherland
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Norway.xls')
olymp_winter_Norway <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Norway
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Russia.xls')
olymp_winter_Russia <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Russia
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_USA.xls')
olymp_winter_USA <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_USA
odbcClose(channel)

years <- names(olymp_winter_Canada[1,]);years
plot(years,
     olymp_winter_Canada[1,],
     ylim = c(0,20),
     main = "График по количеству золотых медалей\nза последние 4 зимние олимпиады",
     col = 1,
     pch = 15)
lines(years,
      olymp_winter_Canada[1,],
      col = 1)

points(years,
       olymp_winter_China[1,],
       col = 2,
       pch = 15)
lines(years,
      olymp_winter_China[1,],
      col = 2)

points(years,
       olymp_winter_Germany[1,],
       col = 3,
       pch = 15)
lines(years,
      olymp_winter_Germany[1,],
      col = 3)

points(years,
       olymp_winter_Netherland[1,],
       col = 4,
       pch = 15)
lines(years,
      olymp_winter_Netherland[1,],
      col = 4)

points(years,
       olymp_winter_Norway[1,],
       col = 5,
       pch = 15)
lines(years,
      olymp_winter_Norway[1,],
      col = 5)

points(years,
       olymp_winter_Russia[1,],
       col = 6,
       pch = 15)
lines(years,
      olymp_winter_Russia[1,],
      col = 6)

points(years,
       olymp_winter_USA[1,],
       col = 7,
       pch = 15)
lines(years,
      olymp_winter_USA[1,],
      col = 7)

legend("top", 
       title = "Страны", 
       legend = c("Канада","Китай","Германия","Нидерланды","Норвегия","Россия", "США"), 
       fill = 1:7)


plot(years,
     apply(olymp_winter_Canada[1:3,], 2, sum),
     ylim = c(5,55),
     main = "График по количеству призовых мест\nза последние 4 зимние олимпиады",
     xlab = "Год Олимпиады",
     ylab = "Количество призовых мест",
     col = 1,
     pch = 15)
lines(years,
      apply(olymp_winter_Canada[1:3,], 2, sum),
      col = 1)

points(years,
       apply(olymp_winter_China[1:3,], 2, sum),
       col = 2,
       pch = 15)
lines(years,
      apply(olymp_winter_China[1:3,], 2, sum),
      col = 2)

points(years,
       apply(olymp_winter_Germany[1:3,], 2, sum),
       col = 3,
       pch = 15)
lines(years,
      apply(olymp_winter_Germany[1:3,], 2, sum),
      col = 3)

points(years,
       apply(olymp_winter_Netherland[1:3,], 2, sum),
       col = 4,
       pch = 15)
lines(years,
      apply(olymp_winter_Netherland[1:3,], 2, sum),
      col = 4)

points(years,
       apply(olymp_winter_Norway[1:3,], 2, sum),
       col = 5,
       pch = 15)
lines(years,
      apply(olymp_winter_Norway[1:3,], 2, sum),
      col = 5)

points(years,
       apply(olymp_winter_Russia[1:3,], 2, sum),
       col = 6,
       pch = 15)
lines(years,
      apply(olymp_winter_Russia[1:3,], 2, sum),
      col = 6)

points(years,
       apply(olymp_winter_USA[1:3,], 2, sum),
       col = 7,
       pch = 15)
lines(years,
      apply(olymp_winter_USA[1:3,], 2, sum),
      col = 7)

legend("top", 
       title = "Страны", 
       legend = c("Канада","Китай","Германия","Нидерланды","Норвегия","Россия", "США"), 
       fill = 1:7)

# Exercise 4
library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Canada_m.xls')
olymp_winter_Canada_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Canada_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Canada_f.xls')
olymp_winter_Canada_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Canada_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_China_m.xls')
olymp_winter_China_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_China_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_China_f.xls')
olymp_winter_China_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_China_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Germany_m.xls')
olymp_winter_Germany_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Germany_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Germany_f.xls')
olymp_winter_Germany_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Germany_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_France_m.xls')
olymp_winter_France_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_France_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_France_f.xls')
olymp_winter_France_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_France_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Norway_m.xls')
olymp_winter_Norway_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Norway_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Norway_f.xls')
olymp_winter_Norway_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Norway_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Russia_m.xls')
olymp_winter_Russia_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Russia_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_Russia_f.xls')
olymp_winter_Russia_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_Russia_f
odbcClose(channel)


channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_USA_m.xls')
olymp_winter_USA_m <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_USA_m
odbcClose(channel)

channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/olymp_winter_USA_f.xls')
olymp_winter_USA_f <- as.matrix(sqlFetch(channel,'Лист1'));olymp_winter_USA_f
odbcClose(channel)

library(viridis)
layout(matrix(c(1,2,3,4),2,2, byrow = TRUE))

barplot(olymp_winter_Germany_m,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди мужчин, Германия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("top", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))

barplot(olymp_winter_Germany_f,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди женщин, Германия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("top", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))


pie(olymp_winter_Germany_m[1,], 
    names(olymp_winter_Germany_m[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди мужчин, Германия")

pie(olymp_winter_China_f[1,], 
    names(olymp_winter_Germany_f[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди женщин, Германия")

layout(matrix(c(1,2),2,2,byrow = TRUE))
years <- names(olymp_winter_Germany_m[1,]);years
num_prizes <- apply(olymp_winter_Germany_m[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди мужчин, Германия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes)     

years <- names(olymp_winter_Germany_f[1,]);years
num_prizes <- apply(olymp_winter_Germany_f[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди женщин, Германия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes) 


layout(matrix(c(1,2,3,4),2,2, byrow = TRUE))
barplot(olymp_winter_France_m,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди мужчин, Франция",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("top", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))

barplot(olymp_winter_France_f,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди женщин, Франция",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("right", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))


pie(olymp_winter_France_m[1,], 
    names(olymp_winter_France_m[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди мужчин, Франция")

pie(olymp_winter_France_f[1,], 
    names(olymp_winter_France_f[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди женщин, Франция")

layout(matrix(c(1,2),2,2,byrow = TRUE))
years <- names(olymp_winter_France_m[1,]);years
num_prizes <- apply(olymp_winter_France_m[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди мужчин, Франция",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes)     

years <- names(olymp_winter_France_f[1,]);years
num_prizes <- apply(olymp_winter_France_f[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди женщин, Франция",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes) 


layout(matrix(c(1,2,3,4),2,2, byrow = TRUE))
barplot(olymp_winter_Norway_m,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди мужчин, Норвегия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("top", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))

barplot(olymp_winter_Norway_f,
        col = magma(8),
        main = "Столбчатая диаграмма по количеству\nмест 1-8 по биатлону среди женщин, Норвегия",
        xlab = "Год Олимпиады",
        ylab = "Общее количество медалей за олимпиаду")
legend("right", title = "Места", c("1","2","3","4","5","6","7","8"), fill = magma(8))


pie(olymp_winter_Norway_m[1,], 
    names(olymp_winter_Norway_m[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди мужчин, Норвегия")

pie(olymp_winter_Norway_f[1,], 
    names(olymp_winter_Norway_f[1,]), 
    col = magma(8),
    main = "Круговая диаграмма по количеству первых мест\nпо биатлону среди женщин, Норвегия")

layout(matrix(c(1,2),2,2,byrow = TRUE))
years <- names(olymp_winter_Norway_m[1,]);years
num_prizes <- apply(olymp_winter_Norway_m[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди мужчин, Норвегия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes)     

years <- names(olymp_winter_Norway_f[1,]);years
num_prizes <- apply(olymp_winter_Norway_f[1:3,], 2, sum);num_prizes

plot(years, 
     num_prizes, 
     main = "Функциональный график, отображающий тенденцию изменения\nколичества призовых мест среди женщин, Норвегия",
     xlab = "Год Олимпиады", 
     ylab = "Количество призовых мест",
     las = 1,
     pch = 19)

lines(years, num_prizes) 





















