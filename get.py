def dd() :
    import mysql.connector as sql

    data_base = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mony_transfer"
    )
    mycursor = data_base.cursor()
    mysqls = 'SELECT coin_name , coin_price FROM coins_values WHERE date = "2024-06-17" '
    mycursor.execute(mysqls )
    fetch_data_base_coin = mycursor.fetchall()
    # print(fetch_data_base_coin)

    for i in range(len(fetch_data_base_coin)) :
        fetch_data_base_coin[i] ={fetch_data_base_coin[i][0] : fetch_data_base_coin[i][1]}

    # print(fetch_data_base_coin)
    data = dict()
    for j in fetch_data_base_coin :
        data.update(j)
    # print(data)

    l = data.keys()
    # print(l)

    for o in l :
        data[o] = str(data[o])
    return data
    # print(data)