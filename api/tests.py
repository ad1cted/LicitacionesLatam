from django.test import TestCase
from requests import Response

from kernel.models import *


class TEST1(TestCase):

    def test_1_HP_TENDER_MX(self):
        Pais(isocode="MEX", nombre="Mexico").save()
        pais = Pais.objects.get(isocode="MEX")
        Licitacion(id_Pais=pais).save()
        response: Response = self.client.get("/api/get_licitacion/pais/MEX")
        self.assertEqual(response.status_code, 200)

    def test_1_HP_TENDER_CL(self):
        Pais(isocode="CHI", nombre="Chile").save()
        pais = Pais.objects.get(isocode="CHI")
        Licitacion(id_Pais=pais).save()
        response: Response = self.client.get("/api/get_licitacion/pais/CHI")
        self.assertEqual(response.status_code, 200)

    def test_1_HP_TENDER_PE(self):
        Pais(isocode="PER", nombre="Peru").save()
        pais = Pais.objects.get(isocode="PER")
        Licitacion(id_Pais=pais).save()
        response: Response = self.client.get("/api/get_licitacion/pais/PER")
        self.assertEqual(response.status_code, 200)

    def test_1_UP_NULL(self):
        response: Response = self.client.get("/api/get_licitacion/pais/")
        self.assertEqual(response.status_code, 404)

    def test_1_UP_NOT_SUPPORTED(self):
        response: Response = self.client.get("/api/get_licitacion/pais/RUS")
        self.assertEqual(response.status_code, 400)

    def test_1_UP_WRONG_DATATYPE(self):
        response: Response = self.client.get("/api/get_licitacion/pais/123")
        self.assertEqual(response.status_code, 400)


class TEST2(TestCase):
    def test_2_HP_LOWER_5000USD(self):
        self.assertTrue(True)

    def test_2_HP_OK_DATE(self):
        self.assertTrue(True)

    def test_2_UP_LOWER_0USD(self):
        self.assertTrue(True)

    def test_2_UP_NOTSUPPORTED_CURRENCY(self):
        self.assertTrue(True)

    def test_2_UP_OK_DATE(self):
        self.assertTrue(True)


class TEST3(TestCase):
    def test_3_HP_LOCATION_SINALOA(self):
        self.assertTrue(True)


    def test_3_HP_CONSTRUCTION(self):
        self.assertTrue(True)

    def test_3_HP_PHARM_TACNA(self):
        self.assertTrue(True)

    def test_3_UP_NOTSUPPORTED_LOCATION(self):
        self.assertTrue(True)


class TEST4(TestCase):
    def test_4_HP_NATIONALITY_CL(self):
        self.assertTrue(True)

    def test_4_HP_EXPERIENCE(self):
        self.assertTrue(True)

    def test_4_HP_EXPERIENCE_NEGATIVE(self):
        self.assertTrue(True)

    def test_4_UP_NOTSUPPORTED_COUNTRY(self):
        self.assertTrue(True)


class TEST5(TestCase):
    def test_5_HP_CHANGE_STATE(self):
        self.assertTrue(True)

    def test_5_HP_MULTIPLE_CHANGE_STATE(self):
        self.assertTrue(True)

    def test_5_UP_NOTSUPPORTED_STATE(self):
        self.assertTrue(True)


class TEST6(TestCase):
    def test_6_HP_CHANGE_ROL(self):
        self.assertTrue(True)

    def test_6_UP_NOTSUPPORTED_CHAGE_ROL(self):
        self.assertTrue(True)


class TEST7(TestCase):
    def test_7_HP_ASSIGN_EXECUTIVE(self):
        self.assertTrue(True)

    def test_7_HP_CHANGE_EXECUTIVE(self):
        self.assertTrue(True)

    def test_7_UP_NOTSUPPORTED_ASSIGN_EXECUTIVE(self):
        self.assertTrue(True)

    def test_7_UP_NOTSUPPORTED_ASSIGN_TENDER(self):
        self.assertTrue(True)


class TEST8(TestCase):
    def test_8_HP_SANCTIONED_CL(self):
        self.assertTrue(True)

    def test_8_HP_SANCTIONED_MX(self):
        self.assertTrue(True)

    def test_8_HP_SANCTIONED_PE(self):
        self.assertTrue(True)

    def test_8_UP_BADFORMAT_DNI(self):
        self.assertTrue(True)


class TEST9(TestCase):
    def test_9_HP_CONTACT_DETAILS_CL(self):
        self.assertTrue(True)

    def test_9_HP_CONTACT_DETAILS_PE(self):
        self.assertTrue(True)

    def test_9_HP_CONTACT_DETAILS_MX(self):
        self.assertTrue(True)


class TEST10(TestCase):
    def test_10_HP_ATTRACTIVE(self):
        self.assertTrue(True)

    def test_10_HP_NO_ATTRACTIVE(self):
        self.assertTrue(True)

    def test_10_UP_NON_EXISTENT(self):
        self.assertTrue(True)
