import flet as ft
from sqlite3 import connect
from components.cards import CustomDisplayCard  # Importa un componente personalizado para mostrar tarjetas con información
from components.fields import CustomTextField   # Importa un componente personalizado para campos de texto
from utilidades.colores import customBgColor, customBorderColor, customDashboardBG, customPrimaryColor, customSideBarIconColor, customTextHeaderColor, cutomTextColor  # Importa configuraciones de colores personalizadas
from utilidades.validaciones import validaciones  # Importa las validaciones personalizadas
from db.crud import database  # Importa las funciones de base de datos CRUD (Create, Read, Update, Delete)

# Define una clase "dashboard" que hereda de ft.Container
class dashboard(ft.Container):
    
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True  # Expande el contenedor al tamaño máximo disponible
        self.bgcolor = customDashboardBG  # Establece un color de fondo personalizado para el dashboard
        
        # Define el contenido principal del dashboard
        self.main_content = ft.Column(
            controls=[
                # Contenedor para el título del Dashboard
                ft.Container(
                    bgcolor="whitw",  # Color de fondo blanco (nota: hay un error tipográfico en "whitw", debería ser "white")
                    padding=ft.padding.all(20),  # Padding de 20 unidades en todos los lados
                    content= ft.Text("Dashboard",
                                     color="black",  # Texto del título en color negro
                                     size=20,  # Tamaño de la fuente del título
                                     weight=ft.FontWeight.BOLD,  # Establece el título en negrita
                                     )
                ),
                # Línea divisoria debajo del título
                ft.Divider(color="black", height=0.5, thickness=0.5),  # Divider (línea) con un grosor de 0.5 y color negro
                
                # Contenedor para las tarjetas de información
                ft.Container(
                    padding=ft.padding.all(20),  # Padding alrededor del contenedor
                    content=ft.Row(
                        spacing=10,  # Espaciado entre las tarjetas
                        alignment = ft.MainAxisAlignment.SPACE_AROUND,  # Alinea las tarjetas uniformemente alrededor del espacio disponible
                        controls=[
                            # Tarjetas personalizadas que muestran datos como "Usuarios Totales", "Eventos Totales", etc.
                            CustomDisplayCard(customPrimaryColor, "Usuarios Totales", 33),  # Tarjeta personalizada para usuarios totales
                            CustomDisplayCard("#FC544B", "Eventos Totales", 3),  # Tarjeta para eventos totales
                            CustomDisplayCard("#FEA426", "Votos Totales", 43),  # Tarjeta para votos totales
                            CustomDisplayCard("#63ED7A", "Usuarios ", 66),  # Tarjeta adicional para usuarios
                        ]
                    ),
                ),
                
                # Contenedor para un gráfico de barras
                ft.Container(
                   padding=ft.padding.all(20),  # Padding alrededor del gráfico
                   content= ft.BarChart(
                    bar_groups=[  # Define los grupos de barras que aparecerán en el gráfico
                        # Grupo de barras 1
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[

                                ft.BarChartRod(  # Configuración de cada barra individual
                                    from_y= 0,  # Altura inicial de la barra
                                    to_y= 10,  # Altura final de la barra
                                    width=40,  # Ancho de la barra
                                    color= ft.colors.RED,  # Color de la barra (rojo)
                                    tooltip="APPLE",  # Texto del tooltip que aparece al pasar el cursor sobre la barra
                                    border_radius=0  # Radio de los bordes (0 significa bordes rectos)
                                )
                            ]
                        ),
                        # Grupo de barras 2
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[

                                ft.BarChartRod(
                                    from_y= 0,
                                    to_y= 20,  # Altura mayor que en el primer grupo
                                    width=40,
                                    color= ft.colors.YELLOW_400,  # Color amarillo
                                    tooltip="APPLE",
                                    border_radius=0
                                )
                            ]
                        ),
                        # Grupo de barras 3
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[

                                ft.BarChartRod(
                                    from_y= 0,
                                    to_y= 40,  # Altura aún mayor
                                    width=40,
                                    color= ft.colors.ORANGE,  # Color naranja
                                    tooltip="APPLE",
                                    border_radius=0
                                )
                            ]
                        ),
                        # Grupo de barras 4
                        ft.BarChartGroup(
                            x=0,
                            bar_rods=[

                                ft.BarChartRod(
                                    from_y= 0,
                                    to_y= 40,  # Altura igual que en el grupo anterior
                                    width=40,
                                    color= ft.colors.GREEN,  # Color verde
                                    tooltip="APPLE",
                                    border_radius=0
                                )
                            ]
                        ),
                    ],
                    # Configuración del borde del gráfico
                    border = ft.border.all(1, ft.colors.GREY_400),  # Bordes de color gris con grosor 1
                    # Configuración del eje izquierdo
                    left_axis= ft.ChartAxis(labels_size=40, title=ft.Text("Fruits Supply"), title_size=40),  # Eje izquierdo con el título "Fruits Supply"
                    # Configuración del eje inferior
                    bottom_axis= ft.ChartAxis(
                        labels=[  # Etiquetas en el eje X
                            ft.ChartAxisLabel(
                                value=0,
                                label=ft.Container(ft.Text("Apple"), padding=10)  # Etiqueta "Apple" con padding de 10
                            ),
                            ft.ChartAxisLabel(
                                value=1,
                                label=ft.Container(ft.Text("Apple"), padding=10)  # Otra etiqueta "Apple"
                            ),
                            ft.ChartAxisLabel(
                                value=2,
                                label=ft.Container(ft.Text("Apple"), padding=10)  # Otra etiqueta "Apple"
                            ),
                            ft.ChartAxisLabel(
                                value=3,
                                label=ft.Container(ft.Text("Apple"), padding=10)  # Otra etiqueta "Apple"
                            ),
                        ]
                    )
                )
                )
            ]
        )

        # Define el diseño principal, colocando el contenido principal dentro de un contenedor que ocupa el espacio total
        self.content=ft.Row(
            spacing=0,  # Sin espaciado entre los elementos del layout
            controls=[
                ft.Container(
                    expand= True,  # Expande el contenedor al tamaño máximo
                    content= self.main_content  # Inserta el contenido principal definido previamente
                )
            ]
        )
