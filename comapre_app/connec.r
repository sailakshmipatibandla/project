require("RPostgreSQL")
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "compare_prod", user="innova",password="Innova123",host="localhost")
#df_postgres <- dbGetQuery(con, "SELECT * from sessions")

library(DBI)
library(RPostgreSQL)

con <- dbConnect(RPostgreSQL::PostgreSQL(),
                 host = url$localhost,
                 dbname = url$compare_prod,
                 user = url(0)$innova,
                 password = url$Innova123
)
