from django.test import TestCase


class TEST1(TestCase):
    def test_1_HP_TENDER_MX(self):
        self.assertFalse(True)

    def test_1_HP_TENDER_CL(self):
        self.assertFalse(True)

    def test_1_HP_TENDER_PE(self):
        self.assertFalse(True)

    def test_1_UP_NULL(self):
        self.assertFalse(True)

    def test_1_UP_NOT_SUPPORTED(self):
        self.assertFalse(True)

    def test_1_UP_WRONG_DATATYPE(self):
        self.assertFalse(True)


class TEST2(TestCase):
    def test_2_HP_LOWER_5000USD(self):
        self.assertFalse(True)

    def test_2_HP_OK_DATE(self):
        self.assertFalse(True)

    def test_2_UP_LOWER_0USD(self):
        self.assertFalse(True)

    def test_2_UP_NOTSUPPORTED_CURRENCY(self):
        self.assertFalse(True)

    def test_2_UP_OK_DATE(self):
        self.assertFalse(True)


class TEST3(TestCase):
    def test_3_HP_LOCATION_SINALOA(self):
        self.assertFalse(True)

    def test_3_HP_CONSTRUCTION(self):
        self.assertFalse(True)

    def test_3_HP_PHARM_TACNA(self):
        self.assertFalse(True)

    def test_3_UP_NOTSUPPORTED_LOCATION(self):
        self.assertFalse(True)


class TEST4(TestCase):
    def test_4_HP_NATIONALITY_CL(self):
        self.assertFalse(True)

    def test_4_HP_EXPERIENCE(self):
        self.assertFalse(True)

    def test_4_HP_EXPERIENCE_NEGATIVE(self):
        self.assertFalse(True)

    def test_4_UP_NOTSUPPORTED_COUNTRY(self):
        self.assertFalse(True)


class TEST5(TestCase):
    def test_5_HP_CHANGE_STATE(self):
        self.assertFalse(True)

    def test_5_HP_MULTIPLE_CHANGE_STATE(self):
        self.assertFalse(True)

    def test_5_UP_NOTSUPPORTED_STATE(self):
        self.assertFalse(True)


class TEST6(TestCase):
    def test_6_HP_CHANGE_ROL(self):
        self.assertFalse(True)

    def test_6_UP_NOTSUPPORTED_CHAGE_ROL(self):
        self.assertFalse(True)


class TEST7(TestCase):
    def test_7_HP_ASSIGN_EXECUTIVE(self):
        self.assertFalse(True)

    def test_7_HP_CHANGE_EXECUTIVE(self):
        self.assertFalse(True)

    def test_7_UP_NOTSUPPORTED_ASSIGN_EXECUTIVE(self):
        self.assertFalse(True)

    def test_7_UP_NOTSUPPORTED_ASSIGN_TENDER(self):
        self.assertFalse(True)


class TEST8(TestCase):
    def test_8_HP_SANCTIONED_CL(self):
        self.assertFalse(True)

    def test_8_HP_SANCTIONED_MX(self):
        self.assertFalse(True)

    def test_8_HP_SANCTIONED_PE(self):
        self.assertFalse(True)

    def test_8_UP_BADFORMAT_DNI(self):
        self.assertFalse(True)


class TEST9(TestCase):
    def test_9_HP_CONTACT_DETAILS_CL(self):
        self.assertFalse(True)

    def test_9_HP_CONTACT_DETAILS_PE(self):
        self.assertFalse(True)

    def test_9_HP_CONTACT_DETAILS_MX(self):
        self.assertFalse(True)


class TEST9(TestCase):
    def test_10_HP_ATTRACTIVE(self):
        self.assertFalse(True)

    def test_10_HP_NO_ATTRACTIVE(self):
        self.assertFalse(True)

    def test_10_UP_NON_EXISTENT(self):
        self.assertFalse(True)
