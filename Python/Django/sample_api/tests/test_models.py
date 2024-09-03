# from django.test import TestCase
# from sample_app.models import Students
# from django.core.exceptions import ValidationError

# class StudentsModelTest(TestCase):

#     def setUp(self):
#         self.student = Students.objects.create(
#             first_name="John",
#             last_name="Doe",
#             address="123 Main St",
#             roll_number=101,
#             mobile="1234567890"
#         )

#     # def test_student_creation(self):
#     #     student = self.student  # Accessing the student created in setUp
#     #     self.assertEqual(student.first_name, "John")
#     #     self.assertEqual(student.last_name, "Doe")
#     #     self.assertEqual(student.address, "123 Main St")
#     #     self.assertEqual(student.roll_number, 101)
#     #     self.assertEqual(student.mobile, "1234567890")

#     # def test_student_str_method(self):
#     #     student = self.student  # Accessing the student created in setUp
#     #     self.assertEqual(str(student), "John Doe")

#     # def test_student_roll_number_unique(self):
#     #     with self.assertRaises(Exception):
#     #         Students.objects.create(
#     #             first_name="Jane",
#     #             last_name="Doe",
#     #             address="456 Elm St",
#     #             roll_number= 101,
#     #             mobile="0987654321"
#     #         )
            
#     # def test_first_name_max_length(self):
#     #     student = self.student
#     #     max_length = student._meta.get_field('first_name').max_length
#     #     self.assertEqual(max_length, 5)
        
#     def test_first_name_exceeds_max_length(self):
#         student = Students(
#             first_name='J' * 201,
#             last_name='Doe',
#             address='123 Main St',
#             roll_number=102,
#             mobile='1234567890'
#         )
#         with self.assertRaises(ValidationError):
#             student.full_clean()