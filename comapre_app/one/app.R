
library(shiny)
library(shinydashboard)

ui<-dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody(
    fluidRow(
      qry = paste0("SELECT name,price,rating FROM compare_app_productmetadata where lower(name) like('%",search,"%') ORDER BY ",input$orderfield," ",input$orderdirection," LIMIT 10 ;"),
      s = dbGetQuery(con, qry),
      box(barplot(s$price,las = 2, main="Price", xlab="Products",  
                  ylab="Total", names.arg=s$name, 
                  border="blue"))
    )
  )
)

server<-function(qry,output){
  
}
shinyApp(ui,server)