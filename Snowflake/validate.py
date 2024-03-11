import snowflake.connector

# Gets the version

ctx = snowflake.connector.connect(
    user = 'pavuladbt',
    password = 'Pra@mod!98832609',
    account = 'tu22917.us-east-2.aws'

)

cs = ctx.cursor()
try:
    cs.execute("select current_version()"
               )
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()

ctx.close()