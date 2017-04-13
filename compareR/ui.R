library(plotly)
library(shiny)
library(shinydashboard)
shinyUI(fluidPage(
    ui<-dashboardPage(skin = "blue",
        dashboardHeader(title = tags$a(href='#',tags$img(src='http://ec2-52-66-29-252.ap-south-1.compute.amazonaws.com/1.gif',height=50,width=185,align = "fit"))),
    dashboardSidebar(
      width = 340,
        sidebarSearchForm(textId = "search", buttonId = "searchButton",
                          label = "Search..."),
        selectInput("plotfield", 
                    label = "Choose a variable to display",
                    choices = list("By price", "By rating"),
                    selected = "By price"),
        selectInput("orderfield", 
                    label = "Sort by",
                    choices = list(" Price", " Rating","Name"),
                    selected = " Price"),
        selectInput("orderdirection", 
                    label = "Order by",
                    choices = list("DESC", "ASC"),
                    selected = "DESC"),
        br(),
        br(),
        
        tags$img(src="http://ec2-52-66-29-252.ap-south-1.compute.amazonaws.com/search.png",height=300,width=330)
    
      
    ),
    dashboardBody(
    
      HTML('<center><img src="http://ec2-52-66-29-252.ap-south-1.compute.amazonaws.com/9.gif" height="80" width="450"></center>'),
      #tags$img(src='9.gif', align = "left",height=80,width=450),
      #h1("Analytics on electronic products",align = "center"),
      br(),
      br(),
      h4("Every product detail differs in different websites in different ways. This Product Analysis enables you to understand these differences and helps you to choose the right product before purchasing. ",align="right"),
      br(),
      h4("Analyzing various parameters of a particular product for better understanding .", style = "font-family: 'times'; font-si16pt",align="center"),
      br(),
      plotlyOutput("plots")
      
    
  )
)
)
)





