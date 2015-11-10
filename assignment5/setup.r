
required_packages <- c("caret","rpart","tree","randomForest","e1071","ggplot2")

for (package in required_packages) {
  if (!require(package, character.only=TRUE)) { 
    install.packages(package, character.only=TRUE)
  }
}
