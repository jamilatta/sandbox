## Most of this code was adapted near-verbatim from Neil's post about ISMB 2012.
## http://nsaunders.wordpress.com/2012/08/16/twitter-coverage-of-the-ismb-2012-meeting-some-statistics/

## Modify this. This is where I keep this repo.
repoDir <- ("/Users/jamil/project/sandbox/twitter/twitterarchive/")

## Go to the analysis directory
setwd(paste(repoDir, "repo", sep=""))

## Function needs better documentation
twitterchivePlots <- function (filename=NULL) {

    ## Load required packages
    require(tm)
    require(wordcloud)
    require(RColorBrewer)

    if (class(filename)!="character") stop("filename must be character")
    if (!file.exists(filename)) stop(paste("File does not exist:", filename))

    searchTerm <- sub("\\.txt", "", basename(filename))

    message(paste("Filename:", filename))
    message(paste("Search Term: ", searchTerm))

    ## Read in the data and munge around the dates.
    ## I can't promise the fixed widths will always work out for you.
    message("Lendo dados")
    trim.whitespace <- function(x) gsub("^\\s+|\\s+$", "", x) # Function to trim leading and trailing whitespace from character vectors.
    d <- read.fwf(filename, widths=c(18, 14, 18, 1000), stringsAsFactors=FALSE, comment.char="")
    d <- as.data.frame(sapply(d, trim.whitespace))
    names(d) <- c("id", "datetime", "user", "text")
    d$user <- sub("#user_", "@", d$user)
    d$datetime <- as.POSIXlt(d$datetime, format="%b %d %H:%M")
    d$date <- as.Date(d$datetime)
    d$hour <- d$datetime$hour
    d <- na.omit(d) # CRs cause a problem. explain this later.
    head(d)

    ## Number of tweets by date for the last n days
    recentDays <- 7
    message(paste("Número de tweets por dia nos últimos", recentDays, "days."))
    recent <- subset(d, date>=(max(date)-recentDays))
    byDate <- as.data.frame(table(recent$date))
    names(byDate) <- c("date", "tweets")
    png(paste(searchTerm, "barplot-tweets-by-date.png", sep="--"), w=1000, h=700)
    par(mar=c(8.5,4,4,1))
    with(byDate, barplot(tweets, names=date, col="red", las=2, cex.names=1.2, cex.axis=1.2, mar=c(10,4,4,1), main=paste("Número de tweets por dia nos últimos 7 dias.", paste("Termos: "), paste(searchTerm), sep="\n")))
    dev.off()


    ## Number of tweets by hour
    message("Traçando número de tweets por hora")
    byHour <- as.data.frame(table(d$hour))
    names(byHour) <- c("hour", "tweets")
    png(paste(searchTerm, "barplot-tweets-by-hour.png", sep="--"), w=1000, h=700)
    with(byHour, barplot(tweets, names.arg=hour, col="red", las=1, cex.names=1.2, cex.axis=1.2, main=paste("Número de tweets por hora", paste("Termos:"), paste(searchTerm), paste("Data:", Sys.Date()), sep="\n")))
    dev.off()

    ## Barplot of top 20 hashtags
    message("Traçando os top 20 hashtags.")
    words <- unlist(strsplit(as.character(d$text), " "))
    head(table(words))
    ht <- words[grep("^#", words)]
    ht <- tolower(ht)
    ht <- gsub("[^A-Za-z0-9]", "", ht) # remove anything not starting with a letter or number
    ht <- as.data.frame(table(ht))
    ht <- subset(ht, ht!="") # remove blanks
    ht <- ht[sort.list(ht$Freq, decreasing=TRUE), ]
    ht <- ht[-1, ] # remove the term you're searching for? it usually dominates the results.
    ht <- head(ht, 20)
    head(ht)
    png(paste(searchTerm, "barplot-top-hashtags.png", sep="--"), w=1000, h=700)
    par(mar=c(5,10,4,2))
    with(ht[order(ht$Freq), ], barplot(Freq, names=ht, horiz=T, col="red", las=1, cex.names=1.2, cex.axis=1.2, main=paste("Os top 20 hashtags", paste("Termos: "), paste(searchTerm), paste("Data:", Sys.Date()), sep="\n")))
    dev.off()

    ## Top Users
    message("Traçando os usuários que mais falam do SciELO no Twitter")
    users <- as.data.frame(table(d$user))
    colnames(users) <- c("user", "tweets")
    users <- users[order(users$tweets, decreasing=T), ]
    users <- subset(users, user!=searchTerm)
    users <- head(users, 20)
    head(users)
    png(paste(searchTerm, "barplot-top-users.png", sep="--"), w=1000, h=700)
    par(mar=c(5,10,4,2))
    with(users[order(users$tweets), ], barplot(tweets, names=user, horiz=T, col="red", las=1, cex.names=1.2, cex.axis=1.2, main=paste("Os 20 usuários que mais tweetam.", paste("Termos: "), paste(searchTerm), paste("Data:", Sys.Date()), sep="\n")))
    dev.off()

    ## Word clouds
    message("Traçando a nuvem de palavras.")
    words <- unlist(strsplit(as.character(d$text), " "))
    words <- grep("^[A-Za-z0-9]+$", words, value=T)
    words <- tolower(words)
    words <- words[-grep("^[rm]t$", words)] # remove "RT"
    words <- words[!(words %in% stopwords("pt"))] # remove pt stop words
    words <- words[!(words %in% stopwords("en"))] # remove en stop words
    words <- words[!(words %in% stopwords("es"))] # remove es stop words
    words <- words[!(words %in% c("rt", "via", "using", "sobre", 1:9))] # remove RTs, MTs, via, and single digits.
    wordstable <- as.data.frame(table(words))
    wordstable <- wordstable[order(wordstable$Freq, decreasing=T), ]
    wordstable <- wordstable[-1, ] # remove the hashtag you're searching for? need to functionalize this.
    head(wordstable)
    png(paste(searchTerm, "wordcloud.png", sep="--"), w=800, h=800)
    wordcloud(wordstable$words, wordstable$Freq, scale = c(8, .2), min.freq = 3, max.words = 200, random.order = FALSE, rot.per = .15, colors = brewer.pal(8, "Dark2"))
    dev.off()

    message(paste(searchTerm, ": Feito!\n"))
}

filelist <- list("somatic_embryogenesis.txt")
lapply(filelist, twitterchivePlots)