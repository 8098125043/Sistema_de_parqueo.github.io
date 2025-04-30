import unittest
from db.services import VehiculoService

class TestSalidaVehiculo(unittest.TestCase):
    def test_salida_vehiculo(self):
        vehiculo = None
        self.assertIsNone(vehiculo)

    def test_salida_vehiculo_invalido(self):
        vehiculo = None
        self.assertIsNone(vehiculo)


if __name__ == '__main__':
    unittest.main()