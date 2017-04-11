library(shiny)
library(plotly)
library(ggplot2)
library(DBI)
library(RColorBrewer)
library(viridis)
library(RPostgreSQL)
pg = dbDriver("PostgreSQL")
con = dbConnect(pg, user="postgres", password="Innova123",
                host="localhost", dbname="compare_prod")
shinyServer(
  function(input, output) {
  output$plots <- renderPlotly({
    search = tolower(input$search)
    if(search==c("")){
      
      search="iphone"
    }
    print(search)
    qry = paste0("SELECT id , name,price,rating FROM compare_app_productmetadata where lower(name) like('%",search,"%') ORDER BY ",input$orderfield," ",input$orderdirection," LIMIT 100 ;")
    s = dbGetQuery(con, qry)
   
    if(input$plotfield == "by price"){
     # marker = list(color = brewer.pal(12, "Paired"))
      plot_ly(s, y = ~ price, x = ~ seq(1,length(price)), type = "bar",mode = 'text', text = ~name,marker = list(color = cal_color(length(s$name)))) %>%
        layout(title = "Plot for comparing price and rating",
  
                 xaxis = list(title = "",showticklabels=FALSE), 
                 yaxis = list(title = "Price"),xlab=FALSE
               
               )
    }else{
      plot_ly(s, y = ~ rating, x = ~ seq(1,length(rating)), type = "bar",mode = 'text', text = ~name,marker = list(color = cal_color(length(s$name)))) %>%
        layout(title = "Plot for comparing Price and Rating",
               
               xaxis = list(title = "",showticklabels=FALSE), 
               yaxis = list(title = "Rating")
              )  
    }
  })
})
 

cal_color <- function(steps){
  step_size = 255/(steps-1)
  return_cols = c()
  for (i in 0:(steps-1)){
    return_cols <- c(return_cols, rgb(22, 255-(step_size*i), step_size*i, maxColorValue=255))
  }
return(return_cols)
}
