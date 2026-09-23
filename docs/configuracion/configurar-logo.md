# Configurar logo de la empresa

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Actualizar o retirar el logo visible de la empresa cuando esa opción esté habilitada.

## Acceso condicional

La pantalla se carga dentro de una sesión con módulo disponible. No se afirma quién
puede guardar o eliminar un logo ni dónde se verá el resultado en producción.

## Requisitos y datos

- Acceso a la opción de logo.
- Archivo PNG preparado para cargar.
- Una imagen de al menos 200 píxeles de ancho o alto y sin superar 1500 píxeles por lado.

## Punto de partida

Abra la pantalla de logo y revise la vista previa o el estado sin logo que se muestre.

## Pasos

1. Seleccione un archivo PNG desde el control de carga.
2. Revise la vista previa antes de guardar.
3. Si la imagen es válida, use **Guardar logo** una sola vez.
4. Espere el resultado mostrado y confirme que la vista previa se actualice.
5. Para retirarlo, use **Eliminar logo** solo después de confirmar que corresponde; la
   interfaz solicita confirmación antes de continuar.

## Campos y validaciones observados

El navegador acepta PNG, rechaza otro formato y valida dimensiones mínimas y máximas.
El botón de guardar permanece deshabilitado hasta que exista una selección válida; las
imágenes grandes pueden redimensionarse manteniendo proporciones según el texto visible.

## Resultado revisado en fuente

La fuente muestra una vista previa, envía el archivo seleccionado y actualiza o limpia
esa vista tras una respuesta exitosa. No confirma la publicación del logo en documentos,
impresiones o integraciones externas.

## Advertencias y casos límite

No elimine un logo por una vista previa incierta. Conserve una copia autorizada del
archivo fuera de esta guía y no cargue archivos distintos de una imagen PNG.

## Problemas frecuentes y condiciones de detención

- Formato o dimensiones rechazados: corrija el archivo antes de volver a seleccionarlo.
- No se actualiza la vista previa: no repita la carga; confirme el resultado con soporte autorizado.
- No aparece la opción: no suponga que la sesión tiene permiso para cambiarla.

## Verificaciones pendientes en runtime

- Tamaño final, redimensionamiento y almacenamiento de la imagen.
- Permisos, mensajes y efecto de eliminar el logo.
- Lugares donde el logo actualizado se muestra en el entorno desplegado.

## Enlaces relacionados

- [Revisar parámetros generales](revisar-parametros-generales.md)
- [Configuración](index.md)
