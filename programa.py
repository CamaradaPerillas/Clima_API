import requests
import sqlite3

"""Información importante, la API acepta regiones que comiencen
con una mayúscula, al igual que con minúsculas, el programa
preserva el nombre de la región según se escribiese al almacenar
los datos en la base de datos, al comprobar se tiene que escribir
la región de la misma manera, al igual que al borrar datos."""

class Incluir_Datos:
	
	def __init__(self):
		
		self.bd = sqlite3.connect("base_de_datos.db")
		self.cursor = self.bd.cursor()
		
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS datos (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		día INTEGER NOT NULL,
		mes INTEGER NOT NULL,
		año INTEGER NOT NULL,
		tma FLOAT NOT NULL,
		tmi FLOAT NOT NULL,
		región TEXT NOT NULL
		)""")
		
		self.bd.commit()
	
	def borrar_tabla(self, elección):
		if elección == 1:
			self.cursor.execute("""DROP TABLE datos""")
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS datos (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			día INTEGER NOT NULL,
			mes INTEGER NOT NULL,
			año INTEGER NOT NULL,
			tmi FLOAT NOT NULL,
			tma FLOAT NOT NULL,
			región TEXT NOT NULL
			)""")
			self.bd.commit()
			
			print("Tabla borrada.")
			
		elif elección == 2:
			print ("Tabla no borrada.")
	
		
	def borrar(self, día, mes, año, región):
		
		self.cursor.execute("""DELETE FROM datos WHERE
		día = ? AND 
		mes = ? AND
		año = ? AND
		región = ?
		""", (día, mes, año, región))
		
		self.bd.commit()
	
	def introducir_datos(self, día, mes, año, región):
		información = requests.get(
		f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{región}{año}-{mes}-{día}/{año}-{mes}-{día}?unitGroup=metric&elements=tempmax,tempmin"
		)
		información_d = información.json()
		for a in información_d["days"]:
			tmi = a["tempmin"]
			tma = a["tempmax"]
		self.cursor.execute("""INSERT INTO datos
		 (día, mes, año, región, tmi, tma) VALUES 
		(?, ?, ?, ?, ?, ?)""", (día, mes, año, región, tmi, tma))
		
		self.bd.commit()
	
	def comprobar_datos(self, día, mes, año, región):
		self.cursor.execute("""SELECT tmi, tma FROM datos WHERE
		día = ? AND
		mes = ? AND
		año = ?
		 """, (día, mes, año)
		 )
		datos = self.cursor.fetchone()
		tmi, tma= datos
		 
		print(
		f"Día: {día}\nMes: {mes}\nAño: {año}\nTemperatura máxima: {tma}\nTemperatura mínima: {tmi}"
		)
	
	def comprobar_bd(self):
		self.cursor.execute("""SELECT * FROM datos
		 """)
		datos = self.cursor.fetchall()
		 
		print(datos)


incluir_datos = Incluir_Datos()

print("BORRAR TABLA")
incluir_datos.borrar_tabla(
int(input("1. Borrar\n2. No borrar\nElección:"))
)

print("INTODUCIR DATOS")
incluir_datos.introducir_datos(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:")),
str(input("Región:"))
)

print("COMPROBAR DATOS")
incluir_datos.comprobar_datos(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:")),
str(input("Región:"))
  )

print("BORRAR DATOS")
incluir_datos.borrar(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:")),
str(input("Región:"))
)

print("COMPROBAR TABLA")
incluir_datos.comprobar_bd()

print("BORRAR TABLA")
incluir_datos.borrar_tabla(
int(input("1. Borrar\n2. No borrar\nElección:"))
)

	
	
		
		
