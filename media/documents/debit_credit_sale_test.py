# -*- coding: utf-8 -*-

from src.funtions.functions import Functions
import unittest
import pytest
import allure
import time


class DebitCreditSale(Functions, unittest.TestCase):
    def setUp(self):
        print("¡¡¡DebitCreditSale - setUp!!!")
        Functions.set_up(self)
        Functions.set_wifi(self)
        Functions.main_activity(self)

    # Metodo para realizar una venta cuota
    def test_instalment_sale(self):
        print("¡¡¡DebitCreditSale - test_instalment_sale!!!")
        # Carga el archivo JSON para la pantalla principal de ventas
        Functions.json_file(self, 'main_sales_page')
        # Espera la disponibilidad del elemento
        Functions.wait_json_element(self, 'Amount')

        # Carga el archivo JSON para el teclado
        Functions.json_file(self, 'keyboard_page')
        # Ingresa el monto
        Functions.find_json_element(self, '5').click()
        Functions.find_json_element(self, '000').click()
        print("¡¡¡INGRESO DE MONTO EXITOSO!!!")
        Functions.find_json_element(self, 'Ok').click()
        print("¡¡¡ENVIO DE MONTO EXITOSO!!!")
        # Tiempo de espera explicito para el proximo comando
        time.sleep(3)

        # Carga el archivo JSON para la pantalla tipo de venta
        Functions.json_file(self, 'sale_type_page')
        # Espera la disponibilidad del elemento
        Functions.wait_json_element(self, 'Debit/Credit Sale')
        # Selecciona el tipo de venta
        Functions.find_json_element(self, 'Debit/Credit Sale').click()
        # Tiempo de espera explicito para el proximo comando
        time.sleep(3)

        # Carga el archivo JSON para la pantalla tipo de tarjeta extranjera
        Functions.json_file(self, 'debit_credit_page')
        # Espera la disponibilidad del elemento
        Functions.wait_json_element(self, 'Sale Name')
        # Selecciona el tipo de tarjeta extranjera
        Functions.find_json_element(self, 'Credit').click()

        print("¡¡¡ACERQUE/DESLICE/INSERTE LA TARJETA!!!")
        # Tiempo de espera explicito para el proximo comando
        time.sleep(15)

    '''
    def tearDown(self):
        print("¡¡¡InicializarTest - tearDown!!!")
        Functions.tear_down(self)
    '''


if __name__ == '__main__':
    unittest.main()
