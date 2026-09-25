<a id="registrar-el-saldo-inicial-de-caja"></a>

# 6.14 Registrar el saldo inicial de caja

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un saldo inicial para comenzar la revisión de caja cuando esta opción esté
habilitada en la sesión.

## Acceso condicional

La acción es condicional y depende de la sesión y configuración. La interfaz
limita el registro a uno por día, establecimiento y persona usuaria; esto no define
una política de apertura, autorización, arqueo o responsabilidad de caja.

## Requisitos y datos

- Importe mayor que cero.
- Método disponible en el formulario.
- Fecha y hora que representen el momento a registrar.
- Observación opcional que permita identificar el contexto sin incluir datos sensibles.

## Punto de partida

Desde el reporte de caja, seleccione **Registrar saldo inicial** y revise el aviso
del formulario antes de completar los datos.

## Pasos

1. Verifique establecimiento, sesión y fecha antes de abrir el formulario.
2. Confirme que no exista otro saldo inicial para el mismo día en ese contexto.
3. Ingrese un importe mayor que cero y seleccione el método disponible.
4. Revise fecha y hora; agregue una observación solo si ayuda a identificar el registro.
5. Seleccione **Guardar** y espere el resultado mostrado por el formulario.
6. Cierre el formulario y vuelva a consultar el reporte para revisar el saldo inicial
   que aparece con el filtro actual.

## Campos y validaciones observados

El formulario solicita importe, método y fecha y hora; la observación es opcional.
La validación revisada exige importe numérico mayor que cero y una fecha válida. Para
el saldo inicial, la interfaz verifica que no exista otro registro el mismo día para la
persona usuaria y establecimiento del contexto de sesión.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El recorrido registra una operación manual de tipo saldo inicial y actualiza el
reporte después de una respuesta exitosa. La interfaz fija su dirección como ingreso.
La persistencia, el método disponible, el resultado visible y su efecto operativo
pueden variar según la configuración disponible.

## Advertencias y casos límite

No use este registro para corregir diferencias detectadas después. Si ya existe un
saldo inicial para el día, detenga el flujo en vez de intentar duplicarlo. No infiera
conversión de moneda, aprobación ni disponibilidad física a partir del formulario.

## Problemas frecuentes y condiciones de detención

- Importe vacío, no numérico o no positivo: corríjalo antes de guardar.
- Fecha u hora no representativa: detenga el registro y revise el contexto.
- Ya existe un saldo inicial: no repita la operación; confirme el registro existente.

## Enlaces relacionados

- [Revisar ingresos, egresos y saldo de caja](revisar-ingresos-y-egresos.md)
- [Registrar una inyección o ajuste manual de caja](registrar-operacion-manual.md)
- [Caja y reportes](index.md)
