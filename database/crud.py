from database.connector import DatabaseConnector


class CRUD(DatabaseConnector):

    def insert_gamepress(self, pokemon_list):
        argument_string = ','.join(["%s"] * len(pokemon_list))
        sql = "INSERT INTO pokemon.pokemon_gamepress (pokedex_number,generation,primary_type,sub_type,pokemon_name_english,attack,defense,stamina,is_mega,level_20_cp,level_30_cp,level_35_cp,level_40_cp,purification_candy,purification_dust,buddy_km,candy_for_evolution,catch_rate,flee_rate,primary_move,secondary_move,detail_link) values {}".format(argument_string)
        try:
            self.cursor.execute(self.cursor.mogrify(sql, pokemon_list).decode("utf8"))
            self.db.commit()
        except Exception as e:
            print(" INSERT Exception : ", e)

    def read(self, schema, table, colum):
        sql = " SELECT {colum} from {schema}.{table}".format(colum=colum, schema=schema, table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            result = (" READ Exception : ", e)
        return result

    def updateDB(self, schema, table, colum, value, condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema
                                                                                                   , table=table,
                                                                                                   colum=colum,
                                                                                                   value=value,
                                                                                                   condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" UPDATE Exception : ", e)

    def deleteDB(self, schema, table, condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema, table=table,
                                                                          condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" DELETE Exception : ", e)