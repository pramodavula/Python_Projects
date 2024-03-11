import snowflake.connector

conn = snowflake.connector.connect(
    user = 'pavuladbt',
    password = 'Pra@mod!98832609',
    account = 'tu22917.us-east-2.aws',
    session_parameters = {
        'QUERY_TAG':'EndofMonthFinancials'        
    }

)

conn.cursor().execute("select * from ")