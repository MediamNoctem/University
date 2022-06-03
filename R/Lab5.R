library(rvest)
library(stringr)

# Exercise 1
all_years <- list()
names_years <- c(2014:2021)
column_names <- c("Страна", "Качество жизни", "Покупательная способность", "Безопасность",
                   "Здравоохранение", "Прожиточный минимум", "Недвижимость к доходу",
                   "Пробки", "Загрязнения", "Климат")

for (i in c(2014:2021)){
  url <- read_html(paste0("https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title=", toString(i)))
  arr <- html_nodes(url, "td")
  arr <- html_text(arr) %>% as.array()
  arr <- arr[-c(1,2,3)]
  arr <- matrix(arr, ncol = 11, nrow = 83, byrow = TRUE)
  arr <- arr[,-c(11)]
  one_year <- data.frame(arr)
  names(one_year) <- column_names
  all_years[[1+length(all_years)]] = one_year
}
names(all_years) <- names_years;all_years

# Exercise 3
countries <- c("Brazil", "India", "Lebanon", "Turkey", "Denmark")

arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 2]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса качества жизни',
     xlab='Год',
     ylab='Индекс качества жизни', ylim = c(20,250))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)



arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 3]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса покупательной способности',
     xlab='Год',
     ylab='Индекс покупательной способности', ylim = c(20,145))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)



arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 4]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса безопасности',
     xlab='Год',
     ylab='Индекс безопасности', ylim = c(25,90))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 5]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса здравоохранения',
     xlab='Год',
     ylab='Индекс здравоохранения', ylim = c(50,90))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 6]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения прожиточного минимума',
     xlab='Год',
     ylab='Индекс прожиточного минимума', ylim = c(20,125))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 7]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса стоимости недвижимости к доходу',
     xlab='Год',
     ylab='Индекс стоимости недвижимости к доходу', ylim = c(5,20))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 8]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса времени движения на дороге',
     xlab='Год',
     ylab='Индекс времени движения на дороге', ylim = c(25,55))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2014:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 9]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения индекса загрязнения',
     xlab='Год',
     ylab='Индекс загрязнения', ylim = c(20,105))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)



arr_of_index <- list()
years_for_arr <- list()

for(i in c(1:length(countries))){
  temp_index <- c()
  years <- c()
  for (j in c(2016:2021)){
    t <- all_years[[toString(j)]][all_years[[toString(j)]][,1] == countries[i], 10]
    temp_index <- c(temp_index, t)
    if (!identical(t, character(0)))
      years <- c(years,j)
  }
  arr_of_index[[length(arr_of_index)+1]] = temp_index
  years_for_arr[[i]] = years
}
names(arr_of_index) <- countries;arr_of_index;years_for_arr

plot(years_for_arr[[1]],arr_of_index[[1]], type='o', lty=1, pch=20, col='#66CD00', cex = 3,
     main='Тенденции изменения климатического индекса',
     xlab='Год',
     ylab='Климатический индекс', ylim = c(5,120))
lines(years_for_arr[[2]], arr_of_index[[2]], type='o', lty=1, pch=20, col='#CDAD00',cex = 3)
lines(years_for_arr[[3]], arr_of_index[[3]], type='o', lty=1, pch=20, col='#9A32CD',cex = 3)
lines(years_for_arr[[4]], arr_of_index[[4]], type='o', lty=1, pch=20, col='#1E90FF',cex = 3)
lines(years_for_arr[[5]], arr_of_index[[5]], type='o', lty=1, pch=20, col='#FF3030',cex = 3)

legend('topright', countries,
       pch=rep(c(20), 5), lty=c(1,1,1,1,1,1,1),
       col=c('#66CD00', '#CDAD00', '#9A32CD', '#1E90FF', '#FF3030'),
       y.intersp = 0.8, text.width = 1)


# Exercise 4
url <- read_html("https://tonkosti.ru/Музеи_Санкт-Петербурга")
url2 <- read_html("https://tonkosti.ru/Музеи_Санкт-Петербурга?page=2#ttl")
names <- c(html_nodes(url, "h3 a") %>% html_text() %>% as.array(),html_nodes(url2, "h3 a") %>% html_text() %>% as.array());names
address <- c(html_nodes(url, ".places-list__address--rc") %>% html_text() %>% as.array(),html_nodes(url2, ".places-list__address--rc") %>% html_text() %>% as.array());address
ref <- c(html_nodes(url, ".places-list__item-img--rc") %>% html_attr("href"),html_nodes(url2, ".places-list__item-img--rc") %>% html_attr("href"));ref
d <- data.frame(Название = names,Адрес = address,Ссылка = ref);d

