source("setup.r")
seaflow <- read.csv("seaflow_21min.csv")

# q2
table(seaflow$pop)

# q3
# assuming the question actually should be 3rd QUARTILE, not quantile(x, 0.03)
# quantile(seaflow$fsc_small, 0.75) != summary(seaflow$fsc_small)[5] (!)
summary(seaflow$fsc_small)[5]

# q4
trainset <- sample(seq_len(nrow(seaflow)), round(nrow(seaflow) / 2))
testset <- setdiff(seq_len(nrow(seaflow)), trainset)
training <- seaflow[trainset, ] 
mean(training$time)

# q5
qplot(pe, chl_small, data=seaflow, color=pop, shape=pop, size=pop)

# q6
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small) 
model <- rpart(fol, method="class", data=training)
model

# q7
model

# q8 
model

# q9 
testing <- seaflow[testset,] 
predictions <- predict(model, testing, type="class")
correct <- sum(predictions == testing$pop) / nrow(testing)
print(correct) 

# q10 
training$pop <- as.factor(training$pop)
rfmodel <- randomForest(fol, data=training)
rfpredictions <- predict(rfmodel, testing)
rfcorrect <- sum(rfpredictions == testing$pop) / nrow(testing)
print(rfcorrect)

# q11
importance(rfmodel)

# q12
svmmodel <- svm(fol, data=training)
svmpredictions <- predict(svmmodel, testing)
svmcorrect <- sum(svmpredictions == testing$pop) / nrow(testing)
print(svmcorrect)

# q13
confmat <- function(pred) table(pred, true=testing$pop)
confmat(svmpredictions)
confmat(rfpredictions)
confmat(predictions)

# q14 
newseaflow <- seaflow[seaflow$file_id != 208, ] 
newtrain <- sample(seq_len(nrow(newseaflow)), round(nrow(newseaflow) / 2))
newtest <- setdiff(seq_len(nrow(newseaflow)), newtrain)
newtraining <- newseaflow[newtrain, ] 
newtraining$pop <- as.factor(newtraining$pop)a
if (any(newtraining$file_id == 208)) stop("You botched your new training set.")
newsvmmodel <- svm(fol, data=newtraining)
newtesting <- newseaflow[newtest, ] 
if (any(newtesting$file_id == 208)) stop("You botched your new test set.")
newsvmpredictions <- predict(newsvmmodel, newtesting)
newsvmcorrect <- sum(newsvmpredictions == newtesting$pop) / nrow(newtesting)
print(newsvmcorrect)

# q15 
for (v in names(seaflow)) print(paste(v, length(table(seaflow[[v]])))) # fsc_big

# extra: distribution of the mean of training$time for 100 samples
getTrainingMeans <- function(x, n=1000) {
  sapply(1:n, function(y) mean(x[sample(seq_along(x),round(length(x)/2))]))
}
plot(density(getTrainingMeans(seaflow$time, 1000)), main="mean(training$time)")

