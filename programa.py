import requests
import sqlite3

class Incluir_Datos:
	
	def __init__(self):
		
		self.bd = sqlite3.connect("base_de_datos.db")
		self.cursor = self.bd.cursor()
		
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS datos (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		día INTEGER NOT NULL,
		mes INTEGER NOT NULL,
		año INTEGER NOT NULL,
		temperatura FLOAT NOT NULL,
		clima TEXT NOT NULL
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
			temperatura FLOAT NOT NULL,
			clima TEXT NOT NULL
			)""")
			self.bd.commit()
			
			print("Tabla borrada.")
			
		elif elección == 2:
			print ("Tabla no borrada.")
	
		
	def borrar(self, día, mes, año):
		
		self.cursor.execute("""DELETE FROM datos WHERE
		día = ? AND 
		mes = ? AND
		año = ?
		""", (día, mes, año))
		
		self.bd.commit()
	
	def introducir_datos(self, día, mes, año, temperatura, clima):
		self.cursor.execute("""INSERT INTO datos
		 (día, mes, año, temperatura, clima) VALUES 
		(?, ?, ?, ?, ?)""", (día, mes, año, temperatura, clima))
		
		self.bd.commit()
	
	def comprobar_datos(self, día, mes, año):
		self.cursor.execute("""SELECT temperatura, clima FROM datos WHERE
		día = ? AND
		mes = ? AND
		año = ?
		 """, (día, mes, año)
		 )
		datos = self.cursor.fetchone()
		temperatura, clima = datos
		 
		print(
		f"Día: {día}\nMes: {mes}\nAño: {año}\nTemperatura: {temperatura}\nClima: {clima}"
		)
	
	def comprobar_bd(self):
		self.cursor.execute("""SELECT * FROM datos
		 """)
		datos = self.cursor.fetchall()
		 
		print(datos)

incluir_datos = Incluir_Datos()

print("INTODUCIR DATOS")
incluir_datos.introducir_datos(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:")),
float(input("Temperatura:")),
str(input("Clima:"))
)

print("COMPROBAR DATOS")
incluir_datos.comprobar_datos(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:"))
  )

print("BORRAR DATOS")
incluir_datos.borrar(
int(input("Día:")),
int(input("Mes:")),
int(input("Año:"))
)

print("COMPROBAR TABLA")
incluir_datos.comprobar_bd()

print("BORRAR TABLA")
incluir_datos.borrar_tabla(
int(input("1. Borrar\n2. No borrar\nElección:"))
)

	
	
		
		
