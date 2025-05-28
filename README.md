Proyecto final de Modelamiento.

Busca resolver problemas de ingeniería, de manera específica, mecánica de fracturas, mediante métodos numéricos como puede ser el método de punto fijo.

K = σ * sqrt(pi*a) * f(a/W)
Se hace uso de la función geométrica de corrección para una probeta tipo SENB (Single Edge Notched Beam), donde f(x) = 1 / cos(pi*x/2) * 1.99 - x(1-x)(2.15 - 3.93x + 2.7x^2), siendo W el ancho de la probeta.

Single Edge Notched Beam - Viga con muesca en un solo borde
Es un tipo de probeta estandarizada usada en ensayos de mecánica de fracturas para medir la tenacidad a la fractura (K) de un material.
El ensayo SENB se usa para simular la propagación de una grieta en un material sometido a flexión, y calcular el valor crítico de 𝐾 (tenacidad).
Sirve para estudiar fallas frágiles en estructuras, especialmente: metales, cerámicos, compuestos.

+----------------------------+
|                            |
|                            |  <- Material
|             a              |  <- Grieta (muesca)
|         |------->          |
+----------------------------+
          ↑
        muesca

Tiene:
Longitud total: L
Ancho: W
Una grieta artificial (a) en uno de los bordes
Se carga con una fuerza en flexión hasta que se propaga la grieta.

La fórmula del factor de intensidad de esfuerzos (K) para SENB:
K = σ * sqrt(pi*a) * f(a/W)
Donde:
σ: esfuerzo aplicado
a: longitud de grieta
W: ancho de la probeta
f(a/W): función de corrección geométrica, porque el borde afecta cómo se propaga la grieta

La fórmula no se puede despejar directamente porque f(a/W) depende de a, así que usamos el método de punto fijo para resolverla numéricamente.

Desarollado en 2025.
