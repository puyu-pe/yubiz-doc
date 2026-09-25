<a id="ubicarse-en-yubiz-y-reconocer-el-menú-disponible"></a>

# 1.2 Ubicarse en Yubiz y reconocer el menú disponible

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Reconocer el contexto de trabajo y localizar una tarea sin asumir que todas las
opciones están habilitadas.

## Acceso condicional

El menú se construye según los módulos disponibles para la sesión. Las secciones
y acciones visibles pueden cambiar entre cuentas, roles y entornos.

## Requisitos y datos

- Sesión iniciada.
- Tarea que se desea realizar y, si aplica, establecimiento confirmado.

## Punto de partida

En la pantalla inicial posterior al acceso.

## Pasos

1. Revise el nombre de la empresa y el establecimiento mostrados en el encabezado.
2. Abra el menú de navegación disponible para su sesión.
3. Ubique la sección relacionada con la tarea y revise sus opciones antes de
   abrir una acción.
4. Si una opción esperada no aparece, confirme el contexto y la disponibilidad
   con el equipo responsable.

## Campos y validaciones observados

El encabezado muestra el establecimiento de la sesión. La interfaz usa
entradas de menú condicionadas por módulo, por lo que la presencia de una opción
no puede generalizarse a todas las personas usuarias.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La persona usuaria puede usar el menú disponible y el contexto visible para
orientarse hacia tareas habilitadas en su sesión.

## Advertencias y casos límite

No interprete una opción ausente como una autorización para habilitarla ni como
un fallo definitivo. Evite realizar operaciones desde una sección distinta solo
por similitud de nombre.

## Problemas frecuentes y condiciones de detención

- Menú distinto al esperado: confirme establecimiento, rol y módulo disponible.
- Contexto de empresa o establecimiento incorrecto: vuelva a revisarlo antes de
  abrir una tarea operativa.
- Duda sobre una función: detenga la operación y use la guía específica cuando
  exista.

## Enlaces relacionados

- [Iniciar sesión y elegir establecimiento](iniciar-sesion.md)
- [Cambiar de establecimiento durante la sesión](cambiar-establecimiento.md)
