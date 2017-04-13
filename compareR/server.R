library(shiny)
library(plotly)
library(ggplot2)
library(DBI)
library(RColorBrewer)
library(viridis)
library(RPostgreSQL)
pg = dbDriver("PostgreSQL")
con = dbConnect(pg, user="innova", password="Innova123", host="sailakshmiakhila.c9fc66eyon9l.ap-south-1.rds.amazonaws.com", dbname="compare_prod")
shinyServer(
  function(input, output) {
  output$plots <- renderPlotly({
    event.data <- event_data("plotly_click", source = "select")
    if(is.null(event.data) == F){
      
    }
    search = tolower(input$search)
    if(search==c("")){
      
      search="iphone"
    }
    qry = paste0("SELECT compare_app_productmetadata.id , name,price,rating, url FROM compare_app_productmetadata join compare_app_product on compare_app_product.id = compare_app_productmetadata.product_id where lower(name) like('%",search,"%') ORDER BY ",input$orderfield," ",input$orderdirection," LIMIT 100 ;")
    s = dbGetQuery(con, qry)
    print(qry)
    if(input$plotfield == "By price"){
     # marker = list(color = brewer.pal(12, "Paired"))
      plot_ly(s, y = ~ price, x = ~ seq(1,length(s$price)), type = "bar",mode = 'text', text = ~name,marker = list(color = cal_color(length(s$name)))) %>%
        layout(title = "Plot for comparing price and rating",
  
                 xaxis = list(title = "",showticklabels=FALSE), 
                 yaxis = list(title = "Price"),xlab=FALSE
               
               )
    }else{
      plot_ly(s, y = ~ rating, x = ~ seq(1,length(s$rating)), type = "bar",mode = 'text', text = ~name,marker = list(color = cal_color(length(s$name)))) %>%
        layout(title = "Plot for comparing Price and Rating",
               
               xaxis = list(title = "",showticklabels=FALSE), 
               yaxis = list(title = "Rating")
               
              )  
    }
    #p$data[[1]]$links = s$url
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


