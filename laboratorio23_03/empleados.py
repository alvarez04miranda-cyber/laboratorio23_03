class Empleado:
    """Clase base que representa a cualquier empleado"""
    def __init__(self, nombre, edad, salario_base, años_experiencia=0):
        # Atributos públicos
        self.nombre = nombre
        self.edad = edad
        # Atributo protegido (convención: _ significa "no tocar directamente")
        self._salario_base = salario_base
        # Nuevo atributo para el reto
        self.años_experiencia = años_experiencia
    def calcular_salario(self):
        """Método base que será sobrescrito por las clases hijas"""
        return self._salario_base
    def mostrar_info(self):
        """Muestra la información básica del empleado"""
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: ${self.calcular_salario():.2f}"
    def aumentar_salario(self, porcentaje):
        """Aumenta el salario base en un porcentaje dado"""
        incremento = self._salario_base * (porcentaje / 100)
        self._salario_base += incremento
        return f"Salario aumentado en {porcentaje}%. Nuevo salario base: ${self._salario_base:.2f}"


class Gerente(Empleado):
    """Gerente - Hereda de Empleado"""
    
    def __init__(self, nombre, edad, salario_base, bono, departamento, años_experiencia=0):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base, años_experiencia)
        # Atributos específicos de Gerente
        self.bono = bono
        self.departamento = departamento
    
    def calcular_salario(self):
        """SOBRESCRITURA: El salario del gerente incluye el bono"""
        # Los años de experiencia dan un bono adicional del 2% por año
        bono_experiencia = self._salario_base * (self.años_experiencia * 0.02)
        return self._salario_base + self.bono + bono_experiencia
    
    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica del gerente"""
        return (f"Gerente: {self.nombre}, Edad: {self.edad}, "
                f"Departamento: {self.departamento}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base} + Bono: ${self.bono})")


class Desarrollador(Empleado):
    """Desarrollador - Hereda de Empleado"""
    
    def __init__(self, nombre, edad, salario_base, lenguaje, horas_extra=0, pago_hora=50, años_experiencia=0):
        super().__init__(nombre, edad, salario_base, años_experiencia)
        # Atributos específicos
        self.lenguaje = lenguaje
        self.horas_extra = horas_extra
        self.pago_hora = pago_hora
    
    def calcular_salario(self):
        """SOBRESCRITURA: El desarrollador gana extra por horas extra y por experiencia"""
        extra_horas = self.horas_extra * self.pago_hora
        # Los años de experiencia dan un bono adicional del 3% por año
        bono_experiencia = self._salario_base * (self.años_experiencia * 0.03)
        return self._salario_base + extra_horas + bono_experiencia
    
    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica"""
        extra = self.horas_extra * self.pago_hora
        return (f"Desarrollador: {self.nombre}, Edad: {self.edad}, "
                f"Lenguaje: {self.lenguaje}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base} + "
                f"HE: {self.horas_extra} x ${self.pago_hora} = ${extra})")


# RETO 1: Clase Practicante
class Practicante(Empleado):
    """Practicante - Hereda de Empleado, gana el 70% del salario base"""
    
    def __init__(self, nombre, edad, salario_base, universidad, años_experiencia=0):
        super().__init__(nombre, edad, salario_base, años_experiencia)
        self.universidad = universidad
    
    def calcular_salario(self):
        """SOBRESCRITURA: El practicante gana el 70% del salario base"""
        return self._salario_base * 0.70
    
    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica del practicante"""
        return (f"Practicante: {self.nombre}, Edad: {self.edad}, "
                f"Universidad: {self.universidad}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(70% de ${self._salario_base})")


def mostrar_nomina(empleados):
    """FUNCIÓN QUE DEMUESTRA POLIMORFISMO"""
    print("\n" + "="*60)
    print("NOMINA DE EMPLEADOS")
    print("="*60)
    
    total_nomina = 0
    
    for empleado in empleados:
        print(empleado.mostrar_info())
        total_nomina += empleado.calcular_salario()
    
    print("="*60)
    print(f"TOTAL NOMINA: ${total_nomina:.2f}")
    print("="*60)


def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("="*50)
    print("1. Agregar empleado regular")
    print("2. Agregar gerente")
    print("3. Agregar desarrollador")
    print("4. Agregar practicante (RETO)")
    print("5. Ver todos los empleados")
    print("6. Calcular salario de un empleado")
    print("7. Ver total de nómina")
    print("8. Aumentar salario a un empleado (RETO)")
    print("9. Salir")
    print("-"*50)


def agregar_empleado(empleados):
    """Agrega un empleado regular"""
    print("\n--- NUEVO EMPLEADO REGULAR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    años_exp = int(input("Años de experiencia: "))
    
    nuevo = Empleado(nombre, edad, salario, años_exp)
    empleados.append(nuevo)
    print(f"✓ Empleado {nombre} agregado exitosamente")
    return empleados


def agregar_gerente(empleados):
    """Agrega un gerente"""
    print("\n--- NUEVO GERENTE ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    bono = float(input("Bono: $"))
    depto = input("Departamento: ")
    años_exp = int(input("Años de experiencia: "))
    
    nuevo = Gerente(nombre, edad, salario, bono, depto, años_exp)
    empleados.append(nuevo)
    print(f"✓ Gerente {nombre} agregado exitosamente")
    return empleados


def agregar_desarrollador(empleados):
    """Agrega un desarrollador"""
    print("\n--- NUEVO DESARROLLADOR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    lenguaje = input("Lenguaje principal: ")
    horas = int(input("Horas extra (0 si no tiene): "))
    años_exp = int(input("Años de experiencia: "))
    
    nuevo = Desarrollador(nombre, edad, salario, lenguaje, horas, 50, años_exp)
    empleados.append(nuevo)
    print(f"✓ Desarrollador {nombre} agregado exitosamente")
    return empleados


def agregar_practicante(empleados):
    """Agrega un practicante (RETO)"""
    print("\n--- NUEVO PRACTICANTE ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base (referencia): $"))
    universidad = input("Universidad: ")
    
    nuevo = Practicante(nombre, edad, salario, universidad)
    empleados.append(nuevo)
    print(f"✓ Practicante {nombre} agregado exitosamente")
    return empleados


def ver_empleados(empleados):
    """Muestra todos los empleados"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return
    
    print("\n" + "="*60)
    print("LISTA DE EMPLEADOS")
    print("="*60)
    
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.mostrar_info()}")
    
    print("="*60)


