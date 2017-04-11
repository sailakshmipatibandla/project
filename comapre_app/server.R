library(shiny)
library(DBI)
library(RPostgreSQL)
pg = dbDriver("PostgreSQL")
con = dbConnect(pg, user="postgres", password="Innova123",
                host="localhost", dbname="compare_prod")
shinyServer(function(input, output) {
  
  s = dbGetQuery(con, "SELECT * FROM compare_app_productmetadata LIMIT 100 ;")
  x    <- s$price
  y    <- s$rating
  
  output$distPlot <- renderPlot({
    # draw the histogram with the specified number of bins
    bins <- seq(min(x), max(x), length.out = input$bins + 1)
    hist(x, breaks = bins, col = 'darkgray', border = 'white')
  })
  
    output$distPlot1 <- renderPlot({
      plot(y ~ x, data=s, type="o", xlab="PC1", ylab="PC2")
    })
    
          output$distPlot2 <- renderPlot({ 
        hist(x, 
             main="Histogram for comparision", 
             xlab="Passengers", 
             border="blue", 
             col="green",
             xlim=c(100,700),
             las=1, 
             breaks=5) 
      
  })
  
})
  

