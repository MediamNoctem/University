# GooglePlay
#install.packages("scatterplot3d")
#install.packages("klaR")
library("viridis")
library(lattice)
library("scatterplot3d")

# 1
d=read.csv("C:/Users/romAn/OneDrive/Documents/GitHub/R/Lab6/13_GooglePlay/googleplaystore.csv",sep = ",");d


ind.nan <- unique(which(d == "NaN", arr.ind = TRUE)[,1]);ind.nan
d <- d[-ind.nan,]
d <- d[!is.na(d),]
d$Reviews <- as.numeric(d$Reviews)

# d <- d[1:500,]

hist(d$Reviews)
max1 <- max(d$Reviews, na.rm = TRUE);max1
min1 <- min(d$Reviews, na.rm = TRUE);min1

d$Reviews <- (d$Reviews - min1)/(max1 - min1);d

dist.d <- dist(d) # Матрица попарных расстояний 
clust.d <- hclust(dist.d, "ward.D")

plot(clust.d,  main="Дендрограмма кластеров",xlab="")
rect.hclust(clust.d, k=3, border="red")
groups <- cutree(clust.d, k = 3)

groups_f <- factor(groups)
d1 <- cbind(d,groups_f)

rownames(d[groups==1,])
rownames(d[groups==2,])
rownames(d[groups==3,])
# rownames(d[groups==4,])

g1<-mean(d[groups==1,4]);g1
g2<-mean(d[groups==2,4]);g2
g3<-mean(d[groups==3,4]);g3
# g4<-colMeans(d[groups==4,]);g4

df <- data.frame(g1,g2,g3)
rownames(df) <- col_names
barplot(data.matrix(df), main="Занятость", col=viridis(9), ylim = c(0,80), beside = TRUE)
legend("topright", col_names, col=viridis(9), lwd=5, bty = "n", text.width = 6)

##2 Каменная осыпь
plot(25:1, clust.d$height, type='b', main = "Диаграмма каменная осыпь") 



##3 Двумерные диаграммы рассеяния
xyplot(d[,7] ~ d[,3], d, main='Зависимость финансов от производства',
       xlab='финансы', ylab='производство',  auto.key = TRUE, group = groups, type = c("p", "smooth"))


##4
boxplot(df, col = viridis(4))

##5
scatterplot(d1[,7:9], pch = 16, color=viridis(26))



######6/2
library(klaR)
library(party)
library(randomForest)


naive_jobs <- NaiveBayes(d1$groups_f ~ ., d1)
naive_jobs$tables

# Ядерные функции плотности условной вероятности
layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE)) 
plot(naive_jobs)

d2 <- data.frame(d[,-10])
predict <- predict(naive_jobs, d2)$class
table(Факт = d1$groups_f, Прогноз = predict)

acc <- mean(predict == d1$groups_f)
acc

paste("Точность = ", round(100*acc, 2), "%", sep = "")


# Классификация с помощью дерева решений
set.seed(2235)

ind <- sample(2, nrow(d1), replace=TRUE, prob=c(0.7, 0.3))
trainData <- d1[ind==1,]
testData <- d1[ind==2,]
nrow(trainData) 
nrow(testData)
nrow(d1)

#install.packages("Boruta")

#library(Boruta)
#v<-Boruta(d1,d1$groups_f, pValue=0.01,mcAdj = TRUE, maxRuns = 100,
#          doTrace = 0,holdHistory = TRUE,getImp = getImpRfZ) 


myFormula <- groups_f ~.-groups_f
job_ctree <- ctree(myFormula, trainData)

# Обучение модели
predict(job_ctree)
trainData$groups_f
table(predict(job_ctree), trainData$groups_f)
plot(job_ctree)
dev.off()

# Применяем к произвольной выборке
test_predict <- predict(job_ctree, newdata=testData)
table(test_predict, testData$groups_f)
acc_tree <- mean(test_predict == testData$groups_f);acc_tree
plot(test_predict)


# Random Forest
set.seed(1235)

ind <- sample(2, nrow(d1), replace=TRUE, prob=c(0.7, 0.3))
trainData <- d1[ind==1,]
testData <- d1[ind==2,]
nrow(trainData) 
nrow(testData)
nrow(d1)

myFormula <- groups_f ~.-groups_f
job_ctree <- ctree(myFormula, trainData)


job_forest <- randomForest(groups_f ~.-groups_f,data = trainData, ntree=25, proximity=TRUE)
table(predict(job_forest), trainData$groups_f)
#plot(job_forest)

test_forest <- randomForest(groups_f ~.-groups_f,data = testData, ntree=25, proximity=TRUE)
table(predict(test_forest), testData$groups_f)

