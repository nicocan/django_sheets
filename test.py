from gsheets.gsheets import GoogleSheets

g = GoogleSheets()

data = [['A','B','C','D','E','F','G','H'],[1,2,3,4,5,6,7,8]]

g.create('Test')
g.update_values(data)
g.share('nico.candela@gmail.com')

print(g.url)
print(g.spreadsheet_id)

input('Pres to delete')

g.delete(g.spreadsheet_id,permanet=True)