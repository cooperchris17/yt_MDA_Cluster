# https://stackoverflow.com/questions/27485549/how-to-colour-the-labels-of-a-dendrogram-by-an-additional-factor-variable-in-r

Sys.setenv(LANG = "en")

library(dendextend)

setwd("~/PHD/Main_Corpus_Project/Cluster_Analysis")

yt <- read.csv('yt22_bnc_dim_grey.csv', row.names = 1)
head(yt)
tail(yt)

data <- yt[,1:6]
head(data)

scaled <- scale(data)
head(scaled)

# Agglomerative clustering, using the default method 'complete'
# 'The algorithm compares the farthest neighbours in all pairs 
# of clusters and merges those clusters whose farthest neighbours
# are the closest' (Levshina, 2015, p. 310). 
# Ward.D2 might also be usable
dend <- as.dendrogram(hclust(dist(scaled)))

# Change the colors: YouTube '1'(black), BNC '4'(grey)
labels_colors(dend) <- as.numeric(yt[,9][order.dendrogram(dend)])
# Change the labels to 'Y' and 'B' 
# still can't read, but it's a bit cleaner
labels(dend) <- paste(as.character(yt[,8])[order.dendrogram(dend)])

plot(dend)

# give each text a label in df with cluster number (class-1 or class-2)
# https://stackoverflow.com/questions/50856937/how-to-add-cluster-id-in-a-seperate-column-of-a-dataframe

# make the clusters more visible in the plot
# plot + color the dend's branches before, based on  clusters:
# plot dendrogram with cluster labels

# trying the 11 cluster solution
dend %>% color_branches(k=11) %>% plot()

solution <- cutree(dend, k=11)

res <- cbind(yt, cluster = factor(solution))
head(res)

write.csv(res,'yt22_bnc_clusters_scaled_11.csv')