def calcular_salario_individual(empleados):
    """Calcula el salario de un empleado específico"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return
    
    print("\n--- SELECCIONE EMPLEADO ---")
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.nombre} ({type(emp).__name__})")
    
    try:
        opcion = int(input("\nNúmero del empleado: ")) - 1
        if 0 <= opcion < len(empleados):
            emp = empleados[opcion]
            print("\n" + "- "*40)
            print(emp.mostrar_info())
            print(f"Salario calculado: ${emp.calcular_salario():.2f}")
            print("- "*40)
        else:
            print("△ Opción inválida")
    except ValueError:
        print("△ Por favor ingrese un número válido")


def aumentar_salario_empleado(empleados):
    """Aumenta el salario de un empleado específico (RETO)"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return
    
    print("\n--- SELECCIONE EMPLEADO PARA AUMENTAR SALARIO ---")
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.nombre} ({type(emp).__name__}) - Salario actual: ${emp.calcular_salario():.2f}")
    
    try:
        opcion = int(input("\nNúmero del empleado: ")) - 1
        if 0 <= opcion < len(empleados):
            emp = empleados[opcion]
            porcentaje = float(input("Porcentaje de aumento: "))
            resultado = emp.aumentar_salario(porcentaje)
            print(f"\n✓ {resultado}")
            print(f"Nuevo salario total: ${emp.calcular_salario():.2f}")
        else:
            print("△ Opción inválida")
    except ValueError:
        print("△ Por favor ingrese un número válido")


def ver_total_nomina(empleados):
    """Muestra el total de la nómina"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return
    
    total = sum(emp.calcular_salario() for emp in empleados)
    
    print("\n" + "="*50)
    print("RESUMEN DE NÓMINA")
    print("="*50)
    print(f"Total empleados: {len(empleados)}")
    print(f"Total nómina: ${total:.2f}")
    print("="*50)


if __name__ == "__main__":
    # Lista para almacenar empleados
    empleados = []
    
    # Agregar algunos empleados de ejemplo
    empleados.append(Empleado("Juan Pérez", 30, 3000, 5))
    empleados.append(Gerente("Ana Gómez", 45, 5000, 2000, "Tecnología", 10))
    empleados.append(Desarrollador("Carlos López", 28, 3500, "Python", 10, 50, 3))
    empleados.append(Desarrollador("María Rodríguez", 32, 4000, "Java", 0, 50, 2))
    empleados.append(Gerente("Roberto Sánchez", 50, 8000, 3500, "Ventas", 15))
    empleados.append(Practicante("Luis Fernández", 22, 2000, "Universidad Nacional", 0))
    
    print("\n" + "="*50)
    print("SISTEMA DE EMPLEADOS CON HERENCIA Y POLIMORFISMO")
    print("="*50)
    print("Empleados de ejemplo cargados")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            empleados = agregar_empleado(empleados)
        elif opcion == "2":
            empleados = agregar_gerente(empleados)
        elif opcion == "3":
            empleados = agregar_desarrollador(empleados)
        elif opcion == "4":
            empleados = agregar_practicante(empleados)
        elif opcion == "5":
            ver_empleados(empleados)
        elif opcion == "6":
            calcular_salario_individual(empleados)
        elif opcion == "7":
            ver_total_nomina(empleados)
        elif opcion == "8":
            aumentar_salario_empleado(empleados)
        elif opcion == "9":
            print("\n" + "="*50)
            print("¡Hasta luego! Gracias por usar el sistema")
            print("="*50)
            break
        else:
            print("\n△ Opción inválida. Intente nuevamente.")

