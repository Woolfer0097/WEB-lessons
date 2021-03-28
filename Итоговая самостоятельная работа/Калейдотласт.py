import sqlite3

filename = input()
size = int(input())
rate = int(input())

connection = sqlite3.connect(filename)
cursor = connection.cursor()
first_color_list = []
second_color_list = []
size_list = []
first_color_list.append(*list(str(*i) for i in cursor.execute("""SELECT colors.name FROM colors 
LEFT JOIN streelers ON colors.id = streelers.start_id """ + f"WHERE streelers.size > {size} "
                                                            f"AND streelers.rate < {rate}")))
second_color_list.append(*list(str(*i) for i in cursor.execute(f"SELECT colors.name "
                                                               f"FROM colors "
                                                               f"LEFT JOIN streelers ON colors.id = streelers.end_id "
                                                               f"WHERE streelers.size > {size} "
                                                               f"AND streelers.rate < {rate}")))
size_list.append(*list(str(*i) for i in cursor.execute(f"SELECT streelers.size "
                                                       f"FROM colors "
                                                       f"LEFT JOIN streelers ON colors.id = streelers.end_id "
                                                       f"WHERE streelers.size > {size} "
                                                       f"AND streelers.rate < {rate}")))
result = []
for (first_color, second_color, size) in zip(first_color_list, second_color_list, size_list):
    result.append([first_color, second_color, size])
result.sort(key=lambda x: x[2])
print(" ".join(*result))
