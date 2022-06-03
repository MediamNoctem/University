# Exercise 1
g <- c(1, 0, 2, 3, 6, 8, 12, 15, 0, NA, NA, 9, 4, 16, 2, 0)

# 1.2
g[1]

# 1.5
g[g == 2 & !is.na(g)]


# Exercise 2
df <- data.frame(var1=c(11,21,31), var2=c(12,22,32), var3=c(13,23,33), var4=c(14,24,34), row.names=c("case1", "case2", "case3"))

# 2.1
df[1,1:3]
df[2,df[2,] > 22]

# 2.2
colnames(df)[1]
colnames(df)[3]

# 2.3
df <- cbind(df, Y=c(-1, 0, 1))

# 2.4
df <- df[c(TRUE,FALSE,TRUE),]

# 2.5
df[,2]**3


# Exercise 3
emp <- data.frame(Nrow=c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), Name=c("Abraham","Ada","Adam","Adeline","Adrian","Agatha","Alan","Alice","Albert","Alexander","Andrew","Austin","Benjamin","Bernard","Brian","Carter","Charles","Daniel","David","Emily"))

BirthYear <- as.integer(runif(20,1960,1985))

EmployYear <- as.integer(runif(20,BirthYear + 18,2006))

salary <- double(20)

salary[BirthYear < 1975] <- (log(2007 - EmployYear[BirthYear < 1975]) + 1) * 8000

salary[BirthYear >= 1975] <- (log(2007 - EmployYear[BirthYear >= 1975], 2) + 1) * 8000


emp <- cbind(emp,BirthYear)
emp <- cbind(emp, EmployYear)
emp <- cbind(emp, salary)

remove(BirthYear,EmployYear,salary)

sum(emp$salary > 15000)

i <- integer(20)

IncomeTax <- double(20)

while (sum((2007 - emp$EmployYear - i) > 0) > 0) {
  i[(2007 - emp$EmployYear - i) > 0] <- i[(2007 - emp$EmployYear - i) > 0] + 1
  
  IncomeTax[emp$BirthYear < 1975 & (2007 - emp$EmployYear - i) > 0] <- ((log(i[emp$BirthYear < 1975 & (2007 - emp$EmployYear - i) > 0]) + 1) * 8000) * 0.13
  IncomeTax[emp$BirthYear >= 1975 & (2007 - emp$EmployYear - i) > 0] <- ((log(i[emp$BirthYear >= 1975 & (2007 - emp$EmployYear - i) > 0], 2) + 1) * 8000) * 0.13
}

emp <- cbind(emp,IncomeTax)


# Exercise 4
df <- data.frame(var1=c(1,2,3), var2=c(4,5,6), var3=c(7,8,0), var4=c(9,10,11), row.names=c("case1", "case2", "case3"))

# 4.1
df[1,]

# 4.2
df[3,df[3,] < 8]

# 4.3
colnames(df)[2]
colnames(df)[4]

# 4.4
df <- cbind(df, Y=c(-10, 0, 11))

# 4.5
df <- df[c(TRUE,FALSE,TRUE),]

# 4.6
df[,2]**3


# Exercise 5
#v = scan()
v =  c(5,4,3,-11,50,0)
v[sample(0:1,length(v),1) == 1] <- NA
which(is.na(v))
sum(is.na(v))


# Exercise 6


# Exercise 7
country <- c(rep("France",5),rep("Italy",5), rep("Spain",5))
year <- rep(c(2000,2001,2002,2003,2004),3)


# Exercise 8
income <- c(10000, 32000, 28000, 150000, 65000, 1573)
sr <- mean(income)
income_class <- (income >= sr)


# Exercise 9
v <- runif(100,0,500)
sr <- mean(v)
v[v < sr]
m <- matrix(v, nrow=10)

matrix(m[rep(c(FALSE,TRUE),5)], nrow = 5)
matrix(m[rep(c(TRUE,FALSE),5)], nrow = 5)


# Exercise 10
vect <- sample(1:100,10,replace=T)
sum(vect%%2 == 0 | vect%%3 == 0 | vect%%5 == 0)


# Exercise 11
v <- sample(1:100,100,replace=T)
sum(v[(which(v > 0) > which.min(v)) & (which(v > 0) < which.max(v)) | (which(v > 0) > which.max(v)) & which(v > 0) < which.min(v)])


# Exercise 12
v <- sample(-20:50,10,replace=T)
min <- which.min(v)
max <- which.max(v)
t <- v[max] 
v[max] <- v[min]
v[min] <- t

sum(v < 0)
v[v < 0] <- 0


# Exercise 13
v <- seq(2,99,by=1)
sum(v%%2 == 0 | v%%3 == 0 | v%%5 == 0 | v%%7 == 0)


# Exercise 14
v <- sample(-15:14,20,replace=T)
v
sum(abs(v) > v[which.max(v)])
sum(v == 3)
sum(v == 5)
sum(v == 7)


# Exercise 15
cat('Введите названия планет:')
Планета <- readLines(n = 6)
cat('Введите расстояния до Солнца от планет:')
Расс_до_Солнца <- scan()
cat('Введите относительный объем планет:')
Относ_объем <- scan()
cat('Введите относительную массу планет:')
Относ_масса <- scan()

df <- data.frame(Планета, Расс_до_Солнца, Относ_объем, Относ_масса)
df
df[which.min(df[,2]),1]
df[which.max(df[,2]),1]

# df[sort(df$Относ_объем,decreasing=F)]


# Exercise 27