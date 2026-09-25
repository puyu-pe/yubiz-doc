<a id="consultar-las-estancias-del-día-la-lista-y-el-detalle"></a>

# 5.7 Consultar las estancias del día, la lista y el detalle

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Ubicar una estancia registrada, revisar el conjunto del día y abrir su detalle
sin asumir que todos los datos estarán disponibles en cada entorno.

## Acceso condicional

En **Estancias**, abra la lista o la vista diaria declarada en el menú. Use un
registro de prueba conocido cuando el entorno permita hacerlo.

## Punto de partida

Confirme el contexto de trabajo antes de interpretar una lista o detalle.

## Requisitos y datos

- La vista diaria consulta las estancias creadas para la fecha actual.
- La lista admite una consulta paginada y el detalle carga información de una
  estancia seleccionada.
- El detalle reúne los datos de la estancia, sus ítems y referencias operativas.

## Pasos

1. Abra la vista diaria para revisar los registros asociados a la fecha actual.
2. Cambie a la lista si necesita localizar otro registro o revisar más filas.
3. Use los filtros y columnas que estén disponibles en su entorno; no suponga
   que el diseño coincidirá con otra instalación.
4. Abra el detalle de una estancia y compare sujeto, tarifa, ítems, importes y
   observaciones con el caso que está revisando.
5. Si necesita corregir un dato, vuelva al flujo de edición disponible y revise
   el resultado en el detalle antes de continuar con otra acción.

## Campos y validaciones observados

- La vista diaria está delimitada por la fecha actual de la interfaz; confirme el
  resultado visible antes de usarla como cierre operativo.
- La consulta de lista separa la carga de filas del detalle individual.
- Si el registro no existe o no puede cargarse, deténgase y confirme el
  identificador o los filtros; no cree una segunda estancia como sustituto.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz puede devolver la lista diaria, una lista paginada y el detalle del
registro seleccionado. La presentación, filtros disponibles y datos reales
siguen pendientes de verificación en el entorno.

## Advertencias y casos límite

Una lista o detalle visible no reemplaza la confirmación del caso operativo.

## Problemas frecuentes y condiciones de detención

- La vista diaria no muestra el caso esperado: revise fecha y contexto antes de
  realizar cambios.
- El detalle no coincide con el caso: no convierta ni anule hasta confirmar el
  registro correcto.
- Una lista vacía no demuestra que no existan registros fuera del filtro actual.

## Enlaces relacionados

- [Registrar una estancia](registrar-estancia.md)
- [Convertir, anular y consultar reportes de estancias](convertir-o-anular-estancia.md)
