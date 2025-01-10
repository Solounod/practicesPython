
dates = {
  "proyecto": "Techo de zinc de dos aguas",
  "dimensiones": {
    "largo": 2,
    "ancho": 3,
    "superficie_total": 12
  },
  "plancha_zinc": {
    "tamaño": "2 mt",
    "cantidad": 6
  },
  "materiales": {
    "clavos": {
      "cantidad": 500,
      "precio_unitario": 2000,
      "total": 2000
    },
    "zinc": {
      "precio_unitario": 10000,
      "total": 60000
    },
    "fieltro": {
      "cantidad": 1,
      "precio_unitario": 15000,
      "total": 15000
    }
  },
  "total_proyecto": 77000
}

dimention = dates["dimensiones"]
planche = dates["plancha_zinc"]
planche_dimentions = planche["tamaño"]
planche_quantity = planche["cantidad"]
total_zinc = dates["materiales"]["zinc"]["total"]
materials_clavos = dates["materiales"]["clavos"]
total_clavos = materials_clavos["total"]

print(total_zinc, total_clavos)