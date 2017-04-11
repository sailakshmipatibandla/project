library(shiny)
library(plotly)

ui <- fluidPage(
  plotlyOutput("plot"),
  verbatimTextOutput("event")
  pg = dbDriver("PostgreSQL")
  con = dbConnect(pg, user="postgres", password="Innova123",
                  host="localhost", dbname="compare_prod")
  qry = paste0("SELECT name,price,rating FROM compare_app_productmetadata where lower(name) like('%",search,"%') ORDER BY ",input$orderfield," ",input$orderdirection," LIMIT 10 ;")
  s = dbGetQuery(con, qry)
)


server <- function(input, output) {
 
  # renderPlotly() also understands ggplot2 objects!
  output$plot <- renderPlotly({
    plot_ly(s, x = s$name, y = s$price)
  })
  
  output$event <- renderPrint({
    d <- event_data("plotly_hover")
    if (is.null(d)) "Hover on a point!" else d
  })
}

shinyApp(ui, server)