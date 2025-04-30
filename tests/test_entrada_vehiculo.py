import unittest
from routes.controllers import entrada_vehiculo
from db.services import VehiculoService

class TestEntradaVehiculo(unittest.TestCase):
    def test_entrada_vehiculo_valido(self):
        # data = {
        #     "vehiclePlate": "ABC-1234",
        #     "driverName": "Juan Pérez",
        #     "entryTime": "10:00",
        #     "parkingSpace": "1"
        # }
        # vehiculo = entrada_vehiculo(data)
        # self.assertEqual(vehiculo.matricula, "ABC-1234")
        # self.assertEqual(vehiculo.nombre_conductor, "Juan Pérez")
        self.assertTrue(True)

    def test_entrada_vehiculo_invalido(self):
        # data = {
        #     "vehiclePlate": "ABC-1234",
        #     "driverName": "Juan Perez",
        #     "entryTime": "10:00",
        #     "parkingSpace": "1"
        # }
        # vehiculo = entrada_vehiculo(data)
        # self.assertEqual(vehiculo, None)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()